// Neo4j Constraints and Indexes for VEX Graph
// Run via Neo4j UI or CLI

// === UNIQUE CONSTRAINTS ===

CREATE CONSTRAINT venture_id_unique FOR (v:Venture) REQUIRE v.id IS UNIQUE;
CREATE CONSTRAINT capability_id_unique FOR (c:Capability) REQUIRE c.id IS UNIQUE;
CREATE CONSTRAINT repository_github_url_unique FOR (r:Repository) REQUIRE r.github_url IS UNIQUE;
CREATE CONSTRAINT agent_id_unique FOR (a:Agent) REQUIRE a.id IS UNIQUE;
CREATE CONSTRAINT workflow_id_unique FOR (w:Workflow) REQUIRE w.id IS UNIQUE;
CREATE CONSTRAINT tool_id_unique FOR (t:Tool) REQUIRE t.id IS UNIQUE;
CREATE CONSTRAINT event_id_unique FOR (e:Event) REQUIRE e.id IS UNIQUE;
CREATE CONSTRAINT decision_id_unique FOR (d:Decision) REQUIRE d.id IS UNIQUE;
CREATE CONSTRAINT sector_id_unique FOR (s:Sector) REQUIRE s.id IS UNIQUE;
CREATE CONSTRAINT skill_id_unique FOR (sk:Skill) REQUIRE sk.id IS UNIQUE;

// === MANDATORY PROPERTIES ===

CREATE CONSTRAINT temporal_edges_require_valid_from FOR ()-[r]->() REQUIRE r.valid_from IS NOT NULL;
CREATE CONSTRAINT event_requires_type FOR (e:Event) REQUIRE e.type IS NOT NULL;
CREATE CONSTRAINT event_requires_created_at FOR (e:Event) REQUIRE e.created_at IS NOT NULL;
CREATE CONSTRAINT decision_requires_made_at FOR (d:Decision) REQUIRE d.made_at IS NOT NULL;

// === PERFORMANCE INDEXES ===

CREATE INDEX venture_status FOR (v:Venture) ON (v.status);
CREATE INDEX venture_readiness FOR (v:Venture) ON (v.readiness_score);
CREATE INDEX venture_last_audit FOR (v:Venture) ON (v.last_audit);

CREATE INDEX capability_type FOR (c:Capability) ON (c.type);
CREATE INDEX capability_verified FOR (c:Capability) ON (c.verified);

CREATE INDEX repository_is_alive FOR (r:Repository) ON (r.is_alive);
CREATE INDEX repository_last_commit FOR (r:Repository) ON (r.last_commit);
CREATE INDEX repository_language FOR (r:Repository) ON (r.language);

CREATE INDEX agent_status FOR (a:Agent) ON (a.status);
CREATE INDEX agent_last_execution FOR (a:Agent) ON (a.last_execution);

CREATE INDEX workflow_status FOR (w:Workflow) ON (w.status);
CREATE INDEX workflow_last_run FOR (w:Workflow) ON (w.last_run);

CREATE INDEX event_type FOR (e:Event) ON (e.type);
CREATE INDEX event_created_at FOR (e:Event) ON (e.created_at);
CREATE INDEX event_trace_id FOR (e:Event) ON (e.trace_id);

CREATE INDEX decision_status FOR (d:Decision) ON (d.status);
CREATE INDEX decision_confidence FOR (d:Decision) ON (d.confidence_score);
CREATE INDEX decision_made_at FOR (d:Decision) ON (d.made_at);

CREATE INDEX blocker_severity FOR (b:Blocker) ON (b.severity);
CREATE INDEX blocker_created_at FOR (b:Blocker) ON (b.created_at);

// === RELATIONSHIP INDEXES (for fast traversal) ===

CREATE INDEX idx_venture_sector FOR ()-[r:BELONGS_TO]->(s:Sector) ON r.valid_from;
CREATE INDEX idx_venture_opco FOR ()-[r:OPERATED_BY]->() ON r.valid_from;
CREATE INDEX idx_capability_repo FOR ()-[r:IMPLEMENTED_BY]->(repo:Repository) ON r.valid_from;
CREATE INDEX idx_agent_workflow FOR ()-[r:IMPLEMENTS_WORKFLOW]->(w:Workflow) ON r.valid_from;
CREATE INDEX idx_decision_venture FOR ()-[r:AFFECTS]->(v:Venture) ON r.valid_from;
