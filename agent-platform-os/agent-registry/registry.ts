/**
 * Agent Registry — in-memory store for agent metadata
 * Read from family-office-os OPCO agents, write capability updates
 * Round 3: Supabase integration replaces in-memory store
 */

export interface AgentMetadata {
  id: string;
  name: string;
  capabilities: string[];
  cost_per_hour: number;
  available: boolean;
  last_heartbeat: Date;
  max_concurrent_tasks: number;
  opco?: string;
}

export class AgentRegistry {
  private agents: Map<string, AgentMetadata> = new Map();

  /**
   * Register a new agent or update existing metadata
   */
  register_agent(metadata: AgentMetadata): void {
    metadata.last_heartbeat = new Date();
    this.agents.set(metadata.id, metadata);
    console.log(`[AgentRegistry] Registered agent: ${metadata.name} (${metadata.id})`);
  }

  /**
   * List all agents, optionally filtered by availability
   */
  list_agents(available_only?: boolean): AgentMetadata[] {
    const agents = Array.from(this.agents.values());
    if (available_only) {
      return agents.filter((a) => a.available);
    }
    return agents;
  }

  /**
   * Get agent by ID
   */
  get_agent(id: string): AgentMetadata | undefined {
    return this.agents.get(id);
  }

  /**
   * Update agent availability (heartbeat + status)
   */
  update_availability(id: string, available: boolean): void {
    const agent = this.agents.get(id);
    if (agent) {
      agent.available = available;
      agent.last_heartbeat = new Date();
      console.log(
        `[AgentRegistry] Updated ${agent.name}: available=${available}, heartbeat=${agent.last_heartbeat.toISOString()}`
      );
    }
  }

  /**
   * Check if agent has a capability
   */
  has_capability(id: string, capability: string): boolean {
    const agent = this.agents.get(id);
    return agent ? agent.capabilities.includes(capability) : false;
  }

  /**
   * Get all agents with a specific capability
   */
  agents_with_capability(capability: string): AgentMetadata[] {
    return Array.from(this.agents.values()).filter((a) =>
      a.capabilities.includes(capability)
    );
  }

  /**
   * Get agent load (approximate, for dispatch routing)
   * Returns: { agent_id, load_percentage }
   */
  get_agent_load(id: string): number {
    const agent = this.agents.get(id);
    if (!agent) return 0;
    // ponytail: naive load estimation; upgrade to per-agent task counter if contention matters
    return agent.available ? 30 : 100; // 30% baseline if available, 100% if not
  }
}
