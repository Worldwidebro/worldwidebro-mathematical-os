---
id: PORTAL-INFRA-HELPER-001
title: "_INFRASTRUCTURE — Master Operational Infrastructure & Configuration Hub"
aliases: ["_INFRASTRUCTURE", "Infrastructure Helpers", "Component Configs", "Operational Infrastructure"]
tags: ["infrastructure", "docker", "configs", "deployment", "components", "runbooks", "database", "mcp"]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[INDEX]] | [[CLAUDE]] | [[56-ENGINEERING/README|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE Master]] | [[50-MASTER-CONTROL/50-MASTER-CONTROL|Master Control]] | [[REALITY]]

# _INFRASTRUCTURE — Operational Infrastructure & Configuration Hub

> **Authority:** Infrastructure Control Plane ([[50-MASTER-CONTROL/50-MASTER-CONTROL|CP-027]])  
> **Master Operating Contract:** [[ANTIGRAVITY.md]] (Rule 1: Continuous Delivery, Rule 7: Zero-Trust Security)  
> **Canonical Engineering Master:** [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE.md]]  
> **Live Runtime State:** [[CLAUDE.md]]  
> **Status:** 🟢 ACTIVE — Fully Wired Operational Hub (2026-09-06)

---

## 1. Executive Summary & Hardware Topology

The **`_INFRASTRUCTURE`** subsystem coordinates the physical hardware nodes, container daemons, database engines, local LLM inference routers, and Model Context Protocol (MCP) server connectors powering the Company Brain operating system:

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                               TAILSCALE ENCRYPTED MESH                                 │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │
                    ┌───────────────────────┴───────────────────────┐
                    ▼                                               ▼
     ┌─────────────────────────────┐                 ┌─────────────────────────────┐
     │   PRIMARY ENGINEERING NODE  │                 │    MOBILE INFERENCE NODE    │
     │      Mac Studio M4 Max      │                 │     MacBook Air M-series    │
     │       (100.87.214.70)       │                 │       (100.121.17.63)       │
     ├─────────────────────────────┤                 ├─────────────────────────────┤
     │ • Neo4j Graph (:7687/:7474) │                 │ • Local Inference Models    │
     │ • Qdrant Vectors (:6333)    │                 │ • T7 Shield 2TB NVMe Cache  │
     │ • PostgreSQL DB (:5432)     │                 │ • Rapid Prototyping Runner  │
     │ • Redis Cache (:6379)       │                 │ • Mobile Dev Agent Harness  │
     │ • MinIO S3 (:9000/:9001)    │                 └─────────────────────────────┘
     │ • LiteLLM Proxy (:4000)     │
     │ • OmniRoute Router (:20128) │
     │ • LaCie 4TB Storage Mount   │
     └─────────────────────────────┘
```

---

## 2. Core Operational Configuration Assets

Beyond documentation, `_INFRASTRUCTURE/` contains mission-critical operational code, schemas, and configurations:

### 2.1 Container & Service Definitions
- **`docker-compose.yml`**: Defines the multi-container database and inference backbone for the Mac Studio node:
  - **PostgreSQL 16** (`:5432`): Core relational state, auth tables, and relational knowledge ledger.
  - **Qdrant** (`:6333`): Vector database with 1536-dim / 3072-dim embeddings for semantic retrieval.
  - **Neo4j Enterprise** (`:7687` Bolt / `:7474` HTTP): Entity relationship graph with Cypher querying.
  - **Redis 7** (`:6379`): Low-latency working memory, session tokens, and pub/sub message bus.
  - **MinIO S3** (`:9000` S3 API / `:9001` Web Console): S3-compatible blob store for raw artifacts, course media, and receipts.
  - **LiteLLM Proxy** (`:4000`): Load-balanced proxy forwarding OpenAI-compatible calls across backends.

### 2.2 Database Schemas & Analytics Queries
- **`supabase-education-schema.sql`**: Production 10-table PostgreSQL/Supabase schema powering the autonomous education agent pipeline:
  - Tables: `courses`, `modules`, `lessons`, `quizzes`, `quiz_questions`, `quiz_options`, `user_courses`, `quiz_attempts`, `quiz_answers`, `analytics_events`.
  - Includes UUID primary keys, foreign key constraints, indexes, timestamps, and JSONB metadata columns.
  - Connected with: [[_INFRASTRUCTURE/mcp-education-integration|mcp-education-integration.md]] and [[16-AGENTS/AGT-009-education-eval|AGT-009 (Education Eval Agent)]].
- **`dashboard-queries.sql`**: SQL operational queries for cross-venture analytics:
  - Query 1: Cross-venture shared code analysis (Jaccard similarity on repository dependencies).
  - Query 2: Tech stack penetration across all 35 business sectors.
  - Query 3: Production deployment health checks against Vercel and local nodes.

### 2.3 Model Context Protocol (MCP) Connectors
- **`postgres-mcp-config.json`**: FastMCP server connector enabling LLMs to run sanitized SQL queries against the local PostgreSQL instance.
- **`trigger-dev-mcp-config.json`**: FastMCP connector for Trigger.dev background workflow automation and event-driven pipelines.
- **`sector-mcp-registry.yaml`**: Definitive mapping assigning toolsets to business sectors:
  - Universal Baseline: Filesystem, Git, GitHub, Memory, Web Search.
  - Sector Extensions: Fintech (`stripe-mcp`, `plaid-mcp`), Healthcare (`fhir-mcp`), Web3 (`solana-mcp`), Developer Tooling (`ast-grep-mcp`).
  - Related Gateway: [[_MCP/README|Company Brain FastMCP Server]].

### 2.4 Inference Routing Scripts & Environment
- **`omniroute/omniroute.py`**: Python CLI client and health monitor for the OmniRoute gateway on port `:20128`.
- **Environment Templates (`.env.example`)**: Sanitized environment variables present across all 9 subdirectories to enforce Rule 7 (Zero-Trust Security).

---

## 3. Component Configuration Subdirectories (9 Modules)

| Subdirectory | Component | Port / Mount | Status | Documentation & Config Gateway |
|---|---|---|---|---|
| `omniroute/` | OmniRoute AI Gateway & Model Router | `:20128` (Tailscale) | ✅ LIVE | [[_INFRASTRUCTURE/omniroute/README|OmniRoute Gateway]] \| [[_INFRASTRUCTURE/omniroute/SETUP|Setup]] \| [[_INFRASTRUCTURE/omniroute/COMPLETION|Completion]] |
| `ollama/` | Ollama Local Model Runtime | `:11434` (Mac Studio) | ✅ LIVE | [[_INFRASTRUCTURE/ollama/README|Ollama Service Config]] |
| `storage/` | Persistent Volume Storage | `/Volumes/LaCie` & `T7` | ✅ LIVE | [[_INFRASTRUCTURE/storage/README|Storage Mounts & Volumes]] |
| `config/` | System Environment & Secret Hygiene | Global `.env` | ✅ CONFIGURED | [[_INFRASTRUCTURE/config/README|Environment Variables & Secrets]] |
| `tools/` | FastMCP Servers & Automation Runners | CLI / Daemons | ✅ CONFIGURED | [[_INFRASTRUCTURE/tools/README|Tools & Daemon Runners]] |
| `agents/` | Autonomous Agent Runtime Environment | Process Supervisor | ✅ CONFIGURED | [[_INFRASTRUCTURE/agents/README|Agent Runtime Configuration]] |
| `observability/` | Langfuse Tracing & Grafana Telemetry | `:3000` / `:3001` | 🟡 CONFIG READY | [[_INFRASTRUCTURE/observability/README|Observability & Tracing Config]] |
| `integrations/` | External SaaS & Webhook Connectors | Cloud Edge | ✅ CONFIGURED | [[_INFRASTRUCTURE/integrations/README|External Integrations Hub]] |
| `memory/` | Working Memory & Episodic Store | `:6379` (Redis) / Qdrant | ✅ CONFIGURED | [[_INFRASTRUCTURE/memory/README|Memory & Cache Configuration]] |

---

## 4. Key Architecture & Deployment Documents

### 4.1 Deployment Roadmaps & Phase Status
- [[_INFRASTRUCTURE/DEPLOYMENT_PHASES|DEPLOYMENT_PHASES.md]]: 4-phase rollout roadmap covering Databases, Model Caches, Exo Distributed Inference, and Observability.
- [[_INFRASTRUCTURE/BUZZ-INTEGRATION-PLAN|BUZZ-INTEGRATION-PLAN.md]]: Strategic architecture for Buzz communication relay and event ingestion.
- [[_INFRASTRUCTURE/BUZZ-PHASE1-DEPLOYMENT|BUZZ-PHASE1-DEPLOYMENT.md]]: Step-by-step deployment guide for Buzz infrastructure (relay, PostgreSQL, Redis, MinIO) on Mac Studio.
- [[_INFRASTRUCTURE/IMPLEMENTATION-STATUS|IMPLEMENTATION-STATUS.md]]: Live milestone tracking across infrastructure components.
- [[_INFRASTRUCTURE/PARALLEL-EXECUTION-STATUS|PARALLEL-EXECUTION-STATUS.md]]: Real-time tracking of parallel execution workstreams.
- [[_INFRASTRUCTURE/EXECUTION-SUMMARY-2026-09-06|EXECUTION-SUMMARY-2026-09-06.md]]: Comprehensive execution summary and milestone verification ledger.
- [[_INFRASTRUCTURE/NEXT-STEPS-2026-09-06|NEXT-STEPS-2026-09-06.md]]: Priority unblocking actions and scheduling roadmap.

### 4.2 Storage, Hardware Topology & Staging
- [[_INFRASTRUCTURE/DEVICE-STORAGE-TOPOLOGY|DEVICE-STORAGE-TOPOLOGY.md]]: Detailed storage layout across Mac Studio, MacBook Air, LaCie 4TB, and T7 Shield.
- [[_INFRASTRUCTURE/T7-SHIELD-STAGING-7-REPOS|T7-SHIELD-STAGING-7-REPOS.md]]: Integration blueprint for 7 strategic staged repositories on T7 Shield NVMe.
- [[_INFRASTRUCTURE/REPO-ANALYSIS-STAGING-06-REPOS|REPO-ANALYSIS-STAGING-06-REPOS.md]]: Architectural deep dive into 6 strategic staged repos (MetaGPT, browser-use, diagram-design, OpenViking).
- [[_INFRASTRUCTURE/ALIGNMENT-ANALYSIS|ALIGNMENT-ANALYSIS.md]]: Hardware sizing, unified memory allocations (128GB on M4 Max), and container resource limits.

### 4.3 Systems Architecture, CRM & Capability Absorption
- [[_INFRASTRUCTURE/COMPANY-BRAIN-ARCHITECTURE|COMPANY-BRAIN-ARCHITECTURE.md]]: Architectural blueprint of the distributed Company Brain operating system.
- [[_INFRASTRUCTURE/CRM-EVALUATION-SUMMARY|CRM-EVALUATION-SUMMARY.md]]: Strategic evaluation of Comp AI CRM (Intelligence), Twenty (Execution), and ClickUp (Productivity).
- [[_INFRASTRUCTURE/REPOSITORY-INTELLIGENCE-SYSTEM|REPOSITORY-INTELLIGENCE-SYSTEM.md]]: Autonomous repo ingestion, AST parsing, and knowledge graph mapping.
- [[_INFRASTRUCTURE/REPOSITORY-INTELLIGENCE-TASK-LIST|REPOSITORY-INTELLIGENCE-TASK-LIST.md]]: Granular execution plan for digesting internal and external repos.
- [[_INFRASTRUCTURE/STARRED_REPOS_CAPABILITY_PHASES|STARRED_REPOS_CAPABILITY_PHASES.md]]: Strategic capability absorption pipeline across 904 external repositories.
- [[_INFRASTRUCTURE/mcp-education-integration|mcp-education-integration.md]]: Complete integration guide connecting Supabase, FastMCP, and the 7-step course generation loop.
- [[_INFRASTRUCTURE/SESSION-UNIFIED-STATUS|SESSION-UNIFIED-STATUS.md]]: Historical change ledger documenting all infrastructure adjustments.

---

## 5. Operational Runbooks & Quickstarts

### 5.1 Booting the Container Daemon (Mac Studio)
```bash
# Navigate to infrastructure root
cd "/Users/acebless/Documents/The Company/Company Brain/_INFRASTRUCTURE"

# Validate configuration syntax
docker compose config

# Launch all backend databases and proxies
docker compose up -d

# Verify service container health
docker compose ps
```

### 5.2 Verifying Service Health
```bash
# OmniRoute AI Gateway (:20128)
curl -s http://100.87.214.70:20128/health | jq .

# Ollama Local Models (:11434)
curl -s http://100.87.214.70:11434/api/tags | jq .

# Neo4j Relational Graph (:7474)
curl -s -I http://100.87.214.70:7474 | grep "200 OK"

# Qdrant Vector Engine (:6333)
curl -s http://100.87.214.70:6333/healthz
```

### 5.3 Initializing Database Schemas
```bash
# Deploy education pipeline schema to Supabase/Postgres
psql "postgresql://postgres:postgres@100.87.214.70:5432/iza_os" -f supabase-education-schema.sql

# Execute resource analytics queries
psql "postgresql://postgres:postgres@100.87.214.70:5432/iza_os" -f dashboard-queries.sql
```

---

## 6. Upstream & Downstream Relationships

- **Upstream Authority:**
  - [[50-MASTER-CONTROL/50-MASTER-CONTROL|50-MASTER-CONTROL]] — Master system orchestrator
  - [[56-ENGINEERING/README|56-ENGINEERING]] — Master engineering specifications
  - [[CLAUDE.md]] — Real-time infrastructure audit ledger
- **Downstream Consumers:**
  - [[16-AGENTS/README|16-AGENTS Fleet]] — Executes on top of agent and MCP runtimes
  - [[_PIPELINES/README|Pipelines Subsystem]] — Dispatches workloads through OmniRoute and Docker containers
  - [[_EVAL/README|Operational Evaluation Hub (_EVAL)]] — Benchmarks latency, throughput, and accuracy
  - [[23-VENTURES/23-VENTURES|Ventures Ecosystem]] — Hosted on top of production infrastructure
