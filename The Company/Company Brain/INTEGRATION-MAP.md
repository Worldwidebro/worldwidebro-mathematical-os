# INTEGRATION-MAP.md — Company Brain System Boundary & Dependency Matrix

**Date:** 2026-09-19  
**Authority:** System Architecture & Infrastructure Control Plane (CP-027)  
**Verification Level:** `EMPIRICAL_PROBE_CONFIRMED`  

---

## 1. System Boundary Architecture

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│                                    INPUTS                                    │
│  - Antigravity IDE / Agent Prompts & Slash Commands                          │
│  - GitHub API Repositories (887 Owned + 928 Starred)                         │
│  - Markdown Registries (_REGISTRIES/CANONICAL/*.yaml)                        │
│  - BrowserOS Neo DOM Snapshots & Actions                                      │
│  - Inbound A2A JSON-RPC Requests (POST :20128/a2a)                           │
└──────────────────────────────────────┬───────────────────────────────────────┘
                                       │
                                       ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│                                 PROCESSING                                   │
│  - OmniRoute Multi-Provider Model Router (:20128)                            │
│  - Ollama Local/Remote Inference (Air :11434 & Studio 100.87.214.70:11434)   │
│  - FastMCP Core Server (_MCP/fastmcp_server.py)                              │
│  - n8n Automation Workflows (100.87.214.70:5678)                             │
│  - Graphify Codebase Knowledge Parser (graphify CLI)                         │
│  - Gary Tan gstack Vector PDF Compiler (scripts/make-pdf)                    │
└──────────────────────────────────────┬───────────────────────────────────────┘
                                       │
                                       ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│                                  STORAGE                                     │
│  - Git Repositories & Markdown Filesystem (Typed Wikilinks)                  │
│  - Neo4j Graph Database (100.87.214.70:7687 / :7474)                         │
│  - Qdrant Vector Engine (100.87.214.70:6333)                                 │
│  - PGLite Vector & BM25 Store (.gbrain/pglite)                               │
│  - OmniRoute SQLite Cache & CCR Store (~/.omniroute/storage.sqlite)          │
└──────────────────────────────────────┬───────────────────────────────────────┘
                                       │
                                       ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│                                   OUTPUTS                                    │
│  - VEX Command Center & Public Portals (http://localhost:5174 & :5175)       │
│  - Publication Vector PDFs (BUSINESS-CAPITAL-DATA-ROOM/EXPORTS/*.pdf)        │
│  - A2A Agent-to-Agent Dispatches & Task Executions                           │
│  - Audited Canonical Registries & Proven Venture Prospectuses                │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. External Dependencies Matrix

| System | Purpose | Protocol | Auth Type | Live Endpoint | Read/Write | Verified Status | Failure Behavior |
|---|---|---|---|---|---|---|---|
| **OmniRoute Gateway** | Multi-provider routing, quota fallback, token compression | HTTP / REST & JSON-RPC | Bearer API Key | `http://localhost:20128` & `100.87.214.70:20128` | Read/Write | `VERIFIED` | Returns 503 if combo exhausted; auto-retries downstream providers |
| **Mac Studio Ollama** | GPU-accelerated local LLM inference | HTTP / REST (OpenAI compat) | None (Protected by Tailscale mesh) | `http://100.87.214.70:11434/v1` | Read | `VERIFIED` | Connection timeout; OmniRoute cascades to fallback model combo |
| **MacBook Air Ollama** | Local node fallback inference | HTTP / REST (OpenAI compat) | None (Localhost only) | `http://127.0.0.1:11434/v1` | Read | `VERIFIED` | Cascades to cloud or studio runner |
| **Neo4j Relational Graph** | Venture-to-capability & sector relational graph | Bolt / Cypher & HTTP | Basic Auth (neo4j:password) | `bolt://100.87.214.70:7687` (`:7474`) | Read/Write | `VERIFIED` | FastMCP falls back to local JSON/YAML graph cache |
| **Qdrant Vector DB** | Semantic vector embeddings for data rooms and ventures | HTTP REST & gRPC | None / API Key | `http://100.87.214.70:6333` | Read/Write | `VERIFIED` | Semantic search falls back to gbrain BM25 keyword matching |
| **Exo Native MLX** | Multi-device Apple Silicon cluster inference | HTTP REST | None | `http://100.87.214.70:52415` | Read | `VERIFIED` | Bypassed if offline, routes to Ollama or OpenRouter |
| **n8n Automation Engine** | Business process automation and webhook handlers | HTTP / MCP | JWT Bearer Token | `http://100.87.214.70:5678` | Read/Write | `VERIFIED` | Queued executions; retry with exponential backoff |
| **BrowserOS Neo** | Agentic browser automation & DOM visual audit | HTTP / MCP | Session UUID | `http://127.0.0.1:9012/mcp` | Read/Write | `VERIFIED` | Disconnected sessions trigger automatic session recovery |
| **GitHub API** | Canonical repository metadata synchronization | HTTPS REST | Bearer PAT (`GITHUB_TOKEN`) | `https://api.github.com` | Read/Write | `VERIFIED` | Rate-limit throttling with cached catalog fallback |
