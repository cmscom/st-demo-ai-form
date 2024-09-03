import os
from typing import Generator
from openai import OpenAI


client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API"),
)


def translate_text(model: str, prompt: str, text: str) -> str | None:
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": prompt,
            },
            {
                "role": "user",
                "content": text,
            },
        ],
        model=model,
    )
    content = chat_completion.choices[0].message.content
    if content:
        return content.strip()
    else:
        return None


def openai_request(
    gpt_models: list[str], prompt: str, text: str
) -> Generator[tuple[str, str | None], None, None]:
    for model in gpt_models:
        yield model, translate_text(model, prompt, text)
