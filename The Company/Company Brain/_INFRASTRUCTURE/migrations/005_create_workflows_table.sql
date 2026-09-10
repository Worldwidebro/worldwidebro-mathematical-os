-- Migration 005: Create workflows table for workflow definitions
-- Created: 2026-09-10 | Phase: 1A (Sep 16-30)

CREATE TABLE IF NOT EXISTS workflows (
    id VARCHAR(26) PRIMARY KEY,                    -- ULID
    ref_id VARCHAR(30) NOT NULL UNIQUE,           -- WFL-0001 format
    
    -- Workflow Definition
    name VARCHAR(255) NOT NULL,
    description TEXT,
    
    -- Stages & Capabilities
    stages JSONB NOT NULL,                         -- Array of stage definitions with capabilities
    
    -- Metadata
    owner VARCHAR(255),
    tags TEXT[],
    version VARCHAR(20) DEFAULT '1.0',
    
    -- Status
    status VARCHAR(30),                            -- active|archived|draft
    
    -- Timestamps
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_workflows_ref_id ON workflows(ref_id);
CREATE INDEX idx_workflows_status ON workflows(status);
CREATE INDEX idx_workflows_created_at ON workflows(created_at DESC);

-- Row-level security
ALTER TABLE workflows ENABLE ROW LEVEL SECURITY;
CREATE POLICY workflows_select_policy ON workflows FOR SELECT USING (
    status != 'draft'  -- Show active + archived only
);

COMMENT ON TABLE workflows IS 'Workflow definitions: sequences of capabilities to execute in order';
COMMENT ON COLUMN workflows.stages IS 'JSONB array of stage definitions, each with capabilities, inputs, outputs, parallelization flags';
