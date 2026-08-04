---
id: supervisor-workflow
type: document
name: SUPERVISOR WORKFLOW
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

# SUPERVISOR WORKFLOW
## Purpose
Detail the Supervisor pattern for managing multi-agent teams.

## Core Concept
A **Supervisor** agent acts as a manager, holding conversation state with the user and dynamically routing sub-steps to specialized child agents, acting as the single source of truth for execution flow.

## Technical Details
- The supervisor is a router node that has child agents mapped as tools.
- It calls child agents via handoffs or sub-graph executions.
- Child agents execute tasks and return outputs to the supervisor, who decides if the task is complete or if further delegation is required.

## Relations
- Alternative to [[03-WORKFLOW-PATTERNS/PLANNER-WORKER-WORKFLOW.md]]
- Implements [[06-MULTI-AGENT/AGENT-HANDOFFS.md]]
