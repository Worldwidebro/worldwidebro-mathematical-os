---
name: PHASE-AUTOMATIONS-MAPPING
title: PHASE-AUTOMATIONS-MAPPING
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# PHASE-AUTOMATIONS-MAPPING

**Date:** 2026-08-05 | **Purpose:** Map 28 Business Lifecycle phases to agents, skills, slash commands, automation schedules

---

## QUICK SUMMARY

| Phase | Agent | Skill | Slash Command | Schedule | Status |
|-------|-------|-------|---------------|----------|--------|
| 00-FOUNDATION | Governance | governance-setup | `/venture foundation` | One-time | 🟢 READY |
| 01-DISCOVERY | Scout | discovery-research | `/discovery` | Weekly | 🟢 READY |
| 02-RESEARCH | Analyst | market-research | `/research` | Weekly | 🟢 READY |
| 03-BUSINESS | Strategist | product-strategy | `/business-model` | Weekly | 🟡 PARTIAL |
| 04-CAPITAL | Finance | finance-plan | `/capitalize` | Monthly | 🟡 PARTIAL |
| 05-FINANCIAL | Accountant | financial-accounting | `/financial-setup` | One-time | 🟡 PARTIAL |
| 06-LEGAL | Legal | compliance-setup | `/legal-setup` | One-time | 🟡 PARTIAL |
| 07-ORGANIZATION | HR | team-building | `/organize` | One-time | ⏳ PLANNED |
| 08-INFRASTRUCTURE | DevOps | infrastructure-setup | `/infra-setup` | One-time | 🟡 PARTIAL |
| 09-ENGINEERING | Developer | code-setup | `/engineering-init` | One-time | 🟡 PARTIAL |
| 10-AGENTS | Agent Planner | agent-deployment | `/deploy-agents` | Weekly | 🟡 PARTIAL |
| 11-PRODUCTS | PM | product-discovery | `/product-spec` | Weekly | 🟡 PARTIAL |
| 12-MARKETING | Marketing | pm-marketing-growth | `/go-to-market` | Weekly | ⏳ PLANNED |
| 13-SALES | Sales | sales-automation | `/sales-activation` | Daily | ⏳ PLANNED |
| 14-OPERATIONS | Operations | execution-workflow | `/ops-start` | Daily | 🟡 PARTIAL |
| 15-SUPPORT | Support | customer-success | `/support-automation` | Daily | ⏳ PLANNED |
| 16-FINANCIAL-OPS | Finance | financial-reporting | `/finance-ops` | Daily | 🟡 PARTIAL |
| 17-OBSERVABILITY | Monitoring | observability-setup | `/observe` | Real-time | 🟡 PARTIAL |
| 18-ANALYTICS | Analytics | pm-data-analytics | `/analytics-dashboard` | Daily | 🟡 PARTIAL |
| 19-R&D | Researcher | research-experiments | `/run-experiment` | Weekly | ⏳ PLANNED |
| 20-RED TEAM | Red Team | red-team-review | `/red-team` | Weekly | ⏳ PLANNED |
| 21-KNOWLEDGE | Archivist | knowledge-capture | `/document` | Weekly | 🟡 PARTIAL |
| 22-OPTIMIZATION | Optimizer | optimization-engine | `/optimize` | Weekly | ⏳ PLANNED |
| 23-PORTFOLIO | Portfolio Manager | portfolio-optimization | `/portfolio-review` | Monthly | ❌ NOT STARTED |
| 24-PARTNERSHIPS | Partner Manager | partnership-strategy | `/find-partners` | Monthly | ❌ NOT STARTED |
| 25-SCALE | Scale Architect | scaling-design | `/scale-design` | Quarterly | ❌ NOT STARTED |
| 26-INNOVATION | Innovation Scout | innovation-pipeline | `/innovation-radar` | Quarterly | ❌ NOT STARTED |
| 27-EVOLUTION | Strategist | evolution-planning | `/pivot-analysis` | Quarterly | ❌ NOT STARTED |
| 28-EXIT | M&A Specialist | exit-strategy | `/exit-plan` | Ad-hoc | ❌ NOT STARTED |

---

## AUTOMATION SCHEDULE

### Daily (2 AM UTC)
- `/observe` — Collect metrics → Langfuse
- `/finance-ops` — Aggregate P&L → Dashboard
- `/analytics-dashboard` — Refresh KPI dashboards
- `/support-automation` — Process tickets
- `/sales-activation` — Qualify + nurture leads

### Weekly (Monday 2 AM UTC)
- `/discovery` — Market signal refresh (early-stage)
- `/research` — Research updates (validation stage)
- `/business-model` — Revenue model refresh
- `/product-spec` — Feature roadmap iteration
- `/go-to-market` — Content calendar + channel updates
- `/run-experiment` — Weekly experiment results
- `/red-team` — Assumptions challenge (pending decisions)
- `/document` — Capture learnings from past week
- `/optimize` — Bottleneck analysis

### Monthly (1st of month)
- `/capitalize` — Funding needs refresh (early-stage)
- `/portfolio-review` — Capital allocation + synergies
- `/financial-reporting` — Monthly P&L + forecast

### Quarterly
- `/scale-design` — Infrastructure scaling (mature ventures)
- `/innovation-radar` — New venture discovery
- `/pivot-analysis` — Business model evolution

---

## PM-SKILLS MARKETPLACE PLUGINS

```bash
# Install from phuryn/pm-skills

pm-toolkit                # Core toolkit (all phases)
pm-product-strategy       # Phase 03 (business models)
pm-product-discovery      # Phase 11 (products)
pm-market-research        # Phase 02 (research)
pm-data-analytics         # Phase 18 (analytics)
pm-marketing-growth       # Phase 12 (marketing)
pm-go-to-market           # Phase 12 (GTM)
pm-execution              # Phase 14 (operations)
pm-ai-shipping            # Phase 09 (engineering)
```

Each plugin exposes:
- CLI commands (e.g., `pm market-size {venture-id}`)
- Skills (loaded into agents)
- Templates (playbooks, checklists)
- Slack integrations

---

## AGENCY-AGENTS PATTERN (msitarzewski/agency-agents)

**Team structure per phase:**

```
Phase 01 (Discovery)     → Team: [Scout, Analyst, Skeptic]
                         Decision: "Pursue / Pivot / Reject"

Phase 03 (Business)      → Team: [Strategist, Finance, Red Team]
                         Decision: "Revenue model validated?"

Phase 13 (Sales)         → Team: [Sales, Support, Analytics]
                         Decision: "Pipeline healthy?"
```

Each agent has:
- **Role** (what they do)
- **Skills** (from pm-skills marketplace)
- **Tools** (MCP servers)
- **Decision authority** (what they can approve)
- **Escalation path** (when to involve human)

---

## SLASH COMMAND EXAMPLE

**User:** `/sales-activation LT-005 --targets 10`

**Execution:**
1. Parse input → venture=LT-005, targets=10
2. Check stage → LT-005 in SALES phase ✓
3. Load agent → Sales Agent
4. Load skills → sales-automation, pipeline-management
5. Execute → Pull 50 warm prospects, score top 10, generate outreach
6. Output → "Outreach queued for 10 prospects. Track in ClickUp."
7. Log → Supabase venture_activations table

---

## CURRENT READINESS

| Section | Agents Ready | Skills Assigned | Commands Wired | Coverage |
|---------|--------------|-----------------|----------------|----------|
| 00-09 | 8/10 | 7/10 | 6/10 | 70% |
| 10-18 | 5/9 | 4/9 | 2/9 | 40% |
| 19-28 | 0/10 | 0/10 | 0/10 | 0% |

---

## NEXT STEPS

**Week 1 (Aug 12):**
- [ ] Install pm-skills plugins (start with pm-marketing-growth, pm-execution)
- [ ] Wire Phase 13 → `/sales-activation` + Sales Agent
- [ ] Test first daily automation: `/finance-ops` (all ventures)

**Week 2-3 (Aug 19):**
- [ ] Wire Phase 12-15 → Marketing, Sales, Operations, Support
- [ ] Enable auto-daily loop: observe → finance → analytics
- [ ] Test red-team automation (Phase 20)

**September:**
- [ ] Wire Phase 16-22 (Financial through Optimization)
- [ ] Enable Phase 23 (Portfolio Management)
- [ ] Full automation for all 8 ventures

---

**Mapped:** 18/28 phases have agents + commands defined | 10/28 ready to activate
