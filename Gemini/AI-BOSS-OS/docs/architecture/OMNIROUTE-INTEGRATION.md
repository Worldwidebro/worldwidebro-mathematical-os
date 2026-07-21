# OmniRoute Integration Architecture

This document outlines **OmniRoute**'s architectural role as the central **AI Traffic Controller** and **Load-Balancing Gateway** in the AI-BOSS-OS.

## 1. Gateway Interfaces

OmniRoute acts as a high-performance routing reverse-proxy, exposing a unified OpenAI-compatible endpoint for all agents:

```text
http://localhost:20128/v1
```

Any downstream tool (such as Cline, Cursor, Aider, Claude Code, or Hermes) connects directly to this port, passing standard messages and options.

---

## 2. Dynamic Auto-Routing Tables

OmniRoute intercepts requests and maps model tags to specific execution backends based on performance, cost, and reliability rules.

```text
Request: model: "auto/coding"
  |
  +--> OmniRoute Rules Engine
         |
         +---> Mode: Online? -> Target: Claude-3-5-Sonnet (Direct API)
         +---> Mode: Offline? -> Target: Qwen-2.5-Coder-32B (via Ollama Port 11434)
```

The system maps the following default routes:

| Route String | Primary Target (Online) | Fallback Target (Offline/Local) | Optimization Focus |
| :--- | :--- | :--- | :--- |
| `auto` | Claude 3.5 Sonnet | Qwen 2.5 32B | Balanced reasoning and quality |
| `auto/coding` | Claude 3.5 Sonnet / DeepSeek | Qwen 2.5 Coder 32B | Code syntax and file edits |
| `auto/fast` | GPT-4o-Mini | Qwen 2.5 7B | Low latency, high throughput |
| `auto/cheap` | DeepSeek-V3 | Llama-3-8B | Minimal cost per token |
| `auto/smart` | Claude 3.5 Sonnet / GPT-4o | DeepSeek-R1 | Complex reasoning and logic |
| `auto/offline` | Qwen 2.5 Coder | Llama 3.1 | Zero network dependance |

---

## 3. Resilience, Compression, & CTrace

### 3.1 Failover & Resilience
If an upstream provider returns a `5xx` error, rate limit (`429`), or times out, OmniRoute intercepts the failure and dynamically transparently retries the request using the mapped fallback target without erroring out to the agent.

### 3.2 Token Compression
OmniRoute incorporates context compression rules (e.g., stripping markdown redundancy and system boilerplate) to reduce input token usage by up to 60-90% before routing to expensive cloud models.

### 3.3 Tracing and Observability
Every request passing through OmniRoute exports tracing metrics to the centralized **Langfuse** server (`http://100.87.214.70:3003`), monitoring:
- Prompt and completion tokens
- Operational cost (USD)
- Latency and TTFT (Time to First Token)
- Routing decisions and failover events
