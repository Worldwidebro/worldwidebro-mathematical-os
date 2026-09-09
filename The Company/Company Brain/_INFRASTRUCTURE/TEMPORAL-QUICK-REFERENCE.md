# Temporal Quick Reference for LT-005

## File Locations

```
_INFRASTRUCTURE/
├── temporal-docker-compose.yml           Docker stack
├── TEMPORAL-SETUP.md                     Full setup guide
├── TEMPORAL-QUICK-REFERENCE.md           This file
├── temporal/
│   ├── bootstrap.sh                      One-command deploy
│   ├── config/
│   │   └── config.yml                    Server config
│   ├── dynamicconfig/
│   │   └── docker.yaml                   Runtime settings
│   └── workflows/
│       ├── package.json                  Dependencies
│       ├── worker.ts                     Task executor
│       ├── client.ts                     CLI client
│       ├── activities.ts                 Work units
│       └── lt005-hipaa-audit-workflow.ts Main workflow

BUSINESS-CAPITAL-DATA-ROOM/LT-005/22_SYSTEM/
└── TEMPORAL-INTEGRATION.md               Growth OS integration
```

## Endpoints

| Service | URL | Purpose |
|---------|-----|---------|
| **Temporal Web UI** | http://localhost:8080 | Dashboard (workflows, executions, monitoring) |
| **Temporal API** | localhost:7233 (gRPC) | Client connections |
| **Admin API** | localhost:6939 | Health checks, admin operations |
| **PostgreSQL** | localhost:5433 | Audit logs & persistence |

Credentials: `temporal` / `temporal_changeme`

## Quick Commands

### Start Services
```bash
cd _INFRASTRUCTURE
docker-compose -f temporal-docker-compose.yml up -d
```

### Verify Running
```bash
docker-compose -f temporal-docker-compose.yml ps
curl http://localhost:6939/health
```

### Install SDK
```bash
cd _INFRASTRUCTURE/temporal/workflows
npm install
```

### Start Worker
```bash
cd _INFRASTRUCTURE/temporal/workflows
npm run worker
```

### Workflow Lifecycle (CLI)
```bash
# Start delivery workflow
npm run client -- start DELIV-001

# Send pickup signal
npm run client -- pickup DELIV-001

# Send delivery attempt
npm run client -- deliver DELIV-001 success

# Query status
npm run client -- status DELIV-001

# Get audit trail
npm run client -- audit DELIV-001

# Wait for completion
npm run client -- wait DELIV-001
```

### Temporal CLI (if installed)
```bash
# List workflows
temporal workflow list --namespace lt-005-audit

# Describe workflow
temporal workflow describe --namespace lt-005-audit --workflow-id DELIV-001

# Show history
temporal workflow show --namespace lt-005-audit --workflow-id DELIV-001

# Cancel workflow
temporal workflow cancel --namespace lt-005-audit --workflow-id DELIV-001
```

## Growth OS Integration

### Install SDK
```bash
npm install @temporalio/client @temporalio/workflow @temporalio/worker
```

### Create Temporal Helper
```typescript
// src/lib/temporal.ts
import { Connection, Client } from '@temporalio/client';

const connection = await Connection.connect({
  address: 'localhost:7233',
});

export const client = new Client({
  connection,
  namespace: 'lt-005-audit',
});
```

### Start Workflow
```typescript
const handle = await client.workflow.start('DeliveryAuditWorkflow', {
  args: [deliveryRequest],
  taskQueue: 'HIPAA_AUDIT_TASK_QUEUE',
  workflowId: deliveryId,
});
```

### Send Signal
```typescript
await handle.signal('pickupCompleted', {
  pickedUpBy: courierId,
  timestamp: new Date().toISOString(),
  items: medicalItems,
});
```

### Query Audit Trail
```typescript
const auditTrail = await handle.query('getAuditTrail');
```

## Workflow Events

| Event | Triggered By | Actor | Details |
|-------|-------------|-------|---------|
| DELIVERY_INITIATED | System | SYSTEM | Workflow starts |
| PICKUP_COMPLETED | Signal | COURIER | pickupCompletedSignal sent |
| DELIVERY_ATTEMPT_FAILED_N | Signal | COURIER | deliveryAttemptedSignal with status=failed |
| DELIVERY_COMPLETED | Signal | COURIER | deliveryAttemptedSignal with status=success |
| DELIVERY_TIMEOUT | System | SYSTEM | Timeout exceeded, no signals received |
| DELIVERY_WORKFLOW_COMPLETED | System | SYSTEM | Workflow finishes, archive triggered |

## Timeouts

- **Pickup Window**: 30 minutes from scheduledPickupTime
- **Delivery Window**: 4 hours per attempt
- **Retry Interval**: 5 minutes between delivery attempts
- **Max Delivery Attempts**: 3
- **Workflow Timeout**: 24 hours

## Database

PostgreSQL runs on port **5433**

```bash
# Connect to database
psql -h localhost -p 5433 -U temporal -d temporal

# Query audit events
SELECT * FROM delivery_audit_events;
```

## Monitoring

### Health Check
```bash
curl -s http://localhost:6939/health | jq .
```

### Metrics (Prometheus format)
```bash
curl http://localhost:8000/metrics | grep temporal
```

### Logs
```bash
docker-compose -f temporal-docker-compose.yml logs temporal
docker-compose -f temporal-docker-compose.yml logs temporal-ui
docker-compose -f temporal-docker-compose.yml logs temporal-postgres
```

## Troubleshooting

### Server not responding
```bash
# Check if container is running
docker ps | grep temporal

# Check logs
docker logs temporal-server

# Restart
docker-compose -f temporal-docker-compose.yml restart
```

### Worker can't connect
```bash
# Verify server port is open
nc -zv localhost 7233

# Check worker logs for connection errors
npm run worker 2>&1 | grep -i error
```

### Workflow stuck
```bash
# Query actual status
temporal workflow describe --namespace lt-005-audit --workflow-id DELIV-001

# Cancel if needed
temporal workflow cancel --namespace lt-005-audit --workflow-id DELIV-001
```

## Port Map

| Port | Service | Purpose |
|------|---------|---------|
| 7233 | Temporal Frontend | gRPC client connections |
| 6933 | Temporal Internal | Cluster communication |
| 6934 | Temporal History | State management |
| 6935 | Temporal Matching | Task distribution |
| 6939 | Temporal Admin | Health checks, admin API |
| 6000 | Temporal Metrics | Prometheus metrics |
| 8080 | Web UI | Dashboard |
| 5433 | PostgreSQL | Persistence |

## Environment Variables

```bash
TEMPORAL_SERVER=localhost:7233
TEMPORAL_NAMESPACE=lt-005-audit
TASK_QUEUE=HIPAA_AUDIT_TASK_QUEUE
DATABASE_URL=postgresql://temporal:temporal_changeme@localhost:5433/temporal
```

## HIPAA Compliance Checklist

- [x] Immutable audit logs (Temporal event sourcing)
- [x] Timestamped events (ISO 8601, server time)
- [x] Actor identification (who, when, what)
- [x] Event classification (PHI, OPERATIONAL, METADATA)
- [x] Retention policy (7+ years configurable)
- [x] Access control (DB credentials)
- [ ] Encryption at rest (requires setup)
- [ ] Encryption in transit (requires TLS config)
- [ ] Role-based access (Growth OS layer)
- [ ] Breach procedures (legal/policy)

## Documentation

- **Full Setup**: `_INFRASTRUCTURE/TEMPORAL-SETUP.md` (16 KB)
- **Growth OS Integration**: `BUSINESS-CAPITAL-DATA-ROOM/LT-005/22_SYSTEM/TEMPORAL-INTEGRATION.md` (8 KB)
- **Temporal Docs**: https://docs.temporal.io/
- **TypeScript SDK**: https://docs.temporal.io/dev-guide/typescript

## Support

For issues or questions:
1. Check `TEMPORAL-SETUP.md` "Troubleshooting" section
2. Review `TEMPORAL-INTEGRATION.md` for Growth OS integration
3. Visit https://docs.temporal.io/ for reference
4. Check container logs: `docker logs temporal-server`

---

**Created**: 2026-09-08  
**Status**: Ready for local development  
**Next**: Run `bash _INFRASTRUCTURE/temporal/bootstrap.sh`
