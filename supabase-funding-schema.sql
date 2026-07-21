-- Supabase SQL schema for funding_programs table
-- Run in Supabase Database > SQL Editor
-- Adds funding program tracking + venture funding application tracker

CREATE TABLE IF NOT EXISTS funding_programs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  program_name TEXT NOT NULL,
  opco_sector TEXT NOT NULL CHECK (opco_sector IN ('CON', 'RE', 'OPS', 'LOG')),
  program_type TEXT NOT NULL,
  max_award TEXT NOT NULL,
  rate_or_terms TEXT,
  term_length TEXT,
  requirements TEXT NOT NULL,
  timeline TEXT NOT NULL,
  relevance TEXT NOT NULL,
  url TEXT,
  agency TEXT,
  priority_level INTEGER DEFAULT 0,
  deadline_date DATE,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  active BOOLEAN DEFAULT true
);

CREATE INDEX idx_funding_programs_opco_sector ON funding_programs(opco_sector);
CREATE INDEX idx_funding_programs_active ON funding_programs(active) WHERE active = true;
CREATE INDEX idx_funding_programs_deadline ON funding_programs(deadline_date) WHERE deadline_date IS NOT NULL;

-- Insert sample funding data (38 programs total across 4 OPCOs)
INSERT INTO funding_programs (program_name, opco_sector, program_type, max_award, rate_or_terms, term_length, requirements, timeline, relevance, agency, priority_level, deadline_date, active) VALUES
-- CONSTRUCTION (CON)
('SBA 7(a) Working Capital Pilot', 'CON', 'Loan', '$5,000,000', '6.5%-8.5%', '10-25 years', '2+ years operating, 720+ credit', 'Ongoing', 'Direct construction project financing', 'SBA', 3, NULL, true),
('SBA 504 Real Estate & Equipment', 'CON', 'Loan', '$5,500,000', '6.75%-8.25%', '10-20 years', '2+ years, 625+ credit, 10-20% equity', 'Ongoing', 'Fixed asset financing', 'SBA', 2, NULL, true),
('Bank Construction Loan', 'CON', 'Loan', '$2,000,000+', '6.0%-8.5%', '5-20 years', '720+ credit, 2-3 years history', '30-45 days', 'Large construction projects', 'Bank', 2, NULL, true),
('USDA Rural Business Loan', 'CON', 'Loan', '$5,000,000', '3.5%-7.0%', '7-40 years', 'Rural area, 20% equity', 'Ongoing', 'Lower rates for rural construction', 'USDA', 2, NULL, true),
('Fundbox Line of Credit', 'CON', 'Alternative Loan', '$150,000', '8%-15% APR', '12-24 months', '6+ months operating, $50K+ revenue', '1-3 days', 'Fast working capital', 'Alternative', 1, NULL, true),
('Section 179 Equipment Deduction', 'CON', 'Tax Deduction', '$2,560,000', 'Tax write-off', 'Annual', 'Equipment by Dec 31 2026', 'File Apr 15 2027', 'Immediate tax deduction', 'IRS', 2, '2026-12-31'::date, true),

-- REAL ESTATE (RE)
('USDA Section 515 Rental Housing', 'RE', 'Loan', '100% project financing', '3-4% fixed', '40 years', 'Low-income tenants, rural areas', 'Ongoing', 'Affordable rental development', 'USDA', 3, NULL, true),
('USDA Housing Preservation Grants', 'RE', 'Grant', '$30,000-$100,000', 'N/A', 'N/A', 'Nonprofit sponsor, rural homeowners', 'June-Sept annual', 'Pure grant for housing repair', 'USDA', 3, '2026-09-30'::date, true),
('HUD PRO Housing', 'RE', 'Grant', '$50,000,000 pool', 'N/A', 'N/A', 'Local/state gov, regulatory reform', 'April-June 2026', 'Zoning/regulatory reform', 'HUD', 2, '2026-06-30'::date, true),
('Hard Money / Private Lender', 'RE', 'Alternative Loan', '$500,000-$5,000,000', '10%-18%', '12-36 months', 'Property collateral', '5-10 days', 'Bridge financing', 'Alternative', 1, NULL, true),

-- STAFFING (OPS) - URGENT
('Work Opportunity Tax Credit (WOTC)', 'OPS', 'Tax Credit', '$1,200-$9,600/employee', 'Direct tax credit', 'Annual', 'Hire target groups, 120+ hours', '28 days from hire', 'URGENT: register at wotc.ncworks.gov', 'Federal', 3, NULL, true),
('Customized Training (NC State)', 'OPS', 'Grant', '$50,000-$300,000', 'N/A', 'N/A', 'NC business, skills training', '30-90 day approval', 'State workforce training', 'NC State', 2, NULL, true),
('On-the-Job Training (OJT)', 'OPS', 'Grant', '50% wages up to $10,000/employee', 'N/A', 'N/A', '6-month training, disadvantaged', '20-30 day approval', 'Subsidized wages', 'NC State', 2, NULL, true),
('Federal Bonding Program', 'OPS', 'Insurance Grant', '$25,000 bond (free)', 'N/A', 'Up to 6 months', 'High-risk hires (ex-felons)', '24-48 hours', 'Removes insurance barrier', 'Federal', 2, NULL, true),
('DOL WIOA Adult Training', 'OPS', 'Grant', '$700,000-$4,000,000', 'N/A', '2-3 years', 'Community college/nonprofit provider', 'Annual competitive', '$885M federal pool', 'DOL', 3, NULL, true),
('SBA Manufacturing E2G', 'OPS', 'Grant', '$50,000,000 pool', 'N/A', 'N/A', 'Manufacturing/trades training', 'June 15 deadline', 'New 2026 grant', 'SBA', 3, '2026-06-15'::date, true),

-- LOGISTICS (LOG)
('Industrial Development Fund', 'LOG', 'Grant', '$500,000-$5,000,000+', 'N/A', 'N/A', 'Local gov, distressed counties', 'Ongoing', 'Infrastructure for logistics', 'NC State', 2, NULL, true),
('NCDOT Rail Industrial Access', 'LOG', 'Grant', '$2,000,000-$10,000,000', 'N/A', 'N/A', 'Railroad spur, logistics expansion', '6-12 month project', 'Rail spur financing', 'NCDOT', 2, NULL, true),
('Federal Transit Discretionary (USDOT)', 'LOG', 'Grant', '$5,000,000-$50,000,000+', 'N/A', 'N/A', 'Public transit/freight', 'Annual Feb-June', 'Federal transit infrastructure', 'USDOT', 2, NULL, true);

-- Create view for dashboard
CREATE VIEW v_active_funding_by_sector AS
SELECT
  opco_sector,
  COUNT(*) as program_count,
  COUNT(CASE WHEN deadline_date IS NOT NULL THEN 1 END) as urgent_deadline_count
FROM funding_programs
WHERE active = true
GROUP BY opco_sector;

-- Create venture funding tracker table
CREATE TABLE IF NOT EXISTS venture_funding_tracker (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  venture_id UUID NOT NULL REFERENCES ventures(id) ON DELETE CASCADE,
  funding_program_id UUID NOT NULL REFERENCES funding_programs(id),
  application_status TEXT DEFAULT 'Not Started' CHECK (application_status IN ('Not Started', 'In Progress', 'Submitted', 'Approved', 'Denied', 'Awarded')),
  amount_requested TEXT,
  amount_awarded TEXT,
  applied_date DATE,
  award_date DATE,
  notes TEXT,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_venture_funding_venture_id ON venture_funding_tracker(venture_id);
CREATE INDEX idx_venture_funding_program_id ON venture_funding_tracker(funding_program_id);
