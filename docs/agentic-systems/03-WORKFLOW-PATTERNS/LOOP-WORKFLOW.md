---
name: docs/agentic-systems/03-WORKFLOW-PATTERNS/LOOP-WORKFLOW
desc: ...
tags:
  - status/active
  - knowledge/current
id: loop-workflow
type: document
status: active
owner: "[[Worldwidebro]]"
source: planning
confidence: 1.0
freshness: current
created: 2026-08-04
updated: 2026-08-06T05:46:10Z
---

# docs/agentic-systems/03-WORKFLOW-PATTERNS/LOOP-WORKFLOW
## Purpose
Detail cyclic workflow logic, allowing loops for validation, self-correction, and retry policies.

## Core Concept
```
                 ┌──► [Execution Node] ◄──┐
        START ───┘           │            │ (Fail Validation)
                             ▼            │
                     [Evaluator / Check] ─┘
                             │
                             ▼ (Pass Validation)
                            END
```

## Technical Details
Used for optimization and validation cycles:
1. **Actor Node**: Generates code/reports.
2. **Evaluator Node**: Runs tests or audits the output.
3. **Condition**: If checks pass, exit. If failed, compile logs, update instructions, and route back to actor.
*Critical Constraint*: Always implement a `max_iterations` counter to prevent infinite run loops and cost overruns.

## Relations
- Composes [[03-WORKFLOW-PATTERNS/WORKFLOW-DESIGN.md]]
- Foundation for [[03-WORKFLOW-PATTERNS/PLANNER-WORKER-WORKFLOW.md]]
