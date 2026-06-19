# Worldwidebro Unified Operating System
## Master Folder Structure (Civilization OS + Venture Nation OS Merged)

**Status**: Live | **Ventures**: 712 | **Updated**: 2026-06-01 | **Template Version**: 2.0

---

## Core Principle
Every venture follows the same 15-folder structure, regardless of type (SaaS, Operations, Construction, etc.). This enables:
- **Parallel execution** across all 712 ventures
- **Consistent automation** (agents, workflows, syncs)
- **Real-time dashboards** pulling from the same schema
- **Rapid scaling** to 1000+ ventures without structural changes

---

## Layer 1: Command & Control (Unified View)

```
01_CEO_COMMAND_CENTER/
├── Goals/
│   ├── quarterly-goals.json
│   ├── annual-goals.json
│   └── 90-day-plan.md
├── KPIs/
│   ├── financial-kpis.json (revenue, burn, cash runway)
│   ├── operational-kpis.json (quote cycle, win rate, equipment ROI)
│   └── venture-kpis.json (by-venture MRR, growth rate, stage)
├── Dashboards/
│   ├── main-dashboard.json (unified P&L, cash, pipeline)
│   ├── ventures-dashboard.json (all 712 ventures status)
│   ├── cash-flow-dashboard.json (by-venture, by-opco)
│   ├── equipment-intelligence.json (pricing, utilization, ROI)
│   └── [synced from 10_VENTURES real-time]
├── Weekly_Reviews/
│   ├── 2026-06-01/
│   │   ├── summary.md
│   │   ├── blockers.json
│   │   └── metrics-snapshot.json
│   └── templates/review-template.md
├── Strategic_Planning/
│   ├── roadmap.json (by-opco, by-venture-type)
│   ├── scenarios.json (bull/base/bear cases)
│   └── M&A-pipeline.json (targets, valuations)
└── Integrations/
    ├── slack-config.json
    ├── supabase-config.json
    ├── obsidian-config.json
    ├── clickup-config.json
    └── n8n-config.json
```

---

## Layer 2: Go-to-Market (Unified Execution)

```
02_MARKETING/
├── Brand_Guides/
│   ├── logo/ (Worldwidebro + OPCO brands)
│   ├── voice.md (tone, messaging, pillars)
│   └── visual-system.json (colors, fonts, guidelines)
├── Content_Calendar/
│   ├── 2026-06.json
│   ├── 2026-05.json
│   └── templates/content-template.md
├── Reels/
│   ├── script-templates/
│   ├── produced-reels/
│   │   ├── hrms-launch-001.json
│   │   ├── hvac-testimonial-001.json
│   │   └── [by venture]
│   └── performance-metrics.json (views, engagement, conversion)
├── Commercials/
│   ├── script-library/
│   └── produced-videos/ (by-venture, by-campaign)
├── Scripts/
│   ├── sales-scripts/ (by-vertical)
│   ├── pitch-scripts/ (by-venture-type)
│   └── demo-scripts/
├── Ad_Creatives/
│   ├── by-platform/ (LinkedIn, YouTube, TikTok, etc.)
│   ├── by-campaign/ (hrms-launch, graphify-beta, hvac-summer)
│   └── performance.json (CPM, CTR, conversion by platform)
└── Campaigns/
    ├── ent-campaign-001-hrms-launch/
    ├── ops-campaign-001-hvac-summer/
    └── [by venture launch phase]

03_SALES/
├── Lead_Lists/
│   ├── by-venture/
│   │   ├── ent-venture-001-hrms.csv
│   │   ├── ops-venture-001-hvac.csv
│   │   └── [all 712 ventures]
│   ├── by-vertical/ (SaaS, HVAC, Electrical, etc.)
│   └── leads.json (id, email, company, source, assigned_venture)
├── CRM_Exports/
│   ├── clickup-sync/ (deal stages, pipeline value)
│   ├── supabase-sync/ (real-time contact data)
│   └── templates/deal-template.json
├── Estimates/
│   ├── templates/ (by-venture-type)
│   ├── draft/ (by-date)
│   └── sent/ (by-date, by-venture)
├── Proposals/
│   ├── templates/
│   ├── draft/
│   └── sent/
├── Contracts/
│   ├── templates/
│   ├── signed/
│   └── active/ (by-venture, renewal dates)
└── Invoices/
    ├── 2026-06/
    ├── 2026-05/
    └── templates/
```

---

## Layer 3: Operational Intelligence (Cross-Venture Synergy)

```
04_EQUIPMENT_INTELLIGENCE/
├── HVAC/
│   ├── Tools/
│   │   ├── prices.json (SKU, vendor, price, date_updated: YYYY-MM-DD)
│   │   ├── vendors.json (vendor_name, contact, lead_time, payment_terms)
│   │   └── specs.json (equipment_id, capacity, efficiency, cost)
│   ├── Equipment/
│   │   ├── industrial.json (large systems, commercial units)
│   │   ├── residential.json (residential units, packages)
│   │   └── commercial.json (mid-market systems)
│   ├── Price_Comparisons/
│   │   ├── 2026-06.json (tracker for historical trending)
│   │   ├── 2026-05.json
│   │   └── historical/ (archive by quarter)
│   ├── Used_Equipment/
│   │   └── listings.json (source, price, condition, location)
│   └── ROI_Analysis/
│       └── by-venture.json (payback period, NPV)
│
├── Electrical/
│   ├── Tools/ (similar to HVAC)
│   ├── Equipment/
│   ├── Price_Comparisons/
│   ├── Used_Equipment/
│   └── ROI_Analysis/
│
├── Low_Voltage/
├── General_Contracting/
├── Pressure_Washing/
├── Media_Equipment/
│   ├── cameras.json (current inventory)
│   ├── lighting.json (studio + field)
│   └── audio.json (mics, recorders, mixers)
├── Office_Equipment/
│   └── current-inventory.json
└── Vehicles/
    ├── current-fleet.json (id, make, model, purchase_date, mileage)
    ├── purchase-history.json (acquisition cost, maintenance cost, ROI)
    └── maintenance-schedule.json

05_QUOTES_ESTIMATES/
├── Blueprint_Templates/
│   ├── HVAC-residential.json
│   ├── HVAC-commercial.json
│   ├── Electrical-service.json
│   └── [by-service-type]
├── Labor_Rates/
│   ├── hvac-rates.json (rate_tier, hourly_cost, date_effective: YYYY-MM-DD)
│   ├── electrical-rates.json
│   ├── general-rates.json
│   └── by-region.json
├── Material_Pricing/
│   ├── hvac-materials.json
│   ├── electrical-materials.json
│   └── general-materials.json
├── Markup_Rules/
│   └── pricing-matrix.json (service_type, markup_percent, min_profit_margin)
├── Proposal_Templates/
│   ├── service-proposal.json
│   ├── product-proposal.json
│   └── consulting-proposal.json
├── Contract_Templates/
│   ├── service-contract.md
│   ├── product-contract.md
│   └── maintenance-contract.md
├── Service_Quotes/
│   ├── HVAC/
│   │   ├── 2026-06/ (quote_id, customer, amount, date_created: YYYY-MM-DD, status)
│   │   ├── 2026-05/
│   │   └── historical/
│   ├── Electrical/
│   ├── Low_Voltage/
│   └── General_Contracting/
└── Completed_Estimates/
    ├── won/ (by-date, by-venture)
    │   └── 2026-06/ (closed_date, final_amount, project_id)
    └── lost/ (lost_reason, lost_date, recovery_notes)
```

---

## Layer 4: Process & Automation (Scaled Operations)

```
06_SOPs/
├── Sales/
│   ├── lead-qualification.md (criteria, time-to-response, escalation rules)
│   ├── discovery-call.md (agenda, discovery questions, next-steps checklist)
│   ├── proposal-process.md (template selection, customization, pricing logic)
│   └── closing.md (negotiation tactics, contract-signing flow, onboarding kickoff)
├── Marketing/
│   ├── content-creation.md (process, approval workflow, distribution)
│   ├── campaign-launch.md (timeline, stakeholders, success metrics)
│   ├── performance-review.md (weekly cadence, metrics dashboard, optimization)
│   └── asset-management.md (tagging, versioning, archival)
├── Operations/
│   ├── project-kickoff.md (scope, timeline, team, communication plan)
│   ├── execution.md (daily standup, status tracking, risk management)
│   ├── quality-check.md (acceptance criteria, testing, customer approval)
│   └── handoff.md (documentation, warranty terms, follow-up schedule)
├── Finance/
│   ├── invoicing.md (timing, payment terms, tracking)
│   ├── payment-processing.md (collection, disputes, reconciliation)
│   ├── reconciliation.md (monthly close, variance analysis)
│   └── reporting.md (dashboard updates, variance reporting, forecasting)
├── Customer_Service/
│   ├── onboarding.md
│   ├── support-ticket.md (triage, escalation, resolution SLA)
│   ├── escalation.md
│   └── renewal.md (outreach, upsell, retention)
└── Technical/
    ├── deployment.md
    ├── incident-response.md
    ├── security.md
    └── maintenance.md

07_AUTOMATIONS/
├── n8n/
│   ├── workflows/
│   │   ├── lead-enrichment.json (trigger: new lead → enrich data → sync CRM)
│   │   ├── quote-generation.json (trigger: sales request → build proposal → send email)
│   │   ├── data-sync.json (trigger: hourly → sync Supabase → Google Sheets → Slack)
│   │   └── reporting.json (trigger: weekly → aggregate metrics → dashboard update)
│   ├── triggers/ (webhook, schedule, form submission)
│   └── integrations/ (Slack, Gmail, Supabase, Click Up, Stripe)
├── Apify/
│   ├── scrapers/
│   │   ├── competitor-monitor.json (run: daily, track competitor pricing/features)
│   │   ├── pricing-tracker.json (run: daily, sync to 04_EQUIPMENT_INTELLIGENCE)
│   │   └── lead-extractor.json (run: on-demand, extract from LinkedIn, ZoomInfo)
│   └── data-pipelines/
├── AI_Agents/
│   ├── scheduler.json (assigns tasks, tracks deadlines, sends reminders)
│   ├── analyzer.json (analyzes sales trends, equipment ROI, forecasting)
│   ├── executor.json (executes workflows, monitors outcomes, escalates failures)
│   └── venture-agents/ (specialized per venture type)
│       ├── hrms-agent.json (customer success, feature prioritization, onboarding)
│       ├── graphify-agent.json (data quality, query optimization, customer support)
│       ├── hvac-agent.json (lead qualification, quote generation, project scheduling)
│       └── [all venture types]
├── Workflows/
│   ├── lead-enrichment.json
│   ├── quote-generation.json
│   ├── data-sync.json
│   └── reporting.json
└── API_Documentation/
    ├── internal-apis.md
    ├── external-integrations.md
    └── webhook-specs.json
```

---

## Layer 5: Intelligence (Cross-Venture Learning)

```
08_RESEARCH/
├── Competitors/
│   ├── by-vertical/
│   │   ├── saas/ (HRMS, GraphQL tools, Pitch tools, etc.)
│   │   ├── hvac/ (local installers, national chains, tech integrators)
│   │   └── [all verticals]
│   └── competitive-analysis.json (competitor_name, pricing, features, market_position)
├── Market_Research/
│   ├── by-region/ (ZIP-code-level TAM for service businesses)
│   ├── by-vertical/ (market size, growth rate, margin benchmarks)
│   └── market-size.json
├── Industry_Reports/
│   ├── saas-trends.md (growth, consolidation, unit economics)
│   ├── service-industry.md (labor costs, equipment trends, seasonality)
│   └── equipment-trends.md
├── Technology_Research/
│   ├── ai-tools.md (for ops, sales, marketing automation)
│   ├── automation-platforms.md (n8n, Zapier, integration options)
│   └── integration-options.json
├── Equipment_Research/
│   ├── hvac-equipment.md
│   ├── electrical-equipment.md
│   └── emerging-tech.md
└── Pricing_Analysis/
    ├── by-vertical/ (benchmark pricing, margin analysis)
    ├── by-region/
    └── benchmarks.json (date_analyzed: YYYY-MM-DD, pricing_tier, margin_percent)
```

---

## Layer 6: Career & Growth

```
09_RESUME_PORTFOLIO/
├── Resume/
│   ├── roles/
│   │   ├── ent-role-001-saas-founder/
│   │   │   ├── description.md
│   │   │   ├── achievements.json (metric, value, date_achieved)
│   │   │   └── artifacts/ (articles, case studies, code samples)
│   │   ├── ent-role-002-product-manager/
│   │   └── [all roles]
│   ├── active-applications.json (company, role, status, interview_date)
│   ├── success-metrics.json (role, kpi_name, value, date_measured)
│   └── resume.pdf
│
└── Portfolio/
    ├── Portfolio_Index.json (ventures, projects, sorted by stage/success)
    ├── ventures/
    │   ├── ent-venture-001-hrms/
    │   │   ├── description.md (vision, market opportunity, current stage)
    │   │   ├── metrics.json (MRR, growth_rate, users, stage, last_updated)
    │   │   ├── screenshots/ (UI, dashboard, key features)
    │   │   └── code-samples/ (architecture, technical depth, innovations)
    │   ├── ops-venture-001-hvac/
    │   │   ├── description.md
    │   │   ├── metrics.json (revenue, job_count, average_job_value, growth)
    │   │   ├── case-studies/ (customer stories, ROI, testimonials)
    │   │   └── process-improvements/ (automation, cost savings)
    │   └── [all 712 ventures]
    ├── projects/
    │   ├── sys-project-001-iza-os/ (unified OS, tech stack, scale)
    │   ├── aut-project-001-crm-integration/ (n8n, Supabase, ClickUp)
    │   └── [key system projects]
    └── success-metrics.json (aggregate: total_ventures, total_revenue, growth_rate)
```

---

## Layer 7: Ventures (712 Total, Structured Consistently)

```
10_VENTURES/

├── SaaS_Ventures/ (ent-venture-00X-*)
│   ├── ent-venture-001-hrms/
│   │   ├── 01_STRATEGY/
│   │   │   ├── Vision.md (market opportunity, why now, why us)
│   │   │   ├── Milestones.json (date_target, description, owner, status)
│   │   │   └── Success_Metrics.json (kpi, target_value, current_value, date_measured)
│   │   │
│   │   ├── 02_RESEARCH/
│   │   │   ├── market-analysis.md
│   │   │   ├── competitive-analysis.md
│   │   │   └── customer-interviews.json
│   │   │
│   │   ├── 03_FINANCE/
│   │   │   ├── cap-table.json
│   │   │   ├── budget.json
│   │   │   ├── cash-forecast.json
│   │   │   └── unit-economics.json
│   │   │
│   │   ├── 04_MARKETING/
│   │   │   ├── positioning.md
│   │   │   ├── channel-strategy.md
│   │   │   ├── campaigns/ (by-campaign)
│   │   │   └── metrics.json
│   │   │
│   │   ├── 05_SALES/
│   │   │   ├── sales-collateral/
│   │   │   ├── pipeline.json
│   │   │   ├── customer-list.json
│   │   │   └── win-loss-analysis.json
│   │   │
│   │   ├── 06_OPERATIONS/
│   │   │   ├── roadmap.md
│   │   │   ├── team-structure.json
│   │   │   ├── hiring-plan.json
│   │   │   └── infrastructure.md
│   │   │
│   │   ├── 07_PRODUCTS_SERVICES/
│   │   │   ├── product-roadmap.json
│   │   │   ├── feature-list.md
│   │   │   ├── pricing-model.json
│   │   │   └── customer-success.md
│   │   │
│   │   ├── 08_SOPS/
│   │   │   ├── onboarding.md
│   │   │   ├── support-process.md
│   │   │   ├── quality-assurance.md
│   │   │   └── handoff.md
│   │   │
│   │   ├── 09_AUTOMATION/
│   │   │   ├── Agent_Manifest.json (agents, tools, responsibilities)
│   │   │   ├── Workflow_Configs/
│   │   │   ├── Skill_Assignments/
│   │   │   └── Integration_Points/ (Slack, Supabase, ClickUp)
│   │   │
│   │   ├── 10_EQUIPMENT/
│   │   │   ├── software-licenses.json
│   │   │   ├── infrastructure-costs.json
│   │   │   └── vendor-contracts.json
│   │   │
│   │   ├── 11_LEGAL/
│   │   │   ├── terms-of-service.md
│   │   │   ├── privacy-policy.md
│   │   │   ├── vendor-agreements.json
│   │   │   └── ip-assignments.json
│   │   │
│   │   ├── 12_ANALYTICS/
│   │   │   ├── dashboard.json
│   │   │   ├── metrics-definitions.md
│   │   │   └── weekly-reports/ (by-date)
│   │   │
│   │   ├── 13_DOCUMENTS/
│   │   │   ├── pitch-deck.pdf
│   │   │   ├── case-studies/
│   │   │   ├── whitepapers/
│   │   │   └── press-releases/
│   │   │
│   │   ├── 14_EXIT_PREPARATION/
│   │   │   ├── valuation-models.json
│   │   │   ├── m&a-targets.json
│   │   │   ├── financial-statements/
│   │   │   └── acquisition-process.md
│   │   │
│   │   ├── 15_PEOPLE_OPERATIONS/
│   │   │   ├── Agent_Manifest.json (HR automation agents)
│   │   │   ├── Team_Roster.json (name, role, email, hire_date)
│   │   │   ├── Skills_Inventory.json (person, skill, proficiency_level)
│   │   │   ├── RACI_Matrix.json (role, responsibility)
│   │   │   ├── Onboarding_Checklist.json (new_hire_tasks)
│   │   │   └── Handoff_Procedures.json (when_employee_leaves, knowledge_transfer)
│   │   │
│   │   ├── VENTURE.json (id, type, status, stage, mrr, created, updated)
│   │   ├── README.md (overview, quick links, onboarding)
│   │   └── metrics.json (date_measured: YYYY-MM-DD, all KPIs)
│   │
│   ├── ent-venture-002-graphify/ (same structure as HRMS)
│   ├── ent-venture-003-pitch-kit/ (same structure)
│   └── [additional SaaS ventures]
│
├── Operations_Ventures/ (ops-venture-00X-*)
│   ├── ops-venture-001-hvac/
│   │   ├── [01_STRATEGY through 15_PEOPLE_OPERATIONS - same 15 folders]
│   │   ├── Service_Quotes/ (linked from 05_QUOTES_ESTIMATES)
│   │   ├── Pricing_Rules/ (markup, labor rates, material costs)
│   │   ├── Vendor_Contacts/ (suppliers, parts distributors, equipment vendors)
│   │   ├── Field_Teams/ (team_name, lead, service_areas, utilization)
│   │   └── metrics.json (revenue, job_count, average_job_value, team_utilization)
│   │
│   ├── ops-venture-002-electrical/ (same 15 + service-specific)
│   ├── ops-venture-003-pressure-washing/ (same 15 + service-specific)
│   ├── ops-venture-004-travel/ (same 15 + booking-specific)
│   ├── ops-venture-005-ai-services/ (same 15 + consulting-specific)
│   ├── ops-venture-006-media/ (same 15 + production-specific)
│   └── [additional operations ventures]
│
├── Construction_Ventures/ (con-venture-00X-*)
│   ├── con-venture-001-general-contracting/
│   │   ├── [01_STRATEGY through 15_PEOPLE_OPERATIONS]
│   │   ├── Projects/ (project_id, scope, budget, timeline, status)
│   │   ├── Blueprints/ (designs, specifications, materials lists)
│   │   ├── Subcontractors/ (name, specialty, capacity, rates)
│   │   └── metrics.json (pipeline_value, active_projects, margin)
│   │
│   ├── con-venture-002-property-development/
│   └── [additional construction ventures]
│
├── Real_Estate_Ventures/ (re-venture-00X-*)
├── Media_Ventures/ (med-venture-00X-*)
├── Financial_Services_Ventures/ (fin-venture-00X-*)
│
├── Departmental_Resources/
│   ├── eng-department-001-backend/
│   │   ├── team-roster.json
│   │   ├── tech-stack.md
│   │   ├── architecture.md
│   │   ├── roadmap.json
│   │   └── oncall-rotation.json
│   │
│   ├── eng-department-002-frontend/
│   ├── prd-department-001-product/
│   ├── sal-department-001-enterprise/
│   ├── mkt-department-001-content/
│   └── ops-department-001-finance/
│
└── Shared_Resources/
    ├── Assets/
    │   ├── logos/ (Worldwidebro, OPCOs, ventures)
    │   ├── templates/
    │   └── brand-guidelines/
    ├── Templates/
    │   ├── proposal-templates/
    │   ├── sop-templates/
    │   ├── contract-templates/
    │   ├── budget-templates/
    │   └── venture-template.json (copy for new ventures)
    ├── Playbooks/
    │   ├── launch-playbook/ (go-to-market, timeline, checklist)
    │   ├── scaling-playbook/ (growth strategy, hiring, operations)
    │   ├── exit-playbook/ (M&A process, valuation, documents)
    │   └── crisis-playbook/ (emergency response, continuity)
    └── Training/
        ├── onboarding-material/ (for all new team members)
        ├── role-training/ (by-role, by-skill)
        └── certification-programs/
```

---

## Data Consistency Rules

| Property | Source | Format | Sync Frequency |
|----------|--------|--------|-----------------|
| Venture Status | Supabase | enum: planned, validation, build, launch, growth, scale, exit | Real-time |
| MRR / Revenue | Supabase → 10_VENTURES/VENTURE.json | numeric, USD | Daily |
| KPIs | Supabase → 10_VENTURES/metrics.json | date_measured: YYYY-MM-DD, value: numeric | Daily |
| Quotes | 05_QUOTES_ESTIMATES → Supabase → Dashboard | YYYY-MM-DD, amount: USD, status: draft/sent/won/lost | Real-time |
| Equipment Pricing | 04_EQUIPMENT_INTELLIGENCE → Apify scraper → Automation | date_updated: YYYY-MM-DD, vendor, price: USD | Daily |
| Team | 15_PEOPLE_OPERATIONS/Team_Roster.json | hire_date: YYYY-MM-DD | On-change |

---

## Automation Triggers

```
n8n Workflows:
├── lead-enrichment (trigger: new lead in ClickUp → enrich → Supabase)
├── quote-generation (trigger: sales request → template selection → email)
├── equipment-price-sync (trigger: daily 8am → Apify scraper → DB)
├── metric-aggregation (trigger: daily 9am → calculate KPIs → Dashboard)
└── slack-notifications (trigger: high-priority events → team alerts)

Apify Scrapers (run on schedule):
├── competitor-monitor (daily)
├── pricing-tracker (daily → 04_EQUIPMENT_INTELLIGENCE)
└── lead-extractor (on-demand)

AI Agents (autonomous):
├── scheduler (assigns tasks, tracks deadlines, escalates)
├── analyzer (trends, forecasting, anomaly detection)
├── executor (orchestrates workflows, monitors outcomes)
└── venture-agents (specialized per venture type)
```

---

## Validation Checklist

Every venture must have:
- [ ] `01_STRATEGY/Vision.md` + `Success_Metrics.json`
- [ ] `VENTURE.json` (id, type, status, stage, created, updated)
- [ ] `README.md` (overview, quick links, team)
- [ ] `15_PEOPLE_OPERATIONS/Team_Roster.json` (at least founder/lead)
- [ ] `metrics.json` with `date_measured: YYYY-MM-DD`
- [ ] Linked to Supabase for dashboard sync
- [ ] Linked to ClickUp for task execution

---

## Quick Links & Automation

- **Dashboard**: `/WORLDWIDEBRO-OS/01_CEO_COMMAND_CENTER/Dashboards/main-dashboard.json`
- **All Ventures**: `/WORLDWIDEBRO-OS/10_VENTURES/Portfolio_Index.json`
- **Equipment Pricing Sync**: Apify → `/WORLDWIDEBRO-OS/04_EQUIPMENT_INTELLIGENCE/` (auto-updated daily)
- **Quote Pipeline**: `/WORLDWIDEBRO-OS/05_QUOTES_ESTIMATES/` (synced from ClickUp real-time)
- **Metrics**: Each venture: `/10_VENTURES/{venture-id}/metrics.json` (daily snapshot from Supabase)

---

## Implementation Notes

1. **Never hardcode venture data** — pull from Supabase (source of truth)
2. **Every folder sync is calculated** — JSON views, not static files
3. **Agents orchestrate execution** — n8n workflows + AI agents handle updates
4. **Slack is the daily interface** — status, blockers, decisions flow through Slack
5. **Obsidian shows interactive views** — Dataview queries render live dashboards from metrics.json files

**Version Control**: This document is a template. Individual ventures follow it exactly. Changes to this structure require approval in #enterprise-planning Slack channel.

