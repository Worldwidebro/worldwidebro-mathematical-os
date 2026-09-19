# Runbooks — Incident Response & Troubleshooting

**Purpose:** Operational procedures for responding to common failures in Company Brain systems.

**Who Should Use:** On-call operators, incident responders, system engineers.

**Tier 4 Status:** ✅ Complete — 6 runbooks wired + escalation policy

---

## Quick Start

**Got an incident?** Follow these 3 steps:

1. **Identify** → Which symptom matches? See runbook list below
2. **Diagnose** → Run "Root Cause Analysis" steps in the runbook
3. **Act** → Follow "Immediate Action" options (pick one)

**Need to escalate?** → See [[ESCALATION-POLICY|ESCALATION-POLICY.md]] (severity matrix + contact info)

---

## All Runbooks (6 Total)

### Revenue & Execution

#### [Orchestrator Task Stalled](ORCHESTRATOR-TASK-STALLED.md)
**Symptoms:** Task submitted but never completes. Status stays "running" for >5 minutes.

**Root Causes:** OmniRoute timeout, network failure, agent crash, webhook never sent.

**MTTR (Mean Time to Resolution):** 5-15 minutes | **Severity:** Medium

---

#### [Webhook Handler Down](WEBHOOK-HANDLER-DOWN.md)
**Symptoms:** Revenue not being attributed. Revenue logs growing empty. OmniRoute job completes but task_executions never updates.

**Root Causes:** API crashed, database connection failed, queue backlog, unhandled exception.

**MTTR:** 5-10 minutes | **Severity:** Critical

---

#### [Database Connection Pool Exhausted](DATABASE-POOL-EXHAUSTED.md)
**Symptoms:** "too many connections" errors. All API calls timeout. Health check fails.

**Root Causes:** Leak in connection management, task stalled holding open connection, migration running long.

**MTTR:** 5-10 minutes | **Severity:** Critical

---

### Knowledge Graph & Discovery

#### [Neo4j Agent Discovery Broken](NEO4J-DISCOVERY-BROKEN.md)
**Symptoms:** Agent matching returns empty results. Top 3 agents list blank. Only fallback to YAML working.

**Root Causes:** Neo4j connection failed, indexes down, query timeout, capability nodes missing.

**MTTR:** 10-30 minutes | **Severity:** High

---

### Authentication & Keys

#### [Auth/API Key Invalid](AUTH-FAILED.md)
**Symptoms:** Task classification always falls back to keyword matching. Log shows "401 Unauthorized".

**Root Causes:** Key expired, wrong key loaded, environment variable not set, credentials rotated.

**MTTR:** 2-5 minutes | **Severity:** Medium

---

### Escalation & Coordination

#### [Escalation Policy](ESCALATION-POLICY.md)
**Purpose:** How to escalate incidents from L1 (Support) → L2 (Specialists) → L3 (Executive).

**Contains:**
- Severity matrix (Critical/High/Medium/Low)
- Category routing (Execution, Discovery, Auth, Revenue)
- Contact information for each team
- Incident response workflow
- Alerting thresholds

**Use This:** When escalating an incident, or setting up monitoring

---

## Using These Runbooks

### Step 1: Identify the Symptom
Read the **Symptoms** section of each runbook. Which one matches what you're seeing?

**Example:** If users report "agent discovery returns no results", check [[NEO4J-DISCOVERY-BROKEN]].

### Step 2: Verify Root Cause
Follow the **Root Cause Analysis** section step-by-step to diagnose the problem.

**Example:** Run the Neo4j health check, verify agent count, check indexes.

### Step 3: Take Immediate Action
Follow **Immediate Action** options. Pick the one that matches your situation (Low/Medium/High risk).

**Example:** Option 1 (restart) vs. Option 2 (use fallback) vs. Option 3 (advanced recovery).

### Step 4: Resolve & Recover
Execute the **Resolution** steps, then verify in **Recovery** section.

### Step 5: Prevent Recurrence
Implement **Prevention** measures to avoid this incident in the future.

---

## By Severity Level

### 🚨 Critical (Page Immediately)
All API calls failing, revenue tracking broken, database exhausted
- [[WEBHOOK-HANDLER-DOWN]] (revenue not attributed)
- [[DATABASE-POOL-EXHAUSTED]] (all connections used)
- **Escalation:** [[ESCALATION-POLICY]] → Page L2 within 5 min

### ⚠️ High (Page Within 5 min)
30-70% of tasks failing, database/Neo4j degraded, fallback in use
- [[NEO4J-DISCOVERY-BROKEN]] (agent discovery empty)
- [[ORCHESTRATOR-TASK-STALLED]] (affecting multiple tasks)
- **Escalation:** [[ESCALATION-POLICY]] → Page L2, escalate to L3 if unresolved after 10 min

### ℹ️ Medium (Ticket + 30-min Check-in)
Single pathway degraded, elevated latency, fallback recovery working
- [[ORCHESTRATOR-TASK-STALLED]] (single task)
- [[AUTH-FAILED]] (classification using fallback)
- **Escalation:** [[ESCALATION-POLICY]] → Create ticket, check-in after 30 min

### 📋 Low (Backlog)
Minor performance drift, documentation out of date
- **Escalation:** Add to standard backlog, review in next sprint

---

## By Team Ownership

| Team | Runbooks |
|------|----------|
| **Orchestrator Team** | ORCHESTRATOR-TASK-STALLED, WEBHOOK-HANDLER-DOWN |
| **Infrastructure Team** | DATABASE-POOL-EXHAUSTED |
| **Knowledge Graph Team** | NEO4J-DISCOVERY-BROKEN |
| **Security Team** | AUTH-FAILED |
| **All Teams** | ESCALATION-POLICY |

---

## Key Dashboards & Queries

### Check System Health
```bash
# API health check
curl -s http://100.87.214.70:8000/api/health | jq .

# Database connection count
psql -c "SELECT count(*) FROM pg_stat_activity WHERE state = 'active';"

# OmniRoute status
curl -s http://100.87.214.70:20128/health | jq .

# Neo4j status
curl -s -u neo4j:changeme http://100.87.214.70:7474/db/neo4j/tx -X POST | jq .
```

### Monitor Orchestrator
```sql
-- Tasks in "stuck" state (>5 min old, not completed)
SELECT task_id, assigned_agent_id, created_at, status
FROM task_executions
WHERE status IN ('pending', 'running')
  AND created_at < NOW() - INTERVAL '5 minutes'
ORDER BY created_at;

-- Recent failures
SELECT task_id, status, error_code, error_message, created_at
FROM task_executions
WHERE status = 'failure'
  AND created_at > NOW() - INTERVAL '1 hour'
ORDER BY created_at DESC;

-- Revenue log gaps (tasks completed, but no revenue attributed)
SELECT te.task_id, te.omniroute_job_id, te.execution_completed_at
FROM task_executions te
LEFT JOIN revenue_logs rl ON te.id = rl.task_execution_id
WHERE te.status = 'success'
  AND te.execution_completed_at < NOW() - INTERVAL '5 minutes'
  AND rl.id IS NULL;
```

---

## On-Call Checklist

**When incident is reported:**
- [ ] Acknowledge and start timer (MTTR clock starts)
- [ ] Identify symptom → which runbook matches?
- [ ] Run Root Cause Analysis steps (5-10 min)
- [ ] Execute Option 1 recovery (low risk)
- [ ] Update Slack #incidents channel with status
- [ ] Did Option 1 work?
  - [ ] YES → Monitor + document + create post-mortem ticket
  - [ ] NO → Move to Option 2-3 or escalate

**Escalation checklist:**
- [ ] MTTR exceeded for severity level? (see [[ESCALATION-POLICY]])
- [ ] Check escalation contacts (Slack handles or PagerDuty)
- [ ] Include: root cause summary + attempts made + impact + resource needs
- [ ] Update incident status every 10 minutes

**Post-incident (24-48h):**
- [ ] Schedule post-mortem meeting
- [ ] Document root cause, timeline, gaps
- [ ] Create action items for [[ESCALATION-POLICY]] prevention section
- [ ] Update runbook based on learnings
- [ ] Close incident ticket

---

## Escalation Contacts

**L1 (Support On-Call)** — Automatic page from monitoring
- Alert channel: `#critical-incidents`
- Response SLA: 15 minutes

**L2 (Domain Specialists)** — Page if L1 can't resolve after 5 min
- Orchestrator Lead: `@orchestrator-lead` + PagerDuty
- Infrastructure Lead: `@infra-lead` + PagerDuty
- Knowledge Graph Lead: `@neo4j-lead` + PagerDuty
- Security Lead: `@security-lead` + PagerDuty

**L3 (Executive)** — Page if unresolved after 10 min (critical) or 20 min (high)
- On-call: CEO / CTO (rotating weekly)
- Channel: `#critical-incidents-exec`
- Direct escalation: Page directly via PagerDuty

See [[ESCALATION-POLICY|ESCALATION-POLICY.md]] for full contact list and escalation matrix.

---

## Related Documentation

- [[STARTHERE]] — Master orientation (Phase 0/1 status)
- [[ORCHESTRATOR-MASTER-SPECIFICATION]] — Architecture & APIs
- [[ORCHESTRATOR-API-REFERENCE]] — All endpoints with examples
- [[ORCHESTRATOR-STATE-MACHINE]] — 13-stage loop with decision trees
- [[REALITY|REALITY.md]] — System health status
- [[CLAUDE|CLAUDE.md]] — Infrastructure state
- [[ESCALATION-POLICY]] — Severity matrix & incident workflow
