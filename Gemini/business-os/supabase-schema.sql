-- 1. VENTURES TABLE
CREATE TABLE ventures (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  sector TEXT NOT NULL,
  location TEXT,
  status TEXT DEFAULT 'active',
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- 2. DELEGATIONS TABLE (The handshake between ventures)
CREATE TABLE delegations (
  id TEXT PRIMARY KEY,
  requesting_venture_id TEXT REFERENCES ventures(id),
  receiving_venture_id TEXT REFERENCES ventures(id),
  opportunity_type TEXT NOT NULL, -- 'labor_sourcing', 'property_management', 'deal_structuring'
  value_estimate DECIMAL(12,2),
  margin_pct DECIMAL(5,4),
  status TEXT CHECK (status IN ('pending', 'accepted', 'in_progress', 'completed', 'rejected')),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  completed_at TIMESTAMP WITH TIME ZONE
);

-- 3. TRANSACTIONS TABLE (The money flow)
CREATE TABLE transactions (
  id TEXT PRIMARY KEY,
  delegation_id TEXT REFERENCES delegations(id),
  from_venture_id TEXT REFERENCES ventures(id),
  to_venture_id TEXT REFERENCES ventures(id),
  amount DECIMAL(12,2) NOT NULL,
  transaction_type TEXT NOT NULL, -- 'labor_invoice', 'management_fee', 'advisory_fee'
  status TEXT CHECK (status IN ('pending', 'paid', 'disputed')),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- 4. COMPLIANCE RECORDS (The risk mitigation)
CREATE TABLE compliance_records (
  id TEXT PRIMARY KEY,
  venture_id TEXT REFERENCES ventures(id),
  entity_type TEXT, -- 'contractor', 'property', 'deal'
  entity_id TEXT,
  license_verified BOOLEAN DEFAULT FALSE,
  insurance_verified BOOLEAN DEFAULT FALSE,
  background_check_verified BOOLEAN DEFAULT FALSE,
  verified_at TIMESTAMP WITH TIME ZONE,
  verified_by_agent_id TEXT
);

-- 5. PERFORMANCE INDEXES (Critical for 712 ventures)
CREATE INDEX idx_delegations_requesting ON delegations(requesting_venture_id);
CREATE INDEX idx_delegations_receiving ON delegations(receiving_venture_id);
CREATE INDEX idx_delegations_status ON delegations(status);
CREATE INDEX idx_transactions_from ON transactions(from_venture_id);
CREATE INDEX idx_transactions_to ON transactions(to_venture_id);

-- ============================================================================
-- OPPORTUNITY GRAPH SCHEMA (B2B Deal Sourcing)
-- ============================================================================

-- 6. COMPANIES TABLE
CREATE TABLE companies (
  company_id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  industry TEXT NOT NULL,
  location TEXT NOT NULL,
  company_size TEXT,
  estimated_revenue DECIMAL(12,2),
  contact_info JSONB, -- { "primary_contact": "John Doe", "email": "john@company.com", "phone": "..." }
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- 7. ASSETS TABLE (Unused machinery, excess capacity, raw inventory, facilities)
CREATE TABLE assets (
  asset_id TEXT PRIMARY KEY,
  asset_type TEXT NOT NULL, -- 'equipment', 'materials', 'capacity', 'real_estate', 'service_line'
  owner_company_id TEXT REFERENCES companies(company_id) ON DELETE CASCADE,
  estimated_value DECIMAL(12,2),
  location TEXT NOT NULL,
  availability_status TEXT CHECK (availability_status IN ('immediate', 'scheduled', 'leased', 'sold')),
  description TEXT,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- 8. NEEDS TABLE (Demands for labor, tools, material procurement, etc.)
CREATE TABLE needs (
  need_id TEXT PRIMARY KEY,
  buyer_company_id TEXT REFERENCES companies(company_id) ON DELETE CASCADE,
  requirement_type TEXT NOT NULL, -- 'labor_sourcing', 'materials_procurement', 'capacity_booking', 'real_estate_leasing'
  budget DECIMAL(12,2),
  deadline TIMESTAMP WITH TIME ZONE,
  description TEXT,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- 9. DEALS TABLE (Tracks broker commissions, pipeline status, and escrow parameters)
CREATE TABLE deals (
  deal_id TEXT PRIMARY KEY,
  seller_company_id TEXT REFERENCES companies(company_id),
  buyer_company_id TEXT REFERENCES companies(company_id),
  asset_id TEXT REFERENCES assets(asset_id),
  need_id TEXT REFERENCES needs(need_id),
  contract_value DECIMAL(12,2) NOT NULL,
  commission_pct DECIMAL(5,4) DEFAULT 0.05,
  commission_fee DECIMAL(12,2) GENERATED ALWAYS AS (contract_value * commission_pct) STORED,
  status TEXT CHECK (status IN ('discovered', 'qualified', 'outreach', 'negotiation', 'closed_won', 'closed_lost')),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  closed_at TIMESTAMP WITH TIME ZONE
);

CREATE INDEX idx_companies_industry ON companies(industry);
CREATE INDEX idx_assets_owner ON assets(owner_company_id);
CREATE INDEX idx_needs_buyer ON needs(buyer_company_id);
CREATE INDEX idx_deals_status ON deals(status);

-- ============================================================================
-- AI AGENT LEARNING + CONTEXT LAYER (Phase 1 - 2026-07-28)
-- ============================================================================

-- 10. AGENT EXECUTION HISTORY (Audit trail + learning)
CREATE TABLE IF NOT EXISTS agent_execution_history (
  id TEXT PRIMARY KEY,
  task_id TEXT NOT NULL,
  venture_id TEXT REFERENCES ventures(id),
  agent_id TEXT NOT NULL,
  skill_id TEXT NOT NULL,
  input_params JSONB,
  status TEXT CHECK (status IN ('pending', 'in_progress', 'completed', 'failed')),
  cost_usd DECIMAL(10,4),
  duration_seconds INT,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  completed_at TIMESTAMP WITH TIME ZONE
);

-- 11. AGENT PERFORMANCE METRICS
CREATE TABLE IF NOT EXISTS agent_performance (
  id TEXT PRIMARY KEY,
  agent_id TEXT NOT NULL,
  venture_id TEXT REFERENCES ventures(id),
  success_rate DECIMAL(5,4),
  avg_cost_usd DECIMAL(10,4),
  total_executions INT DEFAULT 0,
  successful_executions INT DEFAULT 0,
  failed_executions INT DEFAULT 0,
  last_updated TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- 12. TASK OUTCOMES
CREATE TABLE IF NOT EXISTS task_outcomes (
  id TEXT PRIMARY KEY,
  task_id TEXT NOT NULL,
  result_type TEXT CHECK (result_type IN ('success', 'failure', 'partial', 'timeout')),
  output_data JSONB,
  metrics JSONB,
  feedback TEXT,
  learned_pattern TEXT,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- 13. DECISIONS
CREATE TABLE IF NOT EXISTS decisions (
  id TEXT PRIMARY KEY,
  task_id TEXT NOT NULL,
  agent_id TEXT NOT NULL,
  decision_type TEXT CHECK (decision_type IN ('approve', 'reject', 'escalate', 'defer')),
  rationale TEXT NOT NULL,
  authority_level TEXT CHECK (authority_level IN ('autonomous', 'monitored', 'training', 'human')),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_agent_execution_venture ON agent_execution_history(venture_id);
CREATE INDEX IF NOT EXISTS idx_agent_execution_agent ON agent_execution_history(agent_id);
CREATE INDEX IF NOT EXISTS idx_agent_execution_status ON agent_execution_history(status);
CREATE INDEX IF NOT EXISTS idx_agent_performance_agent ON agent_performance(agent_id);
CREATE INDEX IF NOT EXISTS idx_decisions_task ON decisions(task_id);
CREATE INDEX IF NOT EXISTS idx_decisions_agent ON decisions(agent_id);
CREATE INDEX IF NOT EXISTS idx_task_outcomes_task ON task_outcomes(task_id);

