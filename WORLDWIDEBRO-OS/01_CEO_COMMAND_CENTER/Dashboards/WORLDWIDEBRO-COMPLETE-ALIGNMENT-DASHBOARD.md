# WORLDWIDEBRO: Complete 4-Layer Alignment Dashboard

**Status**: Live | **Updated**: 2026-06-01  
**Total Coverage**: 629 Ventures | 853 Owned Repos | 664 Starred Repos | 6 Active Alignments

---

## Executive Summary

You have **four distinct layers of data** across the system:

| Layer | Count | Status | Source |
|-------|-------|--------|--------|
| **Ventures** | 629 | 100% cataloged | `ventures_classification_final.csv` |
| **Owned Repos** (Worldwidebro org) | 853 | 100% cataloged | `venture-hub/registries/github_owned.csv` |
| **Starred Repos** (Following) | 664 | 100% cataloged | `starred_repos_664.csv` |
| **Active Alignments** | 6 repos | 0.4% coverage | `WORLDWIDEBRO-VENTURES-REPOS-ALIGNMENT.csv` |

### The Core Problem

- ✅ **Ventures are defined** (629 with sector, tier, revenue model, capabilities)
- ✅ **Repos are cataloged** (853 owned + 664 starred with language, topics, capabilities)
- ❌ **Alignment is INCOMPLETE** (only 6 repos mapped to ventures)
  - 618 ventures have repo matches (98.3%)
  - 1,510 repos have NO venture assigned (99.6%)
  - 11 ventures have NO repo match (0.2%)

**Why this matters**: Without complete alignment, you can't:
- See which repos serve which ventures
- Route capability requirements to actual code
- Identify duplicate repos
- Clean up unused repos
- Assign repos to sectors

---

## How to Use This Dashboard

### For Venture Teams
**"Which repos do we have for our ventures?"**
→ See `WORLDWIDEBRO-SUPERUNIFIED-4LAYERS.csv`
- Columns: venture_id, venture_name, sector, tier, owned_repos_matched, starred_repos_matched
- Filter by sector to see repo alignment for your ventures

### For Platform Teams
**"Which ventures use this repo?"**
→ See `WORLDWIDEBRO-REPOS-4LAYERS.csv`
- Columns: repo_name, repo_type (owned/starred), language, topics, ventures_matched, venture_count
- Shows which ventures (if any) claim this repo

### For Executives
**"Are we aligned? What's not covered?"**
→ See this section below (Gap Analysis)

---

## Raw Data Files

### Ventures Layer
**File**: `ventures_classification_final.csv`
- **Size**: 629 rows
- **Columns**: venture_id, venture_name, sector, tier, department, control_type, revenue_model, capability_score, confidence, top_repo, dependencies
- **Sectors**: market (195), infra (116), devtools (91), ai (72), edtech (69), fintech (47), con (21), re (15), ops (2), health (1)

### Owned Repos Layer
**File**: `venture-hub/registries/github_owned.csv`
- **Size**: 853 rows
- **Columns**: name_with_owner, name, description, private, fork, archived, language, stars, forks, created_at, updated_at, pushed_at, url, homepage, topics

### Starred Repos Layer
**File**: `starred_repos_664.csv`
- **Size**: 664 rows
- **Columns**: name, owner, language, topics, capabilities, cap_count, url

### Alignment Layer (Current)
**File**: `WORLDWIDEBRO-VENTURES-REPOS-ALIGNMENT.csv`
- **Size**: 629 rows (one per venture)
- **Columns**: venture_id, venture_name, sector, tier, required_capabilities, top_repo_1/2/3, match_pct_1/2/3, is_starred_1/2/3, sector_coverage_pct

---

## Query All 4 Layers Together

### CSV View (Recommended for Excel/Sheets)

**Venture-Centric View:**
```
WORLDWIDEBRO-SUPERUNIFIED-4LAYERS.csv
```
Columns: venture_id, venture_name, sector, tier, owned_repos_matched, starred_repos_matched, total_repos_matched, owned_count, starred_count

**Repo-Centric View:**
```
WORLDWIDEBRO-REPOS-4LAYERS.csv
```
Columns: repo_name, repo_owner, repo_type (owned/starred), language, topics, ventures_matched, venture_count, is_starred

### Gap Analysis

**11 Ventures with NO Repo Match:**
Run this to find them:
```bash
python3 << 'EOF'
import csv
unmatched = []
venture_ids = {r['venture_id'] for r in csv.DictReader(open('WORLDWIDEBRO-VENTURES-REPOS-ALIGNMENT.csv'))}
for row in csv.DictReader(open('ventures_classification_final.csv')):
    if row['venture_id'] not in venture_ids:
        unmatched.append((row['sector'], row['venture_name'], row['venture_id']))
for sector, name, id in sorted(unmatched):
    print(f"{sector:12} | {name}")
EOF
```

**1,510 Repos with NO Venture Assignment:**
These need categorization:
- Are they duplicates?
- Should they be archived?
- Should they be open-sourced?
- Do they serve multiple ventures?

---

## Sector Breakdown

| Sector | Ventures | Top Repos | Action |
|--------|----------|-----------|--------|
| market | 195 | LightRAG | Review SUPERUNIFIED filtered |
| infra | 116 | Civilization OS | See ops repos |
| devtools | 91 | Mission Control | See ops repos |
| ai | 72 | LightRAG | Needs mapping |
| edtech | 69 | [TBD] | Needs mapping |
| fintech | 47 | [TBD] | Needs mapping |
| con | 21 | HVAC/Electrical | Operational repos |
| re | 15 | [TBD] | Needs mapping |
| ops | 2 | Directives exist | Active |
| health | 1 | [TBD] | Needs repo |

---

## What This Dashboard Answers

✅ "Can we see all ventures, sectors, repos, and starred repos together?"  
→ YES: Open the two CSV files above

✅ "Filter by sector?"  
→ YES: Column `sector` in both CSVs

✅ "See owned vs starred?"  
→ YES: `repo_type` column in `REPOS-4LAYERS.csv`

✅ "Which ventures have no repos?"  
→ YES: Look for `total_repos_matched = 0` in SUPERUNIFIED

✅ "Which repos aren't used?"  
→ YES: Look for `venture_count = 0` in REPOS-4LAYERS

---

**Files Created**: 
- `WORLDWIDEBRO-SUPERUNIFIED-4LAYERS.csv` (ventures view)
- `WORLDWIDEBRO-REPOS-4LAYERS.csv` (repos view)

**Referenced by**: `/venture-hub/REPO-ALIGNMENT.md`, `/KNOWLEDGE-GRAPH-DASHBOARD.md`

**Last Updated**: 2026-06-01
