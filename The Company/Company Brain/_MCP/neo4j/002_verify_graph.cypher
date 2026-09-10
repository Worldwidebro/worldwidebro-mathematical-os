// Verification queries for Capability Registry graph
// Run these after 001_create_capability_nodes.cypher completes

// =============================================================================
// VERIFICATION SUITE
// =============================================================================

// 1. Count all nodes by type
MATCH (n) 
RETURN labels(n)[0] as node_type, COUNT(n) as count
ORDER BY node_type
;

// Expected output:
// Capability: 5
// Domain: 6
// MCP: 4
// Total: 15 nodes

// 2. List all capabilities with fit score
MATCH (c:Capability)
RETURN c.ref_id as ID, c.name as Name, c.healthroute_fit as Fit
ORDER BY c.healthroute_fit DESC
;

// Expected: 5 rows (CAP-201: 100, CAP-001: 95, CAP-003: 90, CAP-101: 90, CAP-401: 85)

// 3. Verify domain assignments
MATCH (c:Capability)-[:BELONGS_TO]->(d:Domain)
RETURN d.name as Domain, COUNT(c) as Capabilities
ORDER BY Capabilities DESC
;

// Expected: 5 domains (1 capability each), 1 domain with 0

// 4. Verify MCP dependencies
MATCH (c:Capability)-[r:REQUIRES_MCP]->(m:MCP)
RETURN c.ref_id as Capability, m.name as MCP
;

// Expected: 2 relationships (CAP-003, CAP-201 → MCP-SUPABASE)

// 5. Verify capability composition (workflow edges)
MATCH (c1:Capability)-[r:ORCHESTRATES|INFORMS|STORES_IN|AUDITED_BY]->(c2:Capability)
RETURN c1.ref_id as From, TYPE(r) as Relationship, c2.ref_id as To
;

// Expected: 5 relationships
// CAP-101 ORCHESTRATES CAP-001
// CAP-101 ORCHESTRATES CAP-003
// CAP-001 INFORMS CAP-003
// CAP-003 STORES_IN CAP-401
// CAP-003 AUDITED_BY CAP-201

// 6. Full workflow graph (research → summary → storage + audit)
MATCH path = (c1:Capability {id: 'CAP-001'})-[*]->(c2:Capability {id: 'CAP-201'})
RETURN path
;

// Expected: 2 paths
// Path 1: CAP-001 INFORMS CAP-003 AUDITED_BY CAP-201
// Path 2: CAP-001 INFORMS CAP-003 STORES_IN CAP-401

// 7. Find all capabilities in a domain
MATCH (c:Capability)-[:BELONGS_TO]->(d:Domain {id: 'DOM-SALES'})
RETURN c.ref_id, c.name, c.healthroute_fit
;

// Expected: 2 (CAP-001, CAP-003)

// 8. Find all capabilities with high fit (>= 80%)
MATCH (c:Capability)
WHERE c.healthroute_fit >= 80
RETURN c.ref_id, c.name, c.healthroute_fit
ORDER BY c.healthroute_fit DESC
;

// Expected: 5 (all of them)

// 9. Graph statistics
MATCH (c:Capability) RETURN COUNT(c) as total_capabilities, AVG(c.healthroute_fit) as avg_fit, MIN(c.healthroute_fit) as min_fit, MAX(c.healthroute_fit) as max_fit
;

// Expected: count=5, avg=92, min=85, max=100

// 10. Transitive closure: What capabilities support CAP-003?
MATCH (c:Capability)-[*0..]->(cap003:Capability {id: 'CAP-003'})
RETURN DISTINCT c.ref_id as SupportingCapability
ORDER BY c.ref_id
;

// Expected: CAP-001, CAP-101 (plus CAP-003 itself via *0)
