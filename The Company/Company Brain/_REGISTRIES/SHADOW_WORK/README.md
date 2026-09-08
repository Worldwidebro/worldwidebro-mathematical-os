---
id: REG-SHADOW-WORK
title: "Shadow Work Knowledge Graph (SW-KG) Registry"
aliases: ["Shadow Work Registry", "SW-KG", "_REGISTRIES/SHADOW_WORK"]
tags: [registry, shadow-work, knowledge-graph, ontology, neo4j, wikidata]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[_REGISTRIES/README|Registries Hub]] | [[07-ONTOLOGY/README|Ontology]] | [[09-KNOWLEDGE/Neo4j|Neo4j Graph]]

# Shadow Work Knowledge Graph (SW-KG) Registry

> **Authority:** Knowledge Control Plane (CP-013) & Ontology Architecture (CP-027)  
> **Status:** Canonical Registry  
> **Standard:** Wikidata Linked Data (QID/PID) + RDF/JSON-LD + Neo4j Property Graph  
> **Version:** 1.0.0

---

## 1. Registry Architecture & Identity Principles

The **Shadow Work Knowledge Graph (SW-KG)** transforms psychological, decision-science, and operator-level shadow work into a computable, machine-readable registry.

### Core Identity Rule: Triple Separation of Identity
To guarantee long-term graph stability and RDF compatibility, identities are strictly decoupled:
1. **Internal Canonical Identity (`id`):** Proprietary, stable prefix ID (e.g., `SW-EGO-001`, `CB-001`, `OP-001`). This serves as the internal Primary Key.
2. **External Global Entity Identity (`wikidata.qid` / `uri`):** Permanent Wikidata QIDs (e.g., `Q484678`, `Q189283`). Functions as the linked-data URI for RDF graph resolution.
3. **Human-Readable Reference (`wikipedia.en`):** Canonical Wikipedia article URL (e.g., `https://en.wikipedia.org/wiki/Ego`) for operator inspection.

```
┌─────────────────────────────────────────────────────────────┐
│                    WIKIDATA (Global URI)                    │
│                      QID: Q1360677                          │
└──────────────────────────────┬──────────────────────────────┘
                               │ owl:sameAs
                               ▼
┌─────────────────────────────────────────────────────────────┐
│               SW-KG CANONICAL INTERNAL ENTITY               │
│                  ID: SW-COMP-001 (Complexity)               │
└──────────────┬──────────────────────────────┬───────────────┘
               │ rdfs:seeAlso                 │
               ▼                              │
┌──────────────────────────────┐              │
│      WIKIPEDIA ARTICLE       │              │
│    en.wikipedia.org/wiki/... │              │
└──────────────────────────────┘              │
                                              ▼
               ┌──────────────────────────────────────────────┐
               │         CAUSAL GRAPH & BUSINESS MAPPING      │
               │  • Cognitive Bias: CB-011 (Illusion of Ctrl) │
               │  • Operating Problem: OP-001 (Addiction)     │
               │  • Business Risk: BR-016 (Excess Complexity) │
               │  • Countermeasure: OPR-025 (Complexity Audit)│
               │  • Metric: MET-001 (Revenue / Repo Ratio)    │
               └──────────────────────────────────────────────┘
```

---

## 2. Directory Structure

```text
_REGISTRIES/SHADOW_WORK/
├── README.md               # This architectural reference
├── SCHEMA.yaml             # Master JSON Schema & JSON-LD context definition
├── SHADOW_REGISTRY.yaml    # Canonical machine-readable registry data
└── NEO4J_IMPORT.cypher     # Executable Cypher script for Mac Studio Neo4j
```

---

## 3. ID Taxonomy & Prefixes

| Prefix | Domain / Layer | Description | Example |
| :--- | :--- | :--- | :--- |
| `SW-` | Shadow Work | Core existential/psychological shadow concept | `SW-EGO-001`, `SW-COMP-001` |
| `PSY-` | Psychology | Academic psychological mechanism | `PSY-004` (Impostor Syndrome) |
| `CB-` | Cognitive Bias | Decision science & behavioral heuristics | `CB-001` (Confirmation Bias) |
| `OP-` | Operating Problem | Founder / operational failure mode | `OP-001` (Complexity Addiction) |
| `BEH-` | Behavioral Symptom | Physical trace in code, repos, calendar | `BEH-088` (Repo Sprawl) |
| `BR-` | Business Risk | Measurable threat to enterprise viability | `BR-008` (Insolvency) |
| `OPR-` | Operating Response | Concrete countermeasure / protocol | `OPR-001` (Red-Team Review) |
| `Q-` | Diagnostic Question | Direct falsification self-audit prompt | `Q-001` |
| `MET-` | Metric | Quantitative metric measuring mitigation | `MET-001` |
| `WF-` | Workflow | Executable operational workflow | `WF-DECISION-001` |
| `AGT-` | Agent | Autonomous agent / guardrail | `AGT-REDTEAM-001` |

---

## 4. Graph Traversals & Cypher Queries

### Query 1: Trace Root Cause to Business Risk
```cypher
MATCH path = (s:ShadowWork)-[:MANIFESTS_AS]->(b:CognitiveBias)-[:PRODUCES]->(o:OperatingProblem)-[:CAUSES_RISK]->(r:BusinessRisk)
WHERE s.id = "SW-COMP-001"
RETURN path;
```

### Query 2: Retrieve Mandatory Countermeasures for Active Shadows
```cypher
MATCH (s:ShadowWork {id: "SW-EGO-001"})-[:MANAGED_BY]->(m:OperatingResponse)
RETURN s.name AS Shadow, m.name AS Countermeasure, m.cadence AS Cadence;
```

### Query 3: Export to RDF/JSON-LD
All entities in `SHADOW_REGISTRY.yaml` map directly to RDF triples via `SCHEMA.yaml`'s `@context` block using standard vocabularies (`skos:definition`, `owl:sameAs`, `rdfs:seeAlso`, `prov:wasInfluencedBy`).

---

## 5. Live Infrastructure Integration

1. **Neo4j Enterprise (`100.87.214.70:7687`):** Loaded via `NEO4J_IMPORT.cypher`.
2. **Antigravity Rule Guardrail:** `.agents/rules/shadow-guardrails.md` queries the graph before allowing architectural sprawl.
3. **Observability:** Langfuse trace tags map back to `SW-*` and `CB-*` identifiers to evaluate AI-assisted decision quality.

---

## Subsystem Links & Architecture
- **Master Registries Portal:** [[_REGISTRIES/README|Master Registries]]
- **Neo4j Graph Architecture:** [[09-KNOWLEDGE/Neo4j|Neo4j]]
- **45 Ontologies Master:** [[07-ONTOLOGY/45-ONTOLOGIES-MASTER|07-ONTOLOGY]]
- **Master Control Matrix:** [[50-MASTER-CONTROL/CONTROL_MATRIX|Control Matrix]]
