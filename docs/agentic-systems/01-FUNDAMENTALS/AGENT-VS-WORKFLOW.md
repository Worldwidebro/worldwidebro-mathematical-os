---
name: docs/agentic-systems/01-FUNDAMENTALS/AGENT-VS-WORKFLOW
desc: ...
tags:
  - status/active
  - knowledge/current
id: agent-vs-workflow
type: document
status: active
owner: "[[Worldwidebro]]"
source: planning
confidence: 1.0
freshness: current
created: 2026-08-04
updated: 2026-08-06T05:46:10Z
---

# docs/agentic-systems/01-FUNDAMENTALS/AGENT-VS-WORKFLOW
## Purpose
Differentiate between flexible agentic loops and structured agentic workflows. Help developers choose the correct architecture based on predictability requirements.

## Core Concept
- **Agent**: High autonomy, low predictability. The AI decides *how* to solve a task.
- **Workflow**: Low autonomy, high predictability. The developer dictates the exact steps; the AI simply handles node processing or routing.

```
Structured Workflow:  A --> B --> [AI Classifier] --> C or D
Agentic Loop:         Goal --> [Think -> Act -> Observe] --(Loop until complete)--> Done
```

## Technical Details
Use a **Workflow** when:
1. The business logic requires a deterministic compliance path.
2. The blast radius of a wrong decision is extremely high (e.g., executing transactions).
3. The steps of execution are well-known and static.

Use an **Agent** when:
1. The path to the solution is highly dynamic and multi-layered.
2. You need long-horizon problem solving (e.g., finding and fixing a bug in an arbitrary codebase).
3. The environment requires tool utilization, exploration, and self-correction.

## Examples/Reference
*LangGraph* allows mixing both: defining a structured state graph (Workflow) while letting individual nodes operate with tool-calling loops (Agents).

## Relations
- Composes [[01-FUNDAMENTALS/WHAT-IS-AN-AGENT.md]]
- Leads to [[03-WORKFLOW-PATTERNS/WORKFLOW-DESIGN.md]]
