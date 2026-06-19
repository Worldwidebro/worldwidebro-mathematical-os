# Holding Company Restructuring Plan (June 17, 2026)

## Current State Audit

### What Exists ✅
1. **RE-001-Worldwidebro-Holdings/** (30-folder real estate structure)
   - Specialized for real estate
   - 30 functional departments
   - Not generalizable to 18 OPCOs

2. **venture-hub/** (707 ventures)
   - 707 venture folders
   - 31 sectors (CON, EC, FIN, OPS, BW, RE, ST, EDU, HC, LOG, etc.)
   - 780 files (mostly .md)
   - No OPCO assignment

3. **Root-level documentation** (240 .md files)
   - Planning, strategy, architecture
   - Needs consolidation

4. **5 Agent Loops** (operational automation)
   - Loop 1-5 scripts ready to execute
   - Process 707 ventures

### What's Needed 🏗️
1. **Holding Company Structure** (Worldwidebro Holdings)
   - Dynasty Trust documentation
   - Cap table, governance
   - Master policies

2. **18 OPCOs** (Operating Companies)
   - One standardized 18-PDF template per OPCO
   - NOT one template per venture
   - Shared infrastructure

3. **Venture Mapping**
   - Assign 707 ventures → 18 OPCOs
   - Based on sector/industry match

4. **Reorganized venture-hub/**
   - venture-hub/OPCO-Name/
   - Ventures nested under OPCO
   - Standardized structure

5. **Notion Hierarchy**
   - Holding Company Dashboard
   - 18 OPCO Dashboards
   - 707 Venture Records

---

## Mapping Strategy: 31 Sectors → 18 OPCOs

### Step 1: Define the 18 OPCOs

Based on your venture sectors, map to 18 operating categories:

| # | OPCO | Sectors | Count |
|---|------|---------|-------|
| 1 | OPCO-Financial | FIN, FS | 42 |
| 2 | OPCO-Technology | TECH, LT | 45+ |
| 3 | OPCO-RealEstate | RE, REAL | 35+ |
| 4 | OPCO-Construction | CON, ACE | 45+ |
| 5 | OPCO-Transportation | LOGIS, TRN | 40+ |
| 6 | OPCO-Healthcare | HC, MED | 36+ |
| 7 | OPCO-Education | EDU | 38+ |
| 8 | OPCO-Staffing | ST, STAFF | 32+ |
| 9 | OPCO-Hospitality | HOSP, REST | ? |
| 10 | OPCO-Retail | RET, SHOP | ? |
| 11 | OPCO-Media | MEDIA, COMM | ? |
| 12 | OPCO-BeautyWellness | BW, BEAUTY | 38+ |
| 13 | OPCO-Marketplace | MARKET, SPEC | ? |
| 14 | OPCO-Operations | OPS, ADMIN | 67+ |
| 15 | OPCO-Manufacturing | MFG, MANUF | ? |
| 16 | OPCO-Agriculture | AGR, FARM | ? |
| 17 | OPCO-Energy | ENERGY, UTIL | ? |
| 18 | OPCO-Investment | INVEST, WEALTH | ? |

### Step 2: Identify Missing Sectors

From venture-hub, sectors present:
- BW (38) ✓
- COMM (?)
- CON (45) ✓
- EC (110) → OPCO-Marketplace
- EDU (38) ✓
- EM (?)
- ET (?)
- FH (?)
- FIN (42) ✓
- FS (?)
- LT (?)
- MC (?)
- OPS (67) ✓
- PS (?)
- RE (35) ✓
- SPEC (?)
- ST (32) ✓
- TECH (?)

**Need:** Map all 31 sectors to 18 OPCOs

---

## Execution Sequence (Do Not Create, Only Reorganize)

### Phase 1: Create OPCO Master Structure
**Location:** `/Users/acebless/Documents/Worldwidebro-Holdings/`

```
Worldwidebro-Holdings/
├── 00_HOLDING_COMPANY/
│   ├── Holding_Company_Charter.pdf
│   ├── Dynasty_Trust_Documents.pdf
│   ├── Master_Cap_Table.pdf
│   ├── Governance_Manual.pdf
│   ├── Risk_Framework.pdf
│   ├── Acquisition_Playbook.pdf
│   ├── Venture_Creation_Playbook.pdf
│   ├── Capital_Allocation_Framework.pdf
│   ├── Portfolio_Dashboard.pdf
│   └── Succession_Plan.pdf
│
├── OPCO-Financial/
├── OPCO-Technology/
├── OPCO-RealEstate/
├── OPCO-Construction/
├── OPCO-Transportation/
├── OPCO-Healthcare/
├── OPCO-Education/
├── OPCO-Staffing/
├── OPCO-Hospitality/
├── OPCO-Retail/
├── OPCO-Media/
├── OPCO-BeautyWellness/
├── OPCO-Marketplace/
├── OPCO-Operations/
├── OPCO-Manufacturing/
├── OPCO-Agriculture/
├── OPCO-Energy/
└── OPCO-Investment/
```

### Phase 2: Create One Standardized 18-PDF Template
**File:** `OPCO-MASTER-TEMPLATE.md`

Standard for every OPCO:
1. Business Profile
2. Formation Documents
3. EIN Documents
4. Ownership Structure
5. Operating Agreement
6. Organizational Chart
7. Business Plan
8. Financial Model
9. Banking Profile
10. Licenses & Permits
11. Insurance Portfolio
12. Standard Operating Procedures
13. Sales & Marketing Plan
14. Contracts Library
15. HR Manual
16. Compliance & Risk
17. Technology Stack
18. KPI Dashboard

Each OPCO gets ONE set of these 18 PDFs (not duplicated per venture).

### Phase 3: Reorganize venture-hub/
**Move ventures under OPCO structure:**

```
venture-hub/
├── OPCO-Financial/
│   ├── FIN-001/
│   ├── FIN-002/
│   └── ... (all FIN ventures)
├── OPCO-Technology/
│   ├── TECH-001/
│   └── ... (all TECH ventures)
├── OPCO-Construction/
│   ├── CON-001/
│   └── ... (all CON ventures)
└── ... (rest of OPCOs)
```

**Do NOT create new venture folders, MOVE existing ones.**

### Phase 4: Create Venture Mapping CSV
**File:** `OPCO_VENTURE_MAPPING.csv`

```csv
venture_id,venture_name,sector,assigned_opco,status,owner,revenue_ytd
CON-001,LocalRoof Co,CON,OPCO-Construction,active,antwuan-johns,45000
FIN-001,GenixBank,FIN,OPCO-Financial,active,contractor-1,82000
...
```

### Phase 5: Build Notion Hierarchy
**Structure:**
- Holding Company Dashboard
  - OPCO-Financial Dashboard
    - 42 Venture Records
  - OPCO-Technology Dashboard
    - 45+ Venture Records
  - ... (repeat for all 18)

---

## What NOT to Do ❌
- ❌ Create new PDF documents (only organize existing files)
- ❌ Create 707 separate PDF binders (one per OPCO instead)
- ❌ Move files from venture-hub to random locations
- ❌ Create duplicate directories

## What TO Do ✅
- ✅ Create Worldwidebro-Holdings/ directory
- ✅ Create 18 OPCO folders
- ✅ Move venture-hub/ UNDER Worldwidebro-Holdings/
- ✅ Reorganize ventures by OPCO
- ✅ Create OPCO_VENTURE_MAPPING.csv
- ✅ Update master documents to reference new structure
- ✅ Create Notion dashboard
- ✅ Build one 18-PDF template (shared, not per venture)

---

## Files to Update (No New Files)

Update these existing files to reference new structure:
- `README-WORLDWIDEBRO-OS.md`
- `VENTURE-OS-COMMAND-CENTER-MASTER.md`
- `venture-hub/PROJECT.md`
- `AGENT-LOOPS-CONFIG.md`

---

## Success Criteria

✅ Worldwidebro-Holdings/ exists with 18 OPCOs  
✅ venture-hub/ reorganized under OPCOs  
✅ OPCO_VENTURE_MAPPING.csv created  
✅ One 18-PDF template for OPCOs (not per venture)  
✅ Notion hierarchy established  
✅ Master docs updated  
✅ No duplicate files  
✅ No new unnecessary documents created  

---

**Ready to execute Phase 1?**
