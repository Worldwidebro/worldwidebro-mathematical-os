-- IZA OS Phase 3: Capability Request & Fulfillment Schema
-- Transactional database for capability requests, fulfillment tracking, and decision logging
-- Created: 2026-07-16
-- Status: Production-ready with RLS policies and performance indexes

-- ============================================================================
-- TABLE 1: ventures_requesting
-- ============================================================================
-- Core table for capability requests from ventures to departments
-- Tracks request status, assignment, and fulfillment ownership

CREATE TABLE IF NOT EXISTS ventures_requesting (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  venture_id TEXT NOT NULL,
  capability_required TEXT NOT NULL,
  timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  priority TEXT NOT NULL DEFAULT 'medium' CHECK (priority IN ('low', 'medium', 'high', 'urgent')),
  status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'assigned', 'in_progress', 'complete', 'failed')),
  department_assigned TEXT,
  agent_assigned TEXT,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,

  -- Metadata for venture context
  venture_name TEXT,
  venture_sector TEXT,
  requested_by TEXT,  -- User/agent who submitted request
  notes TEXT,

  CONSTRAINT venture_id_not_empty CHECK (venture_id != ''),
  CONSTRAINT capability_required_not_empty CHECK (capability_required != '')
);

-- ============================================================================
-- TABLE 2: capability_fulfillment
-- ============================================================================
-- Tracks actual work done on capability requests by agents
-- Maps 1:N with ventures_requesting (multiple agents can work on same request)

CREATE TABLE IF NOT EXISTS capability_fulfillment (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  request_id UUID NOT NULL REFERENCES ventures_requesting(id) ON DELETE CASCADE,
  agent_id TEXT NOT NULL,
  status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'working', 'complete', 'failed')),
  started_at TIMESTAMP WITH TIME ZONE,
  completed_at TIMESTAMP WITH TIME ZONE,
  result_data JSONB,  -- Flexible storage: deliverables, outputs, links, metrics
  notes TEXT,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,

  -- Audit fields
  created_by TEXT,
  last_updated_by TEXT,

  CONSTRAINT agent_id_not_empty CHECK (agent_id != ''),
  CONSTRAINT completed_after_started CHECK (
    completed_at IS NULL OR started_at IS NULL OR completed_at >= started_at
  )
);

-- ============================================================================
-- TABLE 3: decisions
-- ============================================================================
-- Audit trail of all decisions made by agents/humans across the system
-- Captures decision context, authority level, and audit metadata

CREATE TABLE IF NOT EXISTS decisions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  decision_id TEXT NOT NULL UNIQUE,
  decision_type TEXT NOT NULL,
  authority_level TEXT NOT NULL CHECK (authority_level IN ('venture_lead', 'dept_director', 'hermes', 'human')),
  made_by TEXT NOT NULL,  -- agent_id or human email
  venture_id TEXT,
  department_id TEXT,
  amount NUMERIC(15,2),  -- For financial decisions
  status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'approved', 'rejected', 'escalated')),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  resolved_at TIMESTAMP WITH TIME ZONE,
  escalated_to TEXT,  -- Target authority for escalation
  reasoning JSONB,  -- Full context: factors considered, alternatives, rationale

  -- Audit metadata
  ip_address INET,
  user_agent TEXT,
  session_id TEXT,

  CONSTRAINT decision_id_not_empty CHECK (decision_id != ''),
  CONSTRAINT decision_type_not_empty CHECK (decision_type != ''),
  CONSTRAINT resolved_after_created CHECK (
    resolved_at IS NULL OR resolved_at >= created_at
  )
);

-- ============================================================================
-- TABLE 4: agent_assignments
-- ============================================================================
-- Tracks which agents are assigned to which ventures for which capabilities
-- Supports capacity tracking and workload balancing

CREATE TABLE IF NOT EXISTS agent_assignments (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  agent_id TEXT NOT NULL,
  venture_id TEXT NOT NULL,
  capability TEXT NOT NULL,
  status TEXT NOT NULL DEFAULT 'active' CHECK (status IN ('active', 'paused', 'completed')),
  start_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  end_date TIMESTAMP WITH TIME ZONE,
  hours_allocated NUMERIC(8,2),  -- Total hours budgeted
  hours_used NUMERIC(8,2) DEFAULT 0,  -- Hours consumed
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,

  -- Metadata
  assignment_notes TEXT,
  performance_score NUMERIC(3,1),  -- 0-10 quality score

  CONSTRAINT agent_id_not_empty CHECK (agent_id != ''),
  CONSTRAINT venture_id_not_empty CHECK (venture_id != ''),
  CONSTRAINT capability_not_empty CHECK (capability != ''),
  CONSTRAINT hours_used_le_allocated CHECK (
    hours_allocated IS NULL OR hours_used IS NULL OR hours_used <= hours_allocated
  ),
  CONSTRAINT end_after_start CHECK (
    end_date IS NULL OR end_date >= start_date
  )
);

-- ============================================================================
-- INDEXES: Performance optimization
-- ============================================================================

-- ventures_requesting: Quick lookup by venture & status
CREATE INDEX idx_ventures_requesting_venture_id ON ventures_requesting(venture_id);
CREATE INDEX idx_ventures_requesting_status ON ventures_requesting(status);
CREATE INDEX idx_ventures_requesting_venture_status ON ventures_requesting(venture_id, status);
CREATE INDEX idx_ventures_requesting_department ON ventures_requesting(department_assigned);
CREATE INDEX idx_ventures_requesting_agent ON ventures_requesting(agent_assigned);
CREATE INDEX idx_ventures_requesting_priority_status ON ventures_requesting(priority, status);
CREATE INDEX idx_ventures_requesting_timestamp ON ventures_requesting(timestamp DESC);

-- capability_fulfillment: Quick lookup by request & agent
CREATE INDEX idx_capability_fulfillment_request_id ON capability_fulfillment(request_id);
CREATE INDEX idx_capability_fulfillment_agent_id ON capability_fulfillment(agent_id);
CREATE INDEX idx_capability_fulfillment_status ON capability_fulfillment(status);
CREATE INDEX idx_capability_fulfillment_agent_status ON capability_fulfillment(agent_id, status);
CREATE INDEX idx_capability_fulfillment_created_at ON capability_fulfillment(created_at DESC);

-- decisions: Audit trail lookups
CREATE INDEX idx_decisions_decision_id ON decisions(decision_id);
CREATE INDEX idx_decisions_decision_type ON decisions(decision_type);
CREATE INDEX idx_decisions_venture_id ON decisions(venture_id);
CREATE INDEX idx_decisions_status ON decisions(status);
CREATE INDEX idx_decisions_made_by ON decisions(made_by);
CREATE INDEX idx_decisions_authority ON decisions(authority_level);
CREATE INDEX idx_decisions_created_at ON decisions(created_at DESC);

-- agent_assignments: Capacity & workload tracking
CREATE INDEX idx_agent_assignments_agent_id ON agent_assignments(agent_id);
CREATE INDEX idx_agent_assignments_venture_id ON agent_assignments(venture_id);
CREATE INDEX idx_agent_assignments_capability ON agent_assignments(capability);
CREATE INDEX idx_agent_assignments_status ON agent_assignments(status);
CREATE INDEX idx_agent_assignments_agent_status ON agent_assignments(agent_id, status);

-- ============================================================================
-- ROW-LEVEL SECURITY (RLS) POLICIES
-- ============================================================================

-- Enable RLS on all tables
ALTER TABLE ventures_requesting ENABLE ROW LEVEL SECURITY;
ALTER TABLE capability_fulfillment ENABLE ROW LEVEL SECURITY;
ALTER TABLE decisions ENABLE ROW LEVEL SECURITY;
ALTER TABLE agent_assignments ENABLE ROW LEVEL SECURITY;

-- ============================================================================
-- RLS POLICIES: ventures_requesting
-- ============================================================================

-- Ventures can see only their own requests
CREATE POLICY ventures_requesting_self_read ON ventures_requesting
  FOR SELECT
  USING (venture_id = current_setting('app.venture_id', TRUE) OR auth.uid()::text = 'hermes');

CREATE POLICY ventures_requesting_self_insert ON ventures_requesting
  FOR INSERT
  WITH CHECK (venture_id = current_setting('app.venture_id', TRUE));

CREATE POLICY ventures_requesting_self_update ON ventures_requesting
  FOR UPDATE
  USING (venture_id = current_setting('app.venture_id', TRUE))
  WITH CHECK (venture_id = current_setting('app.venture_id', TRUE));

-- Departments can see requests for their capabilities
CREATE POLICY ventures_requesting_department_read ON ventures_requesting
  FOR SELECT
  USING (
    department_assigned = current_setting('app.department_id', TRUE)
    OR auth.uid()::text = 'hermes'
  );

-- Hermes (system) can see all requests
CREATE POLICY ventures_requesting_hermes_all ON ventures_requesting
  FOR ALL
  USING (auth.uid()::text = 'hermes')
  WITH CHECK (auth.uid()::text = 'hermes');

-- ============================================================================
-- RLS POLICIES: capability_fulfillment
-- ============================================================================

-- Agents can see their own assignments
CREATE POLICY capability_fulfillment_agent_read ON capability_fulfillment
  FOR SELECT
  USING (
    agent_id = current_setting('app.agent_id', TRUE)
    OR auth.uid()::text = 'hermes'
  );

CREATE POLICY capability_fulfillment_agent_update ON capability_fulfillment
  FOR UPDATE
  USING (agent_id = current_setting('app.agent_id', TRUE))
  WITH CHECK (agent_id = current_setting('app.agent_id', TRUE));

-- Ventures can see fulfillment of their own requests
CREATE POLICY capability_fulfillment_venture_read ON capability_fulfillment
  FOR SELECT
  USING (
    EXISTS (
      SELECT 1 FROM ventures_requesting
      WHERE id = request_id
      AND venture_id = current_setting('app.venture_id', TRUE)
    )
    OR auth.uid()::text = 'hermes'
  );

-- Hermes can manage all fulfillment
CREATE POLICY capability_fulfillment_hermes_all ON capability_fulfillment
  FOR ALL
  USING (auth.uid()::text = 'hermes')
  WITH CHECK (auth.uid()::text = 'hermes');

-- ============================================================================
-- RLS POLICIES: decisions
-- ============================================================================

-- Ventures can see decisions affecting them
CREATE POLICY decisions_venture_read ON decisions
  FOR SELECT
  USING (
    venture_id = current_setting('app.venture_id', TRUE)
    OR authority_level = 'venture_lead'
    OR auth.uid()::text = 'hermes'
  );

-- Hermes can see all decisions
CREATE POLICY decisions_hermes_read ON decisions
  FOR SELECT
  USING (auth.uid()::text = 'hermes');

CREATE POLICY decisions_hermes_write ON decisions
  FOR INSERT
  WITH CHECK (auth.uid()::text = 'hermes');

CREATE POLICY decisions_hermes_update ON decisions
  FOR UPDATE
  USING (auth.uid()::text = 'hermes')
  WITH CHECK (auth.uid()::text = 'hermes');

-- Department directors can see decisions for their department
CREATE POLICY decisions_department_read ON decisions
  FOR SELECT
  USING (
    department_id = current_setting('app.department_id', TRUE)
    AND authority_level IN ('dept_director', 'hermes')
  );

-- ============================================================================
-- RLS POLICIES: agent_assignments
-- ============================================================================

-- Agents can see their own assignments
CREATE POLICY agent_assignments_agent_read ON agent_assignments
  FOR SELECT
  USING (
    agent_id = current_setting('app.agent_id', TRUE)
    OR auth.uid()::text = 'hermes'
  );

-- Ventures can see agents assigned to them
CREATE POLICY agent_assignments_venture_read ON agent_assignments
  FOR SELECT
  USING (
    venture_id = current_setting('app.venture_id', TRUE)
    OR auth.uid()::text = 'hermes'
  );

-- Hermes can manage all assignments
CREATE POLICY agent_assignments_hermes_all ON agent_assignments
  FOR ALL
  USING (auth.uid()::text = 'hermes')
  WITH CHECK (auth.uid()::text = 'hermes');

-- ============================================================================
-- AUDIT TRIGGERS: Auto-update timestamps
-- ============================================================================

-- Function to update updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = CURRENT_TIMESTAMP;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers for each table
CREATE TRIGGER ventures_requesting_updated_at_trigger
BEFORE UPDATE ON ventures_requesting
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER capability_fulfillment_updated_at_trigger
BEFORE UPDATE ON capability_fulfillment
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER agent_assignments_updated_at_trigger
BEFORE UPDATE ON agent_assignments
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

-- ============================================================================
-- HELPER FUNCTIONS
-- ============================================================================

-- Function: Get pending requests for a venture
CREATE OR REPLACE FUNCTION get_pending_requests_for_venture(p_venture_id TEXT)
RETURNS TABLE (
  id UUID,
  capability_required TEXT,
  priority TEXT,
  status TEXT,
  department_assigned TEXT,
  created_at TIMESTAMP WITH TIME ZONE
) AS $$
BEGIN
  RETURN QUERY
  SELECT
    ventures_requesting.id,
    ventures_requesting.capability_required,
    ventures_requesting.priority,
    ventures_requesting.status,
    ventures_requesting.department_assigned,
    ventures_requesting.created_at
  FROM ventures_requesting
  WHERE venture_id = p_venture_id
  AND status IN ('pending', 'assigned', 'in_progress')
  ORDER BY priority DESC, created_at ASC;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- Function: Get agent workload (hours used vs allocated)
CREATE OR REPLACE FUNCTION get_agent_workload(p_agent_id TEXT)
RETURNS TABLE (
  venture_id TEXT,
  capability TEXT,
  hours_allocated NUMERIC,
  hours_used NUMERIC,
  utilization_pct NUMERIC
) AS $$
BEGIN
  RETURN QUERY
  SELECT
    agent_assignments.venture_id,
    agent_assignments.capability,
    agent_assignments.hours_allocated,
    agent_assignments.hours_used,
    CASE
      WHEN agent_assignments.hours_allocated IS NULL THEN NULL
      ELSE ROUND((agent_assignments.hours_used / agent_assignments.hours_allocated * 100)::NUMERIC, 1)
    END as utilization_pct
  FROM agent_assignments
  WHERE agent_id = p_agent_id
  AND status = 'active'
  ORDER BY venture_id, capability;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- Function: Get fulfillment status for a request
CREATE OR REPLACE FUNCTION get_fulfillment_status(p_request_id UUID)
RETURNS TABLE (
  agent_id TEXT,
  status TEXT,
  started_at TIMESTAMP WITH TIME ZONE,
  completed_at TIMESTAMP WITH TIME ZONE,
  notes TEXT
) AS $$
BEGIN
  RETURN QUERY
  SELECT
    capability_fulfillment.agent_id,
    capability_fulfillment.status,
    capability_fulfillment.started_at,
    capability_fulfillment.completed_at,
    capability_fulfillment.notes
  FROM capability_fulfillment
  WHERE request_id = p_request_id
  ORDER BY created_at DESC;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- ============================================================================
-- VERIFICATION QUERIES (Run these to test schema)
-- ============================================================================
-- These queries verify the schema is working correctly:
--
-- 1. Check all tables exist and have data:
--    SELECT table_name FROM information_schema.tables
--    WHERE table_schema = 'public' AND table_name IN
--    ('ventures_requesting', 'capability_fulfillment', 'decisions', 'agent_assignments');
--
-- 2. Test RLS policies (as a venture):
--    SET app.venture_id = 'CON-001';
--    SELECT * FROM ventures_requesting WHERE venture_id = 'CON-001';
--
-- 3. Test RLS policies (as Hermes):
--    SELECT auth.uid();  -- Should show hermes UUID
--    SELECT COUNT(*) FROM ventures_requesting;  -- Should see all
--
-- 4. Verify indexes created:
--    SELECT indexname FROM pg_indexes
--    WHERE tablename IN ('ventures_requesting', 'capability_fulfillment', 'decisions', 'agent_assignments')
--    ORDER BY tablename, indexname;
--
-- 5. Test helper functions:
--    SELECT * FROM get_pending_requests_for_venture('CON-001');
--    SELECT * FROM get_agent_workload('agent-123');
--
-- ============================================================================
-- DOCUMENTATION
-- ============================================================================
--
-- SCHEMA OVERVIEW:
--
-- ventures_requesting (capability intake)
--   |
--   ├─→ capability_fulfillment (work tracking)
--   |
--   └─→ agent_assignments (capacity planning)
--
-- decisions (audit trail for all major actions)
--
-- TYPICAL FLOW:
--
-- 1. Venture requests a capability
--    INSERT INTO ventures_requesting (venture_id, capability_required, priority, ...)
--
-- 2. Hermes assigns the request to a department + agent
--    UPDATE ventures_requesting SET department_assigned='FIN', agent_assigned='agent-123', status='assigned'
--
-- 3. Agent starts working and tracks progress
--    INSERT INTO capability_fulfillment (request_id, agent_id, status='working', ...)
--    UPDATE capability_fulfillment SET result_data='...', status='complete' WHERE id=...
--
-- 4. Request marked complete
--    UPDATE ventures_requesting SET status='complete' WHERE id=...
--
-- 5. Decision logged for audit
--    INSERT INTO decisions (decision_id, decision_type, authority_level, made_by, reasoning, ...)
--
-- RLS SECURITY MODEL:
--
-- - Ventures: See only own requests and fulfillment
-- - Agents: See own assignments and fulfillment work
-- - Departments: See requests for their capabilities
-- - Hermes (system): Sees everything, can modify anything
-- - Humans: Routed through authority_level field in decisions
--
-- AUTHORIZATION:
--
-- Use Supabase client-side auth to set these values before queries:
--   supabase.auth.user().id  → Maps to auth.uid()
--   app.venture_id  → Set via: await supabase.rpc('set_venture_id', {id: 'CON-001'})
--   app.department_id  → Set via: await supabase.rpc('set_department_id', {id: 'FIN'})
--   app.agent_id  → Set via: await supabase.rpc('set_agent_id', {id: 'agent-123'})
--
-- ============================================================================
