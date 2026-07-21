// ============================================================================
// IZA OS Neo4j Indexes - Performance Optimization
// ============================================================================
// Indexes for fast lookups on frequently-queried properties
// Optimizes common query patterns across the IZA OS graph
// ============================================================================

// ====================
// SINGLE PROPERTY INDEXES
// ====================

// VENTURE INDEXES
CREATE INDEX venture_id_idx IF NOT EXISTS FOR (v:Venture) ON (v.venture_id);
CREATE INDEX venture_status_idx IF NOT EXISTS FOR (v:Venture) ON (v.status);
CREATE INDEX venture_stage_idx IF NOT EXISTS FOR (v:Venture) ON (v.stage_code);
CREATE INDEX venture_sector_idx IF NOT EXISTS FOR (v:Venture) ON (v.sector_code);
CREATE INDEX venture_mrr_idx IF NOT EXISTS FOR (v:Venture) ON (v.mrr);
CREATE INDEX venture_runway_idx IF NOT EXISTS FOR (v:Venture) ON (v.runway_months);
CREATE INDEX venture_created_idx IF NOT EXISTS FOR (v:Venture) ON (v.created_at);

// OPCO INDEXES
CREATE INDEX opco_id_idx IF NOT EXISTS FOR (o:OPCO) ON (o.opco_id);
CREATE INDEX opco_territory_idx IF NOT EXISTS FOR (o:OPCO) ON (o.territory);
CREATE INDEX opco_primary_sector_idx IF NOT EXISTS FOR (o:OPCO) ON (o.primary_sector);

// DEPARTMENT INDEXES
CREATE INDEX department_id_idx IF NOT EXISTS FOR (d:Department) ON (d.department_id);
CREATE INDEX department_code_idx IF NOT EXISTS FOR (d:Department) ON (d.department_code);
CREATE INDEX department_owner_idx IF NOT EXISTS FOR (d:Department) ON (d.owner);
CREATE INDEX department_auth_level_idx IF NOT EXISTS FOR (d:Department) ON (d.authorization_level);

// AGENT INDEXES
CREATE INDEX agent_id_idx IF NOT EXISTS FOR (a:Agent) ON (a.agent_id);
CREATE INDEX agent_status_idx IF NOT EXISTS FOR (a:Agent) ON (a.status);
CREATE INDEX agent_type_idx IF NOT EXISTS FOR (a:Agent) ON (a.agent_type);
CREATE INDEX agent_authority_idx IF NOT EXISTS FOR (a:Agent) ON (a.decision_authority);
CREATE INDEX agent_success_rate_idx IF NOT EXISTS FOR (a:Agent) ON (a.success_rate);

// CAPABILITY INDEXES
CREATE INDEX capability_id_idx IF NOT EXISTS FOR (c:Capability) ON (c.capability_id);
CREATE INDEX capability_code_idx IF NOT EXISTS FOR (c:Capability) ON (c.capability_code);
CREATE INDEX capability_category_idx IF NOT EXISTS FOR (c:Capability) ON (c.category);
CREATE INDEX capability_tier_idx IF NOT EXISTS FOR (c:Capability) ON (c.tier);
CREATE INDEX capability_maturity_idx IF NOT EXISTS FOR (c:Capability) ON (c.maturity);

// DECISION INDEXES
CREATE INDEX decision_id_idx IF NOT EXISTS FOR (d:Decision) ON (d.decision_id);
CREATE INDEX decision_status_idx IF NOT EXISTS FOR (d:Decision) ON (d.status);
CREATE INDEX decision_type_idx IF NOT EXISTS FOR (d:Decision) ON (d.decision_type);
CREATE INDEX decision_authority_level_idx IF NOT EXISTS FOR (d:Decision) ON (d.authority_level);
CREATE INDEX decision_amount_idx IF NOT EXISTS FOR (d:Decision) ON (d.amount_usd);
CREATE INDEX decision_created_idx IF NOT EXISTS FOR (d:Decision) ON (d.created_at);

// SECTOR INDEXES
CREATE INDEX sector_code_idx IF NOT EXISTS FOR (s:Sector) ON (s.sector_code);
CREATE INDEX sector_name_idx IF NOT EXISTS FOR (s:Sector) ON (s.sector_name);
CREATE INDEX sector_tier_idx IF NOT EXISTS FOR (s:Sector) ON (s.tier);

// SKILL INDEXES
CREATE INDEX skill_id_idx IF NOT EXISTS FOR (s:Skill) ON (s.skill_id);
CREATE INDEX skill_code_idx IF NOT EXISTS FOR (s:Skill) ON (s.skill_code);
CREATE INDEX skill_category_idx IF NOT EXISTS FOR (s:Skill) ON (s.category);

// REPOSITORY INDEXES
CREATE INDEX repository_id_idx IF NOT EXISTS FOR (r:Repository) ON (r.repo_id);
CREATE INDEX repository_language_idx IF NOT EXISTS FOR (r:Repository) ON (r.language);
CREATE INDEX repository_stars_idx IF NOT EXISTS FOR (r:Repository) ON (r.stars);

// METRIC INDEXES
CREATE INDEX metric_id_idx IF NOT EXISTS FOR (m:Metric) ON (m.metric_id);
CREATE INDEX metric_code_idx IF NOT EXISTS FOR (m:Metric) ON (m.metric_code);
CREATE INDEX metric_frequency_idx IF NOT EXISTS FOR (m:Metric) ON (m.frequency);

// RISK INDEXES
CREATE INDEX risk_id_idx IF NOT EXISTS FOR (r:Risk) ON (r.risk_id);
CREATE INDEX risk_type_idx IF NOT EXISTS FOR (r:Risk) ON (r.risk_type);
CREATE INDEX risk_severity_idx IF NOT EXISTS FOR (r:Risk) ON (r.severity);
CREATE INDEX risk_status_idx IF NOT EXISTS FOR (r:Risk) ON (r.status);

// STAGE INDEXES
CREATE INDEX stage_code_idx IF NOT EXISTS FOR (s:Stage) ON (s.stage_code);
CREATE INDEX stage_sequence_idx IF NOT EXISTS FOR (s:Stage) ON (s.stage_sequence);

// ====================
// COMPOSITE INDEXES (Multi-property lookups)
// ====================

// Venture + Stage (common pattern: find all ventures at a stage)
CREATE INDEX venture_stage_status_idx IF NOT EXISTS
  FOR (v:Venture) ON (v.stage_code, v.status);

// Venture + Sector (find ventures in sector with status)
CREATE INDEX venture_sector_status_idx IF NOT EXISTS
  FOR (v:Venture) ON (v.sector_code, v.status);

// Venture + OPCO (routing: find ventures by territory)
CREATE INDEX venture_opco_status_idx IF NOT EXISTS
  FOR (v:Venture) ON (v.opco_id, v.status);

// OPCO + Territory (domain partitioning)
CREATE INDEX opco_territory_sector_idx IF NOT EXISTS
  FOR (o:OPCO) ON (o.territory, o.primary_sector);

// Department + Authorization (decision routing)
CREATE INDEX department_auth_owner_idx IF NOT EXISTS
  FOR (d:Department) ON (d.authorization_level, d.owner);

// Agent + Status + Authority (agent availability)
CREATE INDEX agent_status_authority_idx IF NOT EXISTS
  FOR (a:Agent) ON (a.status, a.decision_authority);

// Agent + Type + Status (agent discovery by role)
CREATE INDEX agent_type_status_idx IF NOT EXISTS
  FOR (a:Agent) ON (a.agent_type, a.status);

// Capability + Category + Maturity (capability discovery)
CREATE INDEX capability_category_maturity_idx IF NOT EXISTS
  FOR (c:Capability) ON (c.category, c.maturity);

// Capability + Tier + Maturity (capability availability)
CREATE INDEX capability_tier_maturity_idx IF NOT EXISTS
  FOR (c:Capability) ON (c.tier, c.maturity);

// Decision + Type + Status (decision routing)
CREATE INDEX decision_type_status_idx IF NOT EXISTS
  FOR (d:Decision) ON (d.decision_type, d.status);

// Decision + Authority Level + Status (escalation routing)
CREATE INDEX decision_authority_status_idx IF NOT EXISTS
  FOR (d:Decision) ON (d.authority_level, d.status);

// Risk + Type + Severity (risk management)
CREATE INDEX risk_type_severity_idx IF NOT EXISTS
  FOR (r:Risk) ON (r.risk_type, r.severity);

// Metric + Code + Frequency (KPI tracking)
CREATE INDEX metric_code_frequency_idx IF NOT EXISTS
  FOR (m:Metric) ON (m.metric_code, m.frequency);

// ====================
// RELATIONSHIP INDEXES
// ====================
// Neo4j 5.0+ supports relationship property indexes for complex pattern matching

// BELONGS_TO relationship index (venture -> OPCO routing)
CREATE INDEX belongs_to_idx IF NOT EXISTS
  FOR ()-[r:BELONGS_TO]-() ON (r.created_at);

// REQUIRES relationship index (venture capability requirements)
CREATE INDEX requires_idx IF NOT EXISTS
  FOR ()-[r:REQUIRES]-() ON (r.priority, r.status);

// PROVIDES relationship index (department capability inventory)
CREATE INDEX provides_idx IF NOT EXISTS
  FOR ()-[r:PROVIDES]-() ON (r.sla_hours, r.cost);

// MAKES_DECISION relationship index (agent decision authority)
CREATE INDEX makes_decision_idx IF NOT EXISTS
  FOR ()-[r:MAKES_DECISION]-() ON (r.authority_level);

// ESCALATES_TO relationship index (agent escalation chain)
CREATE INDEX escalates_to_idx IF NOT EXISTS
  FOR ()-[r:ESCALATES_TO]-() ON (r.escalation_level);

// ASSIGNED_AGENT relationship index (agent assignment tracking)
CREATE INDEX assigned_agent_idx IF NOT EXISTS
  FOR ()-[r:ASSIGNED_AGENT]-() ON (r.assigned_at, r.status);

// ====================
// FULL-TEXT SEARCH INDEXES
// ====================

// Venture full-text search (name + description + sector)
CREATE FULLTEXT INDEX venture_search_idx IF NOT EXISTS
  FOR (v:Venture) ON EACH [v.venture_name, v.description, v.sector];

// Capability full-text search (name + description + category)
CREATE FULLTEXT INDEX capability_search_idx IF NOT EXISTS
  FOR (c:Capability) ON EACH [c.capability_name, c.description, c.category];

// Repository full-text search (name + description + language)
CREATE FULLTEXT INDEX repository_search_idx IF NOT EXISTS
  FOR (r:Repository) ON EACH [r.repo_name, r.description, r.language];

// Agent full-text search (name + type + description)
CREATE FULLTEXT INDEX agent_search_idx IF NOT EXISTS
  FOR (a:Agent) ON EACH [a.agent_name, a.agent_type];

// Skill full-text search (name + category + description)
CREATE FULLTEXT INDEX skill_search_idx IF NOT EXISTS
  FOR (s:Skill) ON EACH [s.skill_name, s.skill_code];

// Decision full-text search (title + type + description)
CREATE FULLTEXT INDEX decision_search_idx IF NOT EXISTS
  FOR (d:Decision) ON EACH [d.title, d.decision_type];

// ====================
// TEMPORAL INDEXES (for time-range queries)
// ====================

// Venture creation time range queries
CREATE INDEX venture_created_range_idx IF NOT EXISTS
  FOR (v:Venture) ON (v.created_at);

// Venture update time range queries
CREATE INDEX venture_updated_range_idx IF NOT EXISTS
  FOR (v:Venture) ON (v.updated_at);

// Decision review time queries
CREATE INDEX decision_review_time_idx IF NOT EXISTS
  FOR (d:Decision) ON (d.scheduled_review);

// Metric update time range queries
CREATE INDEX metric_updated_range_idx IF NOT EXISTS
  FOR (m:Metric) ON (m.last_updated);

// Risk creation time range queries
CREATE INDEX risk_created_range_idx IF NOT EXISTS
  FOR (r:Risk) ON (r.created_at);

// ====================
// QUERY PATTERN OPTIMIZATION
// ====================

// Pattern 1: Venture routing (venture -> OPCO -> department -> agent)
// Optimized by: venture_status_idx, opco_territory_idx, department_auth_level_idx, agent_status_authority_idx

// Pattern 2: Capability discovery (venture requires capability <- provided by department)
// Optimized by: capability_category_maturity_idx, department_auth_owner_idx,
//               requires_idx relationship index

// Pattern 3: Decision escalation (pending decisions by authority level)
// Optimized by: decision_authority_status_idx, agent_status_authority_idx,
//               escalates_to_idx relationship index

// Pattern 4: Sector analytics (all ventures in sector with risks)
// Optimized by: venture_sector_status_idx, risk_type_severity_idx, risk_status_idx

// Pattern 5: Agent availability (active agents by department and authority)
// Optimized by: agent_status_authority_idx, department_auth_owner_idx

// Pattern 6: Venture search (full-text + filters)
// Optimized by: venture_search_idx (full-text), venture_stage_status_idx (filters)

// Pattern 7: Risk management (critical risks across portfolio)
// Optimized by: risk_type_severity_idx, risk_status_idx, venture_sector_status_idx

// ====================
// MAINTENANCE GUIDELINES
// ====================

// Index creation order (performance impact minimized):
// 1. Single property indexes (first)
// 2. Composite indexes (medium impact)
// 3. Relationship indexes (heavy impact during creation)
// 4. Full-text indexes (minimal additional cost after property indexes)
// 5. Temporal indexes (minimal)

// Recommended index refresh schedule:
// - After bulk loads (populate_venture_knowledge_graph.py): CALL db.index.fulltext.awaitEventuallyConsistent()
// - Weekly: Monitor index statistics via CALL db.indexes()
// - Monthly: Review query plans via PROFILE queries

// Index sizing estimates:
// - Single property indexes: ~200MB total
// - Composite indexes: ~150MB total
// - Relationship indexes: ~100MB total
// - Full-text indexes: ~300MB total
// Total estimated: ~750MB (at 2,500 nodes, 15,000 relationships)

// ====================
// SCHEMA VERSION
// ====================
// Version: 1.0
// Created: 2026-07-16
// Compatible with: Neo4j 5.0+
// Expected index count: 55+ indexes
// Expected storage overhead: ~750MB (at scale)
