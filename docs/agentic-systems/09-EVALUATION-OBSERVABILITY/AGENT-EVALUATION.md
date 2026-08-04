---
id: agent-evaluation
type: document
name: AGENT EVALUATION
status: active
owner: "[[Worldwidebro]]"
created: 2026-08-04
updated: 2026-08-04
source: planning
confidence: 1.0
freshness: current
aliases:
  - "Agent Evals"
  - "Trajectory Scoring"
tags:
  - status/active
  - knowledge/current
---

# AGENT EVALUATION
## Purpose
Outline evaluation methodologies for agent performance, planning quality, and tool selection accuracy.

## Core Concept
Evals ensure system changes don't cause regressions. Agent performance is evaluated using deterministic checks, unit test results, and LLM-as-a-judge scorers.

## Technical Details
Key evaluation criteria:
- **Goal Completion**: Does the final output solve the target prompt?
- **Trajectory Efficiency**: Did the agent use the minimum number of tool steps, or did it enter redundant loops?
- **Tool Correctness**: Did it pass valid JSON schemas and arguments to tools?
- **Cost/Latency**: Did it execute within the allowed budget and time boundaries?

## Relations
- Feeds [[09-EVALUATION-OBSERVABILITY/TRACING.md]]
- Relates to [[09-EVALUATION-OBSERVABILITY/TASK-EVALUATION.md]]
