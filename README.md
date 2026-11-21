# Prompt Engineering Lab

This lab evaluates and improves prompts for three customer-service tasks:

1. Sentiment classification
2. Product description generation
3. Structured data extraction

## Setup

From this folder, create and activate a virtual environment, then install the dependencies:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
pip install openai python-dotenv jupyter
```

macOS/Linux:

```bash
source .venv/bin/activate
pip install openai python-dotenv jupyter
```

Create a local `.env` file containing your own API key:

```text
OPENAI_API_KEY=your_api_key_here
```

Do not commit `.env` or your API key.

## Run the notebook

Start Jupyter from this folder:

```bash
jupyter notebook prompt_engineering_lab.ipynb
```

Open the notebook in the browser and run the cells in order. Cells that call the OpenAI API may use billable API requests.

## Files

- `prompt_engineering_lab.ipynb` — complete lab notebook with prompt versions, repeated tests, failure analysis, variations, and final comparison.
- `lab_proof.md` — detailed evidence and reviewer-oriented failure analysis.
- `lab_summary.md` — required one-paragraph summary of the experiment and lessons learned.
- `.gitignore` — prevents local secret files such as `.env` from being committed.
