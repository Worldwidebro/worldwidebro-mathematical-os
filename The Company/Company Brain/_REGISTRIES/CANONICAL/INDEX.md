# Reconciliation Wiki — Index

**Updated:** 2026-09-23  
**Scope:** Data integrity audit for venture classification  
**Purpose:** Single source of truth for sector, OpCo, Base, and venture mappings  
**Navigation:** [[STARTHERE]] | [[DOMAIN-MAP|DOMAIN-MAP.md]] | [[LOG|LOG.md]] | [[INDEX|INDEX.md]]

---

## Core Registries (Authoritative)

| Page | Records | Updated | Purpose |
|------|---------|---------|---------|
| [[SECTOR-REGISTRY|SECTOR-REGISTRY.yaml]] | 36 sectors | Sep 24 | All sectors with definitions, OpCo mappings, status |
| [[OPCO-REGISTRY|OPCO-REGISTRY.yaml]] | 35 OpCos | Sep 24 | Operating companies, sector links, status |
| [[BASE-REGISTRY|BASE-REGISTRY.yaml]] | 36 bases | Sep 24 | Bases with 11-point gate framework, instantiation status |
| [[VENTURE-REGISTRY|VENTURE-REGISTRY.yaml]] | 6 active + 783 staged | Sep 24 | High-priority ventures (expanded metadata); see CSV for bulk |
| [[ALL_789_VENTURES_36_SECTOR_ALIGNMENT_DEDUPED|ALL_789_VENTURES_36_SECTOR_ALIGNMENT_DEDUPED.csv]] | 655 unique ventures | Sep 23 | Authoritative venture inventory (post-dedup, business-domain classified) |

---

## Audit & Analysis Documents

### Phase Completion Status

| Phase | Document | Status | Completion Date |
|-------|----------|--------|-----------------|
| **Option 4: Root Cause** | [[AUDIT-PHASE2-FINDINGS-2026-09-25]] | ✅ COMPLETE | Sep 25 |
| **Option 3: Classification** | [[sector_classification_model.py]] | ✅ COMPLETE | Sep 23 |
| **Option 2: Workflow Design** | [[RECONCILIATION-ANALYSIS-WORKFLOW-2026-09-23]] | ✅ COMPLETE | Sep 23 |
| **Option 1: Investigation** | (Pending) | ⏳ QUEUED | Sep 24-26 |

### Ground Truth Discovery

| Document | Finding | Status |
|----------|---------|--------|
| [[SUPABASE-RECONCILIATION-PLAN-2026-09-25]] | 25 Supabase categories ≠ 36 SEC codes; 580 real ventures ≠ 789 claimed | ✅ ANALYZED |
| [[AUDIT-PHASE2-FINDINGS-2026-09-25]] | 3 critical misclassifications (LT-005/LT-011, SEC-024, SEC-012, SEC-020) | ✅ FLAGGED |
| [[REGISTRY-README-SEP24|REGISTRY-README-SEP24.md]] | Sep 24 registry freeze; Phase 1-4 plan | ✅ REFERENCE |

---

## Execution Plans

### 5-Phase Reconciliation (Sep 26 - Oct 2)

| Phase | Dates | Document | Status |
|-------|-------|----------|--------|
| **Phase 1: Data Mapping** | Sep 26 | [[RECONCILIATION-ANALYSIS-WORKFLOW-2026-09-23#phase-1-data-mapping-sep-26]] | ⏳ QUEUED |
| **Phase 2: Classification Audit** | Sep 27-28 | [[RECONCILIATION-ANALYSIS-WORKFLOW-2026-09-23#phase-2-classification-audit-sep-27-28]] | ⏳ QUEUED |
| **Phase 3: Multidimensional** | Sep 29 | [[RECONCILIATION-ANALYSIS-WORKFLOW-2026-09-23#phase-3-multidimensional-classification-sep-29]] | ⏳ QUEUED |
| **Phase 4: Supabase Expansion** | Sep 30-Oct 1 | [[RECONCILIATION-ANALYSIS-WORKFLOW-2026-09-23#phase-4-supabase-schema-expansion-sep-30-oct-1]] | ⏳ QUEUED |
| **Phase 5: Verification** | Oct 1-2 | [[RECONCILIATION-ANALYSIS-WORKFLOW-2026-09-23#phase-5-verification--audit-oct-1-2]] | ⏳ QUEUED |

---

## Key Findings & Decisions

### Critical Disputes (Pending Founder Decision)

| Dispute | Question | Status | Decision |
|---------|----------|--------|----------|
| **Venture Count Reality** | Are 209 "missing" ventures phantom or real? (789 vs 580) | 🔴 OPEN | Founder |
| **Sector Model Direction** | Expand Supabase to 36 or stay at 25? | 🔴 OPEN | Founder |
| **Bases Table Location** | Create in Supabase or keep in YAML + sync? | 🔴 OPEN | Founder |
| **Entities Registry Verify** | Is legal_entities the right table? Schema correct? | 🔴 OPEN | Founder |

### Root Causes (Verified)

| Issue | Root Cause | Evidence |
|-------|-----------|----------|
| **82-90% venture count error** | Registry built from pre-dedup (789) while CSV shows post-dedup (655) | DEDUPLICATION_AUDIT_2026-09-23.md shows 134 duplicates removed |
| **177 sector misclassifications** | Ventures classified by tech-domain (AI/ML) not business-domain (Finance) | sector_classification_model.py flagged 177 HIGH-CONFIDENCE cases |
| **LT-005/LT-011 dispute** | CSV shows SEC-001, registry claims SEC-017; Supabase unknown | AUDIT-PHASE2-FINDINGS identifies as CRITICAL |

---

## Reference Materials

### Data Models & Schemas

- [[BASES-CANONICAL-DEFINITION|_ONTOLOGY/BASES-CANONICAL-DEFINITION.md]] — What are Bases? (35 knowledge/operating domains)
- [[VENTURE-REALITY-AUDIT]] — Operating reality calculation (existence, repo, site, product, revenue, etc.)
- [[SECTOR-VENTURE-MANIFEST|_REGISTRIES/CANONICAL/SECTOR-VENTURE-MANIFEST.csv]] — Multidimensional classification (primary + secondary sectors, business domain, customer vertical, tech domain)

### Integration Points

- [[VENTURE-AUDIT-FRAMEWORK|20-DECISIONS/VENTURE-AUDIT-FRAMEWORK.md]] — 12-layer audit methodology
- [[PHASE-2-PHASE-2A-INTEGRATION-MAP|20-DECISIONS/PHASE-2-PHASE-2A-INTEGRATION-MAP.md]] — Phase 2 graph → Phase 2a agents
- [[graph_ingestion_pipeline.py|_PIPELINES/graph_ingestion_pipeline.py]] — Neo4j merge functions (merge_sector, merge_venture, etc.)
- [[VentureOrchestrator|_INFRASTRUCTURE/agents/venture_orchestrator.py]] — Venture operations orchestration

---

## Timeline & History

See [[LOG|LOG.md]] for chronological record of:
- Data discoveries (Supabase schema, venture counts, etc.)
- Analysis completion (Options 4, 3, 2)
- Execution milestones (Phases 1-5)
- Gate evaluations (Base readiness)

---

## All 71 Domains (Complete Navigation)

See [[DOMAIN-MAP|DOMAIN-MAP.md]] for full descriptions. Domain INDEXes (example template):

### Layer 1: Governance (00-07)
[[00-CONSTITUTION/INDEX|00]] | [[01-IDENTITY/INDEX|01]] | [[02-SOURCES/INDEX|02]] | [[03-INGESTION/INDEX|03]] | [[04-DATA/INDEX|04]] | [[05-METADATA/INDEX|05]] | [[06-ENTITY-RESOLUTION/INDEX|06]] | [[07-ONTOLOGY/INDEX|07]]

### Layer 2: Intelligence (08-12)
[[08-KNOWLEDGE-GRAPH/INDEX|08]] | [[09-KNOWLEDGE/INDEX|09]] | [[10-MEMORY/INDEX|10]] | [[11-INDEXING/INDEX|11]] | [[12-CONTEXT/INDEX|12]]

### Layer 3: Capabilities (13-19)
[[13-REPOSITORIES/INDEX|13]] | [[14-CAPABILITIES/INDEX|14]] | [[15-SKILLS/INDEX|15]] | [[16-AGENTS/INDEX|16]] | [[17-MODELS/INDEX|17]] | [[18-TOOLS/INDEX|18]] | [[19-ORCHESTRATION/INDEX|19]]

### Layer 4: Operations (20-28)
[[20-DECISIONS/INDEX|20]] | [[21-POLICY/INDEX|21]] | [[22-EXECUTION/INDEX|22]] | [[22-VENTURES/INDEX|22v]] | [[23-VENTURES/INDEX|23]] | [[24-FINANCE/INDEX|24]] | [[25-SALES/INDEX|25]] | [[26-MARKETING/INDEX|26]] | [[27-CUSTOMERS/INDEX|27]] | [[28-PRODUCT/INDEX|28]]

### Layer 5: Business Ops (29-36)
[[29-OPERATIONS/INDEX|29]] | [[30-HR/INDEX|30]] | [[31-LEGAL/INDEX|31]] | [[32-SECURITY/INDEX|32]] | [[33-COMPLIANCE/INDEX|33]] | [[34-RISK/INDEX|34]] | [[35-ASSETS/INDEX|35]] | [[36-PARTNERS/INDEX|36]]

### Layer 6: Research (37-42)
[[37-RESEARCH/INDEX|37]] | [[38-OPPORTUNITIES/INDEX|38]] | [[39-EXPERIMENTS/INDEX|39]] | [[40-METRICS/INDEX|40]] | [[41-OBSERVABILITY/INDEX|41]] | [[42-EVALUATION/INDEX|42]]

### Layer 7: Learning (43-50)
[[43-OUTCOMES/INDEX|43]] | [[44-LEARNING/INDEX|44]] | [[45-EVOLUTION/INDEX|45]] | [[46-GOVERNANCE/INDEX|46]] | [[47-DOCUMENTS/INDEX|47]] | [[48-AUTOMATION/INDEX|48]] | [[49-SYSTEM/INDEX|49]] | [[50-MASTER-CONTROL/INDEX|50]]

### Layer 8: Specialized (51-67)
[[51-CONSTRUCTION/INDEX|51]] | [[52-PEOPLE/INDEX|52]] | [[53-TEAMS/INDEX|53]] | [[54-FINANCIAL/INDEX|54]] | [[55-LOOP-ENGINEERING/INDEX|55]] | [[56-ENGINEERING/INDEX|56]] | [[57-CODE-INTELLIGENCE/INDEX|57]] | [[58-LOGISTICS/INDEX|58]] | [[59-MCP/INDEX|59]] | [[60-APIS/INDEX|60]] | [[61-KNOWLEDGE-SOURCES/INDEX|61]] | [[62-TECHNOLOGY/INDEX|62]] | [[63-CHANGE-MANAGEMENT/INDEX|63]] | [[64-RELATIONSHIPS/INDEX|64]] | [[65-SYNERGIES/INDEX|65]] | [[66-OPPORTUNITIES-ALT/INDEX|66]] | [[67-EVOLUTION-ALT/INDEX|67]]

### Layer 9: Execution (90)
[[90-EXECUTION/INDEX|90]]

---

## Questions & Next Steps

**For Founder (Sep 25-26):**
1. Confirm venture count reality (209 gap resolution)
2. Select sector model direction (25 vs 36)
3. Decide bases table location
4. Verify entities registry schema

**For Phase 1 Execution (Sep 26):**
1. Query Supabase schema (sectors, OpCos, ventures, legal_entities)
2. Map 25 Supabase categories → 36 SEC-XXX codes
3. Verify data discrepancies (missing ventures, boundary overlaps)

**For Ongoing:**
- Update this INDEX as new pages are created
- Check [[LOG|LOG.md]] for latest activity
- Link related pages with [[wiki-links]]
- See [[DOMAIN-MAP|DOMAIN-MAP.md]] for full domain descriptions

---

**Wiki Maintainers:** Claude Haiku 4.5  
**Last Audit:** 2026-09-23  
**Architecture:** STARTHERE → INDEX (master) → DOMAIN-MAP (all 71) → Domain INDEXes (one per domain) → Files

---

## Control Base Reference

This document is mapped to [[B005|Control Base]] in the Company Brain.

**Wiki Link:** [[CBP_REGISTRY|_REGISTRIES/CANONICAL/CBP_REGISTRY.yaml#B005]]