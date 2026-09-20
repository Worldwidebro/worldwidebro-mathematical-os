import neo4j from 'neo4j-driver';
import dotenv from 'dotenv';

dotenv.config();

/**
 * @typedef {Object} Agent
 * @property {string} id
 * @property {string} name
 * @property {string} domain
 * @property {string} category
 * @property {string} description
 * @property {string[]} capabilities
 * @property {'L1' | 'L2' | 'L3'} autonomy_level
 * @property {'READY' | 'BETA' | 'PLANNED'} status
 * @property {number} cost_per_invocation
 * @property {number} estimated_revenue
 */

const driver = neo4j.driver(
  process.env.NEO4J_URI || 'bolt://100.87.214.70:7687',
  neo4j.auth.basic(
    process.env.NEO4J_USER || 'neo4j',
    process.env.NEO4J_PASSWORD || 'changeme'
  )
);

/**
 * Fetch all agents from Neo4j with their capabilities
 * @returns {Promise<Agent[]>}
 */
async function fetchAgents() {
  const session = driver.session();
  try {
    const result = await session.run(`
      MATCH (a:Agent)
      OPTIONAL MATCH (a)-[:HAS_CAPABILITY]->(cap:Capability)
      RETURN {
        id: a.id,
        name: a.name,
        domain: a.domain,
        category: a.category,
        description: a.description,
        capabilities: collect(cap.name),
        autonomy_level: a.autonomy_level,
        status: a.status,
        cost_per_invocation: a.cost_per_invocation,
        estimated_revenue: a.estimated_revenue
      } as agent
      ORDER BY a.name
    `);

    return result.records.map(record => record.get('agent'));
  } catch (error) {
    console.error('Error fetching agents from Neo4j:', error);
    throw error;
  } finally {
    await session.close();
  }
}

/**
 * Verify all agents have required fields
 * @returns {Promise<{missing_count: number, agent_ids: string[]}>}
 */
async function verifyDataCompleteness() {
  const session = driver.session();
  try {
    const result = await session.run(`
      MATCH (a:Agent)
      WITH a,
        CASE WHEN a.id IS NOT NULL THEN 1 ELSE 0 END as has_id,
        CASE WHEN a.name IS NOT NULL THEN 1 ELSE 0 END as has_name,
        CASE WHEN a.domain IS NOT NULL THEN 1 ELSE 0 END as has_domain,
        CASE WHEN a.status IS NOT NULL THEN 1 ELSE 0 END as has_status,
        CASE WHEN a.cost_per_invocation IS NOT NULL THEN 1 ELSE 0 END as has_cost,
        CASE WHEN a.estimated_revenue IS NOT NULL THEN 1 ELSE 0 END as has_revenue
      WHERE NOT (has_id AND has_name AND has_domain AND has_status AND has_cost AND has_revenue)
      RETURN count(*) as missing_count, collect(a.id) as agent_ids
    `);

    if (result.records.length > 0) {
      const record = result.records[0];
      return {
        missing_count: record.get('missing_count').toNumber ? record.get('missing_count').toNumber() : record.get('missing_count'),
        agent_ids: record.get('agent_ids') || []
      };
    }

    return { missing_count: 0, agent_ids: [] };
  } catch (error) {
    console.error('Error verifying data completeness:', error);
    throw error;
  } finally {
    await session.close();
  }
}

/**
 * Get total count of agents in Neo4j
 * @returns {Promise<number>}
 */
async function getAgentCount() {
  const session = driver.session();
  try {
    const result = await session.run(`
      MATCH (a:Agent)
      RETURN count(a) as total_agents
    `);

    if (result.records.length > 0) {
      const count = result.records[0].get('total_agents');
      return count.toNumber ? count.toNumber() : count;
    }

    return 0;
  } catch (error) {
    console.error('Error getting agent count:', error);
    throw error;
  } finally {
    await session.close();
  }
}

/**
 * Get capability count and verify relationships
 * @returns {Promise<{agent_with_caps: number, capability_count: number}>}
 */
async function getCapabilityStats() {
  const session = driver.session();
  try {
    const result = await session.run(`
      MATCH (a:Agent)-[:HAS_CAPABILITY]->(c:Capability)
      RETURN count(DISTINCT a) as agent_with_caps, count(DISTINCT c) as capability_count
    `);

    if (result.records.length > 0) {
      const record = result.records[0];
      return {
        agent_with_caps: record.get('agent_with_caps').toNumber ? record.get('agent_with_caps').toNumber() : record.get('agent_with_caps'),
        capability_count: record.get('capability_count').toNumber ? record.get('capability_count').toNumber() : record.get('capability_count')
      };
    }

    return { agent_with_caps: 0, capability_count: 0 };
  } catch (error) {
    console.error('Error getting capability stats:', error);
    throw error;
  } finally {
    await session.close();
  }
}

/**
 * Close the driver connection
 * @returns {Promise<void>}
 */
async function closeDriver() {
  await driver.close();
}

export {
  fetchAgents,
  verifyDataCompleteness,
  getAgentCount,
  getCapabilityStats,
  closeDriver,
  driver
};
