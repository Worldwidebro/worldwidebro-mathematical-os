-- Migration: Create venture_leads table for CON-001 lead intake automation
-- Purpose: Support Loop 1 (Lead Intake) in construction automation system

CREATE TABLE IF NOT EXISTS venture_leads (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  venture_id VARCHAR(50) REFERENCES ventures(venture_id) ON DELETE CASCADE,

  -- Lead contact info
  email TEXT NOT NULL,
  phone TEXT,
  name TEXT,

  -- Lead qualification
  budget_min INTEGER,
  budget_max INTEGER,
  timeline VARCHAR(100),
  complexity VARCHAR(50), -- 'low', 'medium', 'high', 'complex'
  project_type TEXT,
  location TEXT,

  -- Lead source & classification
  source VARCHAR(100), -- 'houzz', 'angi', 'google-ads', 'website', 'referral', 'email'
  classified_by_agent BOOLEAN DEFAULT FALSE,
  lead_score INTEGER DEFAULT 0, -- 0-100 (set by Classifier agent)

  -- Status
  status VARCHAR(50) DEFAULT 'new', -- 'new', 'contacted', 'qualified', 'proposal_sent', 'won', 'lost'
  contacted_at TIMESTAMP,
  qualified_at TIMESTAMP,

  -- Metadata
  notes TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  -- Tracking
  loop_triggered_at TIMESTAMP, -- When lead intake loop first processed this
  n8n_workflow_id VARCHAR(255) -- Link to n8n workflow execution
);

-- Indexes for common queries
CREATE INDEX idx_venture_leads_venture ON venture_leads(venture_id);
CREATE INDEX idx_venture_leads_status ON venture_leads(status);
CREATE INDEX idx_venture_leads_source ON venture_leads(source);
CREATE INDEX idx_venture_leads_lead_score ON venture_leads(lead_score DESC);
CREATE INDEX idx_venture_leads_created ON venture_leads(created_at DESC);

-- RLS policies
ALTER TABLE venture_leads ENABLE ROW LEVEL SECURITY;

-- Only the venture owner and AI agents (via service role) can see leads
CREATE POLICY "venture_teams_can_see_leads"
  ON venture_leads FOR SELECT
  USING (venture_id IN (
    SELECT venture_id FROM ventures
    WHERE owner_id = auth.uid() OR team_ids::text LIKE auth.uid()::text
  ));

-- Allow service role (agents) to insert leads
CREATE POLICY "service_role_can_insert_leads"
  ON venture_leads FOR INSERT
  WITH CHECK (true); -- Service role bypasses RLS, this is just for client-side access if needed

-- Auto-update updated_at timestamp
CREATE OR REPLACE FUNCTION public.update_venture_leads_timestamp()
RETURNS TRIGGER AS $$
BEGIN
  new.updated_at = now();
  RETURN new;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE TRIGGER trg_venture_leads_updated_at
  BEFORE UPDATE ON venture_leads
  FOR EACH ROW
  EXECUTE FUNCTION public.update_venture_leads_timestamp();

-- Comment for documentation
COMMENT ON TABLE venture_leads IS 'Stores leads captured by Loop 1 (Lead Intake). Classified and scored by Classifier agent. Used for proposal generation (Loop 2), payment tracking (Loop 3), and bid coordination (Loop 6).';
COMMENT ON COLUMN venture_leads.complexity IS 'Complexity scoring: low (small repair), medium (kitchen/bath), high (addition/reno), complex (multi-phase/structural)';
COMMENT ON COLUMN venture_leads.lead_score IS 'AI-generated lead quality score (0-100). Set by Classifier agent based on budget, timeline, and historical conversion patterns.';
