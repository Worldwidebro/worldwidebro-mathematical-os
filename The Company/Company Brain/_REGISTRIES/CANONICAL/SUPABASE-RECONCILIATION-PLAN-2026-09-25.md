# Supabase Reconciliation Plan — Sep 25, 2026

**Status:** CRITICAL DATA INTEGRITY RECONCILIATION INITIATED  
**Authority:** Ground truth validation (Supabase vs. Manual Registries)  
**Timeline:** Sep 25-30, 2026

---

## Ground Truth Discovery (Sep 25)

### Supabase Database State (Actual)
| Table | Rows | Status | Purpose |
|-------|------|--------|---------|
| `sectors` | 16 | INCOMPLETE | Currently 16 sectors; need 36 |
| `opcos` | 5 | INCOMPLETE | Currently 5 OpCos; need 35 |
| `ventures` | 580 (verified) | PARTIAL | 580 real ventures (not 789) across 25 sector categories |
| `legal_entities` | 682 | ✅ LIVE | **ENTITIES REGISTRY FOUND** — This is our entity graph! |
| `graph_entities` | 16,840 | ✅ LIVE | Knowledge graph nodes |
| `graph_relationships` | TBD | ✅ LIVE | Knowledge graph edges |
| `bases` | ❌ MISSING | NOT CREATED | Need to create for 36 Bases |

### Critical Finding: Sector Model Mismatch
**Supabase uses 25 sector categories (flat strings):**
- `e-commerce` (108 ventures)
- `operations` (66 ventures)
- `specialized`, `community`, `emerging` (50 each)
- `beauty-wellness` (40 ventures)
- `technology` + `software-technology` (62 combined)
- `logistics-transport` (28 ventures)
- Plus 15 more categories

**Our Registry claims 36 sectors with SEC-XXX codes** (different model entirely).

### What We Know (Summary)
- ✅ Supabase is the ground truth for REAL data (580 ventures, 25 sectors)
- ✅ Entities registry EXISTS (`legal_entities`, 682 records)
- ✅ Knowledge graph EXISTS (`graph_entities` + `graph_relationships`)
- ❌ Our manual registries are DISCONNECTED from Supabase schema
- ❌ `bases` table does NOT exist
- ❌ 36-sector model is NOT in Supabase (only 16 sectors)
- ❌ 35-OpCo model is NOT in Supabase (only 5 OpCos)

---

## Reconciliation Strategy

### Phase 1: Mapping (Sep 25-26)
**Goal:** Understand relationship between 25 Supabase sectors and our 36-sector model

**Tasks:**
1. List all 16 existing sectors in Supabase
2. List all 25 sector CATEGORIES (from ventures group-by)
3. Map: 25 Supabase categories → 36 SEC-XXX codes
4. Identify: Which 11 SEC-XXX codes have NO Supabase data yet?

**Action:**
```sql
-- What sectors currently exist?
SELECT DISTINCT sector FROM sectors ORDER BY sector;

-- What sector categories are in ventures?
SELECT DISTINCT sector FROM ventures ORDER BY sector;

-- Comparison: sectors table vs ventures data
```

### Phase 2: Infrastructure (Sep 27-28)
**Goal:** Populate Supabase with full 36-sector model + 35-OpCo model + 36-Base model

**Tables to create/update:**
1. **`sectors` (update):** 16 → 36 sectors (add 20 missing SEC-XXX codes)
2. **`opcos` (update):** 5 → 35 OpCos (add 30 missing OpCo records)
3. **`bases` (create):** New table for 36 Bases with gates
4. **`ventures` (verify):** Ensure all 789 should be there (currently 580)
5. **`legal_entities` (verify):** Already exists with 682 records ✅

**Schema for new/updated tables:**

```sql
-- bases table (NEW)
CREATE TABLE bases (
  id BIGSERIAL PRIMARY KEY,
  base_id VARCHAR(10) UNIQUE NOT NULL,  -- BASE-001 to BASE-036
  sector_id VARCHAR(10) NOT NULL REFERENCES sectors(sector_id),
  opco_id VARCHAR(10) NOT NULL REFERENCES opcos(opco_id),
  name VARCHAR(255) NOT NULL,
  status VARCHAR(50),  -- ACTIVE, STAGING, PENDING
  venture_count INT,
  gate_1_sector_defined BOOLEAN,
  gate_2_sector_unique BOOLEAN,
  -- ... all 11 gates ...
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- sectors table (UPDATE schema to match)
ALTER TABLE sectors ADD COLUMN IF NOT EXISTS sector_id VARCHAR(10) UNIQUE;
ALTER TABLE sectors ADD COLUMN IF NOT EXISTS status VARCHAR(50);
ALTER TABLE sectors ADD COLUMN IF NOT EXISTS opco_id VARCHAR(10);

-- opcos table (UPDATE schema)
ALTER TABLE opcos ADD COLUMN IF NOT EXISTS opco_id VARCHAR(10) UNIQUE;
ALTER TABLE opcos ADD COLUMN IF NOT EXISTS sector_id VARCHAR(10);
ALTER TABLE opcos ADD COLUMN IF NOT EXISTS status VARCHAR(50);
```

### Phase 3: Population (Sep 29-30)
**Goal:** Populate new/expanded tables with our 36-sector model data

**Insert statements:**
1. Insert 20 missing sectors (SEC-002, SEC-003, SEC-006, etc.)
2. Insert 30 missing OpCos (OPCO-002, OPCO-003, OPCO-006, etc.)
3. Insert 36 Bases (BASE-001 to BASE-036) with gate tracking
4. Map existing 580 ventures to expanded sector model
5. Identify: Which 209 ventures (789-580) are phantom/new?

---

## Critical Questions to Answer (Before Populating)

### 1. Venture Count Reality
- **In Supabase:** 580 real ventures (verified)
- **In our registry:** 789 ventures claimed
- **Gap:** 209 ventures (26.5% of portfolio)

**Question:** Are the 209 "missing" ventures:
- Phantom duplicates that were deduped?
- Real ventures not yet migrated to Supabase?
- Planned ventures not yet created?
- Misclassified in old CSV?

### 2. Sector Model Direction
- **Option A:** Expand Supabase sectors table from 16 to 36 (add our model)
- **Option B:** Replace with 25-category Supabase model (simpler, less opinionated)
- **Option C:** Create mapping layer (both models coexist)

**Recommendation:** Option A — we've already built the 36-sector model; expand Supabase to match it.

### 3. Bases Table Location
- Create `bases` table in Supabase?
- Or keep it in our YAML registries and sync via API?

**Recommendation:** Create in Supabase — makes gate tracking queryable.

### 4. Entities Registry Verification
- `legal_entities` table (682 rows) — is this the entities registry?
- What's the schema? (entity_id, legal_name, entity_type, owner, etc.)
- Do we need to expand it for 150+ entities from our family office model?

---

## Next Steps (Sep 26-30)

### Sep 26: Data Mapping
1. **List existing Supabase data:**
   - All 16 sectors (current)
   - All 5 OpCos (current)
   - Schema of `legal_entities` (verify entities registry)
   - Schema of `ventures` (field mapping)

2. **Create mapping document:**
   - 25 Supabase categories → 36 SEC-XXX codes
   - Current 580 ventures → SEC-XXX assignment
   - Gap analysis: 209 missing ventures

### Sep 27-28: Infrastructure Build
1. **Update schemas:**
   - Add missing columns to `sectors`, `opcos`
   - Create `bases` table with 11-point gate framework

2. **Insert data:**
   - Populate 20 missing sectors
   - Populate 30 missing OpCos
   - Populate 36 Bases (all gates = PENDING initially)

### Sep 29-30: Verification
1. **Run audit queries:**
   - Verify 36 sectors exist
   - Verify 35 OpCos exist
   - Verify 36 Bases exist
   - Verify ventures → sector assignments

2. **Sync registries:**
   - Update local SECTOR-REGISTRY.yaml from Supabase
   - Update local OPCO-REGISTRY.yaml from Supabase
   - Update local BASE-REGISTRY.yaml from Supabase

---

## Blockers & Decisions

| Issue | Status | Decision | By |
|-------|--------|----------|-----|
| Venture count (580 vs 789) | OPEN | Are 209 ventures phantom or real? | Founder |
| Sector model (25 vs 36) | OPEN | Expand Supabase to 36 or simplify to 25? | Founder |
| Bases table location | OPEN | Create in Supabase or keep in YAML? | Founder |
| Entities registry verify | OPEN | Confirm `legal_entities` is the right table | Founder |

---

## Authority & Verification

**Data sources verified:**
- ✅ Supabase `ventures` table (580 real ventures)
- ✅ Supabase `sectors` group-by (25 categories)
- ✅ Supabase `legal_entities` (682 records — entities registry)
- ✅ Supabase `graph_entities` (16,840 nodes)
- ❌ Manual registries (disconnected, need rebuild)

**Next action:** Confirm reconciliation strategy with founder, then execute Phase 1-3.

---

**Status: AWAITING DECISIONS ON 4 CRITICAL QUESTIONS**

**Updated:** 2026-09-25 (Sep 25 reconciliation initiated)
