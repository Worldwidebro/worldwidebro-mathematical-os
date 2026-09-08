---
id: PIP-STAGE-04
title: "Indexing Pipeline (Stage 04)"
aliases: ['Indexing Pipeline', 'Stage 04 Indexing', '_PIPELINES/indexing']
tags: ['pipeline', 'indexing', 'vector-embeddings', 'qdrant', 'neo4j']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[_PIPELINES/README|Pipelines Hub]] | [[11-INDEXING/11-INDEXING|11-INDEXING]] | [[19-ORCHESTRATION/19-ORCHESTRATION|19-ORCHESTRATION]] | [[REALITY]]

# Indexing Pipeline (Stage 04)

> **Authority:** Orchestration Control Plane (CP-019)  
> **Cognition Flow Phase:** `Stage 04: MEMORY_CONSOLIDATION`  
> **Target Domain:** [[11-INDEXING/11-INDEXING|11-INDEXING]]  
> **Status:** ACTIVE — Standardized & Verified (2026-09-06)

---

## 1. Pipeline Overview
The **Indexing Pipeline** serves as stage 04 of Company Brain's 10-stage cognitive data pipeline.

Computes high-dimensional dense vector embeddings (`nomic-embed-text`), upserts points into Qdrant collections, and commits Cypher transactions into Neo4j.

---

## 2. Data Contracts & Operational Flow

| Specification | Details |
|:---|:---|
| **Input Data** | Resolved triples, normalized chunks, repo cards, venture descriptions, capability records. |
| **Output Data** | Indexed vector points in Qdrant collections (`brain_vectors`, `code_nodes`), Neo4j graph nodes and edges. |
| **Primary Tooling** | Qdrant REST API (`:6333`), Neo4j Bolt driver (`:7687`), Ollama / MLX embedding runners. |
| **Cognition Link** | [[_ONTOLOGY/COGNITION_FLOW.yaml|Cognition Flow Matrix]] |

---

## 3. Pipeline Lifecycle & Architecture

```text
       [[_PIPELINES/transformation/README|03. Transformation Pipeline]]
               │
               ▼
┌───────────────────────────────────────────────┐
│     STAGE 04: INDEXING PIPELINE       │
│                                               │
│  Operations: Computes high-dimensional dense vector embedd... │
└───────────────────────────────────────────────┘
               │
               ▼
       [[_PIPELINES/retrieval/README|05. Retrieval Pipeline]]
```

---

## 4. Connected Subsystems & Domains
- **Parent Stage Hub:** [[_PIPELINES/README|Pipelines Hub]]
- **Domain Gateway:** [[11-INDEXING/11-INDEXING|11-INDEXING]]
- **Autonomous Orchestration:** [[19-ORCHESTRATION/19-ORCHESTRATION|19-ORCHESTRATION]]
- **Master Control:** [[50-MASTER-CONTROL/50-MASTER-CONTROL|50-MASTER-CONTROL]]
- **Execution Tracking:** [[_PIPELINES/execution/EXECUTION_TRACKING|Execution Tracking Standard]]
