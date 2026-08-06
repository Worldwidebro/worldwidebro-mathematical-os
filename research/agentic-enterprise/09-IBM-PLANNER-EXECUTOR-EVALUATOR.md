---
id: ibm-planner-executor-evaluator
name: "Towards Orchestrating Agentic Applications as FaaS Workflows"
publisher: "IBM Research"
year: 2026
key_stats:
  - "Proposes orchestrating agents as Serverless/FaaS workflows"
  - "Introduces the Planner-Executor-Evaluator-Judge pattern"
tags:
  - workflow-patterns
  - serverless
  - ibm-research
---

# Towards Orchestrating Agentic Applications (IBM Research 2026)

Proposes segregating a single agent's execution loop into a coordinated workflow:
`TASK ↓ PLANNER ↓ EXECUTOR ↓ EVALUATOR ↓ JUDGE │ ┌─────┴─────┐ ↓ ↓ SUCCESS REWORK`
