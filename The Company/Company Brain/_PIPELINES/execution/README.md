---
id: PIP-STAGE-08
title: "Execution Pipeline (Stage 08)"
aliases: ['Execution Pipeline', 'Stage 08 Execution', '_PIPELINES/execution']
tags: ['pipeline', 'execution', 'fractal', 'agents', 'loops', 'herdr']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[_PIPELINES/README|Pipelines Hub]] | [[22-EXECUTION/22-EXECUTION|22-EXECUTION]] | [[19-ORCHESTRATION/19-ORCHESTRATION|19-ORCHESTRATION]] | [[REALITY]]

# Execution Pipeline (Stage 08)

> **Authority:** Orchestration Control Plane (CP-019)  
> **Cognition Flow Phase:** `Stage 08: ACTUATION_AND_ACTION`  
> **Target Domain:** [[22-EXECUTION/22-EXECUTION|22-EXECUTION]]  
> **Status:** ACTIVE — Standardized & Verified (2026-09-06)

---

## 1. Pipeline Overview
The **Execution Pipeline** serves as stage 08 of Company Brain's 10-stage cognitive data pipeline.

Dispatches approved tactical plans into autonomous agent trees via Fractal, executes terminal commands inside sandboxes, controls git worktrees, and tracks loop lifecycles.

---

## 2. Data Contracts & Operational Flow

| Specification | Details |
|:---|:---|
| **Input Data** | Execution plans, code diffs, command directives, autonomy level gates (L1/L2/L3). |
| **Output Data** | Git commits, deployed containers, API responses, execution tracking records (`EXC-*`). |
| **Primary Tooling** | Fractal 1.2.0 (`plasma-fractal`), herdr session manager, git worktrees, Docker contexts. |
| **Cognition Link** | [[_ONTOLOGY/COGNITION_FLOW.yaml|Cognition Flow Matrix]] |

---

## 3. Pipeline Lifecycle & Architecture

```text
       [[_PIPELINES/reasoning/README|06. Reasoning Pipeline]]
               │
               ▼
┌───────────────────────────────────────────────┐
│     STAGE 08: EXECUTION PIPELINE       │
│                                               │
│  Operations: Dispatches approved tactical plans into auton... │
└───────────────────────────────────────────────┘
               │
               ▼
       [[_PIPELINES/learning/README|09. Learning Pipeline]]
```

---

## 4. Connected Subsystems & Domains
- **Parent Stage Hub:** [[_PIPELINES/README|Pipelines Hub]]
- **Domain Gateway:** [[22-EXECUTION/22-EXECUTION|22-EXECUTION]]
- **Autonomous Orchestration:** [[19-ORCHESTRATION/19-ORCHESTRATION|19-ORCHESTRATION]]
- **Master Control:** [[50-MASTER-CONTROL/50-MASTER-CONTROL|50-MASTER-CONTROL]]
- **Execution Tracking:** [[_PIPELINES/execution/EXECUTION_TRACKING|Execution Tracking Standard]]
