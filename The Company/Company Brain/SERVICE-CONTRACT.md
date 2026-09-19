[[STARTHERE]] | [[INDEX]] | [[REALITY]] | [[ANTIGRAVITY]]

# SERVICE-CONTRACT.md — Persistent Service Integration Contract

**System:** WorldwideBro Company Brain Distributed Mesh  
**Reference Architecture:** OmniRoute / FastMCP Persistent Connectivity Standard  
**Authority:** CP-027 (Infrastructure Control Plane)  
**Status:** `ACTIVE_SPECIFICATION`  

---

## 1. Unified Service Discovery & Endpoints

| Service | Protocol | Base URL | Health Check Probe | API Endpoint | MCP Endpoint |
|---|---|---|---|---|---|
| **OmniRoute AI Gateway** | HTTP / REST / A2A | `http://localhost:20128` & `http://100.87.214.70:20128` | `GET /.well-known/agent.json` | `POST /v1/chat/completions` | Stdio Adapter (`antigravity-mcp.mjs`) |
| **Ollama Runtime (Studio)** | HTTP / REST | `http://100.87.214.70:11434` | `GET /api/tags` | `POST /v1/chat/completions` | Discovered via OmniRoute |
| **Ollama Runtime (Air)** | HTTP / REST | `http://127.0.0.1:11434` | `GET /api/tags` | `POST /v1/chat/completions` | Discovered via OmniRoute |
| **Neo4j Graph Database** | Bolt / HTTP | `bolt://100.87.214.70:7687` | `GET http://100.87.214.70:7474` | Cypher Query API | Via `company-brain` MCP |
| **Qdrant Vector Engine** | HTTP / REST | `http://100.87.214.70:6333` | `GET /readyz` & `GET /collections` | `POST /collections/{name}/points/search` | Via `company-brain` MCP |
| **Exo Native MLX** | HTTP / REST | `http://100.87.214.70:52415` | `GET /` | `POST /v1/chat/completions` | Via OmniRoute Combo |
| **VEX Command Center** | HTTP / SPA | `http://localhost:5174` & `:5175` | `GET /` | Client UI & Router | BrowserOS Neo |

---

## 2. Authentication & Credential Architecture

```text
                        ┌───────────────────────────────┐
                        │   TAILSCALE ENCRYPTED MESH    │
                        │    (100.87.214.70 / 100.121)  │
                        └───────────────┬───────────────┘
                                        │
           ┌────────────────────────────┼────────────────────────────┐
           │                            │                            │
           ▼                            ▼                            ▼
  OmniRoute Master Key         n8n Automation Token         Neo4j Basic Auth
Bearer sk-30c31902dc...      JWT eyJhbGciOiJIUzI1...     neo4j / <password>
 (API & A2A Routing)          (Workflow Execution)       (Graph Persistence)
```

1. **Mesh Isolation:** Tailscale delivers machine-level authenticated zero-trust encryption without exposing ports to the open internet.
2. **Key Storage:** Stored in `.env` and `~/.gemini/config/mcp_config.json`, never checked into source control or exposed in public artifacts.

---

## 3. Request & Response Contracts

### 3.1 Inference Routing Contract (OmniRoute / OpenAI Standard)
- **Request:**
  ```json
  {
    "model": "auto",
    "messages": [
      {"role": "user", "content": "..."}
    ],
    "temperature": 0.2
  }
  ```
- **Response:**
  ```json
  {
    "id": "chatcmpl-...",
    "object": "chat.completion",
    "choices": [{
      "message": {
        "role": "assistant",
        "content": "..."
      },
      "finish_reason": "stop"
    }],
    "usage": {
      "prompt_tokens": 120,
      "completion_tokens": 45,
      "total_tokens": 165
    }
  }
  ```

### 3.2 Agent2Agent (A2A) Contract (JSON-RPC 2.0)
- **Endpoint:** `POST /a2a`
- **Request:**
  ```json
  {
    "jsonrpc": "2.0",
    "id": "req-001",
    "method": "message/send",
    "params": {
      "skillId": "smart-routing",
      "message": {
        "role": "user",
        "parts": [{"type": "text", "text": "..."}]
      }
    }
  }
  ```

---

## 4. Resilience, Timeout & Failure Policies

1. **Timeouts:**
   - Standard API requests: **15,000 ms**.
   - Heavy local inference (Ollama 14B / MLX 32B): **60,000 ms**.
   - MCP tool calls: **30,000 ms**.
2. **Retry Cascade:**
   - On HTTP 429 / 503 / timeout:
     1. Retry next provider in combo priority order (e.g. `qwen2.5-coder:14b` → `hermes3` → `claude-3-5-haiku`).
     2. Exponential backoff (500ms, 1500ms, 4000ms).
     3. Maximum retries capped at 3 attempts per provider, 28 attempts across complete pool.
3. **Circuit Breakers:**
   - Automatically opens on 5 consecutive failures within 60 seconds; cools down for 120 seconds before half-open probe.
