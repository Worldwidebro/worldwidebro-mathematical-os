# 04 — The Capability System

**Version:** 1.0  
**Status:** Foundation Architecture  
**Authority:** [[REALITY|REALITY.md]] + Capability Registry  

> **The Capability System is the inventory of what's possible.** Before the Orchestrator builds or buys anything, it asks: "Do we already have this capability? Who has it? What would it cost to acquire it?"

---

## What the Capability System Is

The Capability System is **not a skills marketplace.** It is the **organized inventory of: what our organization can do (agents + skills + tools + workflows + research) and what we need but don't have (gaps).**

The system answers four questions:

| Question | Answer |
|----------|--------|
| **"Can we do this?"** | Capability Registry → Yes/No/Partial |
| **"Who can do this?"** | Agent Registry → List of agents sorted by fit |
| **"What will it cost?"** | Cost model → Time + Money + Risk |
| **"What's the gap?"** | Capability Matrix → Coverage + Gaps |

---

## Core Registries

### 1. Capability Registry

**What it contains:** Definitions of all capabilities (skills, tools, workflows, research types).

```yaml
capabilities:
  CAP-501:
    name: "Sales Discovery Call Scheduling"
    category: "sales"
    description: "Schedule qualified leads for discovery calls"
    complexity: "intermediate"
    time_to_acquire: "8 hours"  # To train someone from zero
    
    agents_with_capability:
      - agent_id: "AGT-042"
        competency: "expert"
        cost_per_use: $25
        success_rate: 0.96
      - agent_id: "AGT-107"
        competency: "intermediate"
        cost_per_use: $35
        success_rate: 0.78
    
    skills_required:
      - "Prospect Research"
      - "Calendar Management"
      - "Sales Conversation"
    
    tools_required:
      - "Calendly"
      - "Prospect Database"
      - "Email Finder"
    
    ventures_using_this:
      - "LT-005"
      - "OPS-001"
    
    success_metric: "Confirmed meetings booked / time invested"
```

### 2. Agent Registry

**What it contains:** Complete inventory of 318 agents with capabilities, performance, and availability.

```yaml
agents:
  AGT-042:
    name: "Sales Lead — Discovery Calls"
    capabilities: [CAP-501, CAP-502, CAP-401]
    autonomy_level: "L2"
    success_rate: 0.96
    current_capacity: 6/10
    ventures: ["LT-005", "OPS-001", "RE-001"]
    cost_per_task: $25
    availability: "2026-09-22"
```

### 3. Skill Registry

**What it contains:** Definitions of discrete skills (sales, research, analysis, coding, etc.)

```yaml
skills:
  SKL-501:
    name: "Sales Discovery Call Scheduling"
    level_required: "intermediate"
    prerequisite_skills: ["Prospect Research", "Sales Conversation"]
    
    agents_with_skill:
      - agent_id: "AGT-042", competency: "expert"
      - agent_id: "AGT-107", competency: "intermediate"
    
    training_resources:
      - url: "repo: worldwidebro/sales-scripts"
      - url: "video: discovery-call-framework"
```

### 4. Tool Registry

**What it contains:** Technical tools and their capabilities, APIs, and limitations.

```yaml
tools:
  TOL-201:
    name: "Calendly Integration"
    purpose: "Schedule meetings with automatic reminders"
    api_endpoint: "https://calendly.com/api"
    rate_limit: "1000 requests/hour"
    cost: "free (up to 100 bookings/month)"
    
    used_by_agents:
      - "AGT-042" (primary)
      - "AGT-107" (secondary)
    
    integrated_with:
      - "Gmail"
      - "Salesforce"
      - "Slack"
```

### 5. Workflow Registry

**What it contains:** Repeatable processes (not one-time tasks).

```yaml
workflows:
  WFL-101:
    name: "New Venture Launch Research"
    objective: "Understand market, competitors, regulatory, financial viability"
    
    stages:
      - stage_1: Market Research (5 days)
      - stage_2: Competitor Analysis (3 days)
      - stage_3: Regulatory Research (2 days)
      - stage_4: Financial Modeling (3 days)
      - stage_5: Synthesis (1 day)
    
    agents_required: 5
    estimated_cost: $2500
    estimated_time: 14 days
    
    past_executions:
      - date: "2026-09-01", venture: "LT-005", cost: $2400, time: 13 days, quality: "good"
      - date: "2026-08-15", venture: "OPS-001", cost: $2600, time: 15 days, quality: "excellent"
    
    success_metrics:
      - "Research report written"
      - "Validated with 3+ external sources"
      - "Financial model reviewed by CFO"
```

### 6. Repository Registry

**What it contains:** All 1,740 repos with dependencies, code status, and which ventures use them.

```yaml
repositories:
  repo_id: "worldwidebro/sales-scripts"
    type: "code"
    description: "Sales scripts and conversation frameworks"
    language: "python"
    
    used_by_agents:
      - "AGT-042"
      - "AGT-107"
    
    used_by_ventures:
      - "LT-005"
      - "OPS-001"
    
    dependencies: ["requests", "langchain"]
    last_updated: "2026-09-15"
    code_status: "production"
    tests: "95% coverage"
```

---

## The Capability Matrix

The Matrix maps:

- **Rows:** All business functions needed (sales, operations, research, analysis, etc.)
- **Columns:** What we have vs. what we need
- **Cells:** Coverage %, gaps, and acquisition cost

```
                    LT-005      OPS-001     RE-001      GAPS
Sales Discovery     ✅ 100%     ✅ 100%     ❌ 40%      Need agent for RE-001
Prospect Research   ✅ 95%      ✅ 90%      ⚠️  70%      Missing real estate prospect DB
Market Analysis     ✅ 100%     ✅ 95%      ⚠️  60%      Need real estate market expertise
Regulatory          ✅ 95%      ⚠️ 70%      ❌ 20%      OPS-001 needs healthcare expert
Financial Modeling  ⚠️ 80%      ✅ 85%      ✅ 90%      LT-005 needs venture finance help
Revenue Operations  ✅ 100%     ✅ 100%     ⚠️ 75%      RE-001 needs deal closing automation
```

**Interpretation:**
- ✅ = Covered (>90%)
- ⚠️ = Partial (50-90%)
- ❌ = Missing (<50%)

**Action:** For every gap, decide: **Build / Buy / Partner / Train / Defer**

---

## Acquisition Strategies

### Strategy 1: Use Existing Agent

```
Need: "Charlotte market research"
  ├─ Capability Registry → CAP-XXX exists
  ├─ Agent Registry → AGT-107 has it (expert)
  ├─ Cost: $400
  ├─ Time: 5 days
  └─ Action: Delegate to AGT-107 immediately
```

**Time to capability:** 0 (already have it)  
**Cost:** $400  
**Risk:** None

### Strategy 2: Train Existing Agent (New Skill)

```
Need: "Real estate financial analysis"
  ├─ Capability Registry → CAP-FIN-RE doesn't exist
  ├─ Agent Registry → AGT-053 has general financial skills
  ├─ Can learn? → Yes (prerequisite skills present)
  ├─ Cost: $3K (training materials + 40 hours @ $75/hr)
  ├─ Time: 2 weeks
  └─ Action: Send AGT-053 to training
```

**Time to capability:** 2 weeks  
**Cost:** $3,000  
**Risk:** Low (has prerequisites)

### Strategy 3: Hire New Agent

```
Need: "Real estate deal closing automation"
  ├─ Capability Registry → CAP-DEAL-AUTOMATION doesn't exist
  ├─ Agent Registry → No agent has it
  ├─ Can train? → Maybe, but very specialized
  ├─ Cost: $8K (recruitment + onboarding + training)
  ├─ Time: 6 weeks
  └─ Action: Post job description
```

**Time to capability:** 6 weeks  
**Cost:** $8,000  
**Risk:** Medium (new hire performance unknown)

### Strategy 4: Partner / Buy

```
Need: "Real estate title search automation"
  ├─ Capability Registry → Doesn't exist internally
  ├─ Agent Registry → No one has it
  ├─ Can build? → Would take 12 weeks + $15K
  ├─ Market option: Use TitleTech API ($100/search, 5-min turnaround)
  └─ Action: Integrate TitleTech API
```

**Time to capability:** 1 week (integration)  
**Cost:** $100 per use  
**Risk:** Low (vendor-managed)

### Strategy 5: Defer

```
Need: "Advanced AI agent orchestration research"
  ├─ Capability Registry → Doesn't exist
  ├─ Priority: Low (nice-to-have, not blocking revenue)
  ├─ Cost: High (would need specialized researcher)
  ├─ Urgency: None (can wait 3 months)
  └─ Action: Add to roadmap, revisit in Q4
```

**Time to capability:** Deferred  
**Cost:** $0 now, TBD later  
**Risk:** Low (no blocker)

---

## Gap Analysis Workflow

```
BUSINESS OBJECTIVE
    ↓
REQUIRED CAPABILITIES
    ↓
CAPABILITY REGISTRY: Do we have it?
    ├─ YES (>90%) → Use existing
    ├─ PARTIAL (50-90%) → Improve existing + gap
    └─ NO (<50%) → Build / Buy / Partner / Train / Defer
    ↓
DECISION MATRIX
    ├─ Cost estimate (training vs. hiring vs. buying)
    ├─ Time estimate (when do we need it)
    ├─ Risk assessment (success probability)
    ├─ Strategic fit (does this align with roadmap)
    └─ Priority (business impact vs. other work)
    ↓
ACQUISITION PLAN
    └─ Execute selected strategy
```

---

## Capability Scoring

When deciding whether to build, buy, or train a capability:

```
CAPABILITY: "Real estate deal closing automation"

Build In-House:
  Time: 12 weeks
  Cost: $15,000
  Risk: 70% success (new tech, unproven)
  Maintenance: Ongoing (bugs, updates)
  Score: 4/10 (high risk, high cost, long timeline)

Buy SaaS (TitleTech):
  Time: 1 week (integration)
  Cost: $100/use ($2,000/month estimated)
  Risk: 20% (vendor-managed)
  Maintenance: None (vendor owns)
  Score: 8/10 (low risk, low upfront cost, proven)

Partner with Real Estate Agent:
  Time: 3 days (negotiation)
  Cost: $50/deal referral fee
  Risk: 40% (manual process, slower)
  Maintenance: Relationship management
  Score: 6/10 (medium risk, pay-for-use model)

Train Existing Agent:
  Time: 4 weeks
  Cost: $4,000
  Risk: 60% (agent competency unknown)
  Maintenance: Refresh training periodically
  Score: 5/10 (medium risk, medium cost)

RECOMMENDATION: Buy SaaS (TitleTech). Fastest to capability, lowest risk, predictable cost.
```

---

## Managing the Capability Registry

### Refresh Cycle
- **Daily:** Update agent capacity and success rates (from task execution)
- **Weekly:** Update workflow performance (from completion reports)
- **Monthly:** Audit capability gaps vs. business objectives
- **Quarterly:** Review acquisition strategies and ROI

### Maintenance Tasks
- Remove capabilities no one has/uses
- Consolidate redundant capabilities
- Update cost estimates based on actual execution
- Mark capabilities for improvement or deprecation

---

## References

- [[COMPANY-BRAIN|01-COMPANY-BRAIN.md]] — Where capabilities are stored and discovered
- [[MASTER-ORCHESTRATOR|02-MASTER-ORCHESTRATOR.md]] — How Orchestrator queries capabilities
- [[AGENT-SYSTEM|03-AGENT-SYSTEM.md]] — Who carries capabilities
- [[EXECUTION-LOOP|05-EXECUTION-LOOP.md]] — How to handle "capability not found"

---

**Next:** Read [[EXECUTION-LOOP|05-EXECUTION-LOOP.md]] to understand the complete flow from objective to outcome.

**Last Updated:** 2026-09-18 | **Architecture Version:** 1.0
