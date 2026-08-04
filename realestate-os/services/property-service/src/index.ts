export const serviceName = 'property-service';
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

export function getProperties() {
  return [
    { id: 'prop-1', name: 'Sunset Apartments', address: '123 Main St', totalUnits: 24 }
  ];
}

export function getPropertyDetails(propertyId: string) {
  return {
    propertyId,
    name: 'Sunset Apartments',
    address: '123 Main St, Charlotte, NC 28202',
    totalUnits: 24,
    yearBuilt: 2018
  };
}
