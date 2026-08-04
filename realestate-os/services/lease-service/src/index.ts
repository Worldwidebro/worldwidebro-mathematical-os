export const serviceName = 'lease-service';
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

export function getLeaseByUnit(unitId: string) {
  return {
    leaseId: `lease-${unitId}`,
    unitId,
    tenantId: 'tenant-42',
    monthlyRent: 2200,
    startDate: '2026-01-01',
    endDate: '2026-12-31',
    status: 'active'
  };
}

export function renewLease(leaseId: string, newEndDate: string, newRent: number) {
  return {
    leaseId,
    newEndDate,
    newRent,
    status: 'renewed',
    renewedAt: new Date().toISOString()
  };
}
