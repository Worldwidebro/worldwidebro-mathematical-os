---
id: DOMAIN-08-README
title: "08-KNOWLEDGE-GRAPH — Relationship Ontology & Graph Edges"
aliases: ["08-KNOWLEDGE-GRAPH/README", "Knowledge Graph Overview", "Relationship Ontology Hub"]
tags: ["knowledge-graph", "neo4j", "cypher", "relationships", "edges", "ontology"]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[INDEX]] | [[08-KNOWLEDGE-GRAPH/08-KNOWLEDGE-GRAPH|08-KNOWLEDGE-GRAPH Gateway]] | [[09-KNOWLEDGE/09-KNOWLEDGE|09-KNOWLEDGE]] | [[REALITY]]

# Knowledge Graph (08-KNOWLEDGE-GRAPH)

> **Authority:** Graph Architecture (CP-008) & Infrastructure (CP-027)  
> **Host Node:** Mac Studio M4 Max (`100.87.214.70:7687`)  
> **Status:** ACTIVE — Standardized & Reconciled (2026-09-06)

---

## 1. Overview
**08-KNOWLEDGE-GRAPH** governs the relational connective tissue of WorldwideBro / Company Brain. It standardizes entity node schemas, typed relationships (edges), Cypher query patterns, and graph constraint rules in Neo4j, enabling multi-hop structural reasoning across ventures, capabilities, repositories, agents, and systems.

---

## 2. Core Graph Infrastructure & Documents

| Component | Document | Scope & Specification |
|:---|:---|:---|
| **Relational Store** | [[09-KNOWLEDGE/Neo4j|Neo4j Graph Database]] | `civos_neo4j` Docker container (:7687 Bolt, :7474 HTTP) |
| **Bitemporal Schema** | [[09-KNOWLEDGE/Utopia-World-Model|Utopia World Model]] | Valid time (`valid_from`/`to`) vs. Transaction time (`tx_from`/`to`) |
| **Unified Search** | [[09-KNOWLEDGE/Query-Engine|Unified Query Engine]] | Multi-modal federated queries joining graph paths with vectors |
| **Import Automation** | `_REGISTRIES/RECONCILIATION_2026_09_01/COMPANY_BRAIN_NEO4J_IMPORT.cypher` | Automated ingestion script loading 789 ventures & 893 repos |

---

## 3. Connected Domains

### Upstream (Inputs From):
- [[06-ENTITY-RESOLUTION/06-ENTITY-RESOLUTION|06-ENTITY-RESOLUTION]] — Deduplicated entity IDs (`ID_REGISTRY.yaml`).
- [[07-ONTOLOGY/07-ONTOLOGY|07-ONTOLOGY]] — High-level ontological categories and schema constraints.
- [[_PIPELINES/transformation/README|03. Transformation Pipeline]] — Extracted Cypher triples from incoming text.

### Downstream (Outputs To):
- [[09-KNOWLEDGE/09-KNOWLEDGE|09-KNOWLEDGE]] — Grounded organizational policies and IP repositories.
- [[11-INDEXING/11-INDEXING|11-INDEXING]] & [[_PIPELINES/indexing/README|04. Indexing Pipeline]] — Graph constraint indexing.
- [[12-CONTEXT/12-CONTEXT|12-CONTEXT]] — GraphRAG context expansion for agent prompts.
- [[50-MASTER-CONTROL/50-MASTER-CONTROL|50-MASTER-CONTROL]] — Plane-layer control point verification.

---

## 4. Control Points & Registries
- Control Plane: Graph Architecture (CP-008)
- Control Points: [[_REGISTRIES/control-points.md]]
- Graph Import Pipeline: [[_PIPELINES/indexing/README]]
- Graph Status: 🟢 Operational on Mac Studio (`bolt://100.87.214.70:7687`)
