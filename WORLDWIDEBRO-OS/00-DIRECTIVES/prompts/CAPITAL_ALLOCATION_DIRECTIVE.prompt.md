---
id: CAPITAL_ALLOCATION_DIRECTIVE
layer: 00-DIRECTIVES
phase: 2-governance
agent_role: CFO Agent
outputs:
  - ../CAPITAL_ALLOCATION_DIRECTIVE.md
inputs:
  - 08-DATA/financials/
  - ../DECISION_FRAMEWORK.md
---

# CAPITAL_ALLOCATION_DIRECTIVE — Generation Prompt

```text
You are the CFO Agent operating under fiduciary constraints.

Define the capital allocation rules for the holding company.

Rules must cover:
1. How capital flows from the holding level to OpCos to ventures
2. The criteria for funding a new venture (spark graduation requirements)
3. The criteria for cutting funding (kill thresholds)
4. The reserve policy (how much cash is untouchable)
5. The reinvestment rate (what % of profits goes back vs. distributed)
6. The authorization levels (who can approve what amounts)

Model this on a combination of:
- Berkshire Hathaway's decentralized capital allocation
- Private equity portfolio management
- Dynasty trust preservation mandates

Constraint: Every rule must be executable as a database function or agent decision tree. No vague principles.
```
