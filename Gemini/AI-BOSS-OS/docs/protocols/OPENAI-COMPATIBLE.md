# OpenAI-Compatible API Endpoint Specification

This document details the interface specifications for the unified API endpoint exposed by **OmniRoute** on port `20128`.

## 1. Protocol Base Configuration

The gateway exposes a standard REST API mapping 1:1 with the OpenAI Chat Completions specification:

- **Base URL**: `http://localhost:20128/v1`
- **Port**: `20128`
- **Supported Endpoints**:
  - `POST /v1/chat/completions` (Core Chat Execution)
  - `GET /v1/models` (Model Catalog Query)

---

## 2. Request Schema Reference

Agents submit payloads to OmniRoute containing prompt contents and routing hints:

```json
{
  "model": "auto/coding",
  "messages": [
    {
      "role": "system",
      "content": "You are the AI-BOSS-OS CTO Agent."
    },
    {
      "role": "user",
      "content": "Analyze dependencies for the new venture."
    }
  ],
  "temperature": 0.2,
  "max_tokens": 4096,
  "stream": false
}
```

### Routing Payload Parameters:
- `model`: Maps directly to the OmniRoute routing table. Using `auto/coding`, `auto/smart`, etc., determines model allocation rules.
- `stream`: Supports SSE streaming completions to allow low-latency text rendering for real-time agent loops.

---

## 3. Response Schema Reference

OmniRoute returns standard completion structures, enabling transparent drops into standard client SDKs (e.g., Anthropic SDK, OpenAI SDK):

```json
{
  "id": "chatcmpl-1234567890",
  "object": "chat.completion",
  "created": 1721573620,
  "model": "claude-3-5-sonnet-20241022",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Parsed dependencies successfully: no loops found."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 1520,
    "completion_tokens": 140,
    "total_tokens": 1660
  }
}
```

### Header Additions:
OmniRoute appends custom headers to responses to support token tracking and debug observability:
- `X-OmniRoute-Routing-Target`: Tells the agent which specific LLM model handled the request (e.g., `anthropic/claude-3.5-sonnet`).
- `X-OmniRoute-Latency-Ms`: Reports total transaction latency.
- `X-OmniRoute-Cache-Hit`: Reports whether the request hit local cache layers.
