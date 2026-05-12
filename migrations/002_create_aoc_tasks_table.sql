-- Migration: Create aoc_tasks table (Work Queue)
-- Date: 2026-05-10
-- Purpose: Single source of truth for all orchestrated work

-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Main tasks table
CREATE TABLE IF NOT EXISTS aoc_tasks (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

  -- Task Definition
  task_type VARCHAR(50) NOT NULL,
  venture_id VARCHAR(50),
  contact_id VARCHAR(50),
  assigned_agent VARCHAR(100),

  -- Execution State
  status VARCHAR(20) DEFAULT 'queued' CHECK (status IN ('queued', 'executing', 'complete', 'failed', 'blocked', 'waiting_for_user')),
  priority INT DEFAULT 5 CHECK (priority >= 1 AND priority <= 10),

  -- Data
  payload JSONB,
  result JSONB,
  error_message TEXT,

  -- Timing
  created_at TIMESTAMP DEFAULT NOW(),
  due_at TIMESTAMP,
  started_at TIMESTAMP,
  completed_at TIMESTAMP,

  -- Tracking
  created_by UUID REFERENCES auth.users(id) ON DELETE SET NULL,
  updated_by UUID REFERENCES auth.users(id) ON DELETE SET NULL,
  updated_at TIMESTAMP DEFAULT NOW(),

  -- Audit
  indexed_at TIMESTAMP
);

-- Indexes for common queries
CREATE INDEX idx_aoc_tasks_status ON aoc_tasks(status);
CREATE INDEX idx_aoc_tasks_assigned_agent ON aoc_tasks(assigned_agent);
CREATE INDEX idx_aoc_tasks_venture_id ON aoc_tasks(venture_id);
CREATE INDEX idx_aoc_tasks_contact_id ON aoc_tasks(contact_id);
CREATE INDEX idx_aoc_tasks_created_at ON aoc_tasks(created_at DESC);
CREATE INDEX idx_aoc_tasks_due_at ON aoc_tasks(due_at);
CREATE INDEX idx_aoc_tasks_status_priority ON aoc_tasks(status, priority DESC);
CREATE INDEX idx_aoc_tasks_type_status ON aoc_tasks(task_type, status);

-- Enable RLS
ALTER TABLE aoc_tasks ENABLE ROW LEVEL SECURITY;

-- RLS Policies
CREATE POLICY "Authenticated users can view tasks"
  ON aoc_tasks FOR SELECT
  USING (auth.role() = 'authenticated');

CREATE POLICY "Tasks can be updated by assigned agent or creator"
  ON aoc_tasks FOR UPDATE
  USING (
    auth.uid()::text = assigned_agent OR
    created_by = auth.uid() OR
    auth.uid() IS NULL
  );

CREATE POLICY "Tasks can be inserted by authenticated users"
  ON aoc_tasks FOR INSERT
  WITH CHECK (auth.role() = 'authenticated');

-- Audit trigger to update updated_at
CREATE OR REPLACE FUNCTION update_aoc_tasks_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_aoc_tasks_updated_at
  BEFORE UPDATE ON aoc_tasks
  FOR EACH ROW
  EXECUTE FUNCTION update_aoc_tasks_updated_at();

-- Helper: Quick query for dashboard
CREATE OR REPLACE VIEW aoc_tasks_summary AS
SELECT
  status,
  COUNT(*) as count,
  COUNT(CASE WHEN priority >= 8 THEN 1 END) as urgent_count,
  MAX(created_at) as last_created,
  MAX(completed_at) as last_completed
FROM aoc_tasks
GROUP BY status;

-- Helper: View of queued tasks by priority
CREATE OR REPLACE VIEW aoc_tasks_queued AS
SELECT
  id,
  task_type,
  venture_id,
  contact_id,
  assigned_agent,
  priority,
  due_at,
  payload,
  created_at
FROM aoc_tasks
WHERE status = 'queued'
ORDER BY priority DESC, created_at ASC;

-- Grants
GRANT USAGE ON SCHEMA public TO anon, authenticated;
GRANT SELECT ON aoc_tasks TO anon, authenticated;
GRANT INSERT, UPDATE ON aoc_tasks TO authenticated;
GRANT SELECT ON aoc_tasks_summary TO anon, authenticated;
GRANT SELECT ON aoc_tasks_queued TO authenticated;
