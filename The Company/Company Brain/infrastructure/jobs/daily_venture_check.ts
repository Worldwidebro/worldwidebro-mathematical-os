/**
 * Daily Venture Check Job
 * Evaluates all ventures for readiness, escalates low-readiness to COO
 * Updates confidence scores based on outcomes
 */

import { CronJob } from "trigger.dev";
import { MemoryClient } from "../agents/memory_config";
import { AgentMemoryClientWrapper } from "../agents/agent_memory_client";
import { AgentDispatchRouter } from "../agents/agent_orchestrator";

interface VentureMetrics {
  venture_id: string;
  readiness_pct: number;
  cash_position: number;
  revenue_mtd: number;
  team_size: number;
  last_update: Date;
}

export const dailyVentureCheck = CronJob.schedule(
  "daily-venture-check",
  {
    cron: "0 9 * * *", // 9 AM UTC daily
  },
  async (payload) => {
    console.log("[dailyVentureCheck] Job started");

    const memoryClient = new MemoryClient({
      uri: process.env.NEO4J_URI || "bolt://localhost:7687",
      password: process.env.NEO4J_PASSWORD || "changeme",
    });

    const memoryWrapper = new AgentMemoryClientWrapper(memoryClient);
    const orchestrator = new AgentDispatchRouter(memoryClient);

    try {
      // Fetch all ventures from Neo4j
      const ventures = await fetchAllVentures(memoryClient);
      console.log(`[dailyVentureCheck] Fetched ${ventures.length} ventures`);

      let escalationCount = 0;
      let evaluatedCount = 0;

      // Evaluate each venture (max 50 iterations)
      for (let i = 0; i < Math.min(ventures.length, 50); i++) {
        const venture = ventures[i];
        evaluatedCount++;

        // Check readiness threshold
        if (venture.readiness_pct < 0.3) {
          console.log(
            `[dailyVentureCheck] ESCALATE: ${venture.venture_id} readiness=${venture.readiness_pct}`
          );

          // Create escalation context
          const escalationContext = {
            venture_id: venture.venture_id,
            readiness_pct: venture.readiness_pct,
            cash_position: venture.cash_position,
            revenue_mtd: venture.revenue_mtd,
            team_size: venture.team_size,
            reason: "Readiness below 30% threshold",
            timestamp: new Date().toISOString(),
          };

          // Route to COO via orchestrator
          await orchestrator.routeTask({
            agent_id: "AGT-E003", // COO
            task_type: "venture_readiness_alert",
            context: escalationContext,
          });

          escalationCount++;
        }

        // Log decision to reasoning memory
        const session = await memoryWrapper.get_session(`job-daily-check-${i}`);
        await memoryWrapper.log_decision(
          `job-daily-check-${i}`,
          `evaluate_readiness_${venture.venture_id}`,
          `Readiness: ${venture.readiness_pct}, Cash: ${venture.cash_position}`,
          venture.readiness_pct < 0.3 ? 0.95 : 0.7,
          venture.readiness_pct < 0.3 ? "escalated" : "monitored"
        );

        // Update confidence score in memory
        await memoryClient.add_preference(
          venture.venture_id,
          "readiness_trend",
          venture.readiness_pct < 0.3 ? "declining" : "stable",
          venture.readiness_pct < 0.3 ? 0.9 : 0.6
        );
      }

      console.log(
        `[dailyVentureCheck] Complete: evaluated=${evaluatedCount}, escalated=${escalationCount}`
      );

      return {
        status: "success",
        ventures_evaluated: evaluatedCount,
        ventures_escalated: escalationCount,
        execution_time_ms: Date.now(),
      };
    } catch (error) {
      console.error("[dailyVentureCheck] Error:", error);
      throw error;
    } finally {
      await memoryClient.close();
    }
  }
);

/**
 * Fetch all ventures from Neo4j graph
 * Uses context assembly pattern for efficient retrieval
 */
async function fetchAllVentures(
  memoryClient: MemoryClient
): Promise<VentureMetrics[]> {
  // Query Neo4j for all VENTURE nodes with metrics
  const query = `
    MATCH (v:Venture)
    OPTIONAL MATCH (v)-[:HAS_METRIC]->(m:Metric {type: 'readiness'})
    OPTIONAL MATCH (v)-[:HAS_CASH]->(c:CashPosition)
    OPTIONAL MATCH (v)-[:HAS_REVENUE]->(r:Revenue {period: 'mtd'})
    OPTIONAL MATCH (v)-[:HAS_TEAM]->(t:Team)
    RETURN v.id as venture_id,
           COALESCE(m.value, 0.0) as readiness_pct,
           COALESCE(c.amount, 0) as cash_position,
           COALESCE(r.amount, 0) as revenue_mtd,
           COALESCE(SIZE(t.members), 0) as team_size,
           COALESCE(m.updated_at, datetime()) as last_update
    LIMIT 100
  `;

  // Execute via memory client's Neo4j driver
  const session = memoryClient.driver.session();
  try {
    const result = await session.run(query);
    return result.records.map((record) => ({
      venture_id: record.get("venture_id"),
      readiness_pct: parseFloat(record.get("readiness_pct")),
      cash_position: parseFloat(record.get("cash_position")),
      revenue_mtd: parseFloat(record.get("revenue_mtd")),
      team_size: parseInt(record.get("team_size")),
      last_update: new Date(record.get("last_update")),
    }));
  } finally {
    await session.close();
  }
}
