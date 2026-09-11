---
id: DOC-CAP-INDEX-001
title: Capability Registry Index & Wiki Links
description: "Master index of all capabilities with sector mappings, wiki links, and cross-references"
aliases: ["CAPABILITY-INDEX", "CAP-INDEX", "Capability-Index", "Capabilities-Index"]
tags: [capability, taxonomy, index, governance, registry]
status: ACTIVE
updated: 2026-09-10
---

[[STARTHERE]] | [[REALITY]] | [[00-CONSTITUTION]] | [[SECTOR_INDEX]] | [[SECTOR-TAXONOMY-MASTER]] | [[INDEX]]

# Capability Registry Index

**Purpose:** Centralized index of all 300+ capabilities with wiki links, sector mappings, implementations, and verification.

**Status:** Framework active | **Mapped to Sectors:** 50 of 300 | **Neo4j Synced:** 2026-09-09

**Structure:**
- **300+ Total Capabilities** (CAP-001 to CAP-300+)
- **Organized by Sector** (SEC-001 to SEC-037)
- **Linked to:** [[_REGISTRIES/capabilities-by-sector.yaml|Capability Registry YAML]]
- **Linked to:** [[_ONTOLOGY/CAPABILITY_REGISTRY.yaml|Capability Ontology]]

---

## Core Capability Categories (Mapped to Sectors)

### **SEC-002: Construction & Infrastructure**
[[SECTORS/SEC-002-construction-infrastructure|SEC-002 Main]] | [[00-CONSTITUTION/opcos/OpCo-002|OpCo-002]]

**Capabilities Mapped:**
- [[CAP-012|CAP-012: Database]] — Data persistence for project management
  - **Mapped to:** [[23-VENTURES/CON-001|CON-001 (Ace Construction)]]
  - **Status:** Active
  - **Neo4j Ref:** `:CAPABILITY {id:"CAP-012"}`

---

### **SEC-008: Financial Services**
[[SECTORS/SEC-008-financial-services|SEC-008 Main]] | [[00-CONSTITUTION/opcos/OpCo-008|OpCo-008]]

**Capabilities Mapped:**
- [[CAP-020|CAP-020: Cloud Infrastructure]] — Enterprise cloud for fintech operations
  - **Mapped to:** [[23-VENTURES/FIN-001|FIN-001]] (Gateway)
  - **Status:** Active
  - **Neo4j Ref:** `:CAPABILITY {id:"CAP-020"}`

---

### **SEC-017: Logistics & Transportation**
[[SECTORS/SEC-017-logistics-transportation|SEC-017 Main]] | [[00-CONSTITUTION/opcos/OpCo-017|OpCo-017]]

**Capabilities Mapped:**
- [[CAP-017|CAP-017: Natural Language Processing]] — Route optimization, dispatch comms
  - **Mapped to:** [[23-VENTURES/LT-005|LT-005 (Medical Courier)]]
  - **Status:** Active
  - **Neo4j Ref:** `:CAPABILITY {id:"CAP-017"}`

---

### **SEC-024: Technology & Software**
[[SECTORS/SEC-024-technology-software|SEC-024 Main]] | [[00-CONSTITUTION/opcos/OpCo-024|OpCo-024]]

**Capabilities Mapped (8 total):**

#### **Infrastructure & Data**
- [[CAP-001|CAP-001: API Design]]
  - **Description:** RESTful/GraphQL API architecture
  - **Used By:** [[16-AGENTS|Agent Framework]], [[23-VENTURES/TECH-040|TECH-040]]
  - **Verification:** [[_EVAL/api-design-tests.yaml|API Design Tests]]
  - **Neo4j Ref:** `:CAPABILITY {id:"CAP-001"}`

- [[CAP-004|CAP-004: Data Modeling]]
  - **Description:** Schema design, entity relationships
  - **Used By:** [[23-VENTURES/VEX|VEX Portfolio]]
  - **Status:** Active
  - **Neo4j Ref:** `:CAPABILITY {id:"CAP-004"}`

- [[CAP-012|CAP-012: Database]]
  - **Description:** PostgreSQL, NoSQL, query optimization
  - **Used By:** [[23-VENTURES|All Ventures]]
  - **Status:** Active

#### **Security & Access Control**
- [[CAP-002|CAP-002: Authentication]]
  - **Description:** OAuth 2.0, OIDC, JWT, MFA
  - **Used By:** [[16-AGENTS|Agent Auth]], [[23-VENTURES/TECH-040|TECH-040]]
  - **Verification:** [[_EVAL/auth-integration-tests.yaml|Auth Tests]]
  - **Neo4j Ref:** `:CAPABILITY {id:"CAP-002"}`

- [[CAP-003|CAP-003: Authorization]]
  - **Description:** RBAC, ABAC, policy enforcement
  - **Used By:** [[16-AGENTS|Role-Based Routing]]
  - **Status:** Active
  - **Neo4j Ref:** `:CAPABILITY {id:"CAP-003"}`

#### **Performance & Operations**
- [[CAP-005|CAP-005: Caching]]
  - **Description:** Redis, Memcached, cache invalidation
  - **Used By:** [[23-VENTURES/TECH-040|TECH-040]], [[VEX|VEX Hero]]
  - **Status:** Active

- [[CAP-006|CAP-006: Search]]
  - **Description:** Elasticsearch, full-text search, ranking
  - **Used By:** [[23-VENTURES|Enterprise Search]]
  - **Verification:** [[_EVAL/search-tests.yaml|Search Tests]]
  - **Neo4j Ref:** `:CAPABILITY {id:"CAP-006"}`

- [[CAP-007|CAP-007: Message Queues]]
  - **Description:** Kafka, RabbitMQ, async workflows
  - **Used By:** [[20-DECISIONS|Async Processing]]
  - **Status:** Active

- [[CAP-008|CAP-008: CI/CD]]
  - **Description:** GitHub Actions, deployment pipelines
  - **Used By:** [[23-VENTURES|All Deployment]]
  - **Verification:** [[_EVAL/cicd-tests.yaml|CI/CD Tests]]
  - **Neo4j Ref:** `:CAPABILITY {id:"CAP-008"}`

---

## Unmapped Capabilities (CRITICAL)

**Status:** 9 capabilities without sector assignment — requires [[#Capability-Sector-Mapping-Roadmap|mapping initiative]]

- [[CAP-009|CAP-009: Container Orchestration]] — Kubernetes, Docker Swarm
  - **Status:** UNMAPPED
  - **Sectors Needing:** [[SECTORS/SEC-024-technology-software|SEC-024]], [[SECTORS/SEC-032-artificial-intelligence-ml|SEC-032]]

- [[CAP-010|CAP-010: Microservices]]
  - **Status:** UNMAPPED
  - **Sectors Needing:** [[SECTORS/SEC-024-technology-software|SEC-024]], [[SECTORS/SEC-028-b2b-enterprise-software|SEC-028]]

- [[CAP-011|CAP-011: Observability]]
  - **Status:** UNMAPPED
  - **Sectors Needing:** All sectors (cross-cutting)
  - **Links:** [[_INFRASTRUCTURE/monitoring-stack|Monitoring Stack]]

- [[CAP-013|CAP-013: Performance Tuning]]
  - **Status:** UNMAPPED
  - **Sectors Needing:** All high-scale sectors
  - **Links:** [[_REFERENCE/INFRASTRUCTURE-STATUS|Perf Baselines]]

- [[CAP-014|CAP-014: Security Audit]]
  - **Status:** UNMAPPED
  - **Sectors Needing:** [[SECTORS/SEC-033-cybersecurity-privacy|SEC-033]], all critical sectors

- [[CAP-015|CAP-015: Compliance]]
  - **Status:** UNMAPPED
  - **Sectors Needing:** [[SECTORS/SEC-016-legal-compliance|SEC-016]], [[SECTORS/SEC-033-cybersecurity-privacy|SEC-033]]

- [[CAP-016|CAP-016: Machine Learning]]
  - **Status:** UNMAPPED
  - **Sectors Needing:** [[SECTORS/SEC-032-artificial-intelligence-ml|SEC-032]], [[SECTORS/SEC-024-technology-software|SEC-024]]
  - **Links:** [[_INFRASTRUCTURE/ollama-stack|Ollama LLM Stack]]

- [[CAP-018|CAP-018: Computer Vision]]
  - **Status:** UNMAPPED
  - **Sectors Needing:** [[SECTORS/SEC-032-artificial-intelligence-ml|SEC-032]], [[SECTORS/SEC-002-construction-infrastructure|SEC-002]]

- [[CAP-019|CAP-019: Blockchain]]
  - **Status:** UNMAPPED
  - **Sectors Needing:** [[SECTORS/SEC-030-fintech-payments|SEC-030]], [[SECTORS/SEC-034-decentralized-web3|SEC-034]]

---

## Capability-Sector Mapping Roadmap

**Goal:** Map all 300+ capabilities to sectors by 2026-09-30

**Current Status:**
- **Mapped:** 21 capabilities (7%)
- **Unmapped:** 9 capabilities (3%)
- **Capacity:** 270+ capabilities remain to catalog

### **Phase 1: Critical Capabilities (Week 1-2)**
[[00-CONSTITUTION/CAPABILITY-SECTOR-MAPPING-PLAN.md|Full Roadmap]]

Priority mapping (unmapped → sectors):
1. [[CAP-009|CAP-009: Container Orchestration]] → [[SECTORS/SEC-024-technology-software|SEC-024]], [[SECTORS/SEC-032-artificial-intelligence-ml|SEC-032]]
2. [[CAP-011|CAP-011: Observability]] → All sectors (cross-cutting pattern)
3. [[CAP-014|CAP-014: Security Audit]] → [[SECTORS/SEC-033-cybersecurity-privacy|SEC-033]]
4. [[CAP-016|CAP-016: Machine Learning]] → [[SECTORS/SEC-032-artificial-intelligence-ml|SEC-032]], [[SECTORS/SEC-024-technology-software|SEC-024]]

### **Phase 2: Expansion (Week 3-4)**
- Map secondary capabilities across 35 sectors
- Create [[_REGISTRIES/capabilities-by-sector-expanded.yaml|expanded registry]]
- Wire Neo4j relationships (`:CAPABILITY → :SECTOR`)

### **Phase 3: Verification (Week 5)**
- Validate sector-capability fit against [[23-VENTURES|active ventures]]
- Create [[_EVAL/capability-sector-fit-tests.yaml|fit tests]]
- Update registries

---

## Registry & Ontology Links

**Master Sources:**
- [[_ONTOLOGY/CAPABILITY_REGISTRY.yaml|Capability Ontology]] — Complete schema + examples
- [[_REGISTRIES/capabilities-by-sector.yaml|Capabilities by Sector (YAML)]] — Current state (50 mapped)
- [[CAPABILITY_ORCHESTRATOR_PSEUDOCODE.md|Capability Orchestrator Logic]] — How capabilities route

**Neo4j Integration:**
- **Node Type:** `:CAPABILITY`
- **Example Node:** `(:CAPABILITY {id:"CAP-001", name:"API Design", status:"ACTIVE"})`
- **Relationships:**
  - `:CAPABILITY -[:USED_BY]-> :VENTURE`
  - `:CAPABILITY -[:IMPLEMENTED_BY]-> :IMPLEMENTATION`
  - `:CAPABILITY -[:IN_SECTOR]-> :SECTOR`
  - `:CAPABILITY -[:VERIFIED_BY]-> :EVALUATION`

**Synced:** 2026-09-09 | **Status:** 30 nodes, 45 relationships

---

## Cross-References & Connections

### **By Venture**
[[23-VENTURES|All Ventures]] link to capabilities:
- [[23-VENTURES/CON-001|CON-001 (Ace Construction)]] uses [[CAP-012|CAP-012: Database]]
- [[23-VENTURES/LT-005|LT-005 (Medical Courier)]] uses [[CAP-017|CAP-017: NLP]]
- [[23-VENTURES/FIN-037|FIN-037 (Trading Engine)]] uses [[CAP-020|CAP-020: Cloud]]
- [[VEX|VEX Hero]] uses [[CAP-001|CAP-001: API]], [[CAP-005|CAP-005: Caching]]

### **By Agent**
[[16-AGENTS|All Agents]] route through capabilities:
- [[16-AGENTS/ROUTING-AGENT|Routing Agent]] evaluates [[CAP-001|CAP-001]], [[CAP-003|CAP-003]]
- [[16-AGENTS/SECURITY-AGENT|Security Agent]] uses [[CAP-002|CAP-002]], [[CAP-014|CAP-014]]
- [[16-AGENTS/DEPLOYMENT-AGENT|Deployment Agent]] uses [[CAP-008|CAP-008: CI/CD]]

### **By Control Plane**
[[_REGISTRIES/control-planes-by-sector.yaml|Control Planes]] manage capabilities:
- **CP-020 (Capital)** → [[CAP-020|CAP-020: Cloud]], [[CAP-005|CAP-005: Caching]]
- **CP-024 (Tech)** → [[CAP-001|CAP-001]], [[CAP-008|CAP-008]]
- **CP-033 (Security)** → [[CAP-014|CAP-014]], [[CAP-015|CAP-015]]

---

## Quick Navigation

| Need | Link |
|------|------|
| **Add new capability** | [[_ONTOLOGY/CAPABILITY_REGISTRY.yaml|Edit Registry]] |
| **Map capability to sector** | [[_REGISTRIES/capabilities-by-sector.yaml|Edit Mapping YAML]] |
| **View all sectors** | [[SECTOR_INDEX|Sector Index]] |
| **See venture-capability links** | [[23-VENTURES|Ventures]] |
| **Check Neo4j sync status** | [[_INFRASTRUCTURE/neo4j-sync-status.yaml|Sync Status]] |
| **View capability tests** | [[_EVAL|Evaluation Harness]] |

---

## Summary Statistics

| Metric | Count | Status |
|--------|-------|--------|
| **Total Capabilities Defined** | 300+ | ✅ Defined in YAML |
| **Mapped to Sectors** | 21 | ⚠️ 7% coverage |
| **Unmapped** | 9 | 🔴 Needs mapping |
| **In Neo4j** | 30 | ✅ Synced 2026-09-09 |
| **With Tests** | 8 | ⚠️ Limited coverage |
| **Actively Used** | 12 | ✅ In production ventures |
| **Sectors Using Caps** | 4 | ⚠️ Low adoption |

---

## Next Steps

1. **Map 9 Critical Unmapped Capabilities** (this week)
   - [[CAP-009|CAP-009]], [[CAP-010|CAP-010]], [[CAP-011|CAP-011]], [[CAP-014|CAP-014]], [[CAP-016|CAP-016]]

2. **Expand Registry to 100 Mapped Capabilities** (next week)
   - Add secondary capabilities per sector
   - Create [[_REGISTRIES/capabilities-by-sector-expanded.yaml|expanded YAML]]

3. **Create Capability-Sector Wiki Pages** (ongoing)
   - Each sector gets capability mapping page
   - Link all CAP-### pages to sectors

4. **Wire Neo4j Relationships** (continuous)
   - Run [[_MCP/capability-sector-sync.cypher|sync script]]
   - Verify `:CAPABILITY → :SECTOR` edges

---

**Generated:** 2026-09-10  
**Authority:** [[00-CONSTITUTION|Constitution]] + [[REALITY|Reality Ledger]]  
**Source:** [[_ONTOLOGY/CAPABILITY_REGISTRY.yaml]] + [[_REGISTRIES/capabilities-by-sector.yaml]]
