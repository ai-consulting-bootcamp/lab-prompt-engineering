# Lab Proof – Prompt Engineering Lab (TechFlow Solutions)

**Model:** `gpt-4o-mini`, temperature 0.7 for all versions (only the prompt changes).

## Code & evidence
- [`prompt_engineering_lab.ipynb`](./prompt_engineering_lab.ipynb) – full workflow: helpers (`run_multiple` = same prompt n times in parallel), v1 → v2 → v3 prompts, 5/10/15-run tests, failure analysis, variations, final evaluation
- [`results/`](./results/) – raw responses of every run (`v1_runs.json` … `final_runs.json`, `variations_runs.json`) and [`final_comparison.csv`](./results/final_comparison.csv)

## Results (format adherence, 15 runs)

| Task | v1 | v2 | v3 | Final | Technique that made the difference |
|---|---|---|---|---|---|
| Sentiment | 0 % | 100 % | 100 % | **100 %** | fixed labels (v2); few-shot + rule for mixed messages (v3) |
| Product description | 0 % | 40 % | 100 % | **100 %** | few-shot + "exactly 5 sentences" instead of a word count |
| Data extraction | 0 % | 100 % | 13 % | **100 %** | JSON schema (v2); CoT + typed template (v3.1) |

All final prompts: **100 % consistency** (target >80 %). v1 was *consistently wrong*: full sentences instead of labels, ~300-word texts with invented specs, bullet lists instead of JSON. More runs revealed more variants (sentiment labels 3 → 6 from 5 to 15 runs). On new, harder inputs (Step 12), few-shot raised sentiment accuracy from 87.5 % to 100 %.

## One run: input → evidence → output
Final extraction prompt (v3.1), input:
`I ordered item #12345 on March 15th. The delivery was fast but the packaging was damaged.`

Evidence (CoT reasoning, from `results/final_runs.json`):
```
1. Order ID: The feedback mentions "item #12345", so the Order ID is "12345" after removing the "#".
2. Order date: ... clearly stated as "March 15th".
3. Delivery speed: ... "the delivery was fast", indicating a delivery speed of "fast".
4. Packaging condition: ... "the packaging was damaged", so the packaging condition is "damaged".
```
Output (identical structure in 15/15 runs):
```json
{"order_id": "12345", "order_date": "March 15th", "delivery_speed": "fast", "packaging_condition": "damaged"}
```

## Failure I hit
Adding Chain-of-Thought (v3) caused a **hidden type regression**: in 13/15 runs `order_id` became the number `12345` instead of the string `"12345"`. My first check converted values with `str()`, so it still showed 100 %. A stricter type check exposed it (13 %), and a typed output template (v3.1) fixed it (100 %). Lesson: a metric is only as good as what it checks. CoT also added no accuracy on the variations but ~6× more output, so v2 would be the cheaper choice for this simple extraction.

**Remaining limitation:** for an "ergonomic office chair" the model still invents category-typical features ("adjustable", posture claims) despite an "only given facts" rule. This needs richer product data or an LLM-as-judge check, not more prompt rules.
