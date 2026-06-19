-- Migration: Create repos metadata table
-- Date: 2026-05-10
-- Purpose: Store structured metadata for all 853 starred repos for semantic search and venture matching

CREATE TABLE IF NOT EXISTS repos (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

  -- Basic Info
  repo_id VARCHAR(255) UNIQUE NOT NULL,
  name VARCHAR(255) NOT NULL,
  github_url VARCHAR(500),
  owner VARCHAR(255),

  -- Metadata
  purpose TEXT,
  description TEXT,
  maturity VARCHAR(50) CHECK (maturity IN ('experimental', 'beta', 'production', 'mature')),
  license VARCHAR(100),
  language VARCHAR(100),

  -- Structured Data
  capabilities TEXT[] DEFAULT '{}',  -- Array of capability strings
  stack TEXT[] DEFAULT '{}',  -- Tech stack (python, rust, go, etc.)
  dependencies TEXT[] DEFAULT '{}',  -- Related repo names
  business_use_cases TEXT[] DEFAULT '{}',  -- What business problems does it solve?

  -- Integration Metadata
  integration_effort VARCHAR(50) CHECK (integration_effort IN ('low', 'medium', 'high', 'very_high')),
  estimated_integration_days INT,
  cost_estimate VARCHAR(255),  -- "free", "$5K/month", etc.
  startup_complexity VARCHAR(50),

  -- Venture Relevance
  ventures_count INT DEFAULT 0,  -- How many ventures could use this?
  venture_ids TEXT[] DEFAULT '{}',  -- List of venture IDs that need this
  sectors TEXT[] DEFAULT '{}',  -- Which sectors benefit?

  -- Stars & Community
  github_stars INT,
  last_commit_date TIMESTAMP,
  contributors INT,

  -- Vectors & Search
  embedding VECTOR(1536),  -- OpenAI embedding for semantic search (optional, for LlamaIndex)
  full_text_search TSVECTOR,  -- For full-text search

  -- Operational
  indexed_at TIMESTAMP DEFAULT NOW(),
  last_verified TIMESTAMP,
  verification_status VARCHAR(50) DEFAULT 'pending' CHECK (verification_status IN ('pending', 'verified', 'deprecated')),
  notes TEXT,

  -- Tracking
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_repos_name ON repos(name);
CREATE INDEX idx_repos_capabilities ON repos USING GIN(capabilities);
CREATE INDEX idx_repos_maturity ON repos(maturity);
CREATE INDEX idx_repos_integration_effort ON repos(integration_effort);
CREATE INDEX idx_repos_sectors ON repos USING GIN(sectors);
CREATE INDEX idx_repos_venture_ids ON repos USING GIN(venture_ids);
CREATE INDEX idx_repos_full_text_search ON repos USING GIN(full_text_search);
CREATE INDEX idx_repos_created_at ON repos(created_at DESC);

-- Full-text search trigger
CREATE OR REPLACE FUNCTION update_repos_full_text_search()
RETURNS TRIGGER AS $$
BEGIN
  NEW.full_text_search := to_tsvector('english',
    COALESCE(NEW.name, '') || ' ' ||
    COALESCE(NEW.description, '') || ' ' ||
    COALESCE(NEW.purpose, '') || ' ' ||
    COALESCE(array_to_string(NEW.capabilities, ' '), '')
  );
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_repos_full_text_search
  BEFORE INSERT OR UPDATE ON repos
  FOR EACH ROW
  EXECUTE FUNCTION update_repos_full_text_search();

-- Enable RLS
ALTER TABLE repos ENABLE ROW LEVEL SECURITY;

-- RLS Policies
CREATE POLICY "Authenticated users can view repos"
  ON repos FOR SELECT
  USING (auth.role() = 'authenticated');

CREATE POLICY "Authenticated users can insert repos"
  ON repos FOR INSERT
  WITH CHECK (auth.role() = 'authenticated');

CREATE POLICY "Repos can be updated by authenticated users"
  ON repos FOR UPDATE
  USING (auth.role() = 'authenticated');

-- Helper: Repos by capability (useful for venture matching)
CREATE OR REPLACE VIEW repos_by_capability AS
SELECT
  UNNEST(capabilities) as capability,
  COUNT(*) as repo_count,
  ARRAY_AGG(DISTINCT name) as repo_names,
  ARRAY_AGG(DISTINCT maturity) as maturity_levels,
  AVG(CAST(estimated_integration_days AS FLOAT)) as avg_integration_days
FROM repos
WHERE verification_status = 'verified'
GROUP BY capability
ORDER BY repo_count DESC;

-- Helper: Venture-Repo mapping
CREATE OR REPLACE VIEW venture_repo_needs AS
SELECT
  UNNEST(v.required_capabilities) as required_capability,
  v.id as venture_id,
  v.name as venture_name,
  v.sector,
  r.name as repo_name,
  r.integration_effort,
  r.estimated_integration_days,
  r.cost_estimate,
  r.github_url
FROM ventures v
LEFT JOIN repos r ON v.required_capabilities && r.capabilities
WHERE r.verification_status = 'verified'
ORDER BY v.id, r.integration_effort;

-- Grants
GRANT USAGE ON SCHEMA public TO anon, authenticated;
GRANT SELECT ON repos TO anon, authenticated;
GRANT INSERT, UPDATE ON repos TO authenticated;
GRANT SELECT ON repos_by_capability TO anon, authenticated;
GRANT SELECT ON venture_repo_needs TO authenticated;
