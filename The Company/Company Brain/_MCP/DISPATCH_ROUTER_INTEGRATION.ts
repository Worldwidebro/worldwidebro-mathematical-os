/**
 * DISPATCH_ROUTER_INTEGRATION.ts
 *
 * Wires AgentDispatchRouter to Supabase realtime + MCP endpoint.
 * Handles event processing, autonomy gates, logging.
 *
 * Authority: CP-012 (Agent Control Plane)
 * Updated: 2026-09-18
 */

import { createClient } from "@supabase/supabase-js"
import { AgentDispatchRouter, AgentSuggestion, TaskClassification } from "./AGENT_DISPATCH_ROUTER"

// ============================================================
// TYPES
// ============================================================

export interface DispatchDecision {
  taskId: string
  taskText: string
  classifiedAs: TaskClassification
  suggestedAgent: string
  rank: number
  confidence: number
  autonomyLevel: "L1" | "L2" | "L3"
  costEstimate: number
  projectedRevenue: number
  requiresHumanReview: boolean
  timestamp: string
  status: "SUGGESTED" | "APPROVED" | "ESCALATED" | "EXECUTED" | "ERROR"
  errorMessage?: string
}

export interface DispatcherConfig {
  supabaseUrl: string
  supabaseKey: string
  tasksTable: string
  suggestionsTable: string
  logsTable: string
}

// ============================================================
// DISPATCH ROUTER INTEGRATION
// ============================================================

export class DispatcherIntegration {
  private router: AgentDispatchRouter
  private supabase: any
  private config: DispatcherConfig
  private isListening: boolean = false

  constructor(router: AgentDispatchRouter, config: DispatcherConfig) {
    this.router = router
    this.config = config
    this.supabase = createClient(config.supabaseUrl, config.supabaseKey)
  }

  /**
   * PHASE 2.2a: Start realtime listening on task_queue
   */
  async startRealtimeListener(): Promise<void> {
    if (this.isListening) return

    this.supabase
      .channel("dispatch-tasks")
      .on(
        "postgres_changes",
        {
          event: "INSERT",
          schema: "public",
          table: this.config.tasksTable,
        },
        (payload: any) => {
          this.processTask(payload.new)
        }
      )
      .subscribe()

    this.isListening = true
    console.log("[Dispatcher] Realtime listener started on", this.config.tasksTable)
  }

  /**
   * PHASE 2.2a: Process incoming task
   */
  private async processTask(taskRecord: any): Promise<void> {
    const { id: taskId, task_text: taskText, created_at } = taskRecord

    try {
      // 1. Classify task
      const classification = this.router.classifyTask(taskText)

      // 2. Suggest agent
      const suggestion = this.router.suggestAgent(taskText)

      // 3. Enforce autonomy gate
      const gateDecision = this.enforceAutonomyGate(suggestion)

      // 4. Store suggestion
      const decision: DispatchDecision = {
        taskId,
        taskText,
        classifiedAs: classification,
        suggestedAgent: suggestion.topAgent.name,
        rank: suggestion.topAgent.rankPosition,
        confidence: suggestion.confidence,
        autonomyLevel: gateDecision.autonomyLevel,
        costEstimate: suggestion.costEstimate,
        projectedRevenue: suggestion.revenueProjection,
        requiresHumanReview: gateDecision.requiresHumanReview,
        timestamp: new Date().toISOString(),
        status: gateDecision.requiresHumanReview ? "SUGGESTED" : "APPROVED",
      }

      // 5. Insert into suggestions table
      await this.supabase.from(this.config.suggestionsTable).insert({
        task_id: taskId,
        suggested_agent: suggestion.topAgent.name,
        rank: 1,
        confidence: suggestion.confidence,
        cost: suggestion.costEstimate,
        projected_revenue: suggestion.revenueProjection,
        autonomy_level: gateDecision.autonomyLevel,
        requires_human_review: gateDecision.requiresHumanReview,
        decision_json: decision,
        created_at: new Date().toISOString(),
      })

      // 6. Log decision
      await this.logDispatchDecision(decision)
    } catch (error) {
      console.error("[Dispatcher] Error processing task", taskId, error)
      await this.logDispatchError(taskId, taskText, error as Error)
    }
  }

  /**
   * PHASE 2.2c: Enforce autonomy gates
   */
  private enforceAutonomyGate(suggestion: AgentSuggestion): { autonomyLevel: "L1" | "L2" | "L3"; requiresHumanReview: boolean } {
    const agent = suggestion.topAgent
    let autonomyLevel = agent.autonomyLevel
    let requiresHumanReview = false

    // L1: Always human review
    if (autonomyLevel === "L1") {
      requiresHumanReview = true
    }

    // L2: Human review for high-cost tasks
    if (autonomyLevel === "L2" && suggestion.costEstimate > 100) {
      requiresHumanReview = true
    }

    // L3: Escalate if cost/revenue threshold exceeded
    if (autonomyLevel === "L3" && suggestion.costEstimate > 1000) {
      autonomyLevel = "L1"
      requiresHumanReview = true
    }

    // Override: Don't let payment agents run autonomously on large amounts
    if (agent.name.includes("Payment") && suggestion.costEstimate > 10000) {
      autonomyLevel = "L1"
      requiresHumanReview = true
    }

    return { autonomyLevel, requiresHumanReview }
  }

  /**
   * PHASE 2.2b: MCP endpoint handler
   */
  async handleDispatchRequest(taskId: string): Promise<any> {
    const startTime = Date.now()

    try {
      // Fetch task from DB
      const { data: taskRecord, error } = await this.supabase
        .from(this.config.tasksTable)
        .select("*")
        .eq("id", taskId)
        .single()

      if (error) throw error

      // Process through router
      const classification = this.router.classifyTask(taskRecord.task_text)
      const suggestion = this.router.suggestAgent(taskRecord.task_text)
      const gateDecision = this.enforceAutonomyGate(suggestion)

      const latency = Date.now() - startTime

      // Response
      return {
        success: true,
        taskId,
        agents: [
          {
            name: suggestion.topAgent.name,
            rank: 1,
            confidence: suggestion.confidence,
            autonomy: gateDecision.autonomyLevel,
            cost: `$${suggestion.costEstimate}`,
            projectedRevenue: `$${suggestion.revenueProjection}`,
          },
          ...suggestion.alternatives.slice(0, 2).map((alt, i) => ({
            name: alt.name,
            rank: i + 2,
            confidence: alt.finalScore,
            autonomy: alt.autonomyLevel,
            cost: `$${alt.costPerUse * 10}`,
          })),
        ],
        classification: {
          domain: classification.domain,
          logicLayers: classification.logicLayers,
          complexity: classification.complexity,
        },
        latencyMs: latency,
      }
    } catch (error) {
      return {
        success: false,
        taskId,
        error: (error as Error).message,
        latencyMs: Date.now() - startTime,
      }
    }
  }

  /**
   * PHASE 2.2d: Log dispatch decision
   */
  private async logDispatchDecision(decision: DispatchDecision): Promise<void> {
    try {
      await this.supabase.from(this.config.logsTable).insert({
        task_id: decision.taskId,
        task_text: decision.taskText,
        classified_as: JSON.stringify(decision.classifiedAs),
        suggested_agent: decision.suggestedAgent,
        confidence: decision.confidence,
        autonomy_level: decision.autonomyLevel,
        cost: decision.costEstimate,
        projected_revenue: decision.projectedRevenue,
        status: decision.status,
        created_at: new Date().toISOString(),
      })
    } catch (error) {
      console.error("[Dispatcher] Failed to log decision", error)
    }
  }

  /**
   * PHASE 2.2d: Log dispatch error
   */
  private async logDispatchError(taskId: string, taskText: string, error: Error): Promise<void> {
    try {
      await this.supabase.from(this.config.logsTable).insert({
        task_id: taskId,
        task_text: taskText,
        status: "ERROR",
        error_message: error.message,
        created_at: new Date().toISOString(),
      })
    } catch (err) {
      console.error("[Dispatcher] Failed to log error", err)
    }
  }

  /**
   * Stop realtime listener
   */
  async stop(): Promise<void> {
    await this.supabase.channel("dispatch-tasks").unsubscribe()
    this.isListening = false
  }
}

// ============================================================
// SUPABASE SCHEMA MIGRATION
// ============================================================

export const SCHEMA_MIGRATION = `
-- Create task_queue table if not exists
CREATE TABLE IF NOT EXISTS public.task_queue (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  task_text TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Create suggestions table if not exists
CREATE TABLE IF NOT EXISTS public.suggestions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  task_id UUID REFERENCES task_queue(id),
  suggested_agent TEXT NOT NULL,
  rank INTEGER,
  confidence REAL,
  cost INTEGER,
  projected_revenue INTEGER,
  autonomy_level TEXT CHECK (autonomy_level IN ('L1', 'L2', 'L3')),
  requires_human_review BOOLEAN DEFAULT false,
  decision_json JSONB,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Create dispatch_logs table if not exists
CREATE TABLE IF NOT EXISTS public.dispatch_logs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  task_id UUID REFERENCES task_queue(id),
  task_text TEXT,
  classified_as JSONB,
  suggested_agent TEXT,
  confidence REAL,
  autonomy_level TEXT,
  cost INTEGER,
  projected_revenue INTEGER,
  status TEXT,
  error_message TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Indexes for performance
CREATE INDEX IF NOT EXISTS idx_task_queue_created ON public.task_queue(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_suggestions_task_id ON public.suggestions(task_id);
CREATE INDEX IF NOT EXISTS idx_dispatch_logs_task_id ON public.dispatch_logs(task_id);
CREATE INDEX IF NOT EXISTS idx_dispatch_logs_created ON public.dispatch_logs(created_at DESC);
`

// ============================================================
// MCP ENDPOINT DEFINITION
// ============================================================

export const MCP_ENDPOINT = {
  name: "/dispatch",
  method: "POST",
  description: "Route a task to the best agent and get a suggestion",
  schema: {
    request: {
      type: "object",
      properties: {
        task_id: { type: "string", description: "UUID of task in task_queue" },
      },
      required: ["task_id"],
    },
    response: {
      type: "object",
      properties: {
        success: { type: "boolean" },
        taskId: { type: "string" },
        agents: {
          type: "array",
          items: {
            type: "object",
            properties: {
              name: { type: "string" },
              rank: { type: "number" },
              confidence: { type: "number" },
              autonomy: { type: "string", enum: ["L1", "L2", "L3"] },
              cost: { type: "string" },
              projectedRevenue: { type: "string" },
            },
          },
        },
        classification: { type: "object" },
        latencyMs: { type: "number" },
      },
    },
  },
  examples: [
    {
      request: { task_id: "550e8400-e29b-41d4-a716-446655440000" },
      response: {
        success: true,
        taskId: "550e8400-e29b-41d4-a716-446655440000",
        agents: [
          {
            name: "Cold Email Writer",
            rank: 1,
            confidence: 0.92,
            autonomy: "L2",
            cost: "$25",
            projectedRevenue: "$10000",
          },
        ],
        classification: {
          domain: "30-REVENUE",
          logicLayers: ["LOGIC-019", "LOGIC-049"],
          complexity: "MEDIUM",
        },
        latencyMs: 45,
      },
    },
  ],
}
