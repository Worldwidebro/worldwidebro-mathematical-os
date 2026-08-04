---
id: conditional-workflow
type: document
name: CONDITIONAL WORKFLOW
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

# CONDITIONAL WORKFLOW
## Purpose
Detail routing and branching in graph workflows using conditional logic.

## Core Concept
```
                          ┌──► Node A (Option 1)
        Node -> [Router] ─┼──► Node B (Option 2)
                          └──► Node C (Option 3)
```
Evaluating state values or LLM decisions to choose the next execution node.

## Technical Details
Conditional routing can be:
- **Deterministic**: Checked using code (e.g., if error rate > 5%, route to human rollback).
- **Cognitive**: Checked using LLM classifier (e.g., route query to either customer-support agent or tech-docs agent based on intent).

## Relations
- Under [[03-WORKFLOW-PATTERNS/WORKFLOW-DESIGN.md]]
