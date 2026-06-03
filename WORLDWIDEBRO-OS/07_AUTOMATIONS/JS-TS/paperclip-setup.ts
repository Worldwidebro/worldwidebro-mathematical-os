/**
 * Paperclip Setup Script
 * Populates the Paperclip orchestration platform with:
 * - Worldwidebro Holdings organization (existing)
 * - CEO + operational agents
 * - Budget allocation per agent role
 * - Task templates for venture management
 */

const PAPERCLIP_API = "http://localhost:3101/api";
const COMPANY_ID = "1450a240-2be1-4dc6-b74c-ada307ca6ddb"; // Existing worldwidebro company

interface UpdateCompanyRequest {
  name?: string;
  description?: string;
  budgetMonthlyCents?: number;
}

interface CreateAgentRequest {
  name: string;
  companyId: string;
  role: "ceo" | "cto" | "cmo" | "cfo" | "security" | "engineer" | "designer" | "pm" | "qa" | "devops" | "researcher" | "general";
  budgetMonthlyCents?: number;
  traits?: string[];
  systemPrompt?: string;
}

async function apiCall<T>(
  method: string,
  path: string,
  body?: any
): Promise<T> {
  const response = await fetch(`${PAPERCLIP_API}${path}`, {
    method,
    headers: {
      "Content-Type": "application/json",
    },
    body: body ? JSON.stringify(body) : undefined,
  });

  if (!response.ok) {
    const error = await response.text();
    throw new Error(
      `API Error (${response.status}): ${error || response.statusText}`
    );
  }

  return response.json();
}

async function updateCompany(
  id: string,
  data: UpdateCompanyRequest
): Promise<any> {
  console.log(`Updating company: ${id}`);
  return apiCall("PATCH", `/companies/${id}`, data);
}

async function createAgent(
  data: CreateAgentRequest
): Promise<{ id: string; name: string }> {
  console.log(`  Creating agent: ${data.name} (${data.role})`);
  return apiCall("POST", `/companies/${data.companyId}/agents`, data);
}

async function getCompany(id: string): Promise<any> {
  return apiCall("GET", `/companies/${id}`);
}

async function listAgents(companyId: string): Promise<any[]> {
  return apiCall("GET", `/companies/${companyId}/agents`);
}

async function main() {
  console.log("🚀 Populating Paperclip with Worldwidebro Setup...\n");

  try {
    // 1. Update the existing company
    console.log("📋 Step 1: Update Company Configuration");
    console.log("======================================\n");

    const company = await updateCompany(COMPANY_ID, {
      name: "Worldwidebro Holdings",
      description:
        "4-Layer Capital System: 687 ventures across 17 sectors, $100K+/month target",
      budgetMonthlyCents: 500000, // $5,000/month operational budget
    });

    console.log(
      `✅ Company updated: ${company.name}\n   Budget: $${(company.budgetMonthlyCents / 100).toFixed(2)}/month\n`
    );

    // 2. Create core agents
    console.log("👥 Step 2: Create Operational Agents");
    console.log("===================================\n");

    const agents: Record<string, any> = {};

    const ceoData = {
      name: "Worldwidebro CEO",
      companyId: COMPANY_ID,
      role: "ceo" as const,
      budgetMonthlyCents: 100000, // $1,000/month for CEO decisions
      traits: ["strategic-planning", "capital-allocation", "risk-management"],
      systemPrompt: `You are the CEO of Worldwidebro Holdings, orchestrating 687 ventures across 4 capital layers.
Your responsibilities:
- Strategic capital allocation across ventures
- Portfolio optimization (kill low ROI ventures, scale high ROI)
- Budget approval for ventures exceeding thresholds
- Decision escalation from operational managers
- Monthly portfolio review and rebalancing

Decision Framework:
- ROI < 0%: Kill venture (unless strategic loss leader)
- ROI 0-50%: Hold, optimize, consider pivot
- ROI 50-100%: Scale aggressively, allocate more capital
- ROI > 100%: Compounding machine - reinvest all profit

Always consider: ROI, risk, cashflow timing, and system-wide capital efficiency.`,
    };

    agents.ceo = await createAgent(ceoData);

    const opsData = {
      name: "Operations Manager",
      companyId: COMPANY_ID,
      role: "cto" as const,
      budgetMonthlyCents: 50000, // $500/month for ops
      traits: [
        "process-automation",
        "team-coordination",
        "efficiency",
        "metric-tracking",
      ],
      systemPrompt: `You are the Operations Manager for Worldwidebro Holdings.
Your responsibilities:
- Coordinate day-to-day venture operations
- Monitor venture health metrics (CAC, LTV, churn, margin)
- Escalate issues to CEO when intervention needed
- Route tasks to appropriate sector agents
- Track operational KPIs
- Execute CEO-approved decisions across ventures

Key Metrics You Track:
- CAC (Customer Acquisition Cost)
- LTV (Lifetime Value)
- Churn Rate (% customers lost per month)
- Gross Margin (revenue - direct costs / revenue)
- Cash Runway (if negative revenue)`,
    };

    agents.ops = await createAgent(opsData);

    const analystData = {
      name: "Financial Analyst",
      companyId: COMPANY_ID,
      role: "cfo" as const,
      budgetMonthlyCents: 25000, // $250/month for analysis
      traits: [
        "financial-modeling",
        "metrics-tracking",
        "forecasting",
        "data-analysis",
      ],
      systemPrompt: `You are the Financial Analyst for Worldwidebro Holdings.
Your responsibilities:
- Calculate and track CAC/LTV for each venture
- Identify margin compression or churn spikes
- Model revenue projections by venture type
- Flag ventures underperforming against targets
- Generate monthly financial reports
- Monitor burn rate for negative-revenue ventures
- Track unit economics across all 7 revenue stream types`,
    };

    agents.analyst = await createAgent(analystData);

    console.log(`\n✅ Core agents created:\n`);
    for (const [role, agent] of Object.entries(agents)) {
      console.log(`   • ${agent.name} (${role})`);
    }
    console.log();

    // 3. Create venture sector lead agents
    console.log("🏢 Step 3: Create Sector Lead Agents");
    console.log("===================================\n");

    const sectors = [
      {
        name: "Financial Services",
        icon: "💰",
        ventures: [
          "GenixBank-Lite",
          "PayFlow-Remittance",
          "WealthOS-Advisor",
        ],
      },
      {
        name: "Construction",
        icon: "🏗️",
        ventures: [
          "Ace-General-Contracting",
          "Roofing-Specialists",
          "Equipment-Rental",
        ],
      },
      {
        name: "E-Commerce & Digital",
        icon: "🛒",
        ventures: [
          "ProductHub-Marketplace",
          "DigitalServices-Agency",
          "Fulfillment-Network",
        ],
      },
      {
        name: "SaaS & Software",
        icon: "💻",
        ventures: [
          "ProjectMgmt-Platform",
          "HRMS-Solution",
          "Analytics-Engine",
        ],
      },
    ];

    const sectorAgents: Record<string, string> = {};

    for (const sector of sectors) {
      const agent = await createAgent({
        name: `${sector.name} Lead`,
        companyId: COMPANY_ID,
        role: "pm",
        budgetMonthlyCents: Math.round(100000 / sectors.length),
        traits: [
          "sector-expertise",
          "venture-scaling",
          "market-analysis",
          "partnership-building",
        ],
        systemPrompt: `You manage ${sector.name} ventures at Worldwidebro Holdings.
You oversee ventures like: ${sector.ventures.join(", ")}

Your responsibilities:
- Monitor health of ventures in your sector
- Identify cross-venture collaboration opportunities
- Recommend resource allocation within sector
- Escalate sector-wide risks to CEO
- Facilitate knowledge sharing between ventures
- Lead sector-specific business development`,
      });
      sectorAgents[sector.name] = agent.id;
      console.log(`✅ ${sector.icon} ${sector.name} Lead: ${agent.name}`);
    }

    console.log();

    // 4. Summary
    console.log("📊 Step 4: Setup Complete");
    console.log("========================\n");

    const finalCompany = await getCompany(COMPANY_ID);
    const allAgents = await listAgents(COMPANY_ID);

    console.log(`Organization: ${finalCompany.name}`);
    console.log(`Monthly Budget: $${(finalCompany.budgetMonthlyCents / 100).toFixed(2)}`);
    console.log(
      `Total Agents: ${allAgents.length} (${allAgents.filter((a) => a.role === "ceo").length} CEO, ${allAgents.filter((a) => a.role === "manager").length} managers, ${allAgents.filter((a) => a.role === "analyst").length} analysts)`
    );
    console.log(`\nAgent Breakdown:\n`);

    // Group by role
    const byRole = allAgents.reduce(
      (acc, agent) => {
        if (!acc[agent.role]) acc[agent.role] = [];
        acc[agent.role].push(agent);
        return acc;
      },
      {} as Record<string, any[]>
    );

    for (const [role, roleAgents] of Object.entries(byRole)) {
      console.log(`${role.toUpperCase()}:`);
      for (const agent of roleAgents) {
        console.log(
          `  • ${agent.name} - Budget: $${(agent.budgetMonthlyCents / 100).toFixed(2)}/mo`
        );
      }
      console.log();
    }

    console.log("✅ Paperclip Setup Complete!");
    console.log(`\n📍 Web UI: http://localhost:3101`);
    console.log(`📍 API Base: ${PAPERCLIP_API}`);
    console.log(`📍 Company ID: ${COMPANY_ID}`);
    console.log(`\nNext Steps:`);
    console.log(`1. Open http://localhost:3101 in your browser`);
    console.log(`2. You'll see the Worldwidebro Holdings org chart`);
    console.log(`3. Create projects for ventures under the CEO agent`);
    console.log(`4. Define tasks for sector leads and operations manager`);
  } catch (error) {
    console.error("❌ Setup failed:", error);
    process.exit(1);
  }
}

main();
