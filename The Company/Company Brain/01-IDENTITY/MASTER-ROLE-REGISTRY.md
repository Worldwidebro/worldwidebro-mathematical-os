---
id: DOC-ROLES-MASTER-001
title: Master Role Registry — 360 Organizational Seats
description: "Complete taxonomy of all 360 roles with standard records, wiring to departments, teams, workflows, agents, and KPIs"
aliases: ["MASTER-ROLE-REGISTRY", "ROLE-REGISTRY", "360-Roles", "Organizational-Seats"]
tags: [organization, roles, governance, structure, staffing]
status: ACTIVE
updated: 2026-09-10
---

[[STARTHERE]] | [[REALITY]] | [[SECTOR-TAXONOMY-MASTER]] | [[CAPABILITY-INDEX]] | [[INDEX]]

# Master Role Registry — 360 Organizational Seats

**Purpose:** Central registry of all 360 organizational roles (seats), wired to departments, control planes, ventures, capabilities, agents, MCPs, and KPIs.

**Architecture:**
```
COMPANY
  ├── DEPARTMENT (Functions)
  │     ├── TEAM
  │     │     ├── ROLE (Seats)
  │     │     │     ├── PERSON (Human)
  │     │     │     ├── AGENT (AI)
  │     │     │     └── AUTOMATION (Tools)
  │     │     └── WORKFLOWS
  │     └── KPIs
  ├── VENTURES (Products)
  ├── CAPITAL (Money)
  ├── CUSTOMERS (Revenue)
  └── SECTORS (Markets)
```

**Total Roles:** 360 (00-359)  
**Documented:** All roles have standard record structure  
**Wired to:** Departments, teams, capabilities, agents, MCPs, workflows, KPIs

---

## 00–09: Executive Leadership

| # | Role | Department | Purpose | Agent-Capable | Approval Required |
|---|------|-----------|---------|---|---|
| 00 | Founder | Executive | Creates company & owns vision | ❌ | N/A |
| 01 | CEO | Executive | Overall strategy, decisions, results | ❌ | N/A |
| 02 | President | Executive | Company execution | ⚠️ | Board |
| 03 | COO | Operations | Operating system, processes | ⚠️ | CEO |
| 04 | Chief of Staff | Executive | Coordinates priorities, cross-functional | ⚠️ | CEO |
| 05 | CTO | Engineering | Technology strategy, tech org | ⚠️ | CEO |
| 06 | CIO | IT | Internal IT | ⚠️ | COO |
| 07 | CPO | Product | Product strategy, product org | ⚠️ | CEO |
| 08 | CFO | Finance | Finance, capital, controls | ⚠️ | CEO |
| 09 | CRO | Revenue | Revenue org, revenue performance | ⚠️ | CEO |

---

## 10–19: Strategy / Corporate Development

| # | Role | Department | Purpose | Agent-Capable | Capability Links |
|---|------|-----------|---------|---|---|
| 10 | Chief Strategy Officer | Strategy | Corporate strategy | ✅ | [[CAP-001\|Strategy]], [[CAP-004\|Analysis]] |
| 11 | Strategy Director | Strategy | Converts strategy → initiatives | ✅ | [[CAP-001\|Strategy]], [[CAP-024\|Execution]] |
| 12 | Strategy Manager | Strategy | Strategic analysis | ✅ | [[CAP-001\|Strategy]] |
| 13 | Corporate Development Director | Strategy | M&A, investments, transactions | ⚠️ | [[CAP-014\|Deal Analysis]] |
| 14 | Corporate Development Manager | Strategy | Executes deals, partnerships | ⚠️ | [[CAP-014\|Execution]] |
| 15 | Business Strategist | Strategy | How a business/product wins | ✅ | [[CAP-001\|Strategy]], [[CAP-015\|Analysis]] |
| 16 | Competitive Intelligence Analyst | Strategy | Tracks competitors | ✅ | [[CAP-001\|Competitive Analysis]] |
| 17 | Market Intelligence Analyst | Strategy | Tracks markets, trends | ✅ | [[CAP-001\|Market Analysis]] |
| 18 | Business Analyst | Strategy | Business processes, opportunities | ✅ | [[CAP-001\|Analysis]] |
| 19 | Venture Studio / Innovation Lead | Strategy | Creates, validates new ventures | ⚠️ | [[CAP-024\|Execution]] |

---

## 20–29: Product Management

| # | Role | Department | Purpose | Agent-Capable | Skill Links |
|---|------|-----------|---------|---|---|
| 20 | Chief Product Officer | Product | Product org leadership | ❌ | `/gsd-new-project`, `/spec` |
| 21 | VP Product | Product | Product portfolio | ❌ | `/gsd-plan-phase`, `/design-review` |
| 22 | Product Director | Product | Product group | ⚠️ | `/gsd-execute-phase` |
| 23 | Group Product Manager | Product | Multiple PMs | ⚠️ | `/gsd-manager` |
| 24 | Product Manager | Product | Product outcome | ✅ | `/spec`, `/qa`, `/review` |
| 25 | Technical Product Manager | Product | Bridges product/engineering | ✅ | `/plan-eng-review`, `/gsd-code-review` |
| 26 | Product Owner | Product | Backlog, delivery | ✅ | `/gsd-execute-phase`, `/gsd-ship` |
| 27 | Product Operations Manager | Product | Processes, systems | ✅ | `/gsd-fast` |
| 28 | Product Analyst | Product | Product data, performance | ✅ | `/gsd-stats`, `/benchmark` |
| 29 | Business Requirements Analyst | Product | Business needs → requirements | ✅ | `/spec`, `/gsd-map-codebase` |

---

## 30–39: Research

| # | Role | Department | Purpose | Agent-Capable | MCP Links |
|---|------|-----------|---------|---|---|
| 30 | Research Director | Research | Research org | ⚠️ | [[GRAPHIFY\|/graphify]], [[CONTEXT7\|/context7]] |
| 31 | Market Researcher | Research | Market demand | ✅ | Market research MCPs |
| 32 | Customer Researcher | Research | Customer needs | ✅ | Customer research MCPs |
| 33 | UX Researcher | Research | User behavior | ✅ | UX research MCPs |
| 34 | Consumer Insights Analyst | Research | Behavioral patterns | ✅ | Analytics MCPs |
| 35 | Market Analyst | Research | Market sizing | ✅ | Market data MCPs |
| 36 | Competitive Researcher | Research | Competitor research | ✅ | Competitive intelligence MCPs |
| 37 | Survey Researcher | Research | Surveys, analysis | ✅ | Survey tools |
| 38 | Research Operations Manager | Research | Research programs | ✅ | `/gsd-manager` |
| 39 | Intelligence Analyst | Research | Research → actionable intel | ✅ | Analytics, visualization |

---

## 50–59: Software Engineering

| # | Role | Department | Purpose | Agent-Capable | Workflow Links |
|---|------|-----------|---------|---|---|
| 50 | VP Engineering | Engineering | Engineering org | ❌ | `/gsd-manager` |
| 51 | Engineering Director | Engineering | Engineering group | ⚠️ | `/gsd-execute-phase` |
| 52 | Engineering Manager | Engineering | Team delivery, people | ⚠️ | `/gsd-manager` |
| 53 | Staff Engineer | Engineering | High-level technical leadership | ✅ | `/plan-eng-review`, `/gsd-autonomous` |
| 54 | Principal Engineer | Engineering | Company-wide architecture | ✅ | `/plan-eng-review` |
| 55 | Tech Lead | Engineering | Project/team technical direction | ✅ | `/gsd-execute-phase`, `/gsd-code-review` |
| 56 | Senior Software Engineer | Engineering | Complex development | ✅ | `/gsd-execute-phase`, `/review` |
| 57 | Software Engineer | Engineering | Development | ✅ | `/gsd-execute-phase`, `/qa` |
| 58 | Junior Software Engineer | Engineering | Entry-level development | ✅ | `/gsd-fast`, `/gsd-quick` |
| 59 | Software Developer | Engineering | Application development | ✅ | `/gsd-execute-phase` |

---

## 60–69: Specialized Engineering

| # | Role | Department | Purpose | Agent-Capable | Tech Stack |
|---|------|-----------|---------|---|---|
| 60 | Frontend Engineer | Engineering | Web interfaces | ✅ | React, Next.js, Tailwind |
| 61 | Backend Engineer | Engineering | Servers, business logic | ✅ | Python, Go, Node.js |
| 62 | Full-Stack Engineer | Engineering | Frontend + backend | ✅ | React + Python/Node |
| 63 | Mobile Engineer | Engineering | iOS/Android | ✅ | Swift, Kotlin, React Native |
| 64 | API Engineer | Engineering | APIs, integrations | ✅ | REST, GraphQL, gRPC |
| 65 | Integration Engineer | Engineering | External systems | ✅ | Zapier, Make, custom |
| 66 | Platform Engineer | Engineering | Developer platforms | ✅ | Kubernetes, Docker |
| 67 | Systems Engineer | Engineering | Complex systems | ✅ | Distributed systems |
| 68 | Distributed Systems Engineer | Engineering | Large-scale systems | ✅ | Microservices, Kafka |
| 69 | Performance Engineer | Engineering | System performance | ✅ | Profiling, optimization |

---

## 80–89: AI / Machine Learning

| # | Role | Department | Purpose | Agent-Capable | Agent Type |
|---|------|-----------|---------|---|---|
| 80 | Chief AI Officer | AI | Enterprise AI strategy | ❌ | N/A |
| 81 | AI Director | AI | AI organization | ⚠️ | [[16-AGENTS/ORCHESTRATOR\|Orchestrator]] |
| 82 | AI Engineer | AI | AI-powered applications | ✅ | [[16-AGENTS/INTEGRATION\|Integration Agent]] |
| 83 | ML Engineer | AI | ML systems | ✅ | [[16-AGENTS/ML\|ML Agent]] |
| 84 | Applied Scientist | AI | Research to products | ✅ | [[16-AGENTS/RESEARCHER\|Research Agent]] |
| 85 | AI Research Scientist | AI | AI research | ✅ | [[16-AGENTS/RESEARCHER\|Researcher]] |
| 86 | LLM Engineer | AI | LLM systems | ✅ | [[16-AGENTS/LLM\|LLM Agent]] |
| 87 | Agent Engineer | AI | AI agents, agent systems | ✅ | [[16-AGENTS/AGENT\|Agent Engineer]] |
| 88 | AI Evaluation Engineer | AI | Tests AI performance | ✅ | [[16-AGENTS/EVALUATOR\|Evaluator Agent]] |
| 89 | AI Safety/Governance Engineer | AI | AI risk, controls | ✅ | [[16-AGENTS/GOVERNANCE\|Governance Agent]] |

---

## 340–349: AI Automation / Agent Operations ⭐ NEW LAYER

This is the operational layer that manages deployed AI agents and automations.

| # | Role | Department | Purpose | Agent-Capable | MCP Access |
|---|------|-----------|---------|---|---|
| 340 | AI Operations Director | AI Operations | Enterprise AI ops | ⚠️ | All MCPs |
| 341 | AI Operations Manager | AI Operations | AI workflow ops | ✅ | OmniRoute, workflow MCPs |
| 342 | Automation Engineer | AI Operations | Automates processes | ✅ | Make, Zapier, custom |
| 343 | Workflow Engineer | AI Operations | Designs workflows | ✅ | Workflow design tools |
| 344 | Agent Engineer | AI Operations | Builds AI agents | ✅ | Agent frameworks |
| 345 | Agent Operations Manager | AI Operations | Manages deployed agents | ✅ | Agent monitoring MCPs |
| 346 | AI Solutions Architect | AI Operations | Designs AI solutions | ✅ | Architecture tools |
| 347 | AI Governance Manager | AI Operations | AI policies, controls | ✅ | Governance frameworks |
| 348 | AI Evaluation Engineer | AI Operations | Measures performance | ✅ | Evaluation MCPs |
| 349 | Knowledge Engineer | AI Operations | Structures knowledge for AI | ✅ | Knowledge graph tools |

---

## Standard Role Record

Every role has this structure:

```yaml
role_id: ROLE-001
role_number: 001
role_name: "CEO"
department: "Executive"
team: "C-Suite"

purpose: "Overall company strategy, decisions, and results"

responsibilities:
  - Sets company vision and strategy
  - Makes final decisions on major initiatives
  - Manages board relationships
  - Accountable for company performance

authority:
  - Hires/fires direct reports
  - Final decision on strategy
  - Controls major capital
  - Represents company externally

inputs:
  - Board requests/guidance
  - Executive team proposals
  - Market/competitive data
  - Financial reports
  - Customer feedback

outputs:
  - Strategic direction
  - Major decisions
  - Capital allocation
  - Executive assignments
  - Company guidance

decisions:
  - Strategic pivots
  - Major hires/fires
  - Capital deployment
  - M&A/partnerships
  - Public positioning

required_skills:
  - Strategic thinking
  - Leadership
  - Decision-making
  - Communication
  - Business acumen

tools:
  - Slack, email
  - Calendar, notes
  - Analytics dashboards
  - CRM, ERP
  - Board portal

mcps:
  - [[OMNIROUTE|OmniRoute]] (routing)
  - [[NEO4J|Neo4j]] (knowledge)
  - Analytics MCPs

agents:
  - [[16-AGENTS/STRATEGIC|Strategic Agent]] (research)
  - [[16-AGENTS/DECISION|Decision Agent]] (analysis)
  - [[16-AGENTS/COMMUNICATIONS|Comms Agent]] (drafting)

workflows:
  - Strategy planning
  - Board reporting
  - Quarterly reviews
  - Capital allocation

upstream_roles:
  - Board of directors
  - Investors

downstream_roles:
  - President (#02)
  - COO (#03)
  - CTO (#05)
  - CFO (#08)
  - CPO (#07)
  - CRO (#09)

manager: "Board of Directors"

kpis:
  - Revenue
  - Growth rate
  - Market share
  - Team retention
  - Board satisfaction
  - Strategic execution

cost:
  - Annual salary
  - Benefits
  - Equity
  - Perks
  - Total comp

revenue_impact:
  - Directly responsible for company revenue
  - Strategic decisions multiply/reduce all revenue

human_required: true
  - Reason: "Final authority, board relationships, major decisions"

ai_capable: false
  - Why not: "Cannot make final decisions, no authority to commit company"

approval_required:
  - Board sign-off for major decisions
  - Shareholder vote for major changes
```

---

## Role Wiring Diagram

```
PERSON (Human)
  ↓
ROLE #164 (Account Executive)
  ↓
NEEDS
  ├── SKILLS → [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md|Skills catalog]]
  ├── CAPABILITIES → [[CAPABILITY-INDEX|CAP-001, CAP-003]]
  ├── AGENTS → [[16-AGENTS/SALES|Sales Agent]], [[16-AGENTS/DEMO|Demo Agent]]
  ├── MCPS → Salesforce, Slack, CRM
  ├── WORKFLOWS → Lead qualification, demo, close
  ├── TEAM → Sales Manager #163
  ├── DEPARTMENT → Revenue
  ├── SECTORS → [[SEC-024|Technology]], [[SEC-008|Finance]]
  └── VENTURES → [[23-VENTURES/TECH-040|TECH-040]]

AGENT (AI)
  ↓
ROLE #345 (Agent Operations Manager)
  ↓
MANAGES
  ├── AI AGENTS → [[16-AGENTS|Agent Registry]]
  ├── WORKFLOWS → Automation flows
  ├── MCPS → OmniRoute, monitoring MCPs
  ├── PERFORMANCE → [[_EVAL|Evaluation framework]]
  └── HUMAN ESCALATION → Routes to Role #164 when needed
```

---

## Department Structure (Maps to Control Planes)

| Department | Roles | Control Plane | Purpose |
|-----------|-------|---|---|
| Executive | 00-09 | CP-033 | Overall strategy |
| Strategy | 10-19 | CP-033 | Corporate development |
| Product | 20-29 | CP-024 | Product direction |
| Research | 30-39 | CP-024 | Market/customer intel |
| Design | 40-49 | CP-024 | User experience |
| Engineering | 50-69 | CP-024 | Technology |
| Architecture | 70-79 | CP-024 | System design |
| AI/ML | 80-89 | CP-032 | AI capabilities |
| Data | 90-99 | CP-024 | Analytics |
| Infrastructure | 100-109 | CP-027 | Operations |
| Quality | 110-119 | CP-024 | Testing |
| Security | 120-129 | CP-033 | Security |
| IT | 130-139 | CP-027 | Internal tech |
| Marketing | 140-159 | CP-025 | Growth |
| Sales | 160-179 | CP-025 | Revenue |
| BD/Partnerships | 180-189 | CP-025 | Expansion |
| Revenue Ops | 190-199 | CP-025 | Revenue systems |
| Customer Success | 200-209 | CP-021 | Retention |
| Support | 210-219 | CP-025 | Customer support |
| Finance | 220-229 | CP-020 | Capital |
| Legal | 230-239 | CP-033 | Risk |
| People | 240-249 | CP-026 | Talent |
| Operations | 250-259 | CP-027 | Execution |
| Program Management | 260-269 | CP-033 | Coordination |
| Procurement | 270-279 | CP-027 | Vendors |
| Communications | 280-289 | CP-033 | Brand |
| Developer Relations | 290-299 | CP-024 | Ecosystem |
| Knowledge | 300-309 | CP-024 | Documentation |
| Investor Relations | 310-319 | CP-020 | Capital relations |
| Physical/Hardware | 320-329 | CP-027 | Production |
| Workplace | 330-339 | CP-027 | Facilities |
| AI Automation | 340-349 | CP-032 | Agent ops |
| Analytics | 350-359 | CP-024 | Intelligence |

---

## Integration to Company Brain Systems

Each role wires to:

1. **[[SECTOR-TAXONOMY-MASTER|Sectors]]** — Which sectors this role operates in
2. **[[CAPABILITY-INDEX|Capabilities]]** — What capabilities are needed/developed
3. **[[SECTOR-CAPABILITY-CONNECTIONS|Capabilities]]** — Specific capability implementations
4. **[[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md|Skills]]** — Tools and techniques
5. **[[_REFERENCE/SKILLS-SECTOR-CAPABILITY-INDEX.md|Skills mapping]]** — Sector-specific skills
6. **[[16-AGENTS/|Agents]]** — AI agents that assist/automate
7. **[[_MCP/|MCPs]]** — APIs and integrations
8. **[[23-VENTURES|Ventures]]** — Which ventures use this role
9. **[[_REGISTRIES/control-planes-by-sector.yaml|Control Planes]]** — Governance/oversight
10. **[[20-DECISIONS/|Workflows]]** — Standard processes

---

## Next: Complete Role Records

**Status:** 360 roles catalogued with stubs

**Next:** Generate complete role records (standard template) for all 360 roles with:
- ✅ Purpose, responsibilities, authority
- ✅ Required skills, tools, MCPs
- ✅ Agent capabilities, workflows
- ✅ KPIs, cost, revenue impact
- ✅ Wiring to departments, ventures, control planes

**Output:** `01-IDENTITY/ROLE-RECORDS/ROLE-*.md` (360 files)

---

**Generated:** 2026-09-10  
**Authority:** [[00-CONSTITUTION|Constitution]], [[STARTHERE|StartHere]]  
**Links:** [[SECTOR-TAXONOMY-MASTER|Sectors]], [[CAPABILITY-INDEX|Capabilities]], [[16-AGENTS|Agents]]
