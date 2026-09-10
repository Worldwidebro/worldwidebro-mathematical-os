-- Migration 003: Create capability_executions table for audit logging
-- Created: 2026-09-10 | Phase: 1A (Sep 16-30)

CREATE TABLE IF NOT EXISTS capability_executions (
    id VARCHAR(26) PRIMARY KEY,                    -- ULID (unique, sortable)
    capability_id VARCHAR(26) NOT NULL REFERENCES capabilities(id),
    
    -- Execution Context
    workflow_id VARCHAR(26),                       -- FK to workflows (if part of workflow)
    session_id VARCHAR(255),                       -- Claude session identifier
    
    -- Inputs & Outputs
    inputs JSONB,                                  -- Input parameters
    output JSONB,                                  -- Execution output
    error TEXT,                                    -- Error message (if failed)
    
    -- Performance Metrics
    latency_ms INTEGER,                            -- Wall-clock execution time
    tokens_used INTEGER,                           -- LLM tokens consumed
    cost_usd DECIMAL(10, 4),                       -- Cost in USD
    
    -- Status & Result
    status VARCHAR(30) NOT NULL,                   -- success|error|timeout|cancelled
    outcome_summary TEXT,                          -- One-line summary
    
    -- Governance & Tracking
    executed_by VARCHAR(255),                      -- User or agent ID
    approval_required BOOLEAN DEFAULT FALSE,
    approved_by VARCHAR(255),
    approved_at TIMESTAMPTZ,
    
    -- Timestamps
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    
    -- Indexes
    CONSTRAINT status_valid CHECK (status IN ('success', 'error', 'timeout', 'cancelled', 'pending'))
);

-- Indexes for common queries
CREATE INDEX idx_executions_capability_id ON capability_executions(capability_id);
CREATE INDEX idx_executions_workflow_id ON capability_executions(workflow_id);
CREATE INDEX idx_executions_status ON capability_executions(status);
CREATE INDEX idx_executions_created_at ON capability_executions(created_at DESC);
CREATE INDEX idx_executions_cost ON capability_executions(cost_usd DESC);

-- Composite index for audit queries
CREATE INDEX idx_executions_audit ON capability_executions(capability_id, created_at DESC, status);

-- Row-level security
ALTER TABLE capability_executions ENABLE ROW LEVEL SECURITY;
CREATE POLICY executions_select_policy ON capability_executions FOR SELECT USING (
    TRUE  -- Modify per auth context for sensitive data
);

COMMENT ON TABLE capability_executions IS 'Audit log of all capability executions: inputs, outputs, costs, latency, errors';
COMMENT ON COLUMN capability_executions.tokens_used IS 'LLM token consumption for cost tracking and optimization';
COMMENT ON COLUMN capability_executions.cost_usd IS 'Calculated cost based on model + token count';
