# Canonical Definition: Bases in Company Brain

**Date:** 2026-09-22  
**Status:** AUTHORITATIVE DEFINITION  
**Authority:** Core architecture decision  
**Purpose:** Eliminate "Bases" ambiguity; establish unified schema for 35 domain-level knowledge and operating systems

---

## Definition

**Base** = A governed knowledge-and-operating domain.

A Base is **NOT** synonymous with:
- ❌ Supabase (infrastructure)
- ❌ PostgreSQL (data store)
- ❌ Neo4j (graph store)
- ❌ Qdrant (vector store)
- ❌ Docker (runtime environment)
- ❌ a physical location
- ❌ a generic knowledge base

Those are **infrastructure or storage components** that may support a Base.

---

## Base Hierarchy

```
Base
  ↓
Sector (economic classification)
  ↓
Industry / Market
  ↓
Venture (company/business/product)
  ↓
Product / Service
  ↓
Customer / Partner
  ↓
Workflow
  ↓
Transaction
  ↓
Revenue
```

---

## Standard Base Schema

Every Base follows this architecture (comparable, queryable):

```
BASE-XXX: [Name]
│
├── Identity
│   ├── Base ID
│   ├── Name
│   ├── Description
│   ├── Owner
│   └── Status
│
├── Ontology
│   ├── Entities
│   ├── Relationships
│   └── Classifications
│
├── Knowledge
│   ├── Concepts
│   ├── Sources
│   ├── Documents
│   ├── Research
│   └── Evidence
│
├── Market
│   ├── Customers
│   ├── Competitors
│   ├── Suppliers
│   ├── Partners
│   └── Opportunities
│
├── Ventures
│   ├── Companies
│   ├── Products
│   ├── Services
│   └── Revenue Models
│
├── Operations
│   ├── Processes
│   ├── SOPs
│   ├── Workflows
│   └── Metrics
│
├── Technology
│   ├── Repositories
│   ├── Tools
│   ├── MCPs
│   └── Integrations
│
├── Agents
│   ├── Agents
│   ├── Skills
│   ├── Prompts
│   └── Policies
│
├── Decisions
│   ├── Strategic
│   ├── Operational
│   ├── Financial
│   └── Technical
│
├── Experiments
│   ├── Hypotheses
│   ├── Results
│   └── Learnings
│
└── Outputs
    ├── Reports
    ├── Plans
    └── Revenue Actions
```

---

## The 35 Bases (Sector-Mapped)

```
BASE-001 → Agriculture
BASE-002 → Construction
BASE-003 → Energy
BASE-004 → Finance
BASE-005 → Financial Services
BASE-006 → Healthcare
BASE-007 → Insurance
BASE-008 → Legal
BASE-009 → Logistics
BASE-010 → Manufacturing
BASE-011 → Mining & Resources
BASE-012 → Real Estate
BASE-013 → Retail & E-Commerce
BASE-014 → Staffing & HR
BASE-015 → Technology & Software
BASE-016 → Telecommunications
BASE-017 → Transportation
BASE-018 → Utilities
BASE-019 → Education
BASE-020 → Entertainment & Media
BASE-021 → Food & Beverage
BASE-022 → Government & Defense
BASE-023 → Hospitality & Tourism
BASE-024 → Industrial Services
BASE-025 → Investment & Venture Capital
BASE-026 → Logistics & Supply Chain
BASE-027 → Marketing & Advertising
BASE-028 → Pharmaceuticals & Biotech
BASE-029 → Professional Services
BASE-030 → Real Estate Investment
BASE-031 → Renewable Energy
BASE-032 → Artificial Intelligence & ML
BASE-033 → Blockchain & Crypto
BASE-034 → Digital Commerce
BASE-035 → Platform Ecosystems
BASE-036 → Other Emerging
```

---

## Terminology Clarity

| Term | Meaning | Examples |
|------|---------|----------|
| **Base** | Governed domain (knowledge + operations) | BASE-009: Logistics |
| **Knowledge Base** | Information within a Base | routes, delivery times, driver profiles |
| **Data Store** | Structured operational state | PostgreSQL, Supabase |
| **Graph Store** | Machine relationships | Neo4j (20,363 edges) |
| **Vector Store** | Semantic retrieval | Qdrant (17,236 vectors) |
| **Object Store** | Files, PDFs, images | S3, local files |
| **Operational System** | CRM, dispatch, accounting | Make.com, ClickUp |
| **Physical Base** | Office, warehouse, facility | Charlotte hub, NYC office |
| **Infrastructure Base** | Docker, server, runtime | Mac Studio, Vercel |
| **Sector** | Economic classification | Logistics, Real Estate, Finance |
| **Venture** | Actual company/business | LT-005 (Medical Courier) |
| **Agent Scope** | What agent knows/can do | Revenue Loop Agent → Pricing |

---

## Company Brain Architecture

```
COMPANY BRAIN
    │
    ├── Bases (35 domain systems)
    │     ├── Knowledge layer
    │     ├── Ventures layer
    │     ├── Operations layer
    │     ├── Agents layer
    │     ├── Technology layer
    │     ├── Research layer
    │     └── Revenue layer
    │
    ├── Knowledge Layers
    │     ├── Obsidian (personal/canonical)
    │     └── OpenKnowledge (collaborative)
    │
    ├── Data Stores
    │     ├── Neo4j (graph: 20,363 edges)
    │     ├── Qdrant (vectors: 17,236 embeddings)
    │     ├── PostgreSQL/Supabase (state)
    │     └── Object Store (files)
    │
    ├── Agents (318+ agents)
    │     ├── Read from Bases
    │     ├── Reason over Bases
    │     ├── Execute in Bases
    │     └── Measure in Bases
    │
    └── Outcomes
          ├── Actions
          ├── Results
          ├── Metrics
          ├── Decisions
          └── Memory (feeds back)
```

---

## Core Base Graph

```
                    BASE
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
      Sector       Market       Knowledge
        │            │            │
        ▼            ▼            ▼
     Industry    Customers     Sources
        │            │            │
        ▼            ▼            ▼
      Venture     Problems      Research
        │            │            │
        ▼            ▼            ▼
     Product      Workflow      Insight
        │            │            │
        └────────────┼────────────┘
                     ▼
                   AGENT
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
      Skill         Tool         MCP
        │            │            │
        └────────────┼────────────┘
                     ▼
                  ACTION
                     │
                     ▼
                  RESULT
                     │
                     ▼
                  METRIC
                     │
                     ▼
                 DECISION
                     │
                     ▼
                  MEMORY
```

---

## Base-to-Graph Mapping (Neo4j)

Every Base instantiates these node types:

```cypher
// Identity
CREATE (base:Base {id: "BASE-009", name: "Logistics", status: "active"})

// Entities within Base
CREATE (venture:Venture {id: "LT-005", name: "Medical Courier"})
CREATE (base)-[:CONTAINS_VENTURE]->(venture)

// Knowledge
CREATE (concept:Concept {id: "CON-001", title: "Dispatch Routing"})
CREATE (base)-[:CONTAINS_CONCEPT]->(concept)

// Agents authorized for this Base
CREATE (agent:Agent {id: "AGENT-231", name: "Logistics Dispatch Agent"})
CREATE (base)-[:GOVERNED_BY_AGENT]->(agent)

// Capabilities
CREATE (capability:Capability {id: "CAP-087", name: "Real-time Tracking"})
CREATE (base)-[:REQUIRES_CAPABILITY]->(capability)

// Workflows
CREATE (workflow:Workflow {id: "FLOW-031", name: "Order to Delivery"})
CREATE (base)-[:ORCHESTRATES_WORKFLOW]->(workflow)

// Revenue
CREATE (revenue:Revenue {id: "REV-009", stream: "Delivery Fees"})
CREATE (base)-[:GENERATES_REVENUE]->(revenue)
```

---

## Implementation Implications

### For Obsidian Vault
Each Base gets a wiki folder structure:
```
BASES/
  BASE-001-Agriculture/
    _base.md (frontmatter + identity)
    knowledge.md
    ventures.md
    agents.md
    decisions.md
    ...
  BASE-002-Construction/
    ...
  ...
  BASE-035-Platforms/
```

### For OpenKnowledge
Bases can be collaborative domains where researchers ingest sources per Base:
```
OpenKnowledge/
  Bases/
    Logistics/
      market-research.md
      competitor-analysis.md
      regulatory-landscape.md
      ...
    Real Estate/
      ...
```

### For Neo4j
Base queries return comprehensive domain snapshots:
```cypher
// "Show me everything in the Logistics Base"
MATCH (base:Base {id: "BASE-009"})
OPTIONAL MATCH (base)-[*1..3]->(node)
RETURN base, COLLECT(node) as domain_entities

// "What agents operate in Logistics?"
MATCH (base:Base {id: "BASE-009"})<-[:GOVERNS_BASE]-(agent)
RETURN agent, agent.capabilities

// "What's the revenue for Logistics ventures?"
MATCH (base:Base {id: "BASE-009"})-[:CONTAINS_VENTURE]->(v)
  -[:GENERATES_REVENUE]->(r)
RETURN v, r.amount, r.frequency
```

### For Agents
Agents are scoped to Bases and inherit permissions:
```
Agent (Revenue Loop)
  ├── Authorized Bases: [BASE-004, BASE-005, BASE-030]
  ├── Operations: Read ventures, calculate forecasts, approve pricing
  ├── Escalations: CP-021 (Revenue Control Plane)
  └── Knowledge: Revenue models per Base
```

---

## Instantiation Strategy

**Phase 1 (Sep 23-Oct 6):** Define 3 Bases
- BASE-009 (Logistics) — LT-005, LT-011 active
- BASE-012 (Real Estate) — RE-001 demo-ready
- BASE-014 (Staffing) — OPS-001 revenue-ready

**Phase 2 (Oct 7-Oct 31):** Build agentic instantiation pipeline
- 15-min units per Base component
- Eval-first: capability test + regression test per unit
- Model routing: Haiku (boilerplate), Sonnet (entity definitions), Opus (graph validation)
- Measure: Base completeness (ontology ✅, knowledge ✅, agents ✅, outcomes ✅)

**Phase 3 (Nov 1-30):** Scale to 12 Bases
- Parallel instantiation via agents
- Neo4j consistency validation
- Base-to-Base relationship mapping

**Phase 4 (Dec 1-31):** Complete 35 Bases
- Full Company Brain operationalization
- Cross-Base revenue attribution
- Integrated agent coordination

---

## Key Insight

**The objective: Connect knowledge to execution to outcomes.**

- Obsidian/OpenKnowledge **capture knowledge**
- Bases **organize and bound that knowledge**
- Neo4j **connects Bases into a graph**
- Agents **operationalize across Bases**
- Results **feed back as memory**

Therefore: **When referring to "Bases" in Company Brain, always interpret as domain-level knowledge-and-operating systems, not database infrastructure.**

---

**Authority:** User decision (Sep 22, 2026)  
**Last Updated:** 2026-09-22  
**Next:** Create BASE-INSTANTIATION-PLAN.md with agentic engineering approach

---

## Control Base Reference

This document is mapped to [[B100|Control Base]] in the Company Brain.

**Wiki Link:** [[CBP_REGISTRY|_REGISTRIES/CANONICAL/CBP_REGISTRY.yaml#B100]]