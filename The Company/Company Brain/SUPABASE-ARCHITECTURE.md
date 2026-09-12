[[STARTHERE]] | [[REALITY]] | [[13_ENGINEERING/INFRASTRUCTURE/06_DATA/DATA|Supabase Architecture]] | [[INDEX]]

# Supabase Architecture — Venture Data Projects

**Last Updated:** 2026-09-09  
**Authority:** CP-027 (Infrastructure) + CP-033 (Execution)

---

## CURRENT STATE: Per-Venture Isolation

Each venture currently has its **own isolated Supabase project**:

| Venture | Project ID | Status | Purpose |
|---------|-----------|--------|---------|
| **CON-001** (Ace Construction) | `rhlkjelglvurowdalrgh` | ✅ LIVE | Construction marketplace |
| **LT-005** (HealthRoute Courier) | `aipehhzlsmfxxzwceppd` | ✅ LIVE | Medical delivery ops |
| **RE-001** (WorldwideBro RE) | `ocygjaiokomfvoaozvgv` | ✅ LIVE | Real estate deals |
| **OPS-001** (CareerOps Staffing) | `cyhzilqldouzgynacqpe` | ✅ LIVE | Staffing operations |

---

## THE QUESTION: Can We Consolidate to ONE Project?

**YES** — `cyhzilqldouzgynacqpe` (VEX project) can handle ALL ventures if we:

1. **Create multi-venture schema** with `venture_id` foreign key
2. **Enable Row-Level Security (RLS)** to prevent data leakage
3. **Wire data sync** from Company Brain → consolidated Supabase
4. **Update VEX** to query single project instead of 4

---

## RECOMMENDATION: Consolidate to `cyhzilqldouzgynacqpe`

**Why:**
- VEX needs unified dashboard (impossible with isolated projects)
- Single API key, simpler config
- RLS prevents unauthorized access
- Easier reporting and analytics

**Current Issue:**
- I mistakenly changed VEX to point to `rhlkjelglvurowdalrgh` (CON-001 only)
- Need to revert to `cyhzilqldouzgynacqpe` after migration

---

## DECISION NEEDED

**Should we:**
1. **Consolidate all 4 ventures** → `cyhzilqldouzgynacqpe` (RECOMMENDED)
2. **Keep isolated** → refactor VEX to query 4 projects
3. **Hybrid** → consolidate 3, keep OPS-001 separate

**Your call?**
