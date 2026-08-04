// Knowledge Graph OS — Neo4j Schema
// Nodes: Agent, Task, Capability, Tool, Workflow, Step, Metric, Venture, OPCO
// Relationships: HAS_CAPABILITY, USES, REQUIRES_CAPABILITY, ASSIGNED_TO, EXECUTED, etc.

// ===== NODE LABELS & PROPERTIES =====

// Agent: autonomous actor (AI agent, human, system service)
// Properties: id (unique), name, type (ai|human|system), org_id, availability (0-1), cost_per_hour, success_rate (0-1), status (active|idle|error), updated_at
MATCH (n:Agent) RETURN DISTINCT n LIMIT 1;

// Task: unit of work
// Properties: id, name, status (pending|assigned|executing|completed|failed), priority (0-5), venture_id, created_at, updated_at, due_at
MATCH (n:Task) RETURN DISTINCT n LIMIT 1;

// Capability: skill or ability (e.g., "code-review", "deploy", "bug-fix")
// Properties: id, name, category, description, cost_estimate, success_baseline (0-1), complexity (low|medium|high)
MATCH (n:Capability) RETURN DISTINCT n LIMIT 1;

// Tool: external service or library (e.g., "slack-api", "github", "stripe")
// Properties: id, name, service, endpoint, rate_limit_per_hour, cost_per_call, status (available|rate_limited|error)
MATCH (n:Tool) RETURN DISTINCT n LIMIT 1;

// Workflow: orchestration pattern (e.g., "deploy-pipeline", "code-review-loop")
// Properties: id, name, type, status, venture_id, success_rate, avg_duration_mins
MATCH (n:Workflow) RETURN DISTINCT n LIMIT 1;

// Step: task in a workflow
// Properties: id, step_number, name, estimated_duration_mins, required_capabilities[], depends_on_step_ids[]
MATCH (n:Step) RETURN DISTINCT n LIMIT 1;

// Metric: KPI or measurement
// Properties: id, name, unit, venture_id, metric_type (rate|count|duration), current_value, target_value, measured_at
MATCH (n:Metric) RETURN DISTINCT n LIMIT 1;

// Venture: business initiative
// Properties: id, name, sector, stage (template|planned|mvp|live), readiness (0-100), revenue_monthly, created_at
MATCH (n:Venture) RETURN DISTINCT n LIMIT 1;

// OPCO: operational company (org structure)
// Properties: id, name, type (sector|team|service), parent_id, headcount, budget_monthly
MATCH (n:OPCO) RETURN DISTINCT n LIMIT 1;

// ===== RELATIONSHIP TYPES =====

// HAS_CAPABILITY: Agent → Capability (agent has this skill)
// Properties: proficiency (0-1), last_used_at, num_uses
MATCH (a:Agent)-[r:HAS_CAPABILITY]->(c:Capability) RETURN DISTINCT r LIMIT 1;

// REQUIRES_CAPABILITY: Task → Capability (task needs this skill)
// Properties: criticality (0-1), optional (bool)
MATCH (t:Task)-[r:REQUIRES_CAPABILITY]->(c:Capability) RETURN DISTINCT r LIMIT 1;

// USES: Agent|Task → Tool (uses external service)
// Properties: call_count, last_called_at, cost_total
MATCH (a:Agent)-[r:USES]->(t:Tool) RETURN DISTINCT r LIMIT 1;

// ASSIGNED_TO: Task → Agent (task assigned to agent)
// Properties: assigned_at, started_at, completed_at, success (bool), error_msg
MATCH (t:Task)-[r:ASSIGNED_TO]->(a:Agent) RETURN DISTINCT r LIMIT 1;

// EXECUTED: Task → Workflow (task ran as part of workflow)
// Properties: step_number, duration_secs, cost_incurred, success (bool)
MATCH (t:Task)-[r:EXECUTED]->(w:Workflow) RETURN DISTINCT r LIMIT 1;

// PART_OF: Step → Workflow (step belongs to workflow)
MATCH (s:Step)-[r:PART_OF]->(w:Workflow) RETURN DISTINCT r LIMIT 1;

// TRACKS: Metric → Venture (metric measures venture)
MATCH (m:Metric)-[r:TRACKS]->(v:Venture) RETURN DISTINCT r LIMIT 1;

// PART_OF_ORG: Agent|Venture → OPCO (belongs to org)
MATCH (a:Agent)-[r:PART_OF_ORG]->(o:OPCO) RETURN DISTINCT r LIMIT 1;

// ===== INDEXES (Performance) =====

// Composite indexes for routing queries
CREATE INDEX agent_id IF NOT EXISTS FOR (n:Agent) ON (n.id);
CREATE INDEX agent_org_id IF NOT EXISTS FOR (n:Agent) ON (n.org_id);
CREATE INDEX agent_status IF NOT EXISTS FOR (n:Agent) ON (n.status);
CREATE INDEX agent_org_status IF NOT EXISTS FOR (n:Agent) ON (n.org_id, n.status);

CREATE INDEX task_id IF NOT EXISTS FOR (n:Task) ON (n.id);
CREATE INDEX task_status IF NOT EXISTS FOR (n:Task) ON (n.status);
CREATE INDEX task_venture IF NOT EXISTS FOR (n:Task) ON (n.venture_id);

CREATE INDEX capability_id IF NOT EXISTS FOR (n:Capability) ON (n.id);
CREATE INDEX capability_name IF NOT EXISTS FOR (n:Capability) ON (n.name);
CREATE INDEX capability_category IF NOT EXISTS FOR (n:Capability) ON (n.category);

CREATE INDEX tool_id IF NOT EXISTS FOR (n:Tool) ON (n.id);
CREATE INDEX tool_service IF NOT EXISTS FOR (n:Tool) ON (n.service);
CREATE INDEX tool_status IF NOT EXISTS FOR (n:Tool) ON (n.status);

CREATE INDEX workflow_id IF NOT EXISTS FOR (n:Workflow) ON (n.id);
CREATE INDEX workflow_venture IF NOT EXISTS FOR (n:Workflow) ON (n.venture_id);

CREATE INDEX step_id IF NOT EXISTS FOR (n:Step) ON (n.id);

CREATE INDEX metric_id IF NOT EXISTS FOR (n:Metric) ON (n.id);
CREATE INDEX metric_venture IF NOT EXISTS FOR (n:Metric) ON (n.venture_id);

CREATE INDEX venture_id IF NOT EXISTS FOR (n:Venture) ON (n.id);
CREATE INDEX venture_sector IF NOT EXISTS FOR (n:Venture) ON (n.sector);
CREATE INDEX venture_stage IF NOT EXISTS FOR (n:Venture) ON (n.stage);

CREATE INDEX opco_id IF NOT EXISTS FOR (n:OPCO) ON (n.id);
CREATE INDEX opco_type IF NOT EXISTS FOR (n:OPCO) ON (n.type);

// ===== UNIQUENESS CONSTRAINTS =====

CREATE CONSTRAINT agent_unique IF NOT EXISTS FOR (n:Agent) REQUIRE (n.id) IS UNIQUE;
CREATE CONSTRAINT task_unique IF NOT EXISTS FOR (n:Task) REQUIRE (n.id) IS UNIQUE;
CREATE CONSTRAINT capability_unique IF NOT EXISTS FOR (n:Capability) REQUIRE (n.id) IS UNIQUE;
CREATE CONSTRAINT tool_unique IF NOT EXISTS FOR (n:Tool) REQUIRE (n.id) IS UNIQUE;
CREATE CONSTRAINT workflow_unique IF NOT EXISTS FOR (n:Workflow) REQUIRE (n.id) IS UNIQUE;
CREATE CONSTRAINT step_unique IF NOT EXISTS FOR (n:Step) REQUIRE (n.id) IS UNIQUE;
CREATE CONSTRAINT metric_unique IF NOT EXISTS FOR (n:Metric) REQUIRE (n.id) IS UNIQUE;
CREATE CONSTRAINT venture_unique IF NOT EXISTS FOR (n:Venture) REQUIRE (n.id) IS UNIQUE;
CREATE CONSTRAINT opco_unique IF NOT EXISTS FOR (n:OPCO) REQUIRE (n.id) IS UNIQUE;

// ===== SCHEMA DOCUMENTATION =====
// Run in Round 3 via Neo4j driver after Supabase ingestion.
// Indexes + constraints enable:
//   - O(1) agent lookup by id/org/status
//   - Efficient capability matching for routing
//   - Task status filtering + venture grouping
//   - Cross-org queries with org_id predicates
