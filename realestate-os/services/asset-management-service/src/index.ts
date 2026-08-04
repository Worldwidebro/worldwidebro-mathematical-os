export const serviceName = 'asset-management-service';
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

export function getAssetDetails(assetId: string) {
  return {
    assetId,
    name: 'Main Street Commercial Center',
    valuation: 4500000,
    occupancyRate: 0.95,
    lastValuationDate: '2026-01-15'
  };
}

export function getCapitalExpenditures(assetId: string) {
  return [
    { id: 'capex-1', assetId, description: 'Roof Replacement', budget: 75000, status: 'in_progress' }
  ];
}
