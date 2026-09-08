"""
Thin client smoke tests — every framework talks to OmniRoute (/v1),
which can fall through to Ollama → exo → AirLLM bridge.

  export OPENAI_BASE_URL=http://127.0.0.1:20128/v1
  export OPENAI_API_KEY=$(python3 -c 'import json;print(json.load(open("/Users/acebless/.omniroute/config.json"))["contexts"]["default"]["apiKey"])')
"""

from __future__ import annotations

import os

BASE = os.getenv("OPENAI_BASE_URL", "http://127.0.0.1:20128/v1")
KEY = os.getenv("OPENAI_API_KEY", "sk-local")
MODEL = os.getenv("CODING_MODEL", "qwen2.5-coder:14b")


def via_openai_sdk():
    from openai import OpenAI

    client = OpenAI(base_url=BASE, api_key=KEY)
    r = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": "Reply: CONTINUOUS_CODING_OK"}],
        max_tokens=32,
    )
    print("openai:", r.choices[0].message.content)


def via_instructor():
    import instructor
    from openai import OpenAI
    from pydantic import BaseModel

    class Ping(BaseModel):
        status: str

    client = instructor.from_openai(OpenAI(base_url=BASE, api_key=KEY))
    out = client.chat.completions.create(
        model=MODEL,
        response_model=Ping,
        messages=[{"role": "user", "content": "Return status=ok"}],
    )
    print("instructor:", out)


def via_langchain():
    from langchain_openai import ChatOpenAI

    llm = ChatOpenAI(base_url=BASE, api_key=KEY, model=MODEL, temperature=0)
    print("langchain:", llm.invoke("Reply OK").content)


def via_llamaindex():
    from llama_index.llms.openai import OpenAI as LIOpenAI

    llm = LIOpenAI(api_base=BASE, api_key=KEY, model=MODEL)
    print("llamaindex:", llm.complete("Reply OK"))


def via_dspy():
    import dspy

    lm = dspy.LM(f"openai/{MODEL}", api_base=BASE, api_key=KEY)
    dspy.configure(lm=lm)
    print("dspy:", lm("Reply OK"))


if __name__ == "__main__":
    import sys

    targets = sys.argv[1:] or ["openai"]
    table = {
        "openai": via_openai_sdk,
        "instructor": via_instructor,
        "langchain": via_langchain,
        "llamaindex": via_llamaindex,
        "dspy": via_dspy,
    }
    for name in targets:
        table[name]()
