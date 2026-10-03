---
type: api-reference
canonical: false
authority: intelligence-platform-layer
version: 1.0
updated_at: 2026-10-02T23:42:00Z
relates_to: CLAUDE_MASTER_ONTOLOGY
---

# CLAUDE_API — Programmatic Integration

**Claude as an API: Messages, Batch, Files, Vision, Tools, Structured Output.**

**Last updated:** 2026-10-02  
**Endpoint:** `https://api.anthropic.com/v1`  
**SDKs:** Python, TypeScript, REST

---

## Core APIs

### [[MESSAGES_API]]
**Chat completion with tool use**

```bash
POST /v1/messages
Authorization: Bearer $ANTHROPIC_API_KEY
Content-Type: application/json

{
  "model": "claude-opus-5-5",
  "max_tokens": 1024,
  "system": "You are a helpful assistant.",
  "messages": [
    {
      "role": "user",
      "content": "What is 2+2?"
    }
  ]
}
```

**Response:**
```json
{
  "id": "msg_123",
  "type": "message",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "2 + 2 = 4"
    }
  ],
  "model": "claude-opus-5-5",
  "stop_reason": "end_turn",
  "stop_sequence": null,
  "usage": {
    "input_tokens": 15,
    "output_tokens": 8,
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0
  }
}
```

### [[STREAMING]]
**Server-sent events for real-time responses**

```bash
POST /v1/messages
Authorization: Bearer $ANTHROPIC_API_KEY
Content-Type: application/json

{
  "model": "claude-opus-5-5",
  "max_tokens": 1024,
  "stream": true,
  "messages": [{"role": "user", "content": "..."}]
}
```

**Stream events:**
- `message_start` — Message beginning
- `content_block_start` — Text/tool block
- `content_block_delta` — Incremental token
- `content_block_stop` — Block complete
- `message_delta` — Final metrics
- `message_stop` — Message complete

### [[BATCH_API]]
**Async batch processing (cost-optimized)**

```bash
POST /v1/messages/batches

{
  "requests": [
    {
      "custom_id": "request-1",
      "params": {
        "model": "claude-opus-5-5",
        "max_tokens": 1024,
        "messages": [{"role": "user", "content": "..."}]
      }
    },
    ...
  ]
}
```

**Cost:** 50% discount on batch jobs

**Latency:** 24-48 hour completion (variable)

### [[FILES_API]]
**Upload + reference files**

```bash
# Upload a file
POST /v1/files
Authorization: Bearer $ANTHROPIC_API_KEY

[multipart file upload]

# Response includes file_id

# Use in message
POST /v1/messages
{
  "model": "claude-opus-5-5",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "document",
          "source": {
            "type": "file",
            "file_id": "file_123"
          },
          "title": "Document Title"
        },
        {
          "type": "text",
          "text": "Analyze this document"
        }
      ]
    }
  ]
}
```

**Supported formats:**
- PDF (up to 20 pages)
- DOCX, XLSX, PPTX
- CSV, JSON, TXT
- Images (PNG, JPEG, GIF, WebP)

### [[TOKEN_COUNTING_API]]
**Pre-calculate token cost**

```bash
POST /v1/messages/count_tokens

{
  "model": "claude-opus-5-5",
  "messages": [
    {"role": "user", "content": "What is 2+2?"}
  ]
}
```

**Response:**
```json
{
  "input_tokens": 15
}
```

---

## Advanced Features

### [[TOOL_USE]]
**Define + invoke custom tools**

```json
{
  "model": "claude-opus-5-5",
  "max_tokens": 1024,
  "tools": [
    {
      "name": "search_database",
      "description": "Search internal database",
      "input_schema": {
        "type": "object",
        "properties": {
          "query": {
            "type": "string",
            "description": "Search query"
          }
        },
        "required": ["query"]
      }
    }
  ],
  "messages": [
    {"role": "user", "content": "Find users named John"}
  ]
}
```

**Response includes:**
```json
{
  "content": [
    {
      "type": "tool_use",
      "id": "toolu_123",
      "name": "search_database",
      "input": {"query": "users named John"}
    }
  ]
}
```

### [[VISION]]
**Image input + understanding**

```json
{
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "image",
          "source": {
            "type": "base64",
            "media_type": "image/jpeg",
            "data": "base64_encoded_image"
          }
        },
        {
          "type": "text",
          "text": "What's in this image?"
        }
      ]
    }
  ]
}
```

### [[STRUCTURED_OUTPUT]]
**Guaranteed JSON response**

```json
{
  "model": "claude-opus-5-5",
  "messages": [
    {"role": "user", "content": "Extract person name and age"}
  ],
  "response_format": {
    "type": "json_schema",
    "json_schema": {
      "name": "person_schema",
      "schema": {
        "type": "object",
        "properties": {
          "name": {"type": "string"},
          "age": {"type": "integer"}
        },
        "required": ["name", "age"]
      }
    }
  }
}
```

### [[PROMPT_CACHING]]
**Reuse cached context (50% cost reduction)**

```json
{
  "model": "claude-opus-5-5",
  "system": [
    {
      "type": "text",
      "text": "[large system prompt]"
    },
    {
      "type": "text",
      "text": "[large document]",
      "cache_control": {"type": "ephemeral"}
    }
  ],
  "messages": [
    {"role": "user", "content": "Question about document"}
  ]
}
```

**Cost savings:**
- Input tokens (normal): $3.00 / 1M tokens
- Input tokens (cached): $0.30 / 1M tokens (90% discount)
- Cache creation: 25% premium on first write

---

## Pricing & Token Economics

| Component | Price (per 1M tokens) | Note |
|-----------|---------------------|------|
| **Input (normal)** | $3.00 | Standard rate |
| **Input (cached)** | $0.30 | 90% discount |
| **Cache creation** | $3.75 | 25% premium |
| **Output** | $15.00 | Generation cost |
| **Batch (input)** | $1.50 | 50% discount |
| **Batch (output)** | $7.50 | 50% discount |

---

## SDKs & Clients

### Python
```bash
pip install anthropic

from anthropic import Anthropic

client = Anthropic(api_key="sk-...")
message = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}]
)
print(message.content[[0]].text)
```

### TypeScript
```bash
npm install @anthropic-ai/sdk

import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });
const message = await client.messages.create({
  model: "claude-opus-5-5",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Hello" }]
});
console.log(message.content[[0]].type === "text" && message.content[[0]].text);
```

### REST (curl)
```bash
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d '{
    "model": "claude-opus-5-5",
    "max_tokens": 1024,
    "messages": [{"role": "user", "content": "Hello"}]
  }'
```

---

## Error Handling

### Common Errors

| Code | Status | Cause | Fix |
|------|--------|-------|-----|
| 401 | Unauthorized | Invalid API key | Verify `$ANTHROPIC_API_KEY` |
| 429 | Rate limited | Quota exceeded | Reduce concurrent requests / use batch API |
| 500 | Server error | Anthropic outage | Retry with exponential backoff |
| 400 | Bad request | Invalid JSON | Validate request schema |

**Retry strategy:**
```python
import anthropic
import time

client = anthropic.Anthropic()

for attempt in range(3):
    try:
        message = client.messages.create(...)
        break
    except anthropic.RateLimitError:
        time.sleep(2 ** attempt)  # Exponential backoff
```

---

## Integration with [[OMNIROUTE]]

```
[[CLAUDE_API]]
    ↓
[[OMNIROUTE]]
    ↓
[Model routing + cache affinity]
    ↓
[Route to cached model if available]
    ↓
[Return response with cost headers]
```

OmniRoute wraps the Claude API to add:
- **Model routing** — Auto-select cheapest capable model
- **Cache affinity** — Route to cache-holding models
- **Cost tracking** — Per-request billing
- **Quota management** — Shared account pooling
- **Failover** — Automatic fallback on errors

---

## Rate Limits

| Plan | Requests/min | Tokens/min | Batch Limit |
|------|-------------|-----------|------------|
| Free | 3 | 90K | N/A |
| Pro | 2000 | 60M | 100K/day |
| Enterprise | Custom | Custom | Custom |

---

**Canonical source:** [[CLAUDE_MASTER_ONTOLOGY]]  
**Related:** [[CLAUDE]] [[OMNIROUTE]] [[MCP]]  
**Docs:** https://docs.anthropic.com

