---
id: DOCS-ARCH-001
title: "Company Brain Master System Architecture"
aliases: ["_DOCS/architecture", "Master Architecture Specification"]
tags: [architecture, system-design, control-planes, pipelines, layers]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[INDEX]] | [[ARCHITECTURE|ARCHITECTURE.md]] | [[50-MASTER-CONTROL/50-MASTER-CONTROL|Master Control]] | [[56-ENGINEERING/README|56-ENGINEERING]]

# Company Brain Master System Architecture

> **Authority:** System Architecture & Infrastructure Control Plane ([[CP-027]])  
> **Master Operating Contract:** [[ANTIGRAVITY.md]]  
> **Live Runtime State:** [[CLAUDE.md]]  
> **Location:** `_DOCS/architecture.md`  
> **Status:** 🟢 ACTIVE — Canonical Reference (2026-09-06)

---

## 1. Architectural Foundations
Company Brain is an enterprise-scale distributed cognitive operating system coordinating 700+ ventures, 893 owned repositories, 903 starred capabilities, and local-first AI inference across Apple Silicon hardware.

```text
┌─────────────────────────────────────────────────────────────────────────┐
│                       00-CONSTITUTION & RESPECT                         │
│           Ethical Boundaries • Agency • Governance Constraints          │
└────────────────────────────────────┬────────────────────────────────────┘
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    SEVEN OPERATIONAL PLANES (CP-001 to CP-035)           │
│   Governance • Data • Cognition • Execution • Observation • Evolution   │
└────────────────────────────────────┬────────────────────────────────────┘
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│               TEN-STAGE COGNITIVE PIPELINE (_PIPELINES/)                │
│ Ingestion → Processing → Transformation → Indexing → Retrieval →        │
│ Reasoning → Code Intel → Execution → Learning → Observability           │
└────────────────────────────────────┬────────────────────────────────────┘
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                 50 NUMBERED OPERATING DOMAINS (00 to 50)                │
│ 00-CONSTITUTION ... 14-CAPABILITIES ... 23-VENTURES ... 50-MASTER-CTRL  │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Core Architectural References
- **Master Contract:** [[ANTIGRAVITY.md]] (45 mandatory engineering & agent rules).
- **Executive Orientation:** [[STARTHERE.md]] & [[INDEX.md]].
- **Runtime Infrastructure:** [[CLAUDE.md]] (Mac Studio `100.87.214.70`, Tailscale mesh, OmniRoute `:20128`, Neo4j `:7687`, Qdrant `:6333`).
- **Master Control Hub:** [[50-MASTER-CONTROL/50-MASTER-CONTROL|50-MASTER-CONTROL]] & [[50-MASTER-CONTROL/SEVEN_PLANES|SEVEN_PLANES.md]].
- **Engineering Domain:** [[56-ENGINEERING/README|56-ENGINEERING Hub]] & [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING Gateway]].
- **Evaluation & Benchmarking:** [[42-EVALUATION/README|42-EVALUATION Hub]].
- **Blueprints & Templates:** [[_TEMPLATES/README|Templates Gallery]].
- **Canonical Registries:** [[_REGISTRIES/CANONICAL/REPOSITORY_REGISTRY.yaml]] & [[_REGISTRIES/VENTURE_REGISTRY.yaml]].
