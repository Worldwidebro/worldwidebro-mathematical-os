import { fetchAgents } from './agent-discovery.js';

/**
 * In-memory cache for agents
 * @type {Map<string, Object>}
 */
let agentCache = new Map();

/**
 * Timestamp when cache was last loaded
 * @type {Date | null}
 */
let cacheLoadedAt = null;

/**
 * Load all agents into memory cache from Neo4j
 * @returns {Promise<number>} Number of agents loaded
 */
async function loadAgentCache() {
  try {
    const agents = await fetchAgents();

    // Clear existing cache
    agentCache.clear();

    // Populate cache
    agents.forEach(agent => {
      agentCache.set(agent.id, agent);
    });

    cacheLoadedAt = new Date();
    console.log(`✓ Loaded ${agents.length} agents into cache at ${cacheLoadedAt.toISOString()}`);

    return agents.length;
  } catch (error) {
    console.error('Failed to load agent cache:', error);
    throw error;
  }
}

/**
 * Get a single agent by ID
 * @param {string} id - Agent ID
 * @returns {Object | undefined}
 */
function getAgentById(id) {
  return agentCache.get(id);
}

/**
 * Search agents by capability
 * @param {string} capability - Capability name to search for
 * @returns {Object[]}
 */
function searchAgentsByCapability(capability) {
  return Array.from(agentCache.values()).filter(agent =>
    agent.capabilities && agent.capabilities.includes(capability)
  );
}

/**
 * Search agents by domain
 * @param {string} domain - Domain name
 * @returns {Object[]}
 */
function searchAgentsByDomain(domain) {
  return Array.from(agentCache.values()).filter(agent =>
    agent.domain === domain
  );
}

/**
 * Search agents by status
 * @param {'READY' | 'BETA' | 'PLANNED'} status - Agent status
 * @returns {Object[]}
 */
function searchAgentsByStatus(status) {
  return Array.from(agentCache.values()).filter(agent =>
    agent.status === status
  );
}

/**
 * Search agents by autonomy level
 * @param {'L1' | 'L2' | 'L3'} level - Autonomy level
 * @returns {Object[]}
 */
function searchAgentsByAutonomyLevel(level) {
  return Array.from(agentCache.values()).filter(agent =>
    agent.autonomy_level === level
  );
}

/**
 * Get all agents from cache
 * @returns {Object[]}
 */
function getAllAgents() {
  return Array.from(agentCache.values());
}

/**
 * Get cache statistics
 * @returns {{total_agents: number, ready_agents: number, beta_agents: number, planned_agents: number, agents_with_capabilities: number, cache_loaded_at: string | null}}
 */
function getCacheStats() {
  const all = Array.from(agentCache.values());
  const ready = all.filter(a => a.status === 'READY').length;
  const beta = all.filter(a => a.status === 'BETA').length;
  const planned = all.filter(a => a.status === 'PLANNED').length;
  const withCaps = all.filter(a => a.capabilities && a.capabilities.length > 0).length;

  return {
    total_agents: agentCache.size,
    ready_agents: ready,
    beta_agents: beta,
    planned_agents: planned,
    agents_with_capabilities: withCaps,
    cache_loaded_at: cacheLoadedAt ? cacheLoadedAt.toISOString() : null
  };
}

/**
 * Clear the cache
 */
function clearCache() {
  agentCache.clear();
  cacheLoadedAt = null;
  console.log('✓ Agent cache cleared');
}

/**
 * Check if cache is loaded
 * @returns {boolean}
 */
function isCacheLoaded() {
  return agentCache.size > 0;
}

/**
 * Get cache age in milliseconds
 * @returns {number | null}
 */
function getCacheAge() {
  if (!cacheLoadedAt) return null;
  return Date.now() - cacheLoadedAt.getTime();
}

export {
  loadAgentCache,
  getAgentById,
  searchAgentsByCapability,
  searchAgentsByDomain,
  searchAgentsByStatus,
  searchAgentsByAutonomyLevel,
  getAllAgents,
  getCacheStats,
  clearCache,
  isCacheLoaded,
  getCacheAge
};
