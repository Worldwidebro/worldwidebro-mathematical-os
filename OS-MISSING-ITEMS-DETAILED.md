---
title: Missing & Partial OS Items — Detailed Breakdown
date: 2026-07-20
version: 1.0
---

# 78 Missing/Partial Items Blocking Full OS Completion

**Total Items: 128 | Completed: 50 (✅) | In Progress: 16 (🔄) | Missing: 78 (❌ + ⚠️)**

---

# ❌ MISSING ITEMS — 34 items (zero progress)

## Phase 0 — Vision & Governance
- Risk Framework (venture risk governance doc)
- AI Usage Policies (not documented)

## Phase 1 — Infrastructure
- NAS (not implemented)
- UPS (not implemented)
- GPU Cluster (single machine only)
- Edge Devices (not planned)

## Phase 2 — Identity
- SSO (no centralized single sign-on)
- Customer Permissions (not defined)

## Phase 3 — Development
- Kubernetes (not implemented)

## Phase 6 — Agent Runtime
- Event Bus (Redis not wired as pubsub)
- Voice (not implemented)

## Phase 7 — Department Operating Systems
- Customer Support OS (no ticketing system)
- Accounting OS (no accounting system)
- Legal OS (no case management)
- Procurement OS (no process)

## Phase 8 — Venture Operating Systems (CRITICAL)
- ERP (ventures have no ERP)
- Customer Portal (no customer-facing portals)
- Finance (no per-venture accounting)

## Phase 10 — Data
- Data Lake (no data lake; ad-hoc queries only)
- Streaming (no streaming data layer)

## Phase 11 — Business Intelligence (CRITICAL)
- Department Dashboard (not implemented)
- Security Dashboard (no security metrics)
- Forecast Dashboard (no forecasting UI)

## Phase 12 — Security
- Disaster Recovery (no DR playbook)
- Compliance Tracking (no compliance OS)

## Phase 13 — Financial OS
- Budgeting (no budget planning)
- Payroll (no payroll system)
- AP (no accounts payable)
- Banking (no bank integrations)
- Taxes (no tax tracking)

## Phase 14 — Growth Engine
- Referral Program (not implemented)
- Affiliate Program (not planned)

## Phase 15 — Learning System
- Experiment Tracking (no experiment tracking system)

## Phase 16 — Marketplace
- Agent Marketplace (not planned)
- Workflow Marketplace (not planned)
- Prompt Marketplace (not planned)
- Connector Marketplace (not planned)

---

# ⚠️ PARTIAL ITEMS — 44 items (some progress, needs completion)

## Phase 0 — Vision & Governance
- Decision Framework — ownership model exists; decision-log table not implemented
- Security Policies — no formal ISMS/security policy document

## Phase 1 — Infrastructure
- Backup Storage — Git only; no dedicated backup strategy
- GPU Cluster — Mac Studio only; no cluster
- Package Registry — npm + Docker Hub; no unified registry

## Phase 2 — Identity
- IAM — agent identity layer partial; no machine IAM
- Secrets Management — .env local only; no vault; no rotation
- RBAC — database RLS only; no app-level RBAC

## Phase 3 — Development
- CI/CD — Vercel production only; no staging CI/test automation
- IaC — Vercel config minimal; no Terraform/CDK; manual cloud setup
- Package Registry — npm + Docker Hub; no unified registry
- Testing — Playwright + scattered unit tests; no comprehensive strategy
- Release Pipeline — manual Vercel + git; no automation

## Phase 4 — Knowledge
- PRDs — scattered STATUS.md files; no formal PRD template
- Decision Logs — git commits only; no formal decision log

## Phase 5 — AI Platform
- Prompt Registry — AGENTS.md + scattered code; no centralized versioning
- Workflow Registry — LOOP.md defined; no workflow versioning
- Cost Tracking — manual token counting; no automated tracking
- Model Benchmarking — no benchmark suite

## Phase 6 — Agent Runtime
- Manager — cadence check exists; no full orchestrator
- Messaging — Slack MCP available; not wired to agents
- Vision — Claude has it; no image processing pipeline
- Self-Improvement — eval harness not running
- Human Approval — AskUserQuestion available; not systematic
- Rollback — git available; not automated

## Phase 7 — Department Operating Systems (8 depts missing OS)
- Product OS — no centralized product management
- QA OS — no QA department infrastructure
- Design OS — no formal design OS
- Finance OS — no accounting OS; manual spreadsheets
- HR OS — career-ops partial; no formal HR OS
- Recruiting OS — no recruiting automation
- Research OS — web search available; no formal R&D OS
- Security OS — Tailscale + RLS only; no formal security OS

## Phase 8 — Venture Operating Systems (CRITICAL — applies to all 712 ventures)
- CRM per venture — TwentyHQ running; not wired to individual ventures
- CMS per venture — no integrated CMS per venture
- Marketing per venture — Zapier partial; not per-venture
- Sales per venture — ClickUp by OPCO; not per-venture
- Dashboard per venture — Grafana ready; no per-venture dashboards
- Reporting per venture — CSV only; no automated reporting
- Analytics per venture — DuckDB only; no per-venture dashboards

## Phase 9 — Automation
- Workflow Builder — n8n not deployed; Zapier partial (4 zaps)
- Event Triggers — webhook patterns exist; no systematic triggering
- Queues — Redis available; not used as task queue
- Retries — manual retry logic; no automatic framework
- Escalations — manual rules; not automated
- Human Approval — AskUserQuestion available; not systematic

## Phase 10 — Data
- Warehouse — DuckDB minimal; not full data warehouse
- ETL — Python scripts manual; no orchestrated pipelines

## Phase 11 — Business Intelligence (CRITICAL)
- Executive Dashboard — Hermes UI built; schema mismatch (Task 5)
- Venture Dashboard — CSV only; no interactive dashboard
- Revenue Dashboard — CSV only; no live tracking
- Operations Dashboard — Grafana ready; empty
- Agent Dashboard — Hermes UI; not wired to logs
- Infrastructure Dashboard — Grafana partial; minimal scraping
- Cost Dashboard — manual token counting; no automation

## Phase 12 — Security
- Secrets Management — .env local; no vault; no rotation
- Backups — GitHub + Supabase assumed; no tested restore
- Vulnerability Scanning — Dependabot working; no SLA
- Audit Trails — schema exists; empty table; not instrumented
- Access Reviews — Tailscale list; manual only
- Incident Response — manual process; no formal plan

## Phase 13 — Financial OS
- Forecasting — revenue forecast exists; no P&L
- Billing — Stripe connected; no billing OS; manual invoices
- AR — manual Excel; no AR tracking
- Cash Flow — manual spreadsheets; no forecast

## Phase 14 — Growth Engine
- SEO — tags exist; no SEO strategy
- Ads — Google Ads assumed; no campaigns
- Social Media — handles exist; no automation
- Email — Resend configured; no automation
- Partnerships — manual network; no partnership OS

## Phase 15 — Learning System
- Prompt Library — AGENTS.md + scattered; no version control
- Training Data — Academy designed; not deployed
- Feedback Loops — manual feedback; no systematic collection
- Agent Evaluation — eval harness planned; not running
- Continuous Improvement — manual reviews; no systematic loop

## Phase 16 — Marketplace
- Template Marketplace — local templates only; no platform

## Phase 17 — Enterprise Features
- Multi-Tenant — single-tenant only (bootstrap)
- Organizations — OPCO structure exists; no multi-org support
- Teams — agent teams defined; no team management OS
- Roles — agent roles defined; no RBAC enforcement
- White Label — not planned
- API — Supabase REST available; no public API; no versioning
- SDK — not released
- Billing — manual; no multi-tenant billing
- Licensing — not planned

## Phase 18 — Observability
- Logs — Langfuse fixed; not receiving app logs
- Metrics — Prometheus running; no app instrumentation
- Traces — otel-collector ready; one config change needed
- Cost Tracking — manual; no automation
- Token Usage — manual via LiteLLM; not graphed
- Latency — Vercel analytics only; no end-to-end tracking
- Agent Health — no monitoring
- SLA Monitoring — no SLA tracking
- Error Reporting — local logging; no centralized aggregation

## Phase 19 — Intelligence Layer
- Customer Graph — not tracked
- Decision Graph — git + memory only; no formal log
- Recommendation Engine — not implemented

## Phase 20 — Executive Command Center
- CEO Dashboard — Hermes schema mismatch
- Live Agent Map — manual sector status; not live-updating
- Revenue Tracking — manual projections; no live tracking
- Cash Position — manual spreadsheets; no bank API
- Infrastructure Status — Grafana empty
- Active Automations — cadence-check running; not visible
- Knowledge Graph Explorer — Neo4j UI; not integrated into dashboard
- Risk Center — rules defined; not tracked on dashboard

---

# Quick Win Opportunities (< 1 week each)

1. **Otel-Collector → Prometheus** — Add `otel-collector:9464` to Prometheus targets
2. **Audit Log Instrumentation** — Wire key agent actions to Supabase audit_logs table
3. **Hermes Schema Fix** — Map dashboard queries: aoc_agents→ventures, agent_tasks→venture_decisions
4. **Prompt Library Structure** — Create git-tracked prompt registry + versioning
5. **Decision Log Table** — Create CLI tool to log decisions to Supabase
6. **Grafana Templates** — Copy vendor dashboards (Postgres, Docker, Node) + customize
7. **API Key Rotation Policy** — Document + schedule monthly rotation

**Effort: 1-2 hours each. Impact: High (unblocks observability + governance).**

---

# Medium Effort (1-3 weeks each)

8. **Event Bus Wiring** — Redis pubsub + agent action publishers
9. **Venture OS Template** — Scaffold CRM + dashboard per venture type
10. **Department OS Framework** — Define structure + dashboards for 14 departments
11. **n8n Deployment** — Server setup + venture ops workflows
12. **Secrets Vault** — Migrate .env to HashiCorp Vault or AWS Secrets Manager
13. **CI/CD Pipeline** — GitHub Actions for tests + staging deploy
14. **BI Dashboard Suite** — Grafana revenue, health, operations dashboards
15. **Agent Identity Layer** — AgentToolWiring class (in progress)

**Effort: 20-60 hours each. Impact: Very High (unblocks scaling).**

---

# Major Effort (3-8 weeks each)

16. **Multi-Tenant Architecture** — Refactor for RBAC + org isolation
17. **Financial OS** — QuickBooks + P&L + cash flow
18. **Accounting System** — Chart of accounts + ledger + tax tracking
19. **Marketplace Platform** — Agent/workflow/template storefront
20. **Public API + SDK** — API design + SDK generation
21. **Academy Platform** — Deploy 30-layer curriculum
22. **Customer Portals** — Per-venture customer experience
23. **End-to-End Observability** — Logs + metrics + traces integrated

**Effort: 60-200+ hours each. Impact: Strategic (enables enterprise scale).**

---

# Dependency Graph: What Blocks What

### Blocking CRITICAL (Phase 8, 11, 20) are:

1. **AgentToolWiring** (Phase 2) — enables Slack/ClickUp/automation
2. **Event Bus** (Phase 6) — enables agent coordination
3. **Venture OS Template** (Phase 8) — enables venture self-serve
4. **BI Dashboards** (Phase 11) — enables visibility + decisions
5. **Hermes Schema Fix** (Phase 20) — enables CEO command center

### These 5 unlock everything else.

---

# Priority Sequencing (Next 90 Days)

## Week 1-2: Quick Wins
- [ ] Otel-collector wiring (observability unblocked)
- [ ] Hermes schema fix (CEO dashboard unblocked)
- [ ] Audit log instrumentation (governance unblocked)

## Week 3-4: Medium Effort (Foundation)
- [ ] AgentToolWiring class (agent identity)
- [ ] Event bus wiring (agent coordination)
- [ ] Prompt library structure (AI governance)

## Week 5-8: Venture OS + BI
- [ ] Venture OS template (612 ventures self-serve)
- [ ] BI dashboard suite (Grafana live)
- [ ] Department OS framework (14 depts)

## Week 9-12: Automation + Scaling
- [ ] n8n deployment (workflow automation)
- [ ] Secrets vault (security hardening)
- [ ] CI/CD pipeline (release automation)

---

# By the Numbers

| Category | Count | Hours | Weeks |
|----------|-------|-------|-------|
| Quick Wins (< 1 wk) | 7 | 14 | 1 |
| Medium (1-3 wks) | 8 | 160 | 4 |
| Major (3-8 wks) | 8 | 800 | 20 |
| **Total** | **23** | **974** | **25** |

**To close all 78 gaps: ~6 months @ full-time engineering (if done sequentially)**

**To unblock CRITICAL 5 gaps: ~4 weeks @ 2 engineers**

---

*Last Updated: 2026-07-20*
