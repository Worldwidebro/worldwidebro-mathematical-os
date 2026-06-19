# SkillsLLM Integration — Execution Guide

**Status**: Ready for deployment  
**Created**: 2026-06-04  
**Phases Complete**: 1 ✅, 2a ✅, 2b ✅, 3 ✅

---

## What Was Built

### Phase 1: Research ✅
- Confirmed SkillsLLM: 2,800+ skills, no public API
- Defined skill data structure: 11 fields
- Chose Playwright web scraper

### Phase 2a: Ingest Script ✅
**File**: `PLANE/05_SCRIPTS/populate_skillsllm_skills.py`

```bash
# Test: 1 page (50 skills)
python3 populate_skillsllm_skills.py --sample

# Full: all 2,800 skills
python3 populate_skillsllm_skills.py
```

### Phase 2b: Matching Engine ✅
**File**: `PLANE/05_SCRIPTS/match_ventures_to_skills.py`

```bash
# Dry-run: show recommendations
python3 match_ventures_to_skills.py --dry-run

# Test: specific ventures
python3 match_ventures_to_skills.py --ventures 1,2,3 --dry-run

# Full: all 712 ventures
python3 match_ventures_to_skills.py
```

### Phase 3: Plane Webhook ✅
**File**: `PLANE/04_AUTOMATION/plane_webhook_skills.py`

```bash
# Dry-run: show Plane updates
python3 plane_webhook_skills.py --dry-run

# Full: deploy to all ventures
python3 plane_webhook_skills.py
```

### Database Schema ✅
**File**: `PLANE/01_SCHEMAS/001_create_skills_tables.sql`
- Creates: `skills` table (2,800 rows)
- Creates: `venture_skills` table (~10,000 rows)
- Creates: 6 performance indexes

---

## Quick Start (5 Steps)

### 1. Apply Supabase Migration
```bash
# Supabase Dashboard > SQL Editor
# Copy & run: PLANE/01_SCHEMAS/001_create_skills_tables.sql
```

### 2. Test Ingest
```bash
cd /Users/acebless/Documents
python3 PLANE/05_SCRIPTS/populate_skillsllm_skills.py --sample
# Result: ~50 skills inserted in 2-5 min
```

### 3. Test Matching
```bash
python3 PLANE/05_SCRIPTS/match_ventures_to_skills.py --ventures 1,2,3 --dry-run
# Result: Shows recommendations for ventures 1,2,3
```

### 4. Test Webhook
```bash
python3 PLANE/04_AUTOMATION/plane_webhook_skills.py --dry-run
# Result: Shows which ventures would update in Plane
```

### 5. Full Deployment
```bash
# Sequential (takes ~75 minutes total)
python3 PLANE/05_SCRIPTS/populate_skillsllm_skills.py              # 60 min
python3 PLANE/05_SCRIPTS/match_ventures_to_skills.py              # 5 min
python3 PLANE/04_AUTOMATION/plane_webhook_skills.py               # 10 min
```

---

## Environment Setup

Create/update `/Users/acebless/.env`:

```bash
# Supabase
SUPABASE_URL=https://cyhzilqldouzgynacqpe.supabase.co
SUPABASE_KEY=<your_key>

# Plane
PLANE_API_KEY=<your_key>
PLANE_API_BASE_URL=https://api.plane.so/api/v1
PLANE_WORKSPACE_ID=<workspace_id>
```

---

## Expected Results

### After Ingest (Phase 2a)
- `skills` table: 2,800 rows
- Fields: name, description, author, github_url, category, stars, engagement_count

### After Matching (Phase 2b)
- `venture_skills` table: ~10,000 rows
- Each venture: 5-10 recommended skills
- Relevance scores: 0.0-1.0 (1.0 = highest)

### After Webhook (Phase 3)
- 712 ventures: "Recommended Skills" field populated in Plane
- Shows top 10 skills per venture (sorted by relevance)
- Format: JSON with name, category, score

---

## Execution Flow

```
SkillsLLM (2,800 skills)
    ↓ populate_skillsllm_skills.py
Supabase: skills table
    ↓ match_ventures_to_skills.py
Supabase: venture_skills table
    ↓ plane_webhook_skills.py
Plane: 712 ventures with recommendations
```

---

## Troubleshooting

**Ingest fails (Playwright)**
```bash
pip3 install playwright
playwright install chromium
python3 populate_skillsllm_skills.py --sample
```

**Matching returns 0 skills**
```bash
# Verify skills exist in Supabase
# SELECT COUNT(*) FROM skills;
# Run ingest first if empty
```

**Plane webhook fails**
```bash
# Verify Plane API key and workspace ID
# Use --dry-run to debug
python3 plane_webhook_skills.py --dry-run
```

---

## Success Checklist

- [ ] Supabase migration applied
- [ ] Ingest script: --sample runs (50+ skills)
- [ ] Matching: --dry-run shows recommendations
- [ ] Webhook: --dry-run shows Plane updates
- [ ] Full ingest: 2,800 skills inserted
- [ ] Full matching: ~10,000 relationships created
- [ ] Full webhook: 712 ventures updated in Plane

---

**Next**: See `SKILLSLLM-INTEGRATION-task_plan.md` for phase details or `SKILLSLLM-INTEGRATION-findings.md` for research notes.
