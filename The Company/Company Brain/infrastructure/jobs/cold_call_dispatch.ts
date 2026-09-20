/**
 * Cold Call Dispatch Job
 * Generates call scripts, routes to sales orchestrator, tracks outcomes
 * Writes results to shared Neo4j + Supabase for VEX visibility
 */

import { CronJob } from "trigger.dev";
import { createClient } from "@supabase/supabase-js";
import { MemoryClient } from "../agents/memory_config";
import { AgentMemoryClientWrapper } from "../agents/agent_memory_client";
import { AgentDispatchRouter } from "../agents/agent_orchestrator";
import Anthropic from "@anthropic-ai/sdk";

interface CallProspect {
  prospect_id: string;
  name: string;
  company: string;
  email: string;
  phone: string;
  segment: string;
  last_contacted?: Date;
}

export const coldCallDispatch = CronJob.schedule(
  "cold-call-dispatch",
  {
    cron: "0 8,12,15 * * *", // 8 AM, 12 PM, 3 PM UTC daily
  },
  async (payload) => {
    console.log("[coldCallDispatch] Job started");

    const memoryClient = new MemoryClient({
      uri: process.env.NEO4J_URI || "bolt://localhost:7687",
      password: process.env.NEO4J_PASSWORD || "changeme",
    });

    const supabase = createClient(
      process.env.SUPABASE_URL!,
      process.env.SUPABASE_KEY!
    );

    const memoryWrapper = new AgentMemoryClientWrapper(memoryClient);
    const orchestrator = new AgentDispatchRouter(memoryClient);
    const anthropic = new Anthropic();

    try {
      // Load prospects from Neo4j + Supabase
      const prospects = await loadProspects(memoryClient, supabase);
      console.log(`[coldCallDispatch] Loaded ${prospects.length} prospects`);

      let dispatched = 0;
      let scriptErrors = 0;

      // Dispatch to sales orchestrator (max 100 iterations)
      for (let i = 0; i < Math.min(prospects.length, 100); i++) {
        const prospect = prospects[i];

        try {
          // Generate call script via Claude
          const scriptResponse = await anthropic.messages.create({
            model: "claude-3-5-haiku-20241022",
            max_tokens: 300,
            messages: [
              {
                role: "user",
                content: `Generate a 30-second cold call opener for: ${prospect.name} at ${prospect.company} (segment: ${prospect.segment}). Be direct, value-focused, no fluff. Output only the script.`,
              },
            ],
          });

          const callScript =
            scriptResponse.content[0].type === "text"
              ? scriptResponse.content[0].text
              : "";

          // Route to sales orchestrator
          const routeResult = await orchestrator.routeTask({
            agent_id: "AGT-F001", // Sales Orchestrator
            task_type: "cold_call_dispatch",
            context: {
              prospect_id: prospect.prospect_id,
              name: prospect.name,
              company: prospect.company,
              phone: prospect.phone,
              segment: prospect.segment,
              call_script: callScript,
              scheduled_time: new Date(
                Date.now() + Math.random() * 3600000
              ).toISOString(), // Within next hour
            },
          });

          // Write to shared Supabase (for VEX to display)
          const { error: dbError } = await supabase.from("calls").insert({
            prospect_id: prospect.prospect_id,
            name: prospect.name,
            company: prospect.company,
            script: callScript,
            status: "dispatched",
            scheduled_at: new Date().toISOString(),
            segment: prospect.segment,
          });

          if (dbError) {
            console.warn(
              `[coldCallDispatch] DB insert failed: ${dbError.message}`
            );
            scriptErrors++;
            continue;
          }

          // Log to Neo4j reasoning memory
          await memoryWrapper.log_decision(
            `job-cold-call-${i}`,
            `dispatch_call_${prospect.prospect_id}`,
            `Generated script for ${prospect.name} at ${prospect.company}`,
            0.8,
            "dispatched"
          );

          dispatched++;
        } catch (error) {
          console.error(
            `[coldCallDispatch] Script generation failed for ${prospect.prospect_id}:`,
            error
          );
          scriptErrors++;
        }
      }

      console.log(
        `[coldCallDispatch] Complete: dispatched=${dispatched}, errors=${scriptErrors}`
      );

      return {
        status: "success",
        prospects_loaded: prospects.length,
        calls_dispatched: dispatched,
        script_errors: scriptErrors,
        execution_time_ms: Date.now(),
      };
    } catch (error) {
      console.error("[coldCallDispatch] Error:", error);
      throw error;
    } finally {
      await memoryClient.close();
    }
  }
);

/**
 * Load prospects from Neo4j + Supabase
 * Prefers prospects not contacted in last 7 days
 */
async function loadProspects(
  memoryClient: MemoryClient,
  supabase: ReturnType<typeof createClient>
): Promise<CallProspect[]> {
  // Query Neo4j for high-value prospects
  const neoQuery = `
    MATCH (p:Prospect)
    WHERE p.segment IN ['high_intent', 'high_value']
    OPTIONAL MATCH (p)-[:LAST_CALLED]->(lc:CallEvent)
    WHERE lc.timestamp > datetime() - duration('P7D')
    WITH p, lc
    WHERE lc IS NULL
    RETURN p.id as prospect_id,
           p.name as name,
           p.company as company,
           p.email as email,
           p.phone as phone,
           p.segment as segment
    LIMIT 100
  `;

  const session = memoryClient.driver.session();
  const neoResults: CallProspect[] = [];

  try {
    const result = await session.run(neoQuery);
    result.records.forEach((record) => {
      neoResults.push({
        prospect_id: record.get("prospect_id"),
        name: record.get("name"),
        company: record.get("company"),
        email: record.get("email"),
        phone: record.get("phone"),
        segment: record.get("segment"),
      });
    });
  } finally {
    await session.close();
  }

  // Supplement from Supabase if needed
  if (neoResults.length < 50) {
    const { data: supabaseProspects, error } = await supabase
      .from("prospects")
      .select("*")
      .eq("status", "active")
      .gt("quality_score", 0.7)
      .limit(50 - neoResults.length);

    if (error) {
      console.warn(`[loadProspects] Supabase query failed: ${error.message}`);
    } else if (supabaseProspects) {
      supabaseProspects.forEach((prospect: any) => {
        neoResults.push({
          prospect_id: prospect.id,
          name: prospect.name,
          company: prospect.company,
          email: prospect.email,
          phone: prospect.phone,
          segment: prospect.segment || "standard",
          last_contacted: prospect.last_contacted
            ? new Date(prospect.last_contacted)
            : undefined,
        });
      });
    }
  }

  return neoResults;
}
