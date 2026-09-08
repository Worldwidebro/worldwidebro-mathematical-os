---
id: PIP-STAGE-05
title: "Retrieval Pipeline (Stage 05)"
aliases: ['Retrieval Pipeline', 'Stage 05 Retrieval', '_PIPELINES/retrieval']
tags: ['pipeline', 'retrieval', 'search', 'hybrid-search', 'graphrag']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[_PIPELINES/README|Pipelines Hub]] | [[10-MEMORY/10-MEMORY|10-MEMORY]] | [[19-ORCHESTRATION/19-ORCHESTRATION|19-ORCHESTRATION]] | [[REALITY]]

# Retrieval Pipeline (Stage 05)

> **Authority:** Orchestration Control Plane (CP-019)  
> **Cognition Flow Phase:** `Stage 05: CONTEXT_SYNTHESIS`  
> **Target Domain:** [[10-MEMORY/10-MEMORY|10-MEMORY]]  
> **Status:** ACTIVE — Standardized & Verified (2026-09-06)

---

## 1. Pipeline Overview
The **Retrieval Pipeline** serves as stage 05 of Company Brain's 10-stage cognitive data pipeline.

Executes hybrid search combining dense vector similarity with sparse keyword matching, reciprocal rank fusion (RRF), and multi-hop Neo4j GraphRAG neighborhood expansion.

---

## 2. Data Contracts & Operational Flow

| Specification | Details |
|:---|:---|
| **Input Data** | Natural language agent queries, task specifications, entity lookups. |
| **Output Data** | Ranked context packets, subgraphs, verified factual assertions, citation-linked chunks. |
| **Primary Tooling** | Qdrant vector search, Neo4j Cypher traversal queries, BM25 scorers, GraphRAG orchestrator. |
| **Cognition Link** | [[_ONTOLOGY/COGNITION_FLOW.yaml|Cognition Flow Matrix]] |

---

## 3. Pipeline Lifecycle & Architecture

```text
       [[_PIPELINES/indexing/README|04. Indexing Pipeline]]
               │
               ▼
┌───────────────────────────────────────────────┐
│     STAGE 05: RETRIEVAL PIPELINE       │
│                                               │
│  Operations: Executes hybrid search combining dense vector... │
└───────────────────────────────────────────────┘
               │
               ▼
       [[_PIPELINES/reasoning/README|06. Reasoning Pipeline]]
```

---

## 4. Connected Subsystems & Domains
- **Parent Stage Hub:** [[_PIPELINES/README|Pipelines Hub]]
- **Domain Gateway:** [[10-MEMORY/10-MEMORY|10-MEMORY]]
- **Autonomous Orchestration:** [[19-ORCHESTRATION/19-ORCHESTRATION|19-ORCHESTRATION]]
- **Master Control:** [[50-MASTER-CONTROL/50-MASTER-CONTROL|50-MASTER-CONTROL]]
- **Execution Tracking:** [[_PIPELINES/execution/EXECUTION_TRACKING|Execution Tracking Standard]]

---

## 5. Phase 1 Capabilities (KG-017, KG-028, KG-048)

### KG-017: Hybrid Search ✅
- **File:** `hybrid_query.py` — Unified graph + vector search engine
- **Wrapper:** `_MCP/hybrid_query_tool.py` — FastMCP tool for OmniRoute
- **Endpoint:** `POST /api/graph/query` — FastAPI server (60-APIS/graph_api.py)
- **Status:** ✅ Implementation complete, testing phase
- **Integration:** Agents call via OmniRoute discovery

### KG-028: Agent Context Assembly ✅
- **File:** `12-CONTEXT/agent_context_builder.py` — Build task-specific subgraph
- **Wrapper:** `_MCP/context_assembly_tool.py` — FastMCP tool for OmniRoute
- **Endpoint:** `POST /api/graph/context` — FastAPI server (60-APIS/graph_api.py)
- **Status:** ✅ Implementation complete, testing phase
- **Integration:** Agents call to get relevant entities + risks + opportunities

### KG-048: Graph API Endpoint ✅
- **File:** `60-APIS/graph_api.py` — FastAPI server with all endpoints
- **Type:** Production FastAPI server with authentication
- **Endpoints:**
  - `POST /api/graph/query` — Hybrid search (KG-017)
  - `POST /api/graph/context` — Agent context (KG-028)
  - `GET /api/graph/entity/{id}` — Fetch single entity
  - `GET /api/graph/paths/{from}/{to}` — Find paths between entities
  - `GET /health` — Health check
- **Auth:** Bearer token (via Bitwarden "GRAPH_API_KEY")
- **Status:** ✅ Implementation complete, ready for deployment
- **Port:** 8000 (localhost) or Docker on any port

---

## 6. Infrastructure Status

| Component | Address | Status | Notes |
|-----------|---------|--------|-------|
| **Neo4j** | bolt://100.87.214.70:7687 | ✅ LIVE | 20,363 edges, Cypher ready |
| **Qdrant** | http://100.87.214.70:6333 | ✅ LIVE | 17,236 vectors indexed |
| **OmniRoute** | localhost:20128 | ✅ LIVE | 110 tools, MCP ready |
| **FastAPI** | localhost:8000 | ✅ READY | Waiting for deployment |

---

## 7. Related Documentation

- [[08-KNOWLEDGE-GRAPH|Knowledge Graph Overview]] — Neo4j architecture
- [[11-INDEXING|Indexing Pipeline]] — Qdrant vector indexing
- [[12-CONTEXT|Context Assembly Domain]] — KG-028 details
- [[16-AGENTS|Routing Agents]] — Agent definitions (AGT-001 through AGT-009)
- [[_MCP|MCP Tools & Services]] — Wrapper registration
- [[60-APIS|API Gateway]] — FastAPI configuration
- [[PHASE_1_EXECUTION_PLAN|Phase 1 Roadmap]] — Complete timeline + files
- [[COMPANY_BRAIN_KG_ASSESSMENT|KG Assessment]] — 50 capabilities status (30% complete)
