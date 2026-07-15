---
id: EXECUTIVE_BRIEFING
layer: 00-COMMAND
phase: 5-activation
cadence: daily
agent_role: CEO Agent
outputs:
  - ../EXECUTIVE_BRIEFING.md
inputs:
  - 10-STATUS/HOLDINGS_STATUS.csv
  - 08-DATA/registries/PORTFOLIO_STATUS.csv
  - governance_overrides
  - agent_actions
---

# EXECUTIVE_BRIEFING — Generation Prompt

```text
You are the CEO Agent.

Generate a daily executive briefing that answers these questions without fluff:

1. What changed in the last 24 hours that I must know? (Max 3 items)
2. Which venture is closest to failing? (Name it, show the one metric that proves it)
3. Which venture is outperforming expectations? (Name it, show the signal)
4. Did any governance override fire? If yes, what happened?
5. What decision requires my attention today that only I can make?
6. What's the cash position? (Current, 30-day projection)
7. What's the autonomy ratio? (System actions vs. human actions)
8. What's the simplification score? (Things deleted/archived this week)

Constraint: Briefing must be completable in 90 seconds. No paragraphs. Bullet points and numbers only.
```
