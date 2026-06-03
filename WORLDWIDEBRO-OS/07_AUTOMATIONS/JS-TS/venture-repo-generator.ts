/**
 * Venture Repository Generator
 * Creates starter files in each venture's managed folder so Claude can understand what it does
 * Generates: README, business logic, KPIs, operations guide
 */

import * as fs from "fs";
import * as path from "path";

const PAPERCLIP_ROOT =
  "/Users/acebless/.paperclip/instances/default/projects";
const COMPANY_ID = "1450a240-2be1-4dc6-b74c-ada307ca6ddb";

interface VentureTemplate {
  sector: string;
  name: string;
  description: string;
  businessModel: string;
  kpis: {
    monthlyRevenue: string;
    monthlyChurn: string;
    customerAcquisitionCost: string;
    customerLifetimeValue: string;
  };
  operations: string[];
}

const SECTOR_TEMPLATES: Record<string, VentureTemplate> = {
  "Financial Services": {
    sector: "Financial Services",
    name: "Bank/FinTech Platform",
    description:
      "Provides financial solutions, payments, lending, or investment services",
    businessModel:
      "Fee-based (transaction %, subscription, interest spread margin)",
    kpis: {
      monthlyRevenue: "$50K+ MRR target",
      monthlyChurn: "<3% monthly churn (high lifetime value)",
      customerAcquisitionCost: "$500-$2000 per customer",
      customerLifetimeValue: "$2000-$10000 per customer",
    },
    operations: [
      "Regulatory compliance management",
      "Customer onboarding & KYC",
      "Transaction processing & settlement",
      "Risk & fraud detection",
    ],
  },
  Construction: {
    sector: "Construction",
    name: "Construction/Contractor Services",
    description: "Project management, equipment rental, contracting services",
    businessModel: "Project-based or rental fees",
    kpis: {
      monthlyRevenue: "$30K+ project revenue",
      monthlyChurn: "<5% monthly (project-based cycles)",
      customerAcquisitionCost: "$5000-$15000 per contract",
      customerLifetimeValue: "$50000-$200000 per customer",
    },
    operations: [
      "Project estimation & bidding",
      "Crew scheduling & management",
      "Equipment tracking & maintenance",
      "Safety compliance & certifications",
    ],
  },
  "E-Commerce & Digital": {
    sector: "E-Commerce & Digital",
    name: "E-Commerce Platform",
    description:
      "Online marketplace, fulfillment, inventory, or logistics operations",
    businessModel: "Product margins, fulfillment fees, or marketplace commission",
    kpis: {
      monthlyRevenue: "$20K+ product revenue",
      monthlyChurn: "<10% monthly (high competition)",
      customerAcquisitionCost: "$20-$100 per customer",
      customerLifetimeValue: "$200-$2000 per customer",
    },
    operations: [
      "Inventory management & forecasting",
      "Order fulfillment & shipping",
      "Customer service & returns",
      "Product sourcing & quality control",
    ],
  },
  "SaaS & Software": {
    sector: "SaaS & Software",
    name: "Software-as-a-Service Platform",
    description: "Cloud software, tools, APIs, or enterprise solutions",
    businessModel: "Subscription (per-seat, usage-based, tiered pricing)",
    kpis: {
      monthlyRevenue: "$40K+ MRR target",
      monthlyChurn: "<5% monthly (high NRR target: >110%)",
      customerAcquisitionCost: "$5000-$20000 per enterprise customer",
      customerLifetimeValue: "$50000-$500000 per customer",
    },
    operations: [
      "Product development & releases",
      "Customer success & onboarding",
      "API management & integrations",
      "Security & compliance (SOC2, GDPR)",
    ],
  },
};

function generateVentureReadme(template: VentureTemplate, name: string): string {
  return `# ${name}

## Venture Overview

**Sector**: ${template.sector}
**Type**: ${template.name}
**Description**: ${template.description}

## Business Model

${template.businessModel}

## Key Performance Indicators (KPIs)

- **Monthly Revenue Target**: ${template.kpis.monthlyRevenue}
- **Monthly Churn Rate**: ${template.kpis.monthlyChurn}
- **Customer Acquisition Cost (CAC)**: ${template.kpis.customerAcquisitionCost}
- **Customer Lifetime Value (LTV)**: ${template.kpis.customerLifetimeValue}
- **Healthy Ratio**: LTV/CAC ≥ 3.0

## Critical Operations

${template.operations.map((op) => `- ${op}`).join("\n")}

## Unit Economics Goals

\`\`\`
Monthly Revenue:        $40,000 - $100,000
Monthly Operating Cost: $15,000 - $50,000
Gross Margin:           ≥ 40%
Runway:                 ≥ 12 months cash
\`\`\`

## Scaling Thresholds

- **Optimize** (ROI 0-50%): Reduce costs by 20%, improve retention, test channels
- **Scale** (ROI 50-100%): 2x marketing budget, expand segments, improve margins
- **Compound** (ROI >100%): Reinvest all profits, aggressive hiring, adjacent markets

## Links

- **Dashboard**: http://localhost:3101 (Paperclip)
- **Financials**: See Supabase metrics table
- **Contacts**: OpenVolo CRM integration
- **Tasks**: Queued through sector lead agent
`;
}

function generateOperationsGuide(template: VentureTemplate): string {
  return `# Operations Guide - ${template.name}

## Daily Operations Checklist

### Metrics Tracking
- [ ] Revenue: Track daily/weekly sales, transactions, or bookings
- [ ] Costs: Monitor operational, payroll, infrastructure spend
- [ ] Churn: Track customer cancellations and expansion revenue (NRR)
- [ ] Growth: Monitor new customer acquisition and CAC

### Weekly Review
- [ ] Analyze unit economics (CAC, LTV, margin)
- [ ] Review customer feedback and support tickets
- [ ] Check runway (months of cash remaining)
- [ ] Identify risks and opportunities

### Monthly Planning
- [ ] Generate financial forecast
- [ ] Review ROI against sector benchmarks
- [ ] Adjust budget allocations if needed
- [ ] Plan next month's priorities

## CEO Decision Framework

| ROI | Decision | Action |
|-----|----------|--------|
| < 0% | KILL | Wind down operations, redeploy capital |
| 0-50% | OPTIMIZE | Cut costs 20%, improve retention, test channels |
| 50-100% | SCALE | 2x marketing, expand segments, improve margins |
| > 100% | COMPOUND | Reinvest profits, aggressive hiring, new markets |

## Integration Points

- **Financial Data**: Supabase metrics table
- **Team Communication**: Slack notifications from CEO decisions
- **Issue Tracking**: Linear for task management
- **Contact Management**: OpenVolo CRM
- **Code Repositories**: GitHub (if applicable)

## Approval Workflows

- Allocations < $10K: Sector lead approval
- Allocations $10K-$50K: CEO + CTO approval
- Allocations > $50K: Board approval required

## Escalation Contacts

- **Sector Lead**: [Agent name] (daily operations)
- **CFO/Financial Analyst**: Reviews unit economics
- **CEO Agent**: Strategic decisions
- **CTO/Operations Manager**: Execution & coordination
`;
}

function generateKpiDashboard(template: VentureTemplate): string {
  return `# KPI Dashboard Template

## Current Metrics (Last 30 Days)

\`\`\`
Monthly Revenue:           $________  (Target: ${template.kpis.monthlyRevenue})
Monthly Operational Cost:  $________
Gross Margin:              _____%    (Target: ≥40%)
Return on Investment:      _____%    (Status: HOLD/OPTIMIZE/SCALE/COMPOUND)

Customer Metrics:
├─ New Customers:          ______  (target: depends on CAC)
├─ Customer Churn:         _____%    (Target: ${template.kpis.monthlyChurn})
├─ CAC (Customer Acq. Cost): $______  (Target: ${template.kpis.customerAcquisitionCost})
├─ LTV (Lifetime Value):   $______  (Target: ${template.kpis.customerLifetimeValue})
└─ LTV/CAC Ratio:          ___x     (Healthy: >3.0)

Runway Analysis:
├─ Total Cash:             $________
├─ Monthly Burn Rate:      $________
└─ Months Remaining:       ____     (Alert if <6 months)
\`\`\`

## 90-Day Projection

Based on current trajectory:
- Projected Revenue (90 days): $________
- Projected Burn (90 days): $________
- Projected ROI Change: ___% (up/down)

## Last CEO Decision

- **Date**: ________
- **Decision**: KILL / HOLD / OPTIMIZE / SCALE / COMPOUND
- **ROI at Decision**: ____%
- **Budget Allocation**: $______/month
- **Action Items**:
  1. _____________________
  2. _____________________
  3. _____________________

## Next Review Date

__________ (Usually monthly)
`;
}

async function generateVentureRepos() {
  console.log(
    "🚀 Generating venture repository templates for Claude understanding...\n"
  );

  const companyPath = path.join(PAPERCLIP_ROOT, COMPANY_ID);

  if (!fs.existsSync(companyPath)) {
    console.error(`❌ Company path not found: ${companyPath}`);
    process.exit(1);
  }

  const projectDirs = fs.readdirSync(companyPath);
  let created = 0;
  let skipped = 0;

  for (const projectId of projectDirs) {
    const projectPath = path.join(companyPath, projectId);
    const managedFolder = path.join(projectPath, "_default");

    if (!fs.existsSync(managedFolder)) {
      continue;
    }

    // Read project metadata to get sector
    const metadataPath = path.join(projectPath, ".metadata");
    let sector = "General";

    try {
      // Try to infer sector from Paperclip API call (simplified)
      const apiCall = await fetch(
        `http://localhost:3101/api/companies/${COMPANY_ID}/projects/${projectId}`
      );
      if (apiCall.ok) {
        const project = await apiCall.json();
        // Extract sector from description or infer from name
        for (const s of Object.keys(SECTOR_TEMPLATES)) {
          if (
            project.description?.includes(s) ||
            project.name?.includes(s.split(" ")[0])
          ) {
            sector = s;
            break;
          }
        }

        const template =
          SECTOR_TEMPLATES[sector] || SECTOR_TEMPLATES["SaaS & Software"];
        const readme = generateVentureReadme(template, project.name);
        const opsGuide = generateOperationsGuide(template);
        const kpiDash = generateKpiDashboard(template);

        // Write files
        fs.writeFileSync(path.join(managedFolder, "README.md"), readme);
        fs.writeFileSync(
          path.join(managedFolder, "OPERATIONS.md"),
          opsGuide
        );
        fs.writeFileSync(
          path.join(managedFolder, "KPI_DASHBOARD.md"),
          kpiDash
        );

        created++;
      }
    } catch (error) {
      skipped++;
    }
  }

  console.log(
    `✅ Generated repository templates for ${created} ventures\n`
  );
  console.log(`📍 Each venture now has:`);
  console.log(`   - README.md (what venture does, business model, KPIs)`);
  console.log(
    `   - OPERATIONS.md (daily/weekly/monthly checklists, decision framework)`
  );
  console.log(`   - KPI_DASHBOARD.md (metrics tracking template)\n`);
  console.log(
    `Claude can now read ~/Documents/.paperclip/instances/default/projects/{VentureID}/_default/README.md to understand each venture\n`
  );
  console.log(`💡 Next: Link external repos (GitHub) OR populate with code\n`);
}

generateVentureRepos().catch(console.error);
