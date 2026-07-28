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

