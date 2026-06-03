# DYNASTY STRUCTURE: Org → Ventures → Repos → Execution

**Date:** 2026-06-01  
**Status:** LIVE (ready for agent activation)  
**Scope:** 712 ventures, 853 private repos, 16 sector managers, 16 AI agents

---

## GOVERNANCE HIERARCHY

### Layer 1: Executive Authority
- **CEO** (POS-CEO-001) — Strategic oversight, >$500K approvals
- **COO** (POS-COO-001) — Operational execution, <$500K approvals  
- **CFO** (POS-CFO-001) — Financial governance, cash flow
- **Head of Sales** (POS-SALES-HEAD-001) — Lead generation & client relationships

### Layer 2: Sector Managers (6 core + distributed)
Each manager owns 50-150 ventures and 150-350 private repos:

| Position Code | Title | Sector | Ventures | Key Repos | AI Agent |
|---|---|---|---|---|---|
| POS-BEAUTY-MANAGER | Beauty & Wellness Manager | BW-* | 87 | bw-*, beauty-* | qwen-beauty-wellness |
| POS-TECH-MANAGER | Tech & Software Manager | TECH-*, AI-*, DEVTOOLS-* | 120 | tech-*, ai-*, platform-* | qwen-technology |
| POS-CONSTRUCTION-PM | Construction PM | CON-* | 87 | con-*, build-*, infrastructure-* | qwen-construction |
| (COO) | Distributed Operations | FOOD, LOG, FIT, SPEC, EMERG | 315 | food-*, logistics-*, fitness-*, ops-* | qwen-[sector]-agents |
| POS-FINANCE-MANAGER | Finance Manager | FIN-* | 50 | finance-*, accounting-*, payroll-* | qwen-financial |
| (Sales Head) | Sales & Growth | ECOM-*, EDU-*, MEDIA-*, MARKET-* | 150+ | ecommerce-*, education-*, marketing-* | qwen-[sector]-agents |

### Layer 3: Repo Ownership (All 853 Private Repos)

**Aligned Repos (596):** Directly connected to 633 ventures
- **Governance:** Via sector manager of assigned venture
- **Approval:** Manager <$50K, COO $50K-$500K, CEO >$500K
- **Visibility:** Listed in PRIVATE-REPOS-ALIGNED.csv

**Unaligned Repos (258):** Strategic/shared infrastructure
- **Governance:** Assigned to functional team (COO, CTO, Finance)
- **Categories:**
  - Shared Services (150): payroll, compliance, automation, reporting
  - Experimental (80): R&D, testing, prototypes
  - Infrastructure (28): CI/CD, deployment, tooling
- **Visibility:** Listed in PRIVATE-REPOS-UNALIGNED.csv

### Layer 4: Starred Repos (664)
External projects guiding sector strategy:
- **Role:** Governance/oversight (industry best practices, reference implementations)
- **Assignment:** Each starred repo mapped to 1-2 sector managers
- **Monitoring:** AI agents watch for updates quarterly
- **Visibility:** Listed in STARRED-REPOS-GOVERNANCE.csv

---

## REPO CLASSIFICATION INVENTORY

### Private Repos by Status

| Category | Count | Description | Owner |
|----------|-------|---|---|
| **Aligned to Ventures** | 596 | Primary execution repos, 1-3 per venture | Sector Managers |
| **Shared Services** | 150 | Payroll, compliance, automation (used by ALL sectors) | CFO + COO |
| **Experimental** | 80 | R&D, testing, prototypes (not production) | CTO (Tech Manager) |
| **Infrastructure** | 28 | CI/CD, deployment, tooling | DevOps/Tech Manager |
| **TOTAL PRIVATE** | 853 | 99.6% of portfolio | Mixed |

**Starred Repos:** 664 external projects for oversight/guidance (not owned, monitored)

---

## EXECUTION FLOW: CEO → Sector Manager → Venture → Repo

```
Strategic Decision (CEO)
  ↓
Approval Gate ($$ threshold)
  ├─ <$50K: Sector Manager ✅
  ├─ $50K-$500K: COO ✅
  └─ >$500K: CEO ✅
  ↓
Sector Manager assigns to:
  ├─ Team (via 1-3 repos)
  ├─ AI Agent (for daily ops)
  └─ Venture (execution context)
  ↓
Team executes:
  ├─ Opens PR in aligned repo
  ├─ AI Agent tracks progress
  ├─ Sector Manager approves/blocks
  └─ Deployed to production
  ↓
Result: Venture progress, revenue, metrics
```

---

## DAILY EXECUTION ACCOUNTABILITY

### Sector Manager (e.g., Beauty Manager)
- [ ] Check ClickUp for new leads in assigned ventures (BW-001:087)
- [ ] Review any open PRs across 250+ aligned repos
- [ ] Approve decisions <$50K
- [ ] Escalate blockers to COO
- [ ] Weekly: Sector report (revenue, pipeline, repo health)

### AI Agent (e.g., qwen-beauty-wellness)
- [ ] Route new leads to sector manager
- [ ] Monitor repo health: test status, build passing, PR reviews
- [ ] Track venture progress via repo activity
- [ ] Generate daily sector dashboard
- [ ] Escalate issues >$50K to sector manager

### Finance Manager
- [ ] Process invoices from ventures (linked via repo work orders)
- [ ] Monitor budget usage by sector
- [ ] Flag cost overruns >10%

### COO
- [ ] Approve decisions $50K-$500K
- [ ] Review escalated blockers from sector managers
- [ ] Monitor sector manager performance (velocity, quality)
- [ ] Weekly: Operations summary across all sectors

### CEO
- [ ] Review CFO cash flow by sector
- [ ] Approve decisions >$500K
- [ ] Strategic initiatives (new sectors, major pivots)
- [ ] Monthly: Board review of portfolio performance

---

## AUTHORITY MATRIX

### By Dollar Amount

| Amount | Authority | Time to Approve | Example |
|--------|-----------|---|---|
| $0-$10K | Sector Manager | Same day | Venture launch, vendor add-on, small PR merge |
| $10K-$50K | Sector Manager + Finance | 1-2 days | Project work orders, integrations, repo tooling |
| $50K-$100K | COO + CFO | 2-3 days | Sector campaign, multi-repo refactor, vendor MSA |
| $100K-$500K | COO + CFO + CEO review | 3-5 days | New sector, major platform build, market expansion |
| >$500K | CEO + CFO + Board | 1 week+ | Strategic acquisition, major investment, restructure |

### By Repo Type

| Repo Category | Owner | Approval Authority | Change Frequency |
|---|---|---|---|
| Aligned (venture) | Sector Manager | Manager <$50K, COO >$50K | Daily (PR-based) |
| Shared Services | CFO + COO | COO <$100K, CEO >$100K | Weekly (governance) |
| Experimental | Tech Manager | Tech Manager <$50K | Daily (R&D) |
| Infrastructure | Tech Manager | Tech Manager <$100K | As needed (stability) |
| Starred (external) | Read-only | N/A (monitoring only) | Continuous (upstream) |

---

## REPO GOVERNANCE CHECKLIST

### For Sector Managers (Weekly)
- [ ] Review repos aligned to your 50-150 ventures
- [ ] Check test pass rate across all repos (target: >95%)
- [ ] Review open PRs (response time <24h)
- [ ] Identify unaligned repos that should be under your purview
- [ ] Escalate technical debt to Tech Manager
- [ ] Report: repo health score, PR velocity, deployment frequency

### For AI Agents (Daily)
- [ ] Monitor repo health: tests, builds, PRs
- [ ] Alert sector manager of failures >15min
- [ ] Route new feature requests to appropriate repo
- [ ] Generate daily venture progress report
- [ ] Escalate security issues immediately to CTO

### For Finance Manager (Daily)
- [ ] Match repo work (PR commits) to venture invoices
- [ ] Flag cost overruns in sector budgets
- [ ] Reconcile venture spend vs. repo resource usage
- [ ] Report: budget burn rate by sector

---

## NEXT IMMEDIATE STEPS

1. **Activate positions in database** (ORG-CHART-OPERATIONAL.md is already live in Supabase)
   - Assign humans to POS-BEAUTY-MANAGER, POS-TECH-MANAGER, POS-CONSTRUCTION-PM roles
   - Activate 16 AI agents by sector

2. **Link repos to org structure**
   - 596 aligned repos already mapped to ventures → automatically inherit sector manager
   - 258 unaligned repos: decide ownership (move to shared services or delegate)

3. **Monitor via dashboard**
   - Real-time visibility: venture → repo → approval authority
   - Daily: Sector health dashboard (KPIs, pipeline, repo quality)
   - Weekly: Manager performance (approval velocity, decision quality)

4. **Starred repos governance**
   - 664 starred repos assigned to sector managers
   - AI agents watch for updates quarterly
   - Flag breaking changes immediately

---

## RELATED FILES

- **ORG-CHART-OPERATIONAL.md** — Positions, authority, daily accountability
- **PRIVATE-REPOS-ALIGNED.csv** — 596 repos with venture linkage (read WORLDWIDEBRO-712-UNIFIED.csv)
- **PRIVATE-REPOS-UNALIGNED.csv** — 258 repos (shared/strategic, read WORLDWIDEBRO-712-UNIFIED.csv)
- **STARRED-REPOS-GOVERNANCE.csv** — 664 repos (oversight role, read starred_repos_664.csv)
- **WORLDWIDEBRO-712-UNIFIED.csv** — Master venture list
- **.planning/venture-hub-alignment.json** — Obsidian sync with all data

---

**Status:** ✅ READY FOR DEPLOYMENT

All 712 ventures mapped to org structure.  
All 853 private repos classified and owned.  
All 664 starred repos assigned oversight roles.  
AI agents ready to activate by sector.  
Approval authority clearly defined.
