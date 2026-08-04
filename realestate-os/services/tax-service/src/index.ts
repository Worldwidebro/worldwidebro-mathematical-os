export const serviceName = 'tax-service';
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

export function getTaxAssessment(propertyId: string, taxYear: number) {
  return {
    propertyId,
    taxYear,
    assessedValue: 850000,
    propertyTaxDue: 11050,
    dueDate: `${taxYear}-12-31`
  };
}

export function calculateDepreciationSchedule(assetValue: number, usefulLifeYears: number = 27.5) {
  return {
    assetValue,
    usefulLifeYears,
    annualDepreciation: Math.round((assetValue / usefulLifeYears) * 100) / 100
  };
}
