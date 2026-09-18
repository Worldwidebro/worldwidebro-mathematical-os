# Runbook: Webhook Handler Down

**Status:** Revenue not being attributed. OmniRoute jobs complete but task_executions never updates.

**MTTR:** 5-10 minutes | **Severity:** Critical | **Owned By:** Orchestrator Team

---

## Symptoms

**Operational Impact:**
- Tasks completing in OmniRoute, but status stuck in "running"
- revenue_logs table empty for past N hours
- agent_stats not updating
- Leaderboard frozen at old data

**Monitoring Alerts:**
- Webhook handler HTTP 500 errors
- Queue size growing (tasks_executing_backlog > 100)
- `last_webhook_processed_at` timestamp stale (>5 min old)

**User Reports:**
- "Agent finished the task but it's still marked running"
- "I don't see today's revenue in the dashboard"

---

## Root Cause Analysis

### Step 1: Check Webhook Handler Process
```bash
# SSH to webhook handler machine
ssh macstudio

# Check if handler is running
ps aux | grep webhook-handler

# Check status via systemd
sudo systemctl status orchestrator-webhook-handler

# Expected: active (running)
# If: inactive, disabled, or failed → handler crashed
```

### Step 2: Check Recent Logs
```bash
# Last 50 lines
sudo tail -50 /var/log/orchestrator/webhook-handler.log

# Search for errors
sudo grep "ERROR\|FATAL\|Exception" /var/log/orchestrator/webhook-handler.log | tail -20

# Check handler startup logs
sudo journalctl -u orchestrator-webhook-handler -n 100
```

**Look for:**
- [ ] "Database connection refused" → DB unreachable
- [ ] "HTTP 5xx errors" → API crashed
- [ ] "OutOfMemory" → handler using too much RAM
- [ ] "SIGTERM/SIGKILL" → process killed
- [ ] No recent logs → handler never started

### Step 3: Check Database Connection
```bash
# Verify Supabase is reachable
psql -h db.supabase.internal -U postgres -d company_brain -c "SELECT 1;" 2>&1

# Check active connections
psql -c "SELECT count(*) FROM pg_stat_activity;"

# Check for connection pool exhaustion
psql -c "SHOW max_connections;" 
psql -c "SELECT count(*) FROM pg_stat_activity;"
# If (count / max_connections) > 0.8 → pool exhausted
```

### Step 4: Check Webhook Queue Depth
```bash
# Count unprocessed webhooks
SELECT COUNT(*) as backlog FROM webhook_events
WHERE status = 'pending' AND created_at > NOW() - INTERVAL '1 hour';

# Count retrying webhooks
SELECT COUNT(*) as retrying FROM webhook_events
WHERE status = 'retrying';

# Expected: backlog << 10, retrying << 5
# If backlog > 100 → handler can't keep up
```

### Step 5: Test Handler Manually
```bash
# Send test webhook to handler
curl -X POST "http://localhost:3001/api/webhooks/orchestrator/task-completed" \
  -H "Content-Type: application/json" \
  -H "X-OmniRoute-Signature: test" \
  -d '{
    "webhook_event_id": "EVT-test-123",
    "omniroute_job_id": "JOB-test-456",
    "status": "completed",
    "agent_output": {"actual_revenue": 500, "cost_actual": 25},
    "completed_at": "2026-09-18T14:00:00Z"
  }'

# Expected: 202 Accepted
# If 500, 503, or timeout → handler broken
```

---

## Immediate Action (Stop the Bleeding)

### 1. Acknowledge Incident
**Slack:**
```
🚨 INCIDENT: Webhook handler down. Revenue attribution paused.
Status: investigating. Estimated 5-10 min fix.
```

### 2. Check Handler Memory & Restart
```bash
# Check memory usage
ps aux | grep webhook-handler | awk '{print $6}'  # RSS in KB

# If > 1GB, handler has leak, restart
sudo systemctl restart orchestrator-webhook-handler

# Monitor restart
sudo tail -f /var/log/orchestrator/webhook-handler.log

# Wait 30 seconds for startup, then verify
curl -s "http://localhost:3001/api/health" | jq .
```

### 3. Prevent Data Loss
Webhook events arriving from OmniRoute should queue to disk:
```bash
# Check disk space on webhook queue dir
df -h /var/spool/orchestrator/webhook-queue/

# If < 100MB free, cleanup old events
rm /var/spool/orchestrator/webhook-queue/events_2026-09-17*.json
```

---

## Resolution

### Path 1: Handler Crashed (Most Common)
```bash
# Restart handler
sudo systemctl restart orchestrator-webhook-handler

# Verify it's running
sudo systemctl status orchestrator-webhook-handler

# Tail logs to see startup messages
sudo tail -20 /var/log/orchestrator/webhook-handler.log
```

**Expected output:**
```
✅ Webhook handler starting
✅ Database connected
✅ Listening on :3001
✅ Processing backlog: 47 events
```

### Path 2: Database Connection Lost
```bash
# Verify DB is reachable
psql -h db.supabase.internal -U postgres -d company_brain -c "SELECT 1;"

# If not, check connectivity
ping -c 3 db.supabase.internal

# Check Supabase status
curl -s "https://status.supabase.com/api/v2/components.json" | jq '.[] | select(.name | contains("database"))'

# If DB is down, wait for Supabase to recover (ETA from status page)
# While waiting, pause Orchestrator to prevent queue overflow
```

### Path 3: Connection Pool Exhausted
```bash
# Check active connections
psql -c "SELECT count(*) FROM pg_stat_activity WHERE state = 'active';"

# List long-running queries (likely culprit)
SELECT 
  pid, 
  usename, 
  query, 
  EXTRACT(EPOCH FROM (NOW() - query_start)) as duration_sec
FROM pg_stat_activity
WHERE state = 'active'
ORDER BY query_start ASC;

# Kill long-running queries (if safe to do)
SELECT pg_terminate_backend(pid) FROM pg_stat_activity
WHERE usename = 'orchestrator' AND query_start < NOW() - INTERVAL '30 minutes';

# Then restart handler
sudo systemctl restart orchestrator-webhook-handler
```

### Path 4: Out of Memory
```bash
# Check system memory
free -h

# If < 1GB available, kill non-essential processes
sudo systemctl stop nginx  # if running
sudo systemctl stop redis  # if non-critical

# Restart handler
sudo systemctl restart orchestrator-webhook-handler

# Monitor memory growth
watch -n 1 'ps aux | grep webhook-handler | head -1'
```

### Path 5: Code Crash (Bug in Handler)
```bash
# Check error logs for stack trace
sudo grep -A 10 "Traceback\|Error:" /var/log/orchestrator/webhook-handler.log

# If unhandled exception, need code fix
# Temporary: run handler in debug mode
sudo systemctl stop orchestrator-webhook-handler
/opt/orchestrator/webhook-handler --debug 2>&1 | tee /tmp/webhook-debug.log

# Send test webhook to reproduce
# Once reproduced, stop debug mode and escalate to engineering
```

---

## Recovery

### Step 1: Verify Handler Accepting Webhooks
```bash
# Send test webhook
curl -X POST "http://localhost:3001/api/health" 

# Expected: 200 OK
# If not, handler still not ready
```

### Step 2: Process Backlog
```bash
# Handler should automatically process queued webhooks
# Monitor progress
watch -n 5 'psql -c "SELECT COUNT(*) FROM webhook_events WHERE status = '\''pending'\'';"'

# Expected: count decreases over time (as handler processes)
# Should process ~100 webhooks per second
```

### Step 3: Verify Revenue Attributed
```bash
# Count revenue logs from past hour
SELECT COUNT(*) FROM revenue_logs
WHERE created_at > NOW() - INTERVAL '1 hour';

# Should be increasing (not stuck at old number)

# Check agent stats updated
SELECT updated_at FROM agent_stats
WHERE agent_id = 'AGT-042'
ORDER BY updated_at DESC LIMIT 1;

# Should be very recent (<2 min ago)
```

### Step 4: Verify Dashboard
- [ ] Leaderboard updated (timestamps recent)
- [ ] Webhook backlog = 0
- [ ] No alerts for stalled tasks
- [ ] Revenue attributed > 0 for past hour

### Step 5: Resume Normal Operations
```bash
# Send Slack update
"✅ Incident resolved. Webhook handler recovered and processing backlog.
Revenue attribution back online. ETA to zero backlog: 5 minutes."

# Monitor for next 10 minutes for regression
tail -f /var/log/orchestrator/webhook-handler.log | grep "ERROR"
```

---

## Prevention

### 1. Monitor Handler Health
```yaml
# Add to Prometheus config
- job_name: 'webhook-handler'
  static_configs:
    - targets: ['localhost:3001']
  metrics_path: '/api/metrics'

# Alerting rules
alert: WebhookHandlerDown
  expr: up{job="webhook-handler"} == 0
  for: 2m
  annotations:
    summary: "Webhook handler is down"

alert: WebhookQueueBacklog
  expr: webhook_backlog_count > 50
  for: 5m
  annotations:
    summary: "Webhook queue building up"
```

### 2. Implement Automatic Restart
```bash
# Add to systemd service file
[Unit]
Description=Webhook Handler
Restart=always
RestartSec=10

[Service]
ExecStart=/opt/orchestrator/webhook-handler
# If crashes, automatically restart after 10s
```

### 3. Add Memory Limit
```bash
# Prevent handler from consuming entire system memory
[Service]
MemoryMax=2G  # Max 2GB RAM
MemoryHigh=1.5G  # Warning at 1.5GB

# systemd will kill process if it exceeds MemoryMax
```

### 4. Implement Dead Letter Queue
```sql
-- Webhooks failing >3 retries go to DLQ
CREATE TABLE webhook_dead_letter (
  id UUID PRIMARY KEY,
  webhook_event_id TEXT,
  omniroute_job_id TEXT,
  error_message TEXT,
  failed_at TIMESTAMP,
  needs_manual_review BOOLEAN DEFAULT TRUE
);

-- Periodic job to move failed webhooks
INSERT INTO webhook_dead_letter (...)
SELECT * FROM webhook_events
WHERE status = 'retrying' AND attempts >= 3;

-- Manual retry process (operator reviews before retrying)
```

### 5. Add Graceful Degradation
```typescript
// If handler queue backs up >100, tell Orchestrator to slow down
if (webhookBacklog > 100) {
  // Pause new task submissions
  POST /api/admin/pause-orchestrator
  // Allow in-flight tasks to complete
}
```

---

## Follow-Up

- [ ] Review handler logs for root cause (memory leak? connection leak?)
- [ ] Open ticket: "Implement memory limit for webhook handler"
- [ ] Open ticket: "Add webhook queue monitoring to dashboard"
- [ ] Open ticket: "Implement dead letter queue for failed webhooks"
- [ ] Document incident in REALITY.md
- [ ] Schedule postmortem if MTTR > 15 minutes

---

## Escalation

| Time Elapsed | Action |
|---|---|
| < 2 min | Attempt restart |
| 2-5 min | Check logs for root cause |
| 5-10 min | Escalate to engineering if not resolved |
| > 10 min | Declare incident, activate war room |
