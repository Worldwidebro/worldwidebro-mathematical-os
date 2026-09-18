# Orchestrator Prime — Backend Schema & OmniRoute Integration

**Location:** `20-DECISIONS/ORCHESTRATOR-PRIME-BACKEND-SCHEMA.md`  
**Updated:** 2026-09-18  
**Version:** 1.0  
**Status:** Production-ready  
**Maintainer:** Orchestrator Prime (AGT-001)

---

## Overview

This document describes the complete backend schema for Orchestrator Prime, with focus on OmniRoute integration and webhook processing. Orchestrator Prime (AGT-001) routes incoming tasks to appropriate agents via OmniRoute, tracks execution state in Supabase, and processes webhooks to drive revenue attribution and operational workflows.

**Integration Points:**
- OmniRoute API (110 tools, MCP-enabled routing engine)
- Supabase PostgreSQL (task execution, webhooks, metrics)
- Qdrant (vector context retrieval)
- Neo4j (agent discovery, capability graph)

---

## Core Tables (Supabase Schema)

### 1. Task Executions Table

Stores all task invocations with execution state tracking.

```sql
CREATE TABLE task_executions (
  -- Identity
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  task_id TEXT UNIQUE NOT NULL,
  
  -- Classification (from Orchestrator Prime)
  task_type VARCHAR(50) NOT NULL, -- "agent_invocation", "workflow", "revenue_attribution", etc.
  domain VARCHAR(50) NOT NULL, -- "sales", "operations", "finance", etc.
  priority INTEGER DEFAULT 5, -- 1-10, higher = urgent
  
  -- Source & Routing
  source_venture_id VARCHAR(50),
  source_user_id UUID,
  requested_capability VARCHAR(100),
  
  -- OmniRoute Integration
  omniroute_job_id TEXT UNIQUE, -- OmniRoute async job ID
  omniroute_status VARCHAR(50) DEFAULT 'pending', -- queued, running, completed, failed, cancelled
  omniroute_result JSONB, -- Full response from OmniRoute
  
  -- Execution Tracking
  assigned_agent_id VARCHAR(50), -- AGT-NNN format
  assigned_agent_name VARCHAR(255),
  execution_started_at TIMESTAMP,
  execution_completed_at TIMESTAMP,
  execution_duration_ms INTEGER,
  
  -- Webhook State
  webhook_received_at TIMESTAMP, -- When completion webhook arrived
  webhook_event_id TEXT, -- Links to webhook_events table
  webhook_processed BOOLEAN DEFAULT FALSE,
  webhook_processed_at TIMESTAMP,
  
  -- Result Tracking
  status VARCHAR(50) NOT NULL DEFAULT 'pending', -- pending, running, success, failure, timeout
  error_code VARCHAR(50), -- COP-NNN format (OmniRoute error codes)
  error_message TEXT,
  retry_count INTEGER DEFAULT 0,
  max_retries INTEGER DEFAULT 3,
  
  -- Revenue Attribution (populated by webhook handler)
  attributed_revenue DECIMAL(10, 2),
  attributed_deal_id VARCHAR(50),
  revenue_attributed_at TIMESTAMP,
  
  -- Context & Metadata
  input_params JSONB NOT NULL, -- Task parameters (sanitized)
  context_window_tokens INTEGER, -- Tokens used for context
  model_used VARCHAR(50), -- Claude model used by agent
  cost_estimate DECIMAL(8, 4),
  cost_actual DECIMAL(8, 4),
  
  -- Audit
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),
  
  -- Indexes
  INDEX idx_task_type (task_type),
  INDEX idx_omniroute_job_id (omniroute_job_id),
  INDEX idx_assigned_agent (assigned_agent_id),
  INDEX idx_status (status),
  INDEX idx_webhook_processed (webhook_processed),
  INDEX idx_created_at (created_at DESC),
  CONSTRAINT fk_webhook_event FOREIGN KEY (webhook_event_id) REFERENCES webhook_events(id)
);
```

**Indexes for Performance:**
- `omniroute_job_id`: Webhook handler uses this to correlate responses
- `status`: Polling queries for pending/running tasks
- `webhook_processed`: Find unprocessed webhook events
- `created_at DESC`: Recent tasks query (VEX dashboard)

---

### 2. Webhook Events Table

Raw webhook events from OmniRoute, before processing.

```sql
CREATE TABLE webhook_events (
  -- Identity
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  event_id TEXT UNIQUE NOT NULL, -- OmniRoute-provided event ID (for idempotency)
  
  -- Event Metadata
  event_type VARCHAR(100) NOT NULL, -- "job.completed", "job.failed", "job.timeout", etc.
  received_at TIMESTAMP DEFAULT NOW(),
  received_from_ip INET,
  
  -- Signature Verification
  signature_algorithm VARCHAR(50), -- "hmac-sha256"
  signature_provided TEXT,
  signature_verified BOOLEAN DEFAULT FALSE,
  verification_error TEXT,
  
  -- Raw Event Payload
  raw_payload JSONB NOT NULL, -- Full webhook body
  
  -- OmniRoute Job Reference
  omniroute_job_id TEXT NOT NULL,
  omniroute_status VARCHAR(50), -- Extracted from payload
  omniroute_result JSONB, -- Job result from OmniRoute
  
  -- Processing State
  processing_status VARCHAR(50) DEFAULT 'pending', -- pending, processing, completed, failed, skipped
  processing_started_at TIMESTAMP,
  processing_completed_at TIMESTAMP,
  processing_error TEXT,
  
  -- Retry Logic
  retry_count INTEGER DEFAULT 0,
  max_retries INTEGER DEFAULT 5,
  next_retry_at TIMESTAMP,
  
  -- Audit & Tracing
  traced_task_execution_id UUID, -- Links to task_executions table
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),
  
  -- Indexes
  INDEX idx_event_id (event_id),
  INDEX idx_omniroute_job_id (omniroute_job_id),
  INDEX idx_processing_status (processing_status),
  INDEX idx_received_at (received_at DESC),
  CONSTRAINT fk_task_execution FOREIGN KEY (traced_task_execution_id) REFERENCES task_executions(id)
);
```

**Why Raw Payload?**
- Signature verification requires original bytes
- Audit trail: immutable record of what OmniRoute sent
- Retry recovery: reprocess without re-invoking OmniRoute

---

### 3. Webhook Logs Table

Detailed delivery attempt logs (for debugging, not primary processing).

```sql
CREATE TABLE webhook_logs (
  -- Identity
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  webhook_event_id UUID NOT NULL,
  
  -- Delivery Attempt
  attempt_number INTEGER NOT NULL,
  attempt_timestamp TIMESTAMP DEFAULT NOW(),
  
  -- HTTP Details
  http_status_code INTEGER,
  http_response_body TEXT,
  
  -- Handling Details
  handler_name VARCHAR(100), -- e.g., "revenue_attribution_handler"
  handler_error TEXT,
  handler_completed_successfully BOOLEAN DEFAULT FALSE,
  
  -- Timing
  duration_ms INTEGER,
  
  -- Audit
  created_at TIMESTAMP DEFAULT NOW(),
  
  INDEX idx_webhook_event_id (webhook_event_id),
  INDEX idx_attempt_timestamp (attempt_timestamp DESC),
  CONSTRAINT fk_webhook_event FOREIGN KEY (webhook_event_id) REFERENCES webhook_events(id)
);
```

---

### 4. OmniRoute Metrics Table

Aggregated metrics for monitoring and cost tracking.

```sql
CREATE TABLE omniroute_metrics (
  -- Identity
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  metric_hour TIMESTAMP NOT NULL, -- Hourly bucket
  
  -- Execution Metrics
  invocation_count INTEGER DEFAULT 0,
  completed_count INTEGER DEFAULT 0,
  failed_count INTEGER DEFAULT 0,
  timeout_count INTEGER DEFAULT 0,
  
  -- Latency (milliseconds)
  latency_p50 INTEGER,
  latency_p95 INTEGER,
  latency_p99 INTEGER,
  latency_max INTEGER,
  latency_avg DECIMAL(8, 2),
  
  -- Success Rate
  success_rate_pct DECIMAL(5, 2), -- 0-100
  
  -- Cost Tracking
  total_cost DECIMAL(10, 2),
  cost_by_model JSONB, -- { "claude-haiku": 2.50, "claude-sonnet": 5.75 }
  cost_per_invocation DECIMAL(8, 4),
  
  -- Agent Breakdown
  invocations_by_agent JSONB, -- { "AGT-001": 45, "AGT-002": 32, ... }
  
  -- Task Type Breakdown
  invocations_by_task_type JSONB, -- { "agent_invocation": 50, "workflow": 27, ... }
  
  -- Error Breakdown
  errors_by_code JSONB, -- { "TIMEOUT": 5, "INVALID_INPUT": 2 }
  
  -- Audit
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),
  
  UNIQUE(metric_hour),
  INDEX idx_metric_hour (metric_hour DESC)
);
```

---

### 5. Webhook Delivery Metrics Table

Per-webhook performance and reliability metrics.

```sql
CREATE TABLE webhook_delivery_metrics (
  -- Identity
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  metric_hour TIMESTAMP NOT NULL,
  
  -- Delivery Metrics
  webhook_events_received INTEGER DEFAULT 0,
  webhook_events_processed INTEGER DEFAULT 0,
  webhook_events_failed INTEGER DEFAULT 0,
  
  -- Delivery Attempts
  total_attempts INTEGER DEFAULT 0,
  successful_first_attempt_pct DECIMAL(5, 2),
  
  -- Retry Statistics
  retries_triggered INTEGER DEFAULT 0,
  retries_successful INTEGER DEFAULT 0,
  retries_exhausted INTEGER DEFAULT 0,
  
  -- Processing Latency (milliseconds)
  processing_latency_p50 INTEGER,
  processing_latency_p95 INTEGER,
  processing_latency_p99 INTEGER,
  
  -- Error Codes
  errors_by_code JSONB, -- { "DUPLICATE_EVENT": 3, "SIGNATURE_INVALID": 1 }
  
  -- Audit
  created_at TIMESTAMP DEFAULT NOW(),
  
  UNIQUE(metric_hour),
  INDEX idx_metric_hour (metric_hour DESC)
);
```

---

## OmniRoute API Endpoints

Orchestrator Prime calls these endpoints to invoke agents and receive updates.

### 1. POST /api/omniroute/invoke

**Purpose:** Invoke an agent for a task.

**Request:**
```json
{
  "task_id": "TASK-2026-09-18-001",
  "task_type": "agent_invocation",
  "domain": "sales",
  "requested_agent": "AGT-001",
  "input_params": {
    "scenario": "#6252367",
    "action": "deploy_and_activate",
    "context": "LT-005 revenue system"
  },
  "priority": 8,
  "timeout_seconds": 300,
  "webhook_url": "https://company-brain-api.vercel.app/api/omniroute/webhook",
  "idempotency_key": "idempotency-key-12345"
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "omniroute_job_id": "JOB-67890",
  "status": "queued",
  "estimated_wait_ms": 1500,
  "message": "Task queued for agent AGT-001"
}
```

**Response (400 Bad Request):**
```json
{
  "success": false,
  "error_code": "INVALID_INPUT",
  "error_message": "Missing required field: input_params",
  "details": {
    "field": "input_params",
    "reason": "must be a valid JSON object"
  }
}
```

---

### 2. GET /api/omniroute/status/:taskId

**Purpose:** Poll execution status (for synchronous workflows).

**Request:**
```bash
GET /api/omniroute/status/TASK-2026-09-18-001?include_result=true
Authorization: Bearer <api-key>
```

**Response (200 OK):**
```json
{
  "task_id": "TASK-2026-09-18-001",
  "omniroute_job_id": "JOB-67890",
  "status": "running",
  "started_at": "2026-09-18T14:30:15Z",
  "progress_pct": 45,
  "estimated_completion_ms": 8500,
  "assigned_agent": "AGT-001",
  "model_used": "claude-haiku-4-5-20251001",
  "tokens_used": 1234
}
```

**Response (Complete):**
```json
{
  "task_id": "TASK-2026-09-18-001",
  "omniroute_job_id": "JOB-67890",
  "status": "completed",
  "completed_at": "2026-09-18T14:30:25Z",
  "duration_ms": 10000,
  "assigned_agent": "AGT-001",
  "result": {
    "output": "Scenario #6252367 deployed and activated successfully.",
    "health_check": "200 OK",
    "revenue_attributed": 5400
  },
  "cost": 0.0234,
  "model_used": "claude-haiku-4-5-20251001",
  "tokens_used": {
    "input": 1234,
    "output": 567
  }
}
```

---

### 3. POST /api/omniroute/webhook

**Purpose:** Receive async task completion events from OmniRoute.

**Request (from OmniRoute):**
```bash
POST /api/omniroute/webhook
Content-Type: application/json
X-Omniroute-Signature: hmac-sha256=abc123...
X-Omniroute-Event-ID: evt-2026-09-18-xyz

{
  "event_id": "evt-2026-09-18-xyz",
  "event_type": "job.completed",
  "timestamp": "2026-09-18T14:30:25Z",
  "omniroute_job_id": "JOB-67890",
  "task_id": "TASK-2026-09-18-001",
  "status": "completed",
  "result": {
    "output": "Scenario #6252367 deployed and activated successfully.",
    "health_check": "200 OK",
    "revenue_attributed": 5400,
    "attributed_deal_id": "DEAL-001-LT-005"
  },
  "execution_duration_ms": 10000,
  "assigned_agent": "AGT-001",
  "model_used": "claude-haiku-4-5-20251001",
  "tokens_used": {
    "input": 1234,
    "output": 567
  },
  "cost": 0.0234
}
```

**Response (202 Accepted):**
```json
{
  "success": true,
  "message": "Webhook received and queued for processing",
  "event_id": "evt-2026-09-18-xyz"
}
```

**Response (400 Bad Request):**
```json
{
  "success": false,
  "error_code": "INVALID_SIGNATURE",
  "error_message": "Webhook signature verification failed",
  "expected_signature": "hmac-sha256=def456...",
  "received_signature": "hmac-sha256=abc123..."
}
```

---

### 4. POST /api/omniroute/cancel/:taskId

**Purpose:** Cancel a running task.

**Request:**
```bash
POST /api/omniroute/cancel/TASK-2026-09-18-001
Authorization: Bearer <api-key>
Content-Type: application/json

{
  "reason": "user_requested",
  "message": "User cancelled task via VEX dashboard"
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "task_id": "TASK-2026-09-18-001",
  "omniroute_job_id": "JOB-67890",
  "status": "cancelled",
  "cancelled_at": "2026-09-18T14:30:30Z",
  "reason": "user_requested"
}
```

**Response (409 Conflict):**
```json
{
  "success": false,
  "error_code": "ALREADY_COMPLETED",
  "error_message": "Cannot cancel completed task",
  "current_status": "completed",
  "completed_at": "2026-09-18T14:30:25Z"
}
```

---

## Webhook Processing Flow

### Step 1: Receive & Validate

```sql
-- 1a. Receive webhook (HTTP 202 immediately)
INSERT INTO webhook_events (
  event_id, event_type, omniroute_job_id, raw_payload, received_at, received_from_ip
) VALUES (
  $1, $2, $3, $4, NOW(), $5
) RETURNING id;

-- 1b. Verify signature asynchronously
-- (Do NOT block HTTP response on signature verification)
UPDATE webhook_events
SET 
  signature_verified = CASE 
    WHEN verify_hmac_sha256($raw_payload, $signature_provided) THEN true 
    ELSE false 
  END,
  verification_error = CASE 
    WHEN NOT verify_hmac_sha256($raw_payload, $signature_provided) 
    THEN 'HMAC verification failed' 
    ELSE NULL 
  END,
  processing_status = 'pending'
WHERE id = $event_id;

-- 1c. Reject invalid signatures (skip to retry logic)
UPDATE webhook_events
SET processing_status = 'failed', processing_error = 'Signature verification failed'
WHERE id = $event_id AND NOT signature_verified;
```

### Step 2: Idempotency Check (Prevent Duplicates)

```sql
-- Check for duplicate event (same event_id = idempotent)
SELECT id, processing_status FROM webhook_events 
WHERE event_id = $event_id LIMIT 1;

-- If already processed, skip silently
IF processing_status = 'completed' THEN
  RETURN { success: true, message: 'Duplicate event, already processed' };
END IF;

-- If processing in progress, wait (with timeout)
IF processing_status = 'processing' THEN
  WAIT 30 seconds FOR webhook_events.processing_status = 'completed';
  RETURN { success: true, message: 'Duplicate event, processing completed' };
END IF;
```

### Step 3: Link to Task Execution

```sql
-- Find task execution by omniroute_job_id
UPDATE webhook_events
SET traced_task_execution_id = (
  SELECT id FROM task_executions 
  WHERE omniroute_job_id = $omniroute_job_id
)
WHERE event_id = $event_id;

-- Mark as processing
UPDATE webhook_events
SET processing_status = 'processing', processing_started_at = NOW()
WHERE event_id = $event_id;
```

### Step 4: Update Task Execution State

```sql
-- Update task_executions with result
UPDATE task_executions
SET 
  omniroute_status = $status, -- 'completed', 'failed', 'timeout'
  omniroute_result = $result,
  execution_completed_at = NOW(),
  execution_duration_ms = EXTRACT(EPOCH FROM (NOW() - execution_started_at)) * 1000,
  status = CASE 
    WHEN $status = 'completed' THEN 'success'
    WHEN $status = 'failed' THEN 'failure'
    WHEN $status = 'timeout' THEN 'timeout'
    ELSE 'unknown'
  END,
  error_code = $error_code,
  error_message = $error_message,
  webhook_received_at = NOW(),
  webhook_event_id = $webhook_event_id,
  model_used = $model_used,
  cost_actual = $cost
WHERE omniroute_job_id = $omniroute_job_id;
```

### Step 5: Revenue Attribution (If Applicable)

```sql
-- Extract attributed revenue from result
WITH revenue_data AS (
  SELECT 
    omniroute_result->>'revenue_attributed' AS attributed_revenue,
    omniroute_result->>'attributed_deal_id' AS deal_id
  FROM task_executions
  WHERE omniroute_job_id = $omniroute_job_id
)
UPDATE task_executions
SET 
  attributed_revenue = (revenue_data.attributed_revenue)::DECIMAL,
  attributed_deal_id = revenue_data.deal_id,
  revenue_attributed_at = NOW()
FROM revenue_data
WHERE omniroute_job_id = $omniroute_job_id
  AND revenue_data.attributed_revenue IS NOT NULL;
```

### Step 6: Mark Webhook as Processed

```sql
-- Final state update
UPDATE webhook_events
SET 
  processing_status = 'completed',
  processing_completed_at = NOW()
WHERE event_id = $event_id;

-- Mark task execution as webhook-processed
UPDATE task_executions
SET webhook_processed = true, webhook_processed_at = NOW()
WHERE omniroute_job_id = $omniroute_job_id;
```

---

## Error Handling

### Timeout Recovery

**Problem:** OmniRoute job doesn't respond within 5 minutes.

```sql
-- Scheduled check (every 30 seconds)
SELECT id, omniroute_job_id, execution_started_at
FROM task_executions
WHERE status = 'running' 
  AND (NOW() - execution_started_at) > INTERVAL '5 minutes'
  AND omniroute_job_id IS NOT NULL;

-- Action: Poll OmniRoute status endpoint
GET /api/omniroute/status/{task_id}

-- Update based on polling result
UPDATE task_executions
SET 
  status = 'timeout',
  error_code = 'TIMEOUT',
  error_message = 'No response from OmniRoute after 5 minutes',
  omniroute_status = 'timeout'
WHERE id = $task_execution_id;
```

### Duplicate Event Handling

**Problem:** Same event received twice (network retry).

```sql
-- Solution: Idempotent processing via unique event_id
CREATE UNIQUE INDEX idx_webhook_events_event_id ON webhook_events(event_id);

-- If duplicate arrives:
-- 1. Check exists
SELECT processing_status FROM webhook_events WHERE event_id = $event_id;

-- 2. If already completed, return 202 (idempotent)
-- 3. If processing, wait (max 30 sec), then return 202
-- 4. If pending/failed, restart processing pipeline
```

### Partial Execution Tracking

**Problem:** Task succeeded but webhook never arrives (network partition).

```sql
-- Scheduled reconciliation (every 5 minutes)
WITH orphaned_tasks AS (
  SELECT id, omniroute_job_id, execution_started_at
  FROM task_executions
  WHERE status = 'running'
    AND (NOW() - execution_started_at) > INTERVAL '2 minutes'
    AND webhook_processed = false
)
SELECT * FROM orphaned_tasks;

-- Action: Poll OmniRoute for status
-- If job completed, create synthetic webhook event
INSERT INTO webhook_events (
  event_id, event_type, omniroute_job_id, raw_payload,
  signature_verified, processing_status
) VALUES (
  'synthetic-' || omniroute_job_id,
  'job.completed',
  omniroute_job_id,
  (SELECT omniroute_result FROM task_executions WHERE id = $task_id),
  true, -- Skip signature verification for synthetic events
  'pending'
);
```

### Retry Logic for Failed Webhooks

```sql
-- Failed webhook events get retried
WITH failed_webhooks AS (
  SELECT id, retry_count, processing_error
  FROM webhook_events
  WHERE processing_status = 'failed' AND retry_count < max_retries
)
UPDATE webhook_events
SET 
  retry_count = retry_count + 1,
  next_retry_at = NOW() + INTERVAL '1 second' * POWER(2, retry_count), -- Exponential backoff
  processing_status = 'pending'
WHERE id IN (SELECT id FROM failed_webhooks);

-- Scheduled retry processor (every 10 seconds)
SELECT * FROM webhook_events
WHERE processing_status = 'pending'
  AND next_retry_at <= NOW()
ORDER BY next_retry_at ASC
LIMIT 100;
```

---

## API Response Schemas

### Task Invocation Request

```json
{
  "type": "object",
  "required": ["task_id", "task_type", "domain", "input_params"],
  "properties": {
    "task_id": { "type": "string", "pattern": "^TASK-[0-9]{10}-[0-9]{3}$" },
    "task_type": { "enum": ["agent_invocation", "workflow", "revenue_attribution", "verification"] },
    "domain": { "type": "string", "minLength": 3, "maxLength": 50 },
    "requested_agent": { "type": "string", "pattern": "^AGT-[0-9]{3}$" },
    "requested_capability": { "type": "string" },
    "input_params": { "type": "object", "additionalProperties": {} },
    "priority": { "type": "integer", "minimum": 1, "maximum": 10 },
    "timeout_seconds": { "type": "integer", "minimum": 30, "maximum": 3600 },
    "webhook_url": { "type": "string", "format": "uri" },
    "idempotency_key": { "type": "string", "minLength": 20, "maxLength": 100 }
  }
}
```

### Task Status Response

```json
{
  "type": "object",
  "required": ["task_id", "status"],
  "properties": {
    "task_id": { "type": "string" },
    "omniroute_job_id": { "type": "string" },
    "status": { "enum": ["pending", "queued", "running", "completed", "failed", "timeout", "cancelled"] },
    "progress_pct": { "type": "integer", "minimum": 0, "maximum": 100 },
    "started_at": { "type": "string", "format": "date-time" },
    "completed_at": { "type": "string", "format": "date-time" },
    "duration_ms": { "type": "integer" },
    "assigned_agent": { "type": "string" },
    "model_used": { "type": "string" },
    "result": { "type": "object" },
    "cost": { "type": "number" },
    "error_code": { "type": "string" },
    "error_message": { "type": "string" }
  }
}
```

### Webhook Event Payload

```json
{
  "type": "object",
  "required": ["event_id", "event_type", "timestamp", "omniroute_job_id", "status"],
  "properties": {
    "event_id": { "type": "string", "pattern": "^evt-[0-9]{4}-[0-9]{2}-[0-9]{2}" },
    "event_type": { "enum": ["job.completed", "job.failed", "job.timeout", "job.cancelled"] },
    "timestamp": { "type": "string", "format": "date-time" },
    "omniroute_job_id": { "type": "string" },
    "task_id": { "type": "string" },
    "status": { "type": "string" },
    "result": { "type": "object" },
    "execution_duration_ms": { "type": "integer" },
    "assigned_agent": { "type": "string" },
    "model_used": { "type": "string" },
    "tokens_used": {
      "type": "object",
      "properties": {
        "input": { "type": "integer" },
        "output": { "type": "integer" }
      }
    },
    "cost": { "type": "number" }
  }
}
```

### Error Response

```json
{
  "type": "object",
  "required": ["success", "error_code", "error_message"],
  "properties": {
    "success": { "type": "boolean", "const": false },
    "error_code": { "type": "string", "pattern": "^[A-Z_]+$" },
    "error_message": { "type": "string" },
    "details": { "type": "object" },
    "request_id": { "type": "string" },
    "timestamp": { "type": "string", "format": "date-time" }
  }
}
```

---

## Monitoring Tables & Queries

### Invocation Success Rate (Hourly)

```sql
SELECT 
  DATE_TRUNC('hour', created_at) AS metric_hour,
  COUNT(*) AS total_tasks,
  COUNT(*) FILTER (WHERE status = 'success') AS successful_tasks,
  ROUND(100.0 * COUNT(*) FILTER (WHERE status = 'success') / COUNT(*), 2) AS success_pct
FROM task_executions
WHERE created_at >= NOW() - INTERVAL '24 hours'
GROUP BY DATE_TRUNC('hour', created_at)
ORDER BY metric_hour DESC;
```

### Latency Percentiles

```sql
SELECT 
  PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY execution_duration_ms) AS p50_ms,
  PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY execution_duration_ms) AS p95_ms,
  PERCENTILE_CONT(0.99) WITHIN GROUP (ORDER BY execution_duration_ms) AS p99_ms,
  MAX(execution_duration_ms) AS max_ms,
  AVG(execution_duration_ms) AS avg_ms
FROM task_executions
WHERE status = 'success' AND created_at >= NOW() - INTERVAL '24 hours';
```

### Cost Tracking by Model

```sql
SELECT 
  model_used,
  COUNT(*) AS invocation_count,
  SUM(cost_actual) AS total_cost,
  AVG(cost_actual) AS avg_cost_per_task,
  MIN(cost_actual) AS min_cost,
  MAX(cost_actual) AS max_cost
FROM task_executions
WHERE cost_actual IS NOT NULL AND created_at >= NOW() - INTERVAL '7 days'
GROUP BY model_used
ORDER BY total_cost DESC;
```

### Webhook Delivery Reliability

```sql
SELECT 
  DATE_TRUNC('hour', received_at) AS metric_hour,
  COUNT(*) AS events_received,
  COUNT(*) FILTER (WHERE processing_status = 'completed') AS events_processed,
  ROUND(100.0 * COUNT(*) FILTER (WHERE processing_status = 'completed') / COUNT(*), 2) AS processing_success_pct,
  AVG(EXTRACT(EPOCH FROM (processing_completed_at - received_at))) AS avg_processing_lag_sec
FROM webhook_events
WHERE received_at >= NOW() - INTERVAL '24 hours'
GROUP BY DATE_TRUNC('hour', received_at)
ORDER BY metric_hour DESC;
```

### Error Codes Breakdown

```sql
SELECT 
  error_code,
  COUNT(*) AS error_count,
  COUNT(*) FILTER (WHERE retry_count > 0) AS retried,
  COUNT(*) FILTER (WHERE retry_count >= max_retries) AS exhausted_retries
FROM task_executions
WHERE status IN ('failure', 'timeout') 
  AND created_at >= NOW() - INTERVAL '24 hours'
GROUP BY error_code
ORDER BY error_count DESC;
```

### Revenue Attribution Pipeline

```sql
SELECT 
  DATE_TRUNC('day', revenue_attributed_at) AS attribution_date,
  COUNT(DISTINCT omniroute_job_id) AS tasks_with_revenue,
  SUM(attributed_revenue) AS total_attributed_revenue,
  AVG(attributed_revenue) AS avg_revenue_per_task,
  COUNT(DISTINCT attributed_deal_id) AS deals_attributed
FROM task_executions
WHERE revenue_attributed_at >= NOW() - INTERVAL '30 days'
GROUP BY DATE_TRUNC('day', revenue_attributed_at)
ORDER BY attribution_date DESC;
```

---

## Security & Validation

### Signature Verification (HMAC-SHA256)

```python
import hmac
import hashlib
import json

def verify_webhook_signature(payload_bytes, provided_signature, secret):
    """Verify OmniRoute webhook signature."""
    expected_sig = 'hmac-sha256=' + hmac.new(
        secret.encode(),
        payload_bytes,
        hashlib.sha256
    ).hexdigest()
    
    return hmac.compare_digest(expected_sig, provided_signature)

# Usage
raw_body = request.get_data()  # Raw HTTP body (do NOT parse JSON first)
signature = request.headers.get('X-Omniroute-Signature')
verified = verify_webhook_signature(raw_body, signature, OMNIROUTE_SECRET)
```

### Input Validation

```sql
-- Prevent SQL injection via input_params
UPDATE task_executions
SET input_params = JSONB_STRIP_NULLS($input_params)
WHERE id = $task_id;

-- Validate JSON structure
DO $$
BEGIN
  PERFORM input_params FROM task_executions WHERE id = $task_id;
EXCEPTION WHEN others THEN
  RAISE EXCEPTION 'Invalid JSON in input_params';
END $$;
```

### Rate Limiting

```sql
-- Per-user rate limit (100 tasks/hour)
WITH user_invocations AS (
  SELECT COUNT(*) AS count
  FROM task_executions
  WHERE source_user_id = $user_id 
    AND created_at >= NOW() - INTERVAL '1 hour'
)
SELECT CASE 
  WHEN count > 100 THEN 'RATE_LIMIT_EXCEEDED'
  ELSE 'OK'
END AS rate_limit_status
FROM user_invocations;
```

---

## Deployment Checklist

- [ ] All tables created with indexes
- [ ] Foreign key constraints validated
- [ ] Signature verification code deployed
- [ ] Webhook handler containerized & scaled
- [ ] Monitoring alerts configured (latency p99, error rates)
- [ ] Retry logic tested (network partitions, duplicates)
- [ ] Revenue attribution pipeline verified
- [ ] Cost tracking enabled on all models
- [ ] Orchestrator Prime → OmniRoute integration tested E2E
- [ ] Webhook delivery tested (with signature validation)
- [ ] Reconciliation scheduled (orphaned tasks, duplicate events)
- [ ] Database backups scheduled (task_executions, webhook_events)

---

## See Also

- `ORCHESTRATOR-PRIME-QUICK-REFERENCE.md` — Command reference & CLI usage
- `ORCHESTRATOR-PRIME-CLAUDE-HAIKU-IMPLEMENTATION.md` — Implementation details
- `20-DECISIONS/PHASE-2A-AGENTIC-ENGINEERING-PLAN.md` — Agent deployment timeline
- Neo4j agent discovery patterns (AGENT_REGISTRY.yaml)
- OmniRoute API documentation (internal)

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>
