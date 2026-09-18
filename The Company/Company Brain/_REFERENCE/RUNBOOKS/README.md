# Runbooks — Incident Response & Troubleshooting

**Purpose:** Operational procedures for responding to common failures in Company Brain systems.

**Who Should Use:** On-call operators, incident responders, system engineers.

**Structure:** Each runbook follows the format:
1. **Symptoms** — What the user reports or observes
2. **Root Cause Analysis** — How to diagnose the problem
3. **Immediate Action** — What to do right now (before fixing)
4. **Resolution** — Steps to fix the problem
5. **Recovery** — How to verify the system is healthy
6. **Prevention** — How to prevent recurrence

---

## Runbooks

### [Orchestrator Task Stalled](ORCHESTRATOR-TASK-STALLED.md)
**Symptoms:** Task submitted, but never completes. Status stays "running" for >5 minutes.

**Root Causes:** OmniRoute timeout, network failure, agent crash, webhook never sent.

**MTTR (Mean Time to Resolution):** 5-15 minutes

---

### [Agent Consistently Fails](AGENT-CONSISTENTLY-FAILS.md)
**Symptoms:** Agent execution failing >50% of the time. ROI score dropping. Error rates spiking.

**Root Causes:** Model misconfiguration, capability mismatch, insufficient context, timeout too short.

**MTTR:** 10-30 minutes

---

### [Webhook Handler Down](WEBHOOK-HANDLER-DOWN.md)
**Symptoms:** Revenue not being attributed. Revenue logs growing empty. OmniRoute job completes but task_executions never updates.

**Root Causes:** API crashed, database connection failed, queue backlog, unhandled exception.

**MTTR:** 5-10 minutes

---

### [Revenue Attribution Gap](REVENUE-ATTRIBUTION-GAP.md)
**Symptoms:** $X in executed tasks, but only $Y attributed (X >> Y). Orphaned revenue_log records. Agent stats not updating.

**Root Causes:** Webhook malformed JSON, missing fields, timestamp mismatch, trigger not firing.

**MTTR:** 10-20 minutes

---

### [Neo4j Agent Discovery Broken](NEOJ-AGENT-DISCOVERY-BROKEN.md)
**Symptoms:** Agent matching returns empty results. Top 3 agents list blank. Only fallback to YAML working.

**Root Causes:** Neo4j connection failed, indexes down, query timeout, capability nodes missing.

**MTTR:** 10-30 minutes

---

### [OmniRoute Rate Limited](OMNIROUTE-RATE-LIMITED.md)
**Symptoms:** Tasks reject with 429 (Too Many Requests). Execution queue backs up. Users report slowness.

**Root Causes:** Concurrent task surge, no backoff logic, rate limit not enforced by client.

**MTTR:** 2-5 minutes

---

### [Database Connection Pool Exhausted](DATABASE-POOL-EXHAUSTED.md)
**Symptoms:** "too many connections" errors. All API calls timeout. Health check fails.

**Root Causes:** Leak in connection management, task stalled holding open connection, migration running long.

**MTTR:** 5-10 minutes

---

### [Claude Haiku API Key Invalid](CLAUDE-HAIKU-AUTH-FAILED.md)
**Symptoms:** Task classification always falls back to keyword matching. Log shows "401 Unauthorized".

**Root Causes:** Key expired, wrong key loaded, environment variable not set, credentials rotated.

**MTTR:** 2-5 minutes

---

## Using These Runbooks

### Step 1: Identify the Symptom
Read the symptom section of relevant runbooks. Which one matches?

### Step 2: Verify Root Cause
Follow the "Root Cause Analysis" section to confirm the diagnosis.

### Step 3: Take Immediate Action
Stabilize the system (stop bleeding, preserve data, communicate).

### Step 4: Resolve
Follow the "Resolution" steps in order.

### Step 5: Verify Recovery
Run the checks in the "Recovery" section to confirm the system is healthy.

### Step 6: Document & Prevent
Log the incident. Read the "Prevention" section and open a ticket if needed.

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

- [ ] Verify system health (API, DB, OmniRoute, Neo4j)
- [ ] Check Orchestrator dashboard for stuck tasks
- [ ] Review error logs (last 1 hour)
- [ ] Check Slack for incident reports
- [ ] Escalate if MTTR > 30 minutes
- [ ] Update incident status in ClickUp
- [ ] Notify affected users
- [ ] Document root cause post-incident
- [ ] Open ticket for prevention

---

## Escalation Policy

| MTTR | Action |
|------|--------|
| < 5 min | Resolve immediately |
| 5-15 min | Follow runbook, notify Slack |
| 15-30 min | Escalate to engineering lead |
| > 30 min | Declare incident, activate war room |

---

## Related Documentation

- [[ORCHESTRATOR-MASTER-SPECIFICATION|ORCHESTRATOR Master Specification]] — Architecture & APIs
- [[REALITY|REALITY.md]] — System health status
- [[CLAUDE|CLAUDE.md]] — Infrastructure state
