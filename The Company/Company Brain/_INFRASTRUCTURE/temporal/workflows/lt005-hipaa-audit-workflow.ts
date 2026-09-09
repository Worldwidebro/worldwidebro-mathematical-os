/**
 * HIPAA Audit Workflow for LT-005 (HealthRoute Medical Courier)
 * Tracks delivery workflows with audit event logging for compliance
 * 
 * Workflow: Medical delivery pickup → transport → delivery
 * Audit trail: Every step logged with timestamps, actor, and status changes
 * 
 * Usage: node worker.ts (starts activity workers)
 *        tctl workflow start --tl HIPAA_AUDIT_TASK_QUEUE --wt DeliveryAuditWorkflow \
 *          --input '{...}'
 */

import {
  proxyActivities,
  defineSignal,
  defineQuery,
  defineUpdate,
  startChild,
  waitForSignal,
  sleep,
  Workflow,
  WorkflowExecutionAlreadyStartedError,
  ContinueAsNewOptions,
  ParentClosePolicy,
} from '@temporalio/workflow';

// Activity definitions
const activities = proxyActivities<typeof import('./activities')>({
  startToCloseTimeout: '10 minutes',
  heartbeatTimeout: '5 minutes',
  retryPolicy: {
    initialInterval: '1s',
    backoffCoefficient: 2.0,
    maximumInterval: '1m',
    maximumAttempts: 3,
    nonRetryableErrors: ['InvalidArgument', 'PermissionDenied'],
  },
});

// Workflow input types
export interface DeliveryRequest {
  deliveryId: string;
  patientId: string;
  pickupLocation: string;
  deliveryLocation: string;
  medicalItems: string[];
  requiresSignature: boolean;
  scheduledPickupTime: string;
}

export interface AuditEvent {
  timestamp: string;
  actor: string;
  action: string;
  status: 'SUCCESS' | 'FAILED' | 'PENDING';
  details: Record<string, any>;
  hipaaClassification: 'PHI' | 'OPERATIONAL' | 'METADATA';
}

// Signals for real-time workflow control
export const pickupCompletedSignal = defineSignal<
  [{ pickedUpBy: string; timestamp: string; items: string[] }]
>('pickupCompleted');

export const deliveryAttemptedSignal = defineSignal<
  [{ attemptedAt: string; status: 'success' | 'failed'; reason?: string }]
>('deliveryAttempted');

export const auditRequestSignal = defineSignal<[{ requestId: string }]>(
  'auditRequest'
);

// Queries for external monitoring
export const getDeliveryStatusQuery = defineQuery<string>('getDeliveryStatus');
export const getAuditTrailQuery = defineQuery<AuditEvent[]>('getAuditTrail');
export const getComplianceStatusQuery = defineQuery<{
  hipaaCompliant: boolean;
  missingAudits: string[];
}>('getComplianceStatus');

// Main workflow
export async function DeliveryAuditWorkflow(
  request: DeliveryRequest
): Promise<{ deliveryId: string; status: string; auditTrail: AuditEvent[] }> {
  const auditTrail: AuditEvent[] = [];
  let deliveryStatus = 'INITIATED';
  let pickupDetails: any = null;
  let deliveryAttemptCount = 0;
  const maxDeliveryAttempts = 3;

  // Add initial audit entry
  await activities.logAuditEvent({
    timestamp: new Date().toISOString(),
    deliveryId: request.deliveryId,
    actor: 'SYSTEM',
    action: 'DELIVERY_INITIATED',
    status: 'SUCCESS',
    details: request,
    hipaaClassification: 'PHI',
  });

  // Wait for pickup completion
  const pickupTimeout = new Date(request.scheduledPickupTime).getTime() + 30 * 60 * 1000; // 30 min window
  const now = new Date().getTime();
  const pickupWaitMs = Math.max(0, pickupTimeout - now);

  try {
    const pickupSignal = await waitForSignal(pickupCompletedSignal, {
      timeout: pickupWaitMs,
    });
    pickupDetails = pickupSignal;
    deliveryStatus = 'PICKED_UP';

    await activities.logAuditEvent({
      timestamp: pickupDetails.timestamp,
      deliveryId: request.deliveryId,
      actor: pickupDetails.pickedUpBy,
      action: 'PICKUP_COMPLETED',
      status: 'SUCCESS',
      details: {
        pickedUpBy: pickupDetails.pickedUpBy,
        items: pickupDetails.items,
        location: request.pickupLocation,
      },
      hipaaClassification: 'OPERATIONAL',
    });
  } catch (err) {
    if (err.name === 'TimeoutError') {
      deliveryStatus = 'PICKUP_TIMEOUT';
      await activities.logAuditEvent({
        timestamp: new Date().toISOString(),
        deliveryId: request.deliveryId,
        actor: 'SYSTEM',
        action: 'PICKUP_TIMEOUT',
        status: 'FAILED',
        details: {
          reason: 'No pickup signal received within timeout window',
          timeoutMs: pickupWaitMs,
        },
        hipaaClassification: 'OPERATIONAL',
      });
      throw new Error(`Pickup timeout for delivery ${request.deliveryId}`);
    }
    throw err;
  }

  // Delivery attempts (with retries)
  while (deliveryAttemptCount < maxDeliveryAttempts) {
    deliveryAttemptCount++;

    try {
      const deliverySignal = await waitForSignal(deliveryAttemptedSignal, {
        timeout: '4 hours', // 4-hour delivery window
      });

      if (deliverySignal.status === 'success') {
        deliveryStatus = 'DELIVERED';
        await activities.logAuditEvent({
          timestamp: deliverySignal.attemptedAt,
          deliveryId: request.deliveryId,
          actor: 'COURIER', // Actor determined from context
          action: 'DELIVERY_COMPLETED',
          status: 'SUCCESS',
          details: {
            attempt: deliveryAttemptCount,
            location: request.deliveryLocation,
            signature: request.requiresSignature,
          },
          hipaaClassification: 'OPERATIONAL',
        });
        break;
      } else {
        await activities.logAuditEvent({
          timestamp: deliverySignal.attemptedAt,
          deliveryId: request.deliveryId,
          actor: 'COURIER',
          action: `DELIVERY_ATTEMPT_FAILED_${deliveryAttemptCount}`,
          status: 'FAILED',
          details: {
            attempt: deliveryAttemptCount,
            reason: deliverySignal.reason || 'Unknown',
            retriesRemaining: maxDeliveryAttempts - deliveryAttemptCount,
          },
          hipaaClassification: 'OPERATIONAL',
        });

        if (deliveryAttemptCount < maxDeliveryAttempts) {
          await sleep(5 * 60 * 1000); // Wait 5 minutes before retry
        }
      }
    } catch (err) {
      if (err.name === 'TimeoutError') {
        deliveryStatus = 'DELIVERY_TIMEOUT';
        await activities.logAuditEvent({
          timestamp: new Date().toISOString(),
          deliveryId: request.deliveryId,
          actor: 'SYSTEM',
          action: 'DELIVERY_TIMEOUT',
          status: 'FAILED',
          details: {
            attempt: deliveryAttemptCount,
            reason: 'No delivery confirmation received within 4-hour window',
            maxAttempts: maxDeliveryAttempts,
          },
          hipaaClassification: 'OPERATIONAL',
        });
        throw new Error(`Delivery timeout after ${deliveryAttemptCount} attempts`);
      }
      throw err;
    }
  }

  // Query handlers for external monitoring
  setHandler(getDeliveryStatusQuery, () => deliveryStatus);
  setHandler(getAuditTrailQuery, () => auditTrail);
  setHandler(getComplianceStatusQuery, () => ({
    hipaaCompliant: auditTrail.length > 0 && deliveryStatus !== 'PICKUP_TIMEOUT',
    missingAudits: auditTrail.filter((e) => !e.timestamp).map((e) => e.action),
  }));

  // Signal handlers for external requests
  let auditRequestId = '';
  setHandler(auditRequestSignal, (signal) => {
    auditRequestId = signal.requestId;
  });

  // Final audit completion
  await activities.logAuditEvent({
    timestamp: new Date().toISOString(),
    deliveryId: request.deliveryId,
    actor: 'SYSTEM',
    action: 'DELIVERY_WORKFLOW_COMPLETED',
    status: 'SUCCESS',
    details: {
      finalStatus: deliveryStatus,
      pickupDetails,
      deliveryAttempts: deliveryAttemptCount,
      totalAuditEvents: auditTrail.length,
    },
    hipaaClassification: 'OPERATIONAL',
  });

  return {
    deliveryId: request.deliveryId,
    status: deliveryStatus,
    auditTrail,
  };
}

// Export for query/signal handlers in activities
export const setHandler = (query: any, handler: any) => {
  query.handler = handler;
};
