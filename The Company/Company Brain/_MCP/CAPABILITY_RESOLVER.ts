/**
 * CAPABILITY_RESOLVER.ts
 * 
 * Resolves user needs/capabilities to supporting agents.
 * - Single capability lookup
 * - Complex multi-agent workflows via DAG
 * - Fallback + escalation handling
 * - Integration with AGENT_DISPATCH_ROUTER
 * 
 * Phase 2a Task 3.2 | 4 hours
 */

import { Agent } from './AGENT_REGISTRY';
import { Capability } from './CAPABILITY_REGISTRY';
import { ToolGatewayRegistry } from './TOOL_GATEWAY_REGISTRY';

// ============================================================
// TYPE DEFINITIONS
// ============================================================

export interface CapabilityNeed {
  id: string;
  description: string;
  complexity: 'simple' | 'moderate' | 'complex';
  domain?: string;
  logicLayers?: string[];
  requiredSkills?: string[];
  budget?: number;  // Max spend for this capability
  timeline?: number;  // Days to completion
}

export interface ResolvedCapability {
  capability: Capability;
  matchConfidence: number;  // 0-1
  primaryAgent: Agent;
  secondaryAgents: Agent[];
  workflow?: AgentWorkflow;
  estimatedCost: number;
  estimatedRevenue: number;
  autonomyLevel: 'L1' | 'L2' | 'L3';
  fallbackOptions?: ResolvedCapability[];
  escalationPath?: string;
}

export interface AgentWorkflow {
  name: string;
  steps: WorkflowStep[];
  dependencies: WorkflowDependency[];
  parallelizable: boolean;
  estimatedDuration: number;  // minutes
}

export interface WorkflowStep {
  id: string;
  agent: Agent;
  capability: Capability;
  inputs: Record<string, any>;
  outputs: Record<string, any>;
  autonomyLevel: 'L1' | 'L2' | 'L3';
  fallback?: WorkflowStep;
  timeout: number;  // seconds
}

export interface WorkflowDependency {
  fromStep: string;
  toStep: string;
  type: 'sequential' | 'parallel';
  passthrough: string[];  // Which outputs pass to next step
}

// ============================================================
// CAPABILITY RESOLVER CLASS
// ============================================================

export class CapabilityResolver {
  private capabilityRegistry: Map<string, Capability>;
  private agentRegistry: Map<string, Agent>;
  private toolGateway: ToolGatewayRegistry;

  constructor(
    capabilities: Capability[],
    agents: Agent[],
    toolGateway: ToolGatewayRegistry
  ) {
    this.capabilityRegistry = new Map(
      capabilities.map(c => [c.slug, c])
    );
    this.agentRegistry = new Map(
      agents.map(a => [a.id, a])
    );
    this.toolGateway = toolGateway;
  }

  /**
   * RESOLVE: Find agents that support a capability need
   */
  async resolveCapability(need: CapabilityNeed): Promise<ResolvedCapability> {
    // 1. Search for matching capabilities
    const matches = this.searchCapabilities(need);
    if (!matches.length) {
      return this.handleNoMatch(need);
    }

    // 2. Score and rank candidates
    const ranked = this.rankByRelevance(matches, need);
    const topMatch = ranked[0];

    // 3. Get supporting agents
    const agents = this.getAgents(topMatch.capability);
    const primary = agents[0];
    const secondary = agents.slice(1);

    // 4. Build workflow if multi-agent needed
    let workflow: AgentWorkflow | undefined;
    if (need.complexity === 'complex' && agents.length > 1) {
      workflow = await this.buildWorkflow(topMatch.capability, agents, need);
    }

    // 5. Calculate costs + autonomy level
    const cost = this.estimateCost(primary, topMatch.capability);
    const autonomy = this.determineAutonomyLevel(cost, need.budget);
    const revenue = this.estimateRevenue(topMatch.capability, need);

    // 6. Prepare fallbacks + escalation
    const fallbacks = ranked.slice(1, 3).map(m => ({
      capability: m.capability,
      matchConfidence: m.confidence,
      primaryAgent: this.getAgents(m.capability)[0],
      secondaryAgents: this.getAgents(m.capability).slice(1),
      estimatedCost: this.estimateCost(this.getAgents(m.capability)[0], m.capability),
      estimatedRevenue: this.estimateRevenue(m.capability, need),
      autonomyLevel: autonomy,
    } as ResolvedCapability));

    return {
      capability: topMatch.capability,
      matchConfidence: topMatch.confidence,
      primaryAgent: primary,
      secondaryAgents: secondary,
      workflow,
      estimatedCost: cost,
      estimatedRevenue: revenue,
      autonomyLevel: autonomy,
      fallbackOptions: fallbacks,
      escalationPath: this.getEscalationPath(need),
    };
  }

  /**
   * SEARCH: Find capabilities matching the need
   */
  private searchCapabilities(need: CapabilityNeed): 
    Array<{ capability: Capability; matchType: string }> {
    const results: Array<{ capability: Capability; matchType: string }> = [];

    // Exact slug match
    const exact = this.capabilityRegistry.get(need.description.toLowerCase().replace(/\s+/g, '-'));
    if (exact) {
      results.push({ capability: exact, matchType: 'exact' });
    }

    // Domain filter
    const domainMatches = Array.from(this.capabilityRegistry.values())
      .filter(c => need.domain && c.domain === need.domain)
      .slice(0, 5);
    results.push(...domainMatches.map(c => ({ capability: c, matchType: 'domain' })));

    // Skill-based match (if requiredSkills provided)
    if (need.requiredSkills?.length) {
      const skillMatches = Array.from(this.capabilityRegistry.values())
        .filter(c => need.requiredSkills?.some(s => 
          (c.required_skills || []).includes(s)
        ))
        .slice(0, 5);
      results.push(...skillMatches.map(c => ({ capability: c, matchType: 'skill' })));
    }

    // Remove duplicates
    const seen = new Set<string>();
    return results.filter(r => {
      if (seen.has(r.capability.id)) return false;
      seen.add(r.capability.id);
      return true;
    });
  }

  /**
   * RANK: Score matches by relevance
   */
  private rankByRelevance(
    matches: Array<{ capability: Capability; matchType: string }>,
    need: CapabilityNeed
  ): Array<{ capability: Capability; confidence: number }> {
    return matches
      .map(m => ({
        capability: m.capability,
        confidence: this.scoreMatch(m.capability, m.matchType, need),
      }))
      .sort((a, b) => b.confidence - a.confidence);
  }

  /**
   * SCORE: Confidence score for match
   */
  private scoreMatch(
    capability: Capability,
    matchType: string,
    need: CapabilityNeed
  ): number {
    const baseScore: Record<string, number> = {
      exact: 1.0,
      domain: 0.8,
      skill: 0.7,
    };

    let score = baseScore[matchType] || 0.5;

    // Boost if success_rate is high
    if (capability.success_rate_percent) {
      const rateBoost = (capability.success_rate_percent - 75) / 250;
      score = Math.min(1.0, score + rateBoost * 0.1);
    }

    // Penalize if cost exceeds budget
    const cost = this.estimateCost(
      this.getAgents(capability)[0],
      capability
    );
    if (need.budget && cost > need.budget) {
      score *= 0.7;
    }

    return score;
  }

  /**
   * GET_AGENTS: Retrieve agents supporting capability
   */
  private getAgents(capability: Capability): Agent[] {
    if (!capability.supported_agents?.length) {
      return [];
    }

    return capability.supported_agents
      .map(agentId => this.agentRegistry.get(agentId))
      .filter(Boolean) as Agent[];
  }

  /**
   * BUILD_WORKFLOW: Design DAG for multi-agent execution
   */
  private async buildWorkflow(
    capability: Capability,
    agents: Agent[],
    need: CapabilityNeed
  ): Promise<AgentWorkflow> {
    const steps: WorkflowStep[] = agents.map((agent, idx) => ({
      id: `step-${idx + 1}`,
      agent,
      capability: { ...capability },
      inputs: {},
      outputs: {},
      autonomyLevel: 'L2',
      timeout: 3600,
    }));

    const dependencies: WorkflowDependency[] = [];
    for (let i = 0; i < steps.length - 1; i++) {
      dependencies.push({
        fromStep: steps[i].id,
        toStep: steps[i + 1].id,
        type: 'sequential',
        passthrough: ['output', 'metrics'],
      });
    }

    return {
      name: `${capability.name} Workflow`,
      steps,
      dependencies,
      parallelizable: false,
      estimatedDuration: steps.length * 60,
    };
  }

  /**
   * ESTIMATE_COST: Calculate agent + tool cost
   */
  private estimateCost(agent: Agent, capability: Capability): number {
    const agentBaseCost = 5;
    const toolCosts = (capability.required_tools || [])
      .reduce((sum, toolId) => {
        const tool = this.toolGateway.tools.find(t => t.id === toolId);
        return sum + (tool?.cost_per_call ? parseFloat(String(tool.cost_per_call)) : 0);
      }, 0);

    return agentBaseCost + toolCosts;
  }

  /**
   * ESTIMATE_REVENUE: Projected revenue from capability
   */
  private estimateRevenue(
    capability: Capability,
    need: CapabilityNeed
  ): number {
    const revMatch = (capability.revenue_per_use || "$0")
      .match(/\$(\d+)(?:-\$?(\d+))?/);
    if (!revMatch) return 0;

    const min = parseInt(revMatch[1], 10);
    const max = revMatch[2] ? parseInt(revMatch[2], 10) : min;
    return (min + max) / 2;
  }

  /**
   * AUTONOMY_LEVEL: Determine L1/L2/L3 based on cost + budget
   */
  private determineAutonomyLevel(cost: number, budget?: number): 'L1' | 'L2' | 'L3' {
    if (cost > 1000) return 'L1';
    if (budget && cost > budget * 0.8) return 'L1';
    if (cost > 50) return 'L2';
    return 'L3';
  }

  /**
   * ESCALATION_PATH: Get human escalation route
   */
  private getEscalationPath(need: CapabilityNeed): string {
    if (need.complexity === 'complex') {
      return 'route_to_manager';
    }
    return 'route_to_domain_expert';
  }

  /**
   * NO_MATCH: Handle when capability not found
   */
  private handleNoMatch(need: CapabilityNeed): Promise<ResolvedCapability> {
    const fallback: Capability = {
      id: 'cap-fallback',
      name: 'Manual Review Required',
      slug: 'manual-review',
      description: `Capability "${need.description}" not found. Requires manual expert review.`,
      category: 'escalation',
      domain: need.domain || 'unknown',
      supported_agents: [],
      required_tools: [],
      required_skills: [],
      revenue_per_use: '$0',
      success_rate_percent: 0,
      last_verified: new Date().toISOString().split('T')[0],
    };

    return Promise.resolve({
      capability: fallback,
      matchConfidence: 0,
      primaryAgent: { id: 'escalation-queue', name: 'Human Expert' } as any,
      secondaryAgents: [],
      estimatedCost: 0,
      estimatedRevenue: 0,
      autonomyLevel: 'L1',
      escalationPath: 'escalate_to_cto',
    });
  }
}

export default CapabilityResolver;
