# Prompt Engineering Lab — Evidence

## Overview

This lab evaluates and improves three TechFlow Solutions chatbot tasks:

1. Sentiment analysis
2. Product-description generation
3. Customer-feedback data extraction

The completed workflow is in [prompt_engineering_lab.ipynb](prompt_engineering_lab.ipynb).

## Workflow and evidence

The notebook tested each Version 1 prompt at 5, 10, and 15 runs, then evaluated Version 2 and Version 3 prompts over 15 runs.

- [Final prompt comparison](results/final_prompt_comparison.csv)
- [Task-variation results](results/task_variations.csv)
- [Final prompts](results/final_prompts.json)
- [Version 1 15-run sentiment results](results/sentiment_v1_15_runs.csv)
- [Version 2 15-run sentiment results](results/sentiment_v2_15_runs.csv)
- [Version 3 15-run sentiment results](results/sentiment_v3_15_runs.csv)
- [Version 3 15-run product results](results/product_v3_15_runs.csv)
- [Version 3 15-run extraction results](results/extraction_v3_15_runs.csv)

## Representative query, evidence, and final output

### Task: Sentiment analysis

**Input**

```text
I love this product! It's exactly what I needed.


## Evidence

Across 15 Version 3 runs, sentiment classification achieved 100% success, 100% consistency, and one unique output.

### Final comparison summary		

Sentiment: 
V1 result: Extra explanations and synonym labels; 93.3% measured consistency	
Final result: 100% valid allowed labels across 15 runs

Product description: 
V1 result:Variable branding, invented specifications, and occasional truncation	Final result: 86.7% required-format consistency across 15 runs; structure and factual constraints improved

Data extraction:	V1 result: Variable bullet fields and no valid JSON	
Final result: 100% valid JSON across 15 runs



##Failure or limitation

Product descriptions are intentionally generative, so wording still varies between runs. The Version 3 prompt improved structural consistency to 86.7%, but would need stricter templates, structured fields, or application-side validation if near-identical copy were required.

A second limitation is that relative dates such as “last week” remain relative text because the prompt has no reference date for converting them to a calendar date.