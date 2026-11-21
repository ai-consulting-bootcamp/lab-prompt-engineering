---
name: lab-code-auditor
description: Audit, clean up, and review prompt engineering lab notebooks, multi-run OpenAI test scripts, and lab_proof.md deliverables. Use when asking Codex to inspect code quality, check secret safety, remove clutter, or verify evidence and limitations in the lab.
---

# Lab Code Auditor

A focused workflow for auditing, cleaning up, and verifying prompt engineering lab code and `lab_proof.md` notes without altering experiment results.

## When to Use

- Auditing `prompt_engineering_lab.ipynb` or helper scripts before or after running experiments
- Cleaning up messy cells, unused variables, or missing explanatory comments
- Checking that `.env` and API keys are never exposed and that synthetic data assumptions are clear
- Reviewing `lab_proof.md` to confirm exact inputs, run evidence, final outputs, and real limitations are included

## Steps

1. **Inspect Safety and Environment First**
   - Check that `OPENAI_API_KEY` is loaded from `.env` and never printed or hardcoded.
   - Confirm commands and notebook setup align with the project's Anaconda environment.

2. **Audit Experiment Structure and Reliability**
   - Verify that `v1`, `v2`, and `v3` prompts and 5/10/15-run tests are organized cleanly across sentiment analysis, product description generation, and structured data extraction.
   - Check for rate-limit handling, error handling, and clear distinction between real runs and synthetic test inputs.

3. **Clean Up Without Faking Evidence**
   - Remove redundant test lines or dead cells and add a brief comment above significant code lines explaining what and why.
   - Never invent consistency percentages, run outputs, or token counts; flag missing runs instead.

4. **Verify `lab_proof.md`**
   - Check that `lab_proof.md` serves as a clear entry point with linked supporting files, exact inputs, observed evidence, final outputs, and at least one concrete failure or limitation.

## Gotchas

- Do not rewrite the user's experimental prompts or alter recorded outputs during a cleanup pass unless explicitly asked.
- Keep fixes targeted and explain every change clearly so you can learn from the diff.
- Do not execute notebook cells or make live API calls.