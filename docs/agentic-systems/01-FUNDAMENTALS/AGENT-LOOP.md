---
name: docs/agentic-systems/01-FUNDAMENTALS/AGENT-LOOP
desc: ...
tags:
  - status/active
  - knowledge/current
id: agent-loop
type: document
status: active
owner: "[[Worldwidebro]]"
source: planning
confidence: 1.0
freshness: current
aliases:
  - "Cognitive Loop"
  - "Sense-Plan-Act Loop"
created: 2026-08-04
updated: 2026-08-06T05:46:10Z
---

# docs/agentic-systems/01-FUNDAMENTALS/AGENT-LOOP
## Purpose
Outline the fundamental control loop governing agentic action: OBSERVE -> THINK -> PLAN -> ACT -> OBSERVE.

## Core Concept
The **Agent Loop** is the repeating processor where external context is parsed, analyzed against goals, converted into executable steps, ran, and re-evaluated.

```
   ┌─── OBSERVE ◄───┐
   │        │       │
   │        ▼       │
   │     THINK      │
   │        │       │
   │        ▼       │
   │      PLAN      │
   │        │       │
   │        ▼       │
   └───── ACT ──────┘
```

## Technical Details
1. **Observe**: Retrieve input, system logs, environment state, and human feedback.
2. **Think**: Formulate a cognitive summary of current progress vs goal criteria.
3. **Plan**: Generate the immediate next step or sequence of tool calls.
4. **Act**: Execute the selected tools (e.g., run code, search web, call API).
5. **Repeat**: Loop back to observe changes in environment state.

## Examples/Reference
Our `agent_control_loop.py` script implements this exact sequence, logging inputs, outputs, and confidence intervals at each step to build audit trails.

## Relations
- Details [[01-FUNDAMENTALS/WHAT-IS-AN-AGENT.md]]
- Implemented in [[01-FUNDAMENTALS/REACT-PATTERN.md]]
