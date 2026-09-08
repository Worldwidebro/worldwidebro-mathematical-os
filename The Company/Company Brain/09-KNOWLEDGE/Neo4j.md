---
id: DB-NEO4J-001-DOC
title: "Neo4j Graph Database — Canonical Relational Graph"
aliases: ["Neo4j", "Neo4j Graph Database", "09-KNOWLEDGE/Neo4j", "civos_neo4j", "DB-NEO4J-001"]
tags: ["database", "neo4j", "knowledge-graph", "cypher", "graph-database", "infrastructure"]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[09-KNOWLEDGE/09-KNOWLEDGE|09-KNOWLEDGE]] | [[08-KNOWLEDGE-GRAPH/08-KNOWLEDGE-GRAPH|08-KNOWLEDGE-GRAPH]] | [[56-ENGINEERING/INFRASTRUCTURE/06_DATA/DATABASES|DATABASES]] | [[REALITY]]

# Neo4j Graph Database (DB-NEO4J-001)

> **Authority:** Data Architecture (CP-006) & Infrastructure (CP-027)  
> **Host Node:** Mac Studio M4 Max (`100.87.214.70`)  
> **Status:** ACTIVE & VERIFIED (2026-09-06)

---

## 1. Overview & Instance Topology
**Neo4j** is the canonical relational graph engine powering WorldwideBro / Company Brain. It maintains the authoritative structural ontology, entity resolutions, dependency maps, venture portfolios, and execution relationships.

| Parameter | Operational Value | Context & Security |
|:---|:---|:---|
| **Instance Name** | `civos_neo4j` | Docker container on Mac Studio M4 Max |
| **Bolt Port** | `:7687` | Native binary driver protocol for Cypher execution |
| **HTTP Browser** | `:7474` | Web inspection UI (Tailscale encrypted) |
| **Local Access** | `bolt://127.0.0.1:7687` | Low-latency IPC from local agents and pipelines |
| **Network Mesh** | `bolt://100.87.214.70:7687` | Encrypted Tailscale mesh for remote engineering nodes |

---

## 2. Graph Schema & Ontological Model

### 2.1 Core Node Labels
- **`COMPANY`:** Top-level root entity (`WorldwideBro / Company Brain`).
- **`VENTURE`:** 789 cataloged ventures spanning 35 sectors (`SEC-001` to `SEC-035`).
- **`REPOSITORY`:** 893 owned codebases (`CB-REPO-000001` to `CB-REPO-000893`).
- **`CAPABILITY`:** 300 functional capability definitions (`CAP-001` to `CAP-300`).
- **`AGENT`:** 26 specialized cognitive agents (`AGT-*`).
- **`EXTERNAL_DEP`:** 904 Wikidata-grounded starred libraries and frameworks.

### 2.2 Core Edge Relationships
```text
(VENTURE)-[:IMPLEMENTS]->(CAPABILITY)
(VENTURE)-[:STORED_IN]->(REPOSITORY)
(REPOSITORY)-[:DEPENDS_ON]->(EXTERNAL_DEP)
(AGENT)-[:EXECUTES_FOR]->(VENTURE)
(CAPABILITY)-[:GOVERNED_BY]->(CONTROL_PLANE)
```

---

## 3. Bitemporal Schema Extension (Utopia Pattern)
Following the architecture extraction from [[09-KNOWLEDGE/Utopia-World-Model|Utopia (EXT-KNOW-003)]], edges support bitemporal properties:
- `valid_from` / `valid_to`: Real-world temporal validity.
- `tx_from` / `tx_to`: System transaction assertion timestamps.

---

## 4. Ingestion & Query Operations
- **Canonical Cypher Import:** `_REGISTRIES/RECONCILIATION_2026_09_01/COMPANY_BRAIN_NEO4J_IMPORT.cypher`
- **Pipeline Stage:** [[_PIPELINES/indexing/README|04. Indexing Pipeline]]
- **Query Traversal:** Executed via [[09-KNOWLEDGE/Query-Engine|Query Engine]] and [[18-TOOLS/README|FastMCP Neo4j Tooling]].

---

## 5. Connected Navigation
- Knowledge Gateway: [[09-KNOWLEDGE/09-KNOWLEDGE|09-KNOWLEDGE]]
- Relationship Ontology: [[08-KNOWLEDGE-GRAPH/08-KNOWLEDGE-GRAPH|08-KNOWLEDGE-GRAPH]]
- Polyglot Databases: [[56-ENGINEERING/INFRASTRUCTURE/06_DATA/DATABASES|DATABASES.md]]
- Vector Substrate: [[10-MEMORY/10-MEMORY|10-MEMORY (Qdrant)]]
- World Model: [[09-KNOWLEDGE/Utopia-World-Model|Utopia Enterprise World Model]]
- Master Control: [[50-MASTER-CONTROL/50-MASTER-CONTROL|50-MASTER-CONTROL]]
