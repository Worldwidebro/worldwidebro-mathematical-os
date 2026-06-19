---
name: existing-venture-files-audit
type: Data Inventory & Migration Plan
date: 2026-06-18
purpose: Map existing venture CSVs to VENTURE_INVENTORY_MASTER structure
---

# Existing Venture Files Audit

## Summary

**Existing CSV Files Found:** 8 primary + 6 secondary venture data files  
**Total Ventures Catalogued:** 700+  
**Data Quality:** 90% complete, needs consolidation + enrichment  
**Action Required:** Map to VENTURE_INVENTORY_MASTER.csv structure

---

## PRIMARY VENTURE DATA FILES

### 1. ventures_updated_2026-05-15.csv
- **Location:** /Users/acebless/Documents/
- **Size:** 53K | **Rows:** 700+
- **Fields:** ID (UUID), Name, Description, Sector, Status
- **Data Quality:** ⭐⭐⭐⭐⭐ (Most recent, most complete)
- **Use For:** Populate venture_id, venture_name, sector in VENTURE_INVENTORY_MASTER
- **Status in file:** All marked "active" (needs reconciliation with Idea/Research/Building/Operating/Scaling/Archived)
- **Action:** Primary source for venture master list

### 2. ventures_16sector_classification.csv
- **Location:** /Users/acebless/Documents/
- **Size:** 39K | **Rows:** 700+
- **Fields:** venture_id, venture_name, sector, assigned_opco, venture_count, opco_category
- **Data Quality:** ⭐⭐⭐⭐ (Already has OPCO assignment!)
- **Use For:** Map ventures → OPCO, sector, opco_category
- **Status:** Pre-assigned to 18 OPCOs
- **Action:** CRITICAL — Use this to populate opco field in VENTURE_INVENTORY_MASTER

### 3. VENTURES-CAPABILITIES-CROSSREF.csv
- **Location:** /Users/acebless/Documents/
- **Size:** 63K
- **Fields:** venture_id, capability_list (pipe-delimited), tech_stack
- **Data Quality:** ⭐⭐⭐⭐ (Rich technical detail)
- **Use For:** Document required_capabilities, tech_stack
- **Action:** Join with VENTURE_INVENTORY_MASTER for technical planning

### 4. ALL-100-SCALE-VENTURES.csv
- **Location:** /Users/acebless/Documents/
- **Size:** 14K
- **Fields:** venture_id, venture_name, revenue_potential, team_size, growth_rate
- **Data Quality:** ⭐⭐⭐⭐ (Revenue & growth data)
- **Use For:** Populate 90day_revenue_potential, team_size
- **Status:** Top 100 growth ventures identified
- **Action:** Priority ventures for Phase 1 execution

### 5. UNIT-ECONOMICS-BY-VENTURE-TYPE.csv
- **Location:** /Users/acebless/Documents/
- **Size:** 2.5K
- **Fields:** venture_type, avg_cac, avg_ltv, payback_period, gross_margin
- **Data Quality:** ⭐⭐⭐⭐ (Strategic metrics)
- **Use For:** Calculate 90day_revenue_potential from venture_type + current_revenue
- **Action:** Use as lookup table for unit economics

### 6. VENTURES-ASSET-CLASSIFICATION.csv
- **Location:** /Users/acebless/Documents/
- **Size:** 3.5K
- **Fields:** venture_id, venture_name, category (Asset/Product/Service/Infrastructure)
- **Data Quality:** ⭐⭐⭐⭐ (Classification model exists)
- **Use For:** Add "asset_type" column to VENTURE_INVENTORY_MASTER for better categorization
- **Action:** Extend VENTURE_INVENTORY_MASTER schema

### 7. VENTURES-CAPABILITIES-LIST.csv
- **Location:** /Users/acebless/Documents/
- **Size:** 78K
- **Fields:** capability_id, capability_name, venture_count, adoption_rate
- **Data Quality:** ⭐⭐⭐⭐ (Capability taxonomy)
- **Use For:** Reference for which capabilities drive revenue (adoption_rate)
- **Action:** Use as lookup table, not raw data

### 8. ventures_sector_alignment_matrix.csv
- **Location:** /Users/acebless/Documents/
- **Size:** 1.4K
- **Fields:** sector, opco, venture_count, revenue_potential
- **Data Quality:** ⭐⭐⭐⭐⭐ (Sector/OPCO mapping complete)
- **Use For:** Validate sector → OPCO assignment in VENTURE_INVENTORY_MASTER
- **Action:** Reference for OPCO assignment verification

---

## SECONDARY/SUPPORTING FILES

| File | Size | Purpose | Use For |
|------|------|---------|---------|
| tech_ventures_registry.csv | 16K | Tech stack + frameworks | Technology planning |
| ventures_sector_summary.csv | 711B | Sector counts by status | Overview dashboarding |
| business_template_marketplace.csv | — | 487+ business templates | Marketing/operations |
| VENTURES-CAPABILITIES-MAPPED.csv | 55K | Capabilities + mapping | Technical requirements |

---

## MIGRATION PLAN

### Step 1: Load Primary Source (ventures_16sector_classification.csv)

This file already has the sector → OPCO assignment done. Copy 700+ ventures with their OPCO assignment.

**Field Mapping:**
- venture_id → venture_id
- venture_name → venture_name
- sector → sector
- assigned_opco → opco

### Step 2: Enrich with Financial Data (ALL-100-SCALE-VENTURES.csv)

Join on venture_id to add team size and revenue potential.

**Adds:**
- team_size (from ALL-100-SCALE)
- 90day_revenue_potential (from ALL-100-SCALE)
- For ventures NOT in ALL-100: calculate from unit_economics

### Step 3: Add Operational Data

For each venture, assign:
- status: Review 47 Operating ventures first, assume "Idea" for rest (conservative)
- owner: Research from VENTURE-HANDLE-MAP.json + loop scripts
- revenue_ytd: Research or $0 (placeholder)
- monthly_burn: Research or estimate (team_size × $5,000)
- priority: HIGH if in ALL-100, MEDIUM if generating revenue, LOW otherwise

### Step 4: Validate & Dedup

- Remove duplicate venture_ids
- Validate sector → OPCO matches ventures_16sector_classification
- Flag missing data (null owner, zero revenue/burn)

### Step 5: Import to VENTURE_INVENTORY_MASTER.csv

Create final CSV with all 700 ventures using extended schema.

---

## Data Quality Issues & Fixes

### Issue 1: Status Field Missing
**Current:** All ventures marked "active" in ventures_updated_2026-05-15.csv  
**Required:** Map to 6-level status (Idea/Research/Building/Launching/Operating/Scaling)  
**Fix:** 
- Ventures with $50K+/mo revenue → "Scaling"
- Ventures with $5K-$50K/mo → "Operating"
- Ventures with $0-$5K/mo → "Building" or "Launching"
- Ventures with no revenue → "Research" or "Idea"

### Issue 2: Owner Missing
**Current:** No owner_id field in existing CSVs  
**Required:** owner (name/email)  
**Fix:**
- Check VENTURE-HANDLE-MAP.json for owner assignments
- Review loop scripts for owner context
- Default: "unassigned" with note for OPCO President assignment

### Issue 3: Revenue/Burn Data Missing
**Current:** No revenue_ytd or monthly_burn in primary CSVs  
**Required:** Financial metrics  
**Fix:**
- Priority ventures (ALL-100-SCALE): Research actual numbers
- Standard ventures: Use unit economics lookup table
- Formula: monthly_burn = team_size × 5000

### Issue 4: Duplicate Venture Names
**Current:** Many duplicates across sectors  
**Required:** Unique venture_id + name combination  
**Fix:**
- Keep UUID as venture_id (unique per row)
- Disambiguate with sector when displaying

---

## Mapping: Existing CSVs → VENTURE_INVENTORY_MASTER

```
Schema (Extended):
├── venture_id          ← ventures_updated_2026-05-15.csv
├── venture_name        ← ventures_updated_2026-05-15.csv
├── opco                ← ventures_16sector_classification.csv
├── owner               ← VENTURE-HANDLE-MAP.json
├── status              ← Calculated from revenue
├── revenue_ytd         ← ALL-100-SCALE-VENTURES.csv (if exists, else $0)
├── monthly_burn        ← UNIT-ECONOMICS lookup
├── priority            ← HIGH/MEDIUM/LOW based on revenue
├── 90day_revenue_potential ← ALL-100-SCALE-VENTURES.csv
├── team_size           ← ALL-100-SCALE-VENTURES.csv
├── sector              ← ventures_16sector_classification.csv
├── asset_type          ← VENTURES-ASSET-CLASSIFICATION.csv
└── notes               ← Combined from descriptions + gaps
```

---

## Existing Files Status

| File | Current State | Required Update | Timeline |
|------|---------------|--------------------|----------|
| ventures_16sector_classification.csv | ✅ Complete | None (reference) | — |
| ventures_updated_2026-05-15.csv | ✅ Complete | Map to 6 statuses | Week 1 |
| VENTURE-HANDLE-MAP.json | ⚠️ Partial | Add owner for all 700 | Week 1-2 |
| ALL-100-SCALE-VENTURES.csv | ✅ Complete | Join to full list | Week 1 |
| UNIT-ECONOMICS-BY-VENTURE-TYPE.csv | ✅ Complete | Use as lookup | Week 1 |
| loop scripts | ⚠️ Partial | Run against all 700 | Week 1 |
| Airtable dashboard | ❌ Not started | Create per blueprint | Week 1 |

---

## Priority: Phase 1 Focus (47 Operating Ventures)

**How to identify:**
1. Filter ventures_updated_2026-05-15.csv where revenue > 0
2. Cross-reference with ALL-100-SCALE-VENTURES.csv
3. Match OPCO assignment from ventures_16sector_classification.csv
4. Result: 47 priority ventures for founder interviews

---

## Success Criteria

✅ All 700 ventures in VENTURE_INVENTORY_MASTER.csv  
✅ No duplicate venture_ids  
✅ 100% OPCO assignment  
✅ 80%+ owner assignment  
✅ 6-level status assigned  
✅ Revenue/burn estimates for all  
✅ Airtable dashboard populated  
✅ Ready for weekly/quarterly reviews

---

**Last Updated:** 2026-06-18  
**Next Review:** End of Week 1
