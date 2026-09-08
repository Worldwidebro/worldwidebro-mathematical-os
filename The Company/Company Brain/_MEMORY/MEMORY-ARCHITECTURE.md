# MEMORY-ARCHITECTURE — Physical Infrastructure and Subsystem Topology

[[_MEMORY/MEMORY-OS|MEMORY-OS]] | [[_MEMORY/MEMORY-MODEL|MEMORY-MODEL]] | [[CLAUDE]] | [[STARTHERE]]

> **Canonical Document ID:** `MEM-ARC-001`  
> **Authority:** System Architecture & Infrastructure Control Plane (CP-027)

---

## 1. Physical Node Topology

The Company Brain memory infrastructure spans the Tailscale encrypted mesh:

```text
                                TAILSCALE ENCRYPTED MESH
                                ┌──────────────────────┐
                                │ Worldwidebro@ Mesh   │
                                └──────────┬───────────┘
                                           │
         ┌─────────────────────────────────┼─────────────────────────────────┐
         ▼                                 ▼                                 ▼
MAC STUDIO M4 MAX (Primary)        MACBOOK AIR M-SERIES               MOBILE EDGE
IP: 100.87.214.70                  IP: 100.121.17.63                  iPad / iPhone
Storage: /Volumes/LaCie (4TB)      Storage: /Volumes/T7 Shield (2TB)  OmniRoute Tunnel:
• Neo4j Graph (:7687/:7474)        • Local Working Memory             100.80.229.113:20128
• Qdrant Vector DB (:6333)         • Ollama Local (:11434)
• MLX Native exo (:52415)          • Antigravity IDE Runtime
• OpenObserve Observability (:5080)• Bitwarden CLI (bw)
• LiteLLM Gateway (:4000)          • OmniRoute Daemon (:20128)
```

---

## 2. Component Mapping to Memory Tiers

| Infrastructure Service | Port | Primary Memory Role | Ingestion Method |
|---|---|---|---|
| **Neo4j Community/Enterprise** | `7687` / `7474` | **Associative Graph Memory** (Entities, dependencies, causal trees) | Cypher queries, graphify AST, FastMCP tools |
| **Qdrant Vector DB** | `6333` | **Semantic Memory** (Dense vector embeddings, RAG similarity) | REST API, Python client, OmniRoute embeddings |
| **OpenObserve** | `5080` | **Episodic Telemetry** (Inference spans, tool calls, logs, costs) | OpenTelemetry Collector, HTTP ingestion |
| **OmniRoute Daemon** | `20128` | **Context Routing & Inference** (Model combos, session snapshots) | HTTP REST, FastMCP wrapper (`antigravity-mcp.mjs`) |
| **Ollama Local** | `11434` | **Local Working Inference** (`qwen2.5-coder`, `llama3.1`) | HTTP REST, integrated into OmniRoute combos |
| **MLX Native exo** | `52415` | **Heavy Local Model Compute** (35B-70B model offloading) | OpenAI-compatible `/v1/chat/completions` |
| **Bitwarden CLI** | CLI | **Zero-Knowledge Security Engine** (Secrets resolution) | Subprocess `bw get password` / `bw get item` |
| **Git & Markdown Files** | Disk | **Procedural & Governance Memory** (Canonical registries, rules) | Git commits, Markdown wikilinks, YAML schemas |

---

## 3. High-Throughput Memory Ingestion Flow

```text
[User / Agent Task]
        │
        ▼
[OmniRoute / Antigravity MCP] ───(Filter debug stdout)───> [FastMCP Wrapper]
        │                                                         │
        ├──> Log Span ──> [OpenObserve (:5080)]                   │
        │                                                         │
        ├──> Query Vector ──> [Qdrant (:6333)]                    ▼
        │                                              [Agent Reasoning Core]
        ├──> Query Relationship ──> [Neo4j (:7687)]               │
        │                                                         ▼
        └──> Resolve Secrets ──> [Bitwarden CLI]         [Verified Execution]
                                                                  │
                                                                  ▼
                                                      [Consolidation Engine]
                                                                  │
                                              ┌───────────────────┴───────────────────┐
                                              ▼                                       ▼
                                      [Neo4j Node Update]                    [Qdrant Point Upsert]
```
