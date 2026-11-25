"""A tiny test showing how project tests may be organized."""

from src.prompts import SYSTEM_PROMPT


def test_system_prompt_is_not_empty():
    assert SYSTEM_PROMPT.strip()
