// IZA OS Neo4j Graph Database Schema & Ontology Configuration
// Expands graph structure to support AI Operating System entities.

// ============================================================================
// 1. Constraints & Indexes
// ============================================================================

CREATE CONSTRAINT sector_name IF NOT EXISTS
FOR (s:Sector) REQUIRE s.name IS UNIQUE;

CREATE CONSTRAINT capability_name IF NOT EXISTS
FOR (c:Capability) REQUIRE c.name IS UNIQUE;

CREATE CONSTRAINT agent_name IF NOT EXISTS
FOR (a:Agent) REQUIRE a.name IS UNIQUE;

CREATE CONSTRAINT workflow_name IF NOT EXISTS
FOR (w:Workflow) REQUIRE w.name IS UNIQUE;

CREATE CONSTRAINT output_name IF NOT EXISTS
FOR (o:Output) REQUIRE o.name IS UNIQUE;

CREATE CONSTRAINT metric_name IF NOT EXISTS
FOR (m:Metric) REQUIRE m.name IS UNIQUE;

CREATE CONSTRAINT customer_id IF NOT EXISTS
FOR (cu:Customer) REQUIRE cu.id IS UNIQUE;

// ============================================================================
// 2. Mapped Relationships Reference
// ============================================================================

// (Venture)-[:USES]->(Capability)
// (Capability)-[:IMPLEMENTED_BY]->(Repo)
// (Venture)-[:OPERATED_BY]->(Agent)
// (Agent)-[:EXECUTES]->(Workflow)
// (Workflow)-[:PRODUCES]->(Output)
// (Venture)-[:MAPPED_TO]->(Sector)
// (Sector)-[:REQUIRES]->(Capability)
// (Venture)-[:TRACKS]->(Metric)
// (Venture)-[:SERVES]->(Customer)

// ============================================================================
// 3. Example seeding template (Cypher 25 syntax compliant)
// ============================================================================

// MERGE (s:Sector {name: 'ecommerce', label: 'E-Commerce'})
// MERGE (c:Capability {name: 'storefront', type: 'frontend'})
// MERGE (r:Repo {name: 'medusa'})
// MERGE (c)-[:IMPLEMENTED_BY]->(r)
// MERGE (s)-[:REQUIRES]->(c)
