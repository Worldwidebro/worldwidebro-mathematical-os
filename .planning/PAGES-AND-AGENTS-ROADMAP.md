---
title: Pages Roadmap + Agent Team Structure + Success Metrics
date: 2026-07-20
status: Implementation Blueprint
---

# CAPABILITY-FIRST PAGE ARCHITECTURE

Based on offline AI lab pattern, we need 10 capabilities. Each needs frontend + backend pages.

```
                    Users
                      │
            ┌──────────┴──────────┐
            │                     │
        Landing Pages         Authentication
            │                     │
            └──────────┬──────────┘
                       │
         ┌─────────────┼─────────────┐
         │             │             │
   Sector Hubs    Agent Terminal  Dashboards
         │             │             │
         └─────────────┼─────────────┘
                       │
        ┌──────────────┼──────────────┐
        │              │              │
    Routing       Orchestration   Storage
        │              │              │
        └──────────────┼──────────────┘
                       │
              Monitoring & Logging
```

---

# PAGES INVENTORY

## ✅ EXISTING (Already Deployed or Built)

### Frontend Pages (User-Facing)

| Page | URL | Status | Tech | Purpose |
|------|-----|--------|------|---------|
| VEX Portfolio Hub | https://vex-hero-site-sigma.vercel.app | Live | React/Next.js | Holdings brand site |
| Bloom Community Hub | https://bloom-community-hub.vercel.app | Live | React/Next.js | COMM sector hub + 48 venture links |
| COMM Ventures (48) | https://comm-NNN-*.vercel.app | Live | React/Next.js | Individual venture sites |
| CON-001 Ace | https://con-001-ace-construction.vercel.app | Live (partial) | React/Next.js | Construction venture + checkout |
| STA-001 Staffing | https://ops-staff-001-staffing.vercel.app | Live (partial) | React/Next.js | Staffing venture |
| ET-011 Education Kit | https://et-011-*.vercel.app | Live | React/Next.js | Education landing kit |
| **Org Chart** | /iza-os-org-chart.html | Local | D3.js | Interactive org structure (CEO → OPCOs → teams) |
| **Tech Stack** | /tech-stack-interactive.html | Local | D3.js | 16 layers, tool status, OPCO dependencies |

### Backend Pages (Internal Use)

| Page | Location | Status | Purpose |
|------|----------|--------|---------|
| Supabase Admin | cyhzilqldouzgynacqpe.supabase.co | Live | Database management |
| Neo4j Browser | http://localhost:7474 | Local | Knowledge graph queries |
| Grafana | http://localhost:3001 | Local | Metrics dashboards (not logged in) |
| TwentyHQ CRM | http://localhost:3002 | Local | Customer relationship management |
| n8n Workflows | http://localhost:5678 | Local | Workflow builder |
| Qdrant | http://localhost:6333 | Local | Vector DB (API only) |

---

## ❌ MISSING PAGES (High Priority)

### Frontend Pages (User-Facing)

#### Sector Hero Pages (6 OPCOs)
| Capability | Page | Status | Lead Form | Ventures Link |
|------------|------|--------|-----------|----------------|
| **CON** (Construction) | /sectors/construction | ❌ Missing | Supabase | Link to 12 CON ventures |
| **STA** (Staffing) | /sectors/staffing | ❌ Missing | Supabase | Link to 10 STA ventures |
| **RE** (Real Estate) | /sectors/real-estate | ❌ Missing | Supabase | Link to 8 RE ventures |
| **EDU** (Education) | /sectors/education | ❌ Missing | Supabase | Link to 15 EDU ventures |
| **FIN** (Finance) | /sectors/finance | ❌ Missing | Supabase | Link to 20 FIN ventures |
| **LOG** (Logistics) | /sectors/logistics | ❌ Missing | Supabase | Link to 10 LOG ventures |

#### Venture Landing Pages (100+ individual ventures)
| Type | Count | Status | Priority |
|------|-------|--------|----------|
| CON ventures | 12 | Built, not deployed | 1 |
| STA ventures | 10 | Built, not deployed | 1 |
| RE ventures | 8 | Built, not deployed | 2 |
| EDU ventures | 15 | Built, not deployed | 2 |
| FIN ventures | 20 | Built, not deployed | 2 |
| LOG ventures | 10 | Built, not deployed | 2 |
| Other ventures | 50+ | Not built | 3 |

#### Meta/Admin Pages
| Page | Purpose | Status | Users |
|------|---------|--------|-------|
| **Agent Terminal Dashboard** | Live agent status, outputs, metrics, logs | ❌ Missing | CEO, CTO, OPCOs |
| **Metrics Dashboard** | KPIs by OPCO, venture, agent (MRR, leads, proposals, revenue) | ❌ Missing | CEO, CFO, CMO |
| **Lead Intake Portal** | View + triage incoming leads by OPCO | ❌ Missing | Lead teams |
| **Venture Progress Tracker** | Stage, completeness, revenue per venture | ❌ Missing | CEO, portfolio ops |
| **Admin Control Panel** | Create ventures, assign agents, manage config | ❌ Missing | CEO, CTO |
| **Intake/Apply** | New venture application form | Stashed | Entrepreneurs |
| **Case Studies** | Client success stories | Stashed | Marketing |
| **Advisory Packages** | Consulting tier selector | Stashed | Sales |
| **404 Error** | Not found page | Stashed | All users |

### Backend Pages (Internal Use)

| Page | Purpose | Status | Tech |
|------|---------|--------|------|
| **Agent Execution Logs** | Real-time logs of all agent runs | ❌ Missing | Loki + Grafana |
| **Webhook Monitor** | n8n form→crew→output pipeline visualization | ❌ Missing | Custom dashboard |
| **Vector Search UI** | Query Qdrant repos/notes semantically | ❌ Missing | Vercel AI SDK |
| **Knowledge Graph Explorer** | Neo4j viz + query builder (ventures, repos, agents) | ❌ Missing | Neo4j browser plugin |
| **Audit Trail UI** | All agent decisions logged + searchable | ❌ Missing | Supabase + custom UI |
| **Secrets Rotation Manager** | View + rotate Stripe, Resend, API keys | ❌ Missing | Vault or Infisical UI |

---

# SPACE REQUIREMENTS & HOSTING ARCHITECTURE

## Frontend Hosting (Vercel)

| Asset | Count | Size | Monthly Cost |
|-------|-------|------|--------------|
| Sector hero pages | 6 | 50KB each | Free (Vercel Pro) |
| Venture sites (100) | 100 | 200KB each | $20/month |
| Images/media (CDN) | ~500 | 100KB avg | $10-20/month |
| Videos (guides, demos) | 20 | 50MB each | $50-100/month (Cloudflare Stream) |
| **Total Vercel Stack** | — | ~1.1GB | $80-140/month |

**Where:** All publicly accessible Vercel URLs (vercel.app domain)

## Backend Hosting (Mac Studio via Tailscale)

| Service | Data | Storage | Purpose |
|---------|------|---------|---------|
| Supabase (PostgreSQL) | ventures, leads, products, decisions | 500MB | Transactional data |
| Neo4j (Graph DB) | 712 ventures + relationships | 200MB | Knowledge graph |
| Qdrant (Vectors) | 1,648 repo embeddings + notes | 5GB | Semantic search |
| n8n (Workflows) | 50+ automation workflows | 100MB | Lead routing orchestration |
| Langfuse (LLM Traces) | All agent executions logged | 10GB/month | Agent observability |
| Prometheus + Grafana | Metrics, alerts, dashboards | 2GB | System monitoring |
| **Total Mac Studio** | — | ~16-18GB active | Behind Tailscale VPN |

**Access pattern:**
```
Public (Vercel):     user → landing page → lead form
                                             ↓
Private (Tailscale): form → n8n → Supabase → agent crew → CRM/calendar/proposal/invoice
```

## Cold Storage (T7 Shield: 1.1TB)

| Asset | Size | Backup | Purpose |
|-------|------|--------|---------|
| Ollama models (qwen2.5:32b, etc.) | 30GB | Daily snapshot | Local inference |
| Generated videos (marketing) | 50GB | Weekly archive | YouTube uploads |
| Repository clones (1,639 repos) | 200GB | Monthly tar | Reference indexing |
| Database backups | 5GB | Daily snapshot | Disaster recovery |
| Logs archive (old) | 100GB | Quarterly compress | Compliance |
| **Total T7 Shield** | ~385GB (of 1.1TB) | — | Cold storage tier |

**Layout:**
```
/Volumes/T7\ Shield/14_INFRASTRUCTURE/
├── data/
│   ├── models/              (30GB)
│   ├── embeddings/          (5GB Qdrant snapshots)
│   ├── videos/              (50GB)
│   ├── logs/                (10GB)
│   ├── backups/             (5GB)
│   └── repositories/        (200GB)
├── archive/                 (100GB old logs)
└── config/
    ├── docker-compose.yml
    ├── omnirouter-config.yaml
    └── NETWORK-MAP.md
```

---

# AGENT TEAMS & SUCCESS METRICS

## Team 1: Frontend Page Builders (Week 1-2)

**Goal:** 6 sector hubs + 100 venture sites deployed + 10 meta pages live

### Agents

| Agent | Skill | Output | Success Metric |
|-------|-------|--------|----------------|
| **Sector Hero Generator** | /frontend-design | 6 deployed sector hubs | 6/6 pages live, forms submit to Supabase |
| **Venture Site Deployer** | /deploy-and-link-venture | 100 deployed sites to Vercel | 100/100 live, all links work |
| **Dashboard Creator** | React/Next.js, Vercel | Agent Terminal + Metrics dashboards | 2 dashboards live + real-time updates |
| **QA & Testing** | /e2e-testing (Playwright) | All pages validated | 100% form submission success, <2s load time |

### Assignment

```
Page Builder Team Lead (orchestrator)
├─ Sector Hero Generator (sequential: CON → STA → RE → EDU → FIN → LOG)
├─ Venture Site Deployer (parallel: 3 agents × 30-40 sites each)
├─ Dashboard Creator (sequential: Terminal → Metrics → Admin)
└─ QA Tester (gate: nothing goes live until tests pass)

Skills assigned:
  /frontend-design
  /deploy-and-link-venture
  /e2e-testing
  /nextjs-turbopack
  /accessibility
```

---

## Team 2: Lead Capture & Routing (Week 2-3)

**Goal:** End-to-end form → agent execution pipeline working

### Agents

| Agent | Task | Success Metric |
|-------|------|----------------|
| **Form Wirer** | Add Supabase submission handler to all 6 sector forms | 6/6 sectors capturing leads |
| **Webhook Mapper** | Configure n8n RealTime trigger on venture_leads insert | n8n fires <1s after lead insert |
| **CRM Sync** | Sync TwentyHQ with new leads | 100% leads in CRM within 5min |
| **Notification Bot** | Email/Slack alerts to sales team | Alerts sent <2min after lead capture |

### Workflow

```
User fills /sectors/construction form
         ↓
POST to /api/leads (Supabase edge function)
         ↓
INSERT venture_leads
         ↓
RealTime trigger fires n8n webhook
         ↓
CON crew starts:
  • venture_classifier (94%)
  • estimator_gen1 (88%)
  • risk_assessor (91%)
  • project_scheduler (75%)
         ↓
Outputs: CRM update + calendar event + proposal draft + invoice
         ↓
Sales team notified via Slack + email
```

---

## Team 3: Agent Observability (Week 2-4)

**Goal:** Real-time Agent Terminal dashboard live + all metrics visible

### Agents

| Agent | Deliverable | Success Metric |
|-------|-------------|----------------|
| **Terminal Dashboard Creator** | Vercel-deployed dashboard | Live at /admin/agents, updates every 30s |
| **Metrics Collector** | Langfuse → Prometheus → Grafana | 100% agent executions logged + visible |
| **Log Aggregator** | Loki centralization + Grafana logs view | All logs searchable, indexed by agent/venture/timestamp |
| **Alert Rule Creator** | Auto-create alerts for anomalies | Alerts fire <5min of >5% failure rate |

### Agent Terminal Dashboard Layout

```
/admin/agents (Vercel-deployed)
├─ Live Agent Grid (6 cards)
│  ├─ CON Crew: 4 agents, 94% success rate, 23 executions this week
│  ├─ STA Crew: 4 agents, 91% success rate, 18 executions this week
│  ├─ RE Crew: 3 agents (future), 0 executions yet
│  ├─ EDU Crew: 2 agents (future), 0 executions yet
│  ├─ FIN Crew: 1 agent (future), 0 executions yet
│  └─ LOG Crew: 2 agents (future), 0 executions yet
│
├─ KPI Cards (Real-time)
│  ├─ Leads This Week: 47
│  ├─ Proposals Generated: 12
│  ├─ Contracts Signed: 3
│  ├─ Revenue (Layer 1): $23,450
│  └─ Agent Cost: $340/week
│
├─ Recent Executions (last 20)
│  └─ [Timestamp] | [Lead ID] | [Crew] | [Status] | [Output Summary] | [Duration]
│
└─ Failure Log (last 50 errors)
   └─ [Error] | [Agent] | [Input] | [Stack Trace] | [Retry Status]
```

---

## Team 4: Venture Factory (Week 3-4)

**Goal:** Automate venture instantiation (<30 min from template → live)

### One-Command Venture Creation

```bash
python3 create_venture.py \
  --venture-id CON-013 \
  --name "New Construction Co" \
  --city "Charlotte" \
  --owner-email "founder@example.com"
```

**Auto-created in 30 minutes:**
1. ✅ Folder: `/WORLDWIDEBRO-OS/03-PORTFOLIO/ventures/active/CON-013/`
2. ✅ Landing page deployed to Vercel: `https://con-013-*.vercel.app`
3. ✅ Supabase row created in `ventures` table
4. ✅ Neo4j node + relationships created
5. ✅ Agent assigned to venture (from available pool)
6. ✅ Slack channel created: `#con-013`
7. ✅ ClickUp task created for founder onboarding
8. ✅ Email sent to founder with login credentials + dashboard link

**Success Metric:** 30 ventures launched per week (once factory running)

---

# SUCCESS METRICS & TRACKING (Quantified)

## Phase 1 (Weeks 1-2): Foundation

| Metric | Target | Current | Owner |
|--------|--------|---------|-------|
| Sector hero pages deployed | 6/6 | 0/6 | CMO (Page Builder) |
| Venture sites deployed | 30/100 | 3/100 | CMO (Page Builder) |
| Lead capture wiring complete | 6/6 sectors | 0/6 | COO (Lead Router) |
| Agent crew tested end-to-end | 1 workflow | ✅ Built (not wired) | CTO |
| Stripe integration live | CON-001 | Built, secrets missing | CFO |

## Phase 2 (Weeks 3-4): Scaling

| Metric | Target | How to Measure | Owner |
|--------|--------|---------------|----|
| Pages deployed | 100+ | `vercel list --all \| wc -l` | CMO |
| Leads captured/week | 50+ | `SELECT COUNT(*) FROM venture_leads WHERE created_at > NOW() - INTERVAL 1 WEEK` | COO |
| Agent success rate | 80%+ | `SELECT COUNT(CASE WHEN status='success' THEN 1 END) / COUNT(*) FROM agent_executions` | Data Officer |
| Proposals generated | 20+/week | n8n execution count / 7 | CON crew |
| Lead-to-proposal rate | 30%+ | proposals_generated / leads_captured | CMO |

## Phase 3 (Weeks 5-6): Revenue

| Metric | Target | Acceptance Criteria | Owner |
|--------|--------|-------------------|-------|
| Ventures earning revenue | 10+ | `SELECT COUNT(*) FROM ventures WHERE mrr > 0` | CEO |
| Monthly revenue (Layer 1) | $5K-15K | `SELECT SUM(mrr) FROM ventures WHERE status='active'` | CFO |
| Lead cost | <$5/lead | total_spend / leads_captured | CMO |
| Agent autonomy | 70%+ agents >90% | `SELECT COUNT(*) FROM agents WHERE success_rate > 0.90` | Data Officer |
| Stripe payment success | 95%+ | successful_charges / attempted_charges | CFO |

---

# AGENT TEAM STRUCTURE (Organizational)

```
CEO Agent (You)
└─ Authority: Final approval on all hiring, OPCO assignments, strategy

├─ CTO Agent (Infrastructure)
│  └─ Success: 99.9% uptime, <100ms latency
│     • Manages: docker-compose, Tailscale, networking
│     • Owns: /iza-os-org-chart, tech-stack visibility
│     • Goal: Mac Studio + T7 + Vercel seamless
│
├─ CMO Agent (Marketing & Growth)
│  └─ Success: 100 pages deployed by Week 4, 50+ leads/week
│     ├─ Sub: Page Builder Team Lead
│     │  ├─ Sector Hero Generator (1 agent)
│     │  ├─ Venture Site Deployer (3 agents, parallel)
│     │  ├─ Dashboard Creator (1 agent)
│     │  └─ QA Tester (1 agent, gate)
│     └─ Sub: Content Creator
│        └─ Case studies, advisory packages, 404 (stashed, Week 2)
│
├─ COO Agent (Operations & Automation)
│  └─ Success: Lead-to-crew pipeline 100% automated
│     ├─ Sub: Lead Router Team
│     │  ├─ Form Wirer (1 agent)
│     │  ├─ Webhook Mapper (1 agent)
│     │  ├─ CRM Sync (1 agent)
│     │  └─ Notification Bot (1 agent)
│     └─ Sub: Venture Factory
│        └─ create_venture.py automation (1 agent)
│
├─ CFO Agent (Finance & Revenue)
│  └─ Success: $5K-15K revenue by Week 6
│     ├─ Stripe integration manager (Resend + Stripe secrets)
│     ├─ MRR tracker
│     └─ Revenue attribution
│
└─ Data Officer Agent (Observability & Intelligence)
   └─ Success: 100% visibility into all agents, systems, ventures
      ├─ Agent Terminal Creator
      │  ├─ Dashboard designer
      │  ├─ Metrics collector (Langfuse → Grafana)
      │  ├─ Log aggregator (Loki)
      │  └─ Alert rule creator
      └─ Knowledge Graph Curator
         └─ Neo4j + Qdrant sync
```

---

# SKILLS + TOOLS + MCPs ASSIGNMENT

## Page Builder Team Skills

```python
page_builder_skills = [
    "/frontend-design",             # Create UI/components
    "/deploy-and-link-venture",     # Push to Vercel + add to portfolio
    "/e2e-testing",                 # Playwright validation
    "/accessibility",               # WCAG compliance
    "/nextjs-turbopack",            # Fast builds
    "/react-pro",                   # React component patterns
]
```

## Lead Router Team MCPs

```python
lead_router_mcps = [
    "supabase",                     # venture_leads, edge functions
    "n8n",                          # webhook triggers
    "slack",                        # notifications
    "hubspot",                      # CRM (optional)
    "gmail",                        # email alerts
]
```

## Agent Terminal Team Tools

```python
agent_terminal_tools = [
    "Langfuse API",                 # LLM trace capture
    "Prometheus",                   # metrics scraping
    "Grafana",                      # visualization
    "Loki",                         # log aggregation
    "Vercel API",                   # deployment monitoring
]
```

---

# NEXT ACTIONS (This Week)

## TODAY (Monday)
- [ ] Create CON sector hero (2-3 hours, use SectorHero.tsx template)
- [ ] Wire form to Supabase venture_leads
- [ ] Deploy to Vercel + test

## TOMORROW (Tuesday)
- [ ] Create remaining 5 sector hubs (STA, RE, EDU, FIN, LOG)
- [ ] Deploy all 6 to Vercel (parallel)
- [ ] Wire n8n webhook trigger on venture_leads RealTime event

## WEDNESDAY
- [ ] Create Agent Terminal dashboard (Vercel)
- [ ] Wire Langfuse → Prometheus → Grafana pipeline
- [ ] Test end-to-end: form → venture_leads → n8n → crew execution

## THURSDAY-FRIDAY
- [ ] Deploy first 30 venture sites (parallel deployment)
- [ ] Set up Metrics dashboard (KPIs by OPCO)
- [ ] Build /admin/agents control panel

