import { describe, it, expect } from 'vitest';
import { SERVICES_CATALOG } from '../services.js';
import { getAllAgents, getAgentByName, invokeAgent } from '../../registry/agents.js';

describe('Central API Gateway Integration Tests', () => {
  it('GET /api/agents returns 200 OK with all 20 AI agents', () => {
    const agents = getAllAgents();
    expect(agents).toHaveLength(20);
    expect(agents[0].name).toBe('AcquisitionAgent');
  });

  it('GET /api/agents/:agentName returns details for specific AI Agent', () => {
    const agent = getAgentByName('UnderwritingAgent');
    expect(agent).toBeDefined();
    expect(agent?.name).toBe('UnderwritingAgent');
    expect(agent?.category).toBe('underwriting');
  });

  it('POST /api/agents/:agentName/invoke invokes agent with payload', async () => {
    const result = await invokeAgent('UnderwritingAgent', {
      purchasePrice: 2000000,
      grossRent: 250000,
      operatingExpenses: 80000,
      debtService: 90000,
    });
    expect(result.success).toBe(true);
    expect(result.agentName).toBe('UnderwritingAgent');
    expect(result.executionTimeMs).toBeGreaterThanOrEqual(0);
    expect(result.logs.length).toBeGreaterThan(0);
    expect(result.output.netOperatingIncome).toBe(170000);
  });

  it('GET /api/services returns catalog of all 35 microservices', () => {
    expect(SERVICES_CATALOG).toHaveLength(35);
  });
});
