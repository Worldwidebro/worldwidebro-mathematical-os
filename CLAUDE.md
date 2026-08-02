# Worldwidebro Holdings Operating Protocol (v1.0)

**Scope**: All 712 ventures + Hermes agent + shared platform  
**Effective**: 2026-07-30  
**Enforcement**: TAGGING-STANDARD.md (mandatory for all requests)

---

## 🎯 PHASE 1: FOCUS VENTURES (8 Parallel)

**Live agents** (spawned 2026-07-30, TRAINING stage):
| Venture | Sector | Agents | Status |
|---------|--------|--------|--------|
| LT-005 | Logistics | 3 | TRAINING |
| CON-001 | Construction | 3 | TRAINING (live on Vercel) |
| STA-001 | Staffing | 3 | TRAINING |
| OPS-001 | Operations | 3 | TRAINING |
| EC-001 | E-commerce | 3 | TRAINING |
| EC-112 | E-commerce | 3 | TRAINING |
| RE-001 | Real Estate | 3 | TRAINING |
| LT-011 | Logistics | 3 | TRAINING |

**Timeline**: Week 1-2 training cycle → Monday eval → APPROVAL stage (Week 2)  
**Total agents**: 24 coordinated via Neo4j  
**Next**: OpCo engines per sector (defer to Phase 2)

---

## ⚠️ THE ACTUAL SYSTEM ISSUE (2026-08-01)

**Problem:** 70GB of stale files should be LIVE queries. Services running but isolated. ClickUp doesn't know architecture.

### What's Broken

| Problem | Example | Fix |
|---------|---------|-----|
| **Stale file data** | VENTURE-REGISTRY.json (2MB, manual) | → Query `SELECT * FROM ventures` (live) |
| **Duplicate exports** | VENTURES-CAPABILITIES-MAPPED.csv | → Query Neo4j relationships (live) |
| **Isolated services** | Langfuse/Prometheus running, not wired | → Wire to vex dashboards (5 scripts) |
| **Two CRM systems** | ClickUp + Twenty (both running) | → Use ClickUp only, delete Twenty |
| **ClickUp isolated** | Tasks don't reference infrastructure | → Add GitHub Issues for code work |
| **Manual dashboards** | STAFFING-AGENCY-STATUS.md | → Auto-generate from queries |

### Services Running But Not Integrated

```
✅ Supabase (localhost:5432)          → Queries work
✅ Neo4j (localhost:7687)             → Not synced from knowledge/
✅ Qdrant (localhost:6333)            → Not connected to searches
✅ Langfuse (localhost:3003)          → Not feeding dashboards
✅ Prometheus (localhost:9090)        → Not connected to Grafana
✅ Grafana (localhost:3001)           → Not integrated with vex
✅ LiteLLM (localhost:4000)           → Not connected to agents
✅ Redis (localhost:6379, :6380)      → Not used for caching
✅ Twenty CRM (localhost:3002)        → Duplicate, unused
✅ Ollama + FreeLLM                   → Not connected to anything
```

**Reality:** You have infrastructure worth $500K. None of it talks to Vex.

### Solution: 5 Connector Scripts (Wired 2026-08-01)

**Status:** ✅ Scripts created. Awaiting GitHub secrets + workflow activation.

| Script | Wires | Schedule | Status |
|--------|-------|----------|--------|
| **1. clickup-sync.js** | ClickUp → Supabase | Every 15 min | ✅ Created |
| **2. markdown-to-neo4j.js** | knowledge/ → Neo4j | Every 4 hours | ✅ Created |
| **3. ceo-dashboard.js** | Supabase → API | Every 30 min | ✅ Created |
| **4. langfuse-metrics.js** | Langfuse → Prometheus | Every 8 hours | ⏳ Queued |
| **5. send-daily-brief.js** | All sources → Email | 8am UTC daily | ⏳ Queued |

**Automation:** All scripts run via GitHub Actions. You DON'T run commands manually.
- GitHub Actions triggered by cron schedules (no user action needed)
- Secrets configured once (manual setup: 5 min)
- Then fully automatic forever

**How to Use:**
1. Add GitHub secrets (CLICKUP_API_KEY, SUPABASE_URL, etc.)
2. Merge this branch to main
3. Workflows activate automatically
4. Check dashboards in 15 minutes (ClickUp data syncs first)

---

## ONE RULE: Tag Every Request (For Business Tasks in ClickUp)

**Every request must include `[VENTURE]`, `[ACTION]`, `[STATUS]` to work.**

```
[VENTURE]      CON-001
[ACTION]       BUILD | TEST | DEPLOY | CONNECT | AUDIT | FIX
[STATUS]       NOT_STARTED | IN_PROGRESS | BLOCKED | TESTING | READY | DEPLOYED | LIVE
[PRIORITY]     P0 (critical) | P1 (high) | P2 (medium) | P3 (low) | P4 (nice)
[OBJECTIVE]    One-liner: what should happen when done?
```

**Example**:
```
[VENTURE] CON-042
[ACTION] CONNECT
[STATUS] IN_PROGRESS
[PRIORITY] P1
[OBJECTIVE] Enable form submissions to create CRM leads
```

Without tags → request rejected with link to TAGGING-STANDARD.md  
With tags → Hermes loads context, 95% success rate

See TAGGING-STANDARD.md for complete vocabulary + Hermes routing.

---

## GitHub Issues vs ClickUp (Where Tasks Live)

### ✅ ClickUp = Business Execution (Real-time)

```
STA-001: Call 50 prospects
STA-001: Close first placement
STA-001: Schedule interviews
STA-001: Follow up on offers

CON-001: Contact 5 leads
CON-001: Send proposals
CON-001: Approve invoices

Finance: Approve vendor contract
HR: Onboard engineer
Operations: Weekly review
```

**Principle:** ClickUp is LIVE. Tasks represent actual work happening NOW. Data syncs to dashboards in real-time.

### ❌ ClickUp Does NOT Include Code Work

These tasks **DO NOT belong in ClickUp** (they belong in GitHub Issues):

```
❌ Deploy vex to Vercel
❌ Wire ClickUp→Supabase sync
❌ Write markdown-to-neo4j.js
❌ Add CEO dashboard queries
❌ Delete node_modules/
❌ Clean up archives/
❌ Update GitHub Actions
```

**Principle:** Code work = GitHub Issues + git commits. Business work = ClickUp tasks.

### The Architecture That Emerges

```
BUSINESS (ClickUp) ──(sync)──> DATABASE (Supabase)
  Call 50 prospects             Live prospect list
  Close placement               Live revenue
  Weekly review                 Live KPIs
  
                                    ↓
                            
CODE (GitHub) ──(queries)──> DASHBOARDS (Vex)
  Write sync script              Live metrics
  Add dashboard queries          Live CEO view
  Wire Langfuse                  Live AI insights
```

**ClickUp doesn't need to know about:**
- GitHub branches
- Docker containers
- Neo4j schemas
- Langfuse events

**But vex dashboards MUST pull from ClickUp** (via sync script).

---

## What Should Happen This Week

### GitHub Issues (Code Work)

```
[ ] 1. Consolidate vex-api + vex-hero-site into vex/ monorepo
[ ] 2. Write clickup-sync.js (ClickUp API → Supabase)
[ ] 3. Write markdown-to-neo4j.js (knowledge/ → Neo4j)
[ ] 4. Add dashboard queries (api/routes/dashboards.js)
[ ] 5. Add dashboard components (app/src/pages/dashboard/)
[ ] 6. Write send-daily-brief.js (morning email)
[ ] 7. Update GitHub Actions (auto-sync workflows)
[ ] 8. Delete archives, node_modules, old files (70GB cleanup)
```

### ClickUp (Business Work - Already Correct)

```
✅ STA-001: Call 50 prospects/day
✅ STA-001: Close first placement by 2026-08-29
✅ CON-001: Follow up on leads
✅ Finance: Approve contracts
✅ HR: Onboard engineers
```

**ClickUp needs NO changes. It's working correctly.**
**GitHub needs 8 code tasks to wire everything together.**

---

## STA-001: Staffing Agency Operations

**Status:** TRAINING (Week 1 launch 2026-08-04)  
**Tracking:** ClickUp (real-time) + Weekly MD summary (STAFFING-AGENCY-STATUS.md)  
**Daily Update:** 8am UTC (auto-syncs Fri EOD metrics via GitHub Actions)  
**Goal:** Close 1st placement by 2026-08-29

### Execution Infrastructure

| Component | Location | Purpose |
|-----------|----------|---------|
| **Daily tracking** | ClickUp Staffing Agency space | Task execution (calls, orders, candidates) |
| **Call log** | `templates/WEEKLY-CALL-SHEET.md` | Daily outreach (50 calls/day, outcomes) |
| **Job capture** | `forms/customer/onboarding/client-intake.html` | Company hiring needs → job orders |
| **Candidate capture** | `forms/employee/onboarding/candidate-application.html` | Candidate profiles + applications |
| **Weekly summary** | `STAFFING-AGENCY-STATUS.md` | Metrics, revenue, blockers, sector performance |
| **Extraction script** | `scripts/extract-from-career-ops.mjs` | Career-ops reports → call sheet |

### ClickUp Lists (Staffing Agency Space)
- **Target Accounts** (1000210000002320) — Prospect lists, outreach campaigns
- **Client Job Orders** (1000210000002235) — Locked job specs (JO-001, JO-002...)
- **Candidate Pipeline** (1000210000002236) — Sourced → Submitted → Interviews → Closed
- **Placements & Billing** (1000210000002237) — Closed deals + invoices ($10-22K/placement)

### How to Know Status (Conversion Tracking)

**Truth Sources:** ClickUp lists > STAFFING-AGENCY-STATUS.md (weekly) > WEEKLY-CALL-SHEET.md (daily)

| Stage | Evidence | Where to Check |
|-------|----------|-----------------|
| Prospect | Called, no JO | WEEKLY-CALL-SHEET.md rows |
| **→ Client** | Signed agreement | client-intake.html form captured |
| **→ Active** | Has ≥1 Job Order | ClickUp "Client Job Orders" (JO-001, etc.) |
| **→ Placement** | Candidate sent | ClickUp "Candidate Pipeline" (Submitted status) |
| **→ Closed** | Accepted + paid | ClickUp "Placements & Billing" + Supabase `deal_payments` |

✅ **Real conversion:** Company in "Client Job Orders" list = active (generating jobs)  
✅ **Real revenue:** Entry in "Placements & Billing" = placement closed (payment received)

### Weekly Cycle

**Mon-Fri Execution:**
- Log calls/outcomes in ClickUp
- Fill forms (client-intake, candidate-app) on YES responses
- Update weekly call sheet daily

**Fri EOD Summary:**
- Export ClickUp data
- Update STAFFING-AGENCY-STATUS.md with weekly metrics
- Identify blockers + priorities

**Daily 8am Auto-Update:**
- GitHub Actions workflow fetches ClickUp data
- Updates STAFFING-AGENCY-STATUS.md metrics
- Auto-commits + pushes

**Monthly:**
- Compile YTD revenue + sector analysis
- Leadership report from STAFFING-AGENCY-STATUS.md

---

## Venture Remote Environments

**Master inventory:** `VENTURES-REMOTE-ENV.md` (auto-updated daily 8am)

Tracks all ventures' Supabase instances, Vercel deployments, Stripe configurations, and environment variables.

**Current status:**
- ✅ **Live:** CON-001 (Vercel), vex-hero-site (Vercel)
- 🚀 **Ready to deploy:** LT-005, vex-api
- 🔄 **In training:** STA-001, EC-111, RE-001, OPS-001

**See** `VENTURES-REMOTE-ENV.md` for `/supabase`, `/stripe`, `/vercel` config status per venture + T7 backup mount path

---

## Document Metadata Header

Every venture-specific document starts with:
```
[Venture]       CON-001
[Sector]        construction
[Status]        LIVE
[Owner]         Name
[Updated]       2026-07-30
[Confidence]    VERIFIED | ESTIMATED | ASSUMED | UNCONFIRMED
[Source]        SUPABASE, GITHUB, VERCEL
```

---

## Shared Architecture (25 Core Documents)

Built once, used by all 712 ventures:

**Foundation**: ARCHITECTURE.md, SYSTEM_OVERVIEW.md, DOMAIN_MODEL.md, CAPABILITY_MAP.md, SERVICE_CATALOG.md  
**Standards**: CODING_STANDARDS.md, API_STANDARDS.md, DATA_MODEL.md, SECURITY.md, REPOSITORY_STANDARD.md  
**Intelligence**: AI_ARCHITECTURE.md, AGENT_STANDARD.md, MODEL_ROUTING.md, KNOWLEDGE_GRAPH.md, RAG.md  
**Operations**: RUNBOOK.md, PLAYBOOK.md, INFRASTRUCTURE.md, CI_CD.md, OBSERVABILITY.md  

See ARCHITECTURE-CONSOLIDATION-ROADMAP.md for the complete 25-document framework.

Every venture's `.claude/CLAUDE.md` inherits this set + adds venture-specific overrides only.

---

## Enforcement Points

- GitHub Actions validates `[VENTURE]` in issue titles + PR descriptions
- Hermes agent requires `[ACTION]` + `[OBJECTIVE]` (rejects otherwise)
- Claude Code this session enforces tags or links to TAGGING-STANDARD.md
- VENTURE-REGISTRY.json is the source of truth for all 712 ventures

---

<!-- gitnexus:start -->
# GitNexus — Code Intelligence

This project is indexed by GitNexus as **Documents** (136574 symbols, 270211 relationships, 300 execution flows). Use the GitNexus MCP tools to understand code, assess impact, and navigate safely.

> Index stale? Run `node .gitnexus/run.cjs analyze` from the project root — it auto-selects an available runner. No `.gitnexus/run.cjs` yet? `npx gitnexus analyze` (npm 11 crash → `npm i -g gitnexus`; #1939).

## Always Do

- **MUST run impact analysis before editing any symbol.** Before modifying a function, class, or method, run `impact({target: "symbolName", direction: "upstream"})` and report the blast radius (direct callers, affected processes, risk level) to the user.
- **MUST run `detect_changes()` before committing** to verify your changes only affect expected symbols and execution flows. For regression review, compare against the default branch: `detect_changes({scope: "compare", base_ref: "main"})`.
- **MUST warn the user** if impact analysis returns HIGH or CRITICAL risk before proceeding with edits.
- When exploring unfamiliar code, use `query({search_query: "concept"})` to find execution flows instead of grepping. It returns process-grouped results ranked by relevance.
- When you need full context on a specific symbol — callers, callees, which execution flows it participates in — use `context({name: "symbolName"})`.
- For security review, `explain({target: "fileOrSymbol"})` lists taint findings (source→sink flows; needs `analyze --pdg`).

## Never Do

- NEVER edit a function, class, or method without first running `impact` on it.
- NEVER ignore HIGH or CRITICAL risk warnings from impact analysis.
- NEVER rename symbols with find-and-replace — use `rename` which understands the call graph.
- NEVER commit changes without running `detect_changes()` to check affected scope.

## Resources

| Resource | Use for |
|----------|---------|
| `gitnexus://repo/Documents/context` | Codebase overview, check index freshness |
| `gitnexus://repo/Documents/clusters` | All functional areas |
| `gitnexus://repo/Documents/processes` | All execution flows |
| `gitnexus://repo/Documents/process/{name}` | Step-by-step execution trace |

## CLI

| Task | Read this skill file |
|------|---------------------|
| Understand architecture / "How does X work?" | `.claude/skills/gitnexus/gitnexus-exploring/SKILL.md` |
| Blast radius / "What breaks if I change X?" | `.claude/skills/gitnexus/gitnexus-impact-analysis/SKILL.md` |
| Trace bugs / "Why is X failing?" | `.claude/skills/gitnexus/gitnexus-debugging/SKILL.md` |
| Rename / extract / split / refactor | `.claude/skills/gitnexus/gitnexus-refactoring/SKILL.md` |
| Tools, resources, schema reference | `.claude/skills/gitnexus/gitnexus-guide/SKILL.md` |
| Index, status, clean, wiki CLI commands | `.claude/skills/gitnexus/gitnexus-cli/SKILL.md` |

<!-- gitnexus:end -->