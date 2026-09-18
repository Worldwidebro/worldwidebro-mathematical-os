/**
 * Orchestrator Prime (AGT-001)
 * Routes tasks to the best agent from the 318-agent inventory via OmniRoute
 *
 * Architecture:
 * 1. Load agents from AGENTS_INVENTORY_318.yaml
 * 2. Classify incoming task (intent, capabilities needed)
 * 3. Find best agent match
 * 4. Execute via OmniRoute
 * 5. Track execution + attribute revenue
 */

import { createClient } from "@supabase/supabase-js";
import YAML from "yaml";
import fs from "fs";
import path from "path";

// ============================================================
// TYPES
// ============================================================

interface Agent {
  id: string;
  name: string;
  file: string;
  domain: string;
  category: string;
  description: string;
  deployed: boolean;
  autonomy_level: "L1" | "L2" | "L3";
  status: "READY" | "BUILDING" | "ARCHIVED";
  capabilities?: string[];
  cost_per_invocation?: number;
  estimated_revenue?: number;
}

interface Task {
  id?: string;
  description: string;
  venture: string;
  urgency?: "high" | "medium" | "low";
  budget?: number;
  revenue_target?: number;
}

interface TaskClassification {
  intent: string;
  logic_layers: string[];
  required_capabilities: string[];
  autonomy_suggested: "L1" | "L2" | "L3";
}

interface MatchResult {
  agent_id: string;
  agent_name: string;
  confidence_score: number; // 0-100
  cost: number;
  estimated_revenue: number;
  rationale: string;
}

interface TaskExecution {
  task_id: string;
  agent_id: string;
  status: "queued" | "in_progress" | "completed" | "failed";
  cost_estimated: number;
  cost_actual?: number;
  revenue_estimated: number;
  revenue_actual?: number;
  outcome?: Record<string, any>;
  error?: string;
  created_at: Date;
  completed_at?: Date;
}

// ============================================================
// ORCHESTRATOR PRIME CLASS
// ============================================================

export class OrchestratorPrime {
  private supabase;
  private agents: Agent[] = [];
  private agentsLoaded = false;

  constructor(
    supabaseUrl: string = process.env.SUPABASE_URL || "https://aipehhzlsmfxxzwceppd.supabase.co",
    supabaseKey: string = process.env.SUPABASE_ANON_KEY || ""
  ) {
    this.supabase = createClient(supabaseUrl, supabaseKey);
  }

  // ============================================================
  // PHASE 1: AGENT DISCOVERY
  // ============================================================

  /**
   * Load all 318 agents from AGENTS_INVENTORY_318.yaml
   */
  async loadAgents(): Promise<Agent[]> {
    try {
      // Try to load from file (local development)
      const filePath = path.join(
        process.cwd(),
        "_REGISTRIES/CANONICAL/AGENTS_INVENTORY_318.yaml"
      );

      if (fs.existsSync(filePath)) {
        const content = fs.readFileSync(filePath, "utf-8");
        const data = YAML.parse(content);
        this.agents = data.agents_inventory?.agents || [];
        this.agentsLoaded = true;
        console.log(`✅ Loaded ${this.agents.length} agents from file`);
        return this.agents;
      }

      // Fallback: load from Supabase registry table (if it exists)
      const { data, error } = await this.supabase
        .from("agent_registry")
        .select("*");

      if (error) {
        console.warn("⚠️  Could not load agents from Supabase:", error);
        return [];
      }

      this.agents = data || [];
      this.agentsLoaded = true;
      console.log(`✅ Loaded ${this.agents.length} agents from Supabase`);
      return this.agents;
    } catch (error) {
      console.error("❌ Failed to load agents:", error);
      return [];
    }
  }

  /**
   * Get all agents by category
   */
  getAgentsByCategory(category: string): Agent[] {
    return this.agents.filter((a) => a.category === category);
  }

  /**
   * Get all READY agents (deployed or ready to deploy)
   */
  getReadyAgents(): Agent[] {
    return this.agents.filter((a) => a.status === "READY");
  }

  /**
   * Search agents by name or description
   */
  searchAgents(query: string): Agent[] {
    const q = query.toLowerCase();
    return this.agents.filter(
      (a) =>
        a.name.toLowerCase().includes(q) ||
        a.description.toLowerCase().includes(q) ||
        (a.capabilities?.some((c) => c.toLowerCase().includes(q)) ?? false)
    );
  }

  // ============================================================
  // PHASE 2: TASK CLASSIFICATION (Placeholder)
  // ============================================================

  /**
   * Classify task to extract intent and required capabilities
   * TODO: Wire to Claude Haiku for intelligent classification
   */
  private async classifyTask(task: Task): Promise<TaskClassification> {
    // TODO: Call Claude API to classify task
    // For now, return a basic classification based on keywords

    const description = task.description.toLowerCase();
    let intent = "general";
    let capabilities: string[] = [];

    if (
      description.includes("email") ||
      description.includes("send") ||
      description.includes("outreach")
    ) {
      intent = "outreach";
      capabilities = ["write-emails", "personalize", "track-opens"];
    } else if (
      description.includes("call") ||
      description.includes("phone") ||
      description.includes("prospect")
    ) {
      intent = "sales";
      capabilities = ["cold-calling", "track-calls", "schedule-demos"];
    } else if (description.includes("book") || description.includes("demo")) {
      intent = "booking";
      capabilities = ["schedule-meetings", "send-confirmations"];
    }

    return {
      intent,
      logic_layers: [],
      required_capabilities: capabilities,
      autonomy_suggested: "L2",
    };
  }

  // ============================================================
  // PHASE 3: AGENT MATCHING
  // ============================================================

  /**
   * Find the best agent(s) for a task
   */
  async findBestAgent(task: Task): Promise<MatchResult[]> {
    if (!this.agentsLoaded) {
      await this.loadAgents();
    }

    const classification = await this.classifyTask(task);
    const readyAgents = this.getReadyAgents();

    // Score each agent
    const scored = readyAgents
      .map((agent) => {
        let score = 0;

        // Match by category (e.g., "sales" task → sales agent)
        if (classification.intent === agent.category) {
          score += 40;
        }

        // Match by description keywords
        const descLower = agent.description.toLowerCase();
        classification.required_capabilities.forEach((cap) => {
          if (descLower.includes(cap)) {
            score += 20;
          }
        });

        // Autonomy level match
        if (agent.autonomy_level === classification.autonomy_suggested) {
          score += 10;
        }

        // Cost efficiency (prefer lower cost)
        if (agent.cost_per_invocation && agent.estimated_revenue) {
          const roi = agent.estimated_revenue / agent.cost_per_invocation;
          if (roi > 100) score += 10; // Excellent ROI
          else if (roi > 10) score += 5; // Good ROI
        }

        return {
          agent_id: agent.id,
          agent_name: agent.name,
          confidence_score: Math.min(score, 100),
          cost: agent.cost_per_invocation || 0,
          estimated_revenue: agent.estimated_revenue || 0,
          rationale: `Matches ${classification.intent} + [${classification.required_capabilities.join(", ")}]`,
        };
      })
      .filter((m) => m.confidence_score > 0)
      .sort((a, b) => b.confidence_score - a.confidence_score)
      .slice(0, 3); // Return top 3

    return scored;
  }

  // ============================================================
  // PHASE 4: EXECUTION (Placeholder)
  // ============================================================

  /**
   * Execute a task by invoking the selected agent
   * TODO: Wire to OmniRoute for actual execution
   */
  async executeTask(task: Task, agent: MatchResult): Promise<TaskExecution> {
    const taskId = task.id || `TASK-${Date.now()}`;
    task.id = taskId;

    // Create execution record
    const execution: TaskExecution = {
      task_id: taskId,
      agent_id: agent.agent_id,
      status: "in_progress",
      cost_estimated: agent.cost,
      revenue_estimated: agent.estimated_revenue,
      created_at: new Date(),
    };

    // Store in Supabase
    try {
      await this.supabase.from("task_executions").insert({
        task_id: taskId,
        agent_id: agent.agent_id,
        venture_id: task.venture,
        status: "queued",
        cost_estimated: agent.cost,
        revenue_estimated: agent.estimated_revenue,
        task_description: task.description,
        created_at: new Date().toISOString(),
      });
    } catch (error) {
      console.error("Failed to record execution:", error);
    }

    // TODO: Call OmniRoute API to invoke agent
    // const result = await omniroute.invoke({
    //   agent_id: agent.agent_id,
    //   task: task.description,
    //   context: { venture: task.venture, budget: task.budget }
    // });

    console.log(`✅ Task ${taskId} queued for agent ${agent.agent_name}`);
    return execution;
  }

  // ============================================================
  // PHASE 5: REVENUE ATTRIBUTION (Placeholder)
  // ============================================================

  /**
   * Record revenue attribution for a completed task
   */
  async attributeRevenue(
    taskId: string,
    revenue: number,
    actualCost: number = 0
  ): Promise<void> {
    try {
      // Get execution record
      const { data: execution, error } = await this.supabase
        .from("task_executions")
        .select("*")
        .eq("task_id", taskId)
        .single();

      if (error || !execution) {
        console.error("Task execution not found:", taskId);
        return;
      }

      // Record revenue
      const roi = actualCost > 0 ? revenue / actualCost : 0;
      await this.supabase.from("revenue_log").insert({
        task_id: taskId,
        agent_id: execution.agent_id,
        venture_id: execution.venture_id,
        revenue,
        cost: actualCost || execution.cost_estimated,
        roi,
        recorded_at: new Date().toISOString(),
      });

      // Update execution record
      await this.supabase
        .from("task_executions")
        .update({
          status: "completed",
          revenue_actual: revenue,
          cost_actual: actualCost || execution.cost_estimated,
          completed_at: new Date().toISOString(),
        })
        .eq("task_id", taskId);

      console.log(`✅ Revenue attributed: $${revenue} (ROI: ${roi.toFixed(2)}x)`);
    } catch (error) {
      console.error("Failed to attribute revenue:", error);
    }
  }

  // ============================================================
  // PUBLIC API
  // ============================================================

  /**
   * Main entry point: Route a task to the best agent
   */
  async orchestrate(task: Task): Promise<{
    task_id: string;
    suggested_agents: MatchResult[];
    status: string;
  }> {
    if (!this.agentsLoaded) {
      await this.loadAgents();
    }

    console.log(`\n📋 Orchestrating task: "${task.description.substring(0, 50)}..."`);

    // Find best agents
    const agents = await this.findBestAgent(task);

    if (agents.length === 0) {
      console.warn("⚠️  No suitable agents found");
      return {
        task_id: task.id || `TASK-${Date.now()}`,
        suggested_agents: [],
        status: "no_agents_found",
      };
    }

    console.log(
      `\n✅ Found ${agents.length} agent(s):`
    );
    agents.forEach((a, i) => {
      console.log(
        `   ${i + 1}. ${a.agent_name} (${a.confidence_score}% confidence, $${a.estimated_revenue} revenue)`
      );
    });

    // Execute with top agent
    await this.executeTask(task, agents[0]);

    return {
      task_id: task.id || `TASK-${Date.now()}`,
      suggested_agents: agents,
      status: "queued",
    };
  }
}

// ============================================================
// EXPORT
// ============================================================

export default OrchestratorPrime;
