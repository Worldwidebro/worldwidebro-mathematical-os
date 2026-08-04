export const serviceName = 'ai-gateway-service';
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

export function promptAgent(agentId: string, prompt: string) {
  return {
    requestId: `req-${Date.now()}`,
    agentId,
    prompt,
    response: `Mock response from agent ${agentId} for prompt: "${prompt}"`,
    tokensUsed: 150,
    timestamp: new Date().toISOString()
  };
}

export function getGatewayMetrics() {
  return {
    activeAgents: 12,
    requestsProcessed: 4500,
    averageLatencyMs: 120,
    status: 'operational'
  };
}
