export const serviceName = 'syndication-service';
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

export function getSyndicationDeals() {
  return [
    { dealId: 'deal-501', name: 'Uptown Tower Acquisition', totalEquityNeeded: 10000000, equityRaised: 7500000 }
  ];
}

export function registerInvestment(dealId: string, investorId: string, amount: number) {
  return {
    subscriptionId: `sub-${Date.now()}`,
    dealId,
    investorId,
    amount,
    status: 'confirmed',
    subscribedAt: new Date().toISOString()
  };
}
