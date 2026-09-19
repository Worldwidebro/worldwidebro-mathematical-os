/**
 * OmniRoute Agent Registration Service
 * Wires agents into OmniRoute A2A protocol as JSON-RPC 2.0 skills
 *
 * Authority: CP-012 (Agent Control Plane)
 * Updated: 2026-09-19
 */

import * as fs from "fs";
import * as path from "path";

interface A2ASkillRegistration {
  jsonrpc: "2.0";
  method: "skills/register";
  params: {
    id: string;
    name: string;
    description: string;
    tags: string[];
    examples: string[];
    agent_config: AgentConfig;
  };
  id: string;
}

interface AgentConfig {
  id: string;
  name: string;
  domain: string;
  autonomy_level: "L1" | "L2" | "L3";
  cost_per_use: number;
  success_rate: number;
  required_tools: string[];
}

interface A2AResponse {
  jsonrpc: "2.0";
  id: string;
  result?: {
    status: "registered" | "updated";
    skill_id: string;
    task_id: string;
    registered_at: string;
  };
  error?: {
    code: number;
    message: string;
  };
}

export class OmniRouteAgentRegister {
  private omnirouteEndpoint: string;
  private apiKey: string;

  constructor(omnirouteEndpoint: string = "http://100.87.214.70:3000", apiKey: string = "") {
    this.omnirouteEndpoint = omnirouteEndpoint;
    this.apiKey = apiKey;
  }

  /**
   * Load agent JSON descriptor and register as A2A skill
   */
  async registerAgent(agentJsonPath: string): Promise<A2AResponse> {
    const agentJson = JSON.parse(fs.readFileSync(agentJsonPath, "utf-8"));

    const registration: A2ASkillRegistration = {
      jsonrpc: "2.0",
      method: "skills/register",
      params: {
        id: agentJson.id,
        name: agentJson.name,
        description: agentJson.description,
        tags: agentJson.tags || [],
        examples: agentJson.examples?.map((ex: any) => ex.input) || [],
        agent_config: {
          id: agentJson.id,
          name: agentJson.name,
          domain: agentJson.domain,
          autonomy_level: agentJson.autonomy_level,
          cost_per_use: agentJson.cost_per_use,
          success_rate: agentJson.success_rate,
          required_tools: agentJson.required_tools,
        },
      },
      id: `register-${agentJson.id}-${Date.now()}`,
    };

    try {
      const response = await fetch(`${this.omnirouteEndpoint}/a2a`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          ...(this.apiKey && { Authorization: `Bearer ${this.apiKey}` }),
        },
        body: JSON.stringify(registration),
      });

      const result: A2AResponse = await response.json();

      if (result.error) {
        throw new Error(`A2A Registration failed: ${result.error.message}`);
      }

      console.log(`✅ Agent registered: ${agentJson.name} (${result.result?.skill_id})`);
      return result;
    } catch (error) {
      console.error(`❌ Registration error for ${agentJson.id}:`, error);
      throw error;
    }
  }

  /**
   * Query agent discovery endpoint
   */
  async getAgentCard(): Promise<any> {
    try {
      const response = await fetch(`${this.omnirouteEndpoint}/.well-known/agent.json`);
      return await response.json();
    } catch (error) {
      console.error("Failed to fetch agent card:", error);
      throw error;
    }
  }

  /**
   * Test agent routing via A2A
   */
  async testAgentRouting(skillId: string, message: string): Promise<any> {
    const testRequest = {
      jsonrpc: "2.0",
      id: `test-${Date.now()}`,
      method: "message/send",
      params: {
        skill: skillId,
        messages: [{ role: "user", content: message }],
        metadata: { test: true },
      },
    };

    try {
      const response = await fetch(`${this.omnirouteEndpoint}/a2a`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          ...(this.apiKey && { Authorization: `Bearer ${this.apiKey}` }),
        },
        body: JSON.stringify(testRequest),
      });

      const result = await response.json();

      if (result.error) {
        throw new Error(`Routing failed: ${result.error.message}`);
      }

      console.log(`✅ Agent routing test passed for ${skillId}`);
      console.log(`   Cost envelope:`, result.result?.metadata?.cost_envelope);
      console.log(`   Policy verdict:`, result.result?.metadata?.policy_verdict);
      return result.result;
    } catch (error) {
      console.error(`❌ Routing test failed:`, error);
      throw error;
    }
  }
}

// CLI: Register Lead Qualifier agent
if (require.main === module) {
  const register = new OmniRouteAgentRegister();

  (async () => {
    try {
      const agentPath = path.join(__dirname, "agents/lead-qualifier-a2a.json");
      console.log(`📝 Registering agent from: ${agentPath}`);

      const result = await register.registerAgent(agentPath);
      console.log(`\n✅ Registration result:`, JSON.stringify(result, null, 2));

      // Verify registration
      console.log(`\n🔍 Checking agent discovery...`);
      const card = await register.getAgentCard();
      const skillsCount = card.skills?.length || 0;
      console.log(`   Found ${skillsCount} skills registered in OmniRoute`);

      // Test routing
      console.log(`\n🧪 Testing agent routing...`);
      await register.testAgentRouting("lead-qualifier", "Score these 5 leads: [...]");
    } catch (error) {
      console.error("Registration failed:", error);
      process.exit(1);
    }
  })();
}

export default OmniRouteAgentRegister;
