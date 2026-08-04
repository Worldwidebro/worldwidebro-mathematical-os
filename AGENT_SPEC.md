---
title: Agent Specification Schema (AGENT_SPEC.md)
version: 1.0
date: 2026-07-30
owner: Hermes Agent
applies: Every agent (Hermes, BuildAgent, SalesAgent, etc.)
companion: [[AGENT-BRACKET-STANDARD.md]], [[AGENT_PROTOCOL.md]], [[AGENT_ONTOLOGY.md]]
---

# Agent Specification Schema

**Purpose**: Define agents like APIs — formal contract that specifies identity, mission, capabilities, tools, permissions, memory, inputs, outputs, KPIs, escalation rules, cost limits, and autonomy level.

**Goal**: Enable dynamic agent creation, monitoring, and optimization across 712 ventures.

---

## Core Agent Spec

Every agent (Hermes, BuildAgent, SalesAgent, etc.) has a formal YAML spec stored in Neo4j + Supabase:

```yaml
---
agent_id: AGENT-001
agent_name: Hermes
agent_type: ORCHESTRATOR_AGENT
version: "2.1.0"
mission: "Orchestrate venture operations across 712 ventures"
autonomy_level: LEVEL_3
capabilities:
  - venture_routing
  - capability_matching
  - workflow_orchestration
tools:
  - Neo4j
  - vex-api
  - Supabase
  - Redis
input_schema:
  type: object
  required: [agent, task, venture, objective]
output_schema:
  type: object
  properties: {status, result, audit_log, metrics}
kpis:
  success_rate: {target: "95%", current: "95.2%"}
  response_time: {target: "<1s", current: "0.8s"}
costs:
  per_decision: 0.05
  budget_monthly: 1000
slas:
  response_time: "1s P99"
  availability: "99.9%"
---
```

---

## Agent Types (13 Total)

```yaml
EXECUTIVE_AGENT:
  examples: [CEO Agent, CFO Agent, CTO Agent]
  autonomy: LEVEL_5
  role: "Make business decisions"
  
MANAGER_AGENT:
  examples: [Operations Agent, Sales Manager Agent]
  autonomy: LEVEL_3
  role: "Oversee teams, delegate work"
  
WORKER_AGENT:
  examples: [BuildAgent, DeployAgent]
  autonomy: LEVEL_3
  role: "Execute specific tasks"
  
RESEARCH_AGENT:
  examples: [MarketResearch Agent, CompetitorAnalysis Agent]
  autonomy: LEVEL_2
  role: "Gather and analyze information"
  
ANALYST_AGENT:
  examples: [DataAnalyst Agent, FinanceAnalyst Agent]
  autonomy: LEVEL_2
  role: "Analyze data, provide insights"
  
ENGINEERING_AGENT:
  examples: [BuildAgent, IntegrationAgent]
  autonomy: LEVEL_3
  role: "Build and deploy software"
  
SALES_AGENT:
  examples: [SalesAgent, AccountManager Agent]
  autonomy: LEVEL_3
  role: "Find and close deals"
  
MARKETING_AGENT:
  examples: [MarketingAgent, ContentAgent]
  autonomy: LEVEL_3
  role: "Drive awareness and pipeline"
  
FINANCE_AGENT:
  examples: [FinanceAgent, PayrollAgent]
  autonomy: LEVEL_2
  role: "Manage finances and budgets"
  
LEGAL_AGENT:
  examples: [ContractAgent, ComplianceAgent]
  autonomy: LEVEL_1
  role: "Review legal and compliance"
  
OPERATIONS_AGENT:
  examples: [Operations Agent, LogisticsAgent]
  autonomy: LEVEL_3
  role: "Run day-to-day operations"
  
SECURITY_AGENT:
  examples: [SecurityAgent, AuditAgent]
  autonomy: LEVEL_2
  role: "Protect systems and data"
  
DATA_AGENT:
  examples: [DataEngineer Agent, AnalyticsAgent]
  autonomy: LEVEL_2
  role: "Manage data pipelines and warehouses"
```

---

## Input/Output Contract

### Valid Input to Any Agent

```json
{
  "agent": "BuildAgent",
  "agent_type": "WORKER_AGENT",
  "task": "DEPLOY",
  "venture": "CON-001",
  "objective": "Get production URL live",
  "inputs": {
    "repository": "worldwidebro/con-ventures",
    "branch": "main",
    "deploy_target": "Vercel production"
  },
  "timeline": "2 hours",
  "approvals_required": ["CTO Agent"],
  "monitoring": {
    "deployment_url": "required",
    "health_status": "required"
  }
}
```

### Valid Output from Any Agent

```json
{
  "agent": "BuildAgent",
  "status": "DEPLOYED",
  "result": {
    "deployment_url": "https://con-001-ace-construction.vercel.app",
    "health_status": "HEALTHY",
    "build_time_seconds": 120,
    "deployment_time_seconds": 45
  },
  "metrics": {
    "success_rate": 98.5,
    "cost_usd": 0.75,
    "execution_time_seconds": 165
  },
  "audit_log": [
    "2026-07-30T14:00:00Z: Started build",
    "2026-07-30T14:02:00Z: Tests passed",
    "2026-07-30T14:03:00Z: Deployed to staging",
    "2026-07-30T14:03:45Z: Health checks passed",
    "2026-07-30T14:03:45Z: Promoted to production"
  ],
  "next_steps": ["Monitor for errors", "Get stakeholder sign-off"]
}
```

---

## Version History
- **v1.0 (2026-07-30)**: Agent specification schema foundation.
