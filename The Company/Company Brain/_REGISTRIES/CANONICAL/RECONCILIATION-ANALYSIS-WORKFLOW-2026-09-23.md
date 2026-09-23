# Reconciliation Analysis Workflow — Sep 23, 2026

**Status:** OPTION 2 DESIGN — Comprehensive Reconciliation Strategy  
**Auditor:** Claude Haiku 4.5 (Data Scientist)  
**Data Sources:** CSV (655 dedup), Registries (789), Supabase (580 real)  
**Authority:** Phase 2 Data Integrity (Sep 25-30 execution)  

---

## EXECUTIVE SUMMARY

Three competing venture count models exist. Before we can evaluate Base gates, assign agents, or activate revenue pipelines, we must:

1. **Map** 25 Supabase sector categories → 36 SEC-XXX codes
2. **Reconcile** 580 operational ventures in Supabase against 655 CSV unique ventures
3. **Classify** 177 identified sector misclassifications (tech-domain vs. business-domain)
4. **Verify** 4 critical disputes (LT-005/LT-011, SEC-024, SEC-012, SEC-020)
5. **Populate** Supabase with expanded 36-sector model (36 sectors, 35 OpCos, 36 Bases)

**Success Criteria:**
- ✅ Single source of truth: Supabase (580 operational ventures verified)
- ✅ Expanded model: 36 sectors + 35 OpCos + 36 Bases in Supabase
- ✅ Classification audit: 177 misclassifications reclassified + corrected
- ✅ Base gates: All 36 bases have correct venture assignments
- ✅ Revenue attribution: Each active venture mapped to correct Base, OpCo, Agent

---

## PHASE 1: DATA MAPPING (Sep 26)

### Task 1.1: Inventory Supabase Schema

**Goal:** Understand the shape of operational data in Supabase.

**Steps:**
1. List existing sectors table (16 records currently)
2. List existing opcos table (5 records currently)
3. Query ventures table: group by sector, count ventures per sector
4. Inspect legal_entities schema: is it the entities registry?
5. Check graph_entities + graph_relationships tables (16,840 + ??? records)

**Output:** Supabase_Schema_Audit.md (schema details, row counts, current state)

**Query Examples:**
```sql
-- What sectors exist today?
SELECT id, name, status FROM sectors ORDER BY id;

-- What are the 25 actual sector categories in ventures?
SELECT sector, COUNT(*) as venture_count FROM ventures GROUP BY sector ORDER BY venture_count DESC;

-- Legal entities schema?
SELECT column_name, data_type, is_nullable FROM information_schema.columns 
WHERE table_name='legal_entities' ORDER BY ordinal_position;

-- Are there 682 entities or fewer?
SELECT COUNT(*) as entity_count FROM legal_entities;
```

### Task 1.2: Map Supabase Categories → 36 SEC-XXX Codes

**Goal:** Create definitive mapping from 25 Supabase categories to our 36-sector model.

**Steps:**
1. List all 25 Supabase sector categories (from ventures group-by)
2. For each category, identify which SEC-XXX codes it maps to:
   - Use our 36-sector model (SECTOR-REGISTRY.yaml)
   - Use venture name keyword analysis
   - Use venture ID prefix patterns (FIN-→SEC-008, LT-→SEC-017, etc.)
3. Handle boundary ambiguities (e.g., "technology" might be SEC-024, SEC-028, or SEC-032)
4. Produce mapping table: `Supabase_Category → [SEC-XXX, SEC-YYY, ...]`

**Output:** Supabase_to_SEC_Mapping.csv
```
supabase_category,primary_sec_code,secondary_sec_codes,boundary_notes,venture_examples
technology,SEC-024,SEC-028|SEC-032,"Overlap with enterprise software & AI/ML",CALLCENTER|tech-venture-1|tech-venture-2
operations,SEC-003,SEC-014|SEC-019,"HR/staffing or sales/marketing; check venue names",OPS-001
e-commerce,SEC-021,SEC-004,"Retail or community marketplace; check business model",ecom-venture-1
```

### Task 1.3: Verify Data Discrepancies

**Goal:** Document why 25 categories ≠ 36 sectors.

**Questions to Answer:**
1. Are there 11 SEC-XXX codes with ZERO ventures in Supabase? Which ones?
   - Answer: If SEC-037, SEC-035, etc. have no ventures, they're not in Supabase yet
2. Are there venturesincorrectly categorized in Supabase (category mismatch)?
   - Example: LT-005 is in "operations" in Supabase but should be "logistics"?
3. Missing ventures: Are 580 Supabase ventures a subset of 655 CSV ventures?
   - Answer: Match CSV venture_id against Supabase to find 75 missing
   - Are they duplicates, planned ventures, or data corruption?

**Query:**
```sql
-- Find CSV ventures NOT in Supabase
SELECT v.venture_id, v.venture_name, v.canonical_sector_id 
FROM (SELECT DISTINCT venture_id FROM ALL_789_VENTURES_36_SECTOR_ALIGNMENT_DEDUPED.csv) csv_ventures
LEFT JOIN ventures sb_ventures ON csv_ventures.venture_id = sb_ventures.venture_id
WHERE sb_ventures.venture_id IS NULL;
```

---

## PHASE 2: CLASSIFICATION AUDIT (Sep 27-28)

### Task 2.1: Identify & Classify Misclassifications

**Goal:** Find all ventures classified by tech-domain instead of business-domain.

**Misclassification Patterns:**
```
FIN-* ventures → currently SEC-032 (AI/ML)
           → should be SEC-008 (Financial Services)
  Example: FIN-003 "AI Boss Hub Lite" is tech, but is fundamentally Finance

LT-* ventures → scattered across sectors
           → should be SEC-017 (Logistics) OR SEC-012 (Healthcare Logistics)
  Example: LT-005 "Medical Courier" in SEC-001 should be SEC-017 + SEC-012

HR-* ventures → mixed SEC-014 + SEC-024
           → should be SEC-014 (HR/Staffing)

MKT-* ventures → mixed SEC-019 + SEC-024
           → should be SEC-019 (Marketing & Advertising)
```

**Approach:**
1. Use sector_classification_model.py to detect HIGH-CONFIDENCE misclassifications
2. For each misclassified venture:
   - Current sector: `{assigned_sector}`
   - Predicted sector: `{predicted_sector}` (via ID prefix + name keywords)
   - Confidence: HIGH / MEDIUM / LOW
   - Recommended action: MOVE / FLAG_MANUAL / KEEP
3. Classify into buckets:
   - **Move immediately** (HIGH confidence, clear boundaries)
   - **Flag for review** (MEDIUM confidence, needs founder decision)
   - **Keep** (LOW confidence, boundary unclear, needs stakeholder input)

**Output:** Classification_Audit_2026-09-23.csv
```
venture_id,venture_name,current_sector,predicted_sector,confidence,recommendation,evidence
FIN-003,AI Boss Hub Lite,SEC-032,SEC-008,HIGH,MOVE,"ID prefix FIN → Finance, not AI/ML"
LT-005,HealthRoute Courier,SEC-001,SEC-017,HIGH,MOVE,"ID prefix LT → Logistics, customer vertical=healthcare secondary"
FIN-010,AI Powered Garbage Collection,SEC-032,SEC-008,MEDIUM,FLAG,"Business is waste mgmt (trash) but powered by AI"
```

### Task 2.2: Fix Critical Disputes

**Goal:** Resolve 4 CRITICAL audit findings from Phase 2 audit.

| Dispute | Finding | Evidence | Resolution |
|---------|---------|----------|-----------|
| **LT-005 / LT-011** | Claimed SEC-017, CSV shows SEC-001 | CSV line-by-line audit | Query Supabase: is LT-005 in "healthcare-logistics" or "wellness"? If healthcare, move to SEC-017 + SEC-012 secondary |
| **Venture Counts** | SEC-024: Registry claims 243, CSV shows 24 (-90%) | Registry pre-dedup, CSV post-dedup | Accept CSV as truth (655 unique); calculate corrected registry counts |
| **SEC-012 Unmapped** | 4 ventures in CSV, zero in BASE-012 | All 4 ventures are real (not phantom) | Create BASE-012; add 4 real ventures; activate healthcare sector |
| **SEC-020 Anomaly** | Only 1 venture (RE-001) | Audit universe for property-related ventures across all sectors | If PS-011 is same as RE-001, consolidate. If separate, verify RE-001 exists in Supabase. |

**Action:**
1. Query Supabase directly for each disputed venture
2. Verify venture_id, venture_name, sector assignment
3. Reconcile vs. CSV data
4. Document discrepancy source (data corruption, schema mismatch, deduplication artifact)

---

## PHASE 3: MULTIDIMENSIONAL CLASSIFICATION (Sep 29)

### Task 3.1: Build Corrected Venture-Sector Lookup

**Goal:** Create authoritative venture-sector mapping table with business-domain classification.

**Output:** Venture_Sector_Lookup_Corrected.csv
```
venture_id,venture_name,primary_sector,secondary_sectors,business_domain,customer_vertical,technology_domain,opco_id,base_id,revenue_status,reality_score,notes
OPS-001,Staff Augmentation,SEC-014,,Human Resources,Corporate HR,Talent Matching,OPCO-014,BASE-014,GENERATING,100%,"Active revenue loop"
LT-005,HealthRoute Courier,SEC-017,SEC-012,Logistics,Healthcare,Dispatch Software,OPCO-017,BASE-017,GENERATING,100%,"Corrected: moved from SEC-001 → SEC-017 + SEC-012"
FIN-003,AI Boss Hub Lite,SEC-008,,Financial Services,Business Finance,AI/ML,OPCO-008,BASE-008,PENDING,30%,"Corrected: moved from SEC-032 → SEC-008"
```

**Schema:**
- `venture_id`: Unique venture identifier (FIN-003, LT-005, OPS-001)
- `venture_name`: Human-readable name
- `primary_sector`: Business domain (SEC-008, SEC-017, etc.)
- `secondary_sectors`: Related sectors (healthcare, technology, etc.)
- `business_domain`: What business does this venture do? (not tech)
- `customer_vertical`: Who are the customers?
- `technology_domain`: What technology powers it? (independent of business)
- `opco_id`: Operating company
- `base_id`: Which Base owns this venture
- `revenue_status`: GENERATING | PENDING | FUNDRAISING | PROTOTYPE
- `reality_score`: 0-100% (from Phase 1 audit)
- `notes`: Reclassification rationale, disputes, links to corrections

### Task 3.2: Create Venture-Base Assignment Map

**Goal:** For each venture, determine which Base(s) own it.

**Logic:**
1. Primary sector → Primary Base (e.g., LT-005 with primary SEC-017 → BASE-017)
2. Secondary sectors → Secondary Base assignments (e.g., LT-005 secondary SEC-012 → BASE-012 alert)
3. Cross-Base coordination: If a venture belongs to multiple bases, define handoff protocol

**Output:** Venture_Base_Assignments.csv
```
venture_id,venture_name,primary_base,primary_base_lead,secondary_bases,shared_protocol,notes
LT-005,HealthRoute Courier,BASE-017,Dispatch Agent,"BASE-012","Healthcare Logistics Task Force","Coordinates with healthcare vertical"
OPS-001,Staff Augmentation,BASE-014,HR Agent,"","","No secondary base"
CON-001,ACE Construction,BASE-002,Construction Agent,"","","New venture; gate evaluation pending"
```

---

## PHASE 4: SUPABASE SCHEMA EXPANSION (Sep 30 - Oct 1)

### Task 4.1: Create Missing Tables & Expand Schemas

**SQL Migrations:**
```sql
-- 1. Expand sectors table (16 → 36)
ALTER TABLE sectors ADD COLUMN IF NOT EXISTS sector_id VARCHAR(10) UNIQUE;
ALTER TABLE sectors ADD COLUMN IF NOT EXISTS description TEXT;
ALTER TABLE sectors ADD COLUMN IF NOT EXISTS status VARCHAR(50) DEFAULT 'STAGING';
ALTER TABLE sectors ADD COLUMN IF NOT EXISTS opco_id VARCHAR(10);

-- Insert 20 missing sectors (SEC-002, SEC-003, SEC-005, ...)
INSERT INTO sectors (sector_id, name, description, status, opco_id)
VALUES 
  ('SEC-002', 'Construction & Infrastructure', '...', 'STAGING', 'OPCO-002'),
  ('SEC-003', 'Operations & HR', '...', 'ACTIVE', 'OPCO-003'),
  ...
ON CONFLICT (sector_id) DO NOTHING;

-- 2. Expand opcos table (5 → 35)
ALTER TABLE opcos ADD COLUMN IF NOT EXISTS opco_id VARCHAR(10) UNIQUE;
ALTER TABLE opcos ADD COLUMN IF NOT EXISTS sector_id VARCHAR(10);
ALTER TABLE opcos ADD COLUMN IF NOT EXISTS status VARCHAR(50) DEFAULT 'ACTIVE';

-- Insert 30 missing OpCos
INSERT INTO opcos (opco_id, name, sector_id, status)
VALUES 
  ('OPCO-002', 'Construction OpCo', 'SEC-002', 'ACTIVE'),
  ('OPCO-003', 'Operations OpCo', 'SEC-003', 'ACTIVE'),
  ...
ON CONFLICT (opco_id) DO NOTHING;

-- 3. Create bases table (NEW)
CREATE TABLE IF NOT EXISTS bases (
  id BIGSERIAL PRIMARY KEY,
  base_id VARCHAR(10) UNIQUE NOT NULL,
  sector_id VARCHAR(10) NOT NULL REFERENCES sectors(sector_id),
  opco_id VARCHAR(10) NOT NULL REFERENCES opcos(opco_id),
  name VARCHAR(255) NOT NULL,
  description TEXT,
  status VARCHAR(50) DEFAULT 'PENDING',
  venture_count INT DEFAULT 0,
  
  -- 11-point gate framework
  gate_1_sector_defined BOOLEAN DEFAULT FALSE,
  gate_2_sector_unique BOOLEAN DEFAULT FALSE,
  gate_3_venture_manifest BOOLEAN DEFAULT FALSE,
  gate_4_ventures_verified BOOLEAN DEFAULT FALSE,
  gate_5_opco_mapping BOOLEAN DEFAULT FALSE,
  gate_6_ownership_defined BOOLEAN DEFAULT FALSE,
  gate_7_base_purpose BOOLEAN DEFAULT FALSE,
  gate_8_whoami_file BOOLEAN DEFAULT FALSE,
  gate_9_agent_assignment BOOLEAN DEFAULT FALSE,
  gate_10_skills_mapped BOOLEAN DEFAULT FALSE,
  gate_11_workflows_mapped BOOLEAN DEFAULT FALSE,
  
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- 4. Add sector_id column to ventures (if missing)
ALTER TABLE ventures ADD COLUMN IF NOT EXISTS sector_id VARCHAR(10);

-- 5. Enable RLS on all new tables
ALTER TABLE bases ENABLE ROW LEVEL SECURITY;
ALTER TABLE sectors ENABLE ROW LEVEL SECURITY;
ALTER TABLE opcos ENABLE ROW LEVEL SECURITY;

-- 6. Create basic RLS policies (open for authenticated users)
CREATE POLICY "allow_authenticated_read" ON bases
  FOR SELECT USING (auth.role() = 'authenticated');
```

### Task 4.2: Populate New Tables

**Step 1: Insert 36 sectors**
- Load SECTOR-REGISTRY.yaml
- For each sector (SEC-001 to SEC-036):
  - Extract: name, description, opco_id, status
  - Insert into sectors table

**Step 2: Insert 35 OpCos**
- Load OPCO-REGISTRY.yaml
- For each OpCo (OPCO-001 to OPCO-035):
  - Extract: name, sector_id, status
  - Insert into opcos table

**Step 3: Insert 36 Bases**
- Load BASE-REGISTRY.yaml
- For each Base (BASE-001 to BASE-036):
  - Extract: name, sector_id, opco_id, description
  - Set all 11 gates to FALSE initially
  - Insert into bases table

### Task 4.3: Sync Ventures → Corrected Sectors

**Goal:** Update ventures table with corrected sector assignments.

**Steps:**
1. Load Venture_Sector_Lookup_Corrected.csv
2. For each venture, update ventures.sector to match corrected classification:
```sql
UPDATE ventures SET sector_id = $sector_id
WHERE venture_id = $venture_id;
```
3. Log corrections for audit trail:
   - Old sector vs. new sector
   - Reason (misclassification correction)
   - Date

---

## PHASE 5: VERIFICATION & AUDIT (Oct 1-2)

### Task 5.1: Run Audit Queries

**Goal:** Verify that all tables are correctly populated.

**Queries:**
```sql
-- 1. Verify 36 sectors exist
SELECT COUNT(*) as sector_count FROM sectors WHERE status IS NOT NULL;
-- Expected: 36

-- 2. Verify 35 OpCos exist
SELECT COUNT(*) as opco_count FROM opcos WHERE status IS NOT NULL;
-- Expected: 35

-- 3. Verify 36 Bases exist
SELECT COUNT(*) as base_count FROM bases;
-- Expected: 36

-- 4. Verify ventures are assigned to sectors
SELECT sector_id, COUNT(*) as venture_count
FROM ventures
WHERE sector_id IS NOT NULL
GROUP BY sector_id
ORDER BY venture_count DESC;

-- 5. Identify unassigned ventures
SELECT venture_id, venture_name, sector
FROM ventures
WHERE sector_id IS NULL;
-- Expected: 0 rows (all assigned)

-- 6. Verify no orphaned sectors (no ventures)
SELECT s.sector_id, s.name, COUNT(v.venture_id) as venture_count
FROM sectors s
LEFT JOIN ventures v ON s.sector_id = v.sector_id
GROUP BY s.sector_id
HAVING COUNT(v.venture_id) = 0
ORDER BY s.sector_id;
```

### Task 5.2: Sync Local Registries from Supabase

**Goal:** Make Supabase the source of truth; update local YAML registries.

**Steps:**
1. Export sectors table → SECTOR-REGISTRY.yaml (updated)
2. Export opcos table → OPCO-REGISTRY.yaml (updated)
3. Export bases table → BASE-REGISTRY.yaml (updated)
4. Export ventures table → ALL_789_VENTURES_36_SECTOR_ALIGNMENT_FINAL.csv
5. Commit all 4 files with message:
```
feat(reconciliation): supabase as source of truth
- Synced 36 sectors, 35 OpCos, 36 Bases from Supabase
- 580 operational ventures verified
- 177 sector misclassifications corrected
- All base gates initialized (pending evaluation)
```

---

## REFERENCE: Graph-Native Integration

### Existing Graph Ingestion Functions (From Graft)

The following production functions exist and can be reused for Phase 2 schema updates:

| Function | Location | Purpose |
|----------|----------|---------|
| `merge_sector()` | _PIPELINES/graph_ingestion_pipeline.py:74-114 | Merge Sector node with provenance tracking |
| `merge_venture()` | _PIPELINES/graph_ingestion_pipeline.py:116+ | Merge Venture node with verification |
| `neo4j_merge_classification()` | _MCP/fastmcp_server.py:289-336 | Merge venture classification + sector |
| `VentureOrchestrator` | _INFRASTRUCTURE/agents/venture_orchestrator.py:18-331 | Full orchestration class for venture operations |
| `generate_venture_document_os()` | scripts/venture_os_engine.py:592-1276 | Generate venture operating system docs |
| `getCapabilitiesBySector()` | vex-wired/vex-neo4j-connector.ts:91-105 | Query capabilities by sector (TypeScript) |
| `get_sector_code()` | _REGISTRIES/CANONICAL/NAICS-2022/generate_naics_artifacts.py:81-93 | NAICS sector code mapping |

**How to Use:** After reconciliation, use these functions to:
1. Create Sector + Venture nodes in Neo4j with corrected classifications
2. Establish sector→venture relationships
3. Link ventures to Base ownership nodes
4. Enable Agent context assembly queries

---

## BLOCKERS & DECISIONS

| Issue | Blocker | Resolution Path |
|-------|---------|-----------------|
| 4 Founder Decisions (Sep 25) | YES | Founder confirms: venture count reality, sector model direction, bases table location, entities registry schema |
| Supabase Schema Access | MAYBE | Verify MCP or CLI has write access to sectors/opcos/bases tables |
| Data Validation | LOW | Audit queries in Task 5.1 will catch schema or data errors |

---

## SUCCESS CRITERIA (Oct 2)

- ✅ Supabase contains 36 sectors, 35 OpCos, 36 Bases
- ✅ All 580 operational ventures assigned to SEC-XXX codes
- ✅ 177 sector misclassifications corrected and verified
- ✅ 4 critical disputes resolved with founder input
- ✅ Local registries synced from Supabase (single source of truth)
- ✅ Neo4j ready for agent context assembly queries
- ✅ Base gate evaluation can proceed with confidence

---

## NEXT STEPS (Oct 3 Onward)

1. **Base Gate Evaluation** (Oct 3-6) → Evaluate 11-point gates for each Base
2. **Base WHOAMI Creation** (Oct 6-15) → Create BASE-*/WHOAMI.md files with wiki links
3. **Agent Assignment** (Oct 15-22) → Wire agents to Bases, activate dispatch routers
4. **Revenue Loop Activation** (Oct 22-31) → OPS-001, LT-005, CALLCENTER full execution

---

**Status: OPTION 2 COMPLETE — Ready for Sep 26 execution**

**Updated:** 2026-09-23 (Data scientist reconciliation analysis)

---

## Control Base Reference

This document is mapped to [[B100|Control Base]] in the Company Brain.

**Wiki Link:** [[CBP_REGISTRY|_REGISTRIES/CANONICAL/CBP_REGISTRY.yaml#B100]]