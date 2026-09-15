# 📊 789 Ventures CSV → ChatGPT Analysis Guide

**Extracted:** 2026-09-15  
**Purpose:** Cross-analyze Worldwidebro portfolio structure using private-firm architecture model  

---

## WHAT YOU HAVE

### 1. 789-VENTURES-WITH-GITHUB.csv
**File:** `/private/tmp/claude-501/-Users-acebless-Documents-The-Company-Company-Brain/85c12b01-8717-4e3a-b504-b57ad1ba78af/scratchpad/789-VENTURES-WITH-GITHUB.csv`

**Columns:**
- `ID` — Venture identifier (FIN-001, BW-002, etc.)
- `Name` — Venture name (Genixbank Lite, Mobile Lash Service, etc.)
- `Sector` — Business sector (Financial, Beauty Wellness, Healthcare, etc.)
- `Stage` — Development stage (planned, mvp, validation, growth, operating)
- `GitHub URL` — Repository URL (https://github.com/Worldwidebro/fin-001-...)
- `GitHub Pages URL` — Predicted GitHub Pages (https://worldwidebro.github.io/...)
- `Repo Match` — Exact repository match (fin-001-genixbank-lite)

**Sample rows:**
```
ID,Name,Sector,Stage,GitHub URL,GitHub Pages URL,Repo Match
null,Genixbank Lite,Financial,planned,https://github.com/Worldwidebro/fin-001-genixbank-lite,https://worldwidebro.github.io/genixbank-lite/,fin-001-genixbank-lite
null,Credit Repair Automation,Financial,planned,https://github.com/Worldwidebro/fin-002-credit-repair-automation,https://worldwidebro.github.io/credit-repair-automation/,fin-002-credit-repair-automation
null,Ai Boss Hub Lite,Financial,planned,https://github.com/Worldwidebro/fin-003-ai-boss-hub-lite,https://worldwidebro.github.io/ai-boss-hub-lite/,fin-003-ai-boss-hub-lite
```

**Statistics:**
- Total ventures: 789
- With GitHub repos: 652 (82.6%)
- Without repos: 137 (17.4%)
- Sectors: 35
- Stages: 5 (planned, mvp, validation, growth, operating)

---

## WIKI LINK CONNECTIONS

### Navigation Aliases (Where ventures are referenced)
**File:** `_REGISTRIES/CANONICAL/NAVIGATION_ALIASES.yaml`

**Key links to ventures:**

```yaml
# ROOT DOCUMENTS
[[STARTHERE]] — Master orientation (references Phase 0 ventures)
[[REALITY]] — Live truth ledger (venture readiness snapshot)
[[ANTIGRAVITY]] — 45 operating rules (governance applies to all ventures)
[[INDEX]] — Master navigation

# SECTOR DOCUMENTS
[[SECTOR_INDEX]] — All 35 sectors (SEC-001 to SEC-035)
[[SECTOR-TAXONOMY-MASTER]] — Sector definitions + OpCo mapping

# VENTURE DOCUMENTS
[[VENTURE-ROADMAP-2026-09]] — 7 Tier-1 ventures (OPS-001, LT-005, CALLCENTER, CON-001, RE-001, LT-011, + TBD)
[[VENTURE-READINESS-SCORECARD]] — 789 ventures by readiness % + income distance
[[VENTURE-AUDIT-FRAMEWORK]] — 12-layer methodology for venture assessment

# CAPITAL DOCUMENTS
[[INSTITUTIONAL-VENTURE-ARCHITECTURE]] — Master map: all 789 ventures → repos + OSS deps
[[WORLDWIDEBRO-HOLDINGS-MASTER-OPERATING-MANUAL]] — 789-venture holding company framework
[[CAPITAL-READINESS-ENGINE]] — 5-venture capital matrix + $4.5M capital sources

# ORGANIZATION DOCUMENTS
[[VEX]] — Family office / capital allocation platform
[[WORLDWIDEBRO-HOLDINGS]] — Parent holding company
```

---

## HOW TO ANALYZE IN CHATGPT

### Analysis #1: Portfolio Composition
**Prompt:**
```
I'm providing a CSV of 789 ventures (companies) organized by sector and stage.
Help me understand:
1. How many ventures are in each stage? (planned, mvp, validation, growth, operating)
2. Which sectors have the most ventures?
3. What's the distribution of development maturity?
4. Which sector-stage combinations have the most ventures? (e.g., Financial-planned)
5. Are there any obvious gaps or imbalances in the portfolio?
```

### Analysis #2: Apply Private-Firm Architecture
**Prompt:**
```
Here's the structure of a private holding company with 789 operating ventures:

OWNERSHIP LAYER (Family Trust)
  ↓
HOLDING COMPANY (Worldwidebro Group)
  ↓
OPERATING COMPANIES (789 ventures across 35 sectors)
  ↓
SHARED SERVICES (Company Brain / DispatchOS)

Given my CSV of 789 ventures, help me:
1. Map ventures into 3 tiers (Tier-0 revenue-ready, Tier-1 near-term, Tier-2+ future)
2. Identify which ventures could be "asset companies" vs "operating companies"
3. Suggest which ventures should feed into a shared "investment platform" vs standalone OpCos
4. For Tier-0 ventures (6 total: OPS-001, LT-005, CALLCENTER, CON-001, RE-001, LT-011), suggest portfolio structure
```

### Analysis #3: Revenue Model Mapping
**Prompt:**
```
Here's my 789-venture CSV with sectors and stages. 
Also: I have 6 Tier-0 ventures that need revenue generated within 30 days.

Help me:
1. Map each venture to SUBSCRIPTION (recurring revenue) or TRANSACTIONAL (one-time deals)
2. Estimate realistic monthly revenue for each venture type
3. Rank ventures by "days to first revenue" (quick wins vs long-tail)
4. For Tier-0 ventures, what's the revenue roadmap by week? (Week 1: $7.5K-$20K)
5. Which Tier-1 ventures should launch in Oct/Nov to sustain momentum?
```

### Analysis #4: Sector Intelligence
**Prompt:**
```
I have 35 sectors with varying numbers of ventures. 
Help me understand the portfolio's sector balance:
1. Which sectors are over-invested? (too many ventures)
2. Which sectors are under-invested? (opportunity gap)
3. For high-priority sectors (Financial, Healthcare, Construction), what's the venture distribution?
4. Are there sector-specific risks I should know about?
5. Should I consolidate ventures within sectors or diversify?
```

### Analysis #5: GitHub Integration
**Prompt:**
```
I've provided GitHub URLs for 652 of 789 ventures.
Help me understand:
1. How many ventures have active repositories? (Look at repo names + URL patterns)
2. Which ventures are missing repositories? (137 no GitHub URL = risk?)
3. Are repositories named consistently? (Pattern: {sector}-{number}-{venture-name})
4. For Tier-0 ventures, are GitHub repos production-ready?
5. What's my repository onboarding strategy for the 789 ventures?
```

### Analysis #6: Capital Allocation
**Prompt:**
```
I have 789 ventures at different stages (planned, mvp, validation, growth, operating).
Each needs capital allocation decisions:
1. For OPERATING ventures: maintain + growth capital
2. For GROWTH ventures: scale capital
3. For VALIDATION ventures: proof capital
4. For MVP ventures: build capital
5. For PLANNED ventures: exploration capital

Given a total capital budget of $X, help me allocate:
- How much per stage?
- How much per sector?
- What's the 30-day, 90-day, 1-year capital roadmap?
- Which ventures should I STOP funding?
```

---

## COPY-PASTE FORMAT FOR CHATGPT

### Quick Format (Numbers Only)
```
Portfolio Summary:
- Total ventures: 789
- With GitHub repos: 652
- Operating: XX ventures (Stage=operating)
- Growth: XX ventures (Stage=growth)
- Validation: XX ventures (Stage=validation)
- MVP: XX ventures (Stage=mvp)
- Planned: XX ventures (Stage=planned)

By Sector (Top 10):
1. Financial: XX ventures
2. [Sector]: XX ventures
3. ...

```

### Full Format (Include CSV)
Copy the entire `789-VENTURES-WITH-GITHUB.csv` file and paste into ChatGPT with:

```
Here's a CSV of 789 ventures in my portfolio. Analyze this for:
1. Portfolio composition (stage distribution)
2. Sector concentration
3. Revenue-readiness ranking
4. Risk assessment
5. Capital allocation recommendations

[PASTE CSV HERE]

Additional context:
- Holding company structure: Worldwidebro Group
- Family office: VEX (capital allocation)
- Tier-0 (priority): OPS-001, LT-005, CALLCENTER, CON-001, RE-001, LT-011
- Revenue target: $7.5K-$20K in Week 1 from Tier-0 only
- Total portfolio: 35 sectors, 789 ventures
```

---

## WIKI LINK INTEGRATION

**In Obsidian vault:**

Create a new note:
```
---
title: 789 Ventures Portfolio Analysis
tags: [portfolio, ventures, chatgpt-analysis]
---

# Portfolio Intelligence

## CSV Data
See: 789-VENTURES-WITH-GITHUB.csv

## Sector Navigation
[[SECTOR_INDEX]] — Links to SEC-001 through SEC-035

## Venture Tiers
[[VENTURE-ROADMAP-2026-09]] — Tier-0 (6), Tier-1 (7+), Tier-2+ (770+)

## Capital Architecture
[[CAPITAL-READINESS-ENGINE]] — Capital allocation framework
[[INSTITUTIONAL-VENTURE-ARCHITECTURE]] — Full venture map

## References
- [[WORLDWIDEBRO-HOLDINGS-MASTER-OPERATING-MANUAL]] — 789-venture operating model
- [[REALITY]] — Current portfolio readiness
- [[ANTIGRAVITY]] — Operating rules for all ventures
```

Then link from sector pages, venture roadmap, etc.

---

## NEXT STEPS

1. ✅ **Export CSV** (Done: 789-VENTURES-WITH-GITHUB.csv)
2. ✅ **Identify GitHub URLs** (652 matched, 137 gaps)
3. 📋 **Open ChatGPT** → New chat
4. 📋 **Paste analysis prompt** (choose from 6 options above)
5. 📋 **Paste CSV data**
6. 📋 **Ask for**: Portfolio composition, revenue ranking, capital allocation
7. 📋 **Get insights** → Update Obsidian vault with findings
8. 🔄 **Build n8n workflows** (Week 1 revenue execution based on ChatGPT insights)

---

## CONTEXT NOTES

The private-firm architecture framework provided emphasizes:
- **Separate the 5 functions:** Earn (OpCos), Own (HoldCo), Invest (Investment platform), Manage (Family office), Transfer (Trusts)
- **Worldwidebro = the conglomerate** (all 789 ventures)
- **Worldwidebro Group = the holding company** (ownership layer)
- **VEX = the family office** (capital allocation + coordination)
- **Company Brain = the nervous system** (shared infrastructure + intelligence)

Use this framework when ChatGPT analyzes your ventures to ensure recommendations align with this architecture.

---

**File ready for ChatGPT:** `/private/tmp/claude-501/-Users-acebless-Documents-The-Company-Company-Brain/85c12b01-8717-4e3a-b504-b57ad1ba78af/scratchpad/789-VENTURES-WITH-GITHUB.csv`

**Your move:** Open ChatGPT, paste one of the analysis prompts above, and let it help you understand the portfolio structure.
