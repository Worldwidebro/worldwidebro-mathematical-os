/**
 * Revenue Attribution Bridge
 * Tracks research → task → agent → deal → revenue to attribute revenue to agents
 *
 * Authority: CP-021 (Revenue Control Plane)
 * Updated: 2026-09-19
 */

import { createClient } from "@supabase/supabase-js";

interface TaskExecution {
  id: string;
  task_id: string;
  agent_id: string;
  cost_actual: number;
  revenue_projected: number;
  status: string;
}

interface DealClosure {
  deal_id: string;
  value_usd: number;
  closed_date: string;
  source_task_id?: string;
  attributed_agents?: string[];
}

interface RevenueAttribution {
  deal_id: string;
  agent_id: string;
  task_id: string;
  revenue_attributed: number;
  cost_incurred: number;
  roi: number;
  attribution_date: string;
  contribution_percent: number;
}

export class RevenueAttributionBridge {
  private supabase: ReturnType<typeof createClient>;

  constructor(supabaseUrl: string, supabaseKey: string) {
    this.supabase = createClient(supabaseUrl, supabaseKey);
  }

  /**
   * When a deal closes, attribute revenue to contributing agents
   */
  async attributeRevenueToDeal(deal: DealClosure): Promise<RevenueAttribution[]> {
    try {
      // Find all tasks that contributed to this deal
      const { data: tasks, error: taskError } = await this.supabase
        .from("task_executions")
        .select("*")
        .eq("deal_id", deal.deal_id);

      if (taskError) throw taskError;

      const attributions: RevenueAttribution[] = [];
      const totalTaskCost = tasks?.reduce((sum, t) => sum + (t.cost_actual || 0), 0) || 1;

      // Distribute deal revenue proportionally to task costs
      for (const task of tasks || []) {
        const contributionPercent = (task.cost_actual || 0) / totalTaskCost;
        const attributedRevenue = deal.value_usd * contributionPercent;
        const roi = attributedRevenue / (task.cost_actual || 0.01);

        const attribution: RevenueAttribution = {
          deal_id: deal.deal_id,
          agent_id: task.agent_id,
          task_id: task.id,
          revenue_attributed: attributedRevenue,
          cost_incurred: task.cost_actual,
          roi,
          attribution_date: new Date().toISOString(),
          contribution_percent: contributionPercent * 100,
        };

        // Store attribution
        const { error } = await this.supabase.from("revenue_attributions").insert([attribution]);
        if (error) throw error;

        attributions.push(attribution);
      }

      console.log(`✅ Attributed deal ${deal.deal_id} ($${deal.value_usd}) to ${attributions.length} agents`);
      attributions.forEach((attr) => {
        console.log(
          `   ${attr.agent_id}: $${attr.revenue_attributed.toFixed(2)} (${attr.contribution_percent.toFixed(1)}%, ROI: ${attr.roi.toFixed(2)}x)`
        );
      });

      return attributions;
    } catch (error) {
      console.error(`❌ Revenue attribution failed:`, error);
      throw error;
    }
  }

  /**
   * Get lifetime revenue attribution for an agent
   */
  async getAgentRevenueMetrics(agentId: string): Promise<{
    total_revenue_attributed: number;
    total_cost_incurred: number;
    lifetime_roi: number;
    deal_count: number;
    avg_deal_value: number;
  }> {
    try {
      const { data, error } = await this.supabase
        .from("revenue_attributions")
        .select("revenue_attributed, cost_incurred, deal_id")
        .eq("agent_id", agentId);

      if (error) throw error;

      const metrics = {
        total_revenue_attributed: 0,
        total_cost_incurred: 0,
        lifetime_roi: 0,
        deal_count: new Set<string>(),
        avg_deal_value: 0,
      };

      if (data && data.length > 0) {
        metrics.total_revenue_attributed = data.reduce((sum, attr) => sum + attr.revenue_attributed, 0);
        metrics.total_cost_incurred = data.reduce((sum, attr) => sum + attr.cost_incurred, 0);
        metrics.deal_count = new Set(data.map((attr) => attr.deal_id));
        metrics.lifetime_roi =
          metrics.total_cost_incurred > 0 ? metrics.total_revenue_attributed / metrics.total_cost_incurred : 0;
        metrics.avg_deal_value = metrics.total_revenue_attributed / (metrics.deal_count as any).size;
      }

      return {
        total_revenue_attributed: metrics.total_revenue_attributed,
        total_cost_incurred: metrics.total_cost_incurred,
        lifetime_roi: metrics.lifetime_roi,
        deal_count: (metrics.deal_count as any).size,
        avg_deal_value: metrics.avg_deal_value,
      };
    } catch (error) {
      console.error(`❌ Failed to fetch revenue metrics:`, error);
      throw error;
    }
  }

  /**
   * Validate attribution integrity (no double-counting)
   */
  async validateAttributionIntegrity(dealId: string): Promise<{
    is_valid: boolean;
    total_attributed: number;
    expected_value: number;
    variance_percent: number;
  }> {
    try {
      // Get deal value
      const { data: deals, error: dealError } = await this.supabase
        .from("deals")
        .select("value_usd")
        .eq("id", dealId)
        .single();

      if (dealError) throw dealError;

      // Sum all attributions
      const { data: attributions, error: attrError } = await this.supabase
        .from("revenue_attributions")
        .select("revenue_attributed")
        .eq("deal_id", dealId);

      if (attrError) throw attrError;

      const totalAttributed = attributions?.reduce((sum, attr) => sum + attr.revenue_attributed, 0) || 0;
      const variance = Math.abs((totalAttributed - deals.value_usd) / deals.value_usd);

      const isValid = variance < 0.01; // Allow 1% floating-point variance

      console.log(`🔍 Attribution integrity check for deal ${dealId}:`);
      console.log(`   Expected: $${deals.value_usd} | Attributed: $${totalAttributed.toFixed(2)} | Variance: ${(variance * 100).toFixed(2)}%`);
      console.log(`   Status: ${isValid ? "✅ VALID" : "❌ MISMATCH"}`);

      return {
        is_valid: isValid,
        total_attributed: totalAttributed,
        expected_value: deals.value_usd,
        variance_percent: variance * 100,
      };
    } catch (error) {
      console.error(`❌ Attribution validation failed:`, error);
      throw error;
    }
  }
}

export default RevenueAttributionBridge;
