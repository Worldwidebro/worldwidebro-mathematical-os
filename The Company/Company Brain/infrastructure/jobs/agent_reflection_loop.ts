/**
 * Agent Reflection Loop Job
 * Analyzes past agent decisions, updates trait confidence via Bayesian scoring
 * Decays old memories (>30 days) to prevent stale learning
 * Writes learning results to Neo4j for continuous improvement
 */

import { CronJob } from "trigger.dev";
import { MemoryClient } from "../agents/memory_config";
import { AgentMemoryClientWrapper } from "../agents/agent_memory_client";
import { TraitMemory } from "../agents/trait_memory";

interface AgentDecision {
  decision_id: string;
  agent_id: string;
  entity_id: string;
  category: string;
  decision: string;
  confidence: number;
  outcome: "success" | "failure" | "unknown";
  timestamp: Date;
  reasoning_trace_id: string;
}

export const agentReflectionLoop = CronJob.schedule(
  "agent-reflection-loop",
  {
    cron: "0 19 * * *", // 7 PM UTC daily
  },
  async (payload) => {
    console.log("[agentReflectionLoop] Job started");

    const memoryClient = new MemoryClient({
      uri: process.env.NEO4J_URI || "bolt://localhost:7687",
      password: process.env.NEO4J_PASSWORD || "changeme",
    });

    const memoryWrapper = new AgentMemoryClientWrapper(memoryClient);
    const traitMemory = new TraitMemory(memoryClient);

    try {
      // Fetch all agent decisions from last 24h
      const decisions = await fetchRecentDecisions(memoryClient);
      console.log(`[agentReflectionLoop] Analyzing ${decisions.length} decisions`);

      let reinforced = 0;
      let decayed = 0;
      let confidenceUpdates = 0;

      // Analyze outcomes and update traits (max 1000 iterations)
      for (let i = 0; i < Math.min(decisions.length, 1000); i++) {
        const decision = decisions[i];

        // Update trait confidence based on outcome (Bayesian approach)
        if (decision.outcome !== "unknown") {
          const correct = decision.outcome === "success";

          try {
            // Reinforce or penalize the trait
            const updated = await traitMemory.reinforce_trait(
              decision.entity_id,
              decision.category,
              correct
            );

            if (updated) {
              reinforced++;
              confidenceUpdates++;

              console.log(
                `[agentReflectionLoop] Updated trait: ${decision.entity_id}.${decision.category} confidence=${updated.current_confidence.toFixed(2)}`
              );
            }
          } catch (error) {
            console.warn(
              `[agentReflectionLoop] Failed to reinforce trait:`,
              error
            );
          }
        }

        // Check for old memories to decay (>30 days)
        const daysSinceDecision = Math.floor(
          (Date.now() - decision.timestamp.getTime()) / (1000 * 60 * 60 * 24)
        );

        if (daysSinceDecision > 30) {
          try {
            const trait = await traitMemory.get_trait(
              decision.entity_id,
              decision.category
            );

            if (trait) {
              trait.decay(daysSinceDecision);
              decayed++;

              console.log(
                `[agentReflectionLoop] Decayed old trait: ${decision.entity_id}.${decision.category} (${daysSinceDecision} days old)`
              );
            }
          } catch (error) {
            console.warn(`[agentReflectionLoop] Failed to decay trait:`, error);
          }
        }

        // Log meta-learning outcome to Neo4j reasoning memory
        await memoryClient.add_reasoning_trace(
          agent_id: "AGT-META-001", // Meta-learning agent
          session_id: `reflection-loop-${i}`,
          decision: `analyze_decision_outcome_${decision.decision_id}`,
          reasoning: `Evaluated decision for ${decision.entity_id} on ${decision.category}. Outcome: ${decision.outcome}. Updated confidence accordingly.`,
          confidence: 0.9,
          outcome: "learning_updated",
        );
      }

      // Cleanup: delete stale memories (>90 days)
      const staleCount = await cleanupStaleMemories(memoryClient);

      console.log(
        `[agentReflectionLoop] Complete: reinforced=${reinforced}, decayed=${decayed}, stale_removed=${staleCount}`
      );

      return {
        status: "success",
        decisions_analyzed: Math.min(decisions.length, 1000),
        traits_reinforced: reinforced,
        traits_decayed: decayed,
        stale_memories_removed: staleCount,
        confidence_updates: confidenceUpdates,
        execution_time_ms: Date.now(),
      };
    } catch (error) {
      console.error("[agentReflectionLoop] Error:", error);
      throw error;
    } finally {
      await memoryClient.close();
    }
  }
);

/**
 * Fetch agent decisions from last 24 hours from Neo4j reasoning memory
 */
async function fetchRecentDecisions(
  memoryClient: MemoryClient
): Promise<AgentDecision[]> {
  const query = `
    MATCH (r:ReasoningTrace)
    WHERE r.timestamp > datetime() - duration('PT24H')
    RETURN r.id as decision_id,
           r.agent_id as agent_id,
           r.entity_id as entity_id,
           r.category as category,
           r.decision as decision,
           r.confidence as confidence,
           r.outcome as outcome,
           r.timestamp as timestamp,
           r.id as reasoning_trace_id
    ORDER BY r.timestamp DESC
    LIMIT 500
  `;

  const session = memoryClient.driver.session();
  const results: AgentDecision[] = [];

  try {
    const result = await session.run(query);
    result.records.forEach((record) => {
      const outcome = record.get("outcome");
      results.push({
        decision_id: record.get("decision_id"),
        agent_id: record.get("agent_id"),
        entity_id: record.get("entity_id"),
        category: record.get("category"),
        decision: record.get("decision"),
        confidence: parseFloat(record.get("confidence") || "0.5"),
        outcome: (
          ["success", "failure", "unknown"].includes(outcome)
            ? outcome
            : "unknown"
        ) as "success" | "failure" | "unknown",
        timestamp: new Date(record.get("timestamp")),
        reasoning_trace_id: record.get("reasoning_trace_id"),
      });
    });
  } finally {
    await session.close();
  }

  return results;
}

/**
 * Remove stale reasoning traces older than 90 days
 * Keeps learning loop memory bounded
 */
async function cleanupStaleMemories(
  memoryClient: MemoryClient
): Promise<number> {
  const deleteQuery = `
    MATCH (r:ReasoningTrace)
    WHERE r.timestamp < datetime() - duration('P90D')
    DETACH DELETE r
    RETURN count(*) as deleted
  `;

  const session = memoryClient.driver.session();

  try {
    const result = await session.run(deleteQuery);
    const record = result.records[0];
    return record ? parseInt(record.get("deleted")) : 0;
  } finally {
    await session.close();
  }
}
