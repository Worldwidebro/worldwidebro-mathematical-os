# Temporal Workflow Integration for LT-005 Growth OS

**Venture**: LT-005 (HealthRoute Medical Courier)  
**Purpose**: HIPAA-compliant delivery audit workflow orchestration  
**Status**: Ready for local development  
**Last Updated**: 2026-09-08

## Overview

This document describes how LT-005's Growth OS application integrates with Temporal, a durable workflow engine that provides:

- **State Durability**: Delivery workflows survive server restarts
- **Event Sourcing**: Complete immutable audit trail for HIPAA compliance
- **Automatic Retries**: Failed deliveries retry with exponential backoff
- **Monitoring Dashboard**: Real-time visibility into all deliveries
- **Compliance Reporting**: Automated audit trail export for regulatory reviews

## Architecture

```
Growth OS App (Node.js)
    ↓ HTTP / Event
    ├─ Start delivery workflow
    ├─ Send pickup/delivery signals
    └─ Query audit trail & status
    ↓
Temporal Client SDK
    ↓ gRPC
Temporal Server (Docker)
    ├─ Frontend Service (7233) - Client communication
    ├─ History Service (6934) - State management
    ├─ Matching Service (6935) - Task distribution
    └─ Worker Service (6939) - Admin API
    ↓
PostgreSQL (5433)
    └─ Immutable audit event log
```

## Workflow: Medical Delivery with Audit Trail

### Delivery Process

```
1. Growth OS creates delivery record
    ↓
2. Start DeliveryAuditWorkflow (Temporal)
    - Logs: DELIVERY_INITIATED
    ↓
3. Wait for pickup (30-min timeout)
    - Courier picks up medical items
    - Growth OS sends: pickupCompletedSignal
    - Logs: PICKUP_COMPLETED
    ↓
4. Wait for delivery (4-hour timeout, 3 retries)
    - Courier attempts delivery
    - Growth OS sends: deliveryAttemptedSignal
    - Status: success or failed
    ↓
5. If delivery succeeds:
    - Logs: DELIVERY_COMPLETED
    - Archive audit trail
    - Update Growth OS status
    ↓
6. If delivery fails:
    - Retry up to 3 times (5-min backoff)
    - If all fail: Logs: DELIVERY_TIMEOUT → manual intervention
    ↓
7. Workflow completes
    - Logs: DELIVERY_WORKFLOW_COMPLETED
    - Compliance check: All required audits present?
    - Archive to long-term storage
```

### Data Model

**DeliveryRequest** (input to workflow):
```typescript
{
  deliveryId: string;           // Unique delivery ID
  patientId: string;            // Patient identifier (PHI)
  pickupLocation: string;       // Warehouse address
  deliveryLocation: string;     // Patient home address (PHI)
  medicalItems: string[];       // List of items being delivered
  requiresSignature: boolean;   // Signature requirement
  scheduledPickupTime: string;  // ISO 8601 timestamp
}
```

**AuditEvent** (immutable log entry):
```typescript
{
  timestamp: string;                        // ISO 8601, server time
  deliveryId: string;                       // Which delivery?
  actor: string;                            // Who did it? (SYSTEM, COURIER-ID, etc.)
  action: string;                           // What happened? (DELIVERY_INITIATED, PICKUP_COMPLETED, etc.)
  status: 'SUCCESS' | 'FAILED' | 'PENDING'; // Outcome
  details: Record<string, any>;             // Structured context
  hipaaClassification: 'PHI' | 'OPERATIONAL' | 'METADATA';  // Data sensitivity
}
```

## Setup Instructions

### 1. Install Temporal Stack

```bash
cd "/Users/acebless/Documents/The Company/Company Brain/_INFRASTRUCTURE"

# Start services (Temporal server + PostgreSQL + Web UI)
docker-compose -f temporal-docker-compose.yml up -d

# Verify
docker-compose -f temporal-docker-compose.yml ps
```

### 2. Create Default Namespace

Via Web UI (http://localhost:8080):
1. Click "Create a Namespace"
2. Name: `lt-005-audit`
3. Description: "LT-005 HealthRoute Delivery Audits"
4. Click "Create"

Or via CLI:
```bash
temporal namespace create --name lt-005-audit --description "LT-005 HealthRoute Audit Workflows"
```

### 3. Install SDK & Dependencies

```bash
cd "/Users/acebless/Documents/The Company/Company Brain/_INFRASTRUCTURE/temporal/workflows"

npm install
# or
yarn install
```

### 4. Start Worker

This polls Temporal for workflow and activity tasks:

```bash
npm run worker

# Output:
# 🚀 Starting Temporal Worker for LT-005
#    Server: localhost:7233
#    Namespace: lt-005-audit
#    Task Queue: HIPAA_AUDIT_TASK_QUEUE
# ✅ Worker initialized
#    Workflows: DeliveryAuditWorkflow
#    Listening for tasks...
```

Keep this terminal open while testing.

### 5. Start a Test Delivery

In another terminal:

```bash
cd "/Users/acebless/Documents/The Company/Company Brain/_INFRASTRUCTURE/temporal/workflows"

# Start workflow
npm run client -- start DELIV-20250908-001

# Send pickup signal
npm run client -- pickup DELIV-20250908-001

# Send delivery signal (success)
npm run client -- deliver DELIV-20250908-001 success

# Check status
npm run client -- status DELIV-20250908-001

# View audit trail
npm run client -- audit DELIV-20250908-001
```

## Integration with Growth OS

### 1. Install Temporal Client in Growth OS App

```bash
npm install @temporalio/client @temporalio/workflow
```

### 2. Create Temporal Helper Module

```typescript
// src/lib/temporal.ts
import { Connection, Client } from '@temporalio/client';

const TEMPORAL_SERVER = process.env.TEMPORAL_SERVER || 'localhost:7233';
const TEMPORAL_NAMESPACE = 'lt-005-audit';
const TASK_QUEUE = 'HIPAA_AUDIT_TASK_QUEUE';

let client: Client | null = null;

export async function getTemporalClient(): Promise<Client> {
  if (!client) {
    const connection = await Connection.connect({ address: TEMPORAL_SERVER });
    client = new Client({ connection, namespace: TEMPORAL_NAMESPACE });
  }
  return client;
}

export async function closeTemporalClient(): Promise<void> {
  if (client) {
    await client.connection.close();
    client = null;
  }
}
```

### 3. Start Workflow from Growth OS

```typescript
// src/services/delivery.ts
import { getTemporalClient } from '@/lib/temporal';
import { DeliveryRequest } from '../types';

export async function createDeliveryWorkflow(deliveryRequest: DeliveryRequest) {
  const client = await getTemporalClient();
  
  const handle = await client.workflow.start('DeliveryAuditWorkflow', {
    args: [deliveryRequest],
    taskQueue: 'HIPAA_AUDIT_TASK_QUEUE',
    workflowId: deliveryRequest.deliveryId,
    workflowRunTimeout: '24 hours',
  });
  
  // Store workflow handle in Growth OS database
  await db.deliveries.update(deliveryRequest.deliveryId, {
    workflowId: handle.workflowId,
    status: 'WORKFLOW_STARTED',
    startedAt: new Date(),
  });
  
  return handle;
}
```

### 4. Send Signals from Growth OS

```typescript
// When courier picks up delivery
export async function notifyPickupCompleted(deliveryId: string, courierDetails: any) {
  const client = await getTemporalClient();
  const handle = client.workflow.getHandle(deliveryId);
  
  await handle.signal('pickupCompleted', {
    pickedUpBy: courierDetails.courierId,
    timestamp: new Date().toISOString(),
    items: courierDetails.items,
  });
  
  // Update Growth OS
  await db.deliveries.update(deliveryId, {
    status: 'PICKED_UP',
    courierDetails,
    pickedUpAt: new Date(),
  });
}

// When delivery is attempted
export async function notifyDeliveryAttempted(
  deliveryId: string,
  status: 'success' | 'failed',
  reason?: string
) {
  const client = await getTemporalClient();
  const handle = client.workflow.getHandle(deliveryId);
  
  await handle.signal('deliveryAttempted', {
    attemptedAt: new Date().toISOString(),
    status,
    reason,
  });
  
  // Update Growth OS
  await db.deliveries.update(deliveryId, {
    status: status === 'success' ? 'DELIVERED' : 'DELIVERY_FAILED',
    deliveredAt: status === 'success' ? new Date() : undefined,
    failureReason: reason,
  });
}
```

### 5. Query Status & Audit Trail

```typescript
// Real-time delivery status
export async function getDeliveryStatus(deliveryId: string): Promise<string> {
  const client = await getTemporalClient();
  const handle = client.workflow.getHandle(deliveryId);
  
  return await handle.query('getDeliveryStatus');
}

// Audit trail for compliance
export async function getDeliveryAuditTrail(deliveryId: string): Promise<AuditEvent[]> {
  const client = await getTemporalClient();
  const handle = client.workflow.getHandle(deliveryId);
  
  const auditTrail = await handle.query('getAuditTrail');
  
  // Store in Growth OS audit database
  await db.auditTrails.create({
    deliveryId,
    events: auditTrail,
    retrievedAt: new Date(),
  });
  
  return auditTrail;
}

// HIPAA compliance check
export async function checkComplianceStatus(deliveryId: string): Promise<{
  hipaaCompliant: boolean;
  missingAudits: string[];
}> {
  const client = await getTemporalClient();
  const handle = client.workflow.getHandle(deliveryId);
  
  return await handle.query('getComplianceStatus');
}
```

### 6. Background Job: Wait for Completion

```typescript
// src/jobs/delivery-completion-listener.ts
// Runs in background (Node worker, Bull job, etc.)

export async function watchDeliveryCompletion(deliveryId: string) {
  const client = await getTemporalClient();
  const handle = client.workflow.getHandle(deliveryId);
  
  try {
    const result = await handle.result(); // Blocks until completion
    
    // Update Growth OS with final result
    await db.deliveries.update(deliveryId, {
      status: result.status, // 'DELIVERED', 'FAILED', etc.
      completedAt: new Date(),
      auditTrailCount: result.auditTrail.length,
    });
    
    // Trigger downstream workflows
    await eventBus.publish('delivery.completed', {
      deliveryId,
      status: result.status,
      auditTrail: result.auditTrail,
    });
    
    // Automated compliance report
    const compliance = await checkComplianceStatus(deliveryId);
    if (!compliance.hipaaCompliant) {
      await eventBus.publish('delivery.compliance_violation', {
        deliveryId,
        violations: compliance.missingAudits,
      });
    }
  } catch (err) {
    console.error(`Delivery workflow failed: ${deliveryId}`, err);
    await db.deliveries.update(deliveryId, {
      status: 'WORKFLOW_ERROR',
      error: err.message,
    });
  }
}
```

## Environment Configuration

### .env (Development)

```bash
# Temporal Server
TEMPORAL_SERVER=localhost:7233
TEMPORAL_NAMESPACE=lt-005-audit

# Database (for storing workflow references)
DATABASE_URL=postgresql://user:password@localhost:5432/lt_005_growth_os

# Audit Logging
AUDIT_LOG_LEVEL=info
AUDIT_RETENTION_DAYS=2555  # 7 years for HIPAA
```

### .env (Production on Mac Studio)

```bash
# Temporal Server (via Tailscale)
TEMPORAL_SERVER=100.87.214.70:7233
TEMPORAL_NAMESPACE=lt-005-audit

# Database
DATABASE_URL=postgresql://user:password@100.87.214.70:5432/lt_005_growth_os

# TLS (optional but recommended)
TEMPORAL_TLS_ENABLED=true
TEMPORAL_TLS_CERT_PATH=/etc/temporal/certs/client.pem
TEMPORAL_TLS_KEY_PATH=/etc/temporal/certs/key.pem
TEMPORAL_TLS_CA_PATH=/etc/temporal/certs/ca.pem
```

## Monitoring & Debugging

### 1. Web UI Dashboard

Visit http://localhost:8080

- **Namespaces**: lt-005-audit
- **Workflows**: See all deliveries (running, completed, failed)
- **Workflow Details**: Click a delivery to see:
  - Execution history (every state change)
  - Pending activities
  - Current state
  - Input/output

### 2. CLI Inspection

```bash
# List all deliveries in namespace
temporal workflow list --namespace lt-005-audit

# Get details of specific delivery
temporal workflow describe --namespace lt-005-audit --workflow-id DELIV-20250908-001

# View complete history (event sourcing)
temporal workflow show --namespace lt-005-audit --workflow-id DELIV-20250908-001

# Cancel a workflow (if stuck)
temporal workflow cancel --namespace lt-005-audit --workflow-id DELIV-20250908-001
```

### 3. Worker Logs

The worker logs show activity execution:

```bash
# Tail worker logs
tail -f /tmp/temporal-worker.log

# Or from Docker
docker-compose -f temporal-docker-compose.yml logs -f temporal
```

### 4. Audit Trail Export

```typescript
export async function exportComplianceReport(
  deliveryId: string,
  format: 'json' | 'csv' | 'pdf' = 'json'
) {
  const auditTrail = await getDeliveryAuditTrail(deliveryId);
  
  switch (format) {
    case 'json':
      return JSON.stringify(auditTrail, null, 2);
    case 'csv':
      return auditTrailToCSV(auditTrail);
    case 'pdf':
      return auditTrailToPDF(auditTrail);
  }
}
```

## HIPAA Compliance Checklist

- [x] Immutable audit logs (Temporal event sourcing)
- [x] Timestamped events (every action has ISO 8601 timestamp)
- [x] Actor identification (who performed action)
- [x] Data classification (PHI vs operational)
- [x] 7-year retention (via PostgreSQL archival)
- [x] Access control (database user/password)
- [ ] Encryption at rest (PostgreSQL + pgcrypto, needs setup)
- [ ] Encryption in transit (gRPC TLS, can be enabled)
- [ ] Role-based access (Growth OS layer)
- [ ] Breach notification (legal/operational process)

## Troubleshooting

### Issue: Worker can't connect to Temporal

```bash
# Check server is running
docker-compose -f temporal-docker-compose.yml ps

# Check logs
docker-compose -f temporal-docker-compose.yml logs temporal

# Verify port is open
nc -zv localhost 7233
```

### Issue: Workflow stuck in running state

```bash
# Query actual status
curl -X POST http://localhost:7233 ... # (use temporal CLI instead)

temporal workflow describe --namespace lt-005-audit --workflow-id DELIV-001

# Check worker is processing tasks
ps aux | grep worker
# Should show: ts-node worker.ts (running)

# Check task queue depth
temporal task-queue describe --namespace lt-005-audit --task-queue HIPAA_AUDIT_TASK_QUEUE
```

### Issue: Activity timeout (delivery signal never arrives)

Increase timeout in worker.ts:
```typescript
const activities = proxyActivities({
  startToCloseTimeout: '30 minutes', // Increase from 10 minutes
  ...
});
```

Then restart worker:
```bash
npm run worker
```

## Files Reference

```
_INFRASTRUCTURE/
├── temporal-docker-compose.yml
├── TEMPORAL-SETUP.md (complete setup guide)
└── temporal/
    ├── config/
    │   └── config.yml
    ├── dynamicconfig/
    │   └── docker.yaml
    └── workflows/
        ├── lt005-hipaa-audit-workflow.ts (main workflow)
        ├── activities.ts (work units)
        ├── worker.ts (task executor)
        ├── client.ts (client CLI)
        └── package.json

BUSINESS-CAPITAL-DATA-ROOM/LT-005/22_SYSTEM/
└── TEMPORAL-INTEGRATION.md (this file)
```

## Next Steps

1. **Deploy Temporal** (section "Setup Instructions")
2. **Run local test** (verify workflow + signals work)
3. **Integrate with Growth OS** (use code samples in "Integration with Growth OS")
4. **Deploy on Mac Studio** (update docker-compose for Tailscale IP)
5. **Enable TLS** (for production)
6. **Add encryption at rest** (PostgreSQL pgcrypto)
7. **Set up compliance reporting** (automated PDF export)

## References

- [[TEMPORAL-SETUP.md|Complete Temporal Setup Guide]]
- [Temporal Documentation](https://docs.temporal.io/)
- [TypeScript SDK Guide](https://docs.temporal.io/dev-guide/typescript)
- [HIPAA Compliance](https://docs.temporal.io/security/hipaa-compliance)
- [Workflow Patterns](https://docs.temporal.io/workflow-guide/workflow-patterns)
