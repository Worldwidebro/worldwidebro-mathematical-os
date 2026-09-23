# Company Brain — Domain Map & Wiring Guide

**Purpose:** Master map of all 71 domains + linking strategy  
**Updated:** 2026-09-23  
**Navigation:** [[INDEX|INDEX.md]] | [[LOG|LOG.md]]

---

## SCATTERED & INFRASTRUCTURE DIRECTORIES (Wired Sep 23)

| Folder | Purpose | Index |
|--------|---------|-------|
| **_MEMORY** | Memory system, learning cycles | [[../../_MEMORY/INDEX|_MEMORY/INDEX.md]] |
| **_REFERENCE** | Architecture docs, runbooks | [[../../_REFERENCE/INDEX|_REFERENCE/INDEX.md]] |
| **00_RESPECT** | Respect framework, accountability | [[../../00_RESPECT/INDEX|00_RESPECT/INDEX.md]] |
| **_PROMPTS** | Pre-action awareness, decision prompts | See [[../../../_PROMPTS|_PROMPTS/]] |
| **_AGENTS** | Agent definitions, configurations | See [[../../../_AGENTS|_AGENTS/]] |
| **_REGISTRIES** | Canonical registries, truth sources | See [[../../../_REGISTRIES|_REGISTRIES/]] |
| **_ONTOLOGY** | Schema definitions, taxonomies | See [[../../../_ONTOLOGY|_ONTOLOGY/]] |

---

## WIRING ARCHITECTURE

```
STARTHERE.md (entry)
    ↓
INDEX.md (master catalog)
    ↓
DOMAIN-MAP.md (this file - shows all 71 domains)
    ↓
Domain INDEX.md (one per domain: 00-CONSTITUTION/INDEX.md, etc.)
    ↓
Individual files within each domain
```

Each domain folder should have an **INDEX.md** that lists:
- Domain purpose & authority
- Files in that domain (with one-line descriptions)
- Related domains (cross-links)
- Owner/steward

---

## LAYER 1: GOVERNANCE & FOUNDATION (00-07)

| # | Domain | Purpose | Files | Index |
|---|--------|---------|-------|-------|
| **00** | CONSTITUTION | Mission, principles, governance | [[00-CONSTITUTION/README]] | [[00-CONSTITUTION/INDEX|INDEX.md]] |
| **01** | IDENTITY | Company structure, ventures, brands | [[01-IDENTITY/README]] | [[01-IDENTITY/INDEX|INDEX.md]] |
| **02** | SOURCES | External data sources, feeds | [[02-SOURCES/README]] | [[02-SOURCES/INDEX|INDEX.md]] |
| **03** | INGESTION | Data ingestion pipelines | [[03-INGESTION/README]] | [[03-INGESTION/INDEX|INDEX.md]] |
| **04** | DATA | Raw data, databases, schemas | [[04-DATA/README]] | [[04-DATA/INDEX|INDEX.md]] |
| **05** | METADATA | Entity metadata, attributes | [[05-METADATA/README]] | [[05-METADATA/INDEX|INDEX.md]] |
| **06** | ENTITY-RESOLUTION | Deduplication, identity matching | [[06-ENTITY-RESOLUTION/README]] | [[06-ENTITY-RESOLUTION/INDEX|INDEX.md]] |
| **07** | ONTOLOGY | Schemas, type systems, taxonomies | [[07-ONTOLOGY/README]] | [[07-ONTOLOGY/INDEX|INDEX.md]] |

---

## LAYER 2: INTELLIGENCE & KNOWLEDGE (08-12)

| # | Domain | Purpose | Files | Index |
|---|--------|---------|-------|-------|
| **08** | KNOWLEDGE-GRAPH | Neo4j, relationships, graph structure | [[08-KNOWLEDGE-GRAPH/README]] | [[08-KNOWLEDGE-GRAPH/INDEX|INDEX.md]] |
| **09** | KNOWLEDGE | Synthesized understanding, insights | [[09-KNOWLEDGE/README]] | [[09-KNOWLEDGE/INDEX|INDEX.md]] |
| **10** | MEMORY | Organizational memory system, learning | [[10-MEMORY/README]] | [[10-MEMORY/INDEX|INDEX.md]] |
| **11** | INDEXING | Search indexing, discovery (graft/gbrain) | [[11-INDEXING/README]] | [[11-INDEXING/INDEX|INDEX.md]] |
| **12** | CONTEXT | Context assembly, relevance, retrieval | [[12-CONTEXT/README]] | [[12-CONTEXT/INDEX|INDEX.md]] |

---

## LAYER 3: CAPABILITY SYSTEMS (13-19)

| # | Domain | Purpose | Files | Index |
|---|--------|---------|-------|-------|
| **13** | REPOSITORIES | Git repos, code, documentation | [[13-REPOSITORIES/README]] | [[13-REPOSITORIES/INDEX|INDEX.md]] |
| **14** | CAPABILITIES | Capability registry & coverage analysis | [[14-CAPABILITIES/README]] | [[14-CAPABILITIES/INDEX|INDEX.md]] |
| **15** | SKILLS | Skill registry, procedures, how-tos | [[15-SKILLS/README]] | [[15-SKILLS/INDEX|INDEX.md]] |
| **16** | AGENTS | Agent registry, autonomy levels, performance | [[16-AGENTS/README]] | [[16-AGENTS/INDEX|INDEX.md]] |
| **17** | MODELS | LLM models, inference, fine-tuning | [[17-MODELS/README]] | [[17-MODELS/INDEX|INDEX.md]] |
| **18** | TOOLS | Tool registry, integrations, APIs | [[18-TOOLS/README]] | [[18-TOOLS/INDEX|INDEX.md]] |
| **19** | ORCHESTRATION | Workflow orchestration, routing | [[19-ORCHESTRATION/README]] | [[19-ORCHESTRATION/INDEX|INDEX.md]] |

---

## LAYER 4: OPERATIONS & EXECUTION (20-28)

| # | Domain | Purpose | Files | Index |
|---|--------|---------|-------|-------|
| **20** | DECISIONS | Decision frameworks, ADRs | [[20-DECISIONS/README]] | [[20-DECISIONS/INDEX|INDEX.md]] |
| **21** | POLICY | Rules, standards, SOPs | [[21-POLICY/README]] | [[21-POLICY/INDEX|INDEX.md]] |
| **22** | EXECUTION | Execution loops, work tracking | [[22-EXECUTION/README]] | [[22-EXECUTION/INDEX|INDEX.md]] |
| **22** | VENTURES | Venture definition (duplicate folder?) | [[22-VENTURES/README]] | [[22-VENTURES/INDEX|INDEX.md]] |
| **23** | VENTURES | Active ventures, deployments | [[23-VENTURES/README]] | [[23-VENTURES/INDEX|INDEX.md]] |
| **24** | FINANCE | Financial data, projections, metrics | [[24-FINANCE/README]] | [[24-FINANCE/INDEX|INDEX.md]] |
| **25** | SALES | Sales pipeline, leads, deals | [[25-SALES/README]] | [[25-SALES/INDEX|INDEX.md]] |
| **26** | MARKETING | Marketing campaigns, messaging | [[26-MARKETING/README]] | [[26-MARKETING/INDEX|INDEX.md]] |
| **27** | CUSTOMERS | Customer data, accounts, support | [[27-CUSTOMERS/README]] | [[27-CUSTOMERS/INDEX|INDEX.md]] |
| **28** | PRODUCT | Product specs, roadmap, features | [[28-PRODUCT/README]] | [[28-PRODUCT/INDEX|INDEX.md]] |

---

## LAYER 5: BUSINESS OPERATIONS (29-36)

| # | Domain | Purpose | Files | Index |
|---|--------|---------|-------|-------|
| **29** | OPERATIONS | Core operations, processes | [[29-OPERATIONS/README]] | [[29-OPERATIONS/INDEX|INDEX.md]] |
| **30** | HR | People, payroll, benefits | [[30-HR/README]] | [[30-HR/INDEX|INDEX.md]] |
| **31** | LEGAL | Legal documents, compliance, contracts | [[31-LEGAL/README]] | [[31-LEGAL/INDEX|INDEX.md]] |
| **32** | SECURITY | Security policies, incident response | [[32-SECURITY/README]] | [[32-SECURITY/INDEX|INDEX.md]] |
| **33** | COMPLIANCE | Regulatory compliance, audits | [[33-COMPLIANCE/README]] | [[33-COMPLIANCE/INDEX|INDEX.md]] |
| **34** | RISK | Risk management, mitigation | [[34-RISK/README]] | [[34-RISK/INDEX|INDEX.md]] |
| **35** | ASSETS | Asset inventory, management | [[35-ASSETS/README]] | [[35-ASSETS/INDEX|INDEX.md]] |
| **36** | PARTNERS | Partner networks, integrations | [[36-PARTNERS/README]] | [[36-PARTNERS/INDEX|INDEX.md]] |

---

## LAYER 6: RESEARCH & DISCOVERY (37-42)

| # | Domain | Purpose | Files | Index |
|---|--------|---------|-------|-------|
| **37** | RESEARCH | Market research, competitive analysis | [[37-RESEARCH/README]] | [[37-RESEARCH/INDEX|INDEX.md]] |
| **38** | OPPORTUNITIES | Opportunity identification, analysis | [[38-OPPORTUNITIES/README]] | [[38-OPPORTUNITIES/INDEX|INDEX.md]] |
| **39** | EXPERIMENTS | Experiments, A/B tests, pilots | [[39-EXPERIMENTS/README]] | [[39-EXPERIMENTS/INDEX|INDEX.md]] |
| **40** | METRICS | Key metrics, KPIs, dashboards | [[40-METRICS/README]] | [[40-METRICS/INDEX|INDEX.md]] |
| **41** | OBSERVABILITY | Observability, monitoring, alerts | [[41-OBSERVABILITY/README]] | [[41-OBSERVABILITY/INDEX|INDEX.md]] |
| **42** | EVALUATION | Model evaluation, rubrics | [[42-EVALUATION/README]] | [[42-EVALUATION/INDEX|INDEX.md]] |

---

## LAYER 7: LEARNING & EVOLUTION (43-50)

| # | Domain | Purpose | Files | Index |
|---|--------|---------|-------|-------|
| **43** | OUTCOMES | Outcomes, results, impact | [[43-OUTCOMES/README]] | [[43-OUTCOMES/INDEX|INDEX.md]] |
| **44** | LEARNING | Learning systems, feedback loops | [[44-LEARNING/README]] | [[44-LEARNING/INDEX|INDEX.md]] |
| **45** | EVOLUTION | System evolution, improvement | [[45-EVOLUTION/README]] | [[45-EVOLUTION/INDEX|INDEX.md]] |
| **46** | GOVERNANCE | Higher-level governance, strategy | [[46-GOVERNANCE/README]] | [[46-GOVERNANCE/INDEX|INDEX.md]] |
| **47** | DOCUMENTS | Master documents, archives | [[47-DOCUMENTS/README]] | [[47-DOCUMENTS/INDEX|INDEX.md]] |
| **48** | AUTOMATION | Workflow automation, bots | [[48-AUTOMATION/README]] | [[48-AUTOMATION/INDEX|INDEX.md]] |
| **49** | SYSTEM | System architecture, infrastructure | [[49-SYSTEM/README]] | [[49-SYSTEM/INDEX|INDEX.md]] |
| **50** | MASTER-CONTROL | Master control plane, orchestration | [[50-MASTER-CONTROL/README]] | [[50-MASTER-CONTROL/INDEX|INDEX.md]] |

---

## LAYER 8: SPECIALIZED DOMAINS (51-67)

| # | Domain | Purpose | Files | Index |
|---|--------|---------|-------|-------|
| **51** | CONSTRUCTION | Construction ventures, projects | [[51-CONSTRUCTION/README]] | [[51-CONSTRUCTION/INDEX|INDEX.md]] |
| **52** | PEOPLE | People operations, org structure | [[52-PEOPLE/README]] | [[52-PEOPLE/INDEX|INDEX.md]] |
| **53** | TEAMS | Team management, coordination | [[53-TEAMS/README]] | [[53-TEAMS/INDEX|INDEX.md]] |
| **54** | FINANCIAL | Financial services ventures | [[54-FINANCIAL/README]] | [[54-FINANCIAL/INDEX|INDEX.md]] |
| **55** | LOOP-ENGINEERING | Loop engineering patterns, autonomy | [[55-LOOP-ENGINEERING/README]] | [[55-LOOP-ENGINEERING/INDEX|INDEX.md]] |
| **56** | ENGINEERING | Software engineering practices | [[56-ENGINEERING/README]] | [[56-ENGINEERING/INDEX|INDEX.md]] |
| **57** | CODE-INTELLIGENCE | Code analysis, indexing | [[57-CODE-INTELLIGENCE/README]] | [[57-CODE-INTELLIGENCE/INDEX|INDEX.md]] |
| **58** | LOGISTICS | Logistics ventures, operations | [[58-LOGISTICS/README]] | [[58-LOGISTICS/INDEX|INDEX.md]] |
| **59** | MCP | Model Context Protocol servers | [[59-MCP/README]] | [[59-MCP/INDEX|INDEX.md]] |
| **60** | APIS | API specifications, integrations | [[60-APIS/README]] | [[60-APIS/INDEX|INDEX.md]] |
| **61** | KNOWLEDGE-SOURCES | External knowledge sources | [[61-KNOWLEDGE-SOURCES/README]] | [[61-KNOWLEDGE-SOURCES/INDEX|INDEX.md]] |
| **62** | TECHNOLOGY | Technology stack, infrastructure | [[62-TECHNOLOGY/README]] | [[62-TECHNOLOGY/INDEX|INDEX.md]] |
| **63** | CHANGE-MANAGEMENT | Change management, transitions | [[63-CHANGE-MANAGEMENT/README]] | [[63-CHANGE-MANAGEMENT/INDEX|INDEX.md]] |
| **64** | RELATIONSHIPS | Business relationships, partnerships | [[64-RELATIONSHIPS/README]] | [[64-RELATIONSHIPS/INDEX|INDEX.md]] |
| **65** | SYNERGIES | Cross-venture synergies | [[65-SYNERGIES/README]] | [[65-SYNERGIES/INDEX|INDEX.md]] |
| **66** | OPPORTUNITIES-ALT | Alternative opportunities | [[66-OPPORTUNITIES-ALT/README]] | [[66-OPPORTUNITIES-ALT/INDEX|INDEX.md]] |
| **67** | EVOLUTION-ALT | Alternative evolution paths | [[67-EVOLUTION-ALT/README]] | [[67-EVOLUTION-ALT/INDEX|INDEX.md]] |

---

## LAYER 9: EXECUTION (90)

| # | Domain | Purpose | Files | Index |
|---|--------|---------|-------|-------|
| **90** | EXECUTION | (Special) Execution tracking, loops | [[90-EXECUTION/README]] | [[90-EXECUTION/INDEX|INDEX.md]] |

---

## WIRING CHECKLIST

**Each domain needs:**
- [ ] README.md or INDEX.md in the folder
- [ ] One-line description in this map
- [ ] Links to related domains (cross-references)
- [ ] Owner/steward identified
- [ ] List of key files with descriptions

**Master linking:**
- [ ] STARTHERE.md → INDEX.md
- [ ] INDEX.md → DOMAIN-MAP.md (this file)
- [ ] DOMAIN-MAP.md → each Domain INDEX.md
- [ ] Domain INDEX.md → individual files (wikilinks)
- [ ] LOG.md → append timeline entries

**Example domain INDEX structure:**

```markdown
# [Domain Name] — Index

**Domain:** [XX-DOMAIN]  
**Purpose:** [What this domain covers]  
**Owner:** [Person/team responsible]  
**Related Domains:** [[00-CONSTITUTION]], [[01-IDENTITY]]

## Files in This Domain

| File | Purpose |
|------|---------|
| README.md | Overview + entry point |
| [file1.md] | [Description] |
| [file2.yaml] | [Description] |

## Navigation

← [[DOMAIN-MAP]] | [[INDEX|Master Index]]
```

---

## MASTER REGISTRY INTEGRATION

All domains should link back to:
- [[INDEX|_REGISTRIES/CANONICAL/INDEX.md]] — Master catalog
- [[LOG|_REGISTRIES/CANONICAL/LOG.md]] — Timeline
- [[SECTOR-REGISTRY|SECTOR-REGISTRY.yaml]] — 36 sectors
- [[OPCO-REGISTRY|OPCO-REGISTRY.yaml]] — 35 OpCos
- [[BASE-REGISTRY|BASE-REGISTRY.yaml]] — 36 Bases
- [[VENTURE-REGISTRY|VENTURE-REGISTRY.yaml]] — 789 ventures
- [[FAMILY_OFFICE_ECOSYSTEM_ALIGNMENT_MASTER|FAMILY_OFFICE_ECOSYSTEM_ALIGNMENT_MASTER.md]] — 150 entities

---

## NEXT STEPS

1. ✅ **DOMAIN-MAP.md created** (this file) — all 71 domains listed
2. ⏳ **Create sample Domain INDEX files** for core 8 domains:
   - 00-CONSTITUTION/INDEX.md
   - 01-IDENTITY/INDEX.md
   - 08-KNOWLEDGE-GRAPH/INDEX.md
   - 16-AGENTS/INDEX.md
   - 20-DECISIONS/INDEX.md
   - 23-VENTURES/INDEX.md
   - 24-FINANCE/INDEX.md
   - 50-MASTER-CONTROL/INDEX.md
3. ⏳ **Update STARTHERE.md** to reference INDEX.md + DOMAIN-MAP.md
4. ⏳ **Create remaining 63 Domain INDEXes** (can be stubs + gradual fill-in)
5. ⏳ **Wire all domains together** with cross-links

---

## Control Base Architecture

Each domain (00-50) is assigned 10 control bases (500 total):

| Domain | Control Bases | Example Bases |
|--------|---------------|----|
| 00-CONSTITUTION | B001-B010 | [[B001|Mission]], [[B009|Strategic Constraints]] |
| 01-IDENTITY | B011-B020 | [[B011|Organization]], [[B013|Operating Companies]] |
| 07-ONTOLOGY | B061-B070 | [[B031|Sector Registry]] (domains 2-9) |
| 16-AGENTS | B141-B150 | [[B141|Agent Registry]], [[B144|Agent Skills]] |
| 23-VENTURES | B211-B220 | [[B021|Venture Registry]] |
| 50-MASTER-CONTROL | B491-B500 | [[B491|Control Tower]], [[B492|Reality State]] |

**Reference:** [[CBP_REGISTRY|_REGISTRIES/CANONICAL/CBP_REGISTRY.yaml]] (complete 500-base mapping)

---

**Status:** WIRING LAYER 1 ESTABLISHED (Sep 23, 2026)  
**Wiki-Linking:** Phase 5 Complete (Sep 25) — All hubs wired to control bases  
**Next:** Bidirectional linking verification + triage remaining orphaned files

