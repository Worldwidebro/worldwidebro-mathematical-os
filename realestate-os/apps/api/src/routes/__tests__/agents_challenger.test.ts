import { describe, it, expect } from 'vitest';
import { getAllAgents, getAgentByName, invokeAgent } from '../../registry/agents.js';
import { SERVICES_CATALOG } from '../services.js';

const EXPECTED_20_AGENTS = [
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

describe('Challenger 2 Empirical Verification Suite', () => {
  describe('AI Agent Registry Verification', () => {
    it('should register exactly 20 AI agents in the registry', () => {
      const agents = getAllAgents();
      expect(agents.length).toBe(20);
    });

    it('should contain all 20 specified agent names', () => {
      const agents = getAllAgents();
      const names = agents.map((a) => a.name);
      for (const expectedAgent of EXPECTED_20_AGENTS) {
        expect(names).toContain(expectedAgent);
      }
    });

    for (const agentName of EXPECTED_20_AGENTS) {
      it(`should successfully invoke ${agentName} with valid logs and structured output`, async () => {
        const metadata = getAgentByName(agentName);
        expect(metadata).toBeDefined();
        expect(metadata?.status).toBe('active');

        const result = await invokeAgent(agentName, { testTriggeredBy: 'Challenger2' });

        // 1. Success check
        expect(result.success).toBe(true);
        expect(result.agentName).toBe(agentName);
        expect(typeof result.executionTimeMs).toBe('number');

        // 2. Execution Logs check
        expect(Array.isArray(result.logs)).toBe(true);
        expect(result.logs.length).toBeGreaterThanOrEqual(3);

        for (const log of result.logs) {
          expect(log).toHaveProperty('timestamp');
          expect(log).toHaveProperty('level');
          expect(log).toHaveProperty('message');
          expect(typeof log.timestamp).toBe('string');
          expect(typeof log.message).toBe('string');
        }

        // 3. Domain-appropriate output check
        expect(result.output).toBeDefined();
        expect(typeof result.output).toBe('object');
        expect(Object.keys(result.output).length).toBeGreaterThan(0);
      });
    }
  });

  describe('Microservices Catalog & Service Endpoints Resolution', () => {
    it('should contain at least 35 core service entries in SERVICES_CATALOG', () => {
      expect(SERVICES_CATALOG.length).toBeGreaterThanOrEqual(35);
    });

    const REQUIRED_35_SERVICES = [
      'identity-service',
      'organization-service',
      'property-service',
      'listing-service',
      'loans-service',
      'crm-service',
      'underwriting-service',
      'valuation-service',
      'mortgage-service',
      'closing-service',
      'lease-service',
      'tenant-service',
      'rent-collection-service',
      'maintenance-service',
      'asset-management-service',
      'syndication-service',
      'document-service',
      'notification-service',
      'analytics-service',
      'market-intelligence-service',
      'inspection-service',
      'disposition-service',
      'tax-service',
      'insurance-service',
      'utility-management-service',
      'vendor-service',
      'marketing-automation-service',
      'e-signature-service',
      'audit-logging-service',
      'spatial-service',
      'construction-service',
      'portfolio-optimization-service',
      'investor-relations-service',
      'accounting-service',
      'ai-gateway-service',
    ];

    for (const serviceId of REQUIRED_35_SERVICES) {
      it(`should resolve service metadata for ${serviceId}`, () => {
        const found = SERVICES_CATALOG.find((s) => s.id === serviceId);
        expect(found).toBeDefined();
        expect(found?.status).toBe('HEALTHY');
        expect(found?.route).toMatch(/^\/api\//);
      });
    }
  });
});
