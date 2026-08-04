---
id: planner-worker-workflow
type: document
name: PLANNER WORKER WORKFLOW
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

# PLANNER WORKER WORKFLOW
## Purpose
Detail the Planner-Worker pattern for complex task decomposition and execution.

## Core Concept
A centralized **Planner** breaks down a large goal into structured sub-tasks, assigns them to individual **Workers** (specialist agents or sub-graphs), and merges the results.

```
       [Goal] ──► [Planner] ──► [Sub-task Checklist]
                                      │
                         ┌────────────┼────────────┐
                         ▼            ▼            ▼
                     Worker 1      Worker 2     Worker 3
                         │            │            │
                         └────────────┼────────────┘
                                      ▼
                               [Merge / Review]
```

## Technical Details
1. **Planner**: High-reasoning LLM (e.g., GPT-4o / Claude 3.5 Sonnet) focused on task breakdown.
2. **Workers**: Specialized agents with access to targeted tools.
3. **Task Tracking**: Shared checklist state (`task.md` model) where progress is updated.

## Relations
- Uses [[03-WORKFLOW-PATTERNS/LOOP-WORKFLOW.md]]
- Governs [[03-WORKFLOW-PATTERNS/SUPERVISOR-WORKFLOW.md]]
