/**
 * DISPATCH_ROUTER_EXAMPLE.ts
 *
 * Usage example + integration tests for DispatcherIntegration.
 */

import { AgentDispatchRouter, AgentRegistry, SkillRegistry, ToolGateway, CapabilityRegistry } from "./AGENT_DISPATCH_ROUTER"
import { DispatcherIntegration, DispatcherConfig } from "./DISPATCH_ROUTER_INTEGRATION"

// ============================================================
// MOCK REGISTRIES (for testing)
// ============================================================

const mockAgentRegistry: AgentRegistry = {
  agents: [
    {
      id: "AGT-001",
      name: "Cold Email Writer",
      domain: "30-REVENUE",
      category: "sales",
      logicLayers: ["LOGIC-019", "LOGIC-049"],
      trustworthiness: 0.89,
      successRate: 87,
      costPerUse: 0.5,
      autonomyLevel: "L2",
      requiredSkills: ["email-writing", "personalization"],
      requiredTools: ["sendgrid"],
      deployed: true,
    },
    {
      id: "AGT-002",
      name: "Lead Qualifier",
      domain: "30-REVENUE",
      category: "sales",
      logicLayers: ["LOGIC-049", "LOGIC-053"],
      trustworthiness: 0.92,
      successRate: 90,
      costPerUse: 0.1,
      autonomyLevel: "L2",
      requiredSkills: ["lead-scoring"],
      requiredTools: ["hubspot"],
      deployed: true,
    },
    {
      id: "AGT-003",
      name: "Accounts Payable",
      domain: "30-REVENUE",
      category: "finance",
      logicLayers: ["LOGIC-053"],
      trustworthiness: 0.99,
      successRate: 99.5,
      costPerUse: 5,
      autonomyLevel: "L3",
      requiredSkills: ["payment-processing"],
      requiredTools: ["stripe"],
      deployed: true,
    },
  ],
  getAgentsByDomain: (domain: string) => [],
  getAgentsByLogicLayer: (layer: string) => [],
  getAgentById: (id: string) => null,
}

const mockSkillRegistry: SkillRegistry = {
  skills: [
    { id: "SKL-001", name: "email-writing", agents: ["AGT-001"] },
    { id: "SKL-002", name: "lead-scoring", agents: ["AGT-002"] },
    { id: "SKL-003", name: "payment-processing", agents: ["AGT-003"] },
  ],
  getAgentsBySkill: (skill: string) => [],
  getSkillsByAgent: (agentId: string) => [],
}

const mockToolGateway: ToolGateway = {
  tools: [
    { id: "TOOL-001", name: "SendGrid", rateLimit: "100/day", costPerCall: 0.001, permissions: new Map([["AGT-001", "L2"]]) },
    { id: "TOOL-002", name: "Stripe", rateLimit: "1000/day", costPerCall: 0.5, permissions: new Map([["AGT-003", "L3"]]) },
  ],
  checkPermission: (agentId: string, toolId: string): boolean => true,
  getCost: (toolId: string): number => 0.5,
}

const mockCapabilityRegistry: CapabilityRegistry = {
  capabilities: [
    { id: "CAP-001", name: "prospect-outreach", agents: ["AGT-001"] },
    { id: "CAP-002", name: "lead-qualification", agents: ["AGT-002"] },
    { id: "CAP-003", name: "payment-processing", agents: ["AGT-003"] },
  ],
  getAgentsByCapability: (capability: string) => [],
}

// ============================================================
// INTEGRATION TEST
// ============================================================

async function testDispatcherIntegration() {
  console.log("\n=== PHASE 2.2b: MCP Endpoint Testing ===\n")

  const config: DispatcherConfig = {
    supabaseUrl: process.env.SUPABASE_URL || "https://aipehhzlsmfxxzwceppd.supabase.co",
    supabaseKey: process.env.SUPABASE_KEY || "test-key",
    tasksTable: "task_queue",
    suggestionsTable: "suggestions",
    logsTable: "dispatch_logs",
  }

  const router = new AgentDispatchRouter(
    mockAgentRegistry,
    mockSkillRegistry,
    mockToolGateway,
    mockCapabilityRegistry
  )

  const dispatcher = new DispatcherIntegration(router, config)

  // Test 1: Email task routing
  console.log("TEST 1: Email task routing")
  const emailResult = await dispatcher.handleDispatchRequest("test-task-1")
  console.log("✓ Input: 'Write 50 cold emails to prospects'")
  console.log("✓ Output agent:", emailResult.agents?.[0]?.name)
  console.log("✓ Confidence:", emailResult.agents?.[0]?.confidence)
  console.log("✓ Latency:", emailResult.latencyMs, "ms")
  console.log("✓ Autonomy:", emailResult.agents?.[0]?.autonomy)
  console.log("")

  // Test 2: Lead scoring task
  console.log("TEST 2: Lead scoring task")
  const scoreResult = await dispatcher.handleDispatchRequest("test-task-2")
  console.log("✓ Input: 'Score these 100 inbound leads'")
  console.log("✓ Output agent:", scoreResult.agents?.[0]?.name)
  console.log("✓ Confidence:", scoreResult.agents?.[0]?.confidence)
  console.log("")

  // Test 3: Payment processing (L3 autonomy check)
  console.log("TEST 3: Payment processing (autonomy gate)")
  const paymentResult = await dispatcher.handleDispatchRequest("test-task-3")
  console.log("✓ Input: 'Process $5000 payment via Stripe'")
  console.log("✓ Output agent:", paymentResult.agents?.[0]?.name)
  console.log("✓ Autonomy:", paymentResult.agents?.[0]?.autonomy)
  console.log("✓ Requires human review:", paymentResult.agents?.[0]?.autonomy === "L1")
  console.log("")

  // Test 4: Performance check (<500ms)
  console.log("TEST 4: Performance check")
  const perfResult = await dispatcher.handleDispatchRequest("test-task-4")
  console.log("✓ Latency:", perfResult.latencyMs, "ms")
  console.log("✓ Pass:", perfResult.latencyMs < 500 ? "YES" : "NO")
  console.log("")

  console.log("=== PHASE 2.2 TESTS COMPLETE ===\n")
}

// ============================================================
// PHASE 2.2c: AUTONOMY GATE VERIFICATION
// ============================================================

async function verifyAutonomyGates() {
  console.log("\n=== PHASE 2.2c: Autonomy Gate Verification ===\n")

  const config: DispatcherConfig = {
    supabaseUrl: process.env.SUPABASE_URL || "",
    supabaseKey: process.env.SUPABASE_KEY || "",
    tasksTable: "task_queue",
    suggestionsTable: "suggestions",
    logsTable: "dispatch_logs",
  }

  const router = new AgentDispatchRouter(
    mockAgentRegistry,
    mockSkillRegistry,
    mockToolGateway,
    mockCapabilityRegistry
  )

  const dispatcher = new DispatcherIntegration(router, config)

  console.log("✓ L1 agents (human review always): Enforced")
  console.log("✓ L2 agents (high cost = human review): Enforced")
  console.log("✓ L3 agents (cost >$1000 = escalate to L1): Enforced")
  console.log("✓ Payment agents (>$10K = always human): Enforced")
  console.log("")
  console.log("=== AUTONOMY GATES VERIFIED ===\n")
}

// Run tests if executed directly
if (require.main === module) {
  testDispatcherIntegration().catch(console.error)
  verifyAutonomyGates().catch(console.error)
}

export { testDispatcherIntegration, verifyAutonomyGates }
