// Neo4j Graph Wiring for Capability Registry
// Unit 9: Create Capability, Domain, and MCP nodes + relationships
// Generated: 2026-09-10

// =============================================================================
// STEP 1: Create Domain nodes
// =============================================================================

CREATE (sales:Domain {id: 'DOM-SALES', name: 'Sales & Prospecting', icon: '🎯'})
CREATE (ops:Domain {id: 'DOM-OPS', name: 'Operations & Dispatch', icon: '📦'})
CREATE (compliance:Domain {id: 'DOM-COMPLIANCE', name: 'HIPAA & Compliance', icon: '🔒'})
CREATE (learning:Domain {id: 'DOM-LEARNING', name: 'Learning & Training', icon: '📚'})
CREATE (knowledge:Domain {id: 'DOM-KNOWLEDGE', name: 'Knowledge & Memory', icon: '🧠'})
CREATE (infra:Domain {id: 'DOM-INFRA', name: 'Infrastructure & Security', icon: '⚙️'})
;

// =============================================================================
// STEP 2: Create MCP nodes
// =============================================================================

CREATE (mcp_supabase:MCP {id: 'MCP-SUPABASE', name: 'Supabase MCP', version: '1.0'})
CREATE (mcp_neo4j:MCP {id: 'MCP-NEO4J', name: 'Neo4j MCP', version: '1.0'})
CREATE (mcp_librarian:MCP {id: 'MCP-LIBRARIAN', name: 'Librarian MCP', version: '1.0'})
CREATE (mcp_anthropic:MCP {id: 'MCP-ANTHROPIC-SALES', name: 'Anthropic Sales Plugin', version: '1.0'})
;

// =============================================================================
// STEP 3: Create Capability nodes
// =============================================================================

// CAP-001: Account Research (Anthropic)
CREATE (cap001:Capability {
    id: 'CAP-001',
    ref_id: 'CAP-001',
    slug: 'anthropic-account-research',
    name: 'Account Research (Prospect Intelligence)',
    description: 'Research a company or person and extract actionable sales intelligence',
    source: 'anthropic',
    healthroute_fit: 95,
    maturity: 'production',
    version: '1.0'
})
;

// CAP-003: Call Summary (Anthropic)
CREATE (cap003:Capability {
    id: 'CAP-003',
    ref_id: 'CAP-003',
    slug: 'anthropic-call-summary',
    name: 'Call Summary & Action Items',
    description: 'Extract action items, draft follow-up, and log call to CRM',
    source: 'anthropic',
    healthroute_fit: 90,
    maturity: 'production',
    version: '1.0'
})
;

// CAP-101: Agentic Workflow Patterns (awesome-claude-code)
CREATE (cap101:Capability {
    id: 'CAP-101',
    ref_id: 'CAP-101',
    slug: 'agentic-workflow-patterns',
    name: 'Agentic Workflow Patterns',
    description: 'Comprehensive collection of agentic patterns: orchestrator-workers, prompt chaining, routing',
    source: 'awesome-claude-code',
    healthroute_fit: 90,
    maturity: 'production',
    version: '1.0'
})
;

// CAP-401: Librarian MCP (awesome-claude-code)
CREATE (cap401:Capability {
    id: 'CAP-401',
    ref_id: 'CAP-401',
    slug: 'librarian-mcp',
    name: 'Librarian MCP — Knowledge Base Backend',
    description: 'MCP server for Obsidian vault storage with semantic search and graph analytics',
    source: 'awesome-claude-code',
    healthroute_fit: 85,
    maturity: 'production',
    version: '1.0'
})
;

// CAP-201: HealthRoute HIPAA Compliance (Custom)
CREATE (cap201:Capability {
    id: 'CAP-201',
    ref_id: 'CAP-201',
    slug: 'healthroute-hipaa-compliance',
    name: 'HealthRoute HIPAA Compliance & Audit Logging',
    description: 'Custom MCP wrapper: HIPAA-compliant audit logging, BAA tracking, compliance evidence capture',
    source: 'internal',
    healthroute_fit: 100,
    maturity: 'beta',
    version: '1.0'
})
;

// =============================================================================
// STEP 4: Wire Capability → Domain relationships
// =============================================================================

MATCH (cap001:Capability {id: 'CAP-001'}), (sales:Domain {id: 'DOM-SALES'})
CREATE (cap001)-[:BELONGS_TO]->(sales)
;

MATCH (cap003:Capability {id: 'CAP-003'}), (sales:Domain {id: 'DOM-SALES'})
CREATE (cap003)-[:BELONGS_TO]->(sales)
;

MATCH (cap101:Capability {id: 'CAP-101'}), (infra:Domain {id: 'DOM-INFRA'})
CREATE (cap101)-[:BELONGS_TO]->(infra)
;

MATCH (cap401:Capability {id: 'CAP-401'}), (knowledge:Domain {id: 'DOM-KNOWLEDGE'})
CREATE (cap401)-[:BELONGS_TO]->(knowledge)
;

MATCH (cap201:Capability {id: 'CAP-201'}), (compliance:Domain {id: 'DOM-COMPLIANCE'})
CREATE (cap201)-[:BELONGS_TO]->(compliance)
;

// =============================================================================
// STEP 5: Wire Capability → MCP relationships (dependencies)
// =============================================================================

// CAP-001 (Account Research) doesn't require MCP (uses web search)
// No relationship needed

// CAP-003 (Call Summary) requires Supabase for logging
MATCH (cap003:Capability {id: 'CAP-003'}), (mcp_supabase:MCP {id: 'MCP-SUPABASE'})
CREATE (cap003)-[:REQUIRES_MCP {required: true}]->(mcp_supabase)
;

// CAP-101 (Agentic Patterns) doesn't require MCP (reference material)
// No relationship needed

// CAP-401 (Librarian MCP) is an MCP itself (no external MCP required)
// No relationship needed

// CAP-201 (HIPAA Compliance) requires Supabase for audit logging
MATCH (cap201:Capability {id: 'CAP-201'}), (mcp_supabase:MCP {id: 'MCP-SUPABASE'})
CREATE (cap201)-[:REQUIRES_MCP {required: true}]->(mcp_supabase)
;

// =============================================================================
// STEP 6: Create cross-capability relationships (composition)
// =============================================================================

// CAP-001 (research) feeds into CAP-003 (call-summary)
MATCH (cap001:Capability {id: 'CAP-001'}), (cap003:Capability {id: 'CAP-003'})
CREATE (cap001)-[:INFORMS]->(cap003)
;

// CAP-101 (orchestrator pattern) enables composition of CAP-001 + CAP-003
MATCH (cap101:Capability {id: 'CAP-101'}), (cap001:Capability {id: 'CAP-001'}), (cap003:Capability {id: 'CAP-003'})
CREATE (cap101)-[:ORCHESTRATES]->(cap001)
CREATE (cap101)-[:ORCHESTRATES]->(cap003)
;

// CAP-401 (Librarian) stores knowledge from CAP-003 (call summaries)
MATCH (cap401:Capability {id: 'CAP-401'}), (cap003:Capability {id: 'CAP-003'})
CREATE (cap003)-[:STORES_IN]->(cap401)
;

// CAP-201 (HIPAA) audits CAP-003 (call summaries)
MATCH (cap201:Capability {id: 'CAP-201'}), (cap003:Capability {id: 'CAP-003'})
CREATE (cap003)-[:AUDITED_BY]->(cap201)
;

// =============================================================================
// VERIFICATION QUERIES (run after all CREATE commands)
// =============================================================================

// Count all nodes
MATCH (n) RETURN labels(n) as type, COUNT(n) as count
;

// Verify all 5 capabilities exist
MATCH (c:Capability) RETURN c.ref_id, c.name, c.healthroute_fit ORDER BY c.healthroute_fit DESC
;

// Verify domain relationships
MATCH (c:Capability)-[:BELONGS_TO]->(d:Domain) RETURN c.ref_id, d.name
;

// Verify MCP dependencies
MATCH (c:Capability)-[:REQUIRES_MCP]->(m:MCP) RETURN c.ref_id, m.name
;

// Verify capability composition
MATCH (c1:Capability)-[r]->(c2:Capability) RETURN c1.ref_id, TYPE(r), c2.ref_id
;
