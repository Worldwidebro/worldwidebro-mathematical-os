/**
 * API Endpoint: POST /api/orchestrate
 * Routes incoming tasks to the best agent via Orchestrator Prime
 */

import type { NextApiRequest, NextApiResponse } from "next";
import OrchestratorPrime from "@/services/orchestrator-prime";

interface OrchestrationRequest {
  description: string;
  venture: string;
  urgency?: "high" | "medium" | "low";
  budget?: number;
  revenue_target?: number;
}

interface OrchestrationResponse {
  success: boolean;
  task_id: string;
  suggested_agents: Array<{
    agent_id: string;
    agent_name: string;
    confidence_score: number;
    cost: number;
    estimated_revenue: number;
    rationale: string;
  }>;
  status: string;
  error?: string;
}

const orchestrator = new OrchestratorPrime();

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse<OrchestrationResponse>
) {
  // Only allow POST
  if (req.method !== "POST") {
    return res.status(405).json({
      success: false,
      task_id: "",
      suggested_agents: [],
      status: "error",
      error: "Method not allowed. Use POST.",
    });
  }

  try {
    const body: OrchestrationRequest = req.body;

    // Validate required fields
    if (!body.description || !body.venture) {
      return res.status(400).json({
        success: false,
        task_id: "",
        suggested_agents: [],
        status: "error",
        error: "Missing required fields: description, venture",
      });
    }

    // Route task
    const result = await orchestrator.orchestrate({
      description: body.description,
      venture: body.venture,
      urgency: body.urgency,
      budget: body.budget,
      revenue_target: body.revenue_target,
    });

    // Return result
    return res.status(200).json({
      success: true,
      task_id: result.task_id,
      suggested_agents: result.suggested_agents,
      status: result.status,
    });
  } catch (error) {
    console.error("Orchestration error:", error);
    return res.status(500).json({
      success: false,
      task_id: "",
      suggested_agents: [],
      status: "error",
      error: error instanceof Error ? error.message : "Unknown error",
    });
  }
}
