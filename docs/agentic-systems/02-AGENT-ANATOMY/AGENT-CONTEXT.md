---
name: docs/agentic-systems/02-AGENT-ANATOMY/AGENT-CONTEXT
desc: ...
tags:
  - status/active
  - knowledge/current
id: agent-context
type: document
status: active
owner: "[[Worldwidebro]]"
source: planning
confidence: 1.0
freshness: current
created: 2026-08-04
updated: 2026-08-06T05:46:10Z
---

# docs/agentic-systems/02-AGENT-ANATOMY/AGENT-CONTEXT
## Purpose
Define how short-term context is engineered, updated, and managed to prevent context window overflow while maximizing task relevance.

## Core Concept
**Context** is the set of inputs, instructions, files, and system parameters actively fed into the LLM context window during a single loop step.

## Technical Details
Context management requires:
1. **Dynamic Assembly**: Injecting system instructions, target workspace, open file buffers, and recent shell outputs.
2. **Context Compaction**: Summarizing long command logs, trimming repetitive stack traces, and retrieving only the relevant document chunks.
3. **Ontology Mapping**: Structuring context using standard metadata tags to allow the agent to traverse related systems.

## Relations
- Restricts [[02-AGENT-ANATOMY/AGENT-STATE.md]]
- Feed loop: [[01-FUNDAMENTALS/AGENT-LOOP.md]]
