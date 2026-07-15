---
id: NORTH_STAR_METRICS
layer: 00-DIRECTIVES
phase: 1-constitution
agent_role: Institutional intelligence
outputs:
  - ../NORTH_STAR_METRICS.md
inputs:
  - 08-DATA/registries/ventures.csv
  - 08-DATA/registries/agents.csv
---

# NORTH_STAR_METRICS — Generation Prompt

```text
You are the institutional intelligence that defines what "winning" looks like.

Define the North Star Metrics for every level of the enterprise:

Holding Level (1 metric):
- The one number that, if it moves, tells us the entire institution is healthy

OpCo Level (per OpCo, 1 metric):
- The one number that matters for that sector's portfolio

Venture Level (per venture, 1 metric):
- The one number that determines if this venture survives or dies

Agent Level (per agent, 1 metric):
- The one number that proves the agent is earning its existence

For each metric, define:
- What it is (formula)
- Where it comes from (source table/event stream)
- The green/yellow/red thresholds
- The frequency of measurement
- Who is accountable for it

Constraint: If a metric doesn't drive a decision, delete it. No vanity metrics.
```
