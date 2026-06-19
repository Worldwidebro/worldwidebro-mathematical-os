# Worldwidebro Operating System (WWOS) - Setup & Execution Guide

**Status:** Phase 1 - Unification in Progress  
**Date:** 2026-06-16  
**Goal:** Wire WWOS to Supabase → Verify data flows → Enable execution

---

## PHASE 1: FILE STRUCTURE ✅ COMPLETE

**Checkpoint 1: Files in WWOS directories**

```
Worldwidebro-Operating-System/
├── financial/CASH-FLOW-CALENDAR-2026.json
├── registries/UNIT-ECONOMICS-BY-VENTURE-TYPE.csv
├── operations/INCENTIVE-DESIGN-FRAMEWORK.md
├── portfolio/VENTURES-ASSET-CLASSIFICATION.csv
├── load_wwos_data.py (data loader)
└── SETUP.md (this file)
```

✅ Status: 4 files moved, directories created, ready for Supabase

---

## PHASE 2: SUPABASE SETUP (Manual Steps 1-3)

**Step 1: Copy SQL to Supabase**

Go to: https://app.supabase.com → SQL Editor

Execute these CREATE TABLE statements:

```sql
CREATE TABLE IF NOT EXISTS cash_flow_calendar (
  id SERIAL PRIMARY KEY,
  month TEXT NOT NULL,
  layer_1_services INTEGER DEFAULT 0,
  layer_2_products INTEGER DEFAULT 0,
  layer_3_acquisitions INTEGER DEFAULT 0,
  layer_4_capital INTEGER DEFAULT 0,
  total_cash_in INTEGER DEFAULT 0,
  notes TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS unit_economics (
  id SERIAL PRIMARY KEY,
  venture_type TEXT NOT NULL UNIQUE,
  layer INTEGER,
  revenue_model TEXT,
  avg_monthly_revenue TEXT,
  cogs_percent INTEGER,
  operating_costs INTEGER,
  monthly_profit TEXT,
  profit_margin_percent TEXT,
  examples TEXT,
  notes TEXT
);

CREATE TABLE IF NOT EXISTS compensation_frameworks (
  id SERIAL PRIMARY KEY,
  layer INTEGER NOT NULL,
  role TEXT NOT NULL,
  base_salary_range TEXT,
  bonus_structure TEXT,
  equity_percentage DECIMAL,
  comp_example TEXT,
  notes TEXT
);

CREATE TABLE IF NOT EXISTS ventures_asset_classification (
  id SERIAL PRIMARY KEY,
  venture_name TEXT NOT NULL,
  sector TEXT,
  venture_type TEXT,
  asset_classification TEXT,
  revenue_potential_1_5 INTEGER,
  strategic_value_1_5 INTEGER,
  automation_potential_1_5 INTEGER,
  competitive_advantage_1_5 INTEGER,
  scalability_1_5 INTEGER,
  capital_efficiency_1_5 INTEGER,
  asset_score_0_30 INTEGER,
  classification_rationale TEXT,
  monthly_profit_projection TEXT,
  status TEXT
);

CREATE TABLE IF NOT EXISTS phases_completion (
  id SERIAL PRIMARY KEY,
  phase_number INTEGER,
  phase_name TEXT,
  completion_percent INTEGER,
  repos_available INTEGER,
  status TEXT
);
```

**Step 2: Load Data via Python**

```bash
cd /Users/acebless/Documents/Worldwidebro-Operating-System
python3 load_wwos_data.py
```

**Step 3: Verify in Supabase**

```sql
SELECT COUNT(*) as months FROM cash_flow_calendar;
SELECT COUNT(*) as types FROM unit_economics;
SELECT COUNT(*) as ventures FROM ventures_asset_classification;
SELECT COUNT(*) as phases FROM phases_completion;
```

Expected: 12, 14, 30, 12

---

## PHASE 3: OBSIDIAN SYNC (Step 4)

```bash
python3 /Users/acebless/Documents/Influence-Venture-Business-OS/INFRASTRUCTURE_LAYERS/venture-hub/obsidian_graph_sync.py
```

Expected output: ✅ Data synced to `.planning/venture-hub-alignment.json`

---

## PHASE 4: VERIFICATION (Step 5)

**Gears Turning Checklist:**

- [ ] Files in Worldwidebro-Operating-System/ ✅
- [ ] Supabase tables created ✅
- [ ] Data loaded (12+14+30 rows) ✅
- [ ] obsidian_graph_sync.py ran ✅
- [ ] Obsidian shows real data ✅

---

## PHASE 5: EXECUTION READY

Once verified: **WWOS operational. Ready to execute 712 ventures.**

**Next Actions:**
1. Define 13-role org structure (1 week)
2. Build contract management system (2 weeks)
3. Launch first venture execution

