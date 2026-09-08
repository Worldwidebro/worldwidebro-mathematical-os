---
id: PORTAL-PIPELINES-001
aliases: ["PIPELINES", "Cognitive Pipelines Hub", "Execution Pipelines"]
tags: ["pipelines", "cognition", "orchestration", "flow", "automation"]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[19-ORCHESTRATION]] | [[03-INGESTION]] | [[INDEX]]

# _PIPELINES — Cognitive & Execution Data Pipelines Hub

> **Authority:** Orchestration Control Plane (CP-019)  
> **Framework:** [[_ONTOLOGY/COGNITION_FLOW.yaml|22-Stage Cognition Flow (WORLD -> EVOLUTION -> WORLD)]]  
> **Status:** ACTIVE — Updated 2026-09-06

---

## 1. The 10 Pipeline Stages

| Pipeline Stage | Subdirectory | Purpose & Function | Stage Gateway |
|---|---|---|---|
| **01. Ingestion** | `_PIPELINES/ingestion/` | Pulls raw artifacts, papers, repositories, and feeds | [[_PIPELINES/ingestion/README|Ingestion Pipeline]] |
| **02. Processing** | `_PIPELINES/processing/` | Text cleaning, chunking, deduplication, and normalizations | [[_PIPELINES/processing/README|Processing Pipeline]] |
| **03. Transformation** | `_PIPELINES/transformation/` | Entity extraction and structured schema mapping | [[_PIPELINES/transformation/README|Transformation Pipeline]] |
| **04. Indexing** | `_PIPELINES/indexing/` | Vectorization (nomic-embed-text) and Qdrant ingestion | [[_PIPELINES/indexing/README|Indexing Pipeline]] |
| **05. Retrieval** | `_PIPELINES/retrieval/` | Hybrid semantic search and graph traversal retrieval | [[_PIPELINES/retrieval/README|Retrieval Pipeline]] |
| **06. Reasoning** | `_PIPELINES/reasoning/` | Local MLX/Ollama LLM inference, prompt orchestration | [[_PIPELINES/reasoning/README|Reasoning Pipeline]] |
| **07. Code Intelligence** | `_PIPELINES/code-intelligence/` | AST parsing, Graphify extraction, and dependency checks | [[_PIPELINES/code-intelligence/README|Code Intelligence Pipeline]] |
| **08. Execution** | `_PIPELINES/execution/` | Autonomous task dispatch, tool execution, and loops | [[_PIPELINES/execution/EXECUTION_TRACKING|Execution Pipeline]] |
| **09. Learning** | `_PIPELINES/learning/` | Feedback loop recording, reflection, and prompt tuning | [[_PIPELINES/learning/README|Learning Pipeline]] |
| **10. Observability** | `_PIPELINES/observability/` | Telemetry capture, token cost tracing, and Langfuse logs | [[41-OBSERVABILITY/README|Observability Subsystem]] |

---

## 2. Connected Subsystems
- Orchestration Domain: [[19-ORCHESTRATION/19-ORCHESTRATION|19-ORCHESTRATION]]
- Ingestion Domain: [[03-INGESTION/03-INGESTION|03-INGESTION]]
- Knowledge Graph: [[08-KNOWLEDGE-GRAPH/08-KNOWLEDGE-GRAPH|08-KNOWLEDGE-GRAPH]]
- Memory Substrate: [[10-MEMORY/10-MEMORY|10-MEMORY]]
