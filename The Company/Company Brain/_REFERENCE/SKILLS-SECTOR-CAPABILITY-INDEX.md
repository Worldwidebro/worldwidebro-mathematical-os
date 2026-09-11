---
id: DOC-SKILLS-INDEX-001
title: Skills Index — Sector, Capability & Venture Connections
description: "2,093 Claude Code skills mapped to sectors, capabilities, and ventures with wiki links"
aliases: ["SKILLS-INDEX", "Skills-Index", "SKILLS-SECTOR-INDEX"]
tags: [skills, taxonomy, sector-mapping, capability-mapping, wiki-links]
status: ACTIVE
updated: 2026-09-10
---

[[STARTHERE]] | [[SECTOR_INDEX]] | [[CAPABILITY-INDEX]] | [[SECTOR-CAPABILITY-CONNECTIONS]] | [[INDEX]]

# Skills Index: Sector × Capability × Venture Connections

**Purpose:** Complete mapping of all 2,093 Claude Code skills to business sectors, capabilities, ventures, and control planes.

**Master Files:**
- [[_REFERENCE/SKILLS-PHASE-ROADMAP.md|Skills by Phase]] — 8 project lifecycle phases
- [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md|Complete Skill Catalog]] — All 2,093 with variants

**Status:** Framework active | **Indexed Skills:** 500+ (24%) | **Next:** Complete mapping by 2026-09-30

---

## GSD Framework Skills (71 Total) — Maps to All Sectors

**Master List:** `/gsd-*` namespace

[[STARTHERE|Master orientation]] uses these skills across all execution:

### **Project Initiation** → SEC-024 (Technology), SEC-008 (Finance)
- [[_REFERENCE/SKILLS-PHASE-ROADMAP.md#gsd-new-project|/gsd-new-project]] — Used by [[00-CONSTITUTION/opcos|All OpCos]]
  - **Sectors:** All 35
  - **Capability:** [[CAP-001|CAP-001 (API)]], [[CAP-004|CAP-004 (Data)]]
  - **Ventures:** [[VEX|VEX]], [[23-VENTURES|All VENTURES]]
  - **Control Plane:** [[_REGISTRIES/control-planes-by-sector.yaml#CP-033|CP-033]] (Governance)

- [[_REFERENCE/SKILLS-PHASE-ROADMAP.md#gsd-new-milestone|/gsd-new-milestone]] → All sectors
- [[_REFERENCE/SKILLS-PHASE-ROADMAP.md#gsd-plan-phase|/gsd-plan-phase]] → Project planning

### **Execution** → SEC-024 (Technology), All Venture-Bearing Sectors
- [[_REFERENCE/SKILLS-PHASE-ROADMAP.md#gsd-execute-phase|/gsd-execute-phase]] — Core implementation
  - **Used by:** [[23-VENTURES|All active ventures]]
  - **Capabilities:** [[CAP-001|CAP-001]], [[CAP-008|CAP-008 (CI/CD)]]
  - **Ventures:** [[23-VENTURES/CON-001|CON-001]], [[23-VENTURES/LT-005|LT-005]], [[VEX|VEX]]

- [[_REFERENCE/SKILLS-PHASE-ROADMAP.md#gsd-fast|/gsd-fast]] — Quick fixes for all sectors
- [[_REFERENCE/SKILLS-PHASE-ROADMAP.md#gsd-autonomous|/gsd-autonomous]] — Full automation

### **Quality & Testing** → SEC-024, All Sectors
- [[_REFERENCE/SKILLS-PHASE-ROADMAP.md#gsd-code-review|/gsd-code-review]] — Code quality
  - **Capability:** Testing, verification
  - **Ventures:** [[23-VENTURES|All development]]

- [[_REFERENCE/SKILLS-PHASE-ROADMAP.md#gsd-audit-fix|/gsd-audit-fix]] — Fix issues
- [[_REFERENCE/SKILLS-PHASE-ROADMAP.md#gsd-secure-phase|/gsd-secure-phase]] → [[SEC-033|SEC-033 (Security)]]

### **Shipping** → All Production Sectors
- [[_REFERENCE/SKILLS-PHASE-ROADMAP.md#gsd-ship|/gsd-ship]] — Production deployment
  - **Capability:** [[CAP-008|CAP-008 (CI/CD)]]
  - **Control Planes:** [[_REGISTRIES/control-planes-by-sector.yaml#CP-027|CP-027]], [[_REGISTRIES/control-planes-by-sector.yaml#CP-033|CP-033]]

### **Learning** → All Sectors (Knowledge Management)
- [[_REFERENCE/SKILLS-PHASE-ROADMAP.md#gsd-extract-learnings|/gsd-extract-learnings]] → [[23-VENTURES|Ventures]]
- [[_REFERENCE/SKILLS-PHASE-ROADMAP.md#gsd-mempalace-capture|/gsd-mempalace-capture]] → Knowledge base

---

## Skills by Sector Mapping (Active Ventures)

### **SEC-002: Construction & Infrastructure** 
[[SECTORS/SEC-002-construction-infrastructure|Main]] | [[00-CONSTITUTION/opcos/OpCo-002|OpCo-002]]

**Ventures Using Skills:**
- [[23-VENTURES/CON-001|CON-001 (Ace Construction)]] uses:
  - `/gsd-execute-phase` — Build dispatch system
  - `/gsd-code-review` — Quality gates
  - `/qa` — Testing construction logic
  - `/ship` — Deploy to production
  - [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#project-management|Project management skills]]
  - [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#data--databases|Database skills]] for schedules, materials

**Capabilities Needed:**
- [[CAP-001|CAP-001: API Design]] ← `/gsd-execute-phase`, `/plan-eng-review`
- [[CAP-004|CAP-004: Data Modeling]] ← `/gsd-map-codebase`, database skills
- [[CAP-012|CAP-012: Database]] ← SQL skills, database design skills

**Related Skills:**
- [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#project-management|Project management skills]] (25+)
- [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#data--databases|Database skills]] (17+)
- [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#workflow--process-design|Workflow design]] (12+)

---

### **SEC-008: Financial Services**
[[SECTORS/SEC-008-financial-services|Main]] | [[00-CONSTITUTION/opcos/OpCo-008|OpCo-008]]

**Ventures Using Skills:**
- [[23-VENTURES/FIN-001|FIN-001 (Gateway)]] uses:
  - `/gsd-execute-phase` — Build payment APIs
  - `/cso` — Security audit ([[CAP-014|CAP-014]])
  - [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#api-design--development|API skills]] (28+)
  - [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#authentication--authorization|Auth skills]] (22+)
  - [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#compliance--security|Compliance skills]] (18+)

- [[23-VENTURES/FIN-037|FIN-037 (Trading)]] uses:
  - `/gsd-execute-phase` — Build trading engine
  - `/benchmark` — Performance tuning ([[CAP-013|CAP-013]])
  - [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#performance-optimization|Performance skills]] (25+)
  - [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#caching--performance|Caching skills]] (18+)

**Capabilities Needed:**
- [[CAP-001|CAP-001: API Design]] ← API design skills
- [[CAP-002|CAP-002: Authentication]] ← Auth skills (OAuth, JWT, MFA)
- [[CAP-003|CAP-003: Authorization]] ← RBAC skills
- [[CAP-014|CAP-014: Security Audit]] ← Security audit skills
- [[CAP-015|CAP-015: Compliance]] ← Compliance skills

**Critical Unmapped Skills:** [[CAP-019|CAP-019 (Blockchain)]] skills needed for crypto integration

---

### **SEC-017: Logistics & Transportation**
[[SECTORS/SEC-017-logistics-transportation|Main]] | [[00-CONSTITUTION/opcos/OpCo-017|OpCo-017]]

**Ventures Using Skills:**
- [[23-VENTURES/LT-005|LT-005 (Medical Courier)]] uses:
  - `/gsd-execute-phase` — Build dispatch system
  - [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#data--databases|Database skills]] (17+) — Routes, deliveries
  - [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#workflow--process-design|Workflow skills]] (12+) — Dispatch logic
  - `/qa` — Test route optimization
  - [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#machine-learning--ai|ML skills]] — Route prediction

**Capabilities Needed:**
- [[CAP-001|CAP-001: API Design]] ← API design skills
- [[CAP-004|CAP-004: Data Modeling]] ← Geographic, routing data
- [[CAP-017|CAP-017: NLP]] ← Natural language processing skills
- [[CAP-020|CAP-020: Cloud Infrastructure]] ← Maps, geolocation APIs

**Skills for Geolocation:**
- [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#maps--geolocation|Geolocation skills]] (needed)

---

### **SEC-024: Technology & Software**
[[SECTORS/SEC-024-technology-software|Main]] | [[00-CONSTITUTION/opcos/OpCo-024|OpCo-024]]

**Ventures Using Skills:**
- [[VEX|VEX Hero]] uses **ALL major skill categories**:
  - `/gsd-*` (71 skills) — Full execution framework
  - `/design-*` (14+ skills) — Design system
  - `/plan-*` (review skills) — Architecture, strategy
  - `/review` → Code review
  - `/qa` → Testing
  - `/ship` → Deployment
  - [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#react|React skills]] (50+)
  - [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#nextjs|Next.js skills]] (30+)
  - [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#api-design--development|API skills]] (28+)
  - [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#testing|Testing skills]] (70+)
  - [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#devops--infrastructure|DevOps skills]] (40+)

- [[23-VENTURES/TECH-040|TECH-040]] and other TECH-* use subset

**Capabilities Needed (All 8+):**
- [[CAP-001|CAP-001: API Design]] ← API design skills
- [[CAP-002|CAP-002: Authentication]] ← Auth skills
- [[CAP-008|CAP-008: CI/CD]] ← CI/CD skills, GitHub Actions

**Skills By Count:**
1. [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#react|React & JSX]] — 50+ skills
2. [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#javascript|JavaScript]] — 50+ skills
3. [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#testing|Testing]] — 70+ skills
4. [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#devops--infrastructure|DevOps]] — 40+ skills
5. [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#python|Python]] — 45+ skills

---

## Skills by Phase (Maps to Venture Lifecycle)

See [[_REFERENCE/SKILLS-PHASE-ROADMAP.md|Skills Phase Roadmap]] for complete mapping

### **Phase 1: Discovery** (80+ skills)
[[_REFERENCE/SKILLS-PHASE-ROADMAP.md#phase-1-discovery|Full Phase 1 Guide]]
- [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#brainstorming|Brainstorming skills]] (8+)
- [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#research|Research skills]] (25+)
- [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#market-research|Market research]] (20+)
- **Applied to:** [[SECTOR_INDEX|All sectors]] for new ventures

### **Phase 2: Strategy** (120+ skills)
[[_REFERENCE/SKILLS-PHASE-ROADMAP.md#phase-2-strategy|Full Phase 2 Guide]]
- [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#planning|Planning skills]] (25+)
- **Applied to:** [[23-VENTURES/CON-001|CON-001]], [[23-VENTURES/FIN-037|FIN-037]]

### **Phase 3: Design** (280+ skills)
[[_REFERENCE/SKILLS-PHASE-ROADMAP.md#phase-3-design|Full Phase 3 Guide]]
- [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#design-systems|Design system skills]] (40+)
- [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#database-design|Database design]] (25+)
- [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#api-design--development|API design]] (28+)
- **Applied to:** [[VEX|VEX]] architecture

### **Phase 4: Development** (500+ skills)
[[_REFERENCE/SKILLS-PHASE-ROADMAP.md#phase-4-development|Full Phase 4 Guide]]
- Language-specific skills (5 × 40+)
- Framework skills (10 × 25+)
- **Applied to:** All ventures

### **Phase 5: Testing** (350+ skills)
[[_REFERENCE/SKILLS-PHASE-ROADMAP.md#phase-5-testing|Full Phase 5 Guide]]
- [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#testing-frameworks|Testing frameworks]] (70+)
- [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#security--compliance|Security testing]] (50+)
- **Applied to:** [[23-VENTURES/CON-001|CON-001]], [[VEX|VEX]]

### **Phase 6: Shipping** (150+ skills)
[[_REFERENCE/SKILLS-PHASE-ROADMAP.md#phase-6-shipping|Full Phase 6 Guide]]
- Deployment skills (40+)
- Release management (15+)
- **Applied to:** All production ventures

### **Phase 7: Operations** (200+ skills)
[[_REFERENCE/SKILLS-PHASE-ROADMAP.md#phase-7-operations|Full Phase 7 Guide]]
- Monitoring skills (25+)
- Optimization skills (25+)
- **Applied to:** [[VEX|VEX]], [[23-VENTURES/FIN-037|FIN-037]]

### **Phase 8: Learning** (100+ skills)
[[_REFERENCE/SKILLS-PHASE-ROADMAP.md#phase-8-learning|Full Phase 8 Guide]]
- Knowledge management ([[graphify|/graphify]], [[brain|/brain]])
- Analytics skills (30+)
- **Applied to:** [[_REFERENCE/SKILLS-PHASE-ROADMAP.md|All phases (cyclical)]]

---

## Skills by Technology Stack

### **Frontend (React/Next.js)** → SEC-024
- **React Skills:** [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#react|50+ variants]]
  - Used by: [[VEX|VEX]], [[23-VENTURES/TECH-*|TECH ventures]]
  - Capability: [[CAP-001|CAP-001 (API)]], [[CAP-005|CAP-005 (Cache)]]

- **Next.js Skills:** [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#nextjs|30+ variants]]
  - Framework: [[VEX|VEX]], [[23-VENTURES|Multiple ventures]]

- **JavaScript/TypeScript:** [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#javascript|50+ variants]]

### **Backend (Python/Go)** → SEC-024, SEC-008, SEC-017
- **Python:** [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#python|45+ variants]]
  - Used by: [[23-VENTURES/FIN-037|FIN-037 (Trading)]], [[23-VENTURES/LT-005|LT-005]]
  - Capability: [[CAP-004|CAP-004 (Data)]], [[CAP-016|CAP-016 (ML)]]

- **Go:** [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#go|16 variants]]
  - Used by: Infrastructure ventures
  - Capability: [[CAP-001|CAP-001 (API)]], [[CAP-020|CAP-020 (Cloud)]]

### **Database** → All Sectors
- **PostgreSQL:** [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#postgresql|20+ variants]]
  - Used by: [[23-VENTURES|All ventures]]
  - Capability: [[CAP-012|CAP-012 (Database)]]
  - [[_REGISTRIES/control-planes-by-sector.yaml#CP-023|CP-023]] (Commerce) primary user

- **MongoDB:** [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#mongodb|15+ variants]]
- **SQL:** [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#sql|30+ variants]]

### **DevOps/Infrastructure** → SEC-024, SEC-032
- **Docker:** [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#docker|20+ variants]]
  - Capability: [[CAP-020|CAP-020 (Cloud)]]

- **Kubernetes:** [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#kubernetes|25+ variants]]
  - Needed by: [[SEC-024|SEC-024]], [[SEC-032|SEC-032]]
  - Missing Capability: [[CAP-009|CAP-009 (Container Orch)]]

- **Terraform:** [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#terraform|18+ variants]]
- **AWS:** [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#aws|15+ variants]]
- **Azure:** [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#azure|119+ variants]] ⭐ LARGEST

### **Testing** → All Sectors
- **Jest:** [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#jest|15+ variants]]
- **Cypress:** [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#cypress|18+ variants]]
- **Playwright:** [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#playwright|20+ variants]]
- **Pytest:** [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#pytest|15+ variants]]

### **AI/ML** → SEC-032
- **LLMs:** [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#large-language-models|40+ variants]]
  - Used by: [[23-VENTURES/AI-*|AI ventures]], [[VEX|VEX]]
  - Capability: [[CAP-016|CAP-016 (ML)]]

- **PyTorch:** [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#pytorch|18+ variants]]
- **TensorFlow:** [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#tensorflow|15+ variants]]
- **Hugging Face:** [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md#hugging-face|13+ variants]]

---

## Wiki Links Summary

**Sectorsconnected to skills:**
- [[SECTOR_INDEX|All 35 sectors]] → Skills used by sector
- [[SECTOR-CAPABILITY-CONNECTIONS|Sector-capability map]] → Related skills
- [[SECTORS/SEC-024-technology-software|SEC-024]] uses most skills

**Capabilities connected to skills:**
- [[CAPABILITY-INDEX|All capabilities]] → Skills that implement each capability
- [[CAP-001|CAP-001 (API)]] → API design skills (28+)
- [[CAP-016|CAP-016 (ML)]] → ML skills (40+)

**Ventures connected to skills:**
- [[VEX|VEX]] uses 500+ skills across all phases
- [[23-VENTURES/CON-001|CON-001]] uses 50+ project skills
- [[23-VENTURES/FIN-037|FIN-037]] uses 100+ financial + ML skills

**Phases connected to skills:**
- [[_REFERENCE/SKILLS-PHASE-ROADMAP.md|Full roadmap]] organizes by 8 project phases
- [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md|Complete catalog]] lists all 2,093 with variants

---

## Next Steps

1. **Add sector tags to all 2,093 skills** (categorize by primary/secondary sector)
2. **Link each skill to capabilities it implements** (skill → CAP-### relationship)
3. **Create venture-specific skill recommendations** (VEN-### → top 20 skills)
4. **Build Neo4j graph:** `:SKILL -[:USED_BY]-> :VENTURE` + `:SKILL -[:IMPLEMENTS]-> :CAPABILITY`
5. **Enable skill discovery:** Query interface to find "skills for SEC-XXX implementing CAP-YYY"

---

**Generated:** 2026-09-10  
**Authority:** [[00-CONSTITUTION|Constitution]], [[STARTHERE|StartHere]]  
**Cross-References:** [[_REFERENCE/SKILLS-PHASE-ROADMAP.md|Phase Roadmap]], [[_REFERENCE/ALL-2093-SKILLS-COMPLETE-CATALOG.md|Complete Catalog]], [[CAPABILITY-INDEX|Capability Index]]
