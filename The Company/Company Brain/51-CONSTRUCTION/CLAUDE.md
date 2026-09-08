---
# Sector CLAUDE.md Template
# Copy to each active sector: 51-CONSTRUCTION/, 54-FINANCIAL/, 58-LOGISTICS/, 62-TECHNOLOGY/, etc.
# Customize: venture aliases, key projects, sector-specific blockers
---

# CLAUDE.md — SEC-002: Construction & Infrastructure

**Scope:** All construction ventures (CON-001 through CON-200) and related infrastructure.  
**Sector:** SEC-002 | **OpCo:** OpCo-002 | **Control Planes:** CP-012, CP-026, CP-027

---

## SECTOR CONTEXT

**Active Ventures:** CON-001 (Ace Construction, revenue), CON-011 (Electrical, validating)

**Quick Aliases:** 
- CON-NNN = SEC-002-NNN (venture ID)
- Sector repos: `github.com/Worldwidebro/con-ventures`

**Known Blockers:**
- (List sector-specific blockers here)

**ClickUp Workspace:** Construction (empty) | Medical Courier handles LT-005 logistics

---

## DISCOVERY ORDER (Sector-Specific)

1. **Venture state:** Check `ventures-by-sector.yaml#SEC-002`
2. **Active projects:** ClickUp Construction workspace (if populated) or Antwuan Johns > Projects
3. **Control planes:** `control-planes-by-sector.yaml#SEC-002` → CP-012, CP-026, CP-027
4. **Memory files:** `/memory/sec-002-construction/`
5. **Master reference:** [[SEC-002-construction-infrastructure]] in Obsidian

---

## VENTURE QUICK REFERENCE

| ID | Name | Status | Repo | Notes |
|----|------|--------|------|-------|
| CON-001 | Ace Construction | Operating | con-001-ace-construction | Live revenue |
| CON-011 | Electrical Sector | Validating | con-011-electrical | Sector deploy ready |

---

## RULES (Sector-Specific)

- All venture changes → Git + PR (no direct DB edits except migrations)
- Sector branch strategy: `con/venture-id/feature`
- ClickUp integration: Use Construction workspace folder assignments
- Tests must pass before merge to main

---

## THREE SOURCES OF TRUTH

1. **Supabase:** Live venture state (financials, status, relationships)
2. **Neo4j:** Relationships between ventures, projects, control planes
3. **CSV:** VENTURE-READINESS-SCORECARD-V2.csv (readiness %)

---

## GLOBAL OVERRIDES

See `/Users/acebless/.claude/CLAUDE.md` for:
- API KEY & TOKEN EXTRACTION (browser-automated)
- 30 Control Points registry
- 21 MCPs (ClickUp, HubSpot, etc.)
- Loop Engineering (L1/L2/L3 autonomy)

---

**Updated:** 2026-09-02  
**Master Reference:** [[SECTOR-TAXONOMY-MASTER]] | [[SEC-002-construction-infrastructure]]
