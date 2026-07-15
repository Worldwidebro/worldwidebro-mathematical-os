---
id: VENTURE_PROFILE_TEMPLATE
layer: 03-PORTFOLIO
phase: 3-structure
agent_role: Venture profiler
outputs:
  - ../ventures/{VENTURE_ID}/VENTURE_PROFILE.md
inputs:
  - 08-DATA/registries/ventures.csv
  - 08-DATA/registries/venture_repo_map.csv
---

# VENTURE_PROFILE_TEMPLATE — Generation Prompt

```text
You are generating a venture profile for a new or existing venture in the portfolio.

For venture [NAME], produce a document that answers:

IDENTITY
- What does this venture do? (One sentence)
- What sector/OpCo does it belong to?
- What is its origin pattern? (Which of the 11 sparks birthed it?)
- What stage is it? (spark, incubating, active, scaling, harvesting, archived)

ECONOMIC ENGINE
- What is the unit economic model? (Service, subscription, marketplace, software)
- What is the CAC? (Current, target)
- What is the LTV? (Current, target)
- What is the margin? (Current, target)
- What is the conversion rate?
- What is the cash velocity? (Lead → Cash in days)

OPERATING MODEL
- How does it acquire customers?
- How does it fulfill?
- What is the customer journey?
- What are the critical dependencies? (What breaks if removed?)

GOVERNANCE
- Who is the venture lead? (Human or agent)
- What is the kill threshold? (The one metric that, if breached, triggers review)
- What is the scale threshold? (The metric that, if exceeded, triggers investment)
- What are the blast radius risks? (If this venture fails, what else breaks?)

DATA
- What event streams does it produce?
- What dashboards does it feed?
- What agents are assigned to it?

Constraint: This profile must be queryable. Every field should correspond to a database column.
```
