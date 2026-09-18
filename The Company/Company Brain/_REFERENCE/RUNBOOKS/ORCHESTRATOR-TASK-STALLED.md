# Runbook: Orchestrator Task Stalled

**Status:** Task submitted but never completes. Status stays "running" for >5 minutes.

**MTTR:** 5-15 minutes | **Severity:** Medium | **Owned By:** Orchestrator Team

---

## Symptoms

User observes:
- Task created 5+ minutes ago
- `task_executions.status` is still "running" or "pending"
- No webhook received
- No error message
- OmniRoute job_id exists but shows no progress

Dashboard shows:
- "Tasks in Running State" > 3
- Webhook backlog growing
- Agent utilization flat (agent appears idle)

---

## Root Cause Analysis

### Step 1: Check OmniRoute Status
```bash
# Query OmniRoute for job status
curl -s "http://100.87.214.70:20128/jobs/JOB-abc123" | jq .

# Should return: status = "running" or "completed"
# If 404 or "unknown", OmniRoute lost the job
```

**Findings:**
- [ ] Job exists and is "running" (agent executing, waiting for completion)
- [ ] Job exists but "pending" (queued, not started yet)
- [ ] Job exists but "failed" (agent crashed)
- [ ] Job not found (OmniRoute lost track, likely restart/crash)

### Step 2: Check Agent Logs
```bash
# SSH to agent execution environment
ssh macstudio

# Check if agent process is still running
ps aux | grep agent-AGT-NNN

# View recent logs
tail -100f /var/log/orchestrator/agent-AGT-NNN.log
```

**Findings:**
- [ ] Agent process running (check CPU/memory usage)
- [ ] Agent process dead (agent crashed during execution)
- [ ] Agent process hung (using 0% CPU, not responding)
- [ ] No logs (agent never started)

### Step 3: Check Network Connectivity
```bash
# Verify OmniRoute can reach agent
curl -s "http://100.87.214.70:20128/ping-agent/AGT-NNN" | jq .

# Test network latency to agent
ping -c 5 100.87.214.70

# Check firewall rules
sudo ufw status | grep 20128
```

**Findings:**
- [ ] Agent reachable (network OK)
- [ ] Agent unreachable (network issue)
- [ ] High latency (>100ms, possible timeout)

### Step 4: Check Webhook Delivery
```bash
# Query webhook events table
SELECT * FROM webhook_events
WHERE omniroute_job_id = 'JOB-abc123'
ORDER BY created_at DESC;

# Query webhook_handler logs
tail -100 /var/log/orchestrator/webhook-handler.log | grep JOB-abc123

# Check if any webhooks are stuck in retry
SELECT * FROM webhook_events
WHERE status = 'retrying' AND attempts > 5
ORDER BY created_at DESC LIMIT 10;
```

**Findings:**
- [ ] Webhook received and processed (check task_executions.webhook_processed = true)
- [ ] Webhook received but not processed (webhook_processed = false)
- [ ] Webhook never received (check OmniRoute logs)
- [ ] Webhook handler crashed (check logs for exceptions)

---

## Immediate Action (Stop the Bleeding)

### 1. Notify Users
**Slack message template:**
```
🚨 Incident: Task TASK-12345 stuck in running state (5+ minutes).
Investigating cause. Will update in <5 minutes.
```

### 2. Prevent Cascade
```bash
# Stop accepting new tasks (temporary circuit breaker)
curl -X POST "http://100.87.214.70:8000/api/admin/pause-orchestrator"

# This will:
# - Reject new task submissions
# - Continue processing in-flight tasks
# - Allow you to diagnose without making worse
```

### 3. Check Resource Usage
```bash
# Is system out of resources?
docker stats macstudio

# Free disk space?
df -h /

# Memory available?
free -h
```

---

## Resolution

### Scenario A: Agent Process Hung
```bash
# Kill stuck agent process (gracefully)
kill -TERM $(pgrep -f agent-AGT-NNN)
sleep 5

# If still running, force kill
kill -9 $(pgrep -f agent-AGT-NNN)

# OmniRoute will detect crash and mark job as failed
# Task will retry (up to 3 times)
```

### Scenario B: Webhook Handler Crashed
```bash
# Check handler status
systemctl status orchestrator-webhook-handler

# Restart handler
sudo systemctl restart orchestrator-webhook-handler

# Tail logs to verify it's running
tail -f /var/log/orchestrator/webhook-handler.log
```

### Scenario C: OmniRoute Lost Track
```bash
# Query task_executions for the stuck task
SELECT id, omniroute_job_id, status FROM task_executions
WHERE omniroute_job_id = 'JOB-abc123';

# Manually mark task as failed (gives retry chance)
UPDATE task_executions
SET status = 'failed', error_message = 'OmniRoute lost job, retrying'
WHERE omniroute_job_id = 'JOB-abc123';

# OmniRoute will re-submit on next reconciliation (60s interval)
```

### Scenario D: Network Latency / Timeout
```bash
# Check if task timed out waiting for agent
SELECT execution_duration_ms FROM task_executions
WHERE omniroute_job_id = 'JOB-abc123';

# If > 300,000ms (5 min), timeout likely culprit
# Increase timeout for this venture:
UPDATE ventures
SET orchestrator_timeout_ms = 600000  -- 10 minutes
WHERE venture_id = 'OPS-001';

# Retry the stalled task
INSERT INTO task_executions (...) 
SELECT * FROM task_executions
WHERE omniroute_job_id = 'JOB-abc123';
```

---

## Recovery

### Step 1: Verify Task Completes
```bash
# Check task status after fix
SELECT status, webhook_processed, revenue_attributed_at
FROM task_executions
WHERE task_id = 'TASK-12345';

# Expected: status = 'success', webhook_processed = true
# With revenue_attributed_at timestamp
```

### Step 2: Verify Revenue Attributed
```bash
# Check revenue log
SELECT * FROM revenue_logs
WHERE task_execution_id = (
  SELECT id FROM task_executions
  WHERE task_id = 'TASK-12345'
);

# Expected: one row with revenue_amount, cost_amount, net_profit
```

### Step 3: Resume Normal Operations
```bash
# Re-enable orchestrator
curl -X POST "http://100.87.214.70:8000/api/admin/resume-orchestrator"

# Verify it accepts new tasks
curl -X POST "http://100.87.214.70:8000/api/orchestrator/classify-task" \
  -H "Content-Type: application/json" \
  -d '{"description": "Test task", "venture": "OPS-001"}'

# Should return TaskClassification, not 503 Service Unavailable
```

### Step 4: Check Dashboard
- [ ] "Tasks in Running State" back to 0
- [ ] No pending webhooks
- [ ] Leaderboard updated for the recovered task's agent

---

## Prevention

### 1. Implement Timeout Enforcement
Add to OmniRoute executor:
```typescript
const timeout = venture.orchestrator_timeout_ms || 300000; // 5 min default
const timeoutHandle = setTimeout(() => {
  throw new Error(`Task exceeded ${timeout}ms timeout`);
}, timeout);
```

### 2. Add Periodic Reconciliation
```sql
-- Find tasks stuck >10 minutes, force reconciliation
SELECT task_id, omniroute_job_id
FROM task_executions
WHERE status IN ('pending', 'running')
  AND created_at < NOW() - INTERVAL '10 minutes'
  AND webhook_processed = FALSE;

-- Trigger OmniRoute to re-check these jobs
POST /api/admin/reconcile-jobs?job_ids=JOB-abc123,JOB-xyz789
```

### 3. Monitor Webhook Backlog
```sql
-- Alert if >10 webhooks unprocessed
SELECT COUNT(*) as backlog
FROM webhook_events
WHERE status = 'pending' AND created_at < NOW() - INTERVAL '2 minutes';

-- Create alert: IF backlog > 10 THEN page on-call
```

### 4. Add Dead Letter Queue
```sql
-- Store failed webhooks for manual retry
CREATE TABLE webhook_dead_letter (
  id UUID PRIMARY KEY,
  webhook_event_id TEXT,
  error_reason TEXT,
  attempts INTEGER,
  created_at TIMESTAMP
);

-- Move stale webhooks to DLQ
INSERT INTO webhook_dead_letter (...)
SELECT * FROM webhook_events
WHERE status = 'retrying' AND attempts > 5;

-- Manual retry process
SELECT COUNT(*) FROM webhook_dead_letter
WHERE created_at > NOW() - INTERVAL '1 hour';
```

---

## Follow-Up

- [ ] Update REALITY.md with incident summary
- [ ] Open ticket: "Add timeout enforcement to Orchestrator"
- [ ] Open ticket: "Add webhook backlog monitoring"
- [ ] Review agent logs for patterns (why did agent hang?)
- [ ] Add MTTR tracking to dashboard
