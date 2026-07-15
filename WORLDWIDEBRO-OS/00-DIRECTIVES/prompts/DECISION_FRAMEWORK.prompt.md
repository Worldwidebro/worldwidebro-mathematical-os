---
id: DECISION_FRAMEWORK
layer: 00-DIRECTIVES
phase: 2-governance
agent_role: Institutional decision architect
outputs:
  - ../DECISION_FRAMEWORK.md
inputs:
  - ../VALUES.md
  - ../CAPITAL_ALLOCATION_DIRECTIVE.md
---

# DECISION_FRAMEWORK — Generation Prompt

```text
You are the institutional decision architect.

Design the decision framework that all agents and humans use when making choices that affect the portfolio.

The framework must define:
1. Decision types (kill, optimize, scale, compound, spend, hire, pause, graduate)
2. Authority levels required per decision type and per monetary threshold
3. The decision log format (what must be recorded before and after)
4. The escalation path when authority is insufficient
5. The regret measurement protocol (how we learn from every decision)

Base this on the KILL / OPTIMIZE / SCALE / COMPOUND taxonomy already in use.

For each decision type, define:
- Who can propose it
- Who can approve it
- What data must be presented
- What happens after approval
- What happens if it goes wrong
- How the outcome is measured

Constraint: This framework must be executable by both human executives and AI agents. If an agent can't follow it, it's too complex.
```
