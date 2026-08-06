# VENTURE-PIPELINE-ALIASES

**System:** Worldwidebro Holdings  
**Date:** 2026-08-05  
**Purpose:** Document all venture naming conventions, aliases, and canonical IDs for routing and reference  
**Source:** VENTURE-READINESS-SCORECARD-V2.csv + VENTURE-AUDIT-COMPLETE-2026-08-05.md + active portfolio  

---

## PRIMARY VENTURES (8 active in immediate roadmap)

### 1. LT-005 — Medical Courier Dispatch

**Aliases:**
- `LT-005-Medical-Courier-Dispatch` (scorecard)
- `LT-005` (compact)
- Medical logistics
- Courier dispatch

**Canonical ID:** `AIBOS-VEN-LT-005`  
**Status:** Operations (68% complete)  
**Pipeline Stage:** Sales (Stage 10)  
**Autonomy:** 85% (Sep 30, 2026)  
**Prospects:** 3-5 (warm)

---

### 2. LT-011 — Dispatch Software

**Aliases:**
- `LT-011-Dispatch-Software`
- `LT-011`
- White-label dispatcher SaaS

**Canonical ID:** `AIBOS-VEN-LT-011`  
**Status:** Build (3.5% complete)  
**Pipeline Stage:** Build (Stage 6)  
**Autonomy:** 10% (Dec 24, 2026)  
**Prospects:** 0 (pre-launch)

---

### 3. OPS-001-CTO — Fractional CTO Agency

**Aliases:**
- `OPS-001-Fractional-CTO-Agency`
- `OPS-001-CTO`
- `OPS-001` (when context clear)
- Fractional CTO services

**Canonical ID:** `AIBOS-VEN-OPS-001-CTO`  
**Status:** Sales (27.4% complete)  
**Pipeline Stage:** Sales (Stage 10)  
**Autonomy:** 40% (Sep 30, 2026)  
**Prospects:** 50 (qualified)

---

### 4. OPS-001-STAFFING — Venture Staffing Operations

**Aliases:**
- `OPS-001-VENTURE-STAFFING`
- `OPS-001-Staffing`
- `OPS-001` (when context clear)
- Venture staffing operations

**Canonical ID:** `AIBOS-VEN-OPS-001-STAFFING`  
**Status:** Validation (22.8% complete)  
**Pipeline Stage:** Validation (Stage 2)  
**Autonomy:** 15% (Oct 21, 2026)  
**Prospects:** 74 (all in Notion — CRITICAL)

**⚠️ BLOCKER:** Export 74 prospects Notion → Supabase TODAY (Aug 5)

---

### 5. EC-001 — Angels in Daylight

**Aliases:**
- `EC-001-Angels-in-Daylight`
- `EC-001`
- Angels in Daylight (brand)

**Canonical ID:** `AIBOS-VEN-EC-001`  
**Status:** Customer Acquisition (27.4% complete)  
**Pipeline Stage:** Customer Acquisition (Stage 9)  
**Autonomy:** 35% (Sep 30, 2026)  
**Prospects:** 0 (no marketing)

---

### 6. EC-112 — Cosmic Kitty

**Aliases:**
- `EC-112` (compact)
- `EC-112-Cosmic-Kitty` (expected format)
- Cosmic Kitty (brand)
- E-commerce dropshipping

**Canonical ID:** `AIBOS-VEN-EC-112`  
**Status:** Archived codebase (50% complete)  
**Pipeline Stage:** Customer Success (Stage 13)  
**Autonomy:** 60% (Oct 21, 2026)  
**Prospects:** 0 (not deployed)

**Location:**
- Full codebase: `_archive/ec-112-cosmic-kitty/`
- Stub: `WORLDWIDEBRO-OS/03-PORTFOLIO/ventures/active/ec-112/`

---

### 7. CON-001 — Ace Construction

**Aliases:**
- `CON-001-ACE-CONSTRUCTION`
- `CON-001`
- Ace Construction (brand)

**Canonical ID:** `AIBOS-VEN-CON-001`  
**Status:** Build (3.5% complete)  
**Pipeline Stage:** Build (Stage 6)  
**Autonomy:** 10% (Nov 25, 2026)  
**Prospects:** 0 (pre-launch)

---

### 8. RE-001 — Property Holdings

**Aliases:**
- `RE-001-PROPERTY-HOLDINGS`
- `RE-001`
- Property Holdings (brand)

**Canonical ID:** `AIBOS-VEN-RE-001`  
**Status:** Build (3.5% complete)  
**Pipeline Stage:** Build (Stage 6)  
**Autonomy:** 10% (Dec 9, 2026)  
**Prospects:** 0 (pre-launch)

---

## SHARED PIPELINE (Supabase venture_leads table)

**Canonical Source:** Supabase  
**Shared by:** LT-005, OPS-001-CTO, EC-001, EC-112, OPS-001-STAFFING

### Active Prospects Summary

| Venture | Prospects | Status | Confidence |
|---------|-----------|--------|------------|
| OPS-001-STAFFING | 74 | Qualified | 🔴 Notion-only |
| OPS-001-CTO | 50 | Qualified | 🟡 Warm |
| LT-005 | 5 | Proposal | 🟢 Strong |
| EC-001 | 0 | — | 🔴 Cold |
| EC-112 | 0 | — | 🔴 Archived |

---

## NAMING CONVENTION STANDARD

**Format:** `{SECTOR}-{NUMBER}-{NAME}`

**Sectors in roadmap:**
- `LT` = Logistics/Transport
- `EC` = E-Commerce
- `OPS` = Operations/Admin
- `CON` = Construction
- `RE` = Real Estate

**Canonical ID format:** `AIBOS-VEN-{SECTOR}-{NUMBER}[-{TIER}]`

Example: `AIBOS-VEN-OPS-001-CTO` vs `AIBOS-VEN-OPS-001-STAFFING`

---

## DOCUMENTATION RULES

**Use full name:** `OPS-001-Fractional-CTO-Agency` in:
- Supabase venture_id field
- CSV/JSON data files
- First mention in documents

**Use compact:** `OPS-001-CTO` in:
- Code comments (space constraint)
- Branch names: `ops/ops-001-cto/email-automation`
- When context disambiguates

**Avoid bare `OPS-001`** in shared docs (ambiguous; use `-CTO` or `-STAFFING`)

---

## CROSS-REFERENCES

### In code:
```python
if venture_id.startswith("OPS-001"):
    # Could be CTO or STAFFING — check full name
    if "CTO" in venture_id:
        handle_cto_services()
    elif "STAFFING" in venture_id:
        handle_staffing_operations()
```

### In SQL:
```sql
SELECT * FROM ventures 
WHERE venture_id IN (
  'LT-005-Medical-Courier-Dispatch',
  'OPS-001-Fractional-CTO-Agency',
  'OPS-001-VENTURE-STAFFING'
)
```

### In Markdown:
```md
[[AIBOS-VEN-LT-005]]
[[AIBOS-VEN-OPS-001-CTO]]
[[AIBOS-VEN-OPS-001-STAFFING]]
```

---

## CRITICAL BLOCKERS

### 🔴 OPS-001-STAFFING: Notion Lock-In

**Blocker:** All 74 prospects in Notion only (no Supabase backup)  
**Action:** Export → Supabase TODAY (1-2 hours)  
**Impact:** Blocks autonomy roadmap until resolved  
**Risk:** Total data loss if Notion deleted/hacked

---

**Generated:** 2026-08-05 3:55pm EDT  
**Next Review:** 2026-08-12 (Week 1 progress)
