"""A placeholder LLM client; no real network request is made."""


def generate_answer(question: str, system_prompt: str) -> str:
    """Return a placeholder response for Git practice."""
    return (
        "[Demo response] "
        f"Received your question: {question!r}. "
        f"System prompt length: {len(system_prompt)} characters."
    )
