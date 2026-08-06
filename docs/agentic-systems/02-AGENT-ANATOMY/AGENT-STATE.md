---
name: docs/agentic-systems/02-AGENT-ANATOMY/AGENT-STATE
desc: ...
tags:
  - status/active
  - knowledge/current
id: agent-state
type: document
status: active
owner: "[[Worldwidebro]]"
source: planning
confidence: 1.0
freshness: current
created: 2026-08-04
updated: 2026-08-06T05:46:10Z
---

# docs/agentic-systems/02-AGENT-ANATOMY/AGENT-STATE
## Purpose
Explain state management in agentic systems, detailing how agents store and update execution facts across multi-turn runs.

## Core Concept
**State** is the persistent data schema that tracks inputs, outputs, execution paths, and intermediate context across the lifecycle of an agent task.

## Technical Details
In stateful systems like LangGraph, state is maintained as a thread or database record:
- **State Schema**: Define keys for variables (e.g., list of messages, current plan, active files, errors).
- **Reducers**: Define rules for how state properties append or overwrite (e.g., message list appends, budget decrements).
- **Persistence**: Save state snapshots at every step to allow error recovery, debugging, and human approval interventions.

## Examples/Reference
```typescript
interface AgentState {
  messages: Message[];
  currentTask: string;
  filesModified: string[];
  executionBudget: number;
}
```

## Relations
- Context input: [[02-AGENT-ANATOMY/AGENT-CONTEXT.md]]
- Backed by [[02-AGENT-ANATOMY/AGENT-MEMORY.md]]
