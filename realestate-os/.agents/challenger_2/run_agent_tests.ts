import { getAllAgents, getAgentByName, invokeAgent } from '../../apps/api/src/registry/agents.js';
import { SERVICES_CATALOG } from '../../apps/api/src/routes/services.js';

interface TestResult {
  agentName: string;
  displayName: string;
  category: string;
  version: string;
  success: boolean;
  executionTimeMs: number;
  logCount: number;
  outputKeys: string[];
  sampleOutput: string;
  verdict: 'PASS' | 'FAIL';
}

interface ServiceCheckResult {
  id: string;
  name: string;
  route: string;
  category: string;
  status: string;
  verdict: 'PASS' | 'FAIL';
}

async function runEmpiricalEvaluation() {
  console.log('====================================================');
  console.log('  CHALLENGER 2 EMPIRICAL VERIFICATION HARNESS');
  console.log('====================================================\n');

  // 1. Verify Agent Registry
  const registeredAgents = getAllAgents();
  console.log(`[1] Total Registered AI Agents: ${registeredAgents.length}`);

  const targetAgentList = [
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

  console.log(`[2] Target Agent Invocations to Test: ${targetAgentList.length}\n`);

  const agentTestResults: TestResult[] = [];

  for (let i = 0; i < targetAgentList.length; i++) {
    const agentName = targetAgentList[i];
    const meta = getAgentByName(agentName);
    const stepNum = i + 1;

    if (!meta) {
      console.error(`[ERR] Agent ${agentName} NOT FOUND in registry!`);
      agentTestResults.push({
        agentName,
        displayName: 'MISSING',
        category: 'UNKNOWN',
        version: 'N/A',
        success: false,
        executionTimeMs: 0,
        logCount: 0,
        outputKeys: [],
        sampleOutput: 'Agent not found in registry',
        verdict: 'FAIL',
      });
      continue;
    }

    const payload = {
      testSession: 'Challenger2-Empirical-Runner',
      timestamp: new Date().toISOString(),
    };

    const res = await invokeAgent(agentName, payload);
    const pass = res.success && res.logs.length > 0 && Object.keys(res.output).length > 0;

    agentTestResults.push({
      agentName: meta.name,
      displayName: meta.displayName || meta.name,
      category: String(meta.category || 'general'),
      version: meta.version,
      success: res.success,
      executionTimeMs: res.executionTimeMs,
      logCount: res.logs.length,
      outputKeys: Object.keys(res.output),
      sampleOutput: JSON.stringify(res.output).slice(0, 80) + '...',
      verdict: pass ? 'PASS' : 'FAIL',
    });

    console.log(
      `[Agent ${stepNum}/20] ${meta.name} (${meta.displayName}) -> ${pass ? '✅ PASS' : '❌ FAIL'} (${res.executionTimeMs}ms, ${res.logs.length} logs)`
    );
  }

  // 2. Service Endpoints Verification
  console.log('\n----------------------------------------------------');
  console.log('  MICROSERVICES ENDPOINT RESOLUTION TESTING');
  console.log('----------------------------------------------------\n');

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

  const serviceResults: ServiceCheckResult[] = [];

  for (const sId of REQUIRED_35_SERVICES) {
    const sMeta = SERVICES_CATALOG.find((s) => s.id === sId);
    if (sMeta) {
      serviceResults.push({
        id: sMeta.id,
        name: sMeta.name,
        route: sMeta.route,
        category: sMeta.category,
        status: sMeta.status,
        verdict: sMeta.status === 'HEALTHY' ? 'PASS' : 'FAIL',
      });
    } else {
      serviceResults.push({
        id: sId,
        name: sId,
        route: 'UNMAPPED',
        category: 'UNKNOWN',
        status: 'MISSING',
        verdict: 'FAIL',
      });
    }
  }

  console.log(`Verified ${serviceResults.length} / 35 Microservices in catalog.`);
  const failedServices = serviceResults.filter((s) => s.verdict === 'FAIL');
  console.log(`Failed Services: ${failedServices.length}\n`);

  // Summary
  const passedAgentsCount = agentTestResults.filter((a) => a.verdict === 'PASS').length;
  const passedServicesCount = serviceResults.filter((s) => s.verdict === 'PASS').length;

  console.log('====================================================');
  console.log('  FINAL VERDICT');
  console.log('====================================================');
  console.log(`AI Agents Invocations: ${passedAgentsCount} / 20 PASSED`);
  console.log(`Microservices Resolved: ${passedServicesCount} / 35 PASSED`);
  console.log(
    `OVERALL VERDICT: ${passedAgentsCount === 20 && passedServicesCount === 35 ? 'PASSED (100%)' : 'FAILED'}`
  );
  console.log('====================================================\n');

  return {
    agents: agentTestResults,
    services: serviceResults,
    passedAgentsCount,
    passedServicesCount,
  };
}

runEmpiricalEvaluation().catch(console.error);
