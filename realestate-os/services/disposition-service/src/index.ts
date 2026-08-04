export const serviceName = 'disposition-service';
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

export function getDispositionPipeline() {
  return [
    { propertyId: 'prop-88', listPrice: 1200000, offersReceived: 3, status: 'under_contract' }
  ];
}

export function evaluatePropertyOffer(propertyId: string, offerAmount: number) {
  return {
    propertyId,
    offerAmount,
    recommendation: offerAmount >= 1150000 ? 'accept' : 'counter',
    evaluatedAt: new Date().toISOString()
  };
}
