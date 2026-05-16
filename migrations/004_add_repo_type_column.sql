-- Migration: Add repo_type column to distinguish owned vs starred repos
-- Date: 2026-05-16
-- Purpose: Track which repos are internal products (owned) vs external reference (starred)

-- Add repo_type column
ALTER TABLE repos ADD COLUMN IF NOT EXISTS repo_type VARCHAR(50) DEFAULT 'starred'
  CHECK (repo_type IN ('owned', 'starred'));

-- Add index for repo_type filtering
CREATE INDEX IF NOT EXISTS idx_repos_type ON repos(repo_type);

-- Populate owned repos
UPDATE repos SET repo_type = 'owned' WHERE name IN (
  'pitch-kit',
  'venture-hub',
  'mission-control',
  'omi',
  'iza-os-rag-system',
  'LightRAG',
  'mcp-dashboard',
  'venture-factory-core',
  'vibetunnel',
  'vibe-kanban',
  'ai-venture-studio-template',
  'autonomous-venture-studio',
  'security-stack',
  'opensre',
  'bw-001-lash-extension-studio',
  'con-001-ace-construction',
  'civilization-os-local',
  'thunderbolt'
);

-- Grant permissions
GRANT SELECT ON repos TO anon, authenticated;
