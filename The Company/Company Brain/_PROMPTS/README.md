---
id: PORTAL-PROMPTS-HELPER-001
title: "_PROMPTS — Operational Prompt Stack & Awareness Protocols"
aliases: ["_PROMPTS", "_PROMPTS/README", "Prompt Stack", "Awareness Protocols"]
tags: ["prompts", "awareness", "cognitive-stack", "agents", "protocols"]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[INDEX]] | [[_PROMPTS/10_PRE-ACTION-AWARENESS|10_PRE-ACTION-AWARENESS]] | [[16-AGENTS/README|16-AGENTS]] | [[_MEMORY/MEMORY-OS|MEMORY-OS]]

# _PROMPTS — Operational Prompt Stack & Awareness Protocols

> **Authority:** Agentic Orchestration Control Plane ([[50-MASTER-CONTROL/50-MASTER-CONTROL|CP-016]])  
> **Master Pre-Action Protocol:** [[_PROMPTS/10_PRE-ACTION-AWARENESS|10_PRE-ACTION-AWARENESS.md]]  
> **Status:** 🟢 ACTIVE — 10-Stage Prompt Pipeline (2026-09-06)

---

## 1. The 10-Stage Cognitive Prompt Stack

The **`_PROMPTS/`** directory houses Company Brain's sequential prompt chain that prepares autonomous subagents, LLMs, and human operators for safe, context-aware execution:

| Step | Prompt Specification | Focus Area | File Gateway |
|:---:|---|---|---|
| **01** | `01_IDENTITY-AWARENESS.md` | Sovereign identity, role boundaries, and persona grounding | [[_PROMPTS/01_IDENTITY-AWARENESS|01_IDENTITY]] |
| **02** | `02_CURRENT-STATE-AWARENESS.md` | Hardware state, active branches, and real-time environment | [[_PROMPTS/02_CURRENT-STATE-AWARENESS|02_CURRENT-STATE]] |
| **03** | `03_MEMORY-RETRIEVAL.md` | 10-signal memory query against Qdrant vector space | [[_PROMPTS/03_MEMORY-RETRIEVAL|03_MEMORY-RETRIEVAL]] |
| **04** | `04_CONNECTION-REASONING.md` | Neo4j graph traversal and entity relationship tracing | [[_PROMPTS/04_CONNECTION-REASONING|04_CONNECTION-REASONING]] |
| **05** | `05_PATTERN-RECOGNITION.md` | Historical trajectory matching and anti-pattern alerts | [[_PROMPTS/05_PATTERN-RECOGNITION|05_PATTERN-RECOGNITION]] |
| **06** | `06_DECISION-MEMORY.md` | ADR lookup and precedent alignment before changes | [[_PROMPTS/06_DECISION-MEMORY|06_DECISION-MEMORY]] |
| **07** | `07_PROVENANCE-VERIFICATION.md` | Grade A–E evidence verification and source validation | [[_PROMPTS/07_PROVENANCE-VERIFICATION|07_PROVENANCE]] |
| **08** | `08_MEMORY-CONSOLIDATION.md` | Post-action insight extraction and episodic journaling | [[_PROMPTS/08_MEMORY-CONSOLIDATION|08_CONSOLIDATION]] |
| **09** | `09_MEMORY-DECAY.md` | Context compression, token pruning, and forgetting | [[_PROMPTS/09_MEMORY-DECAY|09_MEMORY-DECAY]] |
| **10** | `10_PRE-ACTION-AWARENESS.md` | **Mandatory 20-point pre-action checklist** before execution | [[_PROMPTS/10_PRE-ACTION-AWARENESS|10_PRE-ACTION]] |

---

## 2. Integration & Usage
- **Rule 1 Compliance**: Run `10_PRE-ACTION-AWARENESS.md` prior to any code generation or state modification.
- **Connected Agent Fleet**: [[16-AGENTS/README|16-AGENTS]] & [[_REGISTRIES/agents/README|Agents Registry]]
- **Cognitive Memory**: [[_MEMORY/MEMORY-OS|MEMORY-OS.md]]
