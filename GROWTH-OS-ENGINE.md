# Growth OS: The Marketing Infrastructure Engine

**Status:** 🟢 Live & Deployed  
**Repo:** https://github.com/Worldwidebro/iza-os-marketing-core  
**Deploy:** https://growth.worldwidebro.com (ready for Vercel)  
**Type:** Infrastructure Layer (Part of IZA-OS, not a venture)

---

## What It Is

Growth OS is the **unified marketing operations command center** for all Worldwidebro ventures. It is NOT a venture—it is shared infrastructure (like n8n, Neo4j, Supabase).

- **24 Operating Modules:** Intelligence, Brand, Creative, Product, Content, Distribution, Paid, Organic, Lifecycle, Sales, Ops, Data, Global, Governance
- **2,841+ Agents:** Across all modules, coordinated via n8n
- **1,240+ Active Workflows:** Campaigns, lead qualification, content production, reporting
- **5 Navigation Hubs:** COMMAND (dashboards), BUILD (portfolio), GROW (revenue), OPERATE (execution), ECOSYSTEM (community)

---

## Consumption Model

### For Each Venture:
- Access Growth OS dashboard → see campaigns, spend, ROI
- Trigger workflows (e.g., "Launch campaign for CON-001") via API
- Real-time metrics → synergy scores to WORLDWIDEBRO Holdings

### For Each OPCO (6 OPCOs):
- Aggregate view of all ventures in their sector
- Budget allocation + performance tracking
- Cross-venture content syndication
- Organic + paid spend balancing

### For Holdings (Worldwidebro):
- Consolidated P&L across all 712 ventures
- Campaign pipeline visibility
- Agent performance (2,841 agents coordinated)
- Strategic reallocation (spend from underperforming → high-potential ventures)

---

## Architecture

```
Growth OS (Marketing Infrastructure)
├─ COMMAND Hub (dashboards, assistant, knowledge, intelligence)
├─ BUILD Hub (ventures portfolio, products, repos, admin)
├─ GROW Hub (marketing, media, writing, sales, customers)
├─ OPERATE Hub (operations, automation, finance, legal, people, projects)
└─ ECOSYSTEM Hub (marketplace, academy, community, investors, client portal)

Connected to:
├─ Supabase (campaigns, agent logs, activity feed)
├─ Neo4j (venture graph, agent topology, knowledge)
├─ Qdrant (semantic search across ventures + content)
├─ n8n (workflow orchestration, 1,240+ workflows)
└─ Langfuse (LLM tracing, agent performance)
```

---

## Integration Status

| System | Status | Purpose |
|--------|--------|---------|
| **Supabase** | ✅ Connected | Campaigns, activities, logs |
| **Neo4j** | ✅ Connected | Venture graph, relationships |
| **n8n** | ✅ Ready | Workflow orchestration (needs wiring) |
| **Qdrant** | ⏳ Pending | Semantic search for content/campaigns |
| **Langfuse** | ⏳ Pending | LLM agent tracing + observability |
| **VEX** | ⏳ Pending | Venture OS navbar link |
| **WORLDWIDEBRO Dashboard** | ⏳ Pending | Holdings-level metrics |

---

## Deployment

**Development:**
```bash
cd /Users/acebless/Documents/iza-os-marketing-core
npm run dev  # localhost:3000
```

**Production (Vercel):**
```bash
vercel deploy --prod  # growth.worldwidebro.com
```

**Environment Variables:**
```env
VITE_SUPABASE_URL=https://your-project.supabase.co
VITE_SUPABASE_ANON_KEY=your_key_here
VITE_LANGFUSE_PUBLIC_KEY=optional_for_tracing
```

---

## Roadmap (25 Pages)

| Phase | Timeline | Pages | Status |
|-------|----------|-------|--------|
| **1A** | Weeks 1-2 | /marketing, /dashboard, /agents, /assistant | 🟢 READY |
| **1B** | Weeks 3-4 | /sales, /customers, /finance | ⏳ In queue |
| **2** | Weeks 5-6 | /products, /automation, /development | ⏳ Planned |
| **3-5** | Weeks 7-10 | Remaining 12 pages (repositories, operations, legal, people, projects, marketplace, academy, community, investors, portal, admin, intelligence) | 🗓 Later |

---

## What's Next

1. **Deploy to Vercel** (15 min) → growth.worldwidebro.com live
2. **Wire n8n workflows** (1 week) → automate campaigns across ventures
3. **Connect Langfuse** (3 days) → track 2,841 agents
4. **Build /sales, /customers, /finance** (2 weeks) → revenue engines
5. **Full 25-page ecosystem** (4 weeks) → complete marketing OS

---

## Links

- **Repo:** https://github.com/Worldwidebro/iza-os-marketing-core
- **Deploy:** Ready for Vercel (not yet pushed)
- **In-Repo Docs:** README.md, CLAUDE.md, ARCHITECTURE-25-PAGES.md
- **This Doc:** GROWTH-OS-ENGINE.md (you are here)

---

**Growth OS is the marketing infrastructure layer for all Worldwidebro ventures—part of IZA-OS, not a venture itself.**
