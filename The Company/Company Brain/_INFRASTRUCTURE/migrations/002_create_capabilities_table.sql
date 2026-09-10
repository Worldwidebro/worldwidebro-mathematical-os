-- Migration 002: Create capabilities table for Capability Registry
-- Created: 2026-09-10 | Phase: 1A (Sep 16-30)

CREATE TABLE IF NOT EXISTS capabilities (
    id VARCHAR(26) PRIMARY KEY,                    -- ULID (unique, sortable)
    ref_id VARCHAR(30) NOT NULL UNIQUE,           -- CAP-000001 format
    slug VARCHAR(128) NOT NULL UNIQUE,            -- URL-safe identifier
    
    -- Identity & Classification
    name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    category VARCHAR(50) NOT NULL,                -- sales|operations|finance|etc.
    vertical VARCHAR(50),                         -- medical|general|sector-specific
    maturity VARCHAR(30) NOT NULL,                -- production|beta|alpha
    
    -- Source & Availability
    source VARCHAR(50) NOT NULL,                  -- anthropic|awesome-claude-code|open-source|internal
    source_url TEXT,
    repo_status VARCHAR(30),                      -- active|maintained|archived
    stars INTEGER DEFAULT 0,
    
    -- Skill Definition
    skill_name VARCHAR(255),
    skill_description TEXT,
    triggers TEXT[],                              -- Array of trigger phrases
    
    -- Inputs & Outputs
    inputs_required TEXT[],                       -- Required input fields
    inputs_optional TEXT[],                       -- Optional input fields
    output_format VARCHAR(50),                    -- text|json|markdown|structured
    
    -- Execution Model
    execution_type VARCHAR(50),                   -- skill|command|workflow|mcp_tool
    execution_model VARCHAR(30),                  -- haiku|sonnet|opus
    estimated_tokens INTEGER,
    estimated_latency_ms INTEGER,
    cost_per_invocation DECIMAL(10, 4),
    
    -- HealthRoute-Specific
    healthroute_fit INTEGER CHECK (healthroute_fit >= 0 AND healthroute_fit <= 100),
    healthroute_use_case TEXT,
    healthroute_gap TEXT,
    
    -- Integrations
    integration_supabase BOOLEAN DEFAULT FALSE,
    integration_neo4j BOOLEAN DEFAULT FALSE,
    integration_slack BOOLEAN DEFAULT FALSE,
    integration_custom_mcp BOOLEAN DEFAULT FALSE,
    
    -- Governance
    owner VARCHAR(255),
    approval_status VARCHAR(30),                  -- approved|pending|blocked
    access_control VARCHAR(30),                   -- public|restricted|internal
    
    -- Metadata
    tags TEXT[],
    related_capabilities VARCHAR(26)[],           -- FK references
    version VARCHAR(20) DEFAULT '1.0',
    
    -- Timestamps
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    
    -- Indexes
    CONSTRAINT category_valid CHECK (category IN ('sales', 'operations', 'finance', 'learning', 'knowledge', 'compliance', 'infrastructure'))
);

-- Indexes for common queries
CREATE INDEX idx_capabilities_category ON capabilities(category);
CREATE INDEX idx_capabilities_healthroute_fit ON capabilities(healthroute_fit);
CREATE INDEX idx_capabilities_source ON capabilities(source);
CREATE INDEX idx_capabilities_approval_status ON capabilities(approval_status);
CREATE INDEX idx_capabilities_tags ON capabilities USING GIN(tags);
CREATE INDEX idx_capabilities_created_at ON capabilities(created_at DESC);

-- Enable full-text search on name + description
CREATE INDEX idx_capabilities_search ON capabilities USING GIN(to_tsvector('english', name || ' ' || description));

-- Row-level security
ALTER TABLE capabilities ENABLE ROW LEVEL SECURITY;
CREATE POLICY capabilities_select_policy ON capabilities FOR SELECT USING (
    access_control = 'public' OR 
    access_control = 'internal'  -- Modify per auth context
);

COMMENT ON TABLE capabilities IS 'Machine-readable registry of reusable skills, plugins, workflows, and MCPs for HealthRoute and Company Brain';
COMMENT ON COLUMN capabilities.id IS 'ULID: unique, sortable identifier (permanent)';
COMMENT ON COLUMN capabilities.ref_id IS 'Human-readable reference (CAP-000001)';
COMMENT ON COLUMN capabilities.healthroute_fit IS 'Percentage fit for HealthRoute: 0-100. 80+ = GO, 60-79 = partial, <60 = not recommended';
