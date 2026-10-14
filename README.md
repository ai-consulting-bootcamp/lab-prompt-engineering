# TechFlow Prompt Engineering Lab

This lab compares three prompt versions for sentiment analysis, product descriptions, and customer-feedback extraction.

## Files
- `prompt_engineering_lab.ipynb`: code, prompts, recorded outputs, failure analysis, and final comparison.
- `lab_summary.md`: one-paragraph learning reflection.
- `requirements.txt`: Python dependencies.
- `.gitignore`: excludes local secrets and temporary files.

## How to run
1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Create a local `.env` file beside the notebook:
   ```text
   OPENAI_API_KEY=your_api_key
   ```
3. Open the notebook in VS Code, select your Python environment, and execute cells in order.

The notebook uses OpenAI API calls. Running all cells again sends new requests and may produce different outputs. Do not commit the `.env` file.