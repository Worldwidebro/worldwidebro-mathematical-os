/**
 * Temporal Client for LT-005 HIPAA Audit Workflows
 * 
 * This client:
 * 1. Connects to Temporal server
 * 2. Starts new delivery workflows
 * 3. Sends signals (pickup completed, delivery attempted)
 * 4. Queries workflow status
 * 5. Retrieves audit trails
 * 
 * Usage:
 * - Start workflow: npx ts-node client.ts start <deliveryId>
 * - Send signal: npx ts-node client.ts signal <workflowId> <signalName>
 * - Query status: npx ts-node client.ts status <workflowId>
 */

import {
  Client,
  Connection,
  WorkflowFailedError,
} from '@temporalio/client';
import {
  DeliveryRequest,
  getDeliveryStatusQuery,
  getAuditTrailQuery,
  pickupCompletedSignal,
  deliveryAttemptedSignal,
} from './lt005-hipaa-audit-workflow';

const NAMESPACE = 'lt-005-audit';
const TASK_QUEUE = 'HIPAA_AUDIT_TASK_QUEUE';
const TEMPORAL_SERVER = 'localhost:7233';

async function main() {
  const connection = await Connection.connect({
    address: TEMPORAL_SERVER,
  });

  const client = new Client({
    connection,
    namespace: NAMESPACE,
  });

  const command = process.argv[2];
  const arg1 = process.argv[3];
  const arg2 = process.argv[4];

  try {
    switch (command) {
      case 'start': {
        // Start a new delivery workflow
        const deliveryId = arg1 || `DELIV-${Date.now()}`;
        const request: DeliveryRequest = {
          deliveryId,
          patientId: `PAT-${Math.random().toString(36).substr(2, 9)}`,
          pickupLocation: '123 Medical Supply Warehouse, Suite 100, Boston MA 02101',
          deliveryLocation: '456 Patient Home, Apt 5B, Boston MA 02102',
          medicalItems: ['Insulin Pens x10', 'Glucose Strips x50'],
          requiresSignature: true,
          scheduledPickupTime: new Date(Date.now() + 30 * 60 * 1000).toISOString(),
        };

        console.log(`📦 Starting delivery workflow: ${deliveryId}`);
        const handle = await client.workflow.start('DeliveryAuditWorkflow', {
          args: [request],
          taskQueue: TASK_QUEUE,
          workflowId: deliveryId,
          workflowRunTimeout: '24 hours',
        });

        console.log(`✅ Workflow started`);
        console.log(`   Workflow ID: ${handle.workflowId}`);
        console.log(`   Run ID: ${handle.firstExecutionRunId}`);
        break;
      }

      case 'pickup': {
        // Send pickup completed signal
        const workflowId = arg1;
        if (!workflowId) {
          console.error('❌ Usage: client.ts pickup <workflowId>');
          process.exit(1);
        }

        const handle = client.workflow.getHandle(workflowId);
        const pickedUpBy = `COURIER-${Math.random().toString(36).substr(2, 5).toUpperCase()}`;

        console.log(`📍 Sending pickup signal to ${workflowId}`);
        await handle.signal(pickupCompletedSignal, {
          pickedUpBy,
          timestamp: new Date().toISOString(),
          items: ['Insulin Pens x10', 'Glucose Strips x50'],
        });

        console.log(`✅ Pickup signal sent (courier: ${pickedUpBy})`);
        break;
      }

      case 'deliver': {
        // Send delivery attempted signal
        const workflowId = arg1;
        const status = arg2 === 'success' ? 'success' : 'failed';

        if (!workflowId) {
          console.error('❌ Usage: client.ts deliver <workflowId> [success|failed]');
          process.exit(1);
        }

        const handle = client.workflow.getHandle(workflowId);

        console.log(`🚚 Sending delivery signal to ${workflowId} (${status})`);
        await handle.signal(deliveryAttemptedSignal, {
          attemptedAt: new Date().toISOString(),
          status,
          reason: status === 'failed' ? 'Recipient not available' : undefined,
        });

        console.log(`✅ Delivery signal sent (status: ${status})`);
        break;
      }

      case 'status': {
        // Query workflow status
        const workflowId = arg1;
        if (!workflowId) {
          console.error('❌ Usage: client.ts status <workflowId>');
          process.exit(1);
        }

        const handle = client.workflow.getHandle(workflowId);

        const description = await handle.describe();
        console.log(`📊 Workflow Status: ${description.status.name}`);
        console.log(`   Workflow ID: ${description.workflowId}`);
        console.log(`   Start Time: ${description.startTime}`);
        console.log(`   Close Time: ${description.closeTime}`);

        try {
          const status = await handle.query(getDeliveryStatusQuery);
          console.log(`   Delivery Status: ${status}`);
        } catch (err) {
          console.log(`   (Status not available)`);
        }
        break;
      }

      case 'audit': {
        // Retrieve audit trail
        const workflowId = arg1;
        if (!workflowId) {
          console.error('❌ Usage: client.ts audit <workflowId>');
          process.exit(1);
        }

        const handle = client.workflow.getHandle(workflowId);
        const auditTrail = await handle.query(getAuditTrailQuery);

        console.log(`📋 Audit Trail for ${workflowId}:`);
        console.log(`   Total Events: ${auditTrail.length}`);
        auditTrail.forEach((event: any, idx: number) => {
          console.log(`\n   Event ${idx + 1}:`);
          console.log(`      Timestamp: ${event.timestamp}`);
          console.log(`      Actor: ${event.actor}`);
          console.log(`      Action: ${event.action}`);
          console.log(`      Status: ${event.status}`);
          console.log(`      HIPAA Class: ${event.hipaaClassification}`);
        });
        break;
      }

      case 'wait': {
        // Wait for workflow completion
        const workflowId = arg1;
        if (!workflowId) {
          console.error('❌ Usage: client.ts wait <workflowId>');
          process.exit(1);
        }

        const handle = client.workflow.getHandle(workflowId);
        console.log(`⏳ Waiting for workflow ${workflowId} to complete...`);

        try {
          const result = await handle.result();
          console.log(`✅ Workflow completed successfully`);
          console.log(`   Delivery Status: ${result.status}`);
          console.log(`   Audit Events: ${result.auditTrail.length}`);
        } catch (err) {
          if (err instanceof WorkflowFailedError) {
            console.error(`❌ Workflow failed: ${err.message}`);
          } else {
            throw err;
          }
        }
        break;
      }

      default:
        console.log(`Temporal Client for LT-005 HIPAA Audit Workflows`);
        console.log(`\nUsage:`);
        console.log(`  start       - Start new delivery workflow`);
        console.log(`  pickup      - Send pickup completed signal`);
        console.log(`  deliver     - Send delivery attempt signal`);
        console.log(`  status      - Query workflow status`);
        console.log(`  audit       - Retrieve audit trail`);
        console.log(`  wait        - Wait for workflow completion`);
        console.log(`\nExamples:`);
        console.log(`  npx ts-node client.ts start DELIV-001`);
        console.log(`  npx ts-node client.ts pickup DELIV-001`);
        console.log(`  npx ts-node client.ts deliver DELIV-001 success`);
        console.log(`  npx ts-node client.ts status DELIV-001`);
        console.log(`  npx ts-node client.ts audit DELIV-001`);
    }
  } catch (err) {
    console.error('❌ Error:', err.message);
    process.exit(1);
  } finally {
    await connection.close();
  }
}

main();
