# Prompt Engineering Lab Proof (`v1` → `v3`)

**Evidence source:** [prompt_engineering_lab.ipynb](./prompt_engineering_lab.ipynb). This review uses only the notebook's saved source and recorded outputs; no cells were re-run and no live API calls were made.

## Environment & Execution Setup
- **Notebook:** `prompt_engineering_lab.ipynb` executed via Anaconda kernel in VS Code.
- **Model:** `gpt-5-mini` via shared `call_openai` helper with retry/rate-limit handling and `run_multiple_fast` batch runner.
- **Evaluation Dimensions:** Output uniqueness (variance), JSON parseability and exact key conformance, length and factual grounding constraints, and latency/stability across 5-, 10-, and 15-run batches.
- **Inputs:** The wireless-mouse prompt and the feedback `I ordered item #12345 on March 15th. The delivery was fast but the packaging was damaged.` are synthetic test inputs, not real customer records.
- **Coverage:** Saved results are not a complete 5/10/15 matrix for every prompt version: v1 has 5- and 10-run tests, v2 has 10-run tests, and v3 has 15-run tests. Missing combinations are not inferred.

## Empirical Results by Version

### 1. Sentiment Classification
- **`v1` (5 & 10 runs):** `5/5` and `10/10` unique outputs. Only 1 of 10 runs returned bare `Positive`; others added prefixes (`Label:`, `Sentiment:`), modifiers (`strongly positive`), or full explanations/suggested replies.
- **`v2` (10 runs):** Added strict single-word output constraint (`positive`, `negative`, `neutral`) with no punctuation or commentary. Achieved `1/10` unique outputs and `10/10` exact `'positive'` matches.
- **`v3` (15 runs):** Added few-shot classification examples alongside strict single-word rules. Achieved `1/15` unique outputs and `15/15` exact `'positive'` matches.

### 2. Product Description Generation
- **`v1` (5 & 10 runs):** `5/5` and `10/10` unique outputs with wide length spread (`1,165–1,733` characters) and ungrounded brand/model names (`NovaWave Wireless Mouse`, `GlidePro`, `SmoothClick Pro`, `SmoothGlide`, `Wireless Comfort Mouse`).
- **`v2` (10 runs):** Enforced single paragraph, `80–120` word target, exact `$29.99` price inclusion, and no invented brand names or hardware specs. Achieved `10/10` `$29.99` inclusion and `79–95` words (1 run at `79` words, 1 word under the lower bound).
- **`v3` (15 runs):** Tightened target window to `85–115` words while preserving anti-hallucination and price rules. Achieved `15/15` word-count compliance (`90–100` words) and `15/15` `$29.99` price compliance (`15/15` unique prose variations).

### 3. Structured Data Extraction
- **`v1` (10 runs):** `10/10` unique outputs and only `5/10` valid JSON. Failures included prose prefaces (`"Here’s the information extracted..."`) and key drift (`order_id` vs. `item_number`, `packaging_condition` vs. `packaging`).
- **`v2` (10 runs):** Enforced raw JSON only (no fences/prose) and fixed schema keys (`order_id`, `order_date`, `delivery_status`, `packaging_status`, `sentiment`). Improved to `10/10` valid JSON and `10/10` exact schema matches (`4/10` unique outputs).
- **`v3` (15 runs):** Added a concrete few-shot JSON example and strict schema instructions. Achieved `15/15` valid JSON and `15/15` exact schema matches across `5/15` unique output strings (`order_date` varied between `"March 15th"` [12/15] and `"March 15"` [3/15]; `sentiment` was `"mixed"` [13/15] vs. `"negative"` [2/15]).

## Key Takeaways
1. **Explicit output contracts + schema locks eliminate structural drift:** Moving from zero-shot (`v1`) to strict formatting and exact keys (`v2`–`v3`) raised JSON validity from `50%` (`5/10`) to `100%` (`15/15`).
2. **Few-shot examples help, but examples can bias edge labels:** Adding an example reinforced formatting, while minor value variation (`"March 15th"` vs. `"March 15"`, `"mixed"` vs. `"negative"`) showed where post-processing or stricter label rules help.
3. **Sequential-call latency matters in practice:** The notebook executes repeated calls sequentially and inserts sleeps/retries, so 15–30 calls take noticeable wall-clock time. No elapsed-time measurements were saved, so this is a qualitative limitation rather than a quantified latency result.

## Audit Notes and Follow-up

- The saved metrics above match the recorded notebook outputs. Extraction v3 is structurally stable (`15/15` valid JSON and exact schema) but still has value-level variation: `March 15th` vs. `March 15`, and `mixed` vs. `negative`.
- Product v2's one `79`-word response is a real boundary failure against its `80–120` target; Product v3 removes that observed failure in the saved 15-run sample.
- The notebook contains a duplicated saved v2 sentiment test cell with the same recorded `1/10` and `10/10` results. It does not change the reported evidence, but it should be removed or clearly labeled during a future notebook cleanup.
- The product evaluators measure whitespace-delimited word count and literal `$29.99` presence only. They do not programmatically verify the single-paragraph requirement, absence of invented brands/specifications, or factual grounding; those remain prompt-level claims and manual-review follow-ups.
- The extraction evaluators measure JSON parseability and exact top-level key sets only. They do not validate field types, allowed values, date normalization, or whether the extracted values faithfully represent the feedback.
- `run_multiple_fast` performs calls sequentially and passes a fixed sleep to `call_openai`; there is no concurrency or elapsed-time capture. `call_openai` retries rate-limit and generic API errors, but does not explicitly catch timeout, connection, or other client-side transient exceptions.
- Follow-up guardrails should normalize date representation, define the desired aggregate sentiment policy for mixed feedback, and validate product word count/price/schema after generation. These are recommendations, not additional measured results.

## Bonus Challenges

### Challenge 1 — Temperature / Reasoning Experimentation

- The custom-temperature probe was rejected by `gpt-5-mini` with the saved HTTP 400 error: `Unsupported parameter: 'temperature' is not supported with this model.` The notebook therefore tested `reasoning_effort` instead, with three runs per setting.
- `minimal`: `3/3` format passes and `3/3` content passes; `3/3` unique outputs and a recorded consistency ratio of `0.0`. The saved previews show `order_date` as `March 15` twice and as `2023-03-15` once, inventing a year absent from the input.
- `low`: `3/3` format passes and `3/3` content passes; `2/3` unique outputs and consistency ratio `0.333`. Dates varied between `March 15th` once and `March 15` twice.
- `medium`: `3/3` format passes and `3/3` content passes; `2/3` unique outputs and consistency ratio `0.333`. Dates were `March 15` twice and `March 15th` once.
- These are evaluator pass rates, not semantic-accuracy rates: the extraction evaluator checks that the result is a JSON object with the required keys, but does not verify date correctness, field values, or normalization.

### Challenge 2 — Automatic Prompt Improvement

- The workflow supplied a baseline extraction prompt and explicit failure notes to a meta-prompt, asked the model to return only an improved prompt, then ran the generated `v_meta` prompt three times and scored the outputs with `evaluate_batch`.
- The generated prompt requires raw JSON only, exactly five keys in a fixed order, exact order-ID/date substrings without normalization or invented years, `null` for missing or ambiguous values, controlled delivery/packaging/sentiment enums, and standard JSON strings with no extra metadata.
- Saved `v_meta` results: `3/3` format passes, `3/3` content passes, `1/3` unique output, and consistency ratio `0.667`. As above, content means exact-key conformance rather than complete value validation.

### Challenge 3 — Multi-Task Prompt

- One shared prompt routes by task name across sentiment, product description, and data extraction, with global anti-invention rules plus task-specific output requirements. The notebook ran two repeats per task.
- Sentiment: `1/2` unique outputs, consistency ratio `0.5`, format pass rate `1.0`, content pass rate `1.0`.
- Product description: `2/2` unique outputs, consistency ratio `0.0`, format pass rate `1.0`, content pass rate `1.0`.
- Data extraction: `2/2` unique outputs, consistency ratio `0.0`, format pass rate `1.0`, content pass rate `1.0`. The saved previews show an order-ID variation (`#12345` versus `12345`) despite both outputs passing the evaluator.
- These scores use two-run synthetic samples and should not be treated as broad reliability estimates. Product content is scored only by literal price presence, and extraction content by exact keys.

### Challenge 4 — Evaluation Framework

- `evaluate_batch` counts total and unique raw output strings, records per-run details, and returns format-pass rate, content-pass rate, and a consistency ratio calculated as `1 - unique_outputs / total_runs`.
- For data extraction, format requires a parseable JSON object and content requires the exact expected key set. For product descriptions, format requires a regex word count within the configured range and no blank-line paragraph split; content requires the literal required price. For sentiment, format requires one cleaned token and content requires membership in the allowed sentiment set.
- Remaining caveats: the consistency formula gives identical two-run outputs a score of `0.5`, not `1.0`; raw whitespace or formatting changes count as unique outputs; the product regex word count can differ from the earlier whitespace-based metric; and no task checks semantic truth, field types, date normalization, or unsupported claims. Empty batches are handled as zero rates, while non-string and malformed outputs fail the relevant checks.
