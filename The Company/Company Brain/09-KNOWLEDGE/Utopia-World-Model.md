---
id: EXT-KNOW-003-DOC
title: "Utopia Enterprise World Model & Decentralized Mesh"
aliases: [
  "07-KNOWLEDGE/Utopia-World-Model",
  "Utopia-World-Model",
  "EXT-KNOW-003",
  "deeplethe/utopia",
  "Utopia World Model",
  "EXT-DEC-004",
  "utopia-planitia/utopia"
]
tags: ["knowledge-graph", "bitemporal", "world-model", "execution-gates", "external-capability", "web3"]
status: REFERENCED
verdict: EXTRACT
updated: 2026-09-06
---

[[STARTHERE]] | [[09-KNOWLEDGE/09-KNOWLEDGE|09-KNOWLEDGE]] | [[08-KNOWLEDGE-GRAPH/08-KNOWLEDGE-GRAPH|08-KNOWLEDGE-GRAPH]] | [[50-MASTER-CONTROL/EXECUTION_STACK|EXECUTION_STACK]] | [[CLAUDE]] | [[REALITY]]

# Utopia: Enterprise World Model & Autonomous Compute Mesh

> **Registry Tracking:** [[_REGISTRIES/CANONICAL/EXTERNAL_CAPABILITY_UNIVERSE.yaml|EXTERNAL_CAPABILITY_UNIVERSE.yaml]] (`EXT-KNOW-003` & `EXT-DEC-004`)  
> **Wikidata Grounding:** [Bitemporal Modeling (Q4918872)](https://www.wikidata.org/entity/Q4918872)  
> **Gap Fill Targets:** `GAP-TEMPORAL-KNOWLEDGE` & `GAP-AGENT-EXECUTION-GATES`  
> **Decision Verdict:** `EXTRACT` (Confidence: 0.85) — Extract bitemporal schema & execution gate patterns.

---

## 1. Executive Identification & Dual Role
Within the Company Brain ecosystem, the identifier **Utopia** refers to two complementary open-source capabilities cataloged in our external capability supply chain:

1. **`deeplethe/utopia` (`EXT-KNOW-003`):**  
   - **Repository:** `https://github.com/deeplethe/utopia`  
   - **Category:** ENTERPRISE KNOWLEDGE & GOVERNANCE  
   - **Architecture:** Open-source enterprise world model featuring bitemporal relational graphs, ontology-driven reasoning, and financial agent execution gates.
   - **Role:** Architectural candidate evaluated against Neo4j/Qdrant in [[oss-integration-candidates-2026-09-05]].

2. **`utopia-planitia/utopia` (`EXT-DEC-004`):**  
   - **Repository:** `https://github.com/utopia-planitia/utopia`  
   - **Category:** DECENTRALIZED & WEB3 COMPUTE  
   - **Sector Mapping:** [[SECTORS/SEC-034-decentralized-web3|Sector 34: Decentralized & Web3]]  
   - **Venture Alignment:** `V-WEB3-001 (Utopia Compute Mesh)`  
   - **Role:** Decentralized peer-to-peer compute and resilient execution mesh.

---

## 2. Deep Dive: `deeplethe/utopia` Architecture

### 2.1 Bitemporal Knowledge Graph
Unlike standard point-in-time graph models, Utopia structures knowledge along two orthogonal time axes:
- **Valid Time (Real-World Time):** When the asserted business relationship or state actually existed in the physical/corporate world.
- **Transaction Time (System Time):** When the assertion was recorded in the database ledger.

```text
               Transaction Time (System Record)
                             ▲
                             │
     Historical State        │     Current Knowledge State
     (Asserted at T_past)    │     (Asserted at T_now)
  ───┼───────────────────────┼───────────────────────────► Valid Time (Real-world event)
     │                       │
     Retroactive Corrections │     Forecasts & Scheduled Plans
```

### 2.2 Agent Safety & Financial Execution Gates
Utopia introduces programmable gate contracts (`AgentExecutionGate`) that intercept LLM execution before side-effects are dispatched:
- **Financial Thresholds:** Autonomous transactions below \$10 execute via L3 autonomy; transactions exceeding policy thresholds mandate human approval (L1/L2).
- **Blast Radius Validation:** Ensures no file modification exceeds permitted subtrees.
- **Invariance Checking:** Re-evaluates ontology consistency constraints prior to committing state changes.

---

## 3. Company Brain Evaluation & Extraction Plan

As recorded in [[CLAUDE.md]] and [[_REGISTRIES/CANONICAL/CAPABILITY_GAP_MATRIX.yaml]]:

| Architectural Dimension | Company Brain Native Stack | Utopia (`deeplethe/utopia`) | Architectural Decision |
|:---|:---|:---|:---|
| **Graph Database** | [[08-KNOWLEDGE-GRAPH/08-KNOWLEDGE-GRAPH|Neo4j (:7687)]] | Embedded Neo4j / PostgreSQL | **Retain Neo4j native**; extract schema patterns |
| **Vector Search** | [[10-MEMORY/10-MEMORY|Qdrant (:6333)]] | Embedded vectors | **Retain Qdrant native** |
| **Bitemporal Reasoning** | Missing (`GAP-TEMPORAL-KNOWLEDGE`) | Native bitemporal schema | **EXTRACT bitemporal schema into Neo4j** |
| **Execution Gates** | Missing (`GAP-AGENT-EXECUTION-GATES`) | Python/Pydantic gate models | **EXTRACT execution gate pattern into Fractal** |

### Extraction Action Items:
1. **Bitemporal Neo4j Schema:** Port Utopia's `valid_from`, `valid_to`, `tx_from`, and `tx_to` edge property conventions into Company Brain's Cypher ontology (`_ONTOLOGY/`).
2. **Fractal Gate Middleware:** Adapt Utopia's execution gate decorator into [[55-LOOP-ENGINEERING/55-LOOP-ENGINEERING|Fractal]]'s `01-PLAN` and `02-EXECUTE` pipelines to enforce financial caps on autonomous subagents.

---

## 4. Deep Dive: `utopia-planitia/utopia` Compute Mesh

Mapped under [[SECTORS/SEC-034-decentralized-web3]]:
- **Decentralized Node Discovery:** Uses DHT (Distributed Hash Table) for resilient peer coordination without central coordinating servers.
- **Local-First Fallback:** Can operate in air-gapped environments, syncing state across Tailscale or local subnets when connectivity is restored.
- **Support for Venture `V-WEB3-001`:** Provides decentralized backend infrastructure for trustless agent computations.

---

## 5. Connected Canonical Files
- Registry Entry: [[_REGISTRIES/CANONICAL/EXTERNAL_CAPABILITY_UNIVERSE.yaml]] (`EXT-KNOW-003`, `EXT-DEC-004`)
- Gap Matrix: [[_REGISTRIES/CANONICAL/CAPABILITY_GAP_MATRIX.yaml]]
- Integration Decision: [[oss-integration-candidates-2026-09-05]]
- Knowledge Domain: [[09-KNOWLEDGE/09-KNOWLEDGE]]
- Execution Stack: [[50-MASTER-CONTROL/EXECUTION_STACK]]
- Sector Profile: [[SECTORS/SEC-034-decentralized-web3]]
