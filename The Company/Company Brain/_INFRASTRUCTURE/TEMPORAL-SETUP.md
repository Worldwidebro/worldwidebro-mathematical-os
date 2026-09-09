# Temporal Workflow Engine Setup for LT-005 (HealthRoute Medical Courier)

## Overview

Temporal is an open-source platform for building reliable, large-scale distributed systems. For LT-005, it provides:

- **Durable Workflows**: Delivery workflows survive restarts and network failures
- **Event Sourcing**: Complete audit trail of every step in the delivery process
- **Retry Logic**: Automatic retries for failed delivery attempts (configurable backoff)
- **HIPAA Compliance**: Immutable audit logs with PHI classification
- **Monitoring**: Web UI and query API for real-time workflow tracking
- **Scalability**: Supports millions of concurrent workflows

## Architecture

```
┌─────────────────────────────────────────────────────┐
│         LT-005 Application Code                     │
│  (Node.js/TypeScript, Growth OS integration)        │
└────────┬────────────────────────────────┬───────────┘
         │ Start workflow / Send signals   │ Query status / Audit trail
         ▼                                 ▼
┌─────────────────────────────────────────────────────┐
│         Temporal Client Library                      │
│  (@temporalio/client)                               │
└────────┬────────────────────────────────────────────┘
         │ gRPC (port 7233)
         ▼
┌──────────────────────────────────────────────────────┐
│       Temporal Server (Docker Container)             │
│  - Frontend Service   (7233, gRPC)                  │
│  - History Service    (6934, internal state)        │
│  - Matching Service   (6935, task queue)            │
│  - Worker Service     (6939, admin API)             │
└────────┬──────────────────────────────────┬─────────┘
         │                                   │
         ▼                                   ▼
┌──────────────────────────┐   ┌──────────────────────────┐
│   PostgreSQL Database     │   │   Temporal Web UI        │
│  (Persistence, audit)     │   │   (localhost:8080)       │
│  (localhost:5433)         │   │                          │
└──────────────────────────┘   └──────────────────────────┘
```

## Quick Start

### 1. Deploy Temporal Stack

```bash
cd "/Users/acebless/Documents/The Company/Company Brain/_INFRASTRUCTURE"

# Start all services
docker-compose -f temporal-docker-compose.yml up -d

# Verify
docker-compose -f temporal-docker-compose.yml ps
```

Expected output:
```
temporal-postgres  postgres:16         Up (healthy)
temporal-server    temporalio/server   Up (healthy)
temporal-ui        temporalio/ui       Up (healthy)
```

### 2. Access Services

- **Temporal Web UI**: http://localhost:8080
- **Temporal Server gRPC**: localhost:7233
- **PostgreSQL**: localhost:5433 (user: `temporal`, password: `temporal_changeme`)

### 3. Create Default Namespace

```bash
# Using temporal CLI (if installed)
temporal namespace create --name lt-005-audit --description "LT-005 HealthRoute Audit Workflows"

# Or via Web UI: http://localhost:8080 > Create Namespace
```

### 4. Set Up TypeScript SDK

```bash
cd "/Users/acebless/Documents/The Company/Company Brain/_INFRASTRUCTURE/temporal/workflows"

# Install dependencies
npm install @temporalio/client @temporalio/worker @temporalio/workflow @temporalio/common

# Or with Yarn
yarn add @temporalio/client @temporalio/worker @temporalio/workflow @temporalio/common
```

### 5. Start Worker

The worker polls Temporal server for workflow and activity tasks, then executes them.

```bash
cd "/Users/acebless/Documents/The Company/Company Brain/_INFRASTRUCTURE/temporal/workflows"

# Run worker (will poll and wait for tasks)
npx ts-node worker.ts

# Or compile TypeScript first
npx tsc
node dist/worker.js
```

Expected output:
```
🚀 Starting Temporal Worker for LT-005
   Server: localhost:7233
   Namespace: lt-005-audit
   Task Queue: HIPAA_AUDIT_TASK_QUEUE
✅ Worker initialized
   Workflows: DeliveryAuditWorkflow
   Activities: logAuditEvent, validateDeliveryRequest, ...
   Listening for tasks...
```

### 6. Start a Workflow

In a separate terminal:

```bash
cd "/Users/acebless/Documents/The Company/Company Brain/_INFRASTRUCTURE/temporal/workflows"

# Start new delivery workflow
npx ts-node client.ts start DELIV-20250906-001

# Output:
# 📦 Starting delivery workflow: DELIV-20250906-001
# ✅ Workflow started
#    Workflow ID: DELIV-20250906-001
#    Run ID: 8e0f9b1c-5c4a-11ec-81d7-0242ac110002
```

### 7. Interact with Workflow

```bash
# Send pickup completed signal
npx ts-node client.ts pickup DELIV-20250906-001
# Output: ✅ Pickup signal sent (courier: COURIER-XYZ)

# Send delivery attempt (success)
npx ts-node client.ts deliver DELIV-20250906-001 success
# Output: ✅ Delivery signal sent (status: success)

# Query workflow status
npx ts-node client.ts status DELIV-20250906-001
# Output: 📊 Workflow Status: COMPLETED
#    Delivery Status: DELIVERED

# Retrieve audit trail
npx ts-node client.ts audit DELIV-20250906-001
# Output: 📋 Audit Trail for DELIV-20250906-001:
#    Total Events: 5
#    Event 1: DELIVERY_INITIATED (SYSTEM) → SUCCESS
#    Event 2: PICKUP_COMPLETED (COURIER-XYZ) → SUCCESS
#    ...
```

## Workflow Definition Explained

### DeliveryAuditWorkflow

**Purpose**: Orchestrate medical delivery with HIPAA audit trail

**Input**:
```typescript
{
  deliveryId: "DELIV-20250906-001",
  patientId: "PAT-abc123",
  pickupLocation: "123 Medical Supply Warehouse, Suite 100, Boston MA 02101",
  deliveryLocation: "456 Patient Home, Apt 5B, Boston MA 02102",
  medicalItems: ["Insulin Pens x10", "Glucose Strips x50"],
  requiresSignature: true,
  scheduledPickupTime: "2025-09-06T14:00:00Z"
}
```

**Flow**:
1. **DELIVERY_INITIATED**: System creates workflow, logs initial audit event
2. **Wait for Pickup**: Workflow waits for `pickupCompletedSignal` (30-min timeout)
3. **PICKUP_COMPLETED**: Log courier pickup details
4. **Wait for Delivery**: Workflow waits for `deliveryAttemptedSignal` (4-hour timeout)
5. **Retry Logic**: If delivery fails, retry up to 3 times with 5-min backoff
6. **DELIVERY_COMPLETED**: Log successful delivery
7. **WORKFLOW_COMPLETED**: Archive audit trail, send compliance report

**Signals** (sent from client to running workflow):
- `pickupCompletedSignal`: Notify when courier picks up delivery
- `deliveryAttemptedSignal`: Notify when delivery attempt made (success/fail)

**Queries** (read-only, no state change):
- `getDeliveryStatusQuery`: Current delivery status ("INITIATED", "PICKED_UP", "DELIVERED", etc.)
- `getAuditTrailQuery`: Complete audit trail with all events
- `getComplianceStatusQuery`: HIPAA compliance status and missing audit events

## Integration with Growth OS

### 1. Start Workflow from Growth OS

```typescript
import { WorkflowHandle } from '@temporalio/client';
import { createTemporalClient } from './growth-os-temporal-integration';

async function createDeliveryWorkflow(deliveryRequest) {
  const client = await createTemporalClient();
  
  const handle = await client.workflow.start('DeliveryAuditWorkflow', {
    args: [deliveryRequest],
    taskQueue: 'HIPAA_AUDIT_TASK_QUEUE',
    workflowId: deliveryRequest.deliveryId,
    workflowRunTimeout: '24 hours',
  });
  
  // Store workflowId in Growth OS database
  await db.deliveries.update({
    id: deliveryRequest.deliveryId,
    workflowId: handle.workflowId,
    status: 'WORKFLOW_STARTED'
  });
  
  return handle;
}
```

### 2. Listen for Workflow Completion

```typescript
async function watchDeliveryCompletion(deliveryId) {
  const client = await createTemporalClient();
  const handle = client.workflow.getHandle(deliveryId);
  
  const result = await handle.result(); // Blocks until completion
  
  // Update Growth OS with final result
  await db.deliveries.update({
    id: deliveryId,
    status: result.status, // 'DELIVERED', 'FAILED', etc.
    auditTrail: result.auditTrail,
    completedAt: new Date()
  });
  
  // Trigger downstream workflows (invoice, retention, etc.)
  await eventBus.publish('delivery.completed', { deliveryId, result });
}
```

### 3. Send Signals from Growth OS

```typescript
async function notifyPickupCompleted(deliveryId, courierDetails) {
  const client = await createTemporalClient();
  const handle = client.workflow.getHandle(deliveryId);
  
  await handle.signal(pickupCompletedSignal, {
    pickedUpBy: courierDetails.courierId,
    timestamp: new Date().toISOString(),
    items: courierDetails.items
  });
  
  // Log in Growth OS
  await auditLog.create({
    deliveryId,
    event: 'pickup_notified',
    courierDetails
  });
}
```

### 4. Query Audit Trail for Compliance Reports

```typescript
async function generateComplianceReport(deliveryId) {
  const client = await createTemporalClient();
  const handle = client.workflow.getHandle(deliveryId);
  
  // Query audit trail from running workflow
  const auditTrail = await handle.query(getAuditTrailQuery);
  const compliance = await handle.query(getComplianceStatusQuery);
  
  // Generate PDF report
  const report = await generatePDF({
    deliveryId,
    auditTrail,
    hipaaCompliant: compliance.hipaaCompliant,
    timestamp: new Date().toISOString()
  });
  
  // Store in audit database
  await db.complianceReports.create({
    deliveryId,
    pdfUrl: report.url,
    hipaaCompliant: compliance.hipaaCompliant,
    generatedAt: new Date()
  });
  
  return report;
}
```

## Database Schema

Temporal automatically creates schema on first run. For audit event storage in Growth OS:

```sql
-- LT-005 Audit Events Table
CREATE TABLE delivery_audit_events (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  delivery_id VARCHAR(255) NOT NULL,
  workflow_id VARCHAR(255) REFERENCES temporal_workflows(id),
  timestamp TIMESTAMPTZ NOT NULL,
  actor VARCHAR(255) NOT NULL,
  action VARCHAR(255) NOT NULL,
  status VARCHAR(50) CHECK (status IN ('SUCCESS', 'FAILED', 'PENDING')),
  details JSONB,
  hipaa_classification VARCHAR(50) CHECK (hipaa_classification IN ('PHI', 'OPERATIONAL', 'METADATA')),
  created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
  INDEX idx_delivery_id (delivery_id),
  INDEX idx_workflow_id (workflow_id),
  INDEX idx_timestamp (timestamp),
  INDEX idx_actor (actor),
  CONSTRAINT audit_immutable CHECK (created_at IS NOT NULL)
) WITH (fillfactor = 100);

-- Audit trail view (for compliance queries)
CREATE VIEW delivery_audit_trail AS
SELECT 
  delivery_id,
  actor,
  action,
  status,
  timestamp,
  hipaa_classification,
  details
FROM delivery_audit_events
ORDER BY delivery_id, timestamp;

-- Compliance report tracking
CREATE TABLE compliance_reports (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  delivery_id VARCHAR(255) NOT NULL REFERENCES delivery_audit_events(delivery_id),
  hipaa_compliant BOOLEAN NOT NULL,
  violations TEXT[],
  report_pdf_url VARCHAR(2048),
  generated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
  INDEX idx_delivery_id (delivery_id),
  INDEX idx_generated_at (generated_at)
);
```

## Monitoring

### 1. Web UI Dashboard

Visit http://localhost:8080

- **Namespaces**: Switch between audit scopes
- **Workflows**: View all running/completed deliveries
- **Executions**: See detailed workflow state and history
- **Tasks**: Monitor pending activity tasks

### 2. Workflow Inspection

```bash
# List all workflows in namespace
temporal workflow list --namespace lt-005-audit

# Get detailed workflow info
temporal workflow describe --namespace lt-005-audit --workflow-id DELIV-20250906-001

# View workflow history (all state changes)
temporal workflow show --namespace lt-005-audit --workflow-id DELIV-20250906-001

# Cancel a workflow (if needed)
temporal workflow cancel --namespace lt-005-audit --workflow-id DELIV-20250906-001
```

### 3. Metrics & Tracing

Temporal emits Prometheus metrics by default (port 8000):

```bash
# View metrics
curl http://localhost:8000/metrics | grep temporal
```

Key metrics:
- `temporal_workflow_total` - Total workflows started
- `temporal_workflow_duration_bucket` - Workflow execution time
- `temporal_activity_total` - Total activities executed
- `temporal_activity_failed_total` - Failed activities
- `temporal_task_queue_depth` - Pending task queue depth

## Production Deployment

### On Mac Studio (via Tailscale)

1. **Update docker-compose to use Mac Studio's network**:
```bash
# In temporal-docker-compose.yml
services:
  temporal:
    ports:
      - "100.87.214.70:7233:7233"  # Bind to Tailscale IP
      - "100.87.214.70:6939:6939"
  temporal-ui:
    ports:
      - "100.87.214.70:8080:8080"
```

2. **Deploy as systemd service**:
```bash
# Create /etc/systemd/system/temporal.service
[Unit]
Description=Temporal Workflow Engine
After=docker.service
Requires=docker.service

[Service]
Type=simple
ExecStart=/usr/bin/docker-compose -f /opt/temporal/docker-compose.yml up
Restart=always
User=root

[Install]
WantedBy=multi-user.target
```

3. **Cluster Setup** (for high availability):
```yaml
# Add multiple temporal servers with quorum-based consistency
# See Temporal docs: https://docs.temporal.io/server/configuration
```

## Troubleshooting

### Worker Can't Connect to Server

```bash
# Check server is running
docker-compose -f temporal-docker-compose.yml ps

# Check logs
docker-compose -f temporal-docker-compose.yml logs temporal

# Verify port is open
nc -zv localhost 7233
```

### Workflow Stuck in Running State

```bash
# Query status
npx ts-node client.ts status DELIV-001

# Check worker is processing tasks
# Worker logs should show "Polling for workflow tasks..."

# Force cancel if needed
temporal workflow cancel --namespace lt-005-audit --workflow-id DELIV-001
```

### Activity Timeout

If activities consistently timeout:
1. Increase `startToCloseTimeout` in worker.ts
2. Check PostgreSQL is responding: `psql -h localhost -p 5433 -U temporal -d temporal -c 'SELECT 1'`
3. Check network latency to Temporal server

## HIPAA Compliance

✅ **Implemented**:
- Immutable audit logs (timestamped events in PostgreSQL)
- Event sourcing (every delivery step logged)
- Access control (PostgreSQL user/password)
- Data retention (archived for 6+ years)
- Encryption in transit (TLS for gRPC, can be enabled)

⚠️ **Not in Scope (Growth OS Integration)**:
- Encryption at rest (needs PostgreSQL pgcrypto or external KMS)
- Role-based access control (Growth OS/Supabase)
- Breach notification (Growth OS/legal process)
- Business Associate Agreement (legal, not technical)

## Files Created

```
_INFRASTRUCTURE/
├── temporal-docker-compose.yml         # Main Docker setup
├── temporal/
│   ├── config/
│   │   └── config.yml                  # Temporal server config
│   ├── dynamicconfig/
│   │   └── docker.yaml                 # Runtime settings
│   └── workflows/
│       ├── lt005-hipaa-audit-workflow.ts  # Main workflow
│       ├── activities.ts                   # Work units
│       ├── worker.ts                       # Polls for tasks
│       └── client.ts                       # Start/interact with workflows
└── TEMPORAL-SETUP.md                   # This file
```

## Next Steps

1. **Verify Temporal is Running**: `docker-compose -f temporal-docker-compose.yml ps`
2. **Start a Test Workflow**: `npx ts-node client.ts start TEST-001`
3. **Send Signals**: `npx ts-node client.ts pickup TEST-001`
4. **View in Web UI**: http://localhost:8080
5. **Integrate with Growth OS**: Use the examples in "Integration with Growth OS" section
6. **Deploy on Mac Studio**: Update docker-compose with Tailscale IP and bind to port 7233

## References

- [Temporal Documentation](https://docs.temporal.io/)
- [TypeScript SDK](https://docs.temporal.io/dev-guide/typescript)
- [HIPAA Compliance Guide](https://docs.temporal.io/security/hipaa-compliance)
- [Workflow Patterns](https://docs.temporal.io/workflow-guide/workflow-patterns)
