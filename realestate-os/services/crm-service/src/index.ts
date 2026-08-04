export const serviceName = 'crm-service';
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

export function getLeads(status?: string) {
  return [
    { id: 'lead-1', name: 'John Doe', email: 'john@example.com', status: status || 'new' }
  ];
}

export function createLead(lead: { name: string; email: string; phone?: string }) {
  return {
    id: `lead-${Date.now()}`,
    ...lead,
    createdAt: new Date().toISOString()
  };
}
