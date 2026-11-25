# Simple LLM App (Git Team Practice)

A tiny project layout for practicing which files should be committed and which should stay local.

## Project idea

A small command-line AI assistant:
1. `app.py` receives a user question.
2. `llm_client.py` represents the future connection to an LLM provider.
3. `prompts.py` stores the system prompt.

This is a structure-only demo. It does not make real API calls.

## Local setup

```bash
python -m venv .venv
# Windows Git Bash:
source .venv/Scripts/activate
# Install dependencies if needed:
pip install -r requirements.txt
```

Copy `.env.example` to `.env`, then put your own local configuration in `.env`.
Never commit `.env` or real API keys.

## Run

```bash
python src/app.py
```
