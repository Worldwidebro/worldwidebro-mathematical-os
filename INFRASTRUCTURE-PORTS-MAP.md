---
title: Infrastructure Port Map
date: 2026-07-25T23:15:00Z
version: 1.0
---

# IZA OS Port Map & Service Routes

**Updated:** 2026-07-25 | **Status:** ✅ LIVE

## Mac Studio Services (via Tailscale 100.87.214.70)

| Service | Port | Purpose | Status | Access |
|---------|------|---------|--------|--------|
| **Traefik** | 80, 8080 | Route all traffic | ✅ UP | http://100.87.214.70:8080 |
| **Chat2DB** | 8080 | Database Intelligence | ✅ UP | http://100.87.214.70:8080 |
| **OmniRoute** | 20128 | LLM routing engine | ✅ UP | http://100.87.214.70:20128 |
| **n8n** | 5678 | Workflow automation | ✅ UP | http://100.87.214.70:5678 |
| **Neo4j** | 7687 | Knowledge graph (Bolt) | ✅ UP | bolt://100.87.214.70:7687 |
| **Neo4j UI** | 7474 | Graph browser | ✅ UP | http://100.87.214.70:7474 |
| **PostgreSQL** | 5432 | Transactional DB | ✅ UP | postgres://100.87.214.70:5432 |
| **Qdrant** | 6333 | Vector search | ✅ UP | http://100.87.214.70:6333 |
| **Langfuse** | 3003 | LLM observability | ✅ UP | http://100.87.214.70:3003 |
| **Redis** | 6380 | Caching & sessions | ✅ UP | redis://100.87.214.70:6380 |
| **Open WebUI** | 3010 | Ollama frontend | ✅ UP | http://100.87.214.70:3010 |
| **Infisical** | 8091 | Secrets manager | ✅ UP | http://100.87.214.70:8091 |
| **NocoDB** | 8090 | No-code DB UI | ✅ UP | http://100.87.214.70:8090 |
| **MCPJungle** | 8787 | MCP aggregator | ✅ UP | http://100.87.214.70:8787 |
| **MinIO** | 9000-9001 | S3 storage | ✅ UP | http://100.87.214.70:9000 |
| **Changedetection** | 5001 | Website monitoring | ✅ UP | http://100.87.214.70:5001 |

## MacBook Air Services (100.121.17.63)

| Service | Port | Purpose | Status |
|---------|------|---------|--------|
| **FreeLLMAPI** | 8000 | Free LLM (Gemini, Groq, Mistral, Cerebras, GitHub Models) | ✅ UP |
| **PostgreSQL** | 5432 | Local DB | ✅ UP |
| **Qdrant** | 6333 | Vector search (notes) | ✅ UP |
| **Redis** | 6379 | Caching | ✅ UP |
| **Grafana** | 3001 | Dashboards | ✅ UP |

---

## LLM Routing Chain

```
Script → OmniRoute (20128)
         ↓ [select model]
         ↓
         FreeLLMAPI (8000)
         ↓ [route to provider]
         ↓
         Response → Langfuse (3003)
         ↓
         Return
```

---

## Data Query Chain (Zero LLM Tokens)

```
Script → Query Options:
         ├─ Neo4j (7687) — graph queries
         ├─ PostgreSQL (5432) — transactional
         ├─ DuckDB (/data/...) — analytics
         └─ Qdrant (6333) — semantic
         ↓
         Results (no LLM calls)
```

---

## Environment Variables

```bash
# LLM Routing
export OMNIROUTE_URL=http://100.87.214.70:20128
export FREELLMAPI_URL=http://100.121.17.63:8000

# Data Access
export NEO4J_URL=bolt://100.87.214.70:7687
export NEO4J_USER=neo4j
export NEO4J_PASSWORD=ventures2026

export POSTGRES_URL=postgresql://postgres:postgres@100.87.214.70:5432/twenty
export DUCKDB_PATH=/Volumes/T7\ Shield/00_COMMAND_CENTER/worldwidebro-os/08-DATA/databases/worldwidebro_os.duckdb

export QDRANT_URL=http://100.87.214.70:6333

# Observability
export LANGFUSE_URL=http://100.87.214.70:3003
export LANGFUSE_PUBLIC_KEY=pk_...
export LANGFUSE_SECRET_KEY=sk_...
```

---

**Last verified:** 2026-07-25
