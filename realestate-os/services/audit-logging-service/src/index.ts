export const serviceName = 'audit-logging-service';
export const version = '1.0.0';
export const status = 'active';

export interface HealthCheckResult {
  serviceName: string;
  version: string;
  status: 'healthy' | 'unhealthy';
  timestamp: string;
  uptime: number;
}

const startTime = Date.now();

export function getHealthStatus(): HealthCheckResult {
  return {
    serviceName,
    version,
    status: 'healthy',
    timestamp: new Date().toISOString(),
    uptime: Math.floor((Date.now() - startTime) / 1000)
  };
}

export function initializeService(): { serviceName: string; initialized: boolean; timestamp: string } {
  return {
    serviceName,
    initialized: true,
    timestamp: new Date().toISOString()
  };
}

export function logAuditEvent(actor: string, action: string, resource: string) {
  return {
    id: `log-${Date.now()}`,
    actor,
    action,
    resource,
    timestamp: new Date().toISOString()
  };
}

export function queryAuditLogs(limit: number = 50) {
  return Array.from({ length: Math.min(limit, 5) }, (_, i) => ({
    id: `log-${i + 1}`,
    actor: 'user@example.com',
    action: 'UPDATE_PROPERTY',
    resource: `property-${i + 1}`,
    timestamp: new Date().toISOString()
  }));
}
