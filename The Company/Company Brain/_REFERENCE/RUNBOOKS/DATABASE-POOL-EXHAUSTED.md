# Runbook: Database Connection Pool Exhausted

**Status:** All API calls timeout. "too many connections" errors in logs.

**MTTR:** 5-10 minutes | **Severity:** Critical | **Owned By:** Infrastructure Team

---

## Symptoms

**Operational Impact:**
- API endpoints return 503 Service Unavailable
- Task submission fails with "connection pool exhausted"
- Logs show "FATAL: remaining connection slots reserved for non-replication superuser connections"
- Health check endpoint returns 500

**Monitoring Alerts:**
- Supabase connection count >= max_connections
- Average query latency > 10s (stalled queries holding connections)
- New connection requests getting queued instead of served

**User Reports:**
- "I can't submit tasks, getting database error"
- "Dashboard is completely down"

---

## Root Cause Analysis

### Step 1: Check Current Connection Count
```bash
# Connect to database
psql -h db.supabase.internal -U postgres -d company_brain -c "\
SELECT 
  current_setting('max_connections')::int as max_connections,
  count(*) as current_connections,
  round(100.0 * count(*) / current_setting('max_connections')::int, 1) as percent_used
FROM pg_stat_activity;"

# Expected: percent_used < 80%
# Critical: percent_used >= 95%
```

**Findings:**
- [ ] Connections near max (85-95%) → connection leak
- [ ] Connections at max (95-100%) → immediate action needed
- [ ] Connections normal (<80%) → issue elsewhere

### Step 2: Identify Long-Running Queries
```bash
psql -h db.supabase.internal -U postgres -d company_brain -c "\
SELECT 
  pid,
  usename,
  state,
  query,
  query_start,
  EXTRACT(EPOCH FROM (NOW() - query_start)) as seconds_running
FROM pg_stat_activity
WHERE state != 'idle'
ORDER BY query_start ASC;"

# Look for queries running > 30 seconds
```

**Findings:**
- [ ] Long-running query visible (> 300s) → query may be stuck, check if it's waiting for lock
- [ ] Many medium queries (30-60s) → possible migration or maintenance task running
- [ ] No queries visible (state = 'idle') → connection leak from application

### Step 3: Check for Idle Connections
```bash
psql -h db.supabase.internal -U postgres -d company_brain -c "\
SELECT 
  usename,
  count(*) as idle_count,
  max(EXTRACT(EPOCH FROM (NOW() - state_change))) as oldest_idle_seconds
FROM pg_stat_activity
WHERE state = 'idle'
GROUP BY usename
ORDER BY idle_count DESC;"

# High idle counts = connection leak
```

**Findings:**
- [ ] OmniRoute app has 100+ idle connections → app not closing connections
- [ ] Webhook handler has high idle → handler crashed before cleanup
- [ ] Multiple apps with idle → systemic leak

### Step 4: Check for Connection Pool (PgBouncer)
```bash
# If using connection pooler, check its status
psql -h pgbouncer:6432 -U postgres -d pgbouncer -c "\
SHOW POOLS;"

# Expected: database = company_brain, cl_active + cl_waiting < max_db_connections
```

**Findings:**
- [ ] Bouncer working correctly → issue is app-level
- [ ] Bouncer queue growing → too many requests for pool size

---

## Immediate Action

### Option 1: Terminate Idle Connections (Safe — low risk)
```bash
# Kill idle connections older than 5 minutes (keeps active work)
psql -h db.supabase.internal -U postgres -d company_brain -c "\
SELECT pg_terminate_backend(pid) 
FROM pg_stat_activity 
WHERE state = 'idle' 
  AND state_change < NOW() - INTERVAL '5 minutes'
  AND datname = 'company_brain'
  AND pid != pg_backend_pid();"

# Expected: Should release 20-50 connections
```

### Option 2: Terminate Specific App Connections (Medium risk)
```bash
# Kill all webhook handler connections (if handler crashed)
psql -h db.supabase.internal -U postgres -d company_brain -c "\
SELECT pg_terminate_backend(pid) 
FROM pg_stat_activity 
WHERE usename = 'webhook_handler'
  AND pid != pg_backend_pid();"

# Then restart the webhook handler:
ssh macstudio
sudo systemctl restart orchestrator-webhook-handler
```

### Option 3: Restart Connection Pooler (Last resort — ~30s downtime)
```bash
ssh macstudio
docker-compose restart pgbouncer
# or
sudo systemctl restart pgbouncer
```

---

## Resolution

### Step 1: Identify Root Cause (from Step 1-4 above)

**If:** Long-running query stuck
- Check if query is waiting for a lock: `SHOW max_parallel_workers;`
- Kill query: `SELECT pg_terminate_backend(pid);`
- Check for table locks: `SELECT * FROM pg_locks;`

**If:** Connection leak from application
- Application not closing connections after use
- Possible causes: missing connection cleanup, connection timeout not set, connection pool misconfigured
- Fix: Update application connection management (see "Prevention" section)

**If:** Migration or maintenance task running
- Long-running ALTER TABLE or REINDEX
- Check: `SELECT * FROM pg_stat_progress_create_index;`
- Wait for completion or cancel if safe: `SELECT pg_cancel_backend(pid);`

### Step 2: Verify Pool Recovered
```bash
psql -h db.supabase.internal -U postgres -d company_brain -c "\
SELECT 
  current_setting('max_connections')::int as max_connections,
  count(*) as current_connections,
  round(100.0 * count(*) / current_setting('max_connections')::int, 1) as percent_used
FROM pg_stat_activity;"

# Expected: percent_used < 60%
```

### Step 3: Restart Affected Services
```bash
# If OmniRoute or webhook handler was affected:
ssh macstudio
sudo systemctl restart orchestrator-webhook-handler
docker-compose -f services/omniroute/docker-compose.yml restart omniroute
```

---

## Recovery

### Step 1: Check Task Backlog
```bash
psql -h db.supabase.internal -U postgres -d company_brain -c "\
SELECT 
  status,
  count(*) as count
FROM task_executions
WHERE status IN ('queued', 'running', 'pending')
GROUP BY status;"

# Expected: Numbers should be stable or declining (not growing)
```

### Step 2: Resubmit Timeout Tasks
```bash
# Find tasks that were submitted during outage but never started
psql -h db.supabase.internal -U postgres -d company_brain -c "\
SELECT id, omniroute_job_id, status 
FROM task_executions
WHERE created_at > NOW() - INTERVAL '10 minutes'
  AND status = 'queued'
LIMIT 20;"

# Manually resubmit via OmniRoute API if needed
```

### Step 3: Resume Service Monitoring
```bash
# Verify critical services healthy
curl http://100.87.214.70:20128/health
curl http://100.87.214.70:7474
curl http://100.87.214.70:6333/health

# Expected: All return 200 OK
```

---

## Prevention

### 1. Set Connection Timeouts
```yaml
# In OmniRoute config
database:
  pool_size: 30
  idle_timeout: 5m           # Close idle connections after 5 min
  max_connection_time: 30m   # Force close connections after 30 min
  connection_retry: true
```

### 2. Monitor Connection Usage
```sql
-- Create monitoring table
CREATE TABLE connection_pool_events (
  timestamp TIMESTAMP DEFAULT NOW(),
  pool_type TEXT,
  connection_count INT,
  percent_used FLOAT,
  alert_triggered BOOLEAN
);

-- Add to monitoring dashboard
-- Alert if percent_used > 80% for 2+ minutes
```

### 3. Add Connection Pool Assertions
```javascript
// In webhook handler startup
const maxConnections = 30;
const current = await db.query('SELECT count(*) FROM pg_stat_activity');
if (current.rows[0].count > maxConnections * 0.9) {
  logger.error('Starting with high connection usage, possible leak');
  process.exit(1); // Fail fast
}
```

### 4. Implement Connection Cleanup Tests
```javascript
// Test: connections close after task completion
test('connections released after task execution', async () => {
  const before = await getConnectionCount();
  await submitTask(goodTask);
  const after = await getConnectionCount();
  
  expect(after).toBeLessThanOrEqual(before + 1); // Allowance for query execution
});
```

### 5. Set Up Periodic Cleanup Job
```sql
-- Every 1 hour, terminate idle connections older than 15 minutes
CREATE EXTENSION IF NOT EXISTS pg_cron;

SELECT cron.schedule('cleanup-idle-connections', '0 * * * *', $$
  SELECT pg_terminate_backend(pid) 
  FROM pg_stat_activity 
  WHERE state = 'idle' 
    AND state_change < NOW() - INTERVAL '15 minutes'
    AND pid != pg_backend_pid();
$$);
```

---

**Related Runbooks:**
- [[WEBHOOK-HANDLER-DOWN]] (when handler crashes)
- [[ORCHESTRATOR-TASK-STALLED]] (when individual tasks hang)

**Owned By:** Infrastructure Team  
**Escalation:** If pool remains exhausted after 5 min, page on-call SRE
