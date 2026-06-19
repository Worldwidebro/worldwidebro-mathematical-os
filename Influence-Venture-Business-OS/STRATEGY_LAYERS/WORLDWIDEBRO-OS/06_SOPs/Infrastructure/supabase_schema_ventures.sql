-- Worldwidebro OS Ventures Database Schema
-- Persistent Supabase schema for 773 ventures + knowledge graph
-- Created: 2026-06-04

-- ============================================================================
-- TABLE 1: VENTURES (Central registry - replaces CSV)
-- ============================================================================
CREATE TABLE IF NOT EXISTS ventures (
  venture_id VARCHAR(100) PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  sector VARCHAR(100),
  stage VARCHAR(50),
  status VARCHAR(50) DEFAULT 'planned',

  -- Repository & Code
  repo_url VARCHAR(500),
  github_stars INTEGER DEFAULT 0,
  github_issues INTEGER DEFAULT 0,
  github_contributors INTEGER DEFAULT 0,
  github_last_commit TIMESTAMP,
  github_topics TEXT,

  -- Business Model
  business_model VARCHAR(100),
  revenue_model VARCHAR(100),
  target_cac FLOAT,
  target_ltv FLOAT,

  -- Financial (actual)
  revenue_ytd FLOAT DEFAULT 0,
  costs_mom FLOAT DEFAULT 0,
  profit_margin FLOAT,
  burn_rate FLOAT,

  -- Health & Priority
  health_score INTEGER DEFAULT 50,
  research_priority INTEGER DEFAULT 50,

  -- Relationships
  owner_id VARCHAR(100),
  team_ids TEXT,
  blockers TEXT,
  blocked_by TEXT,

  -- Metadata
  description TEXT,
  keywords TEXT,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),
  last_github_sync TIMESTAMP,
  last_research_date TIMESTAMP,

  -- Status tracking
  is_active BOOLEAN DEFAULT TRUE,
  research_status VARCHAR(50),
  decision_status VARCHAR(50)
);

CREATE INDEX idx_ventures_sector ON ventures(sector);
CREATE INDEX idx_ventures_stage ON ventures(stage);
CREATE INDEX idx_ventures_research_priority ON ventures(research_priority DESC);
CREATE INDEX idx_ventures_health ON ventures(health_score DESC);

-- ============================================================================
-- TABLE 2: KNOWLEDGE GRAPH (Relationships between ventures)
-- ============================================================================
CREATE TABLE IF NOT EXISTS knowledge_graph (
  relation_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  from_venture_id VARCHAR(100) REFERENCES ventures(venture_id),
  to_venture_id VARCHAR(100) REFERENCES ventures(venture_id),
  relation_type VARCHAR(50),
  strength INTEGER DEFAULT 5,
  pattern_name VARCHAR(255),
  pattern_url VARCHAR(500),
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_knowledge_from ON knowledge_graph(from_venture_id);
CREATE INDEX idx_knowledge_to ON knowledge_graph(to_venture_id);
CREATE INDEX idx_knowledge_type ON knowledge_graph(relation_type);

-- ============================================================================
-- TABLE 3: STARRED REPO PATTERNS (Pattern library from starred repos)
-- ============================================================================
CREATE TABLE IF NOT EXISTS starred_repo_patterns (
  repo_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  repo_name VARCHAR(255) NOT NULL,
  repo_url VARCHAR(500),
  stars INTEGER DEFAULT 0,
  forks INTEGER DEFAULT 0,
  issues INTEGER DEFAULT 0,
  category VARCHAR(100),
  tags TEXT,
  description TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_patterns_category ON starred_repo_patterns(category);
CREATE INDEX idx_patterns_stars ON starred_repo_patterns(stars DESC);

-- ============================================================================
-- TABLE 4: VENTURE → PATTERN MAPPING (Which ventures use which patterns)
-- ============================================================================
CREATE TABLE IF NOT EXISTS venture_pattern_mapping (
  mapping_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  venture_id VARCHAR(100) REFERENCES ventures(venture_id),
  repo_id UUID REFERENCES starred_repo_patterns(repo_id),
  relevance_score FLOAT,
  is_core_pattern BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_mapping_venture ON venture_pattern_mapping(venture_id);
CREATE INDEX idx_mapping_repo ON venture_pattern_mapping(repo_id);

-- ============================================================================
-- TABLE 5: RESEARCH STATUS (What we know about each venture)
-- ============================================================================
CREATE TABLE IF NOT EXISTS venture_research_status (
  research_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  venture_id VARCHAR(100) REFERENCES ventures(venture_id),
  research_phase VARCHAR(50),
  research_priority INTEGER,
  research_score FLOAT,
  last_research_date TIMESTAMP,
  assigned_researcher VARCHAR(100),
  key_findings TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_research_venture ON venture_research_status(venture_id);
CREATE INDEX idx_research_priority ON venture_research_status(research_priority DESC);

-- ============================================================================
-- TABLE 6: DECISIONS (Log of all decisions made on ventures)
-- ============================================================================
CREATE TABLE IF NOT EXISTS venture_decisions (
  decision_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  venture_id VARCHAR(100) REFERENCES ventures(venture_id),
  decision_type VARCHAR(50),
  decision_reasoning TEXT,
  decided_by VARCHAR(100),
  decided_at TIMESTAMP DEFAULT NOW(),
  status VARCHAR(50) DEFAULT 'pending',
  outcome TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_decisions_venture ON venture_decisions(venture_id);
CREATE INDEX idx_decisions_type ON venture_decisions(decision_type);

-- ============================================================================
-- VIEW: Research priority ranking
-- ============================================================================
CREATE OR REPLACE VIEW venture_research_ranking AS
SELECT
  v.venture_id,
  v.name,
  v.sector,
  v.research_priority,
  COUNT(DISTINCT vpm.repo_id) as pattern_count,
  v.github_stars,
  v.github_contributors
FROM ventures v
LEFT JOIN venture_pattern_mapping vpm ON v.venture_id = vpm.venture_id
WHERE v.is_active = TRUE
GROUP BY v.venture_id, v.name, v.sector, v.research_priority, v.github_stars, v.github_contributors
ORDER BY v.research_priority DESC;
