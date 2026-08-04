export const serviceName = 'construction-service';
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

export function getConstructionProjects() {
  return [
    { id: 'proj-101', name: 'Oakridge Manor Renovation', budget: 250000, progressPercent: 65, status: 'active' }
  ];
}

export function updateProjectMilestone(projectId: string, milestone: string, progress: number) {
  return {
    projectId,
    milestone,
    progress,
    updatedAt: new Date().toISOString()
  };
}
