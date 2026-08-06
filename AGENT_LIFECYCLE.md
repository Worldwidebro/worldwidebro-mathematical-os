---
name: AGENT_LIFECYCLE
title: Agent Lifecycle Management
desc: ...
version: 1.0
date: 2026-07-30
companion: [[AGENT_SPEC.md]], [[AGENT_PERMISSIONS.md]], [[AGENT-BRACKET-STANDARD.md]]
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# Agent Lifecycle Management

**Purpose**: Define stages from agent creation through deployment, updates, and retirement. Enable reproducible agent provisioning across 712 ventures.

---

## Lifecycle Stages

### Stage 1: Creation (T+0)

```yaml
[AGENT_LIFECYCLE]
STAGE: CREATION
AGENT: SalesAgent-CON-001
ACTION: PROVISION
STATUS: CREATED
TEMPLATE: sales_agent_v2.yaml

Inputs:
  - venture_id: CON-001
  - agent_type: SALES_AGENT
  - domain: construction
  - initial_tools: [crm_lookup, lead_create, email_send]

Outputs:
  - agent_id: SA-CON-001-v1
  - config_url: /agents/SA-CON-001-v1.yaml
  - audit_log: created_2026-07-30_08:00:00Z
```

Checklist: Generate agent_id, load spec template, assign initial permissions (LEVEL_0), register in Neo4j, initialize memory storage, log creation event to Supabase.

---

### Stage 2: Training (T+1 day)

Agent learns venture-specific context through supervised feedback.

```yaml
[AGENT_LIFECYCLE]
STAGE: TRAINING
AGENT: SalesAgent-CON-001
ACTION: LEARN_FROM_FEEDBACK
STATUS: IN_PROGRESS
ITERATIONS: 5
```

**Success Criteria**: Accuracy ≥ 85%, Latency ≤ 2s, Confidence ≥ 0.75, Zero data loss.

---

### Stage 3: Approval (T+2-4 days)

Human director reviews agent and approves for production.

```yaml
Required Sign-Off:
  - Sales Manager
  - Finance
  - CEO: Final authorization

Approval Storage: Neo4j
  (agent:Agent)-[:APPROVED_BY]->(director:Director)
  {timestamp, scope, expiry_date}
```

---

### Stage 4: Deployment (T+5 days)

Agent goes live to production.

```yaml
[AGENT_LIFECYCLE]
STAGE: DEPLOYMENT
AGENT: SalesAgent-CON-001
ACTION: DEPLOY_TO_PRODUCTION
STATUS: LIVE

Health Check:
  - Agent responding? ✅
  - Error rate < 5%? ✅
  - Memory stable? ✅
  - Decisions logged? ✅
```

Rollback trigger: If error rate > 10% in first 30 min, revert to previous version.

---

### Stage 5: Operations (T+6+ days)

Agent runs autonomously with monitoring.

```yaml
Weekly Cadence:
  Monday: Measure KPIs
  Tuesday: Review escalations
  Wednesday: Retrain on new data
  Thursday: A/B test prompts
  Friday: Update permissions

Continuous Monitoring:
  - Latency alert: p99 > 5s
  - Error rate alert: > 2%
  - Cost alert: > 110% budget
  - Drift alert: accuracy drop > 5%
```

---

### Stage 6: Updates (T+ongoing)

Deploy improved versions without downtime.

```yaml
[AGENT_LIFECYCLE]
STAGE: UPDATES
AGENT: SalesAgent-CON-001
ACTION: DEPLOY_VERSION_2
STATUS: ROLLING_RELEASE

Canary Deployment:
  1. Deploy v2 alongside v1 (both live)
  2. Route 10% traffic to v2
  3. Monitor for 24h
  4. Increase to 50%, then 100%
  5. Retire v1
```

Rollback: If v2 error rate > 5%, instant revert to v1.

---

### Stage 7: Retirement (T+end)

Agent decommissioned when venture closes or task automated differently.

```yaml
[AGENT_LIFECYCLE]
STAGE: RETIREMENT
AGENT: SalesAgent-CON-001
ACTION: DECOMMISSION
STATUS: RETIRED
RETIRED_DATE: 2026-12-31
```

Checklist: Stop accepting tasks, complete in-flight work (24h SLA), export reflective memory, delete credentials, mark Neo4j, retire from production.

Data retention: audit_log 7 years, agent_state 30 days, metrics 1 year, credentials deleted immediately.

---

## Lifecycle State Machine

```
CREATED → TRAINING → APPROVAL ─[REJECTED]→ TRAINING
              ↓
          DEPLOYMENT ─[ROLLBACK]→ APPROVAL
              ↓
             LIVE
           ↙  ↓  ↘
       UPDATES MONITORING PAUSED
              ↓
           RETIRED
```

---

## Storage

**Neo4j**:
```cypher
(agent:Agent)-[:LIFECYCLE_STATE {stage, started_at, ended_at}]->(state:LifecycleStage)
(agent)-[:TRAINED_BY {iterations, accuracy}]->(dataset:Dataset)
(agent)-[:APPROVED_BY {timestamp, approver}]->(director:Director)
(agent)-[:DEPLOYED_TO {environment, timestamp}]->(env:Environment)
```

**Supabase**:
```sql
CREATE TABLE agent_lifecycle (
  agent_id TEXT PRIMARY KEY,
  stage TEXT,
  status TEXT,
  started_at TIMESTAMP,
  ended_at TIMESTAMP,
  metadata JSONB,
  audit_log TEXT[]
);
```

**Files**:
- `/agents/prod/{agent_id}-v{N}.yaml` — deployment config
- `/agents/logs/{agent_id}.jsonl` — execution logs
- `/agents/archive/{agent_id}-{RETIRED_DATE}/` — retired data

---

## Version History

- **v1.0 (2026-07-30)**: Agent lifecycle from creation through retirement.

