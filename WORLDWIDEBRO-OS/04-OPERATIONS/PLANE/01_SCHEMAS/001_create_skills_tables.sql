-- Create SkillsLLM integration tables
-- Run this migration in Supabase

-- Table 1: skills (canonical skills from SkillsLLM marketplace)
CREATE TABLE IF NOT EXISTS skills (
  id BIGSERIAL PRIMARY KEY,
  skill_id TEXT UNIQUE NOT NULL,
  name TEXT NOT NULL,
  description TEXT,
  author TEXT,
  github_url TEXT,
  github_stars INT DEFAULT 0,
  github_forks INT DEFAULT 0,
  language TEXT,
  category TEXT,
  related_tags TEXT[],
  engagement_count INT DEFAULT 0,
  embedding_status TEXT DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),
  synced_from_skillsllm_at TIMESTAMP,

  CONSTRAINT skills_name_not_empty CHECK (length(name) > 0)
);

-- Table 2: venture_skills (junction table)
CREATE TABLE IF NOT EXISTS venture_skills (
  id BIGSERIAL PRIMARY KEY,
  venture_id BIGINT NOT NULL REFERENCES ventures(id) ON DELETE CASCADE,
  skill_id BIGINT NOT NULL REFERENCES skills(id) ON DELETE CASCADE,
  relevance_score FLOAT NOT NULL DEFAULT 0.0,
  recommended_by TEXT NOT NULL DEFAULT 'manual',
  notes TEXT,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),

  CONSTRAINT venture_skills_score_range CHECK (relevance_score >= 0.0 AND relevance_score <= 1.0),
  CONSTRAINT venture_skills_unique UNIQUE (venture_id, skill_id)
);

-- Indexes for performance
CREATE INDEX idx_skills_category ON skills(category);
CREATE INDEX idx_skills_language ON skills(language);
CREATE INDEX idx_skills_embedding_status ON skills(embedding_status);
CREATE INDEX idx_venture_skills_venture_id ON venture_skills(venture_id);
CREATE INDEX idx_venture_skills_skill_id ON venture_skills(skill_id);
CREATE INDEX idx_venture_skills_relevance ON venture_skills(relevance_score DESC);
