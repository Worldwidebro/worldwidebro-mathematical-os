# 📊 SYSTEM AWARENESS AUDIT
**Date:** 2026-08-05  
**Purpose:** Complete inventory of all files, tools, repos. Necessity scoring. Cost alignment.  
**Status:** Framework ready; you fill in scores

---

## SECTION 1: FILE INVENTORY BY SYSTEM

### Obsidian Vault

| File | Purpose | Necessity (0-1.0) | Revenue Driver | Notes |
|------|---------|----------|---|-------|
| WORLDWIDEBRO-OS/01-CEO/* | Strategic docs | 0.9 | YES | Read quarterly; blocks decisions |
| WORLDWIDEBRO-OS/02-OPS/* | Operations playbooks | 0.7 | MEDIUM | Used for onboarding; could be in Notion |
| WORLDWIDEBRO-OS/03-PORTFOLIO/* | Venture tracking | 0.8 | YES | Source of truth for venture status |
| WORLDWIDEBRO-OS/04-CUSTOMERS/* | Customer data | 0.6 | MEDIUM | Duplicates Supabase; consider delete |
| WORLDWIDEBRO-OS/05-FINANCE/* | Financial models | 0.9 | YES | Used for pricing; move to Notion? |
| WORLDWIDEBRO-OS/06-TECH/* | Tech architecture | 0.5 | NO | Aspirational; rarely read |
| WORLDWIDEBRO-OS/07-KNOWLEDGE/* | Research notes | 0.3 | NO | Stale; archive 80% |
| WORLDWIDEBRO-OS/08-PEOPLE/* | Team info | 0.4 | NO | Outdated; use ClickUp instead |
| **Obsidian Total** | **8 folders** | **0.61 avg** | — | **Consolidation target: move 40% to Notion** |

### File System (Documents root)

| File | Purpose | Necessity | Revenue Driver | Notes |
|------|---------|----------|---|-------|
| AGENTS.md | Agent intelligence types | 0.8 | YES | Used for agent dispatch |
| MASTER-INDEX.md | Central navigation | 0.9 | NO | Navigation only; nice-to-have |
| REPOS-ORGANIZATION-MAP.md | Repo taxonomy | 0.7 | MEDIUM | Used for capability lookup |
| VENTURE-READINESS-SCORECARD.csv | Venture status | 0.95 | YES | **Critical**: source of truth |
| TASKS-TO-FIRST-REVENUE.md | Sprint roadmap | 0.8 | YES | Active use through Week 12 |
| task_plan.md | Historical tasks | 0.1 | NO | **Archive**: superseded by TASKS-TO-FIRST-REVENUE |
| build_kg.py | Knowledge graph builder | 0.6 | MEDIUM | Runs weekly; could be cron job |
| bootstrap_venture.py | Venture creation | 0.7 | YES | Used for new ventures |
| **Filesystem Total** | **40+ files** | **0.65 avg** | — | **Quick wins: delete task_plan.md, old docs** |

### Apple Notes (Mobile)

| Note | Purpose | Necessity | Revenue Driver | Notes |
|------|---------|----------|---|-------|
| Daily standup notes | Capture mobile ideas | 0.7 | MEDIUM | Will be synced via Agent 1.1 |
| Customer calls | CRM input | 0.8 | YES | Currently dark; must integrate |
| Product ideas | Innovation backlog | 0.3 | NO | Ideas decay; not actionable |
| **Apple Notes Total** | **N/A (unstructured)** | **0.6 avg** | — | **Action: wire via Agent 1.1** |

### Database (Supabase)

| Table | Purpose | Necessity | Revenue Driver | Notes |
|------|---------|----------|---|-------|
| ventures | Live venture state | 0.99 | YES | **CRITICAL**: master record |
| venture_leads | Sales pipeline | 0.95 | YES | **CRITICAL**: money tracker |
| customers | Customer records | 0.95 | YES | **CRITICAL**: LTV calculation |
| deal_payments | Revenue events | 0.95 | YES | **CRITICAL**: income proof |
| apple_notes_inbox | Mobile capture | 0.8 | MEDIUM | Will be active post-1.1 |
| venture_readiness | Venture scoring | 0.7 | YES | Duplicates CSV; consolidate? |
| user_profiles | Team info | 0.3 | NO | Outdated; use ClickUp |
| **Supabase Total** | **7 tables active** | **0.84 avg** | — | **Consolidate venture_readiness → CSV** |

### Knowledge Graphs

| Store | Purpose | Necessity | Revenue Driver | Notes |
|------|---------|----------|---|-------|
| Neo4j | Code + venture relationships | 0.6 | MEDIUM | Currently offline; not blocking revenue |
| Qdrant | Semantic search (15,558 vectors) | 0.5 | LOW | Stale; used for search only |
| Obsidian Dataview | Vault queries | 0.6 | LOW | Nice-to-have; could replace with Notion DB |
| **Graph Total** | **3 stores** | **0.57 avg** | — | **Action: only fix Neo4j if revenue blocked** |

---

## SECTION 2: TOOL STACK COST ANALYSIS

### Services (Infrastructure)

| Tool | Monthly Cost | Necessity | Revenue Impact | Action |
|------|----------|-----------|----------|--------|
| **Supabase** | $25-50 | 0.99 | YES | KEEP; non-negotiable |
| **Neo4j** | $15 (hobby) | 0.4 | NO | PAUSE; restart if revenue scales |
| **Qdrant** | $0 (local) + infra | 0.3 | NO | CONSOLIDATE to Supabase pgvector |
| **Redis** | $0 (local) | 0.4 | MEDIUM | ARCHIVE if not used daily |
| **Langfuse** | $0 (local) | 0.2 | NO | ARCHIVE; use Supabase logs |
| **Vercel** | $20-50 | 0.8 | YES | KEEP (deployment critical) |
| **Ngrok** | $10-20 | 0.3 | NO | DELETE (only for webhooks) |
| **Subtotal** | **$70-155/mo** | — | — | **Consolidation: cut to $35-50/mo** |

### Automation (Rules-Based)

| Tool | Monthly Cost | Necessity | Revenue Impact | Action |
|------|----------|-----------|----------|--------|
| **Zapier** | $20-50 | 0.7 | YES | OPTIMIZE (use Trigger.dev instead?) |
| **Make** | $0-100 | 0.4 | LOW | ARCHIVE (duplicate of Zapier) |
| **n8n** | $100-500 | 0.3 | LOW | **REPLACE with LangGraph** (Task 2.3) |
| **Subtotal** | **$120-650/mo** | — | — | **Consolidation: cut to $20-50/mo (Zapier only)** |

### Collaboration (Docs)

| Tool | Monthly Cost | Necessity | Revenue Impact | Action |
|------|----------|-----------|----------|--------|
| **Obsidian** | $0 | 0.6 | MEDIUM | KEEP (personal use) |
| **Notion** | $10 | 0.7 | YES | **UPGRADE to team plan ($150)** if scaling |
| **ClickUp** | $99-999 | 0.8 | YES | KEEP (execution hub) |
| **Subtotal** | **$109-1009/mo** | — | — | **Consolidation: ClickUp + Notion, archive Obsidian** |

### Development

| Tool | Monthly Cost | Necessity | Revenue Impact | Action |
|------|----------|-----------|----------|--------|
| **GitHub** | $21 | 0.9 | YES | KEEP |
| **VS Code** | $0 | 1.0 | YES | KEEP |
| **Claude** | $200-500 | 0.8 | YES | OPTIMIZE with OmniRoute (Task 2.3) |
| **Ollama (local)** | $0 | 0.6 | MEDIUM | USE for high-volume tasks |
| **Subtotal** | **$221-521/mo** | — | — | **No change (core tools)** |

### **TOTAL SYSTEM COST**

| Category | Cost | Necessity | Consolidation Potential |
|----------|------|-----------|-------------------------|
| Services | $70-155 | 0.6 avg | -$35/mo (qdrant, redis, langfuse) |
| Automation | $120-650 | 0.5 avg | -$100/mo (replace n8n + Make) |
| Collaboration | $109-1009 | 0.7 avg | -$0/mo (already optimal) |
| Development | $221-521 | 0.8 avg | -$120/mo (OmniRoute routing) |
| **TOTAL** | **$520-2335/mo** | — | **Potential savings: $255-255/mo (45-70%)** |

---

## SECTION 3: REPOSITORY NECESSITY MATRIX

### Quick Scoring Guide (Fill This In)

For each of your 1,592 owned + 831 starred repos:

```
Revenue Impact = (Does this repo directly generate income?) × (How many customers use it?)
Cost = (Annual storage) + (CI/CD runs/mo) + (Maintenance burden)
Vendor Lock-In = (Proprietary vs open-source?) × (Can you migrate in <1 week?)
```

**Necessity Score = (Revenue Impact × 0.5) + (1 - Cost/Max Cost × 0.25) + (Vendor Lock-In × 0.25)**

### Example Scoring

| Repo | Revenue Impact | Cost | Vendor Lock | Necessity | Action |
|------|----------|------|------------|-----------|--------|
| worldwidebro-os | HIGH (0.9) | $5/mo | LOW (0.8) | **0.88** | KEEP (core platform) |
| con-ventures (CON-001) | MEDIUM (0.6) | $8/mo | LOW (0.9) | **0.72** | KEEP (revenue venture) |
| lt-005-medical (LT-005) | LOW (0.2) | $10/mo | HIGH (0.3) | **0.40** | ARCHIVE (stalled venture) |
| random-old-fork | NONE (0.0) | $0 | N/A (0.0) | **0.00** | DELETE |
| **Your task:** | **Score 1,592 repos** | — | — | **Consolidate <0.3** | **See REPO-NECESSITY-MATRIX.csv** |

---

## SECTION 4: ALIGNMENT TO REVENUE (IMPACT MATRIX)

### Direct Revenue Drivers (MUST KEEP)

| File/Tool/Repo | Necessity | Cost/mo | Revenue (Est.) | ROI | Status |
|----------|-----------|---------|----------|-----|--------|
| VENTURE-READINESS-SCORECARD.csv | 0.95 | $0 | $0-5K | ∞ | **LIVE** |
| venture_leads table | 0.95 | $0 | $0-5K | ∞ | **LIVE** |
| Zapier (lead automation) | 0.7 | $25 | $2K | 80x | **LIVE** |
| ClickUp (sales pipeline) | 0.8 | $500 | $2K | 4x | **LIVE** |
| OmniRoute (LLM routing) | 0.6 | $0 | $120/mo savings | ∞ | **PENDING** (Task 2.3) |
| **Subtotal** | — | **$525** | **$2-5K** | **4-80x** | — |

### Medium-Term (Needed for Scaling)

| File/Tool/Repo | Necessity | Cost/mo | Revenue | ROI | Status |
|----------|-----------|---------|----------|-----|--------|
| Apple Notes Agent | 0.6 | $0 | $200/mo savings | ∞ | **IN PROGRESS** (Task 1.1) |
| Trigger.dev (orchestration) | 0.5 | $0-50 | $500/mo savings | 10x | **PENDING** |
| Supabase (database) | 0.99 | $50 | Required for all revenue | ∞ | **LIVE** |
| Notion (playbook docs) | 0.7 | $10 | $100/mo productivity | 10x | **PENDING** |
| **Subtotal** | — | **$60** | **$800/mo savings** | **13x** | — |

### Nice-to-Have (Could Archive)

| File/Tool/Repo | Necessity | Cost/mo | Revenue | ROI | Status |
|----------|-----------|---------|----------|-----|--------|
| Neo4j (relationships) | 0.4 | $15 | $0 (unused) | -$15/mo | **PAUSE** |
| Qdrant (semantic search) | 0.3 | $0 (local) | $0 (unused) | -$0 | **ARCHIVE** |
| Obsidian vault | 0.6 | $0 | $0 | - | **MIGRATE to Notion** |
| task_plan.md | 0.1 | $0 | $0 | - | **DELETE** |
| LangFuse logging | 0.2 | $0 (local) | $0 | - | **ARCHIVE** |
| **Subtotal** | — | **$15** | **$0** | **-$15/mo** | — |

---

## SECTION 5: DECISION CHECKLIST (FILL IN BY AUG 15)

### Question 1: Which 5 files/tools would you delete TODAY if forced?
```
[ ] tool_1: ___________________
[ ] tool_2: ___________________
[ ] tool_3: ___________________
[ ] tool_4: ___________________
[ ] tool_5: ___________________
```

### Question 2: Which 3 files/tools are non-negotiable?
```
[ ] critical_1: ___________________
[ ] critical_2: ___________________
[ ] critical_3: ___________________
```

### Question 3: Where do customer conversations live? (Single source of truth)
```
Current: [ ] Apple Notes [ ] ClickUp [ ] Email [ ] Supabase [ ] Scattered
Target: [ ] ClickUp [ ] Notion [ ] Apple Notes (via Agent 1.1)
```

### Question 4: What's your playbook? (How do you get from $0 → $1K MRR?)
```
In file: _________________ 
In tool: _________________
Status: [ ] Documented [ ] Scattered [ ] Missing
```

---

## SECTION 6: CONSOLIDATION ROADMAP

### PHASE 1: DELETE (Week 1, 2 hours)
- [ ] Remove task_plan.md (old)
- [ ] Archive Obsidian folders 06-08 (unused research)
- [ ] Delete neo4j/qdrant local instances (restart if revenue blocked)
- [ ] Stop paying for Make.com ($0-100/mo savings)
- [ ] Stop paying for Ngrok ($10-20/mo savings)

**Savings: $10-120/mo. Time: 2h. Risk: Low**

### PHASE 2: CONSOLIDATE (Week 2-3, 4 hours)
- [ ] Migrate Obsidian docs → Notion + Archive vault
- [ ] Qdrant vectors → Supabase pgvector
- [ ] Replace n8n → LangGraph + Trigger.dev (Task 2.3)
- [ ] Customer data sync: Supabase → single source of truth

**Savings: $120-200/mo. Time: 4h. Risk: Medium (test migration first)**

### PHASE 3: OPTIMIZE (Week 3-4, 2 hours)
- [ ] Wire OmniRoute for LLM cost reduction (Task 2.3)
- [ ] Audit GitHub Actions: consolidate workflows
- [ ] Set Vercel branch cleanup (auto-delete old deployments)

**Savings: $120/mo. Time: 2h. Risk: Low**

**TOTAL Consolidation: $250-420/mo savings by Week 4.**

---

## SECTION 7: SCORECARD (YOUR 2-HOUR TASK)

**Time Budget: 2 hours (Aug 15)**

1. **30 min:** Inventory Apple Notes (how many? what types?)
2. **30 min:** Fill in the "Decision Checklist" above (5 delete, 3 critical, 2 questions)
3. **30 min:** Score 20 of your highest-impact repos (use matrix above)
4. **30 min:** Write down your playbook (where does it live? is it repeatable?)

**Deliverables:**
- [ ] Section 4 (Alignment Matrix) marked complete
- [ ] Section 5 (Decision Checklist) filled in
- [ ] Top-20 repos in REPO-NECESSITY-MATRIX.csv
- [ ] Playbook location updated in this doc

**Output: SYSTEM-AWARENESS-AUDIT-COMPLETE.md (ready for Gate A on Aug 18)**

---

## NEXT STEPS

**When you finish (Aug 15):**
1. Email me your checklist answers
2. I'll score the remaining 1,572 repos (automated)
3. We'll identify the 40-60% of system that's eliminable
4. Cost savings fund Week 3-4 channel experiment

**Success = You know exactly what matters and what's waste.**

---

## SECTION 8: FREE/OSS CONSOLIDATION OPTIONS

Instead of paid tools, leverage existing local inventory:

**Automation:** Replace n8n ($100-500/mo) + Make ($100/mo) with **Trigger.dev** (OSS) + **LangGraph** (local)
- Savings: $200-600/mo
- Setup: 4 hours (migrate existing workflows)

**Knowledge Graphs:** Replace Qdrant ($0 local + storage) with **Supabase pgvector** (built-in)
- Savings: Storage + maintenance
- Setup: 2 hours (export 15,558 vectors)

**LLM Cost:** Use **OmniRoute** to route 80% of queries to **Ollama** (local), 20% to Claude
- Savings: $120-250/mo
- Setup: 1 hour config (Task 2.3)

**See:** REPOS-ORGANIZATION-MAP.md (Tier 1-9 stack), TASKS-TO-FIRST-REVENUE.md (Task 2.3 LLM routing)

---

**Last Update:** 2026-08-05  
**Next Gate:** Aug 18 (Gate A: Can we eliminate 30%+ of repos/tools?)
