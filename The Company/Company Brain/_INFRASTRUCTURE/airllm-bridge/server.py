#!/usr/bin/env python3
"""
AirLLM → OpenAI-compatible bridge for OmniRoute continuous coding.

Exposes:
  GET  /health
  GET  /v1/models
  POST /v1/chat/completions

Env:
  AIRLLM_MODEL              HF id or local path (default: Qwen/Qwen2.5-Coder-7B-Instruct)
  AIRLLM_SHARDS_PATH        Layer shard cache (LaCie/T7)
  AIRLLM_HOST / AIRLLM_PORT Bind (default 0.0.0.0:8020)
  AIRLLM_MOCK               If 1, return canned replies (no model load)
  AIRLLM_MAX_NEW_TOKENS     Cap generation length (default 256)
  AIRLLM_COMPRESSION        Optional: 4bit | 8bit
  AIRLLM_DELETE_ORIGINAL    If 1, drop HF originals after shard split
"""

from __future__ import annotations

import os
import time
import uuid
from threading import Lock
from typing import Any, Dict, List, Optional, Union

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

HOST = os.getenv("AIRLLM_HOST", "0.0.0.0")
PORT = int(os.getenv("AIRLLM_PORT", "8020"))
MODEL_ID = os.getenv("AIRLLM_MODEL", "Qwen/Qwen2.5-Coder-7B-Instruct")
SHARDS_PATH = os.getenv(
    "AIRLLM_SHARDS_PATH",
    "/Volumes/LaCie/airllm-shards",
)
MOCK = os.getenv("AIRLLM_MOCK", "0") == "1"
MAX_NEW_TOKENS = int(os.getenv("AIRLLM_MAX_NEW_TOKENS", "256"))
COMPRESSION = os.getenv("AIRLLM_COMPRESSION") or None
DELETE_ORIGINAL = os.getenv("AIRLLM_DELETE_ORIGINAL", "0") == "1"

app = FastAPI(title="AirLLM OpenAI Bridge", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

_model = None
_model_lock = Lock()
_load_error: Optional[str] = None


class ChatMessage(BaseModel):
    role: str
    content: Union[str, List[Any]]


class ChatCompletionRequest(BaseModel):
    model: str = Field(default=MODEL_ID)
    messages: List[ChatMessage]
    max_tokens: Optional[int] = None
    temperature: Optional[float] = 0.2
    stream: Optional[bool] = False


def _content_to_text(content: Union[str, List[Any]]) -> str:
    if isinstance(content, str):
        return content
    parts: List[str] = []
    for block in content:
        if isinstance(block, dict) and block.get("type") == "text":
            parts.append(str(block.get("text", "")))
        else:
            parts.append(str(block))
    return "\n".join(parts)


def messages_to_prompt(messages: List[ChatMessage]) -> str:
    lines: List[str] = []
    for m in messages:
        role = m.role.upper()
        lines.append(f"{role}: {_content_to_text(m.content)}")
    lines.append("ASSISTANT:")
    return "\n".join(lines)


def resolve_device():
    try:
        import torch

        if torch.cuda.is_available():
            return "cuda"
        if getattr(torch.backends, "mps", None) and torch.backends.mps.is_available():
            return "mps"
    except Exception:
        pass
    return "cpu"


def get_model():
    global _model, _load_error
    if MOCK:
        return None
    if _model is not None:
        return _model
    with _model_lock:
        if _model is not None:
            return _model
        try:
            os.makedirs(SHARDS_PATH, exist_ok=True)
            from airllm import AutoModel

            kwargs: Dict[str, Any] = {
                "layer_shards_saving_path": SHARDS_PATH,
                "delete_original": DELETE_ORIGINAL,
            }
            if COMPRESSION in ("4bit", "8bit"):
                kwargs["compression"] = COMPRESSION
            _model = AutoModel.from_pretrained(MODEL_ID, **kwargs)
            _load_error = None
            return _model
        except Exception as exc:  # noqa: BLE001
            _load_error = str(exc)
            raise


def generate_text(prompt: str, max_tokens: int) -> str:
    if MOCK:
        return (
            "CONTINUOUS_CODING_OK (airllm-bridge mock). "
            "Point OmniRoute / Instructor / LangChain at this /v1 endpoint."
        )

    model = get_model()
    assert model is not None
    device = resolve_device()

    encoded = model.tokenizer(
        [prompt],
        return_tensors="pt",
        return_attention_mask=False,
        truncation=True,
        max_length=4096,
        padding=False,
    )
    input_ids = encoded["input_ids"]
    if device == "cuda":
        input_ids = input_ids.cuda()
    elif device == "mps":
        input_ids = input_ids.to("mps")

    out = model.generate(
        input_ids,
        max_new_tokens=max_tokens,
        use_cache=True,
        return_dict_in_generate=True,
    )
    return model.tokenizer.decode(out.sequences[0], skip_special_tokens=True)


@app.get("/health")
def health():
    return {
        "status": "ok" if (_load_error is None) else "degraded",
        "mock": MOCK,
        "model": MODEL_ID,
        "shards_path": SHARDS_PATH,
        "device": "mock" if MOCK else resolve_device(),
        "loaded": _model is not None,
        "error": _load_error,
    }


@app.get("/v1/models")
def list_models():
    return {
        "object": "list",
        "data": [
            {
                "id": MODEL_ID,
                "object": "model",
                "created": int(time.time()),
                "owned_by": "airllm-bridge",
            }
        ],
    }


@app.post("/v1/chat/completions")
def chat_completions(req: ChatCompletionRequest):
    if req.stream:
        raise HTTPException(status_code=400, detail="stream=false only in scaffold")
    if not req.messages:
        raise HTTPException(status_code=400, detail="messages required")

    prompt = messages_to_prompt(req.messages)
    max_tokens = min(req.max_tokens or MAX_NEW_TOKENS, MAX_NEW_TOKENS)
    started = time.time()
    try:
        text = generate_text(prompt, max_tokens)
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=503, detail=f"airllm generate failed: {exc}") from exc

    # Prefer assistant continuation if the decoded string still contains the prompt.
    if text.startswith(prompt):
        text = text[len(prompt) :].lstrip()

    elapsed = time.time() - started
    completion_id = f"chatcmpl-airllm-{uuid.uuid4().hex[:12]}"
    return {
        "id": completion_id,
        "object": "chat.completion",
        "created": int(time.time()),
        "model": req.model or MODEL_ID,
        "choices": [
            {
                "index": 0,
                "message": {"role": "assistant", "content": text},
                "finish_reason": "stop",
            }
        ],
        "usage": {
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "total_tokens": 0,
        },
        "_airllm_bridge": {
            "elapsed_sec": round(elapsed, 3),
            "mock": MOCK,
            "shards_path": SHARDS_PATH,
        },
    }


def main():
    import uvicorn

    uvicorn.run(
        "server:app",
        host=HOST,
        port=PORT,
        reload=False,
        factory=False,
    )


if __name__ == "__main__":
    # Allow `python server.py` without module path issues
    import uvicorn

    uvicorn.run(app, host=HOST, port=PORT)
