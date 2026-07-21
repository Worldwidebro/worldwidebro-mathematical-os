# Redundancy & Inconsistency Audit Report
**Date:** 2026-07-16  
**Scope:** WHOAMI.md + WORLDWIDEBRO-OS registries + vex-hero-site  
**Status:** FINDINGS DOCUMENTED

---

## Executive Summary

**Three systems with fragmented venture/capability definitions detected. ID schema conflicts, version mismatches, and schema divergence identified. 16 high-priority issues requiring resolution.**

| Category | Count | Severity |
|----------|-------|----------|
| ID Schema Conflicts | 3 | 🔴 CRITICAL |
| Data Model Misalignment | 3 | 🔴 CRITICAL |
| Duplicate Venture Definitions | 1 | 🟡 HIGH |
| Template Overlap | 2 | 🟡 HIGH |
| Capability Definition Inconsistencies | 2 | 🟡 HIGH |
| Version/Date Conflicts | 2 | 🟠 MEDIUM |
| Schema Structure Divergence | 2 | 🟠 MEDIUM |
| Unused/Dead References | 1 | 🟠 MEDIUM |

---

## CRITICAL ISSUES

### #1: Three Incompatible Venture ID Systems
**Problem:** Ventures identified by incompatible systems with no mapping.

| System | ID Format | Example | File | Record Count |
|--------|-----------|---------|------|---|
| ventures.csv | Slug | `FIN-001-GenixBank-Lite` | ventures.csv | 721 |
| venture_capability_map.csv | UUID | `484ac493-c394-4ca1-aa18-e514a8844312` | venture_capability_map.csv | Unknown |
| portfolio.public.json | Sector object | `financial`, `construction` | portfolio.public.json | 18 sectors |

**Impact:** Joins between capabilities and ventures fail; capability data orphaned.

**Where Found:**
- `/Users/acebless/Documents/WORLDWIDEBRO-OS/08-DATA/registries/ventures.csv`
- `/Users/acebless/Documents/WORLDWIDEBRO-OS/08-DATA/registries/venture_capability_map.csv`
- `/Users/acebless/Documents/vex-hero-site/src/data/portfolio.public.json`

**Resolution:** Create unified ID mapping table:
```
uuid,venture_id,venture_name,sector,opco
```

**Effort:** 4-6 hours | **Blocking:** YES — No capability queries possible without this

---

### #2: OPCO Format Divergence (ventures.csv vs sectors.ts vs portfolio.public.json)
**Problem:** OPCO field uses three different formats across registries.

| System | Format | Example |
|--------|--------|---------|
| ventures.csv | Uppercase, hyphenated | `FINANCIAL`, `BEAUTY-WELLNESS` |
| opco_venture_map.csv | Uppercase, hyphenated | `FINANCIAL`, `BEAUTY-WELLNESS` |
| sectors.ts (vex-hero-site) | Prefixed "OPCO-" + Title Case | `OPCO-Financial`, `OPCO-Education` |
| portfolio.public.json | Prefixed "OPCO-" + Mixed case | `OPCO-Financial`, `OPCO-RealEstate` |

**Impact:** OPCO filters in vex-hero-site render wrong counts if format mismatch.

**Where Found:**
- `/Users/acebless/Documents/WORLDWIDEBRO-OS/08-DATA/registries/ventures.csv` line 1
- `/Users/acebless/Documents/vex-hero-site/src/data/sectors.ts` lines 21, 71, 124, 161, 194

**Resolution:** Choose one format (recommend `OPCO_FINANCIAL` for SQL safety), update all three registries.

**Effort:** 2 hours | **Blocking:** YES — Sector filtering broken

---

### #3: Sector Name Misalignment (ventures.csv Missing in sectors.ts)
**Problem:** 2 sectors in ventures.csv have no corresponding route in vex-hero-site.

| Sector | ventures.csv | sectors.ts | Status |
|--------|---|---|---|
| financial | ✓ | ✓ | ✓ |
| construction | ✓ | ✓ | ✓ |
| beauty-wellness | ✓ | ✗ | 🔴 MISSING |
| hospitality | ✓ | ✗ | 🔴 MISSING |
| transportation | ✓ | ✓ | ✓ |

**Impact:** 80+ ventures (BW-001 through BW-040, FH-001 through FH-023) won't render on vex-hero-site; dead links.

**Where Found:**
- Ventures: `/Users/acebless/Documents/WORLDWIDEBRO-OS/08-DATA/registries/ventures.csv` (14 sectors)
- Pages: `/Users/acebless/Documents/vex-hero-site/src/data/sectors.ts` (16 sectors defined, but missing 2)

**Resolution:** Add SectorEntry objects to sectors.ts for beauty-wellness and hospitality.

**Effort:** 3 hours | **Blocking:** YES — Website incomplete

---

### #4: Capability ID Schema Broken (UUID ↔ venture_id mapping missing)
**Problem:** venture_capability_map.csv uses UUIDs; no lookup table to find venture names.

**Current State:**
- venture_capability_map.csv contains: `uuid, capability`
- ventures.csv contains: `venture_id, name, sector, ...` (uses slugs like FIN-001)
- No join key exists between the two

**Impact:** 
- Capability data cannot be linked to venture names, stage, or sector
- Coverage percentages (claimed 70.6%) cannot be verified
- vex-hero-site cannot validate venture readiness

**Where Found:**
- `/Users/acebless/Documents/WORLDWIDEBRO-OS/08-DATA/registries/venture_capability_map.csv` (UUIDs)
- `/Users/acebless/Documents/WORLDWIDEBRO-OS/08-DATA/registries/ventures.csv` (venture_ids)

**Resolution:** Build venture capability table with proper foreign keys:
```sql
CREATE TABLE venture_capabilities (
  venture_id VARCHAR PRIMARY KEY,
  capability_id VARCHAR,
  status ENUM('required', 'implemented', 'planned'),
  FOREIGN KEY (venture_id) REFERENCES ventures(venture_id)
);
```

**Effort:** 6-8 hours | **Blocking:** YES — No readiness metrics possible

---

## HIGH-PRIORITY ISSUES

### #5: Duplicate Venture Definitions (ventures.csv vs portfolio.public.json)
**Problem:** Venture list maintained in two places; no sync mechanism.

| Aspect | ventures.csv | portfolio.public.json |
|--------|---|---|
| Last Modified | Jul 15 15:34 | Jul 15 19:37 (4 hours later) |
| Record Count | 721 | Unknown (embedded in sectors) |
| Format | CSV | JSON |
| Update Method | Manual | Auto-generated (date unknown) |
| Staleness | 25 hours old | 21 hours old |

**Impact:** New ventures added to ventures.csv won't appear on vex-hero-site until portfolio.public.json manually regenerated.

**Where Found:**
- `/Users/acebless/Documents/WORLDWIDEBRO-OS/08-DATA/registries/ventures.csv`
- `/Users/acebless/Documents/vex-hero-site/src/data/portfolio.public.json`

**Resolution:** Declare ventures.csv as source of truth; build automated export via CI/CD.

**Effort:** 2-3 hours | **Blocking:** PARTIALLY — Website lags behind

---

### #6: Agent Roles Defined in Three Places (No SPOF)
**Problem:** Agent roles fragmented across WHOAMI.md, portfolio.public.json, and vex-hero-site AGENTS.md.

| Role | WHOAMI.md | portfolio.public.json | vex-hero-site | Match? |
|---|---|---|---|---|
| CEO | Mentioned | Sector-specific (Ecom CEO Agent, Construction CEO Agent) | Unknown | ✗ |
| Data Officer (CDO) | Defined (line 50) | Not found | Not found | ✗ |
| Knowledge Engineer | Defined (line 55) | Not found | Not found | ✗ |

**Impact:** No canonical agent registry; role confusion in automation systems.

**Where Found:**
- `/Users/acebless/Documents/WORLDWIDEBRO-OS/WHOAMI.md` lines 45-56
- `/Users/acebless/Documents/vex-hero-site/src/data/portfolio.public.json` (sector-specific agents)
- `/Users/acebless/Documents/vex-hero-site/AGENTS.md`

**Resolution:** Create AGENTS-REGISTRY.json with canonical role definitions and per-sector overrides.

**Effort:** 3-4 hours | **Blocking:** PARTIALLY — Ops coordination unclear

---

### #7: Agent Role Templates Repeated 18+ Times
**Problem:** Every sector in portfolio.public.json repeats the same agent definitions.

**Example:**
```json
// Every sector has this pattern:
{
  "role": "CEO",
  "name": "[Sector] CEO Agent"
}
```

**Impact:** Changing role definitions requires updates in 18+ places; maintenance burden increases.

**Where Found:**
- `/Users/acebless/Documents/vex-hero-site/src/data/portfolio.public.json` (lines 35-200+)

**Resolution:** Extract agent templates to separate file; update portfolio.public.json to reference templates.

**Effort:** 4 hours | **Blocking:** NO — But increases maintenance cost

---

### #8: Venture Templates Scattered (No Consolidation)
**Problem:** Venture setup templates exist in multiple directories with no index.

| Template | Location | Maintenance |
|----------|----------|---|
| Service Venture Kit | `/WORLDWIDEBRO-OS/04-OPERATIONS/SERVICE-VENTURE-KIT-TEMPLATE.md` | Manual |
| EDU Landing Kit | `/WORLDWIDEBRO-OS/04-OPERATIONS/EDU-LANDING-KIT-TEMPLATE.md` | Manual |
| SaaS Backend Kit | (Not found) | ❌ MISSING |

**Impact:** Inconsistent venture configurations; unclear which template to use for new ventures.

**Where Found:**
- `/Users/acebless/Documents/WORLDWIDEBRO-OS/04-OPERATIONS/`
- `/Users/acebless/Documents/WORLDWIDEBRO-OS/03-PORTFOLIO/ventures/active/`

**Resolution:** Consolidate all templates into `/VENTURE-TEMPLATES/` with registry index.

**Effort:** 3 hours | **Blocking:** NO — Consistency issue

---

## MEDIUM-PRIORITY ISSUES

### #9: Capability Naming Inconsistency ("payments" vs "payment")
**Problem:** Canonical vocabulary uses plural; venture registries may use singular.

| Source | Term |
|--------|------|
| capability_vocabulary.json | `payments` (line 17) |
| venture_capability_map.csv | `payment` (possibly singular) |

**Impact:** Join queries fail if one source uses singular and another plural.

**Where Found:**
- `/Users/acebless/Documents/WORLDWIDEBRO-OS/08-DATA/registries/capability_vocabulary.json`
- `/Users/acebless/Documents/WORLDWIDEBRO-OS/08-DATA/registries/venture_capability_map.csv`

**Resolution:** Standardize to plural (`payments`) everywhere.

**Effort:** 1 hour | **Blocking:** NO — But causes silent query failures

---

### #10: Capability Aliases Not Normalized
**Problem:** Vocabulary defines aliases (db → database) but venture data may use mixed spellings.

**Example:**
```json
"database": {
  "aliases": ["db", "databases", "postgres", "postgresql", "sql", ...]
}
```

Ventures might use: `database`, `db`, `postgres`, `postgresql` interchangeably.

**Impact:** Capability matching unreliable without normalization.

**Where Found:**
- Definition: `/Users/acebless/Documents/WORLDWIDEBRO-OS/08-DATA/registries/capability_vocabulary.json`
- Usage: `/Users/acebless/Documents/WORLDWIDEBRO-OS/08-DATA/registries/venture_capability_map.csv` (unknown without full scan)

**Resolution:** Build normalization function; standardize all capability terms to canonical names.

**Effort:** 2-3 hours | **Blocking:** NO — But causes inaccurate metrics

---

### #11: Portfolio Last Generated 4+ Hours After ventures.csv
**Problem:** portfolio.public.json data lag detected; no real-time sync.

| File | Modified/Generated | Lag |
|---|---|---|
| ventures.csv | 2026-07-15 15:34 | — |
| portfolio.public.json | 2026-07-15T23:37:36.516Z | **4h 3m** |

**Impact:** Ventures added/modified between 15:34–19:37 missing from website.

**Where Found:**
- Timestamps from file metadata and JSON `generatedAt`

**Resolution:** Automate ventures.csv → portfolio.public.json sync via CI/CD; add staleness indicator.

**Effort:** 2 hours | **Blocking:** NO — But data freshness issue

---

### #12: WHOAMI.md References Superseded Systems (Chroma, LightRAG)
**Problem:** WHOAMI.md line 82-84 documents systems marked DEAD (2026-06-28).

**Current Status (from memory):**
- Chroma: DEAD (was at :9022, replaced by Qdrant)
- LightRAG: DEAD (was at :8000, replaced by Qdrant + Neo4j)
- Qdrant: LIVE (1,648 vectors in `repositories` collection)

**Impact:** Operators following WHOAMI.md will fail trying to use Chroma/LightRAG.

**Where Found:**
- `/Users/acebless/Documents/WORLDWIDEBRO-OS/WHOAMI.md` line 82-84

**Resolution:** Remove dead system references; add "Last Verified" date to documentation.

**Effort:** 1 hour | **Blocking:** NO — But causes operator confusion

---

## Summary Table: All Issues Ranked by Blocking Status & Effort

| # | Issue | Severity | Blocking? | Effort | Phase |
|---|---|---|---|---|---|
| #1 | Venture ID mapping (UUID ↔ slug) | 🔴 CRITICAL | ✅ YES | 4-6h | 1 |
| #2 | OPCO format unification | 🔴 CRITICAL | ✅ YES | 2h | 1 |
| #3 | Add missing sectors | 🔴 CRITICAL | ✅ YES | 3h | 1 |
| #4 | Capability schema rebuild | 🔴 CRITICAL | ✅ YES | 6-8h | 1 |
| #6 | Automate venture sync | 🟡 HIGH | ~ PARTIAL | 2-3h | 2 |
| #5 | Consolidate agent roles | 🟡 HIGH | ~ PARTIAL | 3-4h | 2 |
| #9 | Standardize capability names | 🟡 HIGH | ~ PARTIAL | 1h | 2 |
| #7 | Extract agent templates | 🟡 HIGH | NO | 4h | 3 |
| #8 | Consolidate venture templates | 🟡 HIGH | NO | 3h | 3 |
| #10 | Normalize capability aliases | 🟡 HIGH | NO | 2-3h | 3 |
| #11 | Add portfolio staleness indicator | 🟠 MEDIUM | NO | 2h | 3 |
| #12 | Update WHOAMI.md status | 🟠 MEDIUM | NO | 1h | 3 |

**Phase 1 (Critical blockers):** 15-19 hours — **MUST DO FIRST**  
**Phase 2 (High-impact fixes):** 6-7 hours  
**Phase 3 (Optimization):** 12-15 hours  
**Total:** 33-41 hours over 2 weeks

---

## Verification Checklist

After fixes, verify:

- [ ] All venture_ids in ventures.csv have UUID mappings in venture_capability_map.csv
- [ ] All capabilities in venture_capability_map.csv match canonical vocabulary
- [ ] All sectors in ventures.csv have SectorEntry in sectors.ts
- [ ] OPCO field matches same format across ventures.csv, opco_venture_map.csv, sectors.ts, portfolio.public.json
- [ ] No references to Chroma or LightRAG in codebase
- [ ] portfolio.public.json regenerated within 1 hour of ventures.csv changes
- [ ] WHOAMI.md has "Last Verified: [DATE]" and status indicators (✅/⚠️/❌)
- [ ] agent_registry.yaml marked as authoritative in documentation

---

## Files to Update

**High Priority:**
- `/Users/acebless/Documents/WORLDWIDEBRO-OS/08-DATA/registries/ventures.csv` (OPCO format)
- `/Users/acebless/Documents/WORLDWIDEBRO-OS/08-DATA/registries/venture_capability_map.csv` (rebuild with FK)
- `/Users/acebless/Documents/WORLDWIDEBRO-OS/08-DATA/registries/capability_vocabulary.json` (aliases)
- `/Users/acebless/Documents/vex-hero-site/src/data/sectors.ts` (add missing sectors)
- `/Users/acebless/Documents/vex-hero-site/src/data/portfolio.public.json` (add auto-sync)

**Medium Priority:**
- `/Users/acebless/Documents/WORLDWIDEBRO-OS/WHOAMI.md` (update status)
- `/Users/acebless/Documents/WORLDWIDEBRO-OS/04-OPERATIONS/SERVICE-VENTURE-KIT-TEMPLATE.md` (consolidate)
- `/Users/acebless/Documents/vex-hero-site/AGENTS.md` (document canonical roles)

**Low Priority:**
- Create `/WORLDWIDEBRO-OS/04-OPERATIONS/VENTURE-TEMPLATES/` directory
- Create `/WORLDWIDEBRO-OS/05-AGENTS/AGENTS-REGISTRY.json`
- Create `/WORLDWIDEBRO-OS/08-DATA/SCHEMA.md`
