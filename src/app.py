"""Entry point for the demo LLM application."""

from llm_client import generate_answer
from prompts import SYSTEM_PROMPT


def main():
    question = input("Ask the demo assistant: ")
    answer = generate_answer(question, SYSTEM_PROMPT)
    print(answer)


if __name__ == "__main__":
    main()
