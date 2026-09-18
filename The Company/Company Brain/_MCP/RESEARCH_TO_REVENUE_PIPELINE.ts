/**
 * RESEARCH_TO_REVENUE_PIPELINE.ts
 * 
 * Maps research outputs → capabilities → agents → revenue tracking
 * Complete end-to-end pipeline from discovery to revenue attribution
 * 
 * Phase 2a Task 3.3 | 3 hours
 */

import { CapabilityResolver, CapabilityNeed, ResolvedCapability } from './CAPABILITY_RESOLVER';
import { AgentDispatchRouter, TaskClassification } from './AGENT_DISPATCH_ROUTER';

// ============================================================
// TYPES
// ============================================================

export interface ResearchOutput {
  id: string;
  type: 'market_research' | 'user_research' | 'competitive_analysis' | 'opportunity';
  findings: string[];
  confidence: number;  // 0-1
  domain?: string;
  relatedCapabilities?: string[];
}

export interface OpportunitySignal {
  id: string;
  description: string;
  estimatedValue: number;  // potential revenue
  urgency: 'high' | 'medium' | 'low';
  capability?: string;
  agent?: string;
}

export interface RevenueAttribution {
  id: string;
  task_id: string;
  agent_id: string;
  capability_id: string;
  cost: number;
  projected_revenue: number;
  actual_revenue?: number;
  roi: number;  // actual_revenue / cost
  status: 'pending' | 'in_progress' | 'completed' | 'failed';
  created_at: string;
  completed_at?: string;
}

// ============================================================
// PIPELINE
// ============================================================

export class ResearchToRevenuePipeline {
  private capabilityResolver: CapabilityResolver;
  private dispatchRouter: AgentDispatchRouter;
  private attributionLog: RevenueAttribution[] = [];

  constructor(
    capabilityResolver: CapabilityResolver,
    dispatchRouter: AgentDispatchRouter
  ) {
    this.capabilityResolver = capabilityResolver;
    this.dispatchRouter = dispatchRouter;
  }

  /**
   * MAIN PIPELINE: Research → Capability → Agent → Revenue
   */
  async processResearchOutput(research: ResearchOutput): Promise<{
    signals: OpportunitySignal[];
    resolutions: ResolvedCapability[];
    attributions: RevenueAttribution[];
  }> {
    // Stage 1: Extract opportunity signals from research
    const signals = this.extractSignals(research);

    // Stage 2: Map signals to capabilities
    const resolutions = await Promise.all(
      signals.map(signal => this.resolveCapability(signal))
    );

    // Stage 3: Create revenue attribution records
    const attributions = resolutions.map((res, idx) => 
      this.createAttribution(signals[idx], res)
    );

    // Log attributions
    this.attributionLog.push(...attributions);

    return { signals, resolutions, attributions };
  }

  /**
   * SIGNAL EXTRACTION: Turn research into opportunity signals
   */
  private extractSignals(research: ResearchOutput): OpportunitySignal[] {
    const signals: OpportunitySignal[] = [];

    research.findings.forEach((finding, idx) => {
      // Parse finding for value + urgency signals
      const valueMatch = finding.match(/\$(\d+)(?:k|K)?(?:\s*-\s*\$?(\d+))?/);
      const value = valueMatch
        ? parseInt(valueMatch[1], 10) * (valueMatch[0].includes('k') ? 1000 : 1)
        : 50000;

      const urgency = finding.includes('urgent') || finding.includes('critical')
        ? 'high'
        : finding.includes('soon') ? 'medium' : 'low';

      signals.push({
        id: `signal-${research.id}-${idx}`,
        description: finding,
        estimatedValue: value,
        urgency,
        domain: research.domain,
      });
    });

    return signals;
  }

  /**
   * RESOLVE: Map signal to capability + agents
   */
  private async resolveCapability(signal: OpportunitySignal): Promise<ResolvedCapability> {
    const need: CapabilityNeed = {
      id: signal.id,
      description: signal.description,
      complexity: signal.urgency === 'high' ? 'complex' : 'moderate',
      domain: signal.domain,
      budget: signal.estimatedValue * 0.1,  // Reserve 10% for execution
    };

    return await this.capabilityResolver.resolveCapability(need);
  }

  /**
   * ATTRIBUTION: Create revenue tracking record
   */
  private createAttribution(
    signal: OpportunitySignal,
    resolution: ResolvedCapability
  ): RevenueAttribution {
    return {
      id: `attr-${signal.id}`,
      task_id: signal.id,
      agent_id: resolution.primaryAgent.id,
      capability_id: resolution.capability.id,
      cost: resolution.estimatedCost,
      projected_revenue: resolution.estimatedRevenue,
      roi: resolution.estimatedRevenue / Math.max(resolution.estimatedCost, 1),
      status: 'pending',
      created_at: new Date().toISOString(),
    };
  }

  /**
   * ROUTE: Dispatch to agent via dispatch router
   */
  async routeToAgent(resolution: ResolvedCapability): Promise<any> {
    // Classify task
    const task: TaskClassification = {
      intent: resolution.capability.slug,
      logicLayers: [resolution.capability.domain],
      domain: resolution.capability.domain,
      complexity: 'high',  // derived from workflow
    };

    // Dispatch
    const dispatch = await this.dispatchRouter.classifyTask(task);
    return dispatch;
  }

  /**
   * TRACK_EXECUTION: Monitor agent execution + revenue outcome
   */
  async trackExecution(
    attributionId: string,
    execution: { status: string; outcome?: any; revenue?: number }
  ): Promise<RevenueAttribution | null> {
    const attribution = this.attributionLog.find(a => a.id === attributionId);
    if (!attribution) return null;

    // Update status
    attribution.status = execution.status as 'completed' | 'in_progress' | 'failed';
    if (execution.status === 'completed') {
      attribution.completed_at = new Date().toISOString();
      if (execution.revenue) {
        attribution.actual_revenue = execution.revenue;
        attribution.roi = execution.revenue / Math.max(attribution.cost, 1);
      }
    }

    return attribution;
  }

  /**
   * REPORT: Generate pipeline metrics
   */
  getMetrics(): {
    totalSignals: number;
    totalCost: number;
    projectedRevenue: number;
    actualRevenue: number;
    roi: number;
    completedTasks: number;
  } {
    const completed = this.attributionLog.filter(a => a.status === 'completed');
    const totalCost = this.attributionLog.reduce((sum, a) => sum + a.cost, 0);
    const projectedRev = this.attributionLog.reduce((sum, a) => sum + a.projected_revenue, 0);
    const actualRev = completed.reduce((sum, a) => sum + (a.actual_revenue || 0), 0);

    return {
      totalSignals: this.attributionLog.length,
      totalCost,
      projectedRevenue: projectedRev,
      actualRevenue: actualRev,
      roi: actualRev / Math.max(totalCost, 1),
      completedTasks: completed.length,
    };
  }
}

export default ResearchToRevenuePipeline;
