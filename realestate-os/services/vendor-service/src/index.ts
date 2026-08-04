export const serviceName = 'vendor-service';
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

export function getVendorList(category?: string) {
  return [
    { vendorId: 'vend-1', companyName: 'QuickFix Plumbing', category: category || 'Plumbing', rating: 4.8 }
  ];
}

export function rateVendorPerformance(vendorId: string, rating: number) {
  return {
    vendorId,
    newRating: rating,
    updatedAt: new Date().toISOString()
  };
}
