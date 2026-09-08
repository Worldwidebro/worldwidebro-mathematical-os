---
id: PIP-STAGE-07
title: "Code Intelligence Pipeline (Stage 07)"
aliases: ['Code Intelligence Pipeline', 'Stage 07 Code Intelligence', '_PIPELINES/code-intelligence']
tags: ['pipeline', 'code-intelligence', 'ast', 'graft', 'graphify']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[_PIPELINES/README|Pipelines Hub]] | [[57-CODE-INTELLIGENCE/57-CODE-INTELLIGENCE|57-CODE-INTELLIGENCE]] | [[19-ORCHESTRATION/19-ORCHESTRATION|19-ORCHESTRATION]] | [[REALITY]]

# Code Intelligence Pipeline (Stage 07)

> **Authority:** Orchestration Control Plane (CP-019)  
> **Cognition Flow Phase:** `Stage 07: SYNTACTIC_COMPREHENSION`  
> **Target Domain:** [[57-CODE-INTELLIGENCE/57-CODE-INTELLIGENCE|57-CODE-INTELLIGENCE]]  
> **Status:** ACTIVE — Standardized & Verified (2026-09-06)

---

## 1. Pipeline Overview
The **Code Intelligence Pipeline** serves as stage 07 of Company Brain's 10-stage cognitive data pipeline.

Parses repository source code into abstract syntax trees, extracts symbols, imports, classes, functions, and cross-repository dependencies via Graft and Graphify.

---

## 2. Data Contracts & Operational Flow

| Specification | Details |
|:---|:---|
| **Input Data** | Source code repositories across 893 owned and external repos. |
| **Output Data** | AST JSON graphs, symbol registries, function call hierarchies, blast radius matrices. |
| **Primary Tooling** | Graft CLI (`@nanonets/graft`), Graphify CLI (`graphify`), tree-sitter, PyCG. |
| **Cognition Link** | [[_ONTOLOGY/COGNITION_FLOW.yaml|Cognition Flow Matrix]] |

---

## 3. Pipeline Lifecycle & Architecture

```text
       [[13-REPOSITORIES/13-REPOSITORIES|13-REPOSITORIES]]
               │
               ▼
┌───────────────────────────────────────────────┐
│     STAGE 07: CODE INTELLIGENCE PIPELINE       │
│                                               │
│  Operations: Parses repository source code into abstract s... │
└───────────────────────────────────────────────┘
               │
               ▼
       [[_PIPELINES/execution/README|08. Execution Pipeline]]
```

---

## 4. Connected Subsystems & Domains
- **Parent Stage Hub:** [[_PIPELINES/README|Pipelines Hub]]
- **Domain Gateway:** [[57-CODE-INTELLIGENCE/57-CODE-INTELLIGENCE|57-CODE-INTELLIGENCE]]
- **Autonomous Orchestration:** [[19-ORCHESTRATION/19-ORCHESTRATION|19-ORCHESTRATION]]
- **Master Control:** [[50-MASTER-CONTROL/50-MASTER-CONTROL|50-MASTER-CONTROL]]
- **Execution Tracking:** [[_PIPELINES/execution/EXECUTION_TRACKING|Execution Tracking Standard]]
