# 23-VENTURES — Index

**Domain:** Active ventures, deployments, operations  
**Authority:** CP-021 (Revenue Control Plane)  
**Owner:** [[WHO-I-AM-ANTWUAN-JOHNS|Founder]] / Venture Leads  
**Related:** [[01-IDENTITY]], [[22-EXECUTION]], [[24-FINANCE]], [[25-SALES]]

---

## Purpose

The ventures layer holds the **operational state and deployments of all active and building ventures**. This is where ventures move from conceptual (in registries) to executed (with code, customers, revenue).

---

## Core Registries (Single Source of Truth)

| Registry | Records | Purpose | Status |
|----------|---------|---------|--------|
| **VENTURE-REGISTRY.yaml** | 6 active + 783 staged | High-priority ventures + bulk reference | ✅ LIVE |
| **ALL_789_VENTURES_36_SECTOR_ALIGNMENT_DEDUPED.csv** | 655 unique | Authoritative venture inventory | ✅ VERIFIED |
| **SECTOR-VENTURE-MANIFEST.csv** | 789 rows | Multidimensional classification (business domain + customer vertical + tech domain) | ✅ IN PROGRESS |
| **Supabase ventures table** | 580 real | Operational ventures (live ground truth) | ✅ VERIFIED |

---

## Files in This Domain

| File | Purpose | Status |
|------|---------|--------|
| **Worldwidebro-Vex/** | Public portfolio showcase | ✅ DEPLOYED |
| **OPS-001/** | Staff augmentation (active revenue) | ✅ ACTIVE |
| **LT-005/** | Medical courier (active revenue) | ✅ ACTIVE |
| **LT-011/** | Dispatch software (assessment) | ✅ BUILD-READY |
| **CALLCENTER/** | Call center routing (deployment-ready) | ✅ ACTIVE |
| **CON-001/** | Construction marketing (demo) | 🟡 DEMO |
| **RE-001/** | Real estate fund (pitch) | 🟡 PROTOTYPE |
| **[789 venture folders]** | Complete venture universe | ⏳ STAGED |

---

## Venture Classifications

### Revenue-Ready (Week 1 Execution)

| Venture | Sector | Stage | Monthly Revenue | Status |
|---------|--------|-------|-----------------|--------|
| **OPS-001** | SEC-014 (HR/Staffing) | SELLING | $2.5K+ | ✅ ACTIVE |
| **LT-005** | SEC-017 (Logistics) + SEC-012 (Healthcare) | SELLING | $1.5K-$2K+ | ✅ ACTIVE |
| **CALLCENTER** | SEC-024 (Technology) | DEPLOYING | $50-$200/call | ✅ DEPLOYING |

### Build-Ready (1-2 Days)

| Venture | Effort | Status |
|---------|--------|--------|
| **CON-001** | 6 hours API build | 🟡 DEMO |
| **LT-011** | 1 hour assessment | 🟡 ASSESSMENT |

### Prototype (Longer Timeline)

| Venture | Effort | Status |
|---------|--------|--------|
| **RE-001** | 25 hours deal engine | 🟡 PITCH |

---

## Reconciliation Status (Sep 23-30, 2026)

### Ground Truth Verification

**Completed:**
- ✅ Venture deduplication (789 → 655 unique)
- ✅ Sector misclassification audit (177 HIGH-CONFIDENCE issues found)
- ✅ Root cause analysis (registry pre-dedup vs CSV post-dedup)

**In Progress:**
- ⏳ Phase 1: Supabase schema mapping (Sep 26)
- ⏳ Phase 2: Classification audit (Sep 27-28)
- ⏳ Phase 3: Multidimensional lookup (Sep 29)
- ⏳ Phase 4: Supabase population (Sep 30-Oct 1)
- ⏳ Phase 5: Verification (Oct 1-2)

### Critical Findings

- **3 Catastrophic Misclassifications:** LT-005/LT-011, SEC-024 count error, SEC-012 unmapped
- **4 Pending Founder Decisions:** Venture count reality, sector model direction, bases table location, entities registry verification
- **209 "Missing" Ventures Gap:** 789 registry vs 580 Supabase (phantom or real?)

See: [[RECONCILIATION-ANALYSIS-WORKFLOW-2026-09-23|_REGISTRIES/CANONICAL/RECONCILIATION-ANALYSIS-WORKFLOW-2026-09-23.md]]

---

## Key Documents

### Active Ventures (Revenue Loop)
- [[OPS-001/README|OPS-001 Staffing Venture]] — Cold call campaign + placement execution
- [[LT-005/README|LT-005 Medical Courier]] — B2B managed service + dual 11-stage funnels
- [[CALLCENTER/README|CALLCENTER Dispatch]] — Real-time call routing + quality scoring

### Venture Architecture
- [[INSTITUTIONAL-VENTURE-ARCHITECTURE|../../_REGISTRIES/CANONICAL/INSTITUTIONAL-VENTURE-ARCHITECTURE.md]] — Master map: 789 ventures → OpCos → repos → OSS
- [[WORLDWIDEBRO-HOLDINGS-MASTER-OPERATING-MANUAL|../../WORLDWIDEBRO-HOLDINGS-MASTER-OPERATING-MANUAL.md]] — 789-venture holding company framework
- [[FAMILY_OFFICE_ECOSYSTEM_ALIGNMENT_MASTER|../../_REGISTRIES/CANONICAL/FAMILY_OFFICE_ECOSYSTEM_ALIGNMENT_MASTER.md]] — 150-entity legal structure

### Registries (Source of Truth)
- [[SECTOR-REGISTRY|../../_REGISTRIES/CANONICAL/SECTOR-REGISTRY.yaml]] — 36 sectors + OpCo mappings
- [[VENTURE-REGISTRY|../../_REGISTRIES/CANONICAL/VENTURE-REGISTRY.yaml]] — 6 priority ventures (see CSV for bulk)
- [[OPCO-REGISTRY|../../_REGISTRIES/CANONICAL/OPCO-REGISTRY.yaml]] — 35 operating companies

---

## Related Domains

**Venture Execution Chain:**
- [[23-VENTURES]] (venture operations)
- → [[22-EXECUTION]] (work tracking)
- → [[24-FINANCE]] (financial results)
- → [[25-SALES]] (customer acquisition)
- → [[27-CUSTOMERS]] (customer success)

**Capital Structure Chain:**
- [[23-VENTURES]] (venture businesses)
- → [[35-ASSETS]] (asset ownership)
- → [[00-CONSTITUTION]] (family office governance)
- → [[01-IDENTITY]] (company structure)

**Classification Chain:**
- [[23-VENTURES]] (venture reality)
- → [[07-ONTOLOGY]] (sector/Base taxonomy)
- → [[08-KNOWLEDGE-GRAPH]] (venture relationships)

---

## Navigation

← [[DOMAIN-MAP|../../_REGISTRIES/CANONICAL/DOMAIN-MAP.md]] | [[INDEX|../../_REGISTRIES/CANONICAL/INDEX.md]] →

