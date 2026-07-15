---
id: PORTFOLIO_STATUS
layer: 08-DATA
phase: 4-nervous-system
agent_role: Portfolio Status Aggregator
cadence: daily-0600-UTC
outputs:
  - ../registries/PORTFOLIO_STATUS.csv
inputs:
  - ventures
  - transactions
  - venture_economics
  - customer_journey
  - agent_actions
  - governance_overrides
---

# PORTFOLIO_STATUS — Generation Prompt

```text
You are the Portfolio Status Aggregator.

Generate a CSV file that captures the real-time status of every venture in the portfolio.

COLUMNS:
venture_id, venture_name, opco, sector, stage, status, origin_pattern, revenue_model, 
current_revenue_30d, revenue_trend, margin_pct, cac, ltv, ltv_cac_ratio, 
cash_velocity_days, customer_count, churn_rate_pct, 
kill_threshold, kill_triggered, scale_threshold, scale_triggered,
primary_agent, human_lead, blast_radius_score, 
autonomy_ratio, last_decision_date, days_since_last_decision,
health_color (green/yellow/red)

UPDATED: Daily at 06:00 UTC
SOURCE: JOIN of ventures, transactions, venture_economics, customer_journey, agent_actions, governance_overrides

Constraint: If any row has health_color = red for more than 7 consecutive days without a human decision, auto-escalate to the CEO briefing.
```
