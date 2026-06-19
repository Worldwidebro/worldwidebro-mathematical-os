-- Worldwidebro OS - Operating System Schema
-- Layer 1 (YOU) → Layer 2 (AI+Systems) → Layer 3 (Humans)

-- ============================================================================
-- TABLE 1: VENTURES (Core data)
-- ============================================================================

CREATE TABLE IF NOT EXISTS ventures (
  venture_id VARCHAR(50) PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  sector VARCHAR(100),
  stage VARCHAR(50),
  business_model VARCHAR(100),
  status VARCHAR(50) DEFAULT 'active',

  -- Financial
  revenue_ytd FLOAT DEFAULT 0,
  revenue_target FLOAT,
  costs_mom FLOAT DEFAULT 0,
  burn_rate FLOAT,
  profit_margin FLOAT,

  -- Unit economics
  cac FLOAT,
  ltv FLOAT,
  churn_rate FLOAT,

  -- Health
  health_score INT DEFAULT 50,
  top_risks TEXT,
  blockers TEXT,

  -- Relationships
  owner_id VARCHAR(100),
  team_ids TEXT,
  repo_id VARCHAR(200),
  layer INT,

  -- Metadata
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  last_reviewed_at TIMESTAMP,
  decision_date TIMESTAMP,
  decision_type VARCHAR(50),

  -- AI fields
  classified_by_agent BOOLEAN DEFAULT FALSE,
  validated_by_human BOOLEAN DEFAULT FALSE,
  indexed_to_chroma BOOLEAN DEFAULT FALSE,

  -- Search
  summary TEXT,
  keywords TEXT
);

-- ============================================================================
-- TABLE 2: VENTURE DECISIONS
-- ============================================================================

CREATE TABLE IF NOT EXISTS venture_decisions (
  decision_id VARCHAR(100) PRIMARY KEY,
  venture_id VARCHAR(50) NOT NULL,
  decision_type VARCHAR(50),
  reasoning TEXT,
  decided_by VARCHAR(100),
  decided_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  affected_roles TEXT,
  status VARCHAR(50) DEFAULT 'pending',
  outcome TEXT,
  actual_roi FLOAT,
  completed_at TIMESTAMP
);

-- ============================================================================
-- TABLE 3: TASKS (Contractor workflows)
-- ============================================================================

CREATE TABLE IF NOT EXISTS tasks (
  task_id VARCHAR(100) PRIMARY KEY,
  title VARCHAR(255),
  description TEXT,

  -- Assignment
  assigned_to VARCHAR(100),
  assigned_by VARCHAR(100),
  assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  -- Status
  status VARCHAR(50) DEFAULT 'pending',
  priority INT DEFAULT 3,
  venture_id VARCHAR(50),

  -- Data
  input_data TEXT,
  output_expected TEXT,

  -- Execution
  started_at TIMESTAMP,
  completed_at TIMESTAMP,
  result TEXT,

  -- QA
  validated_by VARCHAR(100),
  validated_at TIMESTAMP
);

-- ============================================================================
-- TABLE 4: GRAPH RELATIONS
-- ============================================================================

CREATE TABLE IF NOT EXISTS graph_relations (
  relation_id VARCHAR(100) PRIMARY KEY,
  from_venture_id VARCHAR(50) NOT NULL,
  to_venture_id VARCHAR(50) NOT NULL,
  relation_type VARCHAR(50),
  strength INT DEFAULT 5,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================================
-- TABLE 5: AGENT LOGS (What AI did)
-- ============================================================================

CREATE TABLE IF NOT EXISTS agent_logs (
  log_id VARCHAR(100) PRIMARY KEY,
  agent_name VARCHAR(100),
  action VARCHAR(255),
  input_data TEXT,
  output_data TEXT,
  triggered_by VARCHAR(100),
  status VARCHAR(50),
  error_message TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  execution_time_ms INT
);

-- ============================================================================
-- TABLE 6: HUMAN AUDIT (Contractor actions)
-- ============================================================================

CREATE TABLE IF NOT EXISTS human_audit (
  audit_id VARCHAR(100) PRIMARY KEY,
  action_type VARCHAR(50),
  human_role VARCHAR(100),
  object_type VARCHAR(50),
  object_id VARCHAR(100),

  before_state TEXT,
  after_state TEXT,
  reason TEXT,

  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================================
-- TABLE 7: COMPONENTS (Core building blocks - 30-50 components)
-- ============================================================================

CREATE TABLE IF NOT EXISTS components (
  component_id VARCHAR(50) PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  category VARCHAR(100),
  description TEXT,
  keywords TEXT,
  complexity VARCHAR(50),
  provides TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_components_category ON components(category);

-- ============================================================================
-- TABLE 8: REPO-COMPONENT MAPPING (Which repos implement which components)
-- ============================================================================

CREATE TABLE IF NOT EXISTS repo_component_mapping (
  mapping_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  repo_id VARCHAR(500),
  repo_name VARCHAR(255),
  component_id VARCHAR(50) REFERENCES components(component_id),
  implementation_type VARCHAR(100),
  relevance_score FLOAT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_repo_component_mapping ON repo_component_mapping(component_id);
CREATE INDEX idx_repo_by_name ON repo_component_mapping(repo_name);

-- ============================================================================
-- TABLE 9: VENTURE-COMPONENT ASSIGNMENT (Which components each venture needs)
-- ============================================================================

CREATE TABLE IF NOT EXISTS venture_component_assignment (
  assignment_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  venture_id VARCHAR(100) REFERENCES ventures(venture_id),
  component_id VARCHAR(50) REFERENCES components(component_id),
  necessity VARCHAR(50),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_venture_components ON venture_component_assignment(venture_id);
CREATE INDEX idx_component_ventures ON venture_component_assignment(component_id);

-- ============================================================================
-- TABLE 10: SKILL EXECUTIONS (Audit trail for all skill runs)
-- ============================================================================

CREATE TABLE IF NOT EXISTS skill_executions (
  execution_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  venture_id VARCHAR(50),
  skill_name VARCHAR(255) NOT NULL,
  skill_phase INT,

  -- Execution metadata
  status VARCHAR(50) DEFAULT 'pending',
  triggered_by VARCHAR(100),
  triggered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  started_at TIMESTAMP,
  completed_at TIMESTAMP,
  execution_time_ms INT,

  -- Input/output
  inputs JSONB,
  outputs JSONB,
  error_message TEXT,

  -- Context
  branch_name VARCHAR(255),
  commit_sha VARCHAR(100),

  -- Tracking
  parent_task_id VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_skill_executions_venture ON skill_executions(venture_id);
CREATE INDEX idx_skill_executions_skill ON skill_executions(skill_name);
CREATE INDEX idx_skill_executions_phase ON skill_executions(skill_phase);
CREATE INDEX idx_skill_executions_status ON skill_executions(status);
CREATE INDEX idx_skill_executions_timestamp ON skill_executions(created_at DESC);

-- ============================================================================
-- TABLE 11: VENTURE SKILL ROADMAP (Planned skill execution per venture)
-- ============================================================================

CREATE TABLE IF NOT EXISTS venture_skill_roadmap (
  roadmap_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  venture_id VARCHAR(50) NOT NULL REFERENCES ventures(venture_id),
  skill_phase INT NOT NULL,
  skill_name VARCHAR(255) NOT NULL,

  -- Planning
  planned_order INT,
  status VARCHAR(50) DEFAULT 'planned',

  -- Dependencies
  depends_on_skills TEXT[],
  blocks_skills TEXT[],

  -- Execution tracking
  planned_start_date DATE,
  planned_completion_date DATE,
  actual_completion_date DATE,

  -- Notes
  description TEXT,
  outcome TEXT,
  lessons_learned TEXT,

  -- Metadata
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_venture_roadmap_venture ON venture_skill_roadmap(venture_id);
CREATE INDEX idx_venture_roadmap_phase ON venture_skill_roadmap(skill_phase);
CREATE INDEX idx_venture_roadmap_status ON venture_skill_roadmap(status);
CREATE UNIQUE INDEX idx_venture_roadmap_unique ON venture_skill_roadmap(venture_id, skill_phase, skill_name);

-- ============================================================================
-- TABLE 12: SKILL TAXONOMY (Master list of all 296 skills with metadata)
-- ============================================================================

CREATE TABLE IF NOT EXISTS skill_taxonomy (
  skill_id VARCHAR(255) PRIMARY KEY,
  skill_name VARCHAR(255) NOT NULL,
  skill_phase INT NOT NULL,
  description TEXT,
  category VARCHAR(100),
  use_cases TEXT[],
  similar_skills TEXT[],
  requires_user_interaction BOOLEAN DEFAULT FALSE,
  supports_parallel_execution BOOLEAN DEFAULT FALSE,
  estimated_duration_minutes INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_skill_taxonomy_phase ON skill_taxonomy(skill_phase);
CREATE INDEX idx_skill_taxonomy_category ON skill_taxonomy(category);

-- ============================================================================
-- VIEWS FOR SKILL EXECUTION
-- ============================================================================

CREATE VIEW IF NOT EXISTS skill_execution_summary AS
SELECT
  venture_id,
  skill_phase,
  COUNT(*) as execution_count,
  COUNT(CASE WHEN status = 'completed' THEN 1 END) as completed_count,
  COUNT(CASE WHEN status = 'failed' THEN 1 END) as failed_count,
  ROUND(AVG(execution_time_ms)) as avg_execution_ms,
  MAX(completed_at) as last_executed
FROM skill_executions
WHERE status IN ('completed', 'failed')
GROUP BY venture_id, skill_phase;

CREATE VIEW IF NOT EXISTS venture_roadmap_status AS
SELECT
  vsr.venture_id,
  v.name as venture_name,
  COUNT(*) as total_skills,
  COUNT(CASE WHEN vsr.status = 'completed' THEN 1 END) as completed,
  COUNT(CASE WHEN vsr.status = 'in_progress' THEN 1 END) as in_progress,
  COUNT(CASE WHEN vsr.status = 'blocked' THEN 1 END) as blocked,
  ROUND(100.0 * COUNT(CASE WHEN vsr.status = 'completed' THEN 1 END) / COUNT(*), 1) as completion_percentage
FROM venture_skill_roadmap vsr
JOIN ventures v ON vsr.venture_id = v.venture_id
GROUP BY vsr.venture_id, v.name;

-- ============================================================================
-- VIEWS
-- ============================================================================

CREATE VIEW IF NOT EXISTS venture_health_dashboard AS
SELECT
  venture_id,
  name,
  sector,
  stage,
  health_score,
  revenue_ytd,
  costs_mom,
  CASE
    WHEN health_score > 70 THEN 'GREEN'
    WHEN health_score > 40 THEN 'YELLOW'
    ELSE 'RED'
  END as status
FROM ventures
WHERE status = 'active'
ORDER BY health_score DESC;

CREATE VIEW IF NOT EXISTS layer_overview AS
SELECT
  layer,
  COUNT(*) as count,
  SUM(revenue_ytd) as revenue,
  AVG(health_score) as health
FROM ventures
WHERE status = 'active'
GROUP BY layer;

-- ============================================================================
-- SAMPLE DATA
-- ============================================================================

INSERT INTO ventures (venture_id, name, sector, stage, revenue_ytd, costs_mom, health_score, layer)
VALUES
  ('FIN-001', 'GenixBank', 'financial', 'planned', 0, 2000, 30, 1),
  ('HRMS-001', 'HRMS Solutions', 'hr-tech', 'mvp', 50000, 5000, 65, 2),
  ('CON-001', 'Construction Co', 'construction', 'validation', 120000, 8000, 75, 3)
ON CONFLICT DO NOTHING;
