// ============================================================================
// IZA OS Neo4j Schema - Phase 3 Deployment
// Knowledge Backbone for Civilization Operating System
// ============================================================================
// This schema models:
// - 712 Ventures across 18 OPCOs
// - 12 Departments providing capabilities
// - 50+ Agents executing decisions
// - Capability marketplace (25 canonical + variants)
// - Decision governance with 3 authority levels
// - Real-time agent assignment routing
// ============================================================================

// ====================
// UNIQUENESS CONSTRAINTS
// ====================

CREATE CONSTRAINT venture_id_unique IF NOT EXISTS
  FOR (v:Venture) REQUIRE v.venture_id IS UNIQUE;

CREATE CONSTRAINT opco_id_unique IF NOT EXISTS
  FOR (o:OPCO) REQUIRE o.opco_id IS UNIQUE;

CREATE CONSTRAINT department_id_unique IF NOT EXISTS
  FOR (d:Department) REQUIRE d.department_id IS UNIQUE;

CREATE CONSTRAINT agent_id_unique IF NOT EXISTS
  FOR (a:Agent) REQUIRE a.agent_id IS UNIQUE;

CREATE CONSTRAINT capability_id_unique IF NOT EXISTS
  FOR (c:Capability) REQUIRE c.capability_id IS UNIQUE;

CREATE CONSTRAINT decision_id_unique IF NOT EXISTS
  FOR (d:Decision) REQUIRE d.decision_id IS UNIQUE;

CREATE CONSTRAINT sector_code_unique IF NOT EXISTS
  FOR (s:Sector) REQUIRE s.sector_code IS UNIQUE;

CREATE CONSTRAINT skill_id_unique IF NOT EXISTS
  FOR (s:Skill) REQUIRE s.skill_id IS UNIQUE;

CREATE CONSTRAINT repository_id_unique IF NOT EXISTS
  FOR (r:Repository) REQUIRE r.repo_id IS UNIQUE;

CREATE CONSTRAINT metric_id_unique IF NOT EXISTS
  FOR (m:Metric) REQUIRE m.metric_id IS UNIQUE;

CREATE CONSTRAINT risk_id_unique IF NOT EXISTS
  FOR (r:Risk) REQUIRE r.risk_id IS UNIQUE;

CREATE CONSTRAINT stage_code_unique IF NOT EXISTS
  FOR (s:Stage) REQUIRE s.stage_code IS UNIQUE;

// ====================
// REFERENTIAL INTEGRITY
// ====================

// Every Venture must belong to exactly one OPCO
CREATE CONSTRAINT venture_has_one_opco IF NOT EXISTS
  FOR (v:Venture) REQUIRE (v)-[:BELONGS_TO]->(:OPCO);

// Every Agent must belong to exactly one Department
CREATE CONSTRAINT agent_has_one_department IF NOT EXISTS
  FOR (a:Agent) REQUIRE (a)-[:ASSIGNED_TO]->(:Department);

// ====================
// PROPERTY EXISTENCE
// ====================

// Venture required fields
CREATE CONSTRAINT venture_has_id IF NOT EXISTS
  FOR (v:Venture) REQUIRE v.venture_id IS NOT NULL;

CREATE CONSTRAINT venture_has_name IF NOT EXISTS
  FOR (v:Venture) REQUIRE v.venture_name IS NOT NULL;

// OPCO required fields
CREATE CONSTRAINT opco_has_id IF NOT EXISTS
  FOR (o:OPCO) REQUIRE o.opco_id IS NOT NULL;

CREATE CONSTRAINT opco_has_name IF NOT EXISTS
  FOR (o:OPCO) REQUIRE o.opco_name IS NOT NULL;

// Department required fields
CREATE CONSTRAINT department_has_id IF NOT EXISTS
  FOR (d:Department) REQUIRE d.department_id IS NOT NULL;

CREATE CONSTRAINT department_has_name IF NOT EXISTS
  FOR (d:Department) REQUIRE d.department_name IS NOT NULL;

// Agent required fields
CREATE CONSTRAINT agent_has_id IF NOT EXISTS
  FOR (a:Agent) REQUIRE a.agent_id IS NOT NULL;

CREATE CONSTRAINT agent_has_name IF NOT EXISTS
  FOR (a:Agent) REQUIRE a.agent_name IS NOT NULL;

// Capability required fields
CREATE CONSTRAINT capability_has_id IF NOT EXISTS
  FOR (c:Capability) REQUIRE c.capability_id IS NOT NULL;

CREATE CONSTRAINT capability_has_name IF NOT EXISTS
  FOR (c:Capability) REQUIRE c.capability_name IS NOT NULL;

// Decision required fields
CREATE CONSTRAINT decision_has_id IF NOT EXISTS
  FOR (d:Decision) REQUIRE d.decision_id IS NOT NULL;

CREATE CONSTRAINT decision_has_type IF NOT EXISTS
  FOR (d:Decision) REQUIRE d.decision_type IS NOT NULL;

// ====================
// ENUMERATION CONSTRAINTS
// ====================

// Venture status values
CREATE CONSTRAINT venture_status_enum IF NOT EXISTS
  FOR (v:Venture) REQUIRE v.status IN ['active', 'paused', 'archived', 'planned'];

// Venture stage values
CREATE CONSTRAINT venture_stage_enum IF NOT EXISTS
  FOR (v:Venture) REQUIRE v.stage_code IN ['1', '2', '3', '4', '5', '6'];

// Capability tier values
CREATE CONSTRAINT capability_tier_enum IF NOT EXISTS
  FOR (c:Capability) REQUIRE c.tier IN ['core', 'standard', 'premium', 'custom'];

// Capability maturity values
CREATE CONSTRAINT capability_maturity_enum IF NOT EXISTS
  FOR (c:Capability) REQUIRE c.maturity IN ['concept', 'development', 'beta', 'production', 'deprecated'];

// Decision status values
CREATE CONSTRAINT decision_status_enum IF NOT EXISTS
  FOR (d:Decision) REQUIRE d.status IN ['pending', 'approved', 'rejected', 'escalated'];

// Decision authority level values (1=low, 2=medium, 3=high)
CREATE CONSTRAINT decision_authority_enum IF NOT EXISTS
  FOR (d:Decision) REQUIRE d.authority_level IN [1, 2, 3];

// Risk severity values
CREATE CONSTRAINT risk_severity_enum IF NOT EXISTS
  FOR (r:Risk) REQUIRE r.severity IN ['low', 'medium', 'high', 'critical'];

// Agent status values
CREATE CONSTRAINT agent_status_enum IF NOT EXISTS
  FOR (a:Agent) REQUIRE a.status IN ['active', 'inactive', 'training', 'suspended'];

// ====================
// RELATIONSHIP TYPE DEFINITIONS
// ====================

// VENTURES RELATIONSHIPS
// Venture -[:BELONGS_TO]-> OPCO (1:N, mandatory)
// - Every venture belongs to exactly one OPCO
// - Used for territorial routing and OPCO aggregation

// Venture -[:IN_SECTOR]-> Sector (N:N)
// - Ventures classified by economic sector
// - Query: Find all ventures in "Construction" sector

// Venture -[:AT_STAGE]-> Stage (N:1)
// - Venture at current lifecycle stage
// - Query: Find all "MVP" stage ventures

// Venture -[:REQUIRES]-> Capability (N:N)
// - Venture needs this service/capability
// - Used for capability-based routing
// - Query: What does COMM-001 need?

// Venture -[:USES_REPO]-> Repository (N:N)
// - Venture depends on this code repository
// - Query: What repos does COMM-001 use?

// Venture -[:HAS_METRIC]-> Metric (1:N)
// - Venture tracks this KPI
// - Query: Get all metrics for a venture

// Venture -[:HAS_RISK]-> Risk (1:N)
// - Venture exposed to this risk
// - Query: What are the risks for COMM-001?

// Venture -[:ASSIGNED_AGENT]-> Agent (N:N)
// - Agent working on this venture
// - Query: Which agents are on COMM-001?

// ============

// OPCO RELATIONSHIPS
// OPCO -[:OWNS]-> Department (1:N)
// - OPCO owns and governs this department
// - Query: What departments in NC territory?

// OPCO -[:EMPLOYS]-> (implied via Department)
// - Transitive via Department -[:EMPLOYS]-> Agent

// ============

// DEPARTMENT RELATIONSHIPS
// Department -[:EMPLOYS]-> Agent (1:N)
// - Department has these agents on staff
// - Query: List all agents in Sales dept

// Department -[:PROVIDES]-> Capability (1:N)
// - Department provides this capability/service
// - Query: What can Sales dept do?

// ============

// CAPABILITY RELATIONSHIPS
// Capability -[:IMPLEMENTS]-> Skill (N:N)
// - Capability uses these skill components
// - Query: Which skills enable lead capture?

// Capability -[:BACKED_BY]-> Repository (N:N)
// - This code repo implements the capability
// - Query: What repos support lead capture?

// ============

// AGENT RELATIONSHIPS
// Agent -[:MAKES_DECISION]-> Decision (N:N)
// - Agent authorized to make/approve this decision
// - Query: What decisions has agent X made?

// Agent -[:ESCALATES_TO]-> Agent (N:1)
// - This agent escalates to another (chain)
// - Query: Where does deal intake escalate?

// ============

// DECISION RELATIONSHIPS
// Decision -[:AFFECTS]-> Venture (N:1)
// - This decision impacts this venture
// - Query: What pending decisions for COMM-001?

// ====================
// EXAMPLE NODE CREATION (for reference)
// ====================
// These are NOT executed; they show the expected schema

// VENTURE NODE
// CREATE (v:Venture {
//   venture_id: "COMM-001",
//   venture_name: "Ace Senior Care Connect",
//   sector: "Community",
//   sector_code: "COMM",
//   opco_id: "OC-NC-001",
//   stage: "MVP",
//   stage_code: "3",
//   status: "active",
//   mrr: 2500.0,
//   runway_months: 6.5,
//   created_at: 1718000000,
//   updated_at: 1718000000,
//   year_founded: 2026,
//   description: "AI-powered companion and support system for elderly care",
//   revenue_model: "SaaS",
//   cac: 150.0,
//   ltv: 3600.0,
//   churn_rate: 0.05,
//   team_size: 3,
//   founder_email: "contact@venture.com"
// })

// OPCO NODE
// CREATE (o:OPCO {
//   opco_id: "OC-NC-001",
//   opco_name: "North Carolina Construction",
//   territory: "NC",
//   primary_sector: "Construction",
//   secondary_sectors: ["Staffing", "Real Estate"],
//   headquarters: "Charlotte, NC",
//   venture_count: 40,
//   monthly_revenue: 85000.0,
//   created_at: 1718000000,
//   updated_at: 1718000000
// })

// DEPARTMENT NODE
// CREATE (d:Department {
//   department_id: "DEP-EXEC-001",
//   department_name: "Executive Operations",
//   department_code: "EXEC",
//   owner: "Antwuan Divine Johns",
//   capabilities_count: 8,
//   agents_count: 5,
//   budget_annual: 250000.0,
//   created_at: 1718000000,
//   updated_at: 1718000000,
//   authorization_level: 3,
//   description: "Strategic decision-making and venture oversight"
// })

// AGENT NODE
// CREATE (a:Agent {
//   agent_id: "AGT-DEAL-001",
//   agent_name: "Deal Intake Agent",
//   agent_type: "intake",
//   department_id: "DEP-EXEC-001",
//   capabilities: ["lead_capture", "qualification", "routing"],
//   assigned_ventures: 45,
//   decision_authority: 2,
//   success_rate: 0.87,
//   daily_capacity: 100,
//   created_at: 1718000000,
//   updated_at: 1718000000,
//   status: "active",
//   model: "claude-opus",
//   instructions_version: 2
// })

// CAPABILITY NODE
// CREATE (c:Capability {
//   capability_id: "CAP-LEAD-001",
//   capability_name: "Lead Capture & Qualification",
//   capability_code: "LEAD_CAPTURE",
//   category: "Sales",
//   description: "Autonomous lead intake, qualification, and routing",
//   provided_by: "DEP-SALES-001",
//   owner: "Sales Department",
//   tier: "core",
//   maturity: "production",
//   cost_per_use: 5.0,
//   sla_response_hours: 1,
//   success_criteria: ["qualification_rate >= 70%", "routing_accuracy >= 95%"]
// })

// DECISION NODE
// CREATE (d:Decision {
//   decision_id: "DEC-2026-07-001",
//   decision_type: "venture_allocation",
//   title: "Allocate resources to COMM-001",
//   authority_required: 2,
//   authority_level: 3,
//   amount_usd: 15000.0,
//   status: "pending",
//   created_at: 1718000000,
//   updated_at: 1718000000,
//   venture_id: "COMM-001",
//   requested_by: "Sales Agent",
//   approved_by: "Executive",
//   scheduled_review: 1718100000,
//   escalation_count: 0
// })

// ====================
// COMMON QUERY PATHS
// ====================

// Path 1: Venture -> OPCO -> Department -> Agent
// MATCH (v:Venture)-[:BELONGS_TO]->(o:OPCO)-[:OWNS]->(d:Department)-[:EMPLOYS]->(a:Agent)
// WHERE v.venture_id = "COMM-001"
// RETURN v, o, d, a
// Purpose: Route work to correct agent in correct territory

// Path 2: Venture -> Capability <- Department
// MATCH (v:Venture)-[:REQUIRES]->(c:Capability)<-[:PROVIDES]-(d:Department)
// WHERE v.venture_id = "COMM-001"
// RETURN v, c, d
// Purpose: Find which department can service a venture need

// Path 3: Venture -> Capability -> Repository
// MATCH (v:Venture)-[:USES_REPO]->(r:Repository)<-[:BACKED_BY]-(c:Capability)
// WHERE v.venture_id = "COMM-001"
// RETURN v, r, c
// Purpose: Identify code dependencies for a venture

// Path 4: Agent -> Decision -> Venture (escalation)
// MATCH (a1:Agent)-[:MAKES_DECISION]->(d:Decision)-[:AFFECTS]->(v:Venture),
//       (a1)-[:ESCALATES_TO*0..3]->(a2:Agent)
// WHERE v.venture_id = "COMM-001" AND d.status = "pending"
// RETURN a1, d, v, a2
// Purpose: Route pending decisions up escalation chain

// Path 5: Sector -> Ventures -> Capabilities (sector capability view)
// MATCH (s:Sector)<-[:IN_SECTOR]-(v:Venture)-[:REQUIRES]->(c:Capability)
// WHERE s.sector_code = "CONSTR"
// RETURN s, v, c
// Purpose: Find all capability gaps in Construction sector

// ====================
// SCHEMA VERSION & METADATA
// ====================
// Version: 1.0
// Created: 2026-07-16
// Compatible with: Neo4j 5.0+
// Expected node count: ~2,500
//   - 712 Venture nodes
//   - 18 OPCO nodes
//   - 12 Department nodes
//   - 50+ Agent nodes
//   - 25+ Capability nodes
//   - 30+ Decision nodes
//   - 31 Sector nodes
//   - 100+ Skill nodes
//   - 1,600+ Repository nodes
//   - 2,000+ Metric nodes
//   - 500+ Risk nodes
//   - 6 Stage nodes
//
// Expected relationship count: ~15,000+
//   - 712 BELONGS_TO (venture -> OPCO)
//   - 400 IN_SECTOR (venture -> sector)
//   - 712 AT_STAGE (venture -> stage)
//   - 6,542 REQUIRES (venture -> capability)
//   - 1,200 USES_REPO (venture -> repository)
//   - 2,000 HAS_METRIC (venture -> metric)
//   - 500 HAS_RISK (venture -> risk)
//   - 2,000 ASSIGNED_AGENT (venture -> agent)
//   - 18 OWNS (OPCO -> department)
//   - 50 EMPLOYS (department -> agent)
//   - 150 PROVIDES (department -> capability)
//   - 300 IMPLEMENTS (capability -> skill)
//   - 1,000 BACKED_BY (capability -> repository)
//   - 500 MAKES_DECISION (agent -> decision)
//   - 50 ESCALATES_TO (agent -> agent)
//   - 30 AFFECTS (decision -> venture)

// ====================
// INITIALIZATION SEQUENCE
// ====================
// After schema creation, load data in this order:
// 1. CREATE Stage nodes (6 lifecycle stages)
// 2. CREATE Sector nodes (31 economic sectors)
// 3. CREATE Skill nodes (100+ capability taxonomy)
// 4. CREATE OPCO nodes (18 territories)
// 5. CREATE Department nodes (12 per OPCO)
// 6. CREATE Repository nodes (1,600+ from REPOSITORY-REGISTRY.json)
// 7. CREATE Capability nodes (25+ canonical + variants)
// 8. CREATE Agent nodes (50+ per department)
// 9. CREATE Venture nodes (712 from Supabase)
// 10. CREATE Metric nodes (aggregate KPIs)
// 11. CREATE Risk nodes (identified risks)
// 12. CREATE Decision nodes (pending/approved decisions)
// 13. CREATE relationships (in batches)

// Data sources:
// - Supabase tables: ventures, venture_decisions, contacts, products, metrics, risks
// - CSV registries: VENTURES-CAPABILITIES-MAPPED.csv, REPOSITORY-REGISTRY.json
// - Config files: capabilities-catalog.json, agent-registry.json, department-manifest.json
// - Run: populate_venture_knowledge_graph.py to execute this schema + load data
