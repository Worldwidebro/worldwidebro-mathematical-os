---
id: AGENTS-DISCOVERY-GUIDE
title: "Agents Discovery & Invocation Guide — How to Find & Use All 318 Agents"
description: "Wiki links + query patterns + dispatch suggestions for every agent type"
updated: 2026-09-17
---

[[STARTHERE]] | [[_MCP/SYSTEMS-INTEGRATION-MASTER]] | [[_REGISTRIES/CANONICAL/AGENTS_INVENTORY_318.yaml]]

# Agents Discovery & Invocation Guide

**Goal:** Make every one of 318 agents discoverable, queryable, and invokable based on task type.

---

## HOW TO FIND AN AGENT

### Method 1: By Task Type (Query AGENT_DISPATCH_ROUTER.js)

```
Your task: "Write a cold email to 100 prospects"

SYSTEM RESPONSE:
  1. Parse intent → Logic layers: LOGIC-019 (INFORMATION), LOGIC-049 (COGNITION)
  2. Query AGENT_REGISTRY: agents supporting LOGIC-019 + LOGIC-049
  3. Candidates: Cold Email Writer, Email Strategist, Marketing Specialist
  4. Rank by: trustworthiness (0.89), success rate (87%), cost ($0.50 per email)
  5. Recommend: [[Cold Email Writer]] (top match)
```

### Method 2: By Domain (Wiki Links)

**Business Strategist:** [[business-strategist.md]]  
**Chief Financial Officer:** [[chief-financial-officer.md]]  
**Sales Coach:** [[sales-coach.md]]  

Navigate to `[[SECTOR_X]]` → Find business problem → Jump to agent recommendation.

### Method 3: By Deployment Phase

**October 2026 (Ready Now):**
- [[Lead Qualifier]] - Score inbound leads 1-100
- [[Cold Email Writer]] - Personalize outreach
- [[Discovery Caller]] - Qualify over phone
- [[Proposal Generator]] - Create customized proposals
- [[Contract Reviewer]] - Flag risky terms

**Full list:** [[_REGISTRIES/CANONICAL/AGENTS_INVENTORY_318.yaml|Agents Inventory]]

---

## AGENT CATEGORIES & WIKI LINKS

### ACADEMIC AGENTS (6)
Purpose: Research, analysis, domain expertise

| Agent | Wiki Link | Best For | Autonomy |
|-------|-----------|----------|----------|
| Academic Anthropologist | [[academic-anthropologist.md]] | Cultural system analysis | L1 |
| Academic Geographer | [[academic-geographer.md]] | Spatial analysis, climate research | L1 |
| Academic Historian | [[academic-historian.md]] | Historical context, timeline analysis | L1 |
| Academic Narratologist | [[academic-narratologist.md]] | Story structure, narrative design | L1 |
| Academic Psychologist | [[academic-psychologist.md]] | User behavior, motivation modeling | L1 |
| Academic Statistician | [[academic-statistician.md]] | Statistical analysis, experimental design | L1 |

**When to invoke:** Analyzing complex domains, validating research, understanding patterns

---

### BUSINESS AGENTS (8)
Purpose: Strategy, finance, operations, change management

| Agent | Wiki Link | Best For | Autonomy |
|-------|-----------|----------|----------|
| Business Strategist | [[business-strategist.md]] | Competitive analysis, market strategy | L1 |
| Chief Financial Officer | [[chief-financial-officer.md]] | Capital allocation, financial planning | L1 |
| Change Management Consultant | [[change-management-consultant.md]] | Organizational transformation | L1 |
| Accounts Payable Agent | [[accounts-payable-agent.md]] | Payment processing (crypto/fiat) | L3 |
| Economy Designer | [[economy-designer.md]] | Monetization models, currency systems | L2 |
| Automation Governance Architect | [[automation-governance-architect.md]] | Business automation governance | L1 |
| Corporate Training Designer | [[corporate-training-designer.md]] | Curriculum, training programs | L1 |
| Operations Manager | [[operations-manager.md]] | Process optimization, efficiency | L2 |

**When to invoke:** Strategic decisions, financial planning, organizational changes, automations

---

### DESIGN AGENTS (10)
Purpose: Visual design, UX, branding, accessibility

| Agent | Wiki Link | Best For | Autonomy |
|-------|-----------|----------|----------|
| UI Designer | [[design-ui-designer.md]] | Visual design, component systems | L2 |
| UX Architect | [[design-ux-architect.md]] | UX strategy, user flows | L2 |
| UX Researcher | [[design-ux-researcher.md]] | User testing, behavior analysis | L2 |
| Brand Guardian | [[design-brand-guardian.md]] | Brand consistency, identity | L1 |
| Visual Storyteller | [[design-visual-storyteller.md]] | Visual narratives, content | L2 |
| Persona Walkthrough Specialist | [[design-persona-walkthrough.md]] | User scenario analysis, CRO | L2 |
| Image Prompt Engineer | [[design-image-prompt-engineer.md]] | AI image generation optimization | L2 |
| Inclusive Visuals Specialist | [[design-inclusive-visuals-specialist.md]] | Culturally accurate imagery | L2 |
| UI Finish-Gate Reviewer | [[design-ui-finish-gate-reviewer.md]] | Quality gate before ship | L1 |
| Whimsy Injector | [[design-whimsy-injector.md]] | Brand personality, delight | L2 |

**When to invoke:** Product design, brand decisions, UX research, visual strategy

---

### ENGINEERING AGENTS (80+)
Purpose: Code, infrastructure, ML, databases, security

**Subcategories:**
- **Backend & Architecture:** [[engineering-backend-architect.md]], [[engineering-software-architect.md]], [[engineering-database-optimizer.md]], [[engineering-database-reliability-engineer.md]]
- **Frontend & UI:** [[engineering-frontend-developer.md]], [[engineering-mobile-app-builder.md]], [[engineering-desktop-app-engineer.md]]
- **DevOps & Infrastructure:** [[engineering-devops-automator.md]], [[engineering-cloud-security-architect.md]], [[engineering-iot-fleet-engineer.md]]
- **AI & ML:** [[engineering-ai-engineer.md]], [[engineering-llm-post-training-engineer.md]], [[engineering-prompt-engineer.md]], [[engineering-rag-pipeline-engineer.md]]
- **Security:** [[engineering-security-auditor.md]], [[engineering-senior-secops-engineer.md]], [[engineering-privacy-engineer.md]]
- **Specialized:** [[engineering-solidity-smart-contract-engineer.md]], [[engineering-webassembly-engineer.md]], [[engineering-game-audio-engineer.md]]

**When to invoke:** Building software, optimizing infrastructure, improving security, adding AI capabilities

---

### RESEARCH & INTELLIGENCE AGENTS (20+)
Purpose: Research, knowledge synthesis, evidence evaluation

| Agent | Wiki Link | Best For | Autonomy |
|-------|-----------|----------|----------|
| Research Synthesist | [[research-synthesist.md]] | Literature review, evidence synthesis | L2 |
| Research Discovery Agent | [[research-discovery-agent.md]] | Finding relevant papers | L3 |
| Evidence Collector | [[evidence-collector.md]] | Quality evidence gathering | L2 |
| Model QA Specialist | [[model-qa-specialist.md]] | ML model evaluation | L1 |
| Statistical Analysis | [[statistical-analysis.md]] | Data analysis, hypothesis testing | L2 |

**When to invoke:** Research analysis, capability evaluation, evidence validation, academic synthesis

---

### SALES & REVENUE AGENTS (15+)
Purpose: Lead generation, sales, deal closing, customer success

| Agent | Wiki Link | When to Invoke | Autonomy |
|-------|-----------|---------|----------|
| Lead Qualifier | [[lead-qualifier.md]] | Score inbound leads (1-100) | L2 |
| Cold Email Writer | [[cold-email-writer.md]] | Personalized outreach at scale | L2 |
| Discovery Caller | [[discovery-caller.md]] | Qualify prospects over phone | L1 |
| Sales Coach | [[sales-coach.md]] | Sales rep development | L1 |
| Deal Strategist | [[deal-strategist.md]] | Complex B2B deal strategy | L1 |
| Account Strategist | [[account-strategist.md]] | Land-and-expand strategy | L1 |
| Customer Success Manager | [[customer-success-manager.md]] | Account health, retention | L2 |
| Customer Service | [[customer-service.md]] | Support, issue resolution | L2 |
| Offer & Lead Gen Strategist | [[offer-lead-gen-strategist.md]] | Lead magnet creation | L1 |
| Pricing Analyst | [[pricing-analyst.md]] | Price optimization | L2 |
| Revenue Operations Analyst | [[revenue-operations-analyst.md]] | Pipeline health, forecasting | L2 |

**When to invoke:** Every step of revenue cycle (lead gen → close → success)

---

### SPECIALIZED MARKET AGENTS (20+)
Purpose: China market, XR/spatial, blockchain, healthcare, regulatory

**China Market Specialists:**
- [[marketing-douyin-strategist.md]] - Short video content
- [[marketing-xiaohongshu-specialist.md]] - Lifestyle content
- [[marketing-weibo-strategist.md]] - Public discourse
- [[marketing-bilibili-strategist.md]] - Video community
- [[china-ecommerce-operator.md]] - Taobao/Tmall/JD operations
- [[china-market-localization-strategist.md]] - Trend → market strategy
- [[wechat-official-account-manager.md]] - OA content strategy
- [[wechat-mini-program-developer.md]] - Mini program dev
- [[government-digital-presales-consultant.md]] - ToG market

**XR/Spatial/Gaming:**
- [[xr-immersive-developer.md]] - WebXR/AR/VR apps
- [[xr-interface-architect.md]] - Spatial interaction design
- [[xr-cockpit-interaction-specialist.md]] - Cockpit systems
- [[unity-architect.md]] - Unity architecture
- [[godot-gameplay-scripter.md]] - Godot scripting
- [[unreal-systems-engineer.md]] - Unreal systems
- [[game-designer.md]] - Game design, mechanics
- [[game-audio-engineer.md]] - Interactive audio

**Blockchain/Finance:**
- [[solidity-smart-contract-engineer.md]] - Solidity development
- [[trading-os-repository-registry.md]] - Trading systems
- [[payments-billing-engineer.md]] - Payment processing

**Healthcare/Regulatory:**
- [[healthcare-reviewer.md]] - Clinical safety audit
- [[healthcare-compliance-specialist.md]] - Healthcare compliance
- [[data-privacy-officer.md]] - GDPR/CCPA/privacy
- [[legal-compliance-checker.md]] - Legal compliance

**When to invoke:** Entering new markets, regulatory requirements, specialized domains

---

## DISPATCH ROUTER LOGIC

When task arrives → AGENT_DISPATCH_ROUTER.js flow:

```
1. CLASSIFY TASK
   Input: "Write 50 personalized cold emails to prospects"
   → Logic layers: LOGIC-019 (INFORMATION), LOGIC-049 (COGNITION)
   → Domain: 30-REVENUE
   → Category: Sales/Marketing

2. QUERY REGISTRIES
   AGENT_REGISTRY.yaml:
     - Find agents supporting LOGIC-019 + LOGIC-049
     - Filter by domain 30-REVENUE
     - Result: 5 candidate agents
   
   SKILL_REGISTRY.yaml:
     - Skills needed: email-writing, personalization, outreach
     - Which agents have these skills?
   
   TOOL_GATEWAY_REGISTRY.yaml:
     - What tools do top candidates need?
     - Permissions granted? Cost? Rate limits?

3. RANK CANDIDATES
   Cold Email Writer:     score=0.92 (trustworthiness: 0.89, success: 87%, cost: $0.50/email)
   Email Strategist:      score=0.85 (trustworthiness: 0.82, success: 80%, cost: $0.75/email)
   Offer & Lead Gen:      score=0.78 (trustworthiness: 0.76, success: 75%, cost: $1.00/email)
   Sales Coach:           score=0.65 (not ideal for cold email)
   Personification Agent: score=0.60 (wrong domain)

4. AUTONOMY GATE
   Top candidate: Cold Email Writer (L2 = Assisted)
   → Human review required before sending
   → Cost tracking: $0.50 × 50 = $25 total
   → Projected revenue: 50 emails × 8% response = 4 replies × $2.5K deal = $10K

5. SUGGEST TO USER
   ✅ Recommended: [[Cold Email Writer]]
   • Rank: #1 (score 0.92)
   • Autonomy: L2 (human review)
   • Estimated cost: $25
   • Projected revenue: $10K (5K ROI)
   • Confidence: 87%
   
   Alternative: [[Email Strategist]] (score 0.85, higher cost)

6. EXECUTE
   → Agent receives prospect data
   → Generates 50 personalized drafts
   → Stages for human review
   → On approval: sends + tracks
```

---

## WHEN TO INVOKE AGENTS (By Trigger)

### MORNING (Operational Tasks)
- **Lead Qualifier** — Review overnight inbound leads
- **Revenue Forecaster** — Daily revenue prediction + variance
- **Social Media Manager** — Schedule today's posts
- **Invoice Tracker** — Flag unpaid invoices

### SALES CYCLE (Revenue Process)
1. **Cold Email Writer** → Outreach at scale
2. **Discovery Caller** → Qualify hot prospects
3. **Proposal Generator** → Create customized proposal
4. **Closer** → Send contract, handle objections
5. **Accounts Payable Agent** → Process payment

### PRODUCT DEVELOPMENT (Building)
1. **UX Researcher** → Validate user needs
2. **Product Manager** → Roadmap + prioritization
3. **Backend Architect** → System design
4. **Frontend Developer** → UI implementation
5. **QA Tester** → Test suite coverage
6. **Security Auditor** → Code security review

### CUSTOMER SUCCESS (Retention)
1. **Customer Success Manager** → Health scoring
2. **Churn Prediction Agent** → Flag at-risk customers
3. **Customer Service** → Issue resolution
4. **Upsell Recommender** → Expansion opportunities

### STRATEGIC DECISIONS (Quarterly)
1. **Business Strategist** → Market analysis, positioning
2. **Chief Financial Officer** → Capital allocation
3. **Change Management Consultant** → Transformation planning
4. **Organizational Psychologist** → Team dynamics

### RESEARCH (Knowledge)
1. **Research Discovery Agent** → Find relevant papers
2. **Research Synthesist** → Connect findings
3. **Academic [domain] Agent** → Deep domain expertise
4. **Evidence Collector** → Validate claims

---

## REVENUE ATTRIBUTION (How Agents Drive $)

Every agent action gets tracked → revenue traced back:

```
Cold Email Writer
├─ Generated: 50 emails
├─ Cost: $25
├─ Responses: 4 replies
├─ Meetings booked: 2 (via Discovery Caller)
├─ Proposals sent: 2 (via Proposal Generator)
├─ Deals closed: 1 (via Closer)
├─ Revenue: $2.5K
└─ Revenue attribution: $2.5K ← Cold Email Writer

Total attribution: $2.5K revenue from $25 investment
ROI: 100x (or $2.5K/$25 = 100:1)
```

This tracking enables:
- ✅ Know which agents generate most revenue
- ✅ Allocate budget to highest-ROI agents
- ✅ Validate autonomy level (L1 safe, L3 high risk, balance reward/risk)
- ✅ Continuous improvement (which agents keep getting better)

---

## COMPLETE AGENT INDEX

All 318 agents in one place: [[_REGISTRIES/CANONICAL/AGENTS_INVENTORY_318.yaml|Complete Agents Inventory]]

**By category:**
- Academic (6)
- Business (8)
- Design (10)
- Engineering (80+)
- Research (20+)
- Sales/Revenue (15+)
- Support/Compliance (8+)
- China Market (20+)
- Gaming/3D (15+)
- Specialized (50+)
- Workflow (4)

---

## NEXT: MAKE AGENTS INVOKABLE

This guide shows WHERE agents are. Phase 2a (Oct 2026) makes them INVOKABLE:

1. **Tag all 318 agents** in AGENT_REGISTRY.yaml (auto-generate from `.md` files)
2. **Map to logic layers** (what logics does each agent execute?)
3. **Map to capabilities** (what can each agent help with?)
4. **Deploy dispatch router** (task → ranked agents)
5. **Wire revenue tracking** (outcome → $value → agent attribution)

**Result:** Type `@lead-qualifier "Score these 100 inbound leads"` → Agent tagged, ranked, deployed, revenue tracked.

---

**Reference:** [[_MCP/REAL-AGENT-BLUEPRINT.md|Real Agent Blueprint]] — Why 2 agents work + why 273 don't (yet) + how to fix it

