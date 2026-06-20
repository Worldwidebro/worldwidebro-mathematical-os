-- SUPABASE SCHEMA FOR LOOPS INFRASTRUCTURE
-- OPS-001 (Staffing) + CON-001 (Construction) + RE-001 (Real Estate)
-- Created: 2026-06-10
-- Database: CivilizationOS (cyhzilqldouzgynacqpe.supabase.co)

-- ============================================================================
-- OPS-001: VENTURE STAFFING OPERATIONS
-- ============================================================================

CREATE TABLE staffing_contractors (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name TEXT NOT NULL,
  email TEXT NOT NULL UNIQUE,
  phone TEXT,
  skills TEXT[] DEFAULT '{}',
  hourly_rate INT NOT NULL,
  availability_hours_per_week INT DEFAULT 40,
  status TEXT NOT NULL DEFAULT 'available',
  nps_score INT CHECK (nps_score >= 0 AND nps_score <= 100),
  total_hours_completed INT DEFAULT 0,
  total_earnings INT DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  metadata JSONB DEFAULT '{}'
);

CREATE TABLE staffing_assignments (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  contractor_id UUID NOT NULL REFERENCES staffing_contractors(id) ON DELETE CASCADE,
  venture_id TEXT NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE,
  expected_hours INT,
  hours_logged INT DEFAULT 0,
  status TEXT NOT NULL DEFAULT 'active',
  quality_score INT CHECK (quality_score >= 0 AND quality_score <= 100),
  venture_nps INT CHECK (venture_nps >= -100 AND venture_nps <= 100),
  contractor_nps INT CHECK (contractor_nps >= -100 AND contractor_nps <= 100),
  notes TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE staffing_time_logs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  assignment_id UUID NOT NULL REFERENCES staffing_assignments(id) ON DELETE CASCADE,
  contractor_id UUID NOT NULL REFERENCES staffing_contractors(id) ON DELETE CASCADE,
  venture_id TEXT NOT NULL,
  date DATE NOT NULL,
  hours DECIMAL(5,2) NOT NULL,
  task_description TEXT,
  approved BOOLEAN DEFAULT FALSE,
  approved_by UUID,
  approved_at TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UNIQUE(assignment_id, contractor_id, date)
);

CREATE TABLE staffing_payroll (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  contractor_id UUID NOT NULL REFERENCES staffing_contractors(id) ON DELETE CASCADE,
  period_start DATE NOT NULL,
  period_end DATE NOT NULL,
  total_hours DECIMAL(7,2) NOT NULL,
  hourly_rate INT NOT NULL,
  gross_amount INT NOT NULL,
  taxes_withheld INT DEFAULT 0,
  net_amount INT NOT NULL,
  payment_method TEXT NOT NULL,
  stripe_transfer_id TEXT,
  status TEXT NOT NULL DEFAULT 'pending',
  payment_date DATE,
  notes TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE staffing_feedback (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  assignment_id UUID NOT NULL REFERENCES staffing_assignments(id) ON DELETE CASCADE,
  contractor_id UUID NOT NULL REFERENCES staffing_contractors(id) ON DELETE CASCADE,
  venture_id TEXT NOT NULL,
  feedback_from TEXT NOT NULL,
  quality_rating INT CHECK (quality_rating >= 1 AND quality_rating <= 5),
  would_work_again BOOLEAN,
  nps_score INT CHECK (nps_score >= -100 AND nps_score <= 100),
  comments TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================================
-- CON-001: CONSTRUCTION VENTURES
-- ============================================================================

CREATE TABLE construction_projects (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  venture_id TEXT NOT NULL,
  name TEXT NOT NULL,
  description TEXT,
  project_type TEXT NOT NULL,
  client_name TEXT NOT NULL,
  client_email TEXT,
  client_phone TEXT,
  location TEXT NOT NULL,
  budget_amount INT NOT NULL,
  budget_spent INT DEFAULT 0,
  timeline_start DATE NOT NULL,
  timeline_end DATE NOT NULL,
  actual_end_date DATE,
  progress_percent INT DEFAULT 0 CHECK (progress_percent >= 0 AND progress_percent <= 100),
  status TEXT NOT NULL DEFAULT 'planning',
  profit_margin_percent DECIMAL(5,2),
  notes TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE construction_daily_logs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  project_id UUID NOT NULL REFERENCES construction_projects(id) ON DELETE CASCADE,
  log_date DATE NOT NULL,
  crew_hours INT NOT NULL,
  crew_members INT NOT NULL,
  tasks_completed TEXT[] DEFAULT '{}',
  issues_encountered TEXT,
  weather_impact TEXT,
  safety_incidents INT DEFAULT 0,
  photo_url TEXT,
  supervisor_name TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UNIQUE(project_id, log_date)
);

CREATE TABLE construction_subcontractors (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  venture_id TEXT NOT NULL,
  name TEXT NOT NULL,
  trade TEXT NOT NULL,
  email TEXT,
  phone TEXT,
  hourly_rate INT,
  license_number TEXT,
  insurance_expiry DATE,
  preferred BOOLEAN DEFAULT FALSE,
  rating DECIMAL(3,2) CHECK (rating >= 0 AND rating <= 5),
  notes TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE construction_subcontractor_assignments (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  project_id UUID NOT NULL REFERENCES construction_projects(id) ON DELETE CASCADE,
  subcontractor_id UUID NOT NULL REFERENCES construction_subcontractors(id) ON DELETE CASCADE,
  start_date DATE NOT NULL,
  end_date DATE,
  scope_of_work TEXT NOT NULL,
  agreed_rate INT NOT NULL,
  estimated_hours INT,
  hours_logged INT DEFAULT 0,
  amount_billed INT DEFAULT 0,
  amount_paid INT DEFAULT 0,
  status TEXT NOT NULL DEFAULT 'scheduled',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE construction_invoices (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  project_id UUID NOT NULL REFERENCES construction_projects(id) ON DELETE CASCADE,
  venture_id TEXT NOT NULL,
  invoice_number TEXT NOT NULL UNIQUE,
  invoice_date DATE NOT NULL,
  due_date DATE NOT NULL,
  labor_amount INT NOT NULL,
  materials_amount INT NOT NULL,
  equipment_amount INT DEFAULT 0,
  contingency_amount INT DEFAULT 0,
  total_amount INT NOT NULL,
  description TEXT,
  status TEXT NOT NULL DEFAULT 'sent',
  paid_date DATE,
  payment_method TEXT,
  notes TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE construction_opportunities (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  venture_id TEXT NOT NULL,
  source TEXT NOT NULL,
  project_name TEXT NOT NULL,
  project_type TEXT,
  estimated_budget INT,
  location TEXT,
  deadline_to_bid DATE,
  description TEXT,
  match_score INT,
  status TEXT NOT NULL DEFAULT 'new',
  notes TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================================
-- RE-001: REAL ESTATE VENTURES
-- ============================================================================

CREATE TABLE real_estate_properties (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  venture_id TEXT NOT NULL,
  address TEXT NOT NULL,
  city TEXT NOT NULL,
  state TEXT NOT NULL,
  zip_code TEXT NOT NULL,
  property_type TEXT NOT NULL,
  bedrooms INT,
  bathrooms INT,
  square_feet INT,
  purchase_date DATE,
  purchase_price INT,
  current_estimated_value INT,
  monthly_rental_income INT DEFAULT 0,
  status TEXT NOT NULL DEFAULT 'occupied',
  notes TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE real_estate_tenants (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  property_id UUID NOT NULL REFERENCES real_estate_properties(id) ON DELETE CASCADE,
  name TEXT NOT NULL,
  email TEXT,
  phone TEXT,
  lease_start DATE NOT NULL,
  lease_end DATE,
  monthly_rent INT NOT NULL,
  security_deposit INT NOT NULL,
  status TEXT NOT NULL DEFAULT 'active',
  nps_score INT CHECK (nps_score >= -100 AND nps_score <= 100),
  notes TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE real_estate_rent_payments (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id UUID NOT NULL REFERENCES real_estate_tenants(id) ON DELETE CASCADE,
  property_id UUID NOT NULL REFERENCES real_estate_properties(id) ON DELETE CASCADE,
  month DATE NOT NULL,
  rent_due INT NOT NULL,
  rent_received INT DEFAULT 0,
  received_date DATE,
  late_fee_applied INT DEFAULT 0,
  status TEXT NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UNIQUE(tenant_id, month)
);

CREATE TABLE real_estate_maintenance_requests (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  property_id UUID NOT NULL REFERENCES real_estate_properties(id) ON DELETE CASCADE,
  reported_by TEXT,
  category TEXT NOT NULL,
  description TEXT NOT NULL,
  priority TEXT NOT NULL DEFAULT 'routine',
  estimated_cost INT,
  actual_cost INT,
  vendor_name TEXT,
  vendor_email TEXT,
  scheduled_date DATE,
  completion_date DATE,
  status TEXT NOT NULL DEFAULT 'open',
  notes TEXT,
  photo_url TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE real_estate_monthly_expenses (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  property_id UUID NOT NULL REFERENCES real_estate_properties(id) ON DELETE CASCADE,
  month DATE NOT NULL,
  mortgage_payment INT DEFAULT 0,
  property_tax INT DEFAULT 0,
  homeowners_insurance INT DEFAULT 0,
  utilities INT DEFAULT 0,
  maintenance_supplies INT DEFAULT 0,
  maintenance_labor INT DEFAULT 0,
  hoa_fees INT DEFAULT 0,
  other_expenses INT DEFAULT 0,
  total_expenses INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UNIQUE(property_id, month)
);

CREATE TABLE real_estate_valuations (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  property_id UUID NOT NULL REFERENCES real_estate_properties(id) ON DELETE CASCADE,
  valuation_date DATE NOT NULL,
  estimated_value INT NOT NULL,
  valuation_method TEXT NOT NULL,
  notes TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================================
-- CORE TRACKING TABLES (All Ventures)
-- ============================================================================

CREATE TABLE venture_health_scores (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  venture_id TEXT NOT NULL UNIQUE,
  health_score INT CHECK (health_score >= 0 AND health_score <= 100),
  metrics JSONB DEFAULT '{}',
  last_calculated TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE loop_execution_logs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  loop_name TEXT NOT NULL,
  venture_id TEXT,
  execution_start TIMESTAMP,
  execution_end TIMESTAMP,
  status TEXT NOT NULL,
  output_summary JSONB DEFAULT '{}',
  error_message TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================================
-- INDEXES FOR PERFORMANCE
-- ============================================================================

CREATE INDEX idx_staffing_contractor_status ON staffing_contractors(status);
CREATE INDEX idx_staffing_assignment_venture ON staffing_assignments(venture_id);
CREATE INDEX idx_staffing_assignment_contractor ON staffing_assignments(contractor_id);
CREATE INDEX idx_staffing_time_logs_date ON staffing_time_logs(date);
CREATE INDEX idx_staffing_payroll_status ON staffing_payroll(status);

CREATE INDEX idx_construction_project_venture ON construction_projects(venture_id);
CREATE INDEX idx_construction_project_status ON construction_projects(status);
CREATE INDEX idx_construction_daily_logs_date ON construction_daily_logs(log_date);
CREATE INDEX idx_construction_invoice_status ON construction_invoices(status);
CREATE INDEX idx_construction_opportunities_venture ON construction_opportunities(venture_id);

CREATE INDEX idx_real_estate_property_venture ON real_estate_properties(venture_id);
CREATE INDEX idx_real_estate_tenant_property ON real_estate_tenants(property_id);
CREATE INDEX idx_real_estate_rent_payment_month ON real_estate_rent_payments(month);
CREATE INDEX idx_real_estate_maintenance_status ON real_estate_maintenance_requests(status);

CREATE INDEX idx_loop_logs_venture ON loop_execution_logs(venture_id);
CREATE INDEX idx_loop_logs_name ON loop_execution_logs(loop_name);

-- ============================================================================
-- VIEWS FOR REPORTING
-- ============================================================================

CREATE VIEW v_staffing_current_status AS
SELECT
  c.id,
  c.name,
  c.hourly_rate,
  c.status,
  COUNT(DISTINCT a.id) as active_assignments,
  COALESCE(SUM(CAST(tl.hours AS INT)), 0) as hours_this_week,
  (COALESCE(SUM(CAST(tl.hours AS INT)), 0)::DECIMAL / c.availability_hours_per_week * 100)::INT as utilization_percent
FROM staffing_contractors c
LEFT JOIN staffing_assignments a ON c.id = a.contractor_id AND a.status = 'active'
LEFT JOIN staffing_time_logs tl ON c.id = tl.contractor_id AND tl.date >= CURRENT_DATE - 7
GROUP BY c.id, c.name, c.hourly_rate, c.status, c.availability_hours_per_week;

CREATE VIEW v_construction_project_financials AS
SELECT
  p.id,
  p.name,
  p.budget_amount,
  p.budget_spent,
  (p.budget_amount - p.budget_spent) as budget_remaining,
  (p.budget_spent::DECIMAL / p.budget_amount * 100)::INT as budget_used_percent,
  p.progress_percent,
  p.status
FROM construction_projects p;

CREATE VIEW v_real_estate_portfolio_summary AS
SELECT
  p.venture_id,
  COUNT(DISTINCT p.id) as total_properties,
  COUNT(DISTINCT CASE WHEN p.status = 'occupied' THEN p.id END) as occupied,
  COUNT(DISTINCT CASE WHEN p.status = 'vacant' THEN p.id END) as vacant,
  SUM(p.current_estimated_value) as portfolio_value,
  SUM(p.monthly_rental_income) as monthly_rental_income,
  SUM(COALESCE(me.total_expenses, 0)) as monthly_expenses
FROM real_estate_properties p
LEFT JOIN real_estate_monthly_expenses me ON p.id = me.property_id
  AND me.month = DATE_TRUNC('month', CURRENT_DATE)
GROUP BY p.venture_id;

-- ============================================================================
-- ENABLE REALTIME (for live dashboard updates)
-- ============================================================================

ALTER PUBLICATION supabase_realtime ADD TABLE staffing_contractors;
ALTER PUBLICATION supabase_realtime ADD TABLE staffing_assignments;
ALTER PUBLICATION supabase_realtime ADD TABLE construction_projects;
ALTER PUBLICATION supabase_realtime ADD TABLE construction_invoices;
ALTER PUBLICATION supabase_realtime ADD TABLE real_estate_properties;
ALTER PUBLICATION supabase_realtime ADD TABLE real_estate_rent_payments;
