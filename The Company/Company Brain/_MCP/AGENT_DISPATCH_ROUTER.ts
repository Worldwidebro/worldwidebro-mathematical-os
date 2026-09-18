/**
 * AGENT_DISPATCH_ROUTER.ts
 *
 * Core routing engine that classifies tasks and ranks agents.
 * Maps user intent → logic layers → candidate agents → ranked suggestions
 *
 * Authority: CP-012 (Agent Control Plane), CP-027 (Engineering)
 * Updated: 2026-09-18
 */

// ============================================================
// TYPE DEFINITIONS
// ============================================================

export interface TaskClassification {
  intent: string                      // "write emails", "score leads", "close deals"
  logicLayers: string[]              // ["LOGIC-019", "LOGIC-049"]
  domain: string                     // "30-REVENUE", "32-SECURITY", "34-PRODUCT"
  complexity: "LOW" | "MEDIUM" | "HIGH"
  estimatedCost: number              // USD
  estimatedRevenue: number           // USD
}

export interface Agent {
  id: string                         // "AGT-001"
  name: string                       // "Cold Email Writer"
  domain: string                     // "30-REVENUE"
  category: string                   // "sales"
  logicLayers: string[]              // what logic layers does this agent operate on
  trustworthiness: number            // 0-1, confidence in agent quality
  successRate: number                // 0-100, % of successful executions
  costPerUse: number                 // USD, average cost per task
  autonomyLevel: "L1" | "L2" | "L3" // L1: human review, L2: assisted, L3: autonomous
  requiredSkills: string[]           // ["email-writing", "personalization"]
  requiredTools: string[]            // ["sendgrid", "hubspot"]
  deployed: boolean                  // true if in production
}

export interface CandidateAgent extends Agent {
  relevanceScore: number             // 0-1, how well does this agent match?
}

export interface RankedAgent extends CandidateAgent {
  finalScore: number                 // 0-1, composite score for ranking
  rankPosition: number               // 1, 2, 3
  reasoning: string                  // why this agent is recommended
}

export interface GateDecision {
  approved: boolean
  autonomyLevel: "L1" | "L2" | "L3"
  requiresHumanReview: boolean
  reason: string
}

export interface AgentSuggestion {
  topAgent: RankedAgent
  alternatives: RankedAgent[]        // #2, #3, #4
  confidence: number                 // 0-1
  costEstimate: number               // USD
  revenueProjection: number          // USD
  gateDecision: GateDecision
  nextSteps: string[]
}

export interface AgentRegistry {
  agents: Agent[]
  getAgentsByDomain(domain: string): Agent[]
  getAgentsByLogicLayer(layer: string): Agent[]
  getAgentById(id: string): Agent | null
}

export interface SkillRegistry {
  skills: Array<{ id: string; name: string; agents: string[] }>
  getAgentsBySkill(skill: string): string[]
  getSkillsByAgent(agentId: string): string[]
}

export interface ToolGateway {
  tools: Array<{
    id: string
    name: string
    rateLimit: string
    costPerCall: number
    permissions: Map<string, "L1" | "L2" | "L3">
  }>
  checkPermission(agentId: string, toolId: string): boolean
  getCost(toolId: string): number
}

export interface CapabilityRegistry {
  capabilities: Array<{ id: string; name: string; agents: string[] }>
  getAgentsByCapability(capability: string): string[]
}

// ============================================================
// TASK CLASSIFICATION
// ============================================================

const LOGIC_LAYER_MAP = {
  "email": ["LOGIC-019", "LOGIC-049"],
  "call": ["LOGIC-049", "LOGIC-053"],
  "security": ["LOGIC-014", "LOGIC-027"],
  "analyze": ["LOGIC-049", "LOGIC-053"],
  "write": ["LOGIC-019", "LOGIC-049"],
  "close": ["LOGIC-053", "LOGIC-060"],
  "qualify": ["LOGIC-049", "LOGIC-053"],
  "score": ["LOGIC-049", "LOGIC-053"],
  "audit": ["LOGIC-014", "LOGIC-027"],
  "forecast": ["LOGIC-049", "LOGIC-053"],
}

const DOMAIN_MAP = {
  "email": "30-REVENUE",
  "sales": "30-REVENUE",
  "lead": "30-REVENUE",
  "security": "32-SECURITY",
  "data": "16-AGENTS",
  "product": "34-PRODUCT",
  "design": "34-PRODUCT",
  "engineering": "16-AGENTS",
  "infrastructure": "27-INFRASTRUCTURE",
  "marketing": "30-REVENUE",
  "customer": "30-REVENUE",
}

// ============================================================
// AGENT DISPATCH ROUTER CLASS
// ============================================================

export class AgentDispatchRouter {
  private agentRegistry: AgentRegistry
  private skillRegistry: SkillRegistry
  private toolGateway: ToolGateway
  private capabilityRegistry: CapabilityRegistry
  private decisionLog: Array<{ task: string; suggestion: AgentSuggestion; timestamp: Date }>

  constructor(
    agentRegistry: AgentRegistry,
    skillRegistry: SkillRegistry,
    toolGateway: ToolGateway,
    capabilityRegistry: CapabilityRegistry
  ) {
    this.agentRegistry = agentRegistry
    this.skillRegistry = skillRegistry
    this.toolGateway = toolGateway
    this.capabilityRegistry = capabilityRegistry
    this.decisionLog = []
  }

  /**
   * PHASE 2.1b: Classify task into intent, logic layers, domain, complexity
   */
  classifyTask(task: string): TaskClassification {
    const lowerTask = task.toLowerCase()

    // Extract intent from keywords
    let intent = ""
    let logicLayers: string[] = []
    let domain = "30-REVENUE" // default
    let complexity: "LOW" | "MEDIUM" | "HIGH" = "MEDIUM"

    // Classify by keywords
    if (lowerTask.includes("email")) {
      intent = "write emails"
      logicLayers = LOGIC_LAYER_MAP["email"]
      domain = DOMAIN_MAP["email"]
      complexity = "MEDIUM"
    } else if (lowerTask.includes("call") || lowerTask.includes("phone")) {
      intent = "make calls"
      logicLayers = LOGIC_LAYER_MAP["call"]
      domain = DOMAIN_MAP["sales"]
      complexity = "HIGH"
    } else if (lowerTask.includes("score") || lowerTask.includes("qualify")) {
      intent = "qualify leads"
      logicLayers = LOGIC_LAYER_MAP["score"]
      domain = DOMAIN_MAP["lead"]
      complexity = "MEDIUM"
    } else if (lowerTask.includes("security") || lowerTask.includes("audit")) {
      intent = "security audit"
      logicLayers = LOGIC_LAYER_MAP["security"]
      domain = DOMAIN_MAP["security"]
      complexity = "HIGH"
    } else if (lowerTask.includes("write") || lowerTask.includes("create")) {
      intent = "create content"
      logicLayers = LOGIC_LAYER_MAP["write"]
      domain = DOMAIN_MAP["product"]
      complexity = "MEDIUM"
    } else if (lowerTask.includes("close") || lowerTask.includes("deal")) {
      intent = "close deals"
      logicLayers = LOGIC_LAYER_MAP["close"]
      domain = DOMAIN_MAP["sales"]
      complexity = "HIGH"
    } else {
      intent = "unknown task"
      logicLayers = ["LOGIC-049"]
      complexity = "MEDIUM"
    }

    return {
      intent,
      logicLayers,
      domain,
      complexity,
      estimatedCost: complexity === "HIGH" ? 100 : complexity === "MEDIUM" ? 50 : 25,
      estimatedRevenue: complexity === "HIGH" ? 5000 : complexity === "MEDIUM" ? 2500 : 1000,
    }
  }

  /**
   * PHASE 2.1c: Query registries to find candidate agents
   */
  queryRegistries(classification: TaskClassification): CandidateAgent[] {
    const candidates: CandidateAgent[] = []

    // Get all agents in matching domain
    const domainAgents = this.agentRegistry.getAgentsByDomain(classification.domain)

    // Filter by logic layers
    for (const agent of domainAgents) {
      const matchingLayers = agent.logicLayers.filter(layer =>
        classification.logicLayers.includes(layer)
      )

      if (matchingLayers.length > 0) {
        // Check autonomy level matches complexity
        const autonomyOk =
          (classification.complexity === "LOW" && ["L1", "L2", "L3"].includes(agent.autonomyLevel)) ||
          (classification.complexity === "MEDIUM" && ["L2", "L3"].includes(agent.autonomyLevel)) ||
          (classification.complexity === "HIGH" && agent.autonomyLevel === "L3")

        if (autonomyOk) {
          // Calculate relevance score based on logic layer match
          const relevanceScore = matchingLayers.length / classification.logicLayers.length

          candidates.push({
            ...agent,
            relevanceScore,
          })
        }
      }
    }

    // Also check by capability
    const capabilityAgentIds = this.capabilityRegistry
      .getAgentsByCapability(classification.intent)
      .slice(0, 5)

    for (const agentId of capabilityAgentIds) {
      const agent = this.agentRegistry.getAgentById(agentId)
      if (agent && !candidates.find(c => c.id === agent.id)) {
        candidates.push({
          ...agent,
          relevanceScore: 0.8,
        })
      }
    }

    return candidates.slice(0, 10) // Return max 10 candidates
  }

  /**
   * PHASE 2.1d: Rank candidates by composite score
   */
  rankCandidates(candidates: CandidateAgent[]): RankedAgent[] {
    const ranked = candidates.map((agent, idx) => {
      // Composite score: trustworthiness (50%) + success_rate (30%) + cost efficiency (20%)
      const trustScore = agent.trustworthiness * 0.5
      const successScore = (agent.successRate / 100) * 0.3
      const costScore = Math.min(1 / (agent.costPerUse + 1), 1) * 0.2 // Inverse cost, capped at 1

      const finalScore = trustScore + successScore + costScore

      return {
        ...agent,
        finalScore: Math.round(finalScore * 100) / 100,
        rankPosition: idx + 1,
        reasoning: `Trustworthiness: ${(agent.trustworthiness * 100).toFixed(0)}%, Success Rate: ${agent.successRate}%, Cost: $${agent.costPerUse}`,
      }
    })

    // Sort by final score descending
    return ranked.sort((a, b) => b.finalScore - a.finalScore)
  }

  /**
   * PHASE 2.1a (supporting): Check autonomy gate
   */
  enforceAutonomyGate(agent: Agent, task: string): GateDecision {
    const taskLength = task.length
    const isHighRisk =
      task.toLowerCase().includes("delete") ||
      task.toLowerCase().includes("transfer") ||
      task.toLowerCase().includes("critical")

    if (agent.autonomyLevel === "L1") {
      return {
        approved: true,
        autonomyLevel: "L1",
        requiresHumanReview: true,
        reason: "L1 agent requires human review before execution",
      }
    }

    if (agent.autonomyLevel === "L2") {
      return {
        approved: true,
        autonomyLevel: "L2",
        requiresHumanReview: isHighRisk || taskLength > 500,
        reason: isHighRisk ? "High-risk task requires review" : "Assisted execution with optional review",
      }
    }

    return {
      approved: true,
      autonomyLevel: "L3",
      requiresHumanReview: false,
      reason: "L3 agent can execute autonomously",
    }
  }

  /**
   * Main routing method: suggest the best agent for a task
   */
  suggestAgent(task: string): AgentSuggestion {
    // Step 1: Classify the task
    const classification = this.classifyTask(task)

    // Step 2: Query registries for candidates
    const candidates = this.queryRegistries(classification)

    if (candidates.length === 0) {
      throw new Error(`No agents found for task: ${task}`)
    }

    // Step 3: Rank candidates
    const ranked = this.rankCandidates(candidates)

    // Step 4: Enforce autonomy gate
    const topAgent = ranked[0]
    const gateDecision = this.enforceAutonomyGate(topAgent, task)

    // Step 5: Check tool permissions
    const toolsOk = topAgent.requiredTools.every(tool =>
      this.toolGateway.checkPermission(topAgent.id, tool)
    )

    if (!toolsOk) {
      throw new Error(`Agent ${topAgent.name} lacks tool permissions`)
    }

    const suggestion: AgentSuggestion = {
      topAgent,
      alternatives: ranked.slice(1, 4),
      confidence: topAgent.finalScore,
      costEstimate: classification.estimatedCost,
      revenueProjection: classification.estimatedRevenue,
      gateDecision,
      nextSteps: [
        gateDecision.requiresHumanReview ? "✓ Review agent output before executing" : "✓ Execute autonomously",
        `✓ Track ${topAgent.requiredTools.join(", ")} usage`,
        `✓ Monitor for ${topAgent.requiredSkills.join(", ")} quality`,
        "✓ Log revenue attribution",
      ],
    }

    this.logDecision(task, suggestion)
    return suggestion
  }

  /**
   * Supporting: Calculate agent score
   */
  private calculateScore(agent: Agent, task: TaskClassification): number {
    const trustScore = agent.trustworthiness * 0.5
    const successScore = (agent.successRate / 100) * 0.3
    const costScore = Math.min(1 / (agent.costPerUse + 1), 1) * 0.2
    return trustScore + successScore + costScore
  }

  /**
   * Supporting: Check tool permissions
   */
  private checkPermissions(agent: Agent, tools: string[]): boolean {
    return tools.every(tool => this.toolGateway.checkPermission(agent.id, tool))
  }

  /**
   * Supporting: Estimate revenue projection
   */
  private estimateRevenue(agent: Agent, task: string): number {
    const baseRevenue = 1000
    const successMultiplier = agent.successRate / 100
    const complexityMultiplier = task.length > 500 ? 2 : 1
    return baseRevenue * successMultiplier * complexityMultiplier
  }

  /**
   * Supporting: Log routing decisions for audit trail
   */
  private logDecision(task: string, suggestion: AgentSuggestion): void {
    this.decisionLog.push({
      task,
      suggestion,
      timestamp: new Date(),
    })
  }

  /**
   * Public: Get decision audit log
   */
  getDecisionLog(): Array<{ task: string; suggestion: AgentSuggestion; timestamp: Date }> {
    return this.decisionLog
  }
}

// ============================================================
// EXAMPLE USAGE
// ============================================================

/*
const router = new AgentDispatchRouter(
  agentRegistry,
  skillRegistry,
  toolGateway,
  capabilityRegistry
)

// Example 1: Write emails
const suggestion1 = router.suggestAgent("Write 50 cold emails to prospects")
console.log(`Top agent: ${suggestion1.topAgent.name}`)
console.log(`Confidence: ${suggestion1.confidence}`)
console.log(`Requires review: ${suggestion1.gateDecision.requiresHumanReview}`)

// Example 2: Score leads
const suggestion2 = router.suggestAgent("Score these 100 inbound leads")
console.log(`Top agent: ${suggestion2.topAgent.name}`)

// Example 3: Audit security
const suggestion3 = router.suggestAgent("Audit security vulnerabilities in our API")
console.log(`Top agent: ${suggestion3.topAgent.name}`)
*/
