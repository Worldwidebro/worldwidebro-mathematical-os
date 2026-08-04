---
title: Agent Evaluation & KPI Framework
version: 1.0
date: 2026-07-30
companion: [[AGENT_SPEC.md]], [[AGENT_LIFECYCLE.md]], [[AGENT-BRACKET-STANDARD.md]]
---

# Agent Evaluation & KPI Framework

**Purpose**: Standardize how agent performance is measured, tracked, and improved. Enable data-driven decisions about autonomy, permissions, and retirement.

---

## Core KPIs

### Success Rate

```yaml
Definition: % of tasks completed without escalation
Formula: (completed - escalated) / total_tasks
Target: ≥ 95%
Warning: < 90%
Alert: < 80%
```

### Response Latency

```yaml
Metrics: p50, p95, p99
Target: p99 < 2s
Warning: p99 > 3s
Alert: p99 > 5s
```

### Cost Efficiency

```yaml
Formula: (API + tools + LLM) / tasks_completed
Target: < $0.50/task
Budget: $1000/month per agent
Alert: > 50% budget by week 2
```

### Accuracy

```yaml
Definition: % correct decisions vs ground truth
Target: ≥ 90%
Warning: 80-89%
Alert: < 80%
Method: A/B testing, human review, benchmarking
```

### Confidence Score

```yaml
Definition: Agent self-reported certainty (0.0–1.0)
Target: > 0.75 for production
Interpretation:
  0.0–0.5: Escalate
  0.5–0.75: Monitor
  0.75–1.0: Proceed autonomous
```

### Drift Detection

```yaml
Definition: Performance degradation over time
Alert: Success rate drop > 5%, Accuracy drop > 10%
Cadence: Weekly
Action: Trigger TRAINING stage if drift detected
```

---

## Evaluation Dimensions

**Operational**: Uptime, response time, throughput, error rate  
**Business**: ROI, lead quality, deal velocity, customer satisfaction  
**Technical**: API reliability, data quality, security, compliance  
**Safety**: Escalation rate, false positives, risk detection, explainability

---

## Weekly Evaluation Cycle

**Monday 9:00 AM**:
1. Collect metrics (last 7 days from Supabase)
2. Calculate KPIs and compare to previous week
3. Triage alerts (red = P0, yellow = scheduled)
4. Root cause analysis if needed
5. Document findings in agent_evaluation_log
6. Send Slack summary

---

## Evaluation Events

**Daily (Automated)**:
- Log metrics every 6 hours
- Real-time error alerts
- Budget overflow alerts

**Weekly (Manual)**:
- KPI calculation
- Accuracy spot-check (10 random tasks)
- Drift detection
- Cost breakdown

**Monthly (Director Review)**:
```yaml
[AGENT_EVALUATION]
AGENT: SalesAgent-CON-001
PERIOD: 2026-07-01 to 2026-07-31
EVALUATION_DATE: 2026-08-01

Scores:
  - Success Rate: 94% ✅
  - Latency p99: 1.8s ✅
  - Cost/Task: $0.32 ✅
  - Accuracy: 91% ✅
  - Confidence: 0.82 ✅

Grade: A
Recommendation: Increase to LEVEL_4
```

**Quarterly (Executive)**: Trends, ROI, capacity planning

---

## Storage

**Supabase**:
```sql
CREATE TABLE agent_metrics (
  agent_id TEXT,
  timestamp TIMESTAMP,
  success_rate FLOAT,
  latency_p50 FLOAT,
  latency_p99 FLOAT,
  cost_usd FLOAT,
  accuracy FLOAT,
  confidence FLOAT
);

CREATE TABLE agent_evaluation_log (
  agent_id TEXT,
  evaluation_date TIMESTAMP,
  period_start TIMESTAMP,
  period_end TIMESTAMP,
  scores JSONB,
  overall_grade TEXT,
  recommendation TEXT,
  evaluated_by TEXT
);
```

**Neo4j**:
```cypher
(agent:Agent)-[:EVALUATED_ON {timestamp, grade}]->(eval:Evaluation)
(eval)-[:IDENTIFIED_DRIFT]->(:Anomaly)
(agent)-[:REQUIRES_RETRAINING {reason}]->(:Task)
```

---

## Action Thresholds

| Metric | Green | Yellow | Red |
|--------|-------|--------|-----|
| Success Rate | ≥95% | 85-94% | <85% |
| Error Rate | <2% | 2-5% | >5% |
| Latency p99 | <2s | 2-5s | >5s |
| Cost/Task | <$0.40 | $0.40-0.60 | >$0.60 |
| Accuracy | ≥90% | 80-89% | <80% |
| Confidence | >0.75 | 0.60-0.75 | <0.60 |

Red triggers immediate investigation + remediation.

---

## Version History

- **v1.0 (2026-07-30)**: Agent evaluation framework with weekly/monthly cadence.

