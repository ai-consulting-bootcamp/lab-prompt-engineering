# Prompt Engineering Lab — Proof & Evaluation Summary

- **Repository:** frazza90/lab-prompt-engineering
- **Notebook & Workflow:** [prompt_engineering_lab.ipynb](./prompt_engineering_lab.ipynb)
- **Full Step 13 & Suite Observations:** [step13_observations.md](./step13_observations.md)
- **Consistency Formula:** ((top_count - 1) / (n - 1) * 100)

## Code & Workflow
All prompt iterations (v1 through v3), multi-run evaluation loops (5, 10, and 15 runs), consistency calculations, and task variations (Sentiment Analysis, Data Extraction, Product Description, Customer Complaint + Escalation, and Store Locator) live in [prompt_engineering_lab.ipynb](./prompt_engineering_lab.ipynb), with detailed findings in [step13_observations.md](./step13_observations.md).

~~~python
sentiment_v3_template = """Classify the sentiment of the customer text as strictly one word: POSITIVE, NEGATIVE, or NEUTRAL.
Do not include explanations, punctuation, or extra text.

Text:
"{text}"
Sentiment:"""

step13_results = {}
for task_name, prompt in test_inputs_v3.items():
    runs = run_multiple(prompt, n=15)
    step13_results[task_name] = runs
    analyze_consistency(runs)
~~~

## Example Run (Input, Evidence & Final Output)
- **Task & Prompt Config:** Sentiment Analysis v3 (zero-shot, no CoT, single-label constraint), 15 runs.
- **Input Query:** "The delivery arrived a day early and the packaging was spotless."
- **Evidence Produced (15-Run Evaluation):** Total runs: 15 | Unique responses: 1 | Consistency: 100.0% (top match: 15/15) across Runs 1–15.
- **Final Output (v3):** POSITIVE

## Key Limitation & Failure Hit
- **Free-form prose & policy-field variance (0.0% exact-string consistency on Complaint v3):** While Escalate: YES occurred in 15/15 runs, allowing natural wording in Reply: and Reason: (plus occasional trailing spaces) produced 15/15 unique strings (0.0% exact-string consistency), and escalations@example-support.test appeared in 11/15 runs rather than 15/15 (some runs instead asked for order details or a photo or stated an internal escalation).
