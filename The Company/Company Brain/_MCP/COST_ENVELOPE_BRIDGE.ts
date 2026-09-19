/**
 * OmniRoute Cost Envelope Bridge
 * Listens to A2A task completion and flows cost data to Supabase task_executions
 *
 * Authority: CP-027 (Engineering Infrastructure)
 * Updated: 2026-09-19
 */

import { createClient } from "@supabase/supabase-js";

interface CostEnvelope {
  estimated: number; // USD
  actual: number; // USD
  currency: "USD" | "EUR" | "GBP";
}

interface A2ATaskCompletion {
  task: {
    id: string;
    state: "completed" | "failed";
  };
  metadata: {
    cost_envelope: CostEnvelope;
    policy_verdict: {
      allowed: boolean;
      reason: string;
    };
    routing_explanation: string;
    resilience_trace: any[];
  };
}

interface TaskExecution {
  id?: string;
  task_id: string;
  agent_id: string;
  cost_estimated: number;
  cost_actual: number;
  revenue_projected: number;
  roi_calculated: number;
  status: "running" | "completed" | "failed";
  metadata: Record<string, any>;
  created_at?: string;
  updated_at?: string;
}

export class CostEnvelopeBridge {
  private supabase: ReturnType<typeof createClient>;
  private supabaseUrl: string;
  private supabaseKey: string;

  constructor(supabaseUrl: string, supabaseKey: string) {
    this.supabaseUrl = supabaseUrl;
    this.supabaseKey = supabaseKey;
    this.supabase = createClient(supabaseUrl, supabaseKey);
  }

  /**
   * Listen to OmniRoute A2A task completion and flow cost to Supabase
   */
  async processCostEnvelope(completion: A2ATaskCompletion, agentId: string, projectedRevenue: number): Promise<TaskExecution> {
    const { task, metadata } = completion;
    const { cost_envelope, policy_verdict } = metadata;

    // Verify cost is within acceptable bounds (± 10%)
    const variance = Math.abs((cost_envelope.actual - cost_envelope.estimated) / cost_envelope.estimated);
    if (variance > 0.1) {
      console.warn(`⚠️  Cost variance exceeded: estimated $${cost_envelope.estimated}, actual $${cost_envelope.actual}`);
    }

    // Calculate ROI
    const roi = projectedRevenue / (cost_envelope.actual || 0.01);

    // Build task execution record
    const execution: TaskExecution = {
      task_id: task.id,
      agent_id: agentId,
      cost_estimated: cost_envelope.estimated,
      cost_actual: cost_envelope.actual,
      revenue_projected: projectedRevenue,
      roi_calculated: roi,
      status: task.state === "completed" ? "completed" : "failed",
      metadata: {
        policy_allowed: policy_verdict.allowed,
        policy_reason: policy_verdict.reason,
        routing_explanation: metadata.routing_explanation,
        currency: cost_envelope.currency,
        variance_percent: (variance * 100).toFixed(2),
      },
    };

    try {
      // Insert or update task_executions in Supabase
      const { data, error } = await this.supabase.from("task_executions").insert([execution]).select();

      if (error) {
        throw new Error(`Supabase insert failed: ${error.message}`);
      }

      console.log(`✅ Cost envelope recorded for task ${task.id}:`);
      console.log(`   Actual cost: $${cost_envelope.actual} | Projected revenue: $${projectedRevenue} | ROI: ${roi.toFixed(2)}x`);

      return data?.[0] as TaskExecution;
    } catch (error) {
      console.error(`❌ Failed to log cost envelope:`, error);
      throw error;
    }
  }

  /**
   * Query task execution costs for a given agent
   */
  async getAgentMetrics(agentId: string): Promise<{
    total_cost: number;
    total_revenue: number;
    total_roi: number;
    task_count: number;
    avg_roi: number;
  }> {
    try {
      const { data, error } = await this.supabase
        .from("task_executions")
        .select("cost_actual, revenue_projected")
        .eq("agent_id", agentId)
        .eq("status", "completed");

      if (error) throw error;

      const metrics = data?.reduce(
        (acc, task) => {
          acc.total_cost += task.cost_actual || 0;
          acc.total_revenue += task.revenue_projected || 0;
          acc.task_count += 1;
          return acc;
        },
        { total_cost: 0, total_revenue: 0, task_count: 0 }
      ) || { total_cost: 0, total_revenue: 0, task_count: 0 };

      metrics.total_roi = metrics.total_cost > 0 ? metrics.total_revenue / metrics.total_cost : 0;
      metrics.avg_roi = metrics.task_count > 0 ? metrics.total_roi / metrics.task_count : 0;

      return metrics as any;
    } catch (error) {
      console.error(`❌ Failed to fetch agent metrics:`, error);
      throw error;
    }
  }

  /**
   * Audit cost variance for all tasks (sanity check)
   */
  async auditCostVariance(agentId: string, varianceThreshold: number = 0.1): Promise<any[]> {
    try {
      const { data, error } = await this.supabase
        .from("task_executions")
        .select("task_id, cost_estimated, cost_actual")
        .eq("agent_id", agentId);

      if (error) throw error;

      const outliers = data?.filter((task) => {
        const variance = Math.abs((task.cost_actual - task.cost_estimated) / task.cost_estimated);
        return variance > varianceThreshold;
      });

      if (outliers && outliers.length > 0) {
        console.warn(`⚠️  Found ${outliers.length} cost outliers for agent ${agentId}:`);
        outliers.forEach((task) => {
          const variance = (
            ((task.cost_actual - task.cost_estimated) / task.cost_estimated) *
            100
          ).toFixed(2);
          console.warn(`   Task ${task.task_id}: ${variance}% variance`);
        });
      }

      return outliers || [];
    } catch (error) {
      console.error(`❌ Cost variance audit failed:`, error);
      throw error;
    }
  }
}

export default CostEnvelopeBridge;
