export const serviceName = 'maintenance-service';
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

export function getMaintenanceTickets(propertyId?: string) {
  return [
    { id: 'maint-101', propertyId: propertyId || 'prop-1', issue: 'Leaky Faucet', priority: 'medium', status: 'open' }
  ];
}

export function assignWorkOrder(ticketId: string, vendorId: string) {
  return {
    workOrderId: `wo-${Date.now()}`,
    ticketId,
    vendorId,
    status: 'assigned',
    assignedAt: new Date().toISOString()
  };
}
