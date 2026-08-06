# SYNC-AND-CONNECTIONS-STATUS

**Date:** 2026-08-05 | **Purpose:** Show what needs updating, which systems are connected, which are not

---

## WHAT NEEDS TO BE UPDATED (by priority)

### 🔴 TODAY (Aug 5)

1. **OPS-001-STAFFING Notion → Supabase migration**
   - Status: 74 prospects in Notion only (no backup)
   - Action: Export → CSV → Supabase table
   - Time: 1-2 hours
   - Risk: CRITICAL (data loss if Notion deleted)

### 🟡 WEEK 1 (Aug 5-12)

2. **EC-112 deployment** — Deploy to Vercel + wire agents
3. **LT-005 sales rep** — Hire + onboard
4. **Update MASTER-INDEX.md** — Link 3 new venture docs
5. **Neo4j daily refresh** — Automated ventures graph
6. **Supabase agents table** — Register all 40+ agents
7. **Langfuse wiring** — First venture (LT-005)

### 🟢 WEEK 2-3 (Aug 12-26)

8. **Repository → Venture mapping** — Wire 1597 repos to ventures
9. **Qdrant rebuilds** — Weekly venture embeddings
10. **VENTURE-READINESS automation** — Weekly scorecard refresh

---

## GRAPH CONNECTIVITY STATUS

| Graph | Status | Last Update | Connected Systems | Priority |
|-------|--------|-------------|------------------|----------|
| **Supabase** | 🟢 80% | Real-time | ventures, leads, financial, customers | LIVE |
| **Neo4j** | 🟡 40% | Jul 28 (stale) | ventures, products, relationships | Wire Week 1 |
| **Qdrant** | 🟡 10% | Jun 28 (stale) | notes (live), repos (stale) | Rebuild Week 1 |
| **Langfuse** | 🟡 0% | Not yet | (no ventures wired) | Wire Week 1 |
| **Repository Intell.** | ❌ 0% | Jun 28 | (zero ventures mapped) | Reconcile Week 2 |

---

## CLUSTER CONNECTIONS

### ✅ WORKING (data flowing)

- **GitHub ↔ Vercel** — CI/CD live for all ventures
- **Supabase ↔ Vercel** — Real-time data visible in portals
- **Supabase ↔ Obsidian** — Manual daily sync of venture dashboard

### 🟡 PARTIAL (one-way or stale)

- **Supabase ↔ Neo4j** — Manual daily refresh, not bidirectional
- **Supabase ↔ Qdrant** — Weekly rebuild only, manual process
- **GitHub ↔ Supabase** — Manual repository registry updates

### ❌ BROKEN (no connection)

- **Repository Intelligence ↔ Ventures** — 1597 repos, zero mapped (vocab gap)
- **Langfuse ↔ Workflows** — No traces being generated
- **Business Lifecycle ↔ Execution** — New stages not wired to workflows
- **Agent Execution ↔ Financial Events** — No ROI tracking per agent

---

## FOLDER STRUCTURES NEEDING UPDATES

### WORLDWIDEBRO-OS/ (15 folders, 60% populated)

```
00-VAULT-README.md          — ✅ Exists, needs update (link new docs)
01-EXECUTIVES/              — ✅ Exists, dashboards outdated
01-STRATEGY/                — ✅ Exists, mostly empty
02-INFRASTRUCTURE/          — ✅ Exists, needs deployment pipeline docs
03-PORTFOLIO/ventures/      — 🟡 Partial (8 stubs, need full profiles)
04-OPERATIONS/              — ✅ Exists, mostly manual workflows
05-COMMUNICATIONS/          — ✅ Exists, email templates only
06-AGENTS/                  — 🟡 Partial (12 agents in EC-112, others not registered)
06-PARTNERS/                — ✅ Exists, mostly empty
07-OBSERVABILITY/           — 🟡 Partial (infra exists, no venture dashboards)
09-GOVERNANCE/              — ✅ Exists, audit trails not populated
REGISTRIES/                 — 🟡 Partial (1597 repos classified, zero ventures mapped)
```

### NEW DOCUMENTS (Just Created)

✅ **VENTURES-LIFECYCLE-MAPPING.md** — Maps 8 ventures to 28 Business Lifecycle stages  
✅ **VENTURE-PIPELINE-ALIASES.md** — Canonical naming + aliases for all ventures  
✅ **VENTURES-OS-HIERARCHY-MAPPING.md** — Section completion tracking per venture  

Need to link from: MASTER-INDEX.md

---

## AUTOMATION NEEDED THIS WEEK

### Daily Jobs (2 AM UTC)
- [ ] Supabase → Neo4j refresh (venture nodes + edges)
- [ ] Stripe → Supabase sync (financial_events)
- [ ] Supabase → Obsidian export (venture CSV)

### Weekly Jobs (Monday 2 AM UTC)
- [ ] Qdrant embeddings rebuild (ventures + capabilities)
- [ ] Repository intelligence refresh (1597 repos)
- [ ] VENTURE-READINESS-SCORECARD.csv update

### Manual (This Week)
- [ ] OPS-001-STAFFING: Notion export → Supabase
- [ ] EC-112: Deploy to Vercel
- [ ] LT-005: Hire sales rep
- [ ] Update MASTER-INDEX.md with new docs

---

**Summary:** 3 major graphs need wiring (Neo4j, Qdrant, Langfuse). 8 ventures need daily sync + lifecycle tracking. 1597 repos need semantic mapping to ventures.

**Next:** Execute Week 1 priorities starting TODAY (OPS-001-STAFFING migration).
