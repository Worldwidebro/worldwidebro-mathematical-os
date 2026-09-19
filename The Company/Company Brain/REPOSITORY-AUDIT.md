[[STARTHERE]] | [[INDEX]] | [[REALITY]] | [[ANTIGRAVITY]]

# REPOSITORY-AUDIT.md — Company Brain Ecosystem Comprehensive Audit

**Audit Date:** 2026-09-19  
**Authority:** System Architecture & Infrastructure Control Plane (CP-027)  
**Status:** `VERIFIED_EMPIRICAL`  
**Host Architecture:** Distributed Mesh — MacBook Air Engineering Node (`100.121.17.63`) + Mac Studio M4 Max (`100.87.214.70`) via Tailscale  

---

## 1. Executive Summary
Company Brain is the master operating system and operational control plane coordinating:
- **789 Ventures** organized across **36 Canonical Sectors** (SEC-001 through SEC-035 + SEC-037).
- **1,815 Cataloged Repositories** (887 owned + 928 starred external open-source capabilities).
- **Heterogeneous Runtime Engine:** Python FastMCP, Next.js / Node.js OmniRoute Gateway (`:20128`), Vite / React TypeScript VEX Command Center (`:5174`/`:5175`), Neo4j Graph (`:7687`/`:7474`), Qdrant Vector DB (`:6333`), Ollama local LLM runtime (`:11434`), and `exo` native MLX inference (`:52415`).

---

## 2. Technical Stack & Dependencies

| Layer | Component | Language / Framework | Version / Runtime | Entrypoint / Port | Status |
|---|---|---|---|---|---|
| **Core MCP** | `fastmcp_server.py` | Python (FastMCP, PyYAML, Requests) | Python 3.12 via `uv` | `_MCP/fastmcp_server.py` | `VERIFIED` |
| **Automation Bridge** | `n8n_mcp_bridge.py` | Python (JSON-RPC stdio) | Python 3.12 | `_MCP/n8n_mcp_bridge.py` | `VERIFIED` |
| **Inference Router** | OmniRoute AI Gateway | TypeScript / Next.js / Node.js | v3.8.50 / Node 26.7 | `http://localhost:20128` | `VERIFIED` (A2A Active) |
| **Local LLM Engine** | Ollama (Air + Studio) | Go / C++ / GGML | Ollama v0.3.x | `http://localhost:11434` / `100.87.214.70:11434` | `VERIFIED` (qwen2.5-coder:14b, hermes3, llama3.1) |
| **Relational Graph** | Neo4j Community | Java / Cypher | Docker (Mac Studio) | `bolt://100.87.214.70:7687` (`:7474`) | `VERIFIED` (Up 2 days) |
| **Vector Database** | Qdrant Engine | Rust / REST & gRPC | Docker (Mac Studio) | `http://100.87.214.70:6333` | `VERIFIED` (Up 2 days) |
| **Distributed MLX** | Exo MLX Engine | Python / Apple Silicon MLX | Exo v0.1.x | `http://100.87.214.70:52415` | `VERIFIED` (LIVE probe) |
| **Workflow Engine** | n8n Automation | TypeScript / Node.js | Docker (Mac Studio) | `http://100.87.214.70:5678` | `VERIFIED` (Up 23 hours) |
| **Frontend Portal** | Worldwidebro-Vex | React 18 / Vite / Tailwind CSS | Node.js | `http://localhost:5174` & `:5175` | `VERIFIED` (Pushed & Serving) |
| **Knowledge Engine** | gbrain (PGLite) | TypeScript / Postgres PGLite | Embedded CLI | `scripts/gbrain` | `VERIFIED` |
| **Vector PDF Compiler** | make-pdf | Playwright / KaTeX / Chromium | CLI Wrapper | `scripts/make-pdf` | `VERIFIED` |

---

## 3. Structural Breakdown & Codebase Organization

```text
/Users/acebless/Documents/The Company/Company Brain/
├── 00-CONSTITUTION/                 # Foundational charters, sector taxonomies, OpCo definitions
├── 13_ENGINEERING/                  # Architecture specifications & system design contracts
├── 14-CAPABILITIES/                 # 300 modular capability solution specifications
├── 15-SKILLS/                       # Fleet skill definitions & procedures
├── 16-AGENTS/                       # Autonomous agent specifications & directives
├── 20-DECISIONS/                    # Architectural Decision Records (ADRs) & pipeline plans
├── 23-VENTURES/                     # Canonical venture codebase mirrors & specs
├── 38-OPPORTUNITIES/                # Grant action packs & capital stack structures
├── 58-LOGISTICS/                    # Logistics domain gateway & dispatch specifications
├── BUSINESS-CAPITAL-DATA-ROOM/      # Institutional 22-domain data rooms for active ventures
├── SECTORS/                         # SEC-001 through SEC-035 canonical sector files
├── _DOCS/                           # Typed wikilink guides, architecture overviews
├── _MCP/                            # FastMCP servers, bridges, and systems integration master
├── _REGISTRIES/                     # Canonical single-source-of-truth registries (YAML/CSV)
├── .agents/                         # Universal agent contracts, rules, skills, workflows, mcp_config
├── scripts/                         # Operational CLI engines (make-pdf, gbrain, venture_os_engine)
└── graphify-out/                    # AST-extracted 90.9 MB knowledge graph (graph.json)
```

---

## 4. Discovered Integrations & Interfaces

### 4.1 Application Entrypoints
1. `_MCP/fastmcp_server.py`: Direct FastMCP entrypoint supporting command-line execution and stdio transport for IDEs.
2. `scripts/make-pdf`: Headless Chromium vector PDF generator.
3. `scripts/gbrain`: Hierarchical vector and BM25 full-text knowledge retrieval CLI.
4. `scripts/venture_os_engine.py`: Canonical 22-domain document operating system compiler.

### 4.2 APIs & Webhooks
1. **OmniRoute Gateway (`:20128`):**
   - `POST /v1/chat/completions`: OpenAI-compatible multi-provider chat endpoint.
   - `GET /v1/models`: Catalog aggregator across 36+ backends.
   - `POST /a2a`: Google Agent2Agent JSON-RPC 2.0 protocol endpoint (`message/send`, `message/stream`).
   - `GET /.well-known/agent.json`: Canonical Agent Card discovery.
2. **Ollama API (`:11434`):**
   - `GET /api/tags`: Model inventory inspection.
   - `POST /v1/chat/completions`: Direct OpenAI-compatible chat completion.
3. **n8n Automation Engine (`:5678`):**
   - Webhook trigger endpoints and MCP server at `/mcp-server/http`.

### 4.3 Databases & Persistence
1. **Neo4j (`bolt://100.87.214.70:7687`):** Relational knowledge graph storing ventures, capabilities, sectors, dependencies, and agents.
2. **Qdrant (`http://100.87.214.70:6333`):** Vector collection store for semantic text chunks, venture prospectuses, and capability embeddings.
3. **PGLite (`.gbrain/`):** Embedded local PostgreSQL vector database for instantaneous offline BM25 + pgvector searches.
4. **Local Git & Markdown:** Primary canonical storage with bidirectional typed wikilinks.

---

## 5. Deficiencies, Technical Debt & Blockers Identified

1. **LiteLLM Gateway Offline:**
   - LiteLLM (`:4000`) container is down on the Mac Studio. OmniRoute (`:20128`) has replaced LiteLLM as the active routing plane.
2. **SQLite Driver Warning in OmniRoute MCP Stdio Subprocess:**
   - OmniRoute's background stdio MCP adapter logs SQLite driver initialization warnings when accessed outside the main Next.js daemon runtime.
3. **Submodule Disconnection:**
   - An old path `The Company/HealthRoute-Courier/.git` was referenced in git index as a broken submodule. Git commands in Company Brain should bypass fsmonitor hooks when querying index.
