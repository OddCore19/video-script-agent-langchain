"""Minimal chain for generating a short video script outline."""

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


def build_script_chain(model: str = "gpt-4o-mini"):
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a helpful video script planner. Keep it concise and structured.",
            ),
            (
                "user",
                "Topic: {topic}\nAudience: {audience}\nLength: {length}\n"  # noqa: E501
                "Return a short outline with hook, 3 beats, and CTA.",
            ),
        ]
    )

    llm = ChatOpenAI(model=model)
    parser = StrOutputParser()

    return prompt | llm | parser
