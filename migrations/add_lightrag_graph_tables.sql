-- LightRAG → Supabase Graph Tables Migration
-- Created: May 14, 2026
-- Phase: Knowledge Graph OS (Task 13, Phase 1B)
-- Purpose: Persistent storage for extracted entities and relationships

-- Graph entities table (extracted by LightRAG pattern matching)
CREATE TABLE IF NOT EXISTS graph_entities (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  entity_type TEXT NOT NULL, -- 'Venture', 'Decision', 'Metric', 'Risk', 'Sector', 'Agent', 'Contact'
  venture_id TEXT, -- Links to ventures table
  description TEXT,
  metadata JSONB DEFAULT '{}',
  extracted_at TIMESTAMP DEFAULT NOW(),
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Graph relationships table (entity connections)
CREATE TABLE IF NOT EXISTS graph_relationships (
  id TEXT PRIMARY KEY,
  source_id TEXT NOT NULL REFERENCES graph_entities(id) ON DELETE CASCADE,
  target_id TEXT NOT NULL REFERENCES graph_entities(id) ON DELETE CASCADE,
  relation_type TEXT NOT NULL, -- 'owns', 'manages', 'escalates', 'executes', 'reports', 'allocates', 'risks', 'benefits', 'inhibits'
  weight FLOAT DEFAULT 1.0,
  context TEXT,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Indexes for fast queries
CREATE INDEX IF NOT EXISTS idx_graph_entities_venture_id ON graph_entities(venture_id);
CREATE INDEX IF NOT EXISTS idx_graph_entities_entity_type ON graph_entities(entity_type);
CREATE INDEX IF NOT EXISTS idx_graph_relationships_source ON graph_relationships(source_id);
CREATE INDEX IF NOT EXISTS idx_graph_relationships_target ON graph_relationships(target_id);
CREATE INDEX IF NOT EXISTS idx_graph_relationships_type ON graph_relationships(relation_type);

-- Grant permissions for Week 0 agents (update these after service role is configured)
-- GRANT SELECT ON graph_entities TO authenticated;
-- GRANT SELECT ON graph_relationships TO authenticated;
