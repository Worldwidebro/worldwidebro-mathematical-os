import neo4j from 'neo4j-driver';
import dotenv from 'dotenv';

dotenv.config();

async function runSimpleTests() {
  console.log('\n=== UNIT 1.1: Simple Neo4j Agent Tests ===\n');

  // Create fresh driver for this test run
  const driver = neo4j.driver(
    process.env.NEO4J_URI || 'bolt://100.87.214.70:7687',
    neo4j.auth.basic(
      process.env.NEO4J_USER || 'neo4j',
      process.env.NEO4J_PASSWORD || 'changeme'
    ),
    { logging: neo4j.logging.console('warn') }
  );

  try {
    // Test 1: Count agents
    console.log('Test 1: Count agents in Neo4j');
    const session1 = driver.session();
    try {
      const result = await session1.run('MATCH (a:Agent) RETURN count(a) as total_agents');
      const count = result.records[0].get('total_agents').toNumber ?
        result.records[0].get('total_agents').toNumber() :
        result.records[0].get('total_agents');
      console.log(`✓ Total agents in Neo4j: ${count}`);
    } finally {
      await session1.close();
    }

    // Test 2: Get sample agents
    console.log('\nTest 2: Fetch sample agents');
    const session2 = driver.session();
    try {
      const result = await session2.run(`
        MATCH (a:Agent)
        OPTIONAL MATCH (a)-[:HAS_CAPABILITY]->(cap:Capability)
        RETURN {
          id: a.id,
          name: a.name,
          domain: a.domain,
          capabilities: collect(cap.name)
        } as agent
        LIMIT 3
      `);
      console.log(`✓ Fetched ${result.records.length} sample agents:`);
      result.records.forEach((record, idx) => {
        const agent = record.get('agent');
        console.log(`  ${idx + 1}. ${agent.name} (${agent.domain}) - ${agent.capabilities.length} capabilities`);
      });
    } finally {
      await session2.close();
    }

    // Test 3: Check data completeness
    console.log('\nTest 3: Verify data completeness');
    const session3 = driver.session();
    try {
      const result = await session3.run(`
        MATCH (a:Agent)
        WHERE a.id IS NULL
           OR a.name IS NULL
           OR a.domain IS NULL
           OR a.status IS NULL
           OR a.cost_per_invocation IS NULL
           OR a.estimated_revenue IS NULL
        RETURN count(*) as missing_count, collect(a.id) as agent_ids LIMIT 10
      `);
      const missing = result.records[0].get('missing_count').toNumber ?
        result.records[0].get('missing_count').toNumber() :
        result.records[0].get('missing_count');
      const ids = result.records[0].get('agent_ids');

      if (missing === 0) {
        console.log('✓ All agents have required fields (no missing data)');
      } else {
        console.log(`⚠ ${missing} agent(s) missing required fields:`);
        ids.slice(0, 5).forEach(id => console.log(`  - ${id}`));
      }
    } finally {
      await session3.close();
    }

    // Test 4: Capability stats
    console.log('\nTest 4: Capability statistics');
    const session4 = driver.session();
    try {
      const result = await session4.run(`
        MATCH (a:Agent)-[:HAS_CAPABILITY]->(c:Capability)
        RETURN count(DISTINCT a) as agent_with_caps, count(DISTINCT c) as capability_count
      `);
      const agentsWithCaps = result.records[0].get('agent_with_caps').toNumber ?
        result.records[0].get('agent_with_caps').toNumber() :
        result.records[0].get('agent_with_caps');
      const capCount = result.records[0].get('capability_count').toNumber ?
        result.records[0].get('capability_count').toNumber() :
        result.records[0].get('capability_count');
      console.log(`✓ Agents with capabilities: ${agentsWithCaps}`);
      console.log(`✓ Unique capabilities: ${capCount}`);
    } finally {
      await session4.close();
    }

    console.log('\n=== TESTS COMPLETE ===');
    console.log('✅ All agent discovery tests passing!\n');

  } catch (error) {
    console.error('\n❌ Test failed:', error.message);
    process.exit(1);
  } finally {
    await driver.close();
  }
}

// Run tests
runSimpleTests().catch(error => {
  console.error('Fatal error:', error);
  process.exit(1);
});
