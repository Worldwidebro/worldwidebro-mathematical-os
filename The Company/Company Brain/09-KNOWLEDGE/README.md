---
id: DOMAIN-09-README
title: "09-KNOWLEDGE — Knowledge Domain Overview"
aliases: ["09-KNOWLEDGE/README", "Knowledge Overview", "Domain 09 Overview"]
tags: ["knowledge", "policies", "procedures", "playbooks", "research", "world-model"]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[INDEX]] | [[09-KNOWLEDGE/09-KNOWLEDGE|09-KNOWLEDGE Gateway]] | [[08-KNOWLEDGE-GRAPH/08-KNOWLEDGE-GRAPH|08-KNOWLEDGE-GRAPH]] | [[REALITY]]

# 09-KNOWLEDGE

Policies, procedures, playbooks, research, IP, and world models

## 1. Overview
**09-KNOWLEDGE** manages Company Brain's organizational memory, codified operating procedures, intellectual property, external repository knowledge, and world models. It provides the grounded semantic substrate that prevents autonomous agents from hallucinating or acting outside established corporate policies.

---

## 2. Core Knowledge Subsystems

| Subsystem | Document | Scope & Functionality |
|:---|:---|:---|
| **Relational Knowledge Graph** | [[09-KNOWLEDGE/Neo4j|Neo4j Graph Database]] | Canonical graph (:7687) tracking ventures, capabilities, and dependencies |
| **Enterprise World Model** | [[09-KNOWLEDGE/Utopia-World-Model|Utopia World Model]] | Bitemporal modeling (valid vs. tx time) and financial execution gates |
| **Curated Repositories Index** | [[09-KNOWLEDGE/Awesome-Lists|Awesome Lists Index]] | Curated open-source solution space and 904 starred capabilities |
| **Unified Query Engine** | [[09-KNOWLEDGE/Query-Engine|Unified Query Engine]] | Multi-modal federated search across Neo4j, Qdrant, and OmniRoute |

---

## 3. Connected Domains

### Upstream (Inputs From):
- [[00-CONSTITUTION/00-CONSTITUTION|00-CONSTITUTION]] — Foundational company charter and non-negotiable principles.
- [[07-ONTOLOGY/07-ONTOLOGY|07-ONTOLOGY]] — Object types, semantic definitions, and schema structures.
- [[08-KNOWLEDGE-GRAPH/08-KNOWLEDGE-GRAPH|08-KNOWLEDGE-GRAPH]] — Graph relationship definitions and Cypher edge schemas.
- [[37-RESEARCH/37-RESEARCH|37-RESEARCH]] — Academic research, technical whitepapers, and intelligence syntheses.

### Downstream (Outputs To):
- [[12-CONTEXT/12-CONTEXT|12-CONTEXT]] — Context assembly and situational knowledge packets for LLM inference.
- [[19-ORCHESTRATION/19-ORCHESTRATION|19-ORCHESTRATION]] — Multi-agent workflow constraints and tool discovery.
- [[20-DECISIONS/20-DECISIONS|20-DECISIONS]] — Architectural and strategic decision records (ADRs).
- [[22-EXECUTION/22-EXECUTION|22-EXECUTION]] — Actionable execution parameters and guardrails.
- [[50-MASTER-CONTROL/50-MASTER-CONTROL|50-MASTER-CONTROL]] — Global system health and operational plane synchronization.

---

## 4. Control Points & Governance
- **Control Plane:** Knowledge Engine & IP Governance (CP-009)
- **Control Point Registry:** [[_REGISTRIES/control-points.md]]
- **Canonical Capabilities:** [[_REGISTRIES/CANONICAL/CAPABILITY_REGISTRY.yaml]]
- **Supply Chain Universe:** [[_REGISTRIES/CANONICAL/EXTERNAL_CAPABILITY_UNIVERSE.yaml]]

---

## 5. System Status
- **Overall Status:** 🟢 ACTIVE & VERIFIED
- **Relational Store:** Neo4j `civos_neo4j` active on `:7687`.
- **Bitemporal World Model:** Documented & extraction plan established.
- **Query Substrate:** Hybrid search operational across graph and vectors.

---

## 6. Key Documentation & Links
- Master Orientation: [[STARTHERE]]
- System Index: [[INDEX]]
- Architecture Overview: [[_DOCS/architecture]]
- Master Control Gateway: [[50-MASTER-CONTROL/50-MASTER-CONTROL]]
