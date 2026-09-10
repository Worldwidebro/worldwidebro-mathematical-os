-- Migration 004: Create workflow_pauses table for pause/resume orchestration
-- Created: 2026-09-10 | Phase: 1A (Sep 16-30)

CREATE TABLE IF NOT EXISTS workflow_pauses (
    id VARCHAR(26) PRIMARY KEY,                    -- ULID (unique, sortable)
    pause_id VARCHAR(26) NOT NULL UNIQUE,          -- Resume reference
    workflow_id VARCHAR(26) NOT NULL,              -- Which workflow paused
    
    -- Pause Context
    stage_num INTEGER NOT NULL,                    -- Which stage paused (1-N)
    execution_context JSONB NOT NULL,              -- Full context at pause time
    
    -- Resume Instructions
    resume_instructions TEXT,
    inputs_required_to_resume TEXT[],
    
    -- Pause Reason
    reason VARCHAR(50),                            -- user_input|external_wait|manual
    pause_description TEXT,
    
    -- Resume Status
    resumed BOOLEAN DEFAULT FALSE,
    resumed_at TIMESTAMPTZ,
    resume_inputs JSONB,
    
    -- Cleanup
    expires_at TIMESTAMPTZ,                        -- Auto-delete after 7 days
    
    -- Timestamps
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    
    -- Indexes
    CONSTRAINT reason_valid CHECK (reason IN ('user_input', 'external_wait', 'manual', 'approval_gate'))
);

-- Indexes for common queries
CREATE INDEX idx_pauses_workflow_id ON workflow_pauses(workflow_id);
CREATE INDEX idx_pauses_pause_id ON workflow_pauses(pause_id);
CREATE INDEX idx_pauses_resumed ON workflow_pauses(resumed);
CREATE INDEX idx_pauses_created_at ON workflow_pauses(created_at DESC);

-- Auto-cleanup of expired pauses
CREATE OR REPLACE FUNCTION cleanup_expired_pauses()
RETURNS void AS $$
BEGIN
    DELETE FROM workflow_pauses WHERE expires_at < NOW();
END;
$$ LANGUAGE plpgsql;

-- Row-level security
ALTER TABLE workflow_pauses ENABLE ROW LEVEL SECURITY;
CREATE POLICY pauses_select_policy ON workflow_pauses FOR SELECT USING (
    TRUE  -- Modify per auth context
);

COMMENT ON TABLE workflow_pauses IS 'Pause state for long-running workflows (e.g., waiting for user input or external system)';
COMMENT ON COLUMN workflow_pauses.execution_context IS 'Complete context at pause time: all stage outputs, inputs, metadata';
COMMENT ON COLUMN workflow_pauses.pause_id IS 'Reference ID for resume() call (shorter than workflow_id for convenience)';
