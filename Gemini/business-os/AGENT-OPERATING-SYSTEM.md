# Agent Operating System: AI Employee Standard

This document standardizes the specifications, tools, authorities, and performance loops for all AI employees inside **Worldwidebro Holdings**.

---

## 1. AI Employee Standard Definition

Every agent is defined using a structured profile:

```yaml
Agent Profile:
  Name: [Role Name]
  Job Description: [SOP Responsibilities]
  Authority Level: [1, 2, or 3]
  Tools: [Allowed APIs, CLI execution privileges]
  Memory Context: [Qdrant vector collection path]
  KPIs: [Performance metrics targets]
  Escalation Rules: [Thresholds triggering human reviews]
  Compensation Equivalent: [Token API expense budget]
```

---

## 2. Standardized Roles & Profiles

### network-operations
- **Job Description**: Coordinator of delegation flows across the 15 sectors.
- **Authority**: Level 2 (Manager).
- **Tools**: Neo4j Browser, Git CLI.
- **Memory Context**: `network_telemetry` vector collection.
- **KPIs**: Average delegation velocity > 50 runs/week, SLA breach < 5%.
- **Escalation Rules**: Escalate to CEO if queue latency exceeds 24 hours.
- **Compensation Equivalent**: $50.00/month API token budget.

### capital-allocation
- **Job Description**: Financial controller and portfolio treasurer.
- **Authority**: Level 2 (Manager).
- **Tools**: Supabase Ledger SQL, PyPortfolioOpt library.
- **Memory Context**: `portfolio_cash_flows` vector collection.
- **KPIs**: Portfolio ROI > 25% annually, rebalancing precision.
- **Escalation Rules**: Escalate capital requests > $50,000 to CFO.
- **Compensation Equivalent**: $30.00/month API token budget.

---

## 3. Performance Review Loop

At 18:00 EST daily, the **Performance Analytics** agent runs the evaluation sequence:
1. Fetch the agent's task log from Supabase.
2. Calculate completion rate, error frequency, and token expense.
3. If performance falls below 85% for 3 consecutive days, invoke `SkillOpt` to run fine-tuning or update prompt templates.
