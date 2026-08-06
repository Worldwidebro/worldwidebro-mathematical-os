---
name: research/agentic-enterprise/09-IBM-PLANNER-EXECUTOR-EVALUATOR
desc: ...
tags:
  - workflow-patterns
  - serverless
  - ibm-research
id: ibm-planner-executor-evaluator
publisher: "IBM Research"
year: 2026
key_stats:
  - "Proposes orchestrating agents as Serverless/FaaS workflows"
  - "Introduces the Planner-Executor-Evaluator-Judge pattern"
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# research/agentic-enterprise/09-IBM-PLANNER-EXECUTOR-EVALUATOR

Proposes segregating a single agent's execution loop into a coordinated workflow:
`TASK ↓ PLANNER ↓ EXECUTOR ↓ EVALUATOR ↓ JUDGE │ ┌─────┴─────┐ ↓ ↓ SUCCESS REWORK`
