---
id: DOC-ONT-MASTER-001
title: 45 Core Ontologies Master Architecture
aliases: ["45-ONTOLOGIES", "Master-Ontology-Stack", "Ontology-Crosswalk", "Core-Ontologies"]
tags: [ontology, architecture, knowledge-graph, master-stack, neo4j]
status: ACTIVE
updated: 2026-09-06
---

[[00-CONSTITUTION]] | [[07-ONTOLOGY]] | [[08-KNOWLEDGE-GRAPH]] | [[STARTHERE]] | [[INDEX]]

# 45 Core Ontologies Master Architecture

> **Authority:** System Architecture & Infrastructure Control Plane (CP-027)  
> **Master Registry:** [[_ONTOLOGY/45_ONTOLOGIES_REGISTRY.yaml]]  
> **Scope:** Ground-truth ontological tissue connecting all 50 Company Brain domains, canonical registries, and Neo4j relational graph.

---

## 1. Architectural Model

Company Brain does not operate on disconnected silos. The ecosystem is grounded in **45 Unified Ontological Domains**:
- **25 Foundational Ontologies (`ONT-001` to `ONT-025`):** Describe **WHAT EXISTS** (Entities, Capital, Infrastructure, Software, Products).
- **20 Operational Ontologies (`OPS-026` to `OPS-045`):** Describe **WHAT HAPPENS** (Events, Decisions, Workflows, Relationships, Evidence).

```text
                                 COMPANY BRAIN
                                      │
                   ┌──────────────────┼──────────────────┐
                   ↓                  ↓                  ↓
                ECONOMY           TECHNOLOGY          CAPITAL
               (ONT-001)          (ONT-004)          (ONT-017)
                   │                  │                  │
                Markets          Capabilities         Funding
               (ONT-016)          (ONT-005)              │
                   │                  │                Grants
               Companies           Software              │
               (ONT-002)          (ONT-006)            Equity
                   │                  │                  │
                Ventures            Agents               │
               (ONT-003)          (ONT-008)              │
                   │                  │                  │
                   └───────────┬──────┴──────┬───────────┘
                               ↓             ↓
                            PEOPLE        PROCESSES
                           (ONT-012)      (ONT-013)
                               │             │
                               └──────┬──────┘
                                      ↓
                                    DATA (ONT-009)
                                      ↓
                                  KNOWLEDGE (ONT-010)
                                      ↓
                                  DECISION (OPS-027)
                                      ↓
                                   ACTION (OPS-035)
                                      ↓
                                   EVENT (OPS-026)
                                      ↓
                                  METRICS (ONT-025)
                                      ↓
                                 PERFORMANCE (OPS-045)
                                      ↓
                                  FEEDBACK (OPS-040)
                                      │
                                      └────────→ RE-INGESTION (Neo4j / Qdrant)
```

---

## 2. The Relationship Ontology (`OPS-039`) — The Hyper-Connective Tissue

The real power of Company Brain is not merely knowing that entities exist. It is navigating the **hyper-connective relational edges**:

> **Venture A** (`ONT-003`)  
> ├── **operates_as** → Operating Company (`ONT-002`)  
> ├── **targets** → Market & ICP (`ONT-015`, `ONT-016`)  
> ├── **requires** → Capabilities (`ONT-005`)  
> ├── **implemented_by** → Software Repositories (`ONT-006`)  
> ├── **automated_by** → Agent Swarms (`ONT-008`)  
> ├── **runs_on** → Local Mesh Infrastructure (`ONT-007`)  
> ├── **funded_by** → Capital & Grants (`ONT-017`)  
> ├── **measured_by** → Financial & Operational Metrics (`ONT-018`, `ONT-025`)  
> └── **governed_by** → Operating Policies & Constitution (`OPS-028`, `OPS-044`)

---

## 3. The Complete 45 Ontology Stack Crosswalk

| ID | Ontology Name | Category | Primary Domain Gateway | Ground-Truth File / Schema | Tags |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [[07-ONTOLOGY/domains/ONT-001|ONT-001]] | **Economic Ontology** | FOUNDATIONAL | [[00-CONSTITUTION]] | [[00-CONSTITUTION/SECTOR-TAXONOMY-MASTER.md|SECTOR-TAXONOMY-MASTER.md]] | `ontology`, `foundational`, `economic` |
| [[07-ONTOLOGY/domains/ONT-002|ONT-002]] | **Company Ontology** | FOUNDATIONAL | [[01-IDENTITY]] | [[01-IDENTITY/01-IDENTITY.md|01-IDENTITY.md]] | `ontology`, `foundational`, `company` |
| [[07-ONTOLOGY/domains/ONT-003|ONT-003]] | **Venture Ontology** | FOUNDATIONAL | [[23-VENTURES]] | [[23-VENTURES/23-VENTURES.md|23-VENTURES.md]] | `ontology`, `foundational`, `venture` |
| [[07-ONTOLOGY/domains/ONT-004|ONT-004]] | **Technology Ontology** | FOUNDATIONAL | [[24-TECHNOLOGY]] | [[24-TECHNOLOGY/24-TECHNOLOGY.md|24-TECHNOLOGY.md]] | `ontology`, `foundational`, `technology` |
| [[07-ONTOLOGY/domains/ONT-005|ONT-005]] | **Capability Ontology** | FOUNDATIONAL | [[14-CAPABILITIES]] | [[14-CAPABILITIES/14-CAPABILITIES.md|14-CAPABILITIES.md]] | `ontology`, `foundational`, `capability` |
| [[07-ONTOLOGY/domains/ONT-006|ONT-006]] | **Software Ontology** | FOUNDATIONAL | [[13-REPOSITORIES]] | [[13-REPOSITORIES/13-REPOSITORIES.md|13-REPOSITORIES.md]] | `ontology`, `foundational`, `software` |
| [[07-ONTOLOGY/domains/ONT-007|ONT-007]] | **Infrastructure Ontology** | FOUNDATIONAL | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE.md|INFRASTRUCTURE.md]] | `ontology`, `foundational`, `infrastructure` |
| [[07-ONTOLOGY/domains/ONT-008|ONT-008]] | **AI & Agent Ontology** | FOUNDATIONAL | [[16-AGENTS]] | [[16-AGENTS/16-AGENTS.md|16-AGENTS.md]] | `ontology`, `foundational`, `ai` |
| [[07-ONTOLOGY/domains/ONT-009|ONT-009]] | **Data Ontology** | FOUNDATIONAL | [[04-DATA]] | [[04-DATA/04-DATA.md|04-DATA.md]] | `ontology`, `foundational`, `data` |
| [[07-ONTOLOGY/domains/ONT-010|ONT-010]] | **Knowledge Ontology** | FOUNDATIONAL | [[09-KNOWLEDGE]] | [[09-KNOWLEDGE/09-KNOWLEDGE.md|09-KNOWLEDGE.md]] | `ontology`, `foundational`, `knowledge` |
| [[07-ONTOLOGY/domains/ONT-011|ONT-011]] | **Organization Ontology** | FOUNDATIONAL | [[06-TEAMS]] | [[06-TEAMS/06-TEAMS.md|06-TEAMS.md]] | `ontology`, `foundational`, `organization` |
| [[07-ONTOLOGY/domains/ONT-012|ONT-012]] | **People Ontology** | FOUNDATIONAL | [[05-PEOPLE]] | [[05-PEOPLE/05-PEOPLE.md|05-PEOPLE.md]] | `ontology`, `foundational`, `people` |
| [[07-ONTOLOGY/domains/ONT-013|ONT-013]] | **Process Ontology** | FOUNDATIONAL | [[29-OPERATIONS]] | [[29-OPERATIONS/29-OPERATIONS.md|29-OPERATIONS.md]] | `ontology`, `foundational`, `process` |
| [[07-ONTOLOGY/domains/ONT-014|ONT-014]] | **Product Ontology** | FOUNDATIONAL | [[28-PRODUCT]] | [[28-PRODUCT/28-PRODUCT.md|28-PRODUCT.md]] | `ontology`, `foundational`, `product` |
| [[07-ONTOLOGY/domains/ONT-015|ONT-015]] | **Customer Ontology** | FOUNDATIONAL | [[27-CUSTOMERS]] | [[27-CUSTOMERS/27-CUSTOMERS.md|27-CUSTOMERS.md]] | `ontology`, `foundational`, `customer` |
| [[07-ONTOLOGY/domains/ONT-016|ONT-016]] | **Market Ontology** | FOUNDATIONAL | [[26-MARKETING]] | [[26-MARKETING/26-MARKETING.md|26-MARKETING.md]] | `ontology`, `foundational`, `market` |
| [[07-ONTOLOGY/domains/ONT-017|ONT-017]] | **Capital Ontology** | FOUNDATIONAL | [[08-FINANCIAL]] | [[08-FINANCIAL/08-FINANCIAL.md|08-FINANCIAL.md]] | `ontology`, `foundational`, `capital` |
| [[07-ONTOLOGY/domains/ONT-018|ONT-018]] | **Financial Ontology** | FOUNDATIONAL | [[24-FINANCE]] | [[24-FINANCE/24-FINANCE.md|24-FINANCE.md]] | `ontology`, `foundational`, `financial` |
| [[07-ONTOLOGY/domains/ONT-019|ONT-019]] | **Legal Ontology** | FOUNDATIONAL | [[31-LEGAL]] | [[31-LEGAL/31-LEGAL.md|31-LEGAL.md]] | `ontology`, `foundational`, `legal` |
| [[07-ONTOLOGY/domains/ONT-020|ONT-020]] | **Compliance Ontology** | FOUNDATIONAL | [[33-COMPLIANCE]] | [[33-COMPLIANCE/33-COMPLIANCE.md|33-COMPLIANCE.md]] | `ontology`, `foundational`, `compliance` |
| [[07-ONTOLOGY/domains/ONT-021|ONT-021]] | **Partner Ontology** | FOUNDATIONAL | [[36-PARTNERS]] | [[36-PARTNERS/36-PARTNERS.md|36-PARTNERS.md]] | `ontology`, `foundational`, `partner` |
| [[07-ONTOLOGY/domains/ONT-022|ONT-022]] | **Asset Ontology** | FOUNDATIONAL | [[35-ASSETS]] | [[35-ASSETS/35-ASSETS.md|35-ASSETS.md]] | `ontology`, `foundational`, `asset` |
| [[07-ONTOLOGY/domains/ONT-023|ONT-023]] | **Location Ontology** | FOUNDATIONAL | [[00-CONSTITUTION]] | [[00-CONSTITUTION/00-CONSTITUTION.md|00-CONSTITUTION.md]] | `ontology`, `foundational`, `location` |
| [[07-ONTOLOGY/domains/ONT-024|ONT-024]] | **Risk Ontology** | FOUNDATIONAL | [[34-RISK]] | [[34-RISK/34-RISK.md|34-RISK.md]] | `ontology`, `foundational`, `risk` |
| [[07-ONTOLOGY/domains/ONT-025|ONT-025]] | **Metrics Ontology** | FOUNDATIONAL | [[40-METRICS]] | [[40-METRICS/40-METRICS.md|40-METRICS.md]] | `ontology`, `foundational`, `metrics` |
| [[07-ONTOLOGY/domains/OPS-026|OPS-026]] | **Event Ontology** | OPERATIONAL | [[11-LOOP-ENGINEERING]] | [[11-LOOP-ENGINEERING/11-LOOP-ENGINEERING.md|11-LOOP-ENGINEERING.md]] | `ontology`, `operational`, `event` |
| [[07-ONTOLOGY/domains/OPS-027|OPS-027]] | **Decision Ontology** | OPERATIONAL | [[20-DECISIONS]] | [[20-DECISIONS/20-DECISIONS.md|20-DECISIONS.md]] | `ontology`, `operational`, `decision` |
| [[07-ONTOLOGY/domains/OPS-028|OPS-028]] | **Policy Ontology** | OPERATIONAL | [[21-POLICY]] | [[21-POLICY/21-POLICY.md|21-POLICY.md]] | `ontology`, `operational`, `policy` |
| [[07-ONTOLOGY/domains/OPS-029|OPS-029]] | **Permission Ontology** | OPERATIONAL | [[32-SECURITY]] | [[32-SECURITY/32-SECURITY.md|32-SECURITY.md]] | `ontology`, `operational`, `permission` |
| [[07-ONTOLOGY/domains/OPS-030|OPS-030]] | **Identity Ontology** | OPERATIONAL | [[01-IDENTITY]] | [[01-IDENTITY/01-IDENTITY.md|01-IDENTITY.md]] | `ontology`, `operational`, `identity` |
| [[07-ONTOLOGY/domains/OPS-031|OPS-031]] | **Transaction Ontology** | OPERATIONAL | [[24-FINANCE]] | [[24-FINANCE/24-FINANCE.md|24-FINANCE.md]] | `ontology`, `operational`, `transaction` |
| [[07-ONTOLOGY/domains/OPS-032|OPS-032]] | **Contract Ontology** | OPERATIONAL | [[31-LEGAL]] | [[31-LEGAL/31-LEGAL.md|31-LEGAL.md]] | `ontology`, `operational`, `contract` |
| [[07-ONTOLOGY/domains/OPS-033|OPS-033]] | **Opportunity Ontology** | OPERATIONAL | [[38-OPPORTUNITIES]] | [[38-OPPORTUNITIES/38-OPPORTUNITIES.md|38-OPPORTUNITIES.md]] | `ontology`, `operational`, `opportunity` |
| [[07-ONTOLOGY/domains/OPS-034|OPS-034]] | **Project Ontology** | OPERATIONAL | [[22-EXECUTION]] | [[22-EXECUTION/22-EXECUTION.md|22-EXECUTION.md]] | `ontology`, `operational`, `project` |
| [[07-ONTOLOGY/domains/OPS-035|OPS-035]] | **Task Ontology** | OPERATIONAL | [[48-AUTOMATION]] | [[48-AUTOMATION/48-AUTOMATION.md|48-AUTOMATION.md]] | `ontology`, `operational`, `task` |
| [[07-ONTOLOGY/domains/OPS-036|OPS-036]] | **Resource Ontology** | OPERATIONAL | [[35-ASSETS]] | [[35-ASSETS/35-ASSETS.md|35-ASSETS.md]] | `ontology`, `operational`, `resource` |
| [[07-ONTOLOGY/domains/OPS-037|OPS-037]] | **Workflow Ontology** | OPERATIONAL | [[48-AUTOMATION]] | [[48-AUTOMATION/48-AUTOMATION.md|48-AUTOMATION.md]] | `ontology`, `operational`, `workflow` |
| [[07-ONTOLOGY/domains/OPS-038|OPS-038]] | **Dependency Ontology** | OPERATIONAL | [[13-REPOSITORIES]] | [[_REGISTRIES/CANONICAL/OWNED_REPO_DEPENDENCIES.json|OWNED_REPO_DEPENDENCIES.json]] | `ontology`, `operational`, `dependency` |
| [[07-ONTOLOGY/domains/OPS-039|OPS-039]] | **Relationship Ontology** | OPERATIONAL | [[08-KNOWLEDGE-GRAPH]] | [[_ONTOLOGY/RELATIONSHIPS.yaml|RELATIONSHIPS.yaml]] | `ontology`, `operational`, `relationship` |
| [[07-ONTOLOGY/domains/OPS-040|OPS-040]] | **Evidence & Provenance Ontology** | OPERATIONAL | [[EVIDENCE]] | [[EVIDENCE.md|EVIDENCE.md]] | `ontology`, `operational`, `evidence` |
| [[07-ONTOLOGY/domains/OPS-041|OPS-041]] | **Time Ontology** | OPERATIONAL | [[44-LEARNING]] | [[44-LEARNING/44-LEARNING.md|44-LEARNING.md]] | `ontology`, `operational`, `time` |
| [[07-ONTOLOGY/domains/OPS-042|OPS-042]] | **Version Ontology** | OPERATIONAL | [[45-EVOLUTION]] | [[45-EVOLUTION/45-EVOLUTION.md|45-EVOLUTION.md]] | `ontology`, `operational`, `version` |
| [[07-ONTOLOGY/domains/OPS-043|OPS-043]] | **Lifecycle Ontology** | OPERATIONAL | [[07-ONTOLOGY]] | [[_ONTOLOGY/STATUS_LIFECYCLE.md|STATUS_LIFECYCLE.md]] | `ontology`, `operational`, `lifecycle` |
| [[07-ONTOLOGY/domains/OPS-044|OPS-044]] | **Governance Ontology** | OPERATIONAL | [[46-GOVERNANCE]] | [[46-GOVERNANCE/46-GOVERNANCE.md|46-GOVERNANCE.md]] | `ontology`, `operational`, `governance` |
| [[07-ONTOLOGY/domains/OPS-045|OPS-045]] | **Performance Ontology** | OPERATIONAL | [[42-EVALUATION]] | [[42-EVALUATION/42-EVALUATION.md|42-EVALUATION.md]] | `ontology`, `operational`, `performance` |

---

## 4. Machine Verification in Neo4j

All 45 ontologies and their primary nodes are queryable directly in the live Neo4j database (`bolt://100.87.214.70:7687`):

```cypher
// Trace hyper-connective tissue for any venture across the ontologies
MATCH (v:Venture)-[op:OPERATES]->(r:Repository)
OPTIONAL MATCH (r)-[imp:IMPLEMENTS]->(c:Capability)
OPTIONAL MATCH (v)-[dep:DEPLOYS]->(s:Site)
RETURN v.id as Venture, r.name as Repo, collect(c.name) as Capabilities, collect(s.url) as Sites
```
