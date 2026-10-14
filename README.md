# Prompt Engineering Lab: TechFlow Solutions Chatbot

Ironhack AI Consulting & Integration Bootcamp lab. Three customer service prompts (sentiment analysis, product description generation and data extraction) are run 5, 10 and 15 times to measure consistency, then improved in two iterations: v2 (clarity, format, constraints) and v3 (few-shot examples, Chain-of-Thought). Target: more than 80% consistency over 15 runs.

The one-paragraph lab summary is in [`lab_summary.md`](lab_summary.md).

## Repository map

| File | Contents |
|---|---|
| [`prompt_engineering_lab.ipynb`](prompt_engineering_lab.ipynb) | Code, prompts v1 to v3, test results, failure analysis, variations, final report, bonus and costs |
| [`lab_summary.md`](lab_summary.md) | One-paragraph summary of the lab |
| `README.md` | How to run the work and a map of the repository |
| `.gitignore` | Keeps `.env` (the API key) and Jupyter checkpoints out of the repository |

## Where each deliverable is in the notebook

| Deliverable | Location |
|---|---|
| v1, v2 and v3 prompts for all three tasks | Steps 2, 6 to 8, and 9 to 11 |
| Results from the 5, 10 and 15-run tests | Steps 3, 4 and 5 |
| Failure analysis table and failure patterns | Step 5 |
| Variation tests and needed adjustments | Step 12 |
| Consistency for all versions and v1 vs v3 comparison | Cell 13.2 and the Final Report |
| Final v3 prompts and why each improvement was made | Cell 13.3 and the Final Report |
| Bonus: Challenge 4, evaluation framework | Bonus section at the end (cells B.1 to B.3) |
| Cost comparison across versions | Cost section at the end (cells C.1 to C.3) |

## How to run

1. Use Python 3.9 or newer, Jupyter (VS Code or JupyterLab) and an OpenAI API key.
2. In the repository folder, create a `.env` file containing one line: `OPENAI_API_KEY=your-key-here`. The file is listed in `.gitignore`, so the key is never committed.
3. Open `prompt_engineering_lab.ipynb` and run all cells from top to bottom. The first code cell installs `openai`, `python-dotenv` and `pandas`.
4. Save the notebook after the run, so the outputs stay in the file.

A full run makes about 330 calls to `gpt-4o-mini` (60 of them in the bonus section), one after another, and takes about 12 to 18 minutes (well under $1).