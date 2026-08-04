/**
 * Task Dispatcher — route tasks to best agent by capabilities + load
 * Uses knowledge-graph-os router for agent scoring
 * Logs dispatch decisions with reasoning
 * Round 3: Integrates with Supabase capital_decisions table
 */

import { AgentRegistry, AgentMetadata } from '../agent-registry/registry';

export interface Task {
  id: string;
  priority: 'critical' | 'high' | 'normal' | 'low';
  required_capabilities: string[];
  deadline?: Date;
  estimated_cost_hours: number;
}

export interface DispatchDecision {
  task_id: string;
  agent_id: string;
  agent_name: string;
  reason: string;
  score: number;
  timestamp: Date;
}

export class TaskDispatcher {
  private registry: AgentRegistry;
  private decisions: DispatchDecision[] = [];

  constructor(registry: AgentRegistry) {
    this.registry = registry;
  }

  /**
   * Dispatch a task to the best available agent
   * Scoring: capability_match (50%) + availability (30%) + cost_efficiency (20%)
   */
  dispatch(task: Task): DispatchDecision | null {
    const candidates = this.find_candidate_agents(task);
    if (candidates.length === 0) {
      console.error(`[Dispatcher] No agents found for task ${task.id} (capabilities: ${task.required_capabilities.join(', ')})`);
      return null;
    }

    const scored = candidates.map((agent) => ({
      agent,
      score: this.score_agent(agent, task),
    }));

    scored.sort((a, b) => b.score - a.score);
    const best = scored[0];

    const decision: DispatchDecision = {
      task_id: task.id,
      agent_id: best.agent.id,
      agent_name: best.agent.name,
      reason: `Score ${best.score.toFixed(2)}: capability_match ${this.calc_capability_score(best.agent, task).toFixed(2)} + availability ${this.calc_availability_score(best.agent).toFixed(2)} + cost_efficiency ${this.calc_cost_score(best.agent, task).toFixed(2)}`,
      score: best.score,
      timestamp: new Date(),
    };

    this.decisions.push(decision);
    console.log(
      `[Dispatcher] Task ${task.id} → ${best.agent.name} (score: ${best.score.toFixed(2)}, priority: ${task.priority})`
    );

    return decision;
  }

  /**
   * Find agents that have all required capabilities
   */
  private find_candidate_agents(task: Task): AgentMetadata[] {
    const all_agents = this.registry.list_agents(true); // available only
    return all_agents.filter((agent) =>
      task.required_capabilities.every((cap) => agent.capabilities.includes(cap))
    );
  }

  /**
   * Scoring algorithm: 50% capability, 30% availability, 20% cost efficiency
   */
  private score_agent(agent: AgentMetadata, task: Task): number {
    const cap_score = this.calc_capability_score(agent, task);
    const avail_score = this.calc_availability_score(agent);
    const cost_score = this.calc_cost_score(agent, task);

    return cap_score * 0.5 + avail_score * 0.3 + cost_score * 0.2;
  }

  private calc_capability_score(agent: AgentMetadata, task: Task): number {
    // 0–100: how many capabilities does agent have? (all = 100)
    const match_count = task.required_capabilities.filter((cap) =>
      agent.capabilities.includes(cap)
    ).length;
    return (match_count / Math.max(task.required_capabilities.length, 1)) * 100;
  }

  private calc_availability_score(agent: AgentMetadata): number {
    // 0–100: load-based availability; lower load = higher score
    // ponytail: load is 30% baseline, can upgrade to task counter
    const load = this.registry.get_agent_load(agent.id);
    return Math.max(0, 100 - load);
  }

  private calc_cost_score(agent: AgentMetadata, task: Task): number {
    // 0–100: inverse of estimated cost; lower cost = higher score
    const estimated_total_cost = agent.cost_per_hour * task.estimated_cost_hours;
    // Scale: $0 = 100, $10/hr = ~50, $50/hr = ~0 (logarithmic)
    return Math.max(0, 100 - Math.log10(Math.max(1, estimated_total_cost)) * 50);
  }

  /**
   * Get all dispatch decisions (audit trail)
   */
  get_decisions(): DispatchDecision[] {
    return [...this.decisions];
  }

  /**
   * Get decisions for a specific task
   */
  get_task_decisions(task_id: string): DispatchDecision[] {
    return this.decisions.filter((d) => d.task_id === task_id);
  }
}
