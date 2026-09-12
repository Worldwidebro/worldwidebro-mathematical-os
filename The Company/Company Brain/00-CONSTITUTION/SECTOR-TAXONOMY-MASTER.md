---
id: DOC-SEC-MASTER-001
title: 36-Sector Taxonomy Master Index
description: "Company-wide sector classification organizing ventures, capabilities, resources. Master reference for VEX crosswalk and sector-scoped operations."
aliases: ["Sector Taxonomy", "SECTOR-TAXONOMY", "Sector-Taxonomy", "36-Sector-Taxonomy", "Sector-Taxonomy-Master"]
tags: [sector, taxonomy, governance, master-index]
status: active
updated: 2026-09-05
---

[[STARTHERE]] | [[REALITY]] | [[00_RESPECT/RESPECT|RESPECT]] | [[SECTOR_INDEX]] | [[00-CONSTITUTION]] | [[INDEX]]

# 36-Sector Taxonomy Master Index


**Purpose:** Company-wide sector classification. Each sector is a distinct business vertical with operating model, regulatory environment, and venture portfolio.

**Status:** Framework complete | **VEX crosswalk in progress** (validates sector assignments against live ventures)

**Architecture:** 
- **Layers:** 20 processing layers (00-50 domains) = HOW the system works
- **Sectors:** 35 business sectors + 1 discovery slot = WHAT the system works on
- **Integration:** Sectors overlay layers; every venture/capability/agent/skill belongs to exactly one sector

---

## 35-Sector Registry

| # | Sector | Description | OpCo | Control Planes | Repository | Status | Ventures | Active |
|---|--------|-------------|------|---|---|---|---|---|
| SEC-001 | Beauty & Wellness | Cosmetics, skincare, personal care, fitness, wellness | OpCo-001 | CP-022, CP-023, CP-024 | BEAUTY-* | 🟢 | ~12 | ✅ |
| SEC-002 | Construction & Infrastructure | General contracting, project management, materials, equipment | OpCo-002 | CP-012, CP-026, CP-027 | CON-* | 🟢 | ~8 | ✅ CON-001, CON-011 |
| SEC-003 | Consumer Electronics & Hardware | Smartphones, wearables, IoT devices, home appliances | OpCo-003 | CP-012, CP-028, CP-032 | ELEC-* | 🟡 | ~2 | ⏳ |
| SEC-004 | Content & Media | Publishing, podcasting, streaming, news, entertainment | OpCo-004 | CP-013, CP-019, CP-024 | MEDIA-* | 🟡 | ~5 | ⏳ |
| SEC-005 | Education & Training | K-12, higher education, corporate training, skill dev | OpCo-005 | CP-013, CP-025, CP-028 | EDU-*, ET-* | 🟢 | ~15 | ✅ ET-011 |
| SEC-006 | Energy & Utilities | Renewable energy, oil & gas, electricity, water | OpCo-006 | CP-006, CP-026, CP-027 | ENERGY-* | 🟡 | ~3 | ⏳ |
| SEC-007 | Environmental Services | Waste management, recycling, sustainability, carbon | OpCo-007 | CP-007, CP-031, CP-033 | ENV-* | 🟡 | ~2 | ⏳ |
| SEC-008 | Financial Services | Banking, payments, fintech, insurance, investment | OpCo-008 | CP-020, CP-023, CP-030 | FIN-*, FINTECH-* | 🟢 | ~45 | ✅ FIN-001 gateway |
| SEC-009 | Food & Agriculture | Farming, food production, distribution, food tech | OpCo-009 | CP-009, CP-026, CP-029 | FOOD-*, AGRI-* | 🟡 | ~5 | ⏳ |
| SEC-010 | Food Service & Restaurants | QSR, fine dining, ghost kitchens, meal kits | OpCo-010 | CP-010, CP-022, CP-026 | REST-*, F&B-* | 🟡 | ~8 | ⏳ |
| SEC-011 | Gaming & Entertainment | Video games, esports, casinos, gaming platforms | OpCo-011 | CP-011, CP-019, CP-024 | GAME-*, EC-* | 🟢 | ~18 | ✅ EC-111 (Miss Toys) |
| SEC-012 | Healthcare & Biotechnology | Medical devices, pharma, biotech, diagnostics, healthtech | OpCo-012 | CP-012, CP-022, CP-033 | HC-*, BIO-* | 🟡 | ~6 | ⏳ |
| SEC-013 | Hospitality & Travel | Hotels, resorts, travel agencies, tour operators | OpCo-013 | CP-013, CP-025, CP-027 | HOSP-*, TRAVEL-* | 🟡 | ~5 | ⏳ |
| SEC-014 | Human Resources & Staffing | Recruiting, talent mgmt, workforce solutions, payroll | OpCo-014 | CP-025, CP-026, CP-029 | OPS-*, HR-* | 🟢 | ~8 | ✅ OPS-001 |
| SEC-015 | Insurance | Property & casualty, life, health, specialty, reinsurance | OpCo-015 | CP-015, CP-020, CP-030 | INS-* | 🟡 | ~3 | ⏳ |
| SEC-016 | Legal & Compliance | Legal services, compliance tech, contract management | OpCo-016 | CP-016, CP-018, CP-033 | LEGAL-*, COMP-* | 🟡 | ~2 | ⏳ |
| SEC-017 | Logistics & Transportation | Freight, last-mile delivery, supply chain, fleet mgmt | OpCo-017 | CP-017, CP-026, CP-029 | LT-* | 🟢 | ~15 | ✅ LT-005 (Medical Courier) |
| SEC-018 | Manufacturing & Engineering | Industrial equipment, components, contract manufacturing | OpCo-018 | CP-018, CP-026, CP-028 | MFG-*, ENG-* | 🟡 | ~4 | ⏳ |
| SEC-019 | Marketing & Advertising | Ad agencies, marketing tech, programmatic ads, analytics | OpCo-019 | CP-019, CP-024, CP-025 | MKTG-*, AD-* | 🟡 | ~6 | ⏳ |
| SEC-020 | Real Estate & Property | Commercial real estate, residential, property mgmt | OpCo-020 | CP-020, CP-023, CP-026 | RE-*, PROP-* | 🟢 | ~12 | ✅ RE-001 |
| SEC-021 | Retail & E-commerce | Online retail, physical stores, omnichannel, fulfillment | OpCo-021 | CP-021, CP-023, CP-029 | RETAIL-*, EC-* | 🟢 | ~25 | ✅ COMM-* ventures |
| SEC-022 | Telecommunications & Connectivity | Wireless carriers, broadband, ISPs, telecom infra, 5G | OpCo-022 | CP-022, CP-024, CP-033 | TELECOM-*, ISP-* | 🟡 | ~2 | ⏳ |
| SEC-023 | Professional Services | Consulting, accounting, audit, strategy, design, arch | OpCo-023 | CP-023, CP-025, CP-028 | PROF-*, CONSULT-* | 🟡 | ~5 | ⏳ |
| SEC-024 | Technology & Software | SaaS, cloud platforms, enterprise software, infra, AI/ML | OpCo-024 | CP-024, CP-028, CP-032 | TECH-* | 🟢 | ~85 | ✅ VEX, TECH-040 |
| SEC-025 | Automotive & Mobility | Vehicle manufacturing, autonomous vehicles, ride-sharing | OpCo-025 | CP-025, CP-026, CP-027 | AUTO-*, MOBILITY-* | 🟡 | ~3 | ⏳ |
| SEC-026 | Utilities & Infrastructure | Water, sewer, waste, municipal services, smart grid | OpCo-026 | CP-026, CP-027, CP-033 | UTIL-*, INFRA-* | 🟡 | ~2 | ⏳ |
| SEC-027 | Venture Capital & Investment | VC firms, angel networks, equity crowdfunding | OpCo-027 | CP-027, CP-020, CP-030 | VC-*, INVEST-* | 🟡 | ~2 | ⏳ |
| SEC-028 | B2B Enterprise Software | ERP, CRM, HCM, supply chain software, workflow | OpCo-028 | CP-028, CP-023, CP-024 | B2B-*, ENT-* | 🟡 | ~8 | ⏳ |
| SEC-029 | Marketplace & Platform | Multi-sided platforms, buyer-seller networks, gig econ | OpCo-029 | CP-029, CP-021, CP-023 | MARKET-*, PLAT-* | 🟡 | ~10 | ⏳ |
| SEC-030 | Fintech & Payments | Digital payments, cryptocurrency, blockchain, lending | OpCo-030 | CP-030, CP-020, CP-032 | CRYPTO-*, PAYMENT-* | 🟢 | ~22 | ✅ Arbitrage Nexus |
| SEC-031 | Climate & Sustainability | Carbon monitoring, renewable energy, ESG tech, adaptation | OpCo-031 | CP-031, CP-007, CP-024 | CLIMATE-*, SUSTAIN-* | 🟡 | ~3 | ⏳ |
| SEC-032 | Artificial Intelligence & ML | LLMs, computer vision, AI infrastructure, foundation models | OpCo-032 | CP-032, CP-024, CP-033 | AI-*, ML-* | 🟢 | ~12 | ✅ (native MLX via exo :52415) |
| SEC-033 | Cybersecurity & Privacy | Security software, incident response, compliance tools | OpCo-033 | CP-033, CP-018, CP-032 | SEC-*, CYBER-* | 🟡 | ~4 | ⏳ |
| SEC-034 | Decentralized & Web3 | Blockchain infrastructure, DeFi, NFTs, DAOs, exchanges | OpCo-034 | CP-034, CP-030, CP-032 | WEB3-*, DEFI-* | 🟡 | ~8 | ⏳ |
| SEC-035 | [RESERVED] | Discovery slot for 36th sector found in VEX analysis | — | — | — | ⏳ | — | — |
| SEC-037 | Capital & Quantitative Trading | Algorithmic trading, statistical arbitrage, Python execution | OpCo-030 | CP-020, CP-030, CP-032 | FIN-037-* | 🟢 | ~3 | ✅ FIN-037 Trading Engine |

**Note on SEC-037:** Codified in [[00-CONSTITUTION/SEC-037|SEC-037.md]] as a specialized high-performance trading vertical under SEC-030 (Fintech) and SEC-008 (Financial Services).

**Legend:**
- 🟢 = Active (ventures live, revenue, or MVP deployed)
- 🟡 = Staging (ventures planned, validation phase, or builds underway)
- ⏳ = Discovery (slot reserved or waiting for ventures)

---

## Scattered Files Mapping

### Files Currently in `/~/.claude/projects/memory/` (Session Memory)
These need sector organization:

| Memory File | Primary Sector | Type | Status |
|---|---|---|---|
| clickup-company-brain-architecture.md | SEC-024 (multi-sector platform) | Integration | ✅ Ready |
| clickup-v2-complete-model.md | SEC-024 | Spec | ✅ Ready |
| clickup-extraction-results-2026-09-02.md | SEC-017, SEC-002, SEC-024 | Extraction | ✅ Ready |
| clickup-workspace-inventory.md | SEC-024 (multi) | Inventory | ✅ Ready |
| status-2026-09-02-complete.md | SEC-024 | Status | ✅ Ready |
| ClickUp OAuth token | SEC-024 | Auth | ✅ Secure |
| venture-loops-framework.md | Multi-sector | Pattern | Needs update |
| venture-readiness-scorecard-v2.md | Multi-sector | Dashboard | Needs sector pivot |
| skill-execution-framework.md | Multi-sector | Taxonomy | Needs update |
| con-001-live-deployment-2026-07.md | SEC-002 | Venture status | Ready to move |
| lt-005-medical-courier-deployment.md | SEC-017 | Venture status | Ready to move |
| vex-hero-setup-complete.md | SEC-024 | Platform | Ready to move |
| agent-os-completion-2026-07-30.md | Multi-sector | Architecture | Needs update |
| system-topology-2026-07-30.md | Multi-sector | Infrastructure | Needs update |

### Files in Company Brain Folders (Scattered by Layer, Not Sector)
Need sector organization:

| Current Location | Content | Should Map To | Action |
|---|---|---|---|
| /23-VENTURES/README.md | All ventures listed | Needs sector split → 35 sections | Create per-sector venture lists |
| /14-CAPABILITIES/README.md | All capabilities | Needs sector split → 35 sections | Create per-sector capability lists |
| /16-AGENTS/README.md | All agents | Needs sector split → 35 sections | Create per-sector agent lists |
| /15-SKILLS/README.md | All skills | Needs sector split → 35 sections | Create per-sector skill lists |
| /13-REPOSITORIES/README.md | All repos | Needs sector split → 35 sections | Create per-sector repo lists |
| /20-DECISIONS/... | Scattered decisions | Needs sector tagging | Add SEC-### tags |
| /_REGISTRIES/cbp_registry.yaml | Control points | Needs sector assignment | Add sector field per CP |

---

## Obsidian Knowledge Graph Integration

**Vault:** `/Users/acebless/Documents/The Company/` (ID: 074a5603b4ce9231)

**Current State:**
- ✅ 50-layer structure (00-CONSTITUTION through 50-MASTER-CONTROL) indexed in Obsidian
- ❌ NO sector overlay in vault
- ❌ Scattered venture/capability notes not sector-organized
- ❌ ClickUp integration not yet reflected in knowledge graph

**Required Wikilinks (To Create):**

```markdown
# Per-sector entry points (in vault root or INDEX):
[[SECTORS/SEC-001-beauty-wellness|SEC-001]]
[[SECTORS/SEC-002-construction-infrastructure|SEC-002]]
[[SECTORS/SEC-017-logistics-transportation|SEC-017]]
[[SECTORS/SEC-024-technology-software|SEC-024]]
... (35 sectors)

# Backlinks from ventures to sectors:
[[23-VENTURES/CON-001|CON-001]] → [[SECTORS/SEC-002-construction-infrastructure|SEC-002]]
[[23-VENTURES/LT-005|LT-005]] → [[SECTORS/SEC-017-logistics-transportation|SEC-017]]
`TECH-040` (Speculative) → [[SECTORS/SEC-024-technology-software|SEC-024]]

# Backlinks from capabilities to sectors:
`CAP-000247` (Entity Resolution) → [[SECTORS/SEC-024-technology-software|SEC-024]]
`CAP-000001` (Lead Capture) → [[SEC-008-Financial]]

# Backlinks from ClickUp to sectors:
Antwuan Johns Workspace (ClickUp) → [[SECTORS/SEC-024-technology-software|SEC-024]], [[SECTORS/SEC-017-logistics-transportation|SEC-017]], [[SECTORS/SEC-002-construction-infrastructure|SEC-002]]
Medical Courier Workspace (ClickUp) → [[SECTORS/SEC-017-logistics-transportation|SEC-017]]
```

---

## Implementation Checklist (THIS SESSION)

### Task 1: Sector Master Index ✅
- [x] Create SECTOR-TAXONOMY-MASTER.md (this file)
- [ ] Validate 35 sectors against venture pipeline
- [ ] Assign SEC-035 or remove as discovery slot

### Task 2: Sector-Based Registries (NEXT)
- [ ] Create `_REGISTRIES/ventures-by-sector.yaml` (VEN-### → SEC-###)
- [ ] Create `_REGISTRIES/capabilities-by-sector.yaml` (CAP-### → SEC-###)
- [ ] Create `_REGISTRIES/agents-by-sector.yaml` (AGT-### → SEC-###)
- [ ] Create `_REGISTRIES/skills-by-sector.yaml` (SKL-### → SEC-###)
- [ ] Create `_REGISTRIES/repositories-by-sector.yaml` (REP-### → SEC-###)
- [ ] Create `_REGISTRIES/control-planes-by-sector.yaml` (CP-### → SEC-###)

### Task 3: ClickUp Integration Update (NEXT)
- [ ] Update `clickup_registry_v2.yaml` with sector assignments
- [ ] Map Antwuan Johns workspace → 7 sectors
- [ ] Map Medical Courier workspace → SEC-017
- [ ] Map Construction workspace → SEC-002

### Task 4: Scattered Files Mapping (NEXT)
- [ ] Identify all orphaned memory files
- [ ] Map to sectors
- [ ] Create sector-scoped memory folders
- [ ] Update MEMORY.md index with sector organization

### Task 5: Obsidian Knowledge Graph (FOLLOW-UP)
- [ ] Create sector index pages (35 files)
- [ ] Add wikilinks from ventures → sectors
- [ ] Add wikilinks from capabilities → sectors
- [ ] Add wikilinks from ClickUp workspaces → sectors
- [ ] Update Obsidian graph.json with sector relationships

---

## Quick Reference: Sector → OpCo → Control Planes

```
SEC-001 (Beauty) → OpCo-001 → CP-022, CP-023, CP-024
SEC-002 (Construction) → OpCo-002 → CP-012, CP-026, CP-027
SEC-008 (Financial) → OpCo-008 → CP-020, CP-023, CP-030
SEC-017 (Logistics) → OpCo-017 → CP-017, CP-026, CP-029
SEC-024 (Technology) → OpCo-024 → CP-024, CP-028, CP-032
```

---

**Status:** Active | **Next:** Proceed to Task 2 (sector registries)  
**Created:** 2026-09-02 | **Updated:** 2026-09-02
