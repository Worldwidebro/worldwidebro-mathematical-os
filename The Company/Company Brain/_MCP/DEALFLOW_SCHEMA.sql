-- DealFlowOS PostgreSQL Schema
-- Authority: DealFlowOS Engine
-- Created: 2026-09-08

-- ============ DEALS TABLE ============
CREATE TABLE IF NOT EXISTS deals (
    id SERIAL PRIMARY KEY,
    company_id VARCHAR(100) UNIQUE NOT NULL,
    company_name VARCHAR(255) NOT NULL,
    stage VARCHAR(50) NOT NULL DEFAULT 'discovered',
    value DECIMAL(15, 2),
    structure_type VARCHAR(100),
    industry VARCHAR(100),
    location VARCHAR(255),
    contact_email VARCHAR(255),
    contact_phone VARCHAR(20),
    notes TEXT,
    score DECIMAL(5, 2) DEFAULT 75,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100),
    source VARCHAR(100)
);

-- ============ DEAL_NOTES TABLE ============
CREATE TABLE IF NOT EXISTS deal_notes (
    id SERIAL PRIMARY KEY,
    deal_id INTEGER NOT NULL REFERENCES deals(id) ON DELETE CASCADE,
    content TEXT NOT NULL,
    note_type VARCHAR(50) DEFAULT 'general',
    created_by VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_pinned BOOLEAN DEFAULT FALSE
);

-- ============ AGENT_RUNS TABLE ============
CREATE TABLE IF NOT EXISTS agent_runs (
    id SERIAL PRIMARY KEY,
    deal_id INTEGER NOT NULL REFERENCES deals(id) ON DELETE CASCADE,
    agent_type VARCHAR(100) NOT NULL,
    agent_name VARCHAR(255),
    status VARCHAR(50) NOT NULL DEFAULT 'pending',
    input_data JSONB,
    results_json JSONB,
    error_message TEXT,
    execution_time_ms INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    started_at TIMESTAMP,
    completed_at TIMESTAMP
);

-- ============ INDEXES ============
CREATE INDEX IF NOT EXISTS idx_deals_stage ON deals(stage);
CREATE INDEX IF NOT EXISTS idx_deals_created_at ON deals(created_at);
CREATE INDEX IF NOT EXISTS idx_deal_notes_deal_id ON deal_notes(deal_id);
CREATE INDEX IF NOT EXISTS idx_agent_runs_deal_id ON agent_runs(deal_id);

-- ============ SAMPLE QUERIES ============

-- List all deals
-- SELECT * FROM deals ORDER BY created_at DESC;

-- Get deal with notes and agent runs
-- SELECT d.*, 
--        (SELECT COUNT(*) FROM deal_notes WHERE deal_id = d.id) as note_count,
--        (SELECT COUNT(*) FROM agent_runs WHERE deal_id = d.id) as run_count
-- FROM deals d
-- WHERE d.id = 1;

-- Count by stage
-- SELECT stage, COUNT(*) as count FROM deals GROUP BY stage ORDER BY count DESC;

-- High-value deals
-- SELECT id, company_name, value, stage FROM deals WHERE value > 1000000 ORDER BY value DESC;
