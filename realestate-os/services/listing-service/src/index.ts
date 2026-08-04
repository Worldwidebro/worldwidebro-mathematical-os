export const serviceName = 'listing-service';
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

export function getActiveListings() {
  return [
    { id: 'list-1', title: 'Luxury 2BR Apartment', price: 2500, city: 'Charlotte', status: 'active' }
  ];
}

export function publishListing(propertyId: string, price: number) {
  return {
    listingId: `list-${Date.now()}`,
    propertyId,
    price,
    status: 'active',
    publishedAt: new Date().toISOString()
  };
}
