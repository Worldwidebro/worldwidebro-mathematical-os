import { describe, it, expect } from 'vitest';
import { getAllAgents, getAgentByName, invokeAgent } from '../../registry/agents.js';

describe('AI Agent Registry Unit & Integration Tests', () => {
  it('should register all 20 AI agents from PRD Section 6', () => {
    const agents = getAllAgents();
    expect(agents).toHaveLength(20);

    const requiredAgentNames = [
      'AcquisitionAgent',
      'UnderwritingAgent',
      'ValuationAgent',
      'LeadNurtureAgent',
      'ListingOptimizerAgent',
      'TenantScreeningAgent',
      'LeaseGeneratorAgent',
      'RentCollectionAgent',
      'MaintenanceAgent',
      'VendorDispatchAgent',
      'MortgageUnderwriterAgent',
      'TitleEscrowAgent',
      'AssetManagerAgent',
      'InvestorRelationsAgent',
      'InspectionAnalyzerAgent',
      'MarketIntelligenceAgent',
      'PropertyTaxAgent',
      'InsuranceUnderwriterAgent',
      'UtilityAuditAgent',
      'DispositionAgent',
    ];

    requiredAgentNames.forEach((name) => {
      const agent = getAgentByName(name);
      expect(agent).toBeDefined();
      expect(agent?.name).toBe(name);
      expect(agent?.displayName).toBeTruthy();
      expect(agent?.description).toBeTruthy();
      expect(agent?.category).toBeTruthy();
      expect(agent?.capabilities?.length).toBeGreaterThan(0);
      expect(agent?.status).toBe('active');
      expect(agent?.version).toBeTruthy();
      expect(agent?.author).toBeTruthy();
    });
  });

  it('should correctly handle invocation for AcquisitionAgent', async () => {
    const res = await invokeAgent('AcquisitionAgent', { targetMarket: 'Charlotte, NC', minCapRate: 8.0 });
    expect(res.success).toBe(true);
    expect(res.agentName).toBe('AcquisitionAgent');
    expect(res.logs.length).toBeGreaterThan(0);
    expect(res.output.targetMarket).toBe('Charlotte, NC');
    expect(res.output.leadsFoundCount).toBeGreaterThan(0);
    expect(res.output.topDeals).toBeDefined();
  });

  it('should correctly handle invocation for UnderwritingAgent', async () => {
    const res = await invokeAgent('UnderwritingAgent', { purchasePrice: 3000000, grossRent: 350000, operatingExpenses: 110000, debtService: 140000 });
    expect(res.success).toBe(true);
    expect(res.agentName).toBe('UnderwritingAgent');
    expect(res.output.netOperatingIncome).toBe(240000);
    expect(res.output.capRatePct).toBe(8);
    expect(res.output.dscr).toBeGreaterThan(1.2);
  });

  it('should invoke all 20 agents without runtime errors', async () => {
    const agents = getAllAgents();
    for (const agent of agents) {
      const res = await invokeAgent(agent.name, { testMode: true });
      expect(res.success).toBe(true);
      expect(res.agentName).toBe(agent.name);
      expect(res.executionTimeMs).toBeGreaterThanOrEqual(0);
      expect(Array.isArray(res.logs)).toBe(true);
      expect(res.output).toBeDefined();
    }
  });

  it('should return error log for unknown agent invocation', async () => {
    const res = await invokeAgent('NonExistentAgent', {});
    expect(res.success).toBe(false);
    expect(res.logs[0].level).toBe('error');
    expect(res.output.error).toContain('Unknown agent');
  });
});
