import express from 'express';
import http from 'http';
import agentsRouter from '../../apps/api/src/routes/agents';
import servicesRouter from '../../apps/api/src/routes/services';

async function runVerification() {
  console.log('=== STARTING EMPIRICAL API VERIFICATION ===\n');

  const app = express();
  app.use(express.json());
  app.use('/api/agents', agentsRouter);
  app.use('/api', servicesRouter);

  const server = http.createServer(app);
  const PORT = 3899;

  await new Promise<void>((resolve) => server.listen(PORT, resolve));
  const baseUrl = `http://localhost:${PORT}`;

  const results: { test: string; status: 'PASS' | 'FAIL'; details?: any }[] = [];

  try {
    // 1. GET /api/agents
    console.log('[Test 1] GET /api/agents');
    const resAgents = await fetch(`${baseUrl}/api/agents`);
    const agentsData = await resAgents.json();

    if (resAgents.status === 200 && agentsData.success === true && agentsData.count === 20 && Array.isArray(agentsData.agents) && agentsData.agents.length === 20) {
      console.log(`  ✓ GET /api/agents returned 20 agents successfully.`);
      results.push({ test: 'GET /api/agents returns 20 agents', status: 'PASS', details: { count: agentsData.count } });
    } else {
      console.error(`  ✗ GET /api/agents failed! Status: ${resAgents.status}, Data:`, agentsData);
      results.push({ test: 'GET /api/agents returns 20 agents', status: 'FAIL', details: { status: resAgents.status, data: agentsData } });
    }

    // 2. POST /api/agents/:agentName/invoke for key agents
    const keyAgents = ['AcquisitionAgent', 'UnderwritingAgent', 'ValuationAgent', 'MortgageUnderwriterAgent'];

    for (const agentName of keyAgents) {
      console.log(`[Test 2] POST /api/agents/${agentName}/invoke`);
      const resInvoke = await fetch(`${baseUrl}/api/agents/${agentName}/invoke`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ testPayload: true }),
      });
      const invokeData = await resInvoke.json();

      if (resInvoke.status === 200 && invokeData.success === true && invokeData.agentName === agentName && Array.isArray(invokeData.logs) && invokeData.logs.length > 0 && invokeData.output) {
        console.log(`  ✓ POST /api/agents/${agentName}/invoke returned 200 OK with mock logs & output.`);
        results.push({
          test: `POST /api/agents/${agentName}/invoke`,
          status: 'PASS',
          details: { executionTimeMs: invokeData.executionTimeMs, logCount: invokeData.logs.length, outputKeys: Object.keys(invokeData.output) },
        });
      } else {
        console.error(`  ✗ POST /api/agents/${agentName}/invoke failed! Status: ${resInvoke.status}, Data:`, invokeData);
        results.push({ test: `POST /api/agents/${agentName}/invoke`, status: 'FAIL', details: { status: resInvoke.status, data: invokeData } });
      }
    }

    // 3. Test all remaining 16 agents to verify complete coverage
    const allAgentsRes = await fetch(`${baseUrl}/api/agents`);
    const allAgentsData = await allAgentsRes.json();
    const allAgentNames: string[] = allAgentsData.agents.map((a: any) => a.name);

    let allAgentsPassed = true;
    for (const name of allAgentNames) {
      const r = await fetch(`${baseUrl}/api/agents/${name}/invoke`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ ping: 'pong' }),
      });
      const data = await r.json();
      if (r.status !== 200 || !data.success) {
        allAgentsPassed = false;
        console.error(`  ✗ Invocation failed for ${name}`);
      }
    }
    if (allAgentsPassed) {
      console.log(`  ✓ All 20 AI agents invoked successfully without errors.`);
      results.push({ test: 'All 20 agents invocation coverage', status: 'PASS' });
    } else {
      results.push({ test: 'All 20 agents invocation coverage', status: 'FAIL' });
    }

    // 4. Test error handling for non-existent agent
    console.log('[Test 4] POST /api/agents/NonExistentAgent/invoke (Error Handling)');
    const resErr = await fetch(`${baseUrl}/api/agents/NonExistentAgent/invoke`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({}),
    });
    const errData = await resErr.json();
    if (resErr.status === 404 && errData.success === false) {
      console.log(`  ✓ Error handling verified: 404 returned for unknown agent.`);
      results.push({ test: 'Unknown agent 404 error handling', status: 'PASS' });
    } else {
      console.error(`  ✗ Unknown agent error handling failed:`, resErr.status, errData);
      results.push({ test: 'Unknown agent 404 error handling', status: 'FAIL', details: { status: resErr.status, data: errData } });
    }

    // 5. Mock Core Service Endpoints
    const coreServices = [
      '/api/identity',
      '/api/properties',
      '/api/crm',
      '/api/loans',
      '/api/underwriting',
      '/api/valuation',
      '/api/mortgage',
      '/api/organization',
      '/api/listings',
      '/api/closing',
      '/api/lease',
      '/api/tenant',
      '/api/rent-collection',
      '/api/maintenance',
      '/api/asset-management',
      '/api/syndication',
      '/api/document',
      '/api/notification',
      '/api/analytics',
      '/api/market-intelligence',
      '/api/inspection',
      '/api/disposition',
      '/api/tax',
      '/api/insurance',
      '/api/utility-management',
      '/api/vendor',
      '/api/marketing-automation',
      '/api/e-signature',
      '/api/audit-logging',
      '/api/spatial',
      '/api/construction',
      '/api/portfolio-optimization',
      '/api/investor-relations',
      '/api/accounting',
      '/api/ai-gateway',
      '/api/services',
    ];

    console.log(`\n[Test 5] Testing ${coreServices.length} mock core service endpoints...`);
    let servicesPassed = 0;

    for (const servicePath of coreServices) {
      const res = await fetch(`${baseUrl}${servicePath}`);
      const data = await res.json();
      if (res.status === 200 && data && (data.service || data.success || data.totalServicesCount)) {
        servicesPassed++;
      } else {
        console.error(`  ✗ Service endpoint ${servicePath} failed: status ${res.status}, data:`, data);
      }
    }

    if (servicesPassed === coreServices.length) {
      console.log(`  ✓ All ${servicesPassed}/${coreServices.length} mock core service endpoints returned valid JSON.`);
      results.push({ test: `Mock core services endpoints (${coreServices.length} endpoints)`, status: 'PASS', details: { passedCount: servicesPassed } });
    } else {
      console.error(`  ✗ Only ${servicesPassed}/${coreServices.length} service endpoints passed.`);
      results.push({ test: `Mock core services endpoints (${coreServices.length} endpoints)`, status: 'FAIL', details: { passedCount: servicesPassed, total: coreServices.length } });
    }

    console.log('\n=== EMPIRICAL VERIFICATION SUMMARY ===');
    console.table(results);

  } finally {
    server.close();
  }
}

runVerification().catch((err) => {
  console.error('Fatal error during verification script execution:', err);
  process.exit(1);
});
