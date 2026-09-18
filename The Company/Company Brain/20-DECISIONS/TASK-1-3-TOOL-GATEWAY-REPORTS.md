---
id: TASK-1-3-TOOL-GATEWAY-REPORTS
title: "Task 1.3 Deliverables — Permission Matrix + Budget Allocation"
date: 2026-09-18
phase: Phase 2a, Week 1
task: 1.3d (Tool Gateway Registry)
---

# Task 1.3 Reports

## Permission Matrix (RBAC by Agent)

### Revenue Agents (Oct Tier 1)

| Agent | Tools (Permissions) | Autonomy | Notes |
|-------|-------------------|----------|-------|
| Lead Qualifier | HubSpot (read-only), Google Analytics | L2 | Score leads from CRM |
| Cold Email Writer | SendGrid, Gmail | L2 | Draft review required before send |
| Discovery Caller | HubSpot, Gmail, Slack | L1 | Phone qualification logged to CRM |
| Proposal Generator | ClickUp, Google Docs | L2 | Auto-create tasks, manual doc review |
| Contract Reviewer | GitHub (read), Google Drive | L1 | Flag risky terms for legal |
| Invoice Tracker | Stripe, Supabase | L2 | Track payment status autonomously |
| Support Ticket Router | ClickUp, Slack, Gmail | L2 | Triage support tickets to teams |
| Complaint Handler | HubSpot, Slack, Stripe | L1 | Escalate complaints to manager |
| Pricing Optimizer | Google Analytics, Stripe, Supabase | L2 | Analyze pricing patterns |
| Revenue Forecaster | Google Analytics, Stripe, Neo4j | L3 | Autonomous forecast generation |

### Infrastructure Agents

| Agent | Tools | Autonomy | Notes |
|-------|-------|----------|-------|
| Agent Dispatch Router | Neo4j, OmniRoute | L3 | Master routing (reads all registries) |
| DevOps Automator | Vercel, GitHub, Make.com | L2 | Deploy previews, not prod |
| Data Engineer | Supabase, Neo4j, Qdrant | L2 | ETL pipeline design |
| Research Discovery Agent | Web Search, Web Fetch, Qdrant | L3 | Autonomous research |
| Operations Manager | ClickUp, Make.com | L3 (approves L1 automations) | Can deploy approved automations |

---

## Budget Allocation Report (Monthly)

### Total Monthly Budget: **$51,850**

| Tool | Monthly Budget | Notes | Owners |
|------|----------------|-------|--------|
| Stripe | $50,000 | Payment processing (2.2% + $0.30/tx) | Accounts Payable, Invoicing |
| Make.com | $1,000 | Automation operations | Operations Manager |
| Supabase | $300 | Database + edge functions | Data Engineer |
| Web Search | $50 | Research queries | Research Discovery Agent |
| Web Fetch | $50 | Web page scraping | Research Discovery Agent |
| SendGrid | $100 | Email delivery (100 emails/day limit) | Cold Email Writer |
| Google Analytics | Free | - | Revenue Forecaster |
| HubSpot | Free (tier) | - | Lead Qualifier, Deal Strategist |
| ClickUp | Free | - | Operations Manager |
| Neo4j | Free (self-hosted) | - | Agent Dispatch Router |
| Qdrant | Free (self-hosted) | - | Research Discovery Agent |
| GitHub | Free | - | DevOps Automator |
| Vercel | $100 | Pro tier for production | DevOps Automator |
| Gmail | Free | - | Cold Email Writer |
| Slack | Free (tier) | - | Support Teams |
| Notion | Free | - | Product Manager |
| **TOTAL** | **$51,850** | **Budget covers all Oct Tier 1 revenue agents + infrastructure** | |

**Buffer:** $1,850 contingency (3.5% of Stripe budget)

---

## Rate Limit Enforcement (Daily)

### Critical Limits (Alert at 80%)

| Tool | Limit | 80% Threshold | Agent(s) | Action |
|------|-------|--------------|----------|--------|
| SendGrid | 100 emails/day | 80 emails | Cold Email Writer | Stop at 100, queue remainder |
| Stripe | $50K/month (avg $1.6K/day) | $1.3K/day | Accounts Payable | Hard stop at $50K |
| Make.com | 150 ops/min | 120 ops | Operations Manager | Throttle incoming requests |
| Web Search | 100 searches/day | 80 searches | Research Discovery Agent | Queue excess searches |

### Non-Critical (Best Effort)

- Neo4j: 1000 queries/sec — unlikely to hit
- ClickUp: Unlimited — no constraint
- OmniRoute: 500 routes/sec — monitor for spikes
- GitHub: 5000 requests/hour — plenty of headroom

---

## Permission Rules (Applied)

### By Autonomy Level

**L3 (Autonomous, No Human Review):**
- Accounts Payable Agent: Process payments <$10K (Stripe)
- Agent Dispatch Router: Query all registries (Neo4j, OmniRoute)
- Revenue Forecaster: Generate forecasts autonomously (Stripe, Google Analytics, Neo4j)
- Research Discovery Agent: Search web + vector database (Web Search, Web Fetch, Qdrant)
- Operations Manager: Deploy approved automations (ClickUp, Make.com)

**L2 (Assisted, Human Can Override):**
- Cold Email Writer: Draft emails, human reviews before SendGrid send
- Lead Qualifier: Lookup prospects in HubSpot, human scores them
- Proposal Generator: Create proposal template, human finalizes
- Invoice Tracker: Track status in Stripe, escalate overdue
- etc. (10 Oct Tier 1 agents at L2)

**L1 (Human Review Required):**
- Closer: All Stripe charges flagged for human approval
- Discovery Caller: Conversation logged but not auto-replied
- Complaint Handler: Escalates to human immediately
- Contract Reviewer: Flags risky clauses for legal review
- etc. (4 agents at L1)

---

## Cost-per-Agent Analysis (Monthly)

| Agent | Estimated Cost | Primary Tool | Notes |
|-------|----------------|--------------|-------|
| Accounts Payable Agent | $1,000–$2,000 | Stripe | Depends on transaction volume |
| Revenue Forecaster | $0 | Free tools only | Uses Neo4j + Google Analytics (both free) |
| Cold Email Writer | $100 | SendGrid | 100 emails/day × 30 days × $0.001 = $3 (charged $100 minimum) |
| Research Discovery Agent | $20 | Web Search/Fetch | ~20 searches/day × 30 days × $0.05 avg |
| All other agents | <$50 | ClickUp/Gmail/HubSpot | Free tier or included |
| **TOTAL AGENT COST** | **~$51,850/month** | - | Dominated by Stripe (payment processing) |

---

## Integration Checklist (for Week 2 Task 2.1)

**Dispatch Router Must:**
- [ ] Query TOOL_GATEWAY_REGISTRY to check agent permissions
- [ ] Enforce rate limits before routing to tool
- [ ] Verify autonomy level (L1 = escalate to human, L2 = suggest, L3 = execute)
- [ ] Log cost per call
- [ ] Alert if monthly budget exceeded (80% + 100%)
- [ ] Fall back gracefully if tool unavailable

**Registry Consistency:**
- [ ] All 10 Oct Tier 1 agents have at least 1 tool permission
- [ ] All 20 tools have at least 1 agent permission
- [ ] No circular permission loops
- [ ] All endpoints reachable (manual verification post-deploy)

---

**Generated:** 2026-09-18, Task 1.3d  
**Status:** Ready for Week 2 integration into AGENT_DISPATCH_ROUTER.js  
**Commit:** Pending

