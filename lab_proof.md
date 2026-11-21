# Prompt Engineering Lab — Lab Proof

## Reviewer Entry Point

This submission demonstrates systematic prompt improvement for three customer-service chatbot tasks:

1. Sentiment analysis
2. Product description generation
3. Structured data extraction from customer feedback

The working notebook is:

- [Prompt Engineering Lab notebook](prompt_engineering_lab.ipynb)

The submission notebook is `prompt_engineering_lab.ipynb`.

## Objective

The objective is to diagnose inconsistent prompt behaviour and improve reliability through repeated testing, clearer constraints, structured output requirements, few-shot examples, and reasoning techniques where appropriate.

## Environment and Setup

The notebook uses Python, Jupyter, the OpenAI Python library, and a local API key loaded from `.env`. The API key is not included in this repository.

To run the notebook:

```bash
pip install openai python-dotenv jupyter
jupyter notebook prompt_engineering_labbackup.ipynb
```

## Tasks and Prompt Versions

### Task 1: Sentiment Analysis

The prompt classifies customer messages as Positive, Negative, or Neutral. Version 2 adds explicit allowed labels and requires exactly one label without additional explanation.

### Task 2: Product Description Generation

The prompt creates a short description from verified product information. Version 2 prohibits invented specifications, features, and benefits.

### Task 3: Data Extraction

The prompt extracts information from customer feedback. Version 2 requires a JSON object with fixed fields: `item_number`, `order_date`, `delivery`, and `packaging`.

## Testing Completed Through Part 3

The notebook contains:

- Initial Version 1 prompts for all three tasks
- Single-run outputs for all three tasks
- Five-run testing for all three Version 1 prompts
- Ten-run testing for all three Version 1 prompts
- Fifteen-run testing for all three Version 1 prompts
- Failure analysis for the Version 1 prompts
- Version 2 prompts for all three tasks
- Fifteen-run Version 2 tests for all three tasks
- Version 2 automated compliance analysis for all three tasks

## Evidence Produced

The saved notebook shows the following Version 1 findings:

- Sentiment classification was correct, but the model did not reliably return one exact label.
- Product descriptions included unsupported product claims in the baseline prompt.
- Data extraction identified the relevant facts but varied in field names and formatting and did not return standardized JSON.

The notebook also records Version 2 results for sentiment and product description:

- Sentiment Version 1: `0/15` exact-label compliance
- Sentiment Version 2: `15/15` compliance, `100%`
- Product Version 1: `0/15` compliance under the unsupported-claim checker
- Product Version 2: `15/15` compliance under the same checker, `100%`
- Data extraction Version 1: `0/15` JSON compliance
- Data extraction Version 2: `15/15` compliance, `100%`

## Current Results

| Task | Version 1 | Version 2 | Current status |
|---|---:|---:|---|
| Sentiment analysis | 0/15 (0%) | 15/15 (100%) | Version 2 target met |
| Product description generation | 0/15 (0%) | 15/15 (100%) | Version 2 target met |
| Data extraction | 0/15 (0%) | 15/15 (100%) | Version 2 target met |

The lab target is more than 80% consistency across 15 runs. All three Version 2 prompts met this target. The final Version 3 results are reported below.

## Failure Analysis

The baseline prompts showed these failure patterns:

- Inconsistent sentiment labels and extra explanations
- Unsupported product specifications and benefits
- Varying extraction field names and output structures
- No reliable machine-readable JSON output for the baseline extraction prompt

The Version 2 prompts address these issues by adding explicit labels, verified-input constraints, fixed field names, and JSON-only output requirements.

## Completion Status

The notebook includes the required Version 3 prompts, fifteen-run tests, task variations, final comparison, and lessons learned. All three final prompts exceeded the lab target of more than 80% consistency across 15 runs.

## Step 9 — Few-Shot Sentiment Analysis (V3)

**Objective:** Evaluate whether providing labeled examples improves sentiment classification consistency.

**Method:** Added three examples representing Positive, Negative, and Neutral sentiment, while retaining the single-label output requirement.

**Testing:** Ran the V3 prompt 15 times using the same customer message and evaluation rules.

**Results:**

- V1 compliance: 0/15 (0%)
- V2 compliance: 15/15 (100%)
- V3 compliance: 15/15 (100%)

**Conclusion:** Few-shot prompting maintained 100% compliance but showed no measurable improvement over V2 on this test. Further testing with ambiguous or mixed-sentiment messages would be needed to determine whether the examples improve classification accuracy.

## Step 10 — Chain-of-Thought Data Extraction (V3)

**Objective:** Evaluate whether step-by-step reasoning instructions improve structured data extraction.

**Method:** Added five reasoning steps to identify and verify the required information before generating the final JSON response.

**Testing:** Ran the V3 prompt 15 times using the same customer feedback and evaluation criteria as V2.

**Results:**

- V1 compliance: 0/15 (0%)
- V2 compliance: 15/15 (100%)
- V3 compliance: 15/15 (100%)

**Conclusion:** V3 achieved 100% compliance, matching V2. The additional reasoning instructions did not produce a measurable improvement for this simple extraction task. More complex customer feedback would be needed to assess whether step-by-step prompting provides additional value.

## Step 11 — Few-Shot Product Description (V3)

**Objective:** Test whether examples and structured JSON output improve product description reliability.

**Method:** Provided two examples and required a JSON response containing `product`, `price`, and `description`.

**Results:**

- V1 automated compliance: 0/15 (0%)
- V2 automated compliance: 15/15 (100%)
- V3 automated compliance: 13/15 (86.7%)

**Failure analysis:** Runs 6 and 11 included Markdown code fences around otherwise correct JSON objects. These responses failed the strict JSON-only requirement.

**Conclusion:** V3 produced correctly structured product information in all 15 responses, but only 13 followed the required JSON-only format. Few-shot prompting did not eliminate formatting inconsistencies.

**Limitation:** V2 and V3 have different output requirements, so their compliance rates are not directly equivalent. The automated product checker also cannot detect every unsupported claim.

## Step 12A — Sentiment Prompt Variations

**Objective:** Evaluate whether the V3 few-shot sentiment prompt works with different customer messages.

**Method:** Tested four messages: positive, negative, neutral, and mixed sentiment.

**Results:**

- Positive message: Correct
- Negative message: Correct
- Neutral message: Correct
- Mixed message: Classified as Negative, which is reasonable because the product stopped working despite fast delivery.

**Accuracy:** 3/3 (100%) on clearly labeled examples. The mixed-sentiment example was evaluated separately because its expected classification was not predefined.

**Conclusion:** The V3 prompt correctly classified all three clearly labeled examples and produced a defensible classification for the mixed-sentiment message. Further testing is needed to establish reliability on ambiguous feedback.

## Step 12B — Product Description Variations (V3)

**Objective:** Test whether the V3 few-shot product description prompt generalizes to different products and prices.

**Test cases:**

- Water bottle — $14.99
- Backpack — $39.99
- Coffee mug — $12.99

**Results:** All 3 responses returned valid JSON with the correct product, price, and description fields. No unsupported product features were introduced.

**Compliance:** 3/3 (100%).

**Conclusion:** The V3 prompt successfully handled all three product variations while maintaining the required JSON structure and factual constraints. A minor capitalization inconsistency was observed.

## Step 12C — Data Extraction Variations (V3)

**Objective:** Test whether the V3 structured-reasoning extraction prompt works with different customer feedback messages.

**Tests:** Three customer messages with different item numbers, order dates, delivery conditions, and packaging conditions.

**Results:**

- All 3 responses extracted the correct information.
- All 3 returned valid JSON with exactly the four required fields.
- No incorrect or invented values were observed.

**Compliance:** 3/3 (100%).

**Conclusion:** The V3 extraction prompt successfully generalized to all three tested variations while maintaining consistent JSON formatting and accurate information extraction.

## Step 13 — Final Comparison

| Task | V1: Basic prompt | V2: Clear constraints | V3: Advanced techniques |
|---|---:|---:|---:|
| Sentiment analysis | 0/15 (0%) | 15/15 (100%) | 15/15 (100%) |
| Product description | 0/15 (0%) | 15/15 (100%) | 13/15 (86.7%) |
| Data extraction | 0/15 (0%) | 15/15 (100%) | 15/15 (100%) |

All three final prompts exceeded the required 80% consistency target.

## Final Findings and Lessons Learned

**1. Which prompt engineering technique worked best?**

Clear instructions, explicit constraints, and defined output formats (V2) produced the strongest results in this experiment. All three V2 prompts achieved 100% compliance with their respective automated checks.

**2. Did few-shot prompting improve performance?**

Few-shot prompting (V3) maintained 100% compliance for sentiment classification and data extraction but did not demonstrate a measurable improvement over V2.

For product descriptions, V3 achieved 86.7% strict JSON compliance because two responses included Markdown code fences.

**3. What did the variations reveal?**

- Sentiment classification: 3/3 clear examples were correctly classified. One mixed-sentiment example was classified as Negative.
- Product descriptions: 3/3 variations produced compliant descriptions.
- Data extraction: 3/3 variations returned accurate information in valid JSON.

**4. What are the limitations?**

- Each original prompt was tested 15 times with the same input.
- Automated checks did not detect every possible factual error.
- V2 and V3 product descriptions had different formatting requirements, limiting direct comparison.
- Additional tests with more diverse inputs would be necessary to establish broader reliability.

**5. What did I learn?**

Prompt engineering is not simply about writing longer prompts. Clearly defining the task, acceptable outputs, and constraints can improve consistency. Few-shot examples and structured reasoning can be useful, but their effectiveness should be evaluated against simpler alternatives.

## Failure or Limitation

Language-model responses can vary between runs. Consistency is therefore measured against task-specific output and content requirements rather than exact word-for-word equality. The product checker is keyword-based and cannot detect every possible unsupported claim, so manual review remains necessary.

## Submission Checklist

- [x] All three tasks are implemented.
- [x] Version 1 and Version 2 prompts are included.
- [x] Version 1 prompts are tested 5, 10, and 15 times.
- [x] Responses are recorded as evidence.
- [x] Failure patterns are explained.
- [x] The saved notebook contains no error outputs.
- [x] Version 2 data-extraction results are verified cleanly.
- [x] Version 3 prompts are included.
- [x] Version 3 prompts are tested 15 times.
- [x] Final consistency percentages are calculated.
- [x] Final prompts achieve more than 80% consistency across 15 runs.
- [x] Task variations are tested.
- [x] At least one limitation is documented.
- [x] No API key is included in the repository.

The notebook was checked without rerunning the API cells. A fresh start-to-finish execution would make API calls, so the checklist records the saved notebook evidence rather than claiming a new full rerun.
