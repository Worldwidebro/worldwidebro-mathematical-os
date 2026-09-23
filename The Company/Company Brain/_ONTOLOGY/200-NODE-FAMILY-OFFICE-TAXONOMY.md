# 200-Node Master Taxonomy for Family Office Ecosystem

**Date:** 2026-09-23  
**Purpose:** Schema layer for Company Brain (types) + instances (actual entities)  
**Integration:** Neo4j ontology + Wiki links + Supabase records  
**Authority:** Family office architecture + billionaire-scale estate design

---

## The Key Distinction: Schema vs. Instance

### 200 Node Types (Schema Layer)
These are **entity types** that define what kinds of vehicles can exist:
- Trusts, LLCs, Corps, Funds, SPVs, Foundations, etc.
- Each type has rules, tax treatment, governance, purpose

### 150 Actual Entities (Instance Layer)
These are the **specific entities** in your estate that are instances of these types:
- "Family Trust" (instance of node 21: Revocable Living Trust)
- "OpCo-009" (instance of node 81: Operating Company)
- "Property LLC - Denver" (instance of node 112: Property LLC)

### 789 Ventures (Sub-Instance Layer)
These are companies/businesses operated by OpCos/Holdings:
- "LT-005 Medical Courier" (operated by OpCo-009)
- "RE-001 Real Estate" (operated by OpCo-012)

---

## How the 200 Nodes Map to Company Brain

### Neo4j Graph Structure

```cypher
// NODE TYPE LAYER (Ontology - 200 nodes)
CREATE (entity_type:EntityType {
  id: "21",
  name: "Revocable Living Trust",
  category: "Estate & Trust Architecture",
  tax_treatment: "Grantor trust (disregarded)",
  governance_level: "High autonomy",
  typical_assets: ["Real Estate", "Investment Securities", "Operating Companies"],
  governance_rules: ["Amendable", "Revocable", "Privacy advantage"],
  wiki_link: "entity-type-21-revocable-living-trust"
})

// INSTANCE LAYER (Actual entities - ~150 nodes)
CREATE (family_trust:FamilyTrust {
  id: "ENT-001",
  name: "Family Trust",
  type: "entity-type-21",  // Links to EntityType
  created: "2000-01-01",
  tax_id: "XX-XXXXXXXXX",
  status: "Active",
  wiki_link: "ent-001-family-trust"
})

// OWNERSHIP RELATIONSHIP
CREATE (family_trust)-[:INSTANCE_OF]->(entity_type)
CREATE (principal)-[:TRUSTS_HELD_BY]->(family_trust)

// OPERATES RELATIONSHIP
CREATE (family_trust)-[:OWNS_OPCO]->(opco_009)
CREATE (opco_009)-[:OPERATES_VENTURE]->(lt_005)
```

### Wiki Link Hierarchy

```
[[200-NODE-FAMILY-OFFICE-TAXONOMY]] (this file, master ontology)
  ├─ [[ENTITY-TYPE-21-REVOCABLE-LIVING-TRUST]] (type definition)
  │   └─ [[ENT-001-FAMILY-TRUST]] (our actual instance)
  │       ├─ [[ENT-OpCo-009]] (OpCo owned by Family Trust)
  │       │   └─ [[LT-005-MEDICAL-COURIER]] (venture in OpCo)
  │       └─ [[ENT-OpCo-012]] (OpCo owned by Family Trust)
  │           └─ [[RE-001-REAL-ESTATE]] (venture in OpCo)
  │
  ├─ [[ENTITY-TYPE-46-SINGLE-FAMILY-OFFICE]] (type definition)
  │   └─ [[ENT-002-FAMILY-OFFICE]] (our actual instance)
  │
  ├─ [[ENTITY-TYPE-61-MASTER-HOLDING-COMPANY]] (type definition)
  │   └─ [[ENT-003-HOLDING-COMPANY]] (our actual instance)
  │
  └─ [[ENTITY-TYPE-81-OPERATING-COMPANY]] (type definition, shared with 36 OpCos)
      ├─ [[ENT-OpCo-001]] (Agriculture OpCo)
      ├─ [[ENT-OpCo-009]] (Logistics OpCo)
      └─ ... (34 more OpCos)
```

---

## The Complete 200-Node Taxonomy (Referenced in Company Brain)

### Group 1: Family & Governance (Nodes 1-20)

| Node | Entity Type | Purpose | Wiki Link | Our Instance |
|------|-------------|---------|-----------|---|
| 1 | Family Governance Council | Strategic oversight | [[ENTITY-TYPE-1]] | [[ENT-001-FGC]] |
| 2 | Family Constitution | Governance document | [[ENTITY-TYPE-2]] | Internal doc |
| 3 | Family Office Board | Executive governance | [[ENTITY-TYPE-3]] | [[ENT-001-FOB]] |
| 4 | Family Investment Committee | Capital allocation | [[ENTITY-TYPE-4]] | [[ENT-001-FIC]] |
| 5 | Family Philanthropy Committee | Giving strategy | [[ENTITY-TYPE-5]] | Planned |
| ... | ... | ... | ... | ... |
| 20 | Family Governance Trust | Legal governance vehicle | [[ENTITY-TYPE-20]] | [[ENT-001-FGT]] |

### Group 2: Estate & Trust Architecture (Nodes 21-45)

| Node | Entity Type | Purpose | Our Instance |
|------|-------------|---------|---|
| 21 | Revocable Living Trust | Primary estate vehicle | [[ENT-001-FAMILY-TRUST]] ✅ |
| 22 | Irrevocable Trust | Tax planning | (Planned) |
| 23 | Dynasty Trust | Generational wealth | (Planned) |
| ... | ... | ... | ... |
| 45 | Estate Administration Trust | Succession planning | (Planned) |

### Group 3: Family Office (Nodes 46-60)

| Node | Entity Type | Purpose | Our Instance |
|------|-------------|---------|---|
| 46 | Single-Family Office | Operations hub | [[ENT-002-FAMILY-OFFICE]] ✅ |
| 47 | Multi-Family Office | (Not applicable) | N/A |
| 48 | Family Office Management Company | Admin/operations | [[ENT-002-FOA]] ✅ |
| ... | ... | ... | ... |
| 60 | Family Office Technology Company | Tech infrastructure | Planned |

### Group 4: Holding Companies (Nodes 61-80)

| Node | Entity Type | Purpose | Our Instance |
|------|-------------|---------|---|
| 61 | Master Holding Company | Top-level consolidation | [[ENT-003-MASTER-HOLDCO]] ✅ |
| 62 | Family Holding Company | Secondary consolidation | [[ENT-003-FAMILY-HOLDCO]] ✅ |
| 63-65 | Various Holdcos | Sector specialization | [[ENT-003-TECH-HOLDCO]], etc. |
| ... | ... | ... | ... |
| 80 | Strategic Assets Holding Company | Opportunistic | Planned |

### Group 5: Operating Companies (Nodes 81-110)

| Node | Entity Type | Purpose | Our Instance | Ventures |
|------|-------------|---------|---|---|
| 81 | Operating Company | Generic ops | [[ENT-OpCo-001]] ... [[ENT-OpCo-036]] | ✅ (36 OpCos, 789 ventures) |
| 82 | Management Company | Shared services | [[ENT-003-MGMT]] | Internal |
| ... | ... | ... | ... | ... |
| 110 | Research Company | R&D/innovation | (Planned) | (Planned ventures) |

### Group 6: Real Estate & Development (Nodes 111-135)

| Node | Entity Type | Purpose | Our Instances |
|------|-------------|---------|---|
| 111 | Real Estate Holding Company | RE portfolio consolidation | [[ENT-RE-HOLDCO]] |
| 112 | Property LLC | Single/multi-property | [[ENT-PROPERTY-DENVER]], [[ENT-PROPERTY-NYC]], etc. |
| ... | ... | ... | ... |
| 135 | Real Estate Acquisition SPV | Deal structure | [[ENT-SPV-LAND-DEAL-2026]] |

### Group 7: Investment & Capital Vehicles (Nodes 136-155)

| Node | Entity Type | Purpose | Our Instances |
|------|-------------|---------|---|
| 136 | Investment Holding Company | Investment portfolio | [[ENT-INVESTMENT-HOLDCO]] |
| 139 | Private Equity Fund | PE investments | [[ENT-PE-FUND-2024]] |
| 150 | Family Investment Fund | Co-investments | [[ENT-FAMILY-INVESTMENT-FUND]] |
| ... | ... | ... | ... |

### Group 8: Asset & IP Entities (Nodes 156-170)

| Node | Entity Type | Purpose | Our Instances |
|------|-------------|---------|---|
| 156 | Intellectual Property Holding Company | IP portfolio | [[ENT-IP-HOLDCO]] |
| 160 | Software IP Company | Software assets | [[ENT-SOFTWARE-IP]] |
| 168 | Music Rights Company | Royalty management | [[ENT-MUSIC-RIGHTS]] (if applicable) |
| ... | ... | ... | ... |

### Group 9: Major Physical Assets (Nodes 171-180)

| Node | Entity Type | Purpose | Our Instances |
|------|-------------|---------|---|
| 172 | Aircraft Management Company | Aviation ops | [[ENT-AIRCRAFT-MGMT]] (if applicable) |
| 175 | Vehicle Holding Company | Fleet management | [[ENT-VEHICLE-HOLDCO]] (if applicable) |
| 180 | Art & Collectibles Holding Company | Alternative assets | [[ENT-COLLECTIBLES-HOLDCO]] (if applicable) |

### Group 10: Philanthropy & Social Impact (Nodes 181-190)

| Node | Entity Type | Purpose | Our Instances |
|------|-------------|---------|---|
| 181 | Private Foundation | Charitable giving | (Planned) |
| 185 | Nonprofit Corporation | Mission-driven ops | (Planned) |
| 189 | Social Enterprise | Social impact | (Planned) |

### Group 11: Risk, Succession & Special (Nodes 191-200)

| Node | Entity Type | Purpose | Our Instances |
|------|-------------|---------|---|
| 191 | Captive Insurance Company | Self-insurance | (Planned) |
| 194 | Succession Planning Entity | Next-gen transition | (Planned) |
| 196 | Employee Stock Ownership Plan | Staff alignment | (Planned for OpCos) |

---

## Neo4j Ontology Structure

### Node Types (Schema)

```cypher
// EntityType nodes (200 total, representing the schema)
CREATE (node_21:EntityType {
  type_id: 21,
  type_name: "Revocable Living Trust",
  category: "Estate & Trust Architecture",
  group: 2,
  description: "Primary estate vehicle, revocable, privacy advantage, grantor trust treatment",
  tax_treatment: "Grantor trust (disregarded for tax purposes)",
  governance_level: "High autonomy",
  typical_use_cases: ["Asset consolidation", "Privacy", "Succession planning"],
  wiki_link: "entity-type-21-revocable-living-trust",
  created: "2026-09-23"
})

// EntityInstance nodes (150-200+ actual entities, referencing types)
CREATE (ent_001:EntityInstance {
  entity_id: "ENT-001",
  entity_name: "Family Trust",
  type_id: 21,  // Revocable Living Trust
  created: "2000-01-01",
  status: "Active",
  tax_id: "XX-XXXXXXXXX",
  jurisdiction: "Delaware",
  assets_under_control: "$500M+",
  wiki_link: "ent-001-family-trust"
})

// Relationship: instance → type
CREATE (ent_001)-[:IS_INSTANCE_OF]->(node_21)

// Relationships between entities
CREATE (ent_001)-[:OWNS]->(ent_opco_009)
CREATE (ent_opco_009)-[:OPERATES]->(lt_005_venture)
CREATE (ent_opco_009)-[:GOVERNED_BY]->(cp_026)
CREATE (ent_opco_009)-[:IS_INSTANCE_OF]->(node_81)  // Operating Company
```

### Wiki Link Structure (Markdown)

```markdown
# 200-NODE MASTER TAXONOMY

## Groups

### Group 2: Estate & Trust Architecture (Nodes 21-45)

#### Node 21: Revocable Living Trust
[[ENTITY-TYPE-21-REVOCABLE-LIVING-TRUST]]

Description: Primary estate vehicle, typically holds all family assets

**Our Instance:** [[ENT-001-FAMILY-TRUST]]
- Created: 2000-01-01
- Assets: $500M+
- Owns: [[ENT-OpCo-001]] through [[ENT-OpCo-036]]

**Related:**
- Tax treatment: Grantor trust (disregarded)
- Governance: [[ENT-001-FGT]] (Family Governance Trust)
- Succession: [[ENT-001-SUCCESSION-PLAN]]
- Next generation: [[ENT-002-FAMILY-TRUST]] (planned)

**Ventures operated through OpCos:**
- [[LT-005-MEDICAL-COURIER]] (via OpCo-009)
- [[RE-001-REAL-ESTATE]] (via OpCo-012)
- [[OPS-001-STAFFING]] (via OpCo-014)
- ... (786 more ventures)

---

### Group 4: Holding Companies (Nodes 61-80)

#### Node 61: Master Holding Company
[[ENTITY-TYPE-61-MASTER-HOLDING-COMPANY]]

**Our Instance:** [[ENT-003-MASTER-HOLDCO]]
- Owns: [[ENT-003-FAMILY-HOLDCO]]
- Consolidates: All 36 OpCos
- Tax treatment: C-Corp (consolidation filer)

**OpCos controlled:**
- [[ENT-OpCo-001-AGRICULTURE]] through [[ENT-OpCo-036-EMERGING]]
```

---

## Company Brain Integration

### Nodes in Neo4j

```
Total Nodes: ~1,500+
├─ EntityType nodes: 200 (schema, permanent)
├─ EntityInstance nodes: 150-200 (actual entities)
├─ Base nodes: 35-36 (knowledge domains)
├─ Venture nodes: 789 (operating companies)
├─ Agent nodes: 318 (autonomous agents)
├─ ControlPlane nodes: 30+ (governance)
├─ Capability nodes: 300+ (skills/tools)
└─ Other: Metric, Decision, Financial nodes

Total Edges: 50,000+
├─ IS_INSTANCE_OF: 150-200 (entity → type)
├─ OWNS: ~150 (trust/holdco ownership)
├─ OPERATES: 36 (OpCo → ventures)
├─ GOVERNED_BY: 36+ (entity → control plane)
└─ ... (49,500+ more relationships)
```

### Wiki Link Mapping

```
Master Ontology
  [[200-NODE-FAMILY-OFFICE-TAXONOMY]]
    ├─ [[ENTITY-TYPE-21]] (Revocable Living Trust)
    │   └─ [[ENT-001]] (Family Trust instance)
    │       ├─ [[ENT-OpCo-009]] (Logistics OpCo)
    │       │   ├─ [[LT-005]] (Medical Courier venture)
    │       │   └─ [[LT-011]] (Dispatch venture)
    │       ├─ [[ENT-OpCo-012]] (Real Estate OpCo)
    │       │   └─ [[RE-001]] (Real Estate venture)
    │       └─ ... (34 more OpCos)
    │
    ├─ [[ENTITY-TYPE-81]] (Operating Company)
    │   └─ [[ENT-OpCo-001]] through [[ENT-OpCo-036]]
    │       └─ [[VENTURE-1]] through [[VENTURE-789]]
    │
    └─ [[ENTITY-TYPE-46]] (Single-Family Office)
        └─ [[ENT-002]] (Family Office instance)
```

### Supabase Tables

```sql
-- Schema layer
CREATE TABLE entity_types (
  type_id INT PRIMARY KEY,
  type_name VARCHAR,
  category VARCHAR,
  tax_treatment VARCHAR,
  governance_level VARCHAR,
  wiki_link VARCHAR,
  ...
);

-- Instance layer
CREATE TABLE entities (
  entity_id VARCHAR PRIMARY KEY,
  entity_name VARCHAR,
  type_id INT REFERENCES entity_types,
  created DATE,
  status VARCHAR,
  tax_id VARCHAR,
  assets_under_control DECIMAL,
  wiki_link VARCHAR,
  ...
);

-- Relationships
CREATE TABLE entity_relationships (
  source_entity_id VARCHAR REFERENCES entities,
  relationship_type VARCHAR,
  target_entity_id VARCHAR REFERENCES entities,
  ...
);

-- Operating companies (subset of entities)
CREATE TABLE opcos (
  opco_id VARCHAR PRIMARY KEY,
  entity_id VARCHAR REFERENCES entities,
  sector_id VARCHAR,
  base_id VARCHAR,
  venture_count INT,
  ...
);

-- Ventures (operated by OpCos)
CREATE TABLE ventures (
  venture_id VARCHAR PRIMARY KEY,
  venture_name VARCHAR,
  opco_id VARCHAR REFERENCES opcos,
  base_id VARCHAR,
  ...
);
```

---

## Query Examples: How Wiki Links → Neo4j → Company Brain

### Query 1: "Show me everything owned by Family Trust"
```cypher
MATCH (family_trust:EntityInstance {entity_id: "ENT-001"})
       -[:OWNS]->(opco)
       -[:OPERATES]->(venture)
RETURN family_trust, opco, venture
// Returns: Family Trust → 36 OpCos → 789 ventures
```

**Wiki path:** [[ENT-001-FAMILY-TRUST]] → [[ENT-OpCo-001]] → [[LT-005]]

### Query 2: "Show me all entities of type 'Operating Company'"
```cypher
MATCH (entity:EntityInstance)-[:IS_INSTANCE_OF]->(type:EntityType {type_id: 81})
RETURN entity, type
// Returns: 36 OpCo instances
```

**Wiki path:** [[ENTITY-TYPE-81-OPERATING-COMPANY]] → [[ENT-OpCo-001]] ... [[ENT-OpCo-036]]

### Query 3: "Show me entity types in the Holding Company group"
```cypher
MATCH (type:EntityType {group: 4})
RETURN type
// Returns: Nodes 61-80 (20 holding company types)
```

**Wiki path:** [[200-NODE-FAMILY-OFFICE-TAXONOMY]] → Nodes 61-80

---

## Current State (Sep 23, 2026)

### Schema (200 Nodes) - DEFINED
- ✅ All 200 entity types documented
- ✅ Wiki links created for each type
- ✅ Neo4j schema designed
- Status: **Ready to implement**

### Instances (150+ Entities) - PARTIALLY DEFINED
- ✅ Family Trust (ENT-001)
- ✅ Family Office (ENT-002)
- ✅ Master Holdco (ENT-003)
- ✅ 36 OpCos (ENT-OpCo-001 to ENT-OpCo-036)
- ✅ 789 Ventures (LT-005, OPS-001, RE-001, etc.)
- 🟡 Many other entities (LLCs, property companies, etc.) - To add
- Status: **In progress**

### Wiki Links - IN PROGRESS
- ✅ Master ontology file created
- ✅ 200 type links mapped
- ✅ 150+ instance links mapped
- 🟡 Full wiki structure to build out
- Status: **In progress, Phase 2**

### Neo4j Graph - DESIGNED, NOT YET WIRED
- ✅ Ontology schema designed
- ✅ Query patterns designed
- ❌ Nodes not yet created in Neo4j
- ❌ Relationships not yet created
- Status: **Ready for Phase 2 implementation**

---

## Next Steps (Phase 2, Oct 2026)

1. **Create EntityType nodes in Neo4j** (200 nodes)
   - Populate type_id, type_name, category, tax_treatment, etc.
   - Link to wiki_link URLs

2. **Create EntityInstance nodes** (150-200 nodes)
   - Family Trust, OpCos, property LLCs, investment vehicles, etc.
   - Link each to its EntityType (IS_INSTANCE_OF relationship)

3. **Build wiki link structure**
   - Create markdown files for each type + instance
   - Wire up [[TYPE]] and [[INSTANCE]] links

4. **Populate Supabase tables**
   - Mirror Neo4j data to Supabase for VEX queries
   - Ensure real-time sync

5. **VEX integration**
   - Query by entity type ("Show all Trusts")
   - Query by entity instance ("Show Family Trust assets")
   - Navigate via wiki links

---

## Summary: 200 Nodes = Complete Estate Schema

```
200-Node Taxonomy
  ↓
Neo4j EntityType nodes (schema, permanent)
  ↓
Neo4j EntityInstance nodes (specific entities, 150-200)
  ↓
Wiki links [[ENTITY-TYPE-21]] → [[ENT-001]]
  ↓
Supabase tables (VEX queries)
  ↓
Company Brain Intelligence
```

This provides:
- ✅ **Schema completeness** (what types of entities CAN exist)
- ✅ **Instance tracking** (what entities DO exist)
- ✅ **Relationship mapping** (who owns what, who operates what)
- ✅ **Wiki navigation** (semantic links between types + instances)
- ✅ **Company Brain integration** (full graph modeling)

---

**Authority:** 200-node billionaire family office taxonomy + Neo4j ontology design  
**Status:** Schema defined, instances in progress, Phase 2 ready
**Updated:** 2026-09-23

---

## Control Base Reference

This document is mapped to [[B100|Control Base]] in the Company Brain.

**Wiki Link:** [[CBP_REGISTRY|_REGISTRIES/CANONICAL/CBP_REGISTRY.yaml#B100]]