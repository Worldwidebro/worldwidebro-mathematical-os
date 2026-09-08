// NEO4J RESOURCE LINKING + EDUCATION WIRING
// Execute after auth is fixed

// ===== LAYER 1: CREATE EDUCATION AGENTS =====
CREATE (agt6:Agent {id: 'AGT-006', name: 'Education Teacher', routing_key: 'education-teacher', type: 'routing'})
CREATE (agt7:Agent {id: 'AGT-007', name: 'Education Peer', routing_key: 'education-peer', type: 'routing'})
CREATE (agt8:Agent {id: 'AGT-008', name: 'Education Content', routing_key: 'education-content', type: 'routing'})
CREATE (agt9:Agent {id: 'AGT-009', name: 'Education Eval', routing_key: 'education-eval', type: 'routing'});

// ===== LAYER 2: CREATE EDUCATION SECTOR + CONTROL PLANE =====
CREATE (sec37:Sector {id: 'SEC-037', name: 'Education & Learning'})
CREATE (cp31:ControlPlane {id: 'CP-031', name: 'Education Control Plane', sector: 'SEC-037'});

// ===== LAYER 3: LINK AGENTS TO SECTOR =====
MATCH (a:Agent), (s:Sector)
WHERE a.id IN ['AGT-006', 'AGT-007', 'AGT-008', 'AGT-009'] AND s.id = 'SEC-037'
CREATE (a)-[:SERVES]->(s);

// ===== LAYER 4: LINK AGENTS TO CONTROL PLANE =====
MATCH (a:Agent), (cp:ControlPlane)
WHERE a.id IN ['AGT-006', 'AGT-007', 'AGT-008', 'AGT-009'] AND cp.id = 'CP-031'
CREATE (a)-[:EXECUTES]->(cp);

// ===== LAYER 5: CREATE EDUCATION CAPABILITIES =====
CREATE (cap200:Capability {id: 'CAP-200', name: 'Curriculum planning'})
CREATE (cap201:Capability {id: 'CAP-201', name: 'Slide generation'})
CREATE (cap202:Capability {id: 'CAP-202', name: 'Interactive simulations'})
CREATE (cap203:Capability {id: 'CAP-203', name: 'PBL design'})
CREATE (cap204:Capability {id: 'CAP-204', name: 'TTS rendering'})
CREATE (cap205:Capability {id: 'CAP-205', name: 'PPTX export'})
CREATE (cap206:Capability {id: 'CAP-206', name: 'Diagram creation'})
CREATE (cap207:Capability {id: 'CAP-207', name: 'Discussion prompts'})
CREATE (cap208:Capability {id: 'CAP-208', name: 'Q&A handling'})
CREATE (cap209:Capability {id: 'CAP-209', name: 'Content structuring'})
CREATE (cap210:Capability {id: 'CAP-210', name: 'Peer feedback'})
CREATE (cap211:Capability {id: 'CAP-211', name: 'Progress tracking'})
CREATE (cap212:Capability {id: 'CAP-212', name: 'Performance reporting'});

// ===== LAYER 6: LINK AGENTS TO CAPABILITIES =====
MATCH (a:Agent), (c:Capability)
WHERE a.id = 'AGT-006' AND c.id IN ['CAP-200', 'CAP-201', 'CAP-206', 'CAP-209']
CREATE (a)-[:IMPLEMENTS]->(c);

MATCH (a:Agent), (c:Capability)
WHERE a.id = 'AGT-007' AND c.id IN ['CAP-207', 'CAP-208', 'CAP-210']
CREATE (a)-[:IMPLEMENTS]->(c);

MATCH (a:Agent), (c:Capability)
WHERE a.id = 'AGT-008' AND c.id IN ['CAP-201', 'CAP-202', 'CAP-203', 'CAP-205']
CREATE (a)-[:IMPLEMENTS]->(c);

MATCH (a:Agent), (c:Capability)
WHERE a.id = 'AGT-009' AND c.id IN ['CAP-208', 'CAP-211', 'CAP-212']
CREATE (a)-[:IMPLEMENTS]->(c);

// ===== LAYER 7: CREATE REPOSITORIES =====
CREATE (rep1:Repository {id: 'REP-001', name: 'worldwidebro-venture-portal', type: 'core-platform'})
CREATE (rep2:Repository {id: 'REP-002', name: 'vex-hero-site', type: 'hero-site'})
CREATE (rep3:Repository {id: 'REP-003', name: 'claude-home', type: 'vex-core'});

// ===== LAYER 8: LINK REPOSITORIES TO AGENTS =====
MATCH (r:Repository), (a:Agent)
WHERE r.id = 'REP-003' AND a.id IN ['AGT-001', 'AGT-002', 'AGT-003', 'AGT-004', 'AGT-005']
CREATE (r)-[:USED_BY]->(a);

MATCH (r:Repository), (a:Agent)
WHERE r.id = 'REP-001' AND a.id IN ['AGT-001', 'AGT-002', 'AGT-006']
CREATE (r)-[:USED_BY]->(a);

// ===== LAYER 9: LINK REPOSITORIES TO CAPABILITIES =====
MATCH (r:Repository), (c:Capability)
WHERE r.id = 'REP-001' AND c.id IN ['CAP-001', 'CAP-012', 'CAP-050']
CREATE (r)-[:IMPLEMENTS]->(c);

MATCH (r:Repository), (c:Capability)
WHERE r.id = 'REP-003' AND c.id IN ['CAP-100', 'CAP-101', 'CAP-150']
CREATE (r)-[:IMPLEMENTS]->(c);

// ===== LAYER 10: CREATE TOOLS =====
CREATE (tool_clickup:Tool {id: 'TOL-clickup', name: 'ClickUp API', type: 'task-management'})
CREATE (tool_supabase:Tool {id: 'TOL-supabase', name: 'Supabase Client', type: 'database'})
CREATE (tool_stripe:Tool {id: 'TOL-stripe', name: 'Stripe API', type: 'payments'})
CREATE (tool_neo4j:Tool {id: 'TOL-neo4j', name: 'Neo4j', type: 'graph-database'})
CREATE (tool_qdrant:Tool {id: 'TOL-qdrant', name: 'Qdrant', type: 'vector-search'})
CREATE (tool_anthropic:Tool {id: 'TOL-anthropic', name: 'Anthropic Claude', type: 'llm'});

// ===== LAYER 11: LINK AGENTS TO TOOLS =====
MATCH (a:Agent), (t:Tool)
WHERE a.id IN ['AGT-006', 'AGT-007', 'AGT-008', 'AGT-009'] AND t.id = 'TOL-anthropic'
CREATE (a)-[:CAN_USE]->(t);

MATCH (a:Agent), (t:Tool)
WHERE a.id IN ['AGT-001', 'AGT-002', 'AGT-006'] AND t.id = 'TOL-clickup'
CREATE (a)-[:CAN_USE]->(t);

// ===== VERIFICATION =====
MATCH (a:Agent)-[:SERVES]->(s:Sector)
WHERE s.id = 'SEC-037'
RETURN COUNT(a) as education_agents_wired;

MATCH (a:Agent)-[:IMPLEMENTS]->(c:Capability)
WHERE a.id IN ['AGT-006', 'AGT-007', 'AGT-008', 'AGT-009']
RETURN COUNT(DISTINCT c) as education_capabilities_linked;

MATCH (r:Repository)-[:IMPLEMENTS]->(c:Capability)
RETURN COUNT(*) as repo_capability_links;
