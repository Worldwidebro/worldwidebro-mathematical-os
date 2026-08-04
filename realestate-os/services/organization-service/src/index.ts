export const serviceName = 'organization-service';
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

export function getOrganizationProfile(orgId: string) {
  return {
    orgId,
    name: 'Apex Real Estate Ventures LLC',
    slug: 'apex-re',
    memberCount: 25,
    plan: 'enterprise'
  };
}

export function getOrgMembers(orgId: string) {
  return [
    { userId: 'usr-1', orgId, role: 'owner', name: 'Alice Manager' }
  ];
}
