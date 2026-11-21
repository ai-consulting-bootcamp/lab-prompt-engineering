# Lab Proof — Prompt Engineering

## 1. Code / Workflow

**Supporting file:** `prompt_engineering_lab.ipynb`

This notebook contains the prompt engineering exercises, different prompt versions (V1, V2 and V3), testing results, task variations and final evaluation.

## 2. Example Input

**Task:** Sentiment Analysis

**Customer message:**

"The product arrived late, but the customer service team was very helpful."

## 3. Evidence Produced

Three different customer messages were tested using the Version 3 sentiment prompt.

The model correctly classified the messages as:

- Product arrived broken: Negative.
- Delivery was okay: Neutral.
- Product was good, but customer service was terrible: Negative.

The results showed that the prompt could handle different customer messages, including mixed feedback about a product and its customer service.

The model identified both the negative aspect (late delivery) and the positive aspect (helpful customer service).

## 4. Final Output

The final Version 3 prompts were tested 15 times for each task.

| Task | Total runs | Unique responses | Consistency |
| :--- | ---: | ---: | ---: |
| Sentiment Analysis | 15 | 1 | 100% |
| Product Description | 15 | 8 | 26.7% |
| Data Extraction | 15 | 1 | 100% |

**Final evaluation observations:**

- **Sentiment Analysis:** All 15 runs consistently classified the original positive test message as Positive.
- **Product Description:** The outputs varied in wording and content, despite following the requested structure. The most repeated exact response appeared 4 times out of 15.
- **Data Extraction:** All 15 runs returned the same JSON structure with the four correct fields.

## 5. Failure / Limitation

The Product Description task continued to generate unsupported product features, such as plush ear cushions, an adjustable headband and available colours, despite instructions to use only the information provided.

The final Product Description Version 3 achieved 26.7% exact-response consistency across 15 runs.

This showed that few-shot examples and structured instructions helped maintain the output format but did not fully prevent hallucinations or variations in wording.
