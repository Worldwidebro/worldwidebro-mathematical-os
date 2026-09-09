/**
 * Activities for LT-005 HIPAA Audit Workflow
 * Activities are the actual work units that get executed
 * They are retryable, auditable, and can be distributed across workers
 */

import { Connection } from '@temporalio/client';

export interface AuditEventInput {
  timestamp: string;
  deliveryId: string;
  actor: string;
  action: string;
  status: 'SUCCESS' | 'FAILED' | 'PENDING';
  details: Record<string, any>;
  hipaaClassification: 'PHI' | 'OPERATIONAL' | 'METADATA';
}

/**
 * Log an audit event to PostgreSQL
 * This is HIPAA-compliant audit trail storage
 * Every event is immutable and includes timestamp, actor, and action
 */
export async function logAuditEvent(event: AuditEventInput): Promise<void> {
  // In production, this would connect to the PostgreSQL database
  // For now, we log to console (would be replaced with DB insert)
  console.log(`[AUDIT] ${event.timestamp} | ${event.actor} | ${event.action}`, event.details);

  // Production implementation would be:
  // INSERT INTO audit_events (
  //   delivery_id, timestamp, actor, action, status, details, hipaa_classification, created_at
  // ) VALUES ($1, $2, $3, $4, $5, $6, $7, NOW())
}

/**
 * Validate delivery request before workflow starts
 */
export async function validateDeliveryRequest(input: {
  deliveryId: string;
  patientId: string;
  pickupLocation: string;
  deliveryLocation: string;
}): Promise<{ valid: boolean; errors: string[] }> {
  const errors: string[] = [];

  if (!input.deliveryId) errors.push('deliveryId is required');
  if (!input.patientId) errors.push('patientId is required');
  if (!input.pickupLocation) errors.push('pickupLocation is required');
  if (!input.deliveryLocation) errors.push('deliveryLocation is required');

  return {
    valid: errors.length === 0,
    errors,
  };
}

/**
 * Send notification to courier with delivery instructions
 */
export async function notifyCourierOfDelivery(input: {
  deliveryId: string;
  courierId: string;
  pickupLocation: string;
  deliveryLocation: string;
}): Promise<{ notificationSent: boolean; timestamp: string }> {
  console.log(`[COURIER NOTIFICATION] ${input.courierId} assigned to ${input.deliveryId}`);

  // Production: Call courier notification service (SMS, app push, email)
  // For now, just return success

  return {
    notificationSent: true,
    timestamp: new Date().toISOString(),
  };
}

/**
 * Verify HIPAA compliance of audit trail before completion
 * Checks that all required events are present
 */
export async function verifyHIPAACompliance(input: {
  deliveryId: string;
  auditTrail: any[];
}): Promise<{ compliant: boolean; violations: string[] }> {
  const violations: string[] = [];
  const requiredActions = [
    'DELIVERY_INITIATED',
    'PICKUP_COMPLETED',
    'DELIVERY_COMPLETED',
    'DELIVERY_WORKFLOW_COMPLETED',
  ];

  const auditActions = input.auditTrail.map((e) => e.action);

  for (const required of requiredActions) {
    if (!auditActions.includes(required)) {
      violations.push(`Missing required audit event: ${required}`);
    }
  }

  // Check all events have timestamps
  const noTimestamp = input.auditTrail.filter((e) => !e.timestamp);
  if (noTimestamp.length > 0) {
    violations.push(`${noTimestamp.length} audit events missing timestamps`);
  }

  // Check no sensitive data in audit trail (simplified check)
  const sensitivePatterns = [/password/i, /ssn/i, /creditcard/i];
  for (const event of input.auditTrail) {
    const details = JSON.stringify(event.details);
    for (const pattern of sensitivePatterns) {
      if (pattern.test(details)) {
        violations.push(`Potential sensitive data leak in audit event: ${event.action}`);
      }
    }
  }

  return {
    compliant: violations.length === 0,
    violations,
  };
}

/**
 * Archive audit trail to long-term storage
 * Required for HIPAA retention (typically 6+ years)
 */
export async function archiveAuditTrail(input: {
  deliveryId: string;
  auditTrail: any[];
}): Promise<{ archived: boolean; archiveId: string }> {
  const archiveId = `ARCHIVE-${input.deliveryId}-${Date.now()}`;
  console.log(`[ARCHIVE] Archiving audit trail to ${archiveId}`);

  // Production: Write to immutable S3 bucket with versioning + MFA delete
  // For now, just return success

  return {
    archived: true,
    archiveId,
  };
}

/**
 * Send compliance report to regulatory team
 */
export async function sendComplianceReport(input: {
  deliveryId: string;
  status: string;
  auditTrail: any[];
  hipaaCompliant: boolean;
}): Promise<{ reportId: string; sent: boolean }> {
  const reportId = `REPORT-${input.deliveryId}-${Date.now()}`;
  console.log(
    `[COMPLIANCE] Report ${reportId} for ${input.deliveryId}: ${input.status}, HIPAA compliant: ${input.hipaaCompliant}`
  );

  // Production: Email to compliance@healthroute.com + store in audit database
  // For now, just return success

  return {
    reportId,
    sent: true,
  };
}
