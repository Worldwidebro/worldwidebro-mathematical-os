---
name: TOPOLOGY
title: System Topology (v3.0)
desc: ...
date: 2026-07-30T11:13:00Z
updated_by: Claude Code
version: 3.0
previous_versions: [2.2 (2026-07-25), 2.1 (2026-07-22), 2.0 (2026-07-20)]
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# System Topology (v3.0)

**Updated:** 2026-07-30  
**Status:** ✅ Mac Air (primary) + Mac Studio (services/Ollama) + T7 Shield (source of truth)  
**Change:** Physical hardware unified; T7 as centralized storage; shared access across machines

---

## Physical Hardware Map

```
┌──────────────────────────────────────────────────────────────┐
│  T7 SHIELD (External USB-C SSD, ~1.8TB)                     │
│  ├── Connected to: Mac Studio                                │
│  ├── Mount: /Volumes/T7\ Shield                              │
│  └── Master data:                                            │
│      ├── 00_COMMAND_CENTER/worldwidebro-os/WORLDWIDEBRO-OS/ │
│      │   ├── 01-BOSS-OS/ (registries, scripts)              │
│      │   ├── 03-VENTURES/ (all 712 ventures)                │
│      │   └── Documents/ ← **AFTER MIGRATION**                │
│      └── backups/ (daily snapshots)                          │
└──────────────────────────────────────────────────────────────┘
            │ USB-C cable
            ▼
    ┌───────────────────┐
    │   Mac Studio      │
    │   (16GB, M1/Pro)  │
    │   ├── Ollama      │
    │   │   (qwen3:8b)  │
    │   ├── Neo4j       │
    │   ├── PostgreSQL  │
    │   ├── Redis       │
    │   ├── n8n         │
    │   ├── Chat2DB     │
    │   └── All services│
    │   Port 11434:     │ SSH Tunnel
    │   (exposed)       │◄────────────┐
    └───────────────────┘             │
                                      │
                            ┌─────────┴─────────┐
                            │                   │
                   ┌────────▼──────────┐  ┌────▼────────────┐
                   │   Mac Air         │  │  (SSH Access)   │
                   │   (16GB, M3)      │  │  acebless@...   │
                   │   (CURRENT HERE)  │  │                 │
                   │                   │  │                 │
                   │ ~/Documents ──────┤  │  Remote:        │
                   │ (symlink to T7)   │  │  localhost:11434│
                   │                   │  │  = Mac Studio   │
                   │ vex-api/          │  │  Ollama         │
                   │ vex-engine/       │  │                 │
                   │ vex-hero-site/    │  │                 │
                   │ scripts/          │  │                 │
                   └───────────────────┘  └─────────────────┘
                            ▲
                ┌───────────┼───────────┐
                │           │           │
        ┌───────▼────┐  ┌──▼───────┐  ┌▼──────────┐
        │   iPad     │  │ iPhone   │  │ Any device│
        │ (Tailscale)│  │(Tailscale)  │ (Tailscale)│
        │            │  │          │  │           │
        │ Can access │  │Can access│  │ Read-only │
        │ All services   All services Access via  │
        │ 100.87.x.x │  │100.121.x │ IP          │
        └────────────┘  └──────────┘  └───────────┘
```

**Tailscale Network:** All devices (Mac Air, Mac Studio, iPad, iPhone) on 100.x.x.x subnet  
**Access:** Any device can reach Mac Studio services via Tailscale IPs

---

## Service Map (Layer 5: Network via Tailscale)

```
                        ┌─────────────────────────────────────┐
                        │  USER AGENTS & INTERFACES           │
                        │  ├─ Claude Code (this machine)      │
                        │  ├─ OmniRoute UI (20128)            │
                        │  ├─ Open WebUI (3010)               │
                        │  ├─ Chat2DB UI (8080/traefik)       │
                        │  └─ n8n UI (5678)                   │
                        └──────────────┬──────────────────────┘
                                       │
                ┌──────────────────────┼──────────────────────┐
                │                      │                      │
         ┌──────▼──────┐        ┌─────▼──────┐      ┌────────▼────────┐
         │   LAYER 3   │        │  LAYER 4   │      │    LAYER 5      │
         │  WORKFLOWS  │        │   MODELS   │      │    NETWORK      │
         │             │        │            │      │                 │
         │  ├─ n8n     │        │ ├─ Ollama  │      │  ✅ Tailscale   │
         │  ├─ LangGraph        │ │ (qwen)   │      │  (100.87.214.70)│
         │  └─ Temporal│        │ ├─ FreeLLM │      │                 │
         └──────┬──────┘        │ │ API      │      │  (100.121.17.63)│
                │               │ └─ Claude  │      └────────┬────────┘
                │               └─────┬──────┘               │
                │                     │                      │
         ┌──────▼──────┬──────────────▼───────┬──────────────▼────────┐
         │   LAYER 2   │                      │      LAYER 1: DATA    │
         │ AUTOMATION  │                      │                       │
         │             │                      │  Neo4j (7687)         │
         │  ├─ n8n     │                      │  ├─ Ventures (712)    │
         │  ├─ Zapier  │                      │  ├─ Repos (1,639)     │
         │  └─ MCP     │                      │  └─ Relationships     │
         │    Servers  │                      │                       │
         └─────────────┘                      │  PostgreSQL (5432)    │
                                              │  ├─ TwentyHQ          │
                                              │  └─ Transactional DB  │
                                              │                       │
                                              │  DuckDB (analytics)   │
                                              │  └─ Worldwidebro_os   │
                                              │                       │
                                              │  Qdrant (6333)        │
                                              │  ├─ repositories      │
                                              │  └─ notes             │
                                              └───────────────────────┘
                                                      ↑
                                              ┌───────┴────────┐
                                              │  CHAT2DB NEW   │
                                              │  (8080)        │
                                              │                │
                                              │ ✅ NL → SQL    │
                                              │ ✅ Neo4j Q     │
                                              │ ✅ PostgreSQL Q│
                                              │ ✅ DuckDB Q    │
                                              │ ✅ Schema Viz  │
                                              │ ✅ SQL Optimize│
                                              └────────────────┘
```

---

## Service Inventory (2026-07-25)

| Service | Host | Port | Status | Purpose |
|---------|------|------|--------|---------|
| **Chat2DB** | Mac Studio | 8080 | ✅ UP | Database Intelligence Layer (NEW) |
| OmniRoute | Mac Studio | 20128 | ✅ UP | LLM routing engine |
| n8n | Mac Studio | 5678 | ✅ UP | Workflow automation |
| Neo4j | Mac Studio | 7687 | ✅ UP | Knowledge graph (2,618 nodes) |
| PostgreSQL | Mac Studio | 5432 | ✅ UP | Transactional (TwentyHQ) |
| DuckDB | Mac Studio | — | ✅ UP | Analytics warehouse |
| Qdrant | Mac Studio | 6333 | ✅ UP | Vector search (1,648+ embeddings) |
| Langfuse | Mac Studio | 3003 | ✅ UP | LLM observability |
| Traefik | Mac Studio | 80/8080 | ✅ UP | Reverse proxy |
| Open WebUI | Mac Studio | 3010 | ✅ UP | Ollama frontend |
| Infisical | Mac Studio | 8091 | ✅ UP | Secrets management |
| NocoDB | Mac Studio | 8090 | ✅ UP | No-code database UI |
| MCPJungle | Mac Studio | 8787 | ✅ UP | MCP server aggregator |
| MinIO | Mac Studio | 9000-9001 | ✅ UP | S3-compatible storage |
| Redis | Mac Studio | 6380 | ✅ UP | Caching & sessions |
| Changedetection | Mac Studio | 5001 | ✅ UP | Website monitoring |

---

## Chat2DB Integration (NEW — 2026-07-25)

**Role:** Database Intelligence Layer (natural language queries)

**Connected Databases:**

| Database | Connection | Status | Query Capability |
|----------|-----------|--------|------------------|
| **Neo4j** | bolt://civos_neo4j:7687 | ✅ READY | ✅ NL → Cypher, graph queries |
| **PostgreSQL** | postgres://postgres:postgres@postgres:5432/twenty | ✅ READY | ✅ NL → SQL, transactional queries |
| **DuckDB** | /data/worldwidebro_os.duckdb | ✅ READY | ✅ NL → SQL, analytics queries |
| MySQL | (optional, pre-configured) | ⏳ Future | NL → SQL (when needed) |

**LLM Routing:** FreeLLMAPI (100.121.17.63:8000) → Gemini, Groq, Mistral, Cerebras, GitHub Models

**Confirmed Query Capability (Post-Deployment):**

You can ask Chat2DB:

```
"Show ventures with overdue invoices"
→ Neo4j (relationships) + PostgreSQL (transactions)
→ Auto-generated Cypher + SQL
→ Results + visualization
```

```
"Monthly revenue by sector"
→ DuckDB (analytics warehouse)
→ Auto-generated SQL + optimization suggestions
→ Charts + export
```

```
"Which repos support staffing workflows?"
→ Neo4j (repo graph + capabilities)
→ Auto-generated Cypher
→ Filtered results + recommendations
```

---

## Data Flow

```
Chat2DB User Input
    ↓
Natural Language Processing (FreeLLMAPI)
    ↓
SQL/Cypher Generation
    ↓
Route to appropriate database:
    ├─ Neo4j (relationships, graph queries, entity navigation)
    ├─ PostgreSQL (transactional data, OLTP)
    └─ DuckDB (analytics, aggregations, OLAP)
    ↓
Execute & Optimize
    ↓
Visualize Results (schema, ERDs, charts, network diagrams)
    ↓
Explain Query (why this SQL/Cypher, performance tips)
```

---

## Accessing Services from MacBook Air (via Tailscale)

| Service | URL | Login |
|---------|-----|-------|
| Chat2DB | http://100.87.214.70:8080 | admin / ventures2026 |
| OmniRoute | http://100.87.214.70:20128 | (built-in UI) |
| n8n | http://100.87.214.70:5678 | (OAuth) |
| Neo4j | http://100.87.214.70:7474 | neo4j / ventures2026 |
| Langfuse | http://100.87.214.70:3003 | (OAuth) |
| Open WebUI | http://100.87.214.70:3010 | (Ollama frontend) |

---

## Storage (2026-07-30 Status)

| Device | Capacity | Used | Free | Status | Role |
|--------|----------|------|------|--------|------|
| **Mac Studio** | 228GB | ~150GB | ~78GB | ✅ Services running | Ollama, databases, services |
| **Mac Air** | 251GB | ~160GB | ~91GB | ✅ Primary work | Code editing, git, development |
| **T7 Shield** | ~1.8TB | ~1.0TB | ~800GB | ✅ Source of truth | Master data, ventures (712), Documents (after migration) |

**Next action:** Migrate ~/Documents (13GB) from Mac Air local → T7 Shield, symlink back

---

**Version History:**
- v2.2 (2026-07-25): Added Chat2DB Database Intelligence Layer + Neo4j/PostgreSQL/DuckDB query capability confirmation
- v2.1 (2026-07-22): Initial topology + FreeLLMAPI + OmniRoute
- v2.0 (2026-07-20): Service topology baseline

**Next Update:** When Chat2DB queries are tested and confirmed working
