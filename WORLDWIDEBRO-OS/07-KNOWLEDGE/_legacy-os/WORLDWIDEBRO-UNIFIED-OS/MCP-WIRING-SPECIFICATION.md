# MCP-WIRING-SPECIFICATION.md
## How Each MCP Connects to Your System

**Purpose:** Define data flow, triggers, destinations for 22 MCPs.

---

## QUICK REFERENCE

| MCP | Asset Layer | Status | Effort | Priority |
|-----|-------------|--------|--------|----------|
| **Stripe** | Financial (1) | ❌ | 4h | P0 |
| **HubSpot** | Relationships (12) | ❌ | 5h | P0 |
| **Slack** | Workflows (7) | ⚠️ | 1h | P0 |
| **Portfolio** | Financial (1) | ❌ | 8h | P1 |
| **KPI** | All layers | ❌ | 6h | P1 |
| **Deal-Flow** | Relationships (12) | ❌ | 10h | P1 |
| **Buffer** | Media (10) | ❌ | 4h | P2 |
| **Beehiiv** | Audience (11) | ❌ | 3h | P2 |
| **Twitter** | Audience (11) | ⚠️ | 2h | P2 |
| **Media** | Media (10) | ❌ | 12h | P3 |
| **Qdrant** | Knowledge (2) | ❌ | 6h | P3 |
| **Tavily** | Research | ❌ | 2h | P3 |
| **Crunchbase** | Research | ❌ | 3h | P4 |
| **SOP** | SOPs (4) | ❌ | 8h | P4 |
| **Obsidian** | Documentation (3) | ❌ | 3h | P2 |
| **Notion** | Documentation (3) | ❌ | 3h | P2 |
| **GitHub** | Code (9) | ❌ | 2h | P3 |
| **Google Sheets** | Data (13) | ❌ | 2h | P2 |
| **PostgreSQL** | Data (13) | ✅ | 0h | N/A |
| **Supabase** | Data (13) | ✅ | 0h | N/A |
| **WordPress** | Media (10) | ❌ | 4h | P4 |
| **Postiz** | Audience (11) | ❌ | 3h | P2 |

---

## IMPLEMENTATION TIMELINE

**Week 1 (P0):** Stripe, HubSpot, Slack (10 hours)  
**Week 2 (P1):** Portfolio, KPI, Deal-Flow (24 hours)  
**Week 3 (P2):** Buffer, Beehiiv, Twitter, Obsidian, Notion, Google Sheets, Postiz (20 hours)  
**Week 4 (P3):** Media, Qdrant, Tavily, GitHub (20 hours)  
**Month 2 (P4):** Crunchbase, SOP, WordPress (14 hours)  

**Total: 88 hours to wire all 22 MCPs**

---

## TIER 1: FINANCIAL MCPs

### **Stripe MCP → Revenue Tracking**

```
Stripe payments
    ↓ [Webhook]
Supabase.spending_transaction
    ↓ [Daily 6 AM]
KPI MCP (calculates MRR)
    ↓
Dashboard + Financial Controller Agent
```

**Setup (4h):**
1. Create Supabase function: `stripe-webhook-handler`
2. Stripe webhook → Supabase function
3. Daily batch job (6 AM): fetch all transactions
4. Store: `spending_transaction` table
5. KPI Agent queries: `SUM(amount) WHERE date > NOW() - INTERVAL '1 month'`

---

### **HubSpot MCP → Contact & Deal Tracking**

```
HubSpot API
    ↓ [Hourly sync]
Supabase.hubspot_contacts, .hubspot_deals
    ↓
Deal-Flow MCP (matching)
    ↓
Slack notifications
```

**Setup (5h):**
1. HubSpot API key → secrets
2. Hourly cron: sync contacts, deals, companies
3. Join: HubSpot deals → revenue potential
4. Trigger: Slack notification when deal ≥ $50K

---

### **Portfolio MCP → Company Health**

```
Supabase.portfolio_companies
    ↓ [Real-time]
Portfolio MCP (aggregates)
    ↓
KPI MCP (ROI calculation)
    ↓
Dashboard alerts
```

**Setup (8h):**
1. Build Portfolio MCP server (Node.js)
2. Endpoints: `/portfolio/health`, `/portfolio/company/:id`, `/portfolio/analytics`
3. Queries: revenue, runway, health_score
4. Returns: real-time aggregated data

---

## TIER 2: CONTENT & AUDIENCE MCPs

### **Buffer/Beehiiv/Postiz → Distribution**

```
Content created
    ↓
Buffer MCP (Twitter, LinkedIn, Instagram)
Beehiiv MCP (newsletter)
Postiz MCP (multi-platform)
    ↓ [Scheduled]
Platforms post
    ↓ [Hourly sync]
Analytics → audience_metrics table
```

**Setup (10h total):**
- Buffer: `POST /updates` (create), `GET /analytics` (fetch metrics)
- Beehiiv: `POST /emails` (send), `GET /analytics` (metrics)
- Postiz: Similar multi-platform scheduling
- Daily sync: engagement back to Supabase

---

### **Media MCP → Video Processing**

```
Raw video
    ↓
Media MCP:
├─ Transcribe (Whisper)
├─ Extract clips (FFmpeg)
├─ Dub (Eleven Labs)
└─ Subtitle (auto)
    ↓
Buffer/Beehiiv/Twitter MCPs
    ↓
Content distributed
```

**Setup (12h):**
1. Media MCP server (Python + FFmpeg)
2. Endpoints: `/transcribe`, `/extract-clips`, `/dub`, `/subtitle`
3. Stores: `content_pieces` table
4. Output: 1 video → 5-10 pieces

---

## TIER 3: RESEARCH & KNOWLEDGE MCPs

### **Tavily/Crunchbase → Market Research**

```
Deal Scout Agent ["Find agencies"]
    ↓
Tavily MCP (web search)
Crunchbase MCP (company data)
    ↓
Results → deal_research table
    ↓
Deal scoring uses context
```

**Setup (5h):**
- Tavily: `POST /search` (web search)
- Crunchbase: `GET /companies/:name` (funding, contacts)
- Store in: `deal_research` table

---

### **Qdrant MCP → Semantic Search**

```
Knowledge created
    ↓ [Weekly]
Qdrant MCP (reindex)
├─ Generate embeddings
└─ Update vector index
    ↓
Research Agent query ["Find automation frameworks"]
    ↓
Qdrant returns: Top 5 docs
```

**Setup (6h):**
1. Qdrant container (Docker/cloud)
2. Collections: frameworks, sops, research, media
3. Weekly reindex from Supabase
4. Query endpoint: `/search` (semantic)

---

## TIER 4: OPERATIONAL MCPs

### **Deal-Flow MCP → Pipeline Management**

```
Deal sourced
    ↓
Deal-Flow MCP:
├─ Score (sector, operator, capital, timing)
├─ Match to operator
└─ Track through pipeline
    ↓
Qualified deal → Slack notification
```

**Setup (10h):**
1. Build Deal-Flow MCP server
2. Scoring algorithm (30+30+20+20 points)
3. Operator matching via HubSpot contacts
4. Pipeline stages: sourced→qualified→proposed→negotiated→closed

---

### **SOP MCP → Workflow Execution**

```
SOP created (e.g., "Automation Audit")
    ↓
Operator Coordinator Agent [Trigger]
    ↓
SOP MCP:
├─ List steps
├─ Execute checklist
└─ Track completion
    ↓
Results → sop_execution table
```

**Setup (8h):**
1. Build SOP MCP server
2. SOP structure: {id, steps[], templates[], success_criteria[]}
3. Execution tracking in Supabase
4. Completion updates trigger next workflow

---

### **KPI MCP → Real-time Metrics**

```
All systems generate data
    ├─ Stripe (revenue)
    ├─ Buffer/Beehiiv (engagement)
    ├─ HubSpot (deals)
    └─ Portfolio (health)
    ↓ [Daily 6 AM]
KPI MCP (aggregates)
├─ MRR = SUM(revenue)
├─ Growth% = (current-previous)/previous
└─ Health = (revenue-burn)/runway
    ↓
metrics_weekly table
    ↓
Dashboard updated + Alerts triggered
```

**Setup (6h):**
1. Build KPI MCP server
2. Daily job: query all data sources
3. Calculate: MRR, growth%, health scores
4. Alert thresholds: revenue ↓5%, deals >80, health <6mo

---

## WIRING CHECKLIST

**Week 1:**
- [ ] Stripe webhook → Supabase function
- [ ] HubSpot hourly sync cron job
- [ ] Slack bot integration + notification templates
- [ ] Portfolio MCP server built + tested

**Week 2:**
- [ ] KPI MCP daily job wired
- [ ] Deal-Flow MCP scoring algorithm implemented
- [ ] All 3 feed into dashboard

**Week 3:**
- [ ] Buffer, Beehiiv, Postiz API integrations
- [ ] Twitter/X MCP wired
- [ ] Obsidian/Notion query endpoints
- [ ] Google Sheets sync

**Week 4:**
- [ ] Media MCP (transcribe, clips, dub, subtitle)
- [ ] Qdrant semantic search indexing
- [ ] Tavily web search integration
- [ ] GitHub code search

**Month 2:**
- [ ] Crunchbase company research
- [ ] SOP MCP execution tracking
- [ ] WordPress publishing workflow

---

## RESULT: AUTONOMOUS SYSTEM

When all 22 MCPs are wired:

✅ Revenue automatically tracked (Stripe)  
✅ Relationships automatically synced (HubSpot)  
✅ Content automatically distributed (Buffer/Beehiiv/Postiz)  
✅ Video automatically processed (Media)  
✅ Knowledge automatically searchable (Qdrant)  
✅ Deals automatically sourced (Tavily/Crunchbase)  
✅ Deals automatically scored (Deal-Flow)  
✅ Metrics automatically calculated (KPI)  
✅ Alerts automatically triggered (Slack)  
✅ Team automatically notified (Slack)  
✅ Workflows automatically executed (SOP)  
✅ SOPs automatically tracked (SOP)  

**System runs 24/7 on autopilot.**

