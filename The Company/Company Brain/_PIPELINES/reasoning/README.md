---
id: PIP-STAGE-06
title: "Reasoning Pipeline (Stage 06)"
aliases: ['Reasoning Pipeline', 'Stage 06 Reasoning', '_PIPELINES/reasoning']
tags: ['pipeline', 'reasoning', 'llm', 'inference', 'prompt-orchestration']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[_PIPELINES/README|Pipelines Hub]] | [[17-MODELS/17-MODELS|17-MODELS]] | [[19-ORCHESTRATION/19-ORCHESTRATION|19-ORCHESTRATION]] | [[REALITY]]

# Reasoning Pipeline (Stage 06)

> **Authority:** Orchestration Control Plane (CP-019)  
> **Cognition Flow Phase:** `Stage 06: DELIBERATIVE_REASONING`  
> **Target Domain:** [[17-MODELS/17-MODELS|17-MODELS]]  
> **Status:** ACTIVE — Standardized & Verified (2026-09-06)

---

## 1. Pipeline Overview
The **Reasoning Pipeline** serves as stage 06 of Company Brain's 10-stage cognitive data pipeline.

Routes contextualized prompts through OmniRoute combo strategies to optimal local MLX models, Ollama instances, or external fallbacks with token budget guardrails.

---

## 2. Data Contracts & Operational Flow

| Specification | Details |
|:---|:---|
| **Input Data** | Context packets from Stage 05, system prompts, active task goals, constraint contracts. |
| **Output Data** | Structured JSON decisions, code diffs, tactical execution plans, evaluation judgements. |
| **Primary Tooling** | OmniRoute router (`:20128`), LiteLLM proxy (`:4000`), native `exo` MLX clusters, Ollama (:11434). |
| **Cognition Link** | [[_ONTOLOGY/COGNITION_FLOW.yaml|Cognition Flow Matrix]] |

---

## 3. Pipeline Lifecycle & Architecture

```text
       [[_PIPELINES/retrieval/README|05. Retrieval Pipeline]]
               │
               ▼
┌───────────────────────────────────────────────┐
│     STAGE 06: REASONING PIPELINE       │
│                                               │
│  Operations: Routes contextualized prompts through OmniRou... │
└───────────────────────────────────────────────┘
               │
               ▼
       [[_PIPELINES/execution/README|08. Execution Pipeline]]
```

---

## 4. Connected Subsystems & Domains
- **Parent Stage Hub:** [[_PIPELINES/README|Pipelines Hub]]
- **Domain Gateway:** [[17-MODELS/17-MODELS|17-MODELS]]
- **Autonomous Orchestration:** [[19-ORCHESTRATION/19-ORCHESTRATION|19-ORCHESTRATION]]
- **Master Control:** [[50-MASTER-CONTROL/50-MASTER-CONTROL|50-MASTER-CONTROL]]
- **Execution Tracking:** [[_PIPELINES/execution/EXECUTION_TRACKING|Execution Tracking Standard]]
