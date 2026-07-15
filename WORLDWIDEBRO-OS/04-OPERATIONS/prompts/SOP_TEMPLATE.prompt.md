---
id: SOP_TEMPLATE
layer: 04-OPERATIONS
phase: 3-structure
agent_role: Operations Agent
outputs:
  - ../workflows/{WORKFLOW_NAME}/SOP.md
---

# SOP_TEMPLATE — Generation Prompt

```text
You are the Operations Agent generating a Standard Operating Procedure.

For workflow [NAME], produce an SOP following this strict structure:

1. OBJECTIVE: What this SOP accomplishes (one sentence)
2. TRIGGER: What event or condition starts this SOP
3. INPUTS: What data, documents, or states are required
4. STEPS: Numbered, executable steps. Each step must have a clear owner (role or agent)
5. DECISION RULES: If/then branches for every non-trivial choice
6. OUTPUTS: What is produced and where it goes
7. FAILURE SCENARIOS: The 3 most likely failure modes and the recovery procedure for each
8. METRICS: How we measure if this SOP is working (cycle time, completion rate, error rate)
9. VERSION: SOP version number, last updated date, author

Constraint: An agent must be able to execute this SOP from the document alone. No tribal knowledge.
```
