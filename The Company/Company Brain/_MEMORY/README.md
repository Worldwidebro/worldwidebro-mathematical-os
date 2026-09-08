---
id: PORTAL-MEMORY-HELPER-001
title: "_MEMORY — Four-Tier Memory Operating System Gateway"
aliases: ["_MEMORY", "_MEMORY/README", "Memory OS Hub", "Cognitive Memory"]
tags: ["memory", "qdrant", "redis", "episodic", "retrieval", "cache"]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[INDEX]] | [[10-MEMORY/10-MEMORY|10-MEMORY Domain]] | [[_MEMORY/MEMORY-OS|MEMORY-OS]] | [[CLAUDE]] | [[REALITY]]

# _MEMORY — Four-Tier Memory Operating System Gateway

> **Authority:** Memory & Cognitive Control Plane ([[50-MASTER-CONTROL/50-MASTER-CONTROL|CP-010]])  
> **Master Architecture:** [[_MEMORY/MEMORY-OS|MEMORY-OS.md]] & [[_MEMORY/MEMORY-ARCHITECTURE|MEMORY-ARCHITECTURE.md]]  
> **Active Collections Registry:** [[_MEMORY/MEMORY-REGISTRY.json]]  
> **Status:** 🟢 ACTIVE — Operational Memory Hub (2026-09-06)

---

## 1. The Four-Tier Memory Model

Company Brain manages cognitive state across four distinct operational memory layers:
1. **Working Memory (Tier 1)**: In-session LLM context window + Redis key-value cache (`:6379`).
2. **Episodic Memory (Tier 2)**: Task execution history, session summaries, and audit receipts.
3. **Semantic Memory (Tier 3)**: Vector embeddings in Qdrant (`:6333`) across 1536/3072-dim models.
4. **Procedural Memory (Tier 4)**: Modular agent skills in `.agents/skills/` and executable runbooks.

---

## 2. Operational Memory Documents (16 Files)

| Document | Purpose | File Gateway |
|---|---|---|
| **`MEMORY-OS.md`** | Master Memory Operating System specification | [[_MEMORY/MEMORY-OS|MEMORY-OS.md]] |
| **`MEMORY-ARCHITECTURE.md`** | Four-tier architecture and storage topology | [[_MEMORY/MEMORY-ARCHITECTURE|MEMORY-ARCHITECTURE.md]] |
| **`MEMORY-MODEL.md`** | Mathematical cognition and retrieval model | [[_MEMORY/MEMORY-MODEL|MEMORY-MODEL.md]] |
| **`MEMORY-REGISTRY.json`** | Machine-readable registry of active vector collections | `_MEMORY/MEMORY-REGISTRY.json` |
| **`MEMORY-RETRIEVAL.md`** | 10-signal hybrid retrieval engine algorithms | [[_MEMORY/MEMORY-RETRIEVAL|MEMORY-RETRIEVAL.md]] |
| **`MEMORY-AWARENESS.md`** | Pre-action memory awareness protocols | [[_MEMORY/MEMORY-AWARENESS|MEMORY-AWARENESS.md]] |
| **`MEMORY-CAUSAL.md`** | Causal graphs and temporal dependency tracking | [[_MEMORY/MEMORY-CAUSAL|MEMORY-CAUSAL.md]] |
| **`MEMORY-CONSOLIDATION.md`**| Daily sleep/consolidation offline processing loop | [[_MEMORY/MEMORY-CONSOLIDATION|MEMORY-CONSOLIDATION.md]] |
| **`MEMORY-CONTRADICTIONS.md`**| Conflict detection and automated resolution rules | [[_MEMORY/MEMORY-CONTRADICTIONS|MEMORY-CONTRADICTIONS.md]] |
| **`MEMORY-DECAY.md`** | Ebbinghaus forgetting curves and eviction policies | [[_MEMORY/MEMORY-DECAY|MEMORY-DECAY.md]] |
| **`MEMORY-LIFECYCLE.md`** | End-to-end memory object state transitions | [[_MEMORY/MEMORY-LIFECYCLE|MEMORY-LIFECYCLE.md]] |
| **`MEMORY-POLICY.md`** | Privacy, data retention, and memory governance | [[_MEMORY/MEMORY-POLICY|MEMORY-POLICY.md]] |
| **`MEMORY-PROVENANCE.md`** | Origin tracking and cryptographic proof chains | [[_MEMORY/MEMORY-PROVENANCE|MEMORY-PROVENANCE.md]] |
| **`MEMORY-QUALITY.md`** | Signal-to-noise ratio and retrieval quality metrics | [[_MEMORY/MEMORY-QUALITY|MEMORY-QUALITY.md]] |
| **`MEMORY-RELATIONSHIPS.md`**| Cross-memory links and entity associations | [[_MEMORY/MEMORY-RELATIONSHIPS|MEMORY-RELATIONSHIPS.md]] |
| **`MEMORY-TEMPORAL.md`** | Valid-time and transaction-time temporal logging | [[_MEMORY/MEMORY-TEMPORAL|MEMORY-TEMPORAL.md]] |

---

## 3. Infrastructure & Upstream Connections
- **Vector Database**: Qdrant (`http://100.87.214.70:6333`) via [[_INFRASTRUCTURE/README]]
- **Prompt Integration**: [[_PROMPTS/03_MEMORY-RETRIEVAL]] & [[_PROMPTS/10_PRE-ACTION-AWARENESS]]
- **Knowledge Core**: [[08-KNOWLEDGE-GRAPH/README]] & [[09-KNOWLEDGE/README]]
