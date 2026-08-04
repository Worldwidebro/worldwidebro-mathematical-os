export const serviceName = 'utility-management-service';
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

export function getUtilityBills(propertyId: string) {
  return [
    { billId: 'util-1', propertyId, provider: 'Duke Energy', amount: 340.50, dueDate: '2026-08-15' }
  ];
}

export function recordSubmeterReading(unitId: string, utilityType: string, value: number) {
  return {
    readingId: `read-${Date.now()}`,
    unitId,
    utilityType,
    value,
    recordedAt: new Date().toISOString()
  };
}
