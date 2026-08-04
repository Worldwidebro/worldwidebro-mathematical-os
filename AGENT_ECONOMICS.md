---
title: Agent Economics & Cost Management
version: 1.0
date: 2026-07-30
companion: [[AGENT_SPEC.md]], [[AGENT_EVALUATION.md]], [[AGENT-BRACKET-STANDARD.md]]
---

# Agent Economics & Cost Management

**Purpose**: Track agent costs, optimize ROI, and manage budgets across 712 ventures. Enable cost-aware agent provisioning and retirement decisions.

---

## Cost Structure

### LLM Inference

```yaml
Model: Ollama qwen3:8b (local) or Claude API (remote)
Ollama: $0 (amortized hardware)
Claude: $0.003–0.015 per 1K tokens

Per-Task Estimates:
  Simple decision: $0.001–0.003
  Complex reasoning: $0.005–0.025
  Code generation: $0.025–0.100
```

### Tool Usage (APIs)

```yaml
CRM lookup: $0.01–0.05/call
Email send: $0.001–0.01/email
DB query: $0.001–0.10/query
Third-party API: $0.10–1.00/call

Per-Task Cost:
  Light (< 5 calls): $0.05–0.10
  Medium (5–20): $0.10–0.50
  Heavy (20+): $0.50–5.00
```

### Compute

```yaml
Claude Code: $0.001–0.01/minute
Supabase: $25/month + $0.50/10K reads
Neo4j: <$0.001/query (amortized)

Monthly by Usage:
  Idle: $25
  Active 8h/day: $50–100
  24h continuous: $100–500
```

### Storage

```yaml
Agent state: 1GB @ $0.10/GB = $0.10/month
Logs: 10GB @ $0.023/GB = $0.23/month
Embeddings: <$0.01/month

Annual per-agent: $4–15
```

---

## Cost Model Examples

### SalesAgent-CON-001

```yaml
[AGENT_ECONOMICS]
AGENT: SalesAgent-CON-001
PERIOD: 2026-07
STATUS: ACTIVE

Cost Breakdown:
  LLM Inference:
    1,250 queries * 300 tokens = $0.42
  Tool Usage:
    150 CRM @ $0.02 = $3.00
    300 emails @ $0.005 = $1.50
    500 DB queries @ $0.001 = $0.50
    Subtotal: $5.20
  Compute:
    Server (8h/day): $60
    Supabase: $27
    Subtotal: $87.00
  Storage: $0.33

Total Monthly: $514.41
Tasks: 1,250 completed (75 escalated)
Cost/Task: $0.41
Cost/Successful: $0.44
```

### EngineeringAgent-CON-001

```yaml
[AGENT_ECONOMICS]
AGENT: EngineeringAgent-CON-001
PERIOD: 2026-07

Cost Breakdown:
  LLM Inference:
    300 queries * 5,000 tokens (code heavy) = $22,500
  Tool Usage:
    GitHub API: $20
    Docker builds: $5
    Cloud deployments: $15
    Subtotal: $40
  Compute: $180
  Storage: $6

Total Monthly: $22,726
Tasks: 300 (code generation)
Cost/Task: $75.75

Budget: At limit
Recommendation: Hybrid (agent + human) or smarter routing
```

---

## Budget Allocation

```yaml
Total Monthly: $10,000

Allocation:
  Pilot Agents (10): $2,000 ($200 each)
  Production (30): $6,000 ($200 each)
  Reserve: $2,000

Per-Agent Budget: $200/month
  Increase to $500 after LEVEL_4+
  Reduce to $50 for monitoring-only

Enforcement:
  Hard cap: Agent stops at 100%
  Soft alert: 50%
  Escalation: 80% (director approval)
```

---

## ROI Calculation

```yaml
Formula: (Outcome Value - Cost) / Cost

SalesAgent-CON-001:
  Leads: 125 @ $50 value = $6,250
  Deals: 15 @ $5K value = $75,000
  Total: $81,250
  Cost: $514.41
  ROI: 157.9x ✅ EXCELLENT

EngineeringAgent-CON-001:
  Bug prevention: ~$10K/issue avg
  Deployment savings: 75h @ $50/h = $3,750
  Total: ~$25K
  Cost: $22,726
  ROI: 0.10x ⚠️ MARGINAL
  Action: Reduce scope or hybrid
```

---

## Cost Optimization

### Batch Processing

```yaml
Before: 100 real-time requests * $0.005 = $0.50
After: 1 batch inference = $0.05
Savings: 90%
Tradeoff: 1-hour latency vs real-time
```

### Hybrid Agent-Human

```yaml
Agent: 80% of tasks ($400/mo)
Human: 20% of complex ($200/mo)
Total: $600/mo
Benefit: Better accuracy + human judgment
```

### Tool Selection

```yaml
LLM-based: $0.50/email, 8/10 quality, 2–5s latency
Template-based: $0.001/email, 7/10 quality, <100ms
Recommendation: Templates for routine, LLM for complex
```

### Smart Filtering

```yaml
Before: 1,000 requests @ $0.10 = $100
After: 500 high-value @ $0.10 + 500 rules @ $0.01 = $55
Savings: 45%
```

---

## Storage

**Supabase**:
```sql
CREATE TABLE agent_economics (
  agent_id TEXT,
  period_start TIMESTAMP,
  period_end TIMESTAMP,
  llm_cost FLOAT,
  tool_cost FLOAT,
  compute_cost FLOAT,
  storage_cost FLOAT,
  total_cost FLOAT,
  tasks_completed INT,
  tasks_escalated INT,
  outcome_value FLOAT,
  roi FLOAT
);

CREATE TABLE agent_budget (
  agent_id TEXT,
  month TEXT,
  allocated FLOAT,
  spent FLOAT,
  remaining FLOAT
);
```

**Neo4j**:
```cypher
(agent:Agent)-[:HAS_ECONOMICS {cost_month, roi}]->(econ:Economics)
(agent)-[:BUDGET_ALLOCATED {amount, period}]->(budget:Budget)
```

---

## Retirement Decision

```yaml
Keep SalesAgent-CON-001?

Cost: $514/mo → $6,168/year
ROI: 157.9x
Revenue impact if retired: -$975K/year

Decision: KEEP
Net value: $969K/year
```

---

## Version History

- **v1.0 (2026-07-30)**: Agent economics model with cost tracking and ROI.

