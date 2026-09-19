# Data Locality Map
**Where does every piece of data live? How to access it?**
2026-09-19

## Physical + Cloud Infrastructure

```
WORLDWIDEBRO HOLDINGS (Strategic Data)
├─ VERCEL (Cloud Deployments — Live)
│  ├─ vex-hero-site-sigma.vercel.app (Portfolio dashboard)
│  │  ├─ Live: Venture list, readiness, metrics
│  │  ├─ Storage: Vercel KV (cache), Supabase DB (source)
│  │  └─ Logs: Vercel analytics + error tracking
│  │
│  ├─ ops-staff-001-staffing.vercel.app (OPS-001)
│  │  ├─ Live: Cold call tracking, placements, revenue
│  │  ├─ Storage: PostgreSQL (Supabase)
│  │  └─ Files: Vercel blob storage (resumes, contracts)
│  │
│  ├─ healthroute-courier.vercel.app (LT-005)
│  │  ├─ Live: Orders, routes, driver tracking
│  │  ├─ Storage: PostgreSQL (Supabase), Redis cache
│  │  └─ Files: Courier documents, proofs of delivery
│  │
│  ├─ callcenter-eosin.vercel.app (CALLCENTER)
│  │  ├─ Live: Call routing, SIP/Twilio
│  │  ├─ Storage: PostgreSQL (call logs), Redis (queue)
│  │  └─ Audio: S3 or Vercel blob (call recordings)
│  │
│  ├─ con-001-ace-construction.vercel.app (CON-001)
│  │  ├─ Live: Projects, readiness scoring
│  │  ├─ Storage: PostgreSQL (Supabase)
│  │  └─ Files: JotForm submissions, project images
│  │
│  ├─ re-001-worldwidebro-holdings.vercel.app (RE-001)
│  │  ├─ Live: Deal pipeline, property listings
│  │  ├─ Storage: PostgreSQL (Supabase)
│  │  └─ Files: Property images, contracts, deeds
│  │
│  └─ lt-011-dispatch-software.vercel.app (LT-011)
│     ├─ Live: Skeleton/demo
│     ├─ Storage: PostgreSQL (Supabase)
│     └─ Files: (none yet)
│
├─ SUPABASE (Transactional Database — Source of Truth)
│  ├─ aipehhzlsmfxxzwceppd.supabase.co
│  ├─ Database: PostgreSQL (hosted)
│  ├─ Tables:
│  │  ├─ ventures (789 rows) — all 789 ventures, status, metrics
│  │  ├─ capabilities (300+ rows) — what each can do
│  │  ├─ agents (318 rows) — who's executing
│  │  ├─ metrics (18K+ rows) — 789 ventures × 23 KPIs
│  │  ├─ call_logs (OPS-001, CALLCENTER)
│  │  ├─ orders (LT-005)
│  │  ├─ projects (CON-001)
│  │  ├─ properties (RE-001)
│  │  └─ deployments (all ventures)
│  ├─ Auth: Magic links + OAuth
│  ├─ Storage: PostgreSQL backups (daily)
│  └─ Access: REST API, JS client, Python psycopg2
│
├─ MAC STUDIO (Backbone — Local Infrastructure)
│  ├─ IP: 100.87.214.70 (Tailscale)
│  ├─ Storage:
│  │  ├─ Internal: 228 GB (95% full, 641 MB free)
│  │  └─ T7 Shield: 1.8 TB (51% full, 922 GB available) ← PRIMARY
│  │
│  ├─ Services (Docker):
│  │  ├─ Neo4j (bolt://100.87.214.70:7687)
│  │  │  └─ Data: 20,363 edges (ventures, solutions, capabilities, agents)
│  │  │
│  │  ├─ Qdrant (http://100.87.214.70:6333)
│  │  │  └─ Data: 17,236 vectors (semantic patterns)
│  │  │
│  │  ├─ PostgreSQL (localhost:5433)
│  │  │  └─ Database: company_brain (local copy of Supabase for dev)
│  │  │
│  │  ├─ Redis (localhost:6379)
│  │  │  └─ Cache: session data, rate limiting, job queues
│  │  │
│  │  ├─ OmniRoute (http://100.87.214.70:20128 or :3000)
│  │  │  └─ Routing: 110 tools, agent dispatching
│  │  │
│  │  ├─ LiveKit (localhost:17880-17882)
│  │  │  └─ Real-time: video, audio, data streams
│  │  │
│  │  └─ 70+ other Docker volumes
│  │
│  ├─ Models (Ollama):
│  │  ├─ qwen2.5-coder:14b (8.9 GB) — code generation
│  │  ├─ hermes3:latest (4.6 GB) — reasoning
│  │  └─ llama3.1:8b (4.9 GB) — general inference
│  │
│  ├─ Git Repos:
│  │  ├─ /Users/acebless/Documents/The\ Company/Company\ Brain/ (1.7 GB)
│  │  │  └─ 50 numbered domains + 22 infrastructure folders
│  │  ├─ /Users/acebless/Documents/Worldwidebro-Vex/ (VEX repo)
│  │  ├─ /Users/acebless/Documents/HealthRoute-Courier/ (LT-005 repo)
│  │  └─ repos/ subdirectory (177 code repos, 618 templates)
│  │
│  └─ Data Sync:
│     ├─ Manual: rsync/scp between Mac Air ↔ Mac Studio
│     └─ NOT AUTOMATED (critical gap)
│
├─ MAC AIR (This Session — 641 MB free, CRITICAL)
│  ├─ IP: 100.121.17.63 (Tailscale VPN only)
│  ├─ Storage:
│  │  ├─ Internal: 228 GB (95% full, 641 MB free) ← CRITICAL CLEANUP NEEDED
│  │  └─ External: None (unlike Mac Studio)
│  │
│  ├─ Docker Context: remote to Mac Studio ✅
│  ├─ Ollama: localhost:11434 (1 model: nomic-embed-text, 274 MB)
│  ├─ This Claude Code session (running Solution Finder build)
│  └─ Access to Mac Studio services: Via Tailscale ✅
│
└─ T7 SHIELD + LACIE (External Drives — Cold Storage)
   ├─ T7 Shield (1.8 TB, Mac Studio)
   │  ├─ Status: 51% full, 922 GB available
   │  ├─ Contents: (needs inventory)
   │  ├─ Mount: /Volumes/T7\ Shield
   │  └─ Access: Local (Mac Studio) only
   │
   └─ Lacie (? TB, Mac Studio?)
      ├─ Status: (needs verification)
      ├─ Contents: (needs inventory)
      └─ Access: (needs verification)
```

---

## Where Does Each Venture's Data Live?

### Ventures Table (Supabase)
```
ventures table (789 rows)
├─ Venture ID, name, sector, status
├─ Readiness score + 12 sub-scores
├─ YTD revenue, pipeline value
├─ Contact info, GitHub repo, Vercel URL
├─ Last updated (timestamp)
└─ SYNCHRONIZED WITH: Neo4j (daily), VEX dashboard (real-time)
```

### Per-Venture Data

**OPS-001 (Staffing)**
```
Live: ops-staff-001-staffing.vercel.app
Data locations:
├─ Placements: Supabase.call_logs
├─ Revenue: Supabase.ventures.revenue_ytd
├─ Cold call tracking: PostgreSQL (Supabase)
├─ Contact list: Vercel env (CONTACTS_JSON)
└─ Code: repos/ops-staff-001-staffing/ (Mac Studio)
```

**LT-005 (Medical Courier)**
```
Live: healthroute-courier.vercel.app
Data locations:
├─ Orders: Supabase.orders
├─ Routes: Supabase.routes
├─ Driver tracking: Redis (real-time)
├─ Revenue: Supabase.ventures.revenue_ytd
├─ Documents: Vercel blob storage
└─ Code: repos/lt-005-healthroute-courier/ (Mac Studio)
```

**CON-001 (Construction)**
```
Live: con-001-ace-construction.vercel.app
Data locations:
├─ Projects: Supabase.projects
├─ Readiness score: Supabase.ventures.readinessPercent
├─ JotForm submissions: JotForm API
├─ Revenue: Supabase.ventures.revenue_ytd
├─ Contact data: Supabase.contacts
└─ Code: repos/con-001-ace-construction/ (Mac Studio)
```

**RE-001 (Real Estate)**
```
Live: re-001-worldwidebro-holdings.vercel.app
Data locations:
├─ Deal pipeline: Supabase.deals
├─ Properties: Supabase.properties
├─ Revenue: Supabase.ventures.revenue_ytd
├─ Property images: Vercel blob storage
├─ Contracts: Vercel blob storage
└─ Code: repos/re-001-worldwidebro-holdings/ (Mac Studio)
```

### 7 More Tier-0 + 782 Others
```
Pattern:
├─ Master record: Supabase.ventures (1 row)
├─ Per-venture domain data: sector-specific tables (Supabase)
├─ Deployment: Vercel (domain-specific)
├─ Relationships: Neo4j (venture nodes + edges)
└─ Code: repos/{sector}-ventures/ (Mac Studio)
```

---

## Critical Data Access Paths

### Path 1: Real-Time Data (Supabase → Vercel → User)
```
User → Vercel (vex-hero-site-sigma.vercel.app)
       → Supabase REST API
       → PostgreSQL query
       → Return venture data
       
Latency: ~100ms
Freshness: Real-time (seconds)
```

### Path 2: Relationship Data (Neo4j → Claude Code)
```
Claude/Agent → Neo4j bolt://100.87.214.70:7687
            → Cypher query
            → Return nodes + edges
            
Latency: ~50ms (local network)
Freshness: ~5 min (manual syncs)
```

### Path 3: Semantic Search (Qdrant → Agent)
```
Agent → Qdrant http://100.87.214.70:6333
      → Vector search
      → Return similar patterns
      
Latency: ~30ms (local network)
Freshness: Real-time (as solutions are registered)
```

### Path 4: Routing/Orchestration (OmniRoute)
```
Agent → OmniRoute http://100.87.214.70:20128
      → Dispatch to 110 tools
      → Route to appropriate tool
      
Latency: ~50ms (tool dispatch)
Freshness: Real-time
```

### Path 5: Code Discovery (Git repos on Mac Studio)
```
Solution Finder → /Users/acebless/Documents/The\ Company/Company\ Brain/repos/
                → Grep/graft
                → Return code paths
                
Latency: ~100ms
Freshness: As-checked-in (every commit)
```

---

## Sync Status: Real-Time vs. Batch

| Data | Source | Destination | Sync Method | Freshness | Status |
|------|--------|-------------|------------|-----------|--------|
| **Ventures** | Supabase | VEX | Real-time (REST) | Seconds | ✅ |
| **Ventures** | Supabase | Neo4j | Batch (daily) | ~24h | 🟡 |
| **Solutions** | Neo4j | Qdrant | On-register | Real-time | 🟡 |
| **Code paths** | Git repos | Solution Finder | On-query | Real-time | ✅ |
| **Metrics** | Supabase | VEX | Real-time (REST) | Seconds | ✅ |
| **Revenue** | Vercel/Stripe | Supabase | Webhook | Seconds | ✅ |
| **Logs** | Vercel | Datadog/Loki | Streaming | Real-time | 🟡 |
| **Backups** | Supabase | T7 Shield | Daily (manual) | ~24h | 🔴 |

**Gap:** Batch sync from Supabase → Neo4j takes 24h. Should be hourly or real-time.

---

## T7 Shield Inventory (UNKNOWN)

**Critical:** We don't know what's on T7 Shield.

```bash
# Inventory T7 Shield (from Mac Studio)
ssh macstudio
ls -lh /Volumes/T7\ Shield/

# Expected size: ~900 GB used
# Questions:
# - What's the oldest backup?
# - What's the newest?
# - Any venture data on there?
# - Any database backups?
# - Any media files (videos, images)?
```

**Action needed:** Catalog T7 Shield contents + sync strategy.

---

## Lacie Inventory (UNKNOWN)

```bash
# Find Lacie drives connected to Mac Studio
ssh macstudio
diskutil list
mount | grep -i lacie
```

**Action needed:** Verify Lacie exists, mount it, inventory contents.

---

## OmniRoute Data Distribution

```
OmniRoute (http://100.87.214.70:20128)
├─ 110 tools configured
├─ Which venture uses which tools? → Unknown mapping
├─ Tool outputs → Where stored?
├─ Tool metadata → Where cached?
└─ Tool performance metrics → Not tracked
```

**Gap:** OmniRoute data is not connected to venture graph.

---

## Unified Data Access Strategy

**To make everything visible from VEX:**

```
VEX Dashboard
├─ Queries Supabase for venture data ✅
├─ Queries Neo4j for relationships 🟡 (latency issue)
├─ Queries Qdrant for solution metrics 🟡 (not wired yet)
├─ Queries OmniRoute for tool usage 🔴 (not tracked)
├─ Shows Vercel deployment status 🔴 (not linked)
└─ Shows T7 Shield backup status 🔴 (unknown)
```

---

## Recommendations

### Immediate (This Week)
1. **Inventory T7 Shield** (30 min)
   ```bash
   du -sh /Volumes/T7\ Shield/* | sort -h
   ```

2. **Verify Lacie** (15 min)
   ```bash
   diskutil list
   ```

3. **Map OmniRoute to Ventures** (1h)
   ```
   Create: ventures → tools mapping in Neo4j
   Add edges: Venture -[USES_TOOL]→ OmniRouteTool
   ```

4. **Add Hourly Neo4j Sync** (2h)
   ```bash
   # Currently: manual/daily
   # Target: Every 1h via scheduled job
   ```

### This Month
5. **Persistent Data Sync** (NFS mount or Syncthing)
   ```bash
   # Mac Air ↔ Mac Studio: Real-time sync
   # Instead of: Manual rsync
   ```

6. **Vercel Deployment Tracking** (1h)
   ```
   Add to Neo4j: Venture -[DEPLOYED_TO]→ VercelProject
   Track: URL, status, last deploy time
   ```

7. **Backup Automation** (2h)
   ```bash
   # T7 Shield: Daily snapshots
   # Lacie: Off-site backup
   # Supabase: Automated backups (already enabled)
   ```

---

## Success Criteria

- [ ] VEX shows real-time data from all sources
- [ ] Data freshness: Seconds for transactional, <1h for relationships
- [ ] T7 Shield inventory complete + sync strategy defined
- [ ] Lacie status verified + contents known
- [ ] OmniRoute data connected to venture graph
- [ ] No data access latency >1s from VEX
- [ ] All 789 ventures visible in unified view

---

**Status:** 40% of data discoverable, 60% scattered.  
**Next:** Wire the scattered pieces together.

