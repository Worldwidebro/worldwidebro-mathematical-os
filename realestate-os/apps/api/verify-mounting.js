import app from './dist/index.js';

async function runVerification() {
  console.log('--- Starting API Gateway Router Mounting Verification ---');
  
  const server = app.listen(0, async () => {
    const port = server.address().port;
    const baseUrl = `http://localhost:${port}`;
    let passed = true;

    try {
      // Test 1: GET /api/agents returns 20 agents
      console.log('1. Testing GET /api/agents...');
      const res1 = await fetch(`${baseUrl}/api/agents`);
      const data1 = await res1.json();
      if (res1.status === 200 && data1.success === true && data1.count === 20 && data1.agents.length === 20) {
        console.log('   ✅ PASS: GET /api/agents returned 200 OK with 20 AI agents.');
      } else {
        console.error('   ❌ FAIL: GET /api/agents output unexpected:', data1);
        passed = false;
      }

      // Test 2: GET /api/agents/AcquisitionAgent
      console.log('2. Testing GET /api/agents/AcquisitionAgent...');
      const res2 = await fetch(`${baseUrl}/api/agents/AcquisitionAgent`);
      const data2 = await res2.json();
      if (res2.status === 200 && data2.success === true && data2.agent.name === 'AcquisitionAgent') {
        console.log('   ✅ PASS: GET /api/agents/AcquisitionAgent returned agent details.');
      } else {
        console.error('   ❌ FAIL: GET /api/agents/AcquisitionAgent failed:', data2);
        passed = false;
      }

      // Test 3: POST /api/agents/AcquisitionAgent/invoke returns 200 OK with logs
      console.log('3. Testing POST /api/agents/AcquisitionAgent/invoke...');
      const res3 = await fetch(`${baseUrl}/api/agents/AcquisitionAgent/invoke`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ targetMarket: 'Charlotte, NC', minCapRate: 7.5 }),
      });
      const data3 = await res3.json();
      if (res3.status === 200 && data3.success === true && data3.logs && data3.logs.length > 0 && data3.output) {
        console.log('   ✅ PASS: POST /api/agents/AcquisitionAgent/invoke returned 200 OK with logs and output.');
      } else {
        console.error('   ❌ FAIL: POST /api/agents/AcquisitionAgent/invoke failed:', data3);
        passed = false;
      }

      // Test 4: GET /api/services returns 35 microservices catalog
      console.log('4. Testing GET /api/services...');
      const res4 = await fetch(`${baseUrl}/api/services`);
      const data4 = await res4.json();
      if (res4.status === 200 && data4.success === true && data4.totalServicesCount === 35 && data4.services.length === 35) {
        console.log('   ✅ PASS: GET /api/services returned 200 OK with 35 microservices.');
      } else {
        console.error('   ❌ FAIL: GET /api/services failed:', data4);
        passed = false;
      }

      // Test 5: GET /api returns 35 microservices catalog
      console.log('5. Testing GET /api...');
      const res5 = await fetch(`${baseUrl}/api`);
      const data5 = await res5.json();
      if (res5.status === 200 && data5.success === true && data5.totalServicesCount === 35) {
        console.log('   ✅ PASS: GET /api returned 200 OK with 35 microservices.');
      } else {
        console.error('   ❌ FAIL: GET /api failed:', data5);
        passed = false;
      }

      if (passed) {
        console.log('\n🎉 ALL VERIFICATION TESTS PASSED!');
        server.close(() => process.exit(0));
      } else {
        console.error('\n❌ SOME VERIFICATION TESTS FAILED.');
        server.close(() => process.exit(1));
      }
    } catch (err) {
      console.error('Error during verification:', err);
      server.close(() => process.exit(1));
    }
  });
}

runVerification();
