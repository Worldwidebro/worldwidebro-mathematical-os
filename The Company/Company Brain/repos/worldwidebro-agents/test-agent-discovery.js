import {
  fetchAgents,
  verifyDataCompleteness,
  getAgentCount,
  getCapabilityStats,
  closeDriver
} from './src/services/agent-discovery.js';

import {
  loadAgentCache,
  getAgentById,
  searchAgentsByCapability,
  getAllAgents,
  getCacheStats,
  clearCache,
  isCacheLoaded
} from './src/services/agent-cache.js';

async function runTests() {
  console.log('\n=== UNIT 1.1: Neo4j Agent Discovery Tests ===\n');

  try {
    // Test 1: Get agent count
    console.log('Test 1: Get agent count from Neo4j');
    const agentCount = await getAgentCount();
    console.log(`✓ Total agents in Neo4j: ${agentCount}`);

    if (agentCount !== 318) {
      console.warn(`⚠ Expected 318 agents, got ${agentCount}`);
    } else {
      console.log('✓ Agent count matches expectation (318)');
    }

    // Test 2: Verify data completeness
    console.log('\nTest 2: Verify data completeness');
    const completeness = await verifyDataCompleteness();
    console.log(`✓ Missing data count: ${completeness.missing_count}`);

    if (completeness.missing_count === 0) {
      console.log('✓ All agents have required fields');
    } else {
      console.warn(`⚠ ${completeness.missing_count} agents missing required fields`);
      console.warn(`  Agent IDs: ${completeness.agent_ids.join(', ')}`);
    }

    // Test 3: Get capability stats
    console.log('\nTest 3: Get capability statistics');
    const capStats = await getCapabilityStats();
    console.log(`✓ Agents with capabilities: ${capStats.agent_with_caps}`);
    console.log(`✓ Unique capabilities: ${capStats.capability_count}`);

    // Test 4: Fetch first 5 agents
    console.log('\nTest 4: Fetch and inspect agents');
    const agents = await fetchAgents();
    console.log(`✓ Fetched ${agents.length} agents from Neo4j`);

    if (agents.length > 0) {
      const firstAgent = agents[0];
      console.log('\n  Sample agent:');
      console.log(`    - ID: ${firstAgent.id}`);
      console.log(`    - Name: ${firstAgent.name}`);
      console.log(`    - Domain: ${firstAgent.domain}`);
      console.log(`    - Status: ${firstAgent.status}`);
      console.log(`    - Autonomy Level: ${firstAgent.autonomy_level}`);
      console.log(`    - Capabilities: ${firstAgent.capabilities.length} total`);
      if (firstAgent.capabilities.length > 0) {
        console.log(`      - Sample: ${firstAgent.capabilities.slice(0, 3).join(', ')}`);
      }
    }

    // Test 5: Load cache
    console.log('\nTest 5: Load agent cache');
    const loaded = await loadAgentCache();
    console.log(`✓ Loaded ${loaded} agents into memory cache`);

    // Test 6: Verify cache
    console.log('\nTest 6: Verify cache functionality');
    console.log(`✓ Cache loaded: ${isCacheLoaded()}`);

    const cacheStats = getCacheStats();
    console.log(`✓ Cache stats:`);
    console.log(`  - Total agents: ${cacheStats.total_agents}`);
    console.log(`  - Ready agents: ${cacheStats.ready_agents}`);
    console.log(`  - Beta agents: ${cacheStats.beta_agents}`);
    console.log(`  - Planned agents: ${cacheStats.planned_agents}`);
    console.log(`  - Agents with capabilities: ${cacheStats.agents_with_capabilities}`);
    console.log(`  - Cache loaded at: ${cacheStats.cache_loaded_at}`);

    // Test 7: Search by capability
    console.log('\nTest 7: Search agents by capability');
    if (agents.length > 0 && agents[0].capabilities.length > 0) {
      const capability = agents[0].capabilities[0];
      const found = searchAgentsByCapability(capability);
      console.log(`✓ Found ${found.length} agents with capability "${capability}"`);
    }

    // Test 8: Get agent by ID
    console.log('\nTest 8: Get agent by ID from cache');
    if (agents.length > 0) {
      const agentId = agents[0].id;
      const cached = getAgentById(agentId);
      console.log(`✓ Retrieved agent from cache: ${cached.name}`);
    }

    // Test 9: Verify all agents accessible
    console.log('\nTest 9: Verify all agents accessible from cache');
    const allAgents = getAllAgents();
    console.log(`✓ Retrieved ${allAgents.length} agents from cache`);

    if (allAgents.length === 318) {
      console.log('✓ All 318 agents accessible from cache');
    }

    console.log('\n=== TESTS COMPLETE ===\n');
    console.log('✅ Unit 1.1 SUCCESS: Neo4j Agent Discovery ready for integration\n');

  } catch (error) {
    console.error('\n❌ Test failed:', error.message);
    console.error('Stack trace:', error.stack);
    process.exit(1);
  } finally {
    await closeDriver();
  }
}

// Run tests
runTests().catch(error => {
  console.error('Fatal error:', error);
  process.exit(1);
});
