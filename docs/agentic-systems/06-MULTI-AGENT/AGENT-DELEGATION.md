---
name: docs/agentic-systems/06-MULTI-AGENT/AGENT-DELEGATION
desc: ...
tags:
  - status/active
  - knowledge/current
id: agent-delegation
type: document
status: active
owner: "[[Worldwidebro]]"
source: planning
confidence: 1.0
freshness: current
created: 2026-08-04
updated: 2026-08-06T05:46:10Z
---

# docs/agentic-systems/06-MULTI-AGENT/AGENT-DELEGATION
## Purpose
Explain the Delegation pattern, showing how parent agents spawn and monitor child agents without losing control.

## Core Concept
**Delegation** occurs when a parent agent assigns a sub-task to a child agent, suspends execution (or works on parallel tasks), and waits for the child to return the completed result.

## Technical Details
- The child agent's state is scoped strictly to the sub-task.
- The parent agent defines success and failure thresholds.
- Safe delegation requires budget boundaries to ensure sub-steps don't loop endlessly.

## Relations
- Under [[06-MULTI-AGENT/MULTI-AGENT-FUNDAMENTALS.md]]
- Implements [[03-WORKFLOW-PATTERNS/PLANNER-WORKER-WORKFLOW.md]]
