---
id: PIP-STAGE-03
title: "Transformation Pipeline (Stage 03)"
aliases: ['Transformation Pipeline', 'Stage 03 Transformation', '_PIPELINES/transformation']
tags: ['pipeline', 'transformation', 'entity-resolution', 'ontology', 'triples']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[_PIPELINES/README|Pipelines Hub]] | [[06-ENTITY-RESOLUTION/06-ENTITY-RESOLUTION|06-ENTITY-RESOLUTION]] | [[19-ORCHESTRATION/19-ORCHESTRATION|19-ORCHESTRATION]] | [[REALITY]]

# Transformation Pipeline (Stage 03)

> **Authority:** Orchestration Control Plane (CP-019)  
> **Cognition Flow Phase:** `Stage 03: ONTOLOGICAL_GROUNDING`  
> **Target Domain:** [[06-ENTITY-RESOLUTION/06-ENTITY-RESOLUTION|06-ENTITY-RESOLUTION]]  
> **Status:** ACTIVE — Standardized & Verified (2026-09-06)

---

## 1. Pipeline Overview
The **Transformation Pipeline** serves as stage 03 of Company Brain's 10-stage cognitive data pipeline.

Extracts named entities, resolves aliases against `ID_REGISTRY.yaml`, generates knowledge graph triples, and structures raw events into ontological schemas.

---

## 2. Data Contracts & Operational Flow

| Specification | Details |
|:---|:---|
| **Input Data** | Clean text chunks, code ASTs, and structured metadata from Stage 02 Processing. |
| **Output Data** | Resolved entities (`ENT-*`), relationship tuples (`(Subject)-[RELATION]->(Object)`), Cypher statements. |
| **Primary Tooling** | SpaCy NER, LLM entity extractors, Cypher statement generators, Pydantic schemas. |
| **Cognition Link** | [[_ONTOLOGY/COGNITION_FLOW.yaml|Cognition Flow Matrix]] |

---

## 3. Pipeline Lifecycle & Architecture

```text
       [[_PIPELINES/processing/README|02. Processing Pipeline]]
               │
               ▼
┌───────────────────────────────────────────────┐
│     STAGE 03: TRANSFORMATION PIPELINE       │
│                                               │
│  Operations: Extracts named entities, resolves aliases aga... │
└───────────────────────────────────────────────┘
               │
               ▼
       [[_PIPELINES/indexing/README|04. Indexing Pipeline]]
```

---

## 4. Connected Subsystems & Domains
- **Parent Stage Hub:** [[_PIPELINES/README|Pipelines Hub]]
- **Domain Gateway:** [[06-ENTITY-RESOLUTION/06-ENTITY-RESOLUTION|06-ENTITY-RESOLUTION]]
- **Autonomous Orchestration:** [[19-ORCHESTRATION/19-ORCHESTRATION|19-ORCHESTRATION]]
- **Master Control:** [[50-MASTER-CONTROL/50-MASTER-CONTROL|50-MASTER-CONTROL]]
- **Execution Tracking:** [[_PIPELINES/execution/EXECUTION_TRACKING|Execution Tracking Standard]]
