/**
 * Temporal Worker for LT-005 HIPAA Audit Workflows
 * 
 * This worker connects to the Temporal server and:
 * 1. Polls for workflow tasks
 * 2. Executes workflow logic
 * 3. Polls for activity tasks
 * 4. Executes activities (the actual work)
 * 
 * Start with: npx ts-node worker.ts
 * (or node dist/worker.js after tsc compilation)
 */

import { Worker, NativeConnection } from '@temporalio/worker';
import * as workflows from './lt005-hipaa-audit-workflow';
import * as activities from './activities';

const NAMESPACE = 'lt-005-audit';
const TASK_QUEUE = 'HIPAA_AUDIT_TASK_QUEUE';
const TEMPORAL_SERVER = 'localhost:7233'; // or 100.87.214.70:7233 for Mac Studio

async function run() {
  console.log(`🚀 Starting Temporal Worker for LT-005`);
  console.log(`   Server: ${TEMPORAL_SERVER}`);
  console.log(`   Namespace: ${NAMESPACE}`);
  console.log(`   Task Queue: ${TASK_QUEUE}`);

  // Connect to Temporal server
  const connection = await NativeConnection.connect({
    address: TEMPORAL_SERVER,
  });

  // Create worker
  const worker = await Worker.create({
    connection,
    namespace: NAMESPACE,
    taskQueue: TASK_QUEUE,
    workflowsPath: require.resolve('./lt005-hipaa-audit-workflow'),
    activitiesPath: require.resolve('./activities'),
    // Register workflows and activities
    workflows,
    activities,
    // Workflow execution timeout
    workflowFailureExceptionTypes: [],
    // Activity configuration
    maxActivitiesPerSecond: 100,
    maxConcurrentActivityExecutionSize: 10,
    maxConcurrentWorkflowTaskExecutionSize: 10,
  });

  console.log(`✅ Worker initialized`);
  console.log(`   Workflows: DeliveryAuditWorkflow`);
  console.log(`   Activities: logAuditEvent, validateDeliveryRequest, notifyCourierOfDelivery, ...`);
  console.log(`   Listening for tasks...`);

  // Run the worker
  await worker.run();
}

run().catch((err) => {
  console.error('❌ Worker error:', err);
  process.exit(1);
});
