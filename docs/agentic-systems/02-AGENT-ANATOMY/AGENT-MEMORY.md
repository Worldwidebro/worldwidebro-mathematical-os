---
id: agent-memory
type: document
name: AGENT MEMORY
status: active
owner: "[[Worldwidebro]]"
created: 2026-08-04
updated: 2026-08-04
source: planning
confidence: 1.0
freshness: current
tags:
  - status/active
  - knowledge/current
---

# AGENT MEMORY
## Purpose
Establish the technical division of memory (short-term, long-term, episodic, semantic) in autonomous agent architectures.

## Core Concept
An agent requires different memory layers to maintain task-specific context (short-term) and remember historical outcomes to improve performance over time (long-term).

```
Short-Term Memory (Context Window, Redux State)
Long-Term Memory:
 ├── Episodic Memory (Database logs of past tasks, trial outcomes)
 └── Semantic Memory (Knowledge Graph, Vector embeddings, Ontologies)
```

## Technical Details
- **Short-Term**: Kept in-memory or in Postgres threads. Truncated or summarized when limits are reached.
- **Episodic**: Logged database trials where the outcome (success/fail) is indexed, letting the agent search past runs before tackling a similar goal.
- **Semantic**: Managed via vector databases (e.g., Qdrant) and graph databases (Neo4j) to map permanent business domains.

## Relations
- Detail: [[04-MEMORY-KNOWLEDGE/MEMORY-ARCHITECTURE.md]]
- Utilized in [[07-REASONING-DECISION/SELF-REFLECTION.md]]
