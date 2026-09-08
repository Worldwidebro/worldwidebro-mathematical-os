---
title: AirLLM OpenAI Bridge — OmniRoute Continuous Coding
description: Scaffold OpenAI-compatible AirLLM bridge on Studio/T7/LaCie for OmniRoute fallbacks and framework clients
tags:
  - infrastructure
  - airllm
  - omniroute
  - ollama
  - continuous-coding
  - langchain
  - instructor
---
Hub: `_INFRASTRUCTURE` · OmniRoute · `OMNIROUTE-MODELS-ROUTING` · `START-HERE-INFRASTRUCTURE`

# AirLLM OpenAI Bridge

OpenAI-compatible FastAPI wrapper around [AirLLM](https://github.com/lyogavin/airllm) so OmniRoute (and every OpenAI-shaped client) can fall through to layer-streamed HF models on Mac Studio.

**Port:** `:8020`  
**Shards:** `/Volumes/LaCie/airllm-shards` (Studio) or T7 `04_AI_MODELS/airllm-shards`  
**Default model:** `Qwen/Qwen2.5-Coder-7B-Instruct` (swap up for 70B+/Flash-Next when disk allows)

## Role in the mesh

```
Framework clients (Instructor, LangChain, LlamaIndex, DSPy, …)
        │  OPENAI_BASE_URL=http://127.0.0.1:20128/v1
        ▼
   OmniRoute (:20128)  combo: continuous-coding
        ├─ Air / Studio Ollama  qwen2.5-coder:14b   ← fast continuous coding
        ├─ Studio Ollama        llama3.1:8b
        ├─ AirLLM bridge        (:8020)             ← huge HF, slow/disk-bound
        └─ Studio exo MLX       (:52415)
```

AirLLM is **not** the default coder loop. Keep Ollama first; AirLLM is the overflow for models that do not fit Ollama/exo cleanly.

## Quick start

### Mock wiring test (this machine)

```bash
cd "Company Brain/_INFRASTRUCTURE/airllm-bridge"
./scripts/run-local.sh   # AIRLLM_MOCK=1
curl -s http://127.0.0.1:8020/health
```

### Deploy real inference on Mac Studio

```bash
./scripts/deploy-studio.sh
./scripts/register-omniroute.sh
```

Then point agents at OmniRoute, not `:8020` directly:

```bash
export OPENAI_BASE_URL=http://127.0.0.1:20128/v1
export OPENAI_API_KEY="$(python3 -c 'import json;print(json.load(open("/Users/acebless/.omniroute/config.json"))["contexts"]["default"]["apiKey"])')"
```

## Framework clients

All of these speak OpenAI `/v1` — see on-disk `examples/FRAMEWORKS.md` and `examples/clients_smoke.py` beside this bridge:

| Library | Use via OmniRoute |
| --- | --- |
| Instructor | structured outputs |
| Marvin | AI functions |
| LangChain | chains / agents |
| LlamaIndex | RAG |
| Haystack | pipelines |
| DSPy | programmatic prompts |
| Semantic Kernel | .NET/Python skills |
| Langflow | visual flows |
| Genkit | Google-style flows |

## Files

- `server.py` — FastAPI `/v1/chat/completions` + `/health`
- `scripts/run-local.sh` — mock/local
- `scripts/deploy-studio.sh` — rsync + venv + nohup on Studio
- `scripts/register-omniroute.sh` — provider + `continuous-coding` combo
- `launchd/com.companybrain.airllm-bridge.plist` — keep-alive on Studio

## Notes

- First real load **shards** the HF checkpoint — needs large free disk on LaCie/T7.
- Tailscale: Studio `100.87.214.70:8020` must be reachable from Air (same pattern as Ollama `:11434`).
- Do not re-enable broken Tailscale Serve on ports that already bind `*` (Ollama conflict lesson).
