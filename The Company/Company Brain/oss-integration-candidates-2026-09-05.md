---
id: ADR-OSS-CANDIDATES-20260905
title: "OSS Integration Candidates Analysis (2026-09-05)"
aliases: [
  "oss-integration-candidates-2026-09-05",
  "OSS Candidates 2026-09-05",
  "ADR-OSS-CANDIDATES"
]
tags: ["oss", "architecture-decision", "openwork", "utopia", "neo4j", "capabilities"]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[CLAUDE]] | [[50-MASTER-CONTROL/50-MASTER-CONTROL|50-MASTER-CONTROL]] | [[14-CAPABILITIES/CAPABILITIES_INDEX|CAPABILITIES_INDEX]] | [[REALITY]]

# OSS Integration Candidates Analysis (2026-09-05)

> **Authority:** Architecture Control Plane (CP-027) & Master Control (CP-050)  
> **Originating RFC:** [[CLAUDE.md]] Missing Capability & Knowledge Graph Audits  
> **Candidates Evaluated:** `different-ai/openwork` & `deeplethe/utopia`  
> **Status:** ACTIVE — Architectural Evaluation & Decision Record

---

## 1. Executive Summary
During the comprehensive infrastructure re-verification of 2026-09-05, two architectural gaps were identified in the Company Brain operating layer:
1. **Capability Router Deficit (Layer 9):** Need for a dynamic search and execution interface connecting 26 agents to 300 capabilities.
2. **Bitemporal Knowledge Graph Deficit:** Need for historical entity tracking and temporal reasoning without compromising native Neo4j / Qdrant performance.

This document formally records the evaluation, trade-offs, and integration decisions for both candidate systems.

---

## 2. Candidate 1: `different-ai/openwork` (Capability Router)

- **Repository:** `https://github.com/different-ai/openwork`
- **Target Gap:** Layer 9 Capability Router (`search_capabilities` / `execute_capability` MCP)
- **Role:** Autonomous capability dispatch for 26 domain agents (`AGT-*`) across 300 capabilities (`CAP-001` to `CAP-300`).

### Evaluation
- **Strengths:** Lightweight MCP server interface, zero-configuration local tool exposure, clean JSON-RPC protocol adherence.
- **Weaknesses:** Lacks native awareness of Company Brain's 35 Sectors and multi-tier capability matrices.
- **Architectural Decision:** **HYBRID ADAPTATION**. Rather than replacing native FastMCP (`_MCP/fastmcp_server.py`), we incorporate OpenWork's semantic `search_capabilities` schema into Company Brain's FastMCP server backed by [[14-CAPABILITIES/CAPABILITIES_INDEX|CAPABILITIES_INDEX.md]] and [[14-CAPABILITIES/CAPABILITY_SOLUTION_MATRIX.json|CAPABILITY_SOLUTION_MATRIX.json]].

---

## 3. Candidate 2: `deeplethe/utopia` (Bitemporal World Model)

- **Repository:** `https://github.com/deeplethe/utopia`
- **Target Gap:** Bitemporal Routing Knowledge Graph (`GAP-TEMPORAL-KNOWLEDGE`) & Agent Safety Gates (`GAP-AGENT-EXECUTION-GATES`)
- **Detailed Note:** [[09-KNOWLEDGE/Utopia-World-Model|Utopia Enterprise World Model]]

### Evaluation
- **Strengths:** First-class bitemporal data modeling (valid time vs. transaction time), declarative Pydantic execution gates, financial guardrails.
- **Weaknesses:** Competes with Company Brain's existing Neo4j (`:7687`) and Qdrant (`:6333`) deployment; full adoption would require rewriting existing graph pipelines.
- **Architectural Decision:** **EXTRACT (Do Not Bolt-On)**.
  1. Do not deploy Utopia as an independent competing database.
  2. Extract Utopia's bitemporal property schema (`valid_from`, `valid_to`, `tx_from`, `tx_to`) into Company Brain's Neo4j schema definitions.
  3. Extract Utopia's financial gate decorator pattern into [[55-LOOP-ENGINEERING/55-LOOP-ENGINEERING|Fractal loop engineering]] for autonomous budget caps.

---

## 4. Candidate Summary & Action Matrix

| Candidate Repo | Focus Area | Verdict | Primary Implementation Target |
|:---|:---|:---|:---|
| `different-ai/openwork` | Capability Routing MCP | **HYBRID ADAPT** | [[_MCP/fastmcp_server.py]] & [[14-CAPABILITIES/CAPABILITIES_INDEX]] |
| `deeplethe/utopia` | Bitemporal Graph & Gates | **EXTRACT** | [[08-KNOWLEDGE-GRAPH/08-KNOWLEDGE-GRAPH]] & [[09-KNOWLEDGE/Utopia-World-Model]] |
| `utopia-planitia/utopia` | Decentralized Compute | **REFERENCE** | [[SECTORS/SEC-034-decentralized-web3]] |

---

## 5. Connected Navigation
- Live Infrastructure Record: [[CLAUDE.md]]
- Master Control Gateway: [[50-MASTER-CONTROL/50-MASTER-CONTROL]]
- Execution Stack: [[50-MASTER-CONTROL/EXECUTION_STACK]]
- Capabilities Index: [[14-CAPABILITIES/CAPABILITIES_INDEX]]
- External Capability Universe: [[_REGISTRIES/CANONICAL/EXTERNAL_CAPABILITY_UNIVERSE.yaml]]
