# Canonical Registries — Sep 24 Freeze

**Created:** 2026-09-24  
**Authority:** Ontology layer (Phase 1: Registry Freeze)  
**Status:** PHASE 1 COMPLETE ✅

---

## What's Locked

Five canonical registries created as single source of truth:

| Registry | Records | Status | Purpose |
|----------|---------|--------|---------|
| **SECTOR-REGISTRY.yaml** | 37 sectors | LOCKED | Sector definitions + status (10 active, 25 staging, 1 reserved, 1 anomaly) |
| **OPCO-REGISTRY.yaml** | 35 OpCos | LOCKED | Operating company definitions + sector mappings |
| **BASE-REGISTRY.yaml** | 36 bases | GATED | Base instantiation status + 11-point gate framework |
| **VENTURE-REGISTRY.yaml** | 789 ventures | SKELETON | High-priority ventures (6 active) with expanded metadata; see CSV for bulk |
| **SECTOR-VENTURE-MANIFEST.csv** | 6 → 789 | IN_PROGRESS | Multidimensional venture classification (primary/secondary sectors, business model, customer vertical, technology domain, capability) |

---

## Phase 1: Registry Freeze (Sep 24) ✅ COMPLETE

### Deliverables Created
1. ✅ **SECTOR-REGISTRY.yaml** — All 37 sectors defined with status, OpCo mapping, industries, verification status
2. ✅ **OPCO-REGISTRY.yaml** — All 35 OpCos with sector mappings + collision resolution notes
3. ✅ **BASE-REGISTRY.yaml** — All 36 bases with 11-point gate framework + evaluation checkpoints
4. ✅ **VENTURE-REGISTRY.yaml** — 6 high-priority ventures (expanded) + reference to CSV for bulk
5. ✅ **SECTOR-VENTURE-MANIFEST.csv** — Started with 6 priority ventures; expansion in Phase 2
6. ✅ **Git commit fde5614d** — All registries committed with full attribution

### Critical Issues Identified & Flagged
1. **SEC-037 / OPCO-030 Collision** — SEC-037 (Capital & Quantitative Trading, 3 ventures) currently mapped to OPCO-030 (Fintech & Payments). Status: PENDING OpCo resolution.
   - Options: Create OPCO-037 (recommended) OR reclassify SEC-037
   - Decision gate: 2026-10-01
   
2. **SEC-020 Anomaly** — Only 1 venture (RE-001). Status: VERIFIED but flagged for portfolio audit.
   - Action: Audit entire 789-venture portfolio for missed/misclassified real-estate ventures
   - Do NOT invent ventures; only reclassify existing ones

3. **SEC-024 Concentration Risk** — 243 ventures (30.8% of portfolio) in Technology & Software
   - Boundary overlap risk with SEC-028 (B2B Enterprise Software), SEC-032 (AI/ML), SEC-033 (Cybersecurity)
   - Action: Audit venture classification boundaries

---

## Phase 2: Classification Audit & Reality Check (Sep 25–28)

**Owner:** Claude Haiku 4.5  
**Duration:** 4 days (Sep 25–28)  
**Deliverables:**

### Phase 2a: Venture Classification Audit (Sep 25–26, 8 hours)

Verify venture classification for 6 key sectors:

| Sector | Venture Count | Audit Task | Risk |
|--------|---------------|-----------|------|
| **SEC-017** (Logistics) | 30 | Verify LT-005, LT-011 correctly mapped? Any construction/supply-chain ventures misclassified? | LT-005 secondary→SEC-012? |
| **SEC-020** (Real Estate) | 1 | Audit entire portfolio for property-related ventures (acquisition, management, finance, brokerage) | Missing ventures? |
| **SEC-012** (Healthcare) | ? | Which ventures belong to healthcare? LT-005 (customer vertical)? Biotech ventures? | Unmapped |
| **SEC-024** (Technology) | 243 | Is 30% concentration legitimate? Boundary overlap with SEC-028, SEC-032, SEC-033? | Over-concentration |
| **SEC-029** (Marketplace) | 120 | Multi-sided platforms only? Or SaaS ventures misclassified here? | Boundary unclear |
| **SEC-014** (HR/Staffing) | 117 | HR/Staffing only? Or recruitment tech + payroll tech (should be SEC-028)? | Boundary unclear |

**Output:** 6 audit reports. Each reports: verified count, moved ventures, flagged for reclassification, notes.

### Phase 2b: Reality Audit (Sep 27–28, 10 hours)

Calculate operating reality for all 789 ventures:

Create `VENTURE-REALITY-AUDIT.csv`:

```csv
venture_id,venture_name,exists,repo_exists,site_exists,product_exists,customer_exists,revenue_generating,owner_identified,workflow_mapped,agent_assigned,evidence_exists,reality_score,status,notes
```

**Reality Score Calculation:**
```
Reality Score = (exists + repo + site + product + customer + revenue + owner + workflow + agent + evidence) / 10 × 100%
```

**Gate:** Only ventures with **80%+ reality score** eligible for active Base assignment.

### Phase 2c: Multidimensional Classification (Sep 28, 6 hours)

Populate `SECTOR-VENTURE-MANIFEST.csv` with all 789 ventures:

**Columns:**
```
venture_id, venture_name,
primary_sector, secondary_sectors,
business_model, customer_vertical, technology_domain, capability,
opco_id, base_id,
mapping_status, reality_score, status, verification_status,
notes
```

**Example:**
```
LT-005,HealthRoute,SEC-017,SEC-012,B2B Managed Service,Healthcare Logistics,Dispatch Software,Medical courier dispatch + Route optimization,OPCO-017,BASE-017,VERIFIED,100%,ACTIVE,VERIFIED,Active revenue loop
```

---

## Phase 3: Base Creation Gate (Sep 29–30, 4 hours)

For each sector, evaluate 11-point gate:

```yaml
BASE-XXX:
  gates:
    gate_1_sector_defined: PASS
    gate_2_sector_unique: PASS
    gate_3_venture_manifest: IN_PROGRESS
    gate_4_ventures_verified: IN_PROGRESS
    gate_5_opco_mapping: PASS
    gate_6_ownership_defined: PENDING
    gate_7_base_purpose: PENDING
    gate_8_whoami_file: QUEUED
    gate_9_agent_assignment: QUEUED
    gate_10_skills_mapped: PENDING
    gate_11_workflows_mapped: PENDING
    # (+ 2 more gates in full framework)
  gate_summary:
    total: 11
    passed: 3
    pending: 6
    ready_for_activation: false
```

**Result:** List of bases READY for activation (Oct 1–6) vs. PENDING (missing gate criteria).

---

## Phase 4: Base WHOAMI Layer (Oct 1–6)

**ONLY AFTER gates pass:**
- Create BASE-*/WHOAMI.md files with full wiki links
- Connect upward (OPCO, governance, Company Brain)
- Connect downward (ventures, agents, skills, workflows, loops, revenue, evidence)

---

## Registry Maintenance Cadence

| Task | Frequency | Owner | Status |
|------|-----------|-------|--------|
| Add new ventures | Daily | Supabase sync | Ongoing |
| Reality audit | Weekly | Claude Haiku | Starting Sep 27 |
| Sector boundary audit | Monthly | Founder review | Sep 25-26 |
| Base gate evaluation | Continuous | Gate automation | Sep 24-30 |
| Registry integrity check | Quarterly | Audit system | Next: Oct 15 |

---

## Key Wiki Links (Navigation)

- [[SECTOR-REGISTRY|Registry of all 37 sectors]]
- [[OPCO-REGISTRY|Operating company definitions]]
- [[BASE-REGISTRY|Base instantiation status + gates]]
- [[VENTURE-REGISTRY|High-priority ventures (6 active + 783 staged)]]
- [[SECTOR-VENTURE-MANIFEST|Multidimensional venture classification]]
- [[ALL_789_VENTURES_36_SECTOR_ALIGNMENT_DEDUPED|Raw venture data (CSV source)]]
- [[ANTIGRAVITY|45 operating rules (Rule 2: verification-first classification)]]
- [[REALITY|Verified truth ledger (weekly audits)]]

---

## Next Steps

**Sep 25 at 0600 UTC:**
- Audit 6 key sectors (SEC-017, SEC-020, SEC-012, SEC-024, SEC-029, SEC-014)
- Document venture moves + reclassifications
- Flag boundary ambiguities

**Sep 27 at 0600 UTC:**
- Run reality audit on all 789 ventures
- Populate reality scores
- Identify 80%+ candidates for active Base assignment

**Sep 30 at 0600 UTC:**
- Evaluate 11-point gates for all 36 bases
- Publish READY vs. PENDING list
- Schedule Oct 1-6 Base WHOAMI creation

**Oct 1 at 0600 UTC:**
- Begin Base WHOAMI.md files (6 activated bases first)
- Wire wiki links for organizational graph
- Activate agent dispatch routers

---

## Authority & Approval

**Created by:** Claude Haiku 4.5  
**Authority:** Ontology layer (Sep 24 registry freeze)  
**Approved by:** [[WHO-I-AM-ANTWUAN-JOHNS|Founder]]  
**Commit:** fde5614d  
**Last updated:** 2026-09-24  

---

## Questions & Escalation

- **SEC-037 / OPCO-030 collision:** Escalate to founder by 2026-10-01
- **Real Estate (SEC-020) anomaly:** Escalate audit findings to [[PERSON-002-CFO|CFO]] by 2026-10-01
- **Technology concentration (SEC-024, 30.8%):** Flag to portfolio review committee by 2026-10-01

---

**Status: Phase 1 COMPLETE. Phase 2 begins Sep 25.**

---

## Control Base Reference

This document is mapped to [[B005|Control Base]] in the Company Brain.

**Wiki Link:** [[CBP_REGISTRY|_REGISTRIES/CANONICAL/CBP_REGISTRY.yaml#B005]]