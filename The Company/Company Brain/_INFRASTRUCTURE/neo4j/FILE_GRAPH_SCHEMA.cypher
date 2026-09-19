// FILE GRAPH SCHEMA FOR COMPANY BRAIN
// Purpose: Map all documents, domains, and wiki links as a connected graph
// Date: 2026-09-19

// ==============================================================================
// 1. CONSTRAINTS (Ensure uniqueness and data integrity)
// ==============================================================================

CREATE CONSTRAINT IF NOT EXISTS FOR (f:File) REQUIRE f.path IS UNIQUE;
CREATE CONSTRAINT IF NOT EXISTS FOR (d:Domain) REQUIRE d.name IS UNIQUE;
CREATE CONSTRAINT IF NOT EXISTS FOR (l:Link) REQUIRE (l.from, l.to) IS UNIQUE;

// ==============================================================================
// 2. INDEXES (For fast lookups)
// ==============================================================================

CREATE INDEX IF NOT EXISTS FOR (f:File) ON (f.name);
CREATE INDEX IF NOT EXISTS FOR (f:File) ON (f.domain);
CREATE INDEX IF NOT EXISTS FOR (f:File) ON (f.hasWikiLinks);
CREATE INDEX IF NOT EXISTS FOR (d:Domain) ON (d.layer);

// ==============================================================================
// 3. DOMAIN NODES (All 72 numbered domains + infrastructure)
// ==============================================================================

// Numbered domains (00-57)
WITH [
  {id: '00', name: 'CONSTITUTION', layer: 1, purpose: 'Mission, vision, governance'},
  {id: '01', name: 'IDENTITY', layer: 1, purpose: 'Company structure, ventures'},
  {id: '02', name: 'SOURCES', layer: 2, purpose: 'Data sources, APIs'},
  {id: '03', name: 'INGESTION', layer: 2, purpose: 'Data pipelines'},
  {id: '04', name: 'DATA', layer: 3, purpose: 'Raw, normalized data'},
  {id: '05', name: 'METADATA', layer: 3, purpose: 'Schemas, lineage'},
  {id: '06', name: 'ENTITY-RESOLUTION', layer: 4, purpose: 'Dedup, linking'},
  {id: '07', name: 'ONTOLOGY', layer: 5, purpose: 'Concepts, relationships'},
  {id: '08', name: 'KNOWLEDGE-GRAPH', layer: 6, purpose: 'Nodes, edges, embeddings'},
  {id: '09', name: 'KNOWLEDGE', layer: 7, purpose: 'Policies, procedures, IP'},
  {id: '10', name: 'MEMORY', layer: 8, purpose: 'Working, episodic, semantic'},
  {id: '11', name: 'INDEXING', layer: 9, purpose: 'Full-text, vector, semantic'},
  {id: '12', name: 'CONTEXT', layer: 10, purpose: 'Task, venture, customer context'},
  {id: '13', name: 'REPOSITORIES', layer: 11, purpose: 'Code, ownership, quality'},
  {id: '14', name: 'CAPABILITIES', layer: 12, purpose: 'Registry, implementations'},
  {id: '15', name: 'SKILLS', layer: 13, purpose: 'Library, instructions'},
  {id: '16', name: 'AGENTS', layer: 14, purpose: 'Registry, roles, permissions'},
  {id: '17', name: 'MODELS', layer: 15, purpose: 'ML models, routing'},
  {id: '18', name: 'TOOLS', layer: 16, purpose: 'Tool catalog, SDKs'},
  {id: '19', name: 'ORCHESTRATION', layer: 17, purpose: 'Workflows, routing'},
  {id: '20', name: 'DECISIONS', layer: 18, purpose: 'ADRs, decisions, plans'},
  {id: '21', name: 'POLICY', layer: 18, purpose: 'Business rules, compliance'},
  {id: '22', name: 'EXECUTION', layer: 19, purpose: 'Autonomous execution'},
  {id: '23', name: 'VENTURES', layer: 2, purpose: 'Venture registry, operations'},
  {id: '24', name: 'FINANCE', layer: 2, purpose: 'Capital, budgets, forecasts'},
  {id: '25', name: 'SALES', layer: 2, purpose: 'Sales operations, pipeline'},
  {id: '26', name: 'MARKETING', layer: 2, purpose: 'Campaigns, brand, growth'},
  {id: '27', name: 'CUSTOMERS', layer: 2, purpose: 'Customer data, success'},
  {id: '28', name: 'PRODUCT', layer: 2, purpose: 'Product strategy, roadmap'},
  {id: '29', name: 'OPERATIONS', layer: 2, purpose: 'Operations, processes'},
  {id: '30', name: 'HR', layer: 2, purpose: 'People, hiring, onboarding'},
  {id: '31', name: 'LEGAL', layer: 2, purpose: 'Contracts, compliance'},
  {id: '32', name: 'SECURITY', layer: 2, purpose: 'Security, infosec'},
  {id: '33', name: 'COMPLIANCE', layer: 2, purpose: 'Regulatory, audits'},
  {id: '34', name: 'RISK', layer: 2, purpose: 'Risk management'},
  {id: '35', name: 'ASSETS', layer: 2, purpose: 'Intellectual property'},
  {id: '36', name: 'PARTNERS', layer: 2, purpose: 'Partner management'},
  {id: '37', name: 'RESEARCH', layer: 20, purpose: 'Market research, trends'},
  {id: '38', name: 'OPPORTUNITIES', layer: 20, purpose: 'New ventures, growth'},
  {id: '39', name: 'EXPERIMENTS', layer: 20, purpose: 'Tests, pilots, validation'},
  {id: '40', name: 'METRICS', layer: 20, purpose: 'KPIs, dashboards'},
  {id: '41', name: 'OBSERVABILITY', layer: 21, purpose: 'Monitoring, telemetry'},
  {id: '42', name: 'EVALUATION', layer: 21, purpose: 'Testing, benchmarks'},
  {id: '43', name: 'OUTCOMES', layer: 21, purpose: 'Business outcomes'},
  {id: '44', name: 'LEARNING', layer: 22, purpose: 'What we learned'},
  {id: '45', name: 'EVOLUTION', layer: 22, purpose: 'Continuous improvement'},
  {id: '46', name: 'GOVERNANCE', layer: 1, purpose: 'Control, oversight'},
  {id: '47', name: 'DOCUMENTS', layer: 7, purpose: 'Reports, artifacts'},
  {id: '48', name: 'AUTOMATION', layer: 19, purpose: 'Workflows, triggers'},
  {id: '49', name: 'SYSTEM', layer: 19, purpose: 'System operations'},
  {id: '50', name: 'MASTER-CONTROL', layer: 1, purpose: 'Central control point'},
  {id: '57', name: 'CODE-INTELLIGENCE', layer: 11, purpose: 'Code graphs, symbols'}
] AS domainData
UNWIND domainData AS d
CREATE (domain:Domain {
  id: d.id,
  name: d.name,
  layer: d.layer,
  purpose: d.purpose,
  created: datetime()
});

// Infrastructure domains
WITH [
  {name: '_AGENTS', layer: 14, purpose: 'Agent definitions'},
  {name: '_ORCHESTRATION', layer: 17, purpose: 'Orchestration'},
  {name: '_INFRASTRUCTURE', layer: 19, purpose: 'Infrastructure'},
  {name: '_MCP', layer: 18, purpose: 'MCP tools'},
  {name: '_MEMORY', layer: 8, purpose: 'Memory systems'},
  {name: '_ONTOLOGY', layer: 5, purpose: 'Ontology schemas'},
  {name: '_REGISTRIES', layer: 10, purpose: 'Canonical registries'},
  {name: '_PIPELINES', layer: 11, purpose: 'Data pipelines'}
] AS infra
UNWIND infra AS i
CREATE (domain:Domain {
  name: i.name,
  layer: i.layer,
  purpose: i.purpose,
  isInfra: true,
  created: datetime()
});

// ==============================================================================
// 4. MASTER ENTRY POINTS (All files link back to these)
// ==============================================================================

CREATE (master:MasterNode:File {
  name: 'STARTHERE',
  path: './STARTHERE.md',
  purpose: 'Master orientation entry point',
  type: 'navigation_hub',
  priority: 1
});

CREATE (master2:MasterNode:File {
  name: 'REALITY',
  path: './REALITY.md',
  purpose: 'Verified truth ledger',
  type: 'navigation_hub',
  priority: 1
});

CREATE (master3:MasterNode:File {
  name: 'ANTIGRAVITY',
  path: './ANTIGRAVITY.md',
  purpose: '45 operating rules',
  type: 'navigation_hub',
  priority: 1
});

CREATE (master4:MasterNode:File {
  name: 'INDEX',
  path: './INDEX.md',
  purpose: 'Master file index',
  type: 'navigation_hub',
  priority: 1
});

// ==============================================================================
// 5. RELATIONSHIPS (Link domains to master nodes)
// ==============================================================================

MATCH (master:MasterNode), (d:Domain)
CREATE (master)-[:NAVIGATES_TO {type: 'master_link', weight: 1.0}]->(d);

// ==============================================================================
// 6. QUERIES TO POPULATE (Run separately with file scan data)
// ==============================================================================

// Add FILE nodes:
// MATCH (d:Domain {name: 'VENTURES'})
// CREATE (f:File {
//   name: 'venture-name',
//   path: './23-VENTURES/venture-name.md',
//   domain: d.name,
//   hasWikiLinks: true,
//   linkCount: 5,
//   created: datetime()
// })-[:IN_DOMAIN]->(d);

// Add LINK edges (wiki references):
// MATCH (f1:File), (f2:File)
// WHERE f1.name = 'source' AND f2.name = 'target'
// CREATE (f1)-[:LINKS_TO {type: 'wiki_reference', text: '[[target]]'}]->(f2);

// ==============================================================================
// 7. VERIFICATION QUERIES
// ==============================================================================

// Find all unlinked files:
// MATCH (f:File) WHERE NOT (f)-[:LINKS_TO]->() AND NOT (f)-[:IN_DOMAIN]->() RETURN f;

// Find broken links (references to non-existent files):
// MATCH (f1:File)-[:LINKS_TO]->(f2) WHERE f2 IS NULL RETURN f1, f2;

// Show domain connectivity:
// MATCH (d1:Domain)-[r:CONNECTS_TO]-(d2:Domain) RETURN d1.name, d2.name;

// ==============================================================================
// 8. SUMMARY
// ==============================================================================
// Schema created: 47 domains + 8 infrastructure + 4 master nodes
// Ready to populate with file scan data
// Next: Run file_graph_populate.py to insert all documents and links
