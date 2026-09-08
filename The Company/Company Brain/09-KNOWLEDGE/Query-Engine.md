---
id: KNOW-QRY-001
title: "Unified Query Engine — Graph, Vector & Hybrid Retrieval"
aliases: ["Query-Engine", "Query Engine", "09-KNOWLEDGE/Query-Engine", "Unified Query Engine"]
tags: ["query-engine", "hybrid-search", "graphrag", "neo4j", "qdrant", "omniroute"]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[09-KNOWLEDGE/09-KNOWLEDGE|09-KNOWLEDGE]] | [[08-KNOWLEDGE-GRAPH/08-KNOWLEDGE-GRAPH|08-KNOWLEDGE-GRAPH]] | [[_PIPELINES/retrieval/README|Retrieval Pipeline]] | [[REALITY]]

# Unified Query Engine: Graph, Vector & Hybrid Retrieval

> **Authority:** Retrieval Architecture (CP-010) & Knowledge Engine (CP-009)  
> **Host Node:** Mac Studio M4 Max (`100.87.214.70`)  
> **Status:** ACTIVE — Standardized & Verified (2026-09-06)

---

## 1. Overview
The **Unified Query Engine** is Company Brain's federated retrieval layer. It bridges deterministic relational graph traversals (Neo4j), semantic dense vector search (Qdrant), and intelligent model routing (OmniRoute), enabling autonomous agents to query facts, codebases, and historical states without hallucination.

---

## 2. Multi-Modal Retrieval Architecture

```text
                        Incoming Agent Query
                                 │
                 ┌───────────────┴───────────────┐
                 ▼                               ▼
       Deterministic Cypher             Dense Vector Embedding
     [[09-KNOWLEDGE/Neo4j\|Neo4j]]      [[10-MEMORY/10-MEMORY\|Qdrant]]
         (:7687 Bolt)                     (:6333 REST/gRPC)
                 │                               │
                 └───────────────┬───────────────┘
                                 ▼
                     Reciprocal Rank Fusion (RRF)
                                 │
                                 ▼
                       GraphRAG Neighborhood
                    (1-2 hop Neo4j subgraph)
                                 │
                                 ▼
                    Context Packet Synthesis
                                 │
                                 ▼
                     [[_PIPELINES/reasoning/README|Reasoning Pipeline]]
```

---

## 3. Query Modalities

### 3.1 Graph Traversal (Neo4j Cypher)
- **Role:** Deterministic relationship resolution, dependency chains, ownership hierarchies.
- **Example Cypher Pattern:**
  ```cypher
  MATCH (v:VENTURE {id: $venture_id})-[:IMPLEMENTS]->(c:CAPABILITY)
  OPTIONAL MATCH (c)<-[:FILLS_GAP]-(d:EXTERNAL_DEP)
  RETURN v.name, c.name, d.github_url;
  ```

### 3.2 Dense Vector Search (Qdrant)
- **Role:** Semantic concept matching, code card retrieval, natural language inquiry.
- **Embedding Model:** `nomic-embed-text` (768-dim) via local Ollama / MLX.
- **Collections:** `brain_vectors`, `code_nodes`, `repositories_catalog`.

### 3.3 GraphRAG Expansion
Vector hits are injected as root anchor nodes in Neo4j, pulling adjacent connected entities (ventures, capabilities, tools) to provide structured situational context to the agent prompt.

---

## 4. Integration with Cognition Pipelines
- Ingestion & Embedding: [[_PIPELINES/indexing/README|04. Indexing Pipeline]]
- Execution & RRF: [[_PIPELINES/retrieval/README|05. Retrieval Pipeline]]
- Inference & Combos: [[_PIPELINES/reasoning/README|06. Reasoning Pipeline]]
- Model Gateway: OmniRoute (`:20128`) & LiteLLM (`:4000`)

---

## 5. Connected Navigation
- Knowledge Gateway: [[09-KNOWLEDGE/09-KNOWLEDGE|09-KNOWLEDGE]]
- Relational Graph: [[09-KNOWLEDGE/Neo4j|Neo4j Graph Database]]
- Curated Repositories: [[09-KNOWLEDGE/Awesome-Lists|Awesome Lists Index]]
- World Model: [[09-KNOWLEDGE/Utopia-World-Model|Utopia Enterprise World Model]]
- Memory Substrate: [[10-MEMORY/10-MEMORY|10-MEMORY (Qdrant)]]
- Tools & MCP: [[18-TOOLS/README|18-TOOLS]]
