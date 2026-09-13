-- ==============================================================================
-- LT-005 Medical Courier Dispatch: State Machine Revenue Funnel Migration
-- Tables for State Machine tracking, event telemetry, quote capture, and accounts
-- ==============================================================================

-- 1. Table: lt005_funnel_states
CREATE TABLE IF NOT EXISTS lt005_funnel_states (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  facility_id UUID REFERENCES lt005_charlotte_facilities(id) ON DELETE SET NULL,
  facility_name TEXT NOT NULL,
  contact_name TEXT,
  contact_email TEXT,
  contact_phone TEXT,
  current_stage TEXT NOT NULL DEFAULT 'PROSPECT', -- PROSPECT, CONTACTED, DELIVERED_EMAIL, OPENED, CLICKED, REPLIED, QUALIFIED, QUOTE_REQUESTED, QUOTE_SENT, NEGOTIATING, WON, FIRST_ORDER, ACTIVE_CUSTOMER, RECURRING_CUSTOMER, EXPANSION, INACTIVE, REACTIVATION, LOST
  lead_score INTEGER DEFAULT 10,
  segment TEXT, -- laboratory, hospital, dialysis, pharmacy, clinic, snf
  sales_ready BOOLEAN DEFAULT false,
  sales_owner TEXT DEFAULT 'Antwuan',
  current_sequence_id TEXT DEFAULT 'seq_healthcare_funnel_v1',
  last_event_type TEXT,
  last_event_at TIMESTAMPTZ DEFAULT now(),
  metadata JSONB DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now()
);

-- 2. Table: lt005_funnel_events (Append-only Event Ledger)
CREATE TABLE IF NOT EXISTS lt005_funnel_events (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  funnel_state_id UUID REFERENCES lt005_funnel_states(id) ON DELETE CASCADE,
  facility_id UUID,
  contact_email TEXT,
  stage TEXT NOT NULL,
  event_name TEXT NOT NULL, -- email_sent, email_delivered, email_opened, email_clicked, form_started, quote_requested, booking_created, route_locked, account_submitted, churn_flagged
  event_payload JSONB DEFAULT '{}'::jsonb,
  ip_address TEXT,
  user_agent TEXT,
  created_at TIMESTAMPTZ DEFAULT now()
);

-- 3. Table: lt005_quote_requests
CREATE TABLE IF NOT EXISTS lt005_quote_requests (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  facility_name TEXT NOT NULL,
  facility_type TEXT,
  contact_name TEXT,
  contact_email TEXT,
  contact_phone TEXT,
  pickup_address TEXT NOT NULL,
  delivery_address TEXT NOT NULL,
  est_miles NUMERIC(6,2),
  service_level TEXT NOT NULL,
  temp_handling TEXT NOT NULL,
  specimen_type TEXT NOT NULL,
  estimated_amount NUMERIC(10,2) NOT NULL,
  notes TEXT,
  status TEXT DEFAULT 'pending', -- pending, dispatched, expired, converted
  created_at TIMESTAMPTZ DEFAULT now()
);

-- 4. Table: lt005_account_applications (Institutional Net-30 & BAA)
CREATE TABLE IF NOT EXISTS lt005_account_applications (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  legal_name TEXT NOT NULL,
  npi_ein TEXT,
  primary_address TEXT NOT NULL,
  ap_email TEXT NOT NULL,
  ap_phone TEXT,
  director_name TEXT,
  director_phone TEXT,
  access_notes TEXT,
  signatory_name TEXT NOT NULL,
  signatory_title TEXT NOT NULL,
  baa_signed BOOLEAN DEFAULT true,
  terms_status TEXT DEFAULT 'net_30_approved',
  created_at TIMESTAMPTZ DEFAULT now()
);

-- 5. Table: lt005_route_retainers ($1,200/mo Recurring Daily Route Retainers)
CREATE TABLE IF NOT EXISTS lt005_route_retainers (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  practice_name TEXT NOT NULL,
  route_intent TEXT NOT NULL, -- new_recurring, expansion_add_site, reactivation
  coord_email TEXT NOT NULL,
  coord_phone TEXT NOT NULL,
  frequency TEXT NOT NULL,
  time_slot TEXT NOT NULL,
  stop_1 TEXT NOT NULL,
  stop_2 TEXT,
  stop_final TEXT NOT NULL,
  monthly_retainer NUMERIC(10,2) DEFAULT 1200.00,
  notes TEXT,
  status TEXT DEFAULT 'active',
  created_at TIMESTAMPTZ DEFAULT now()
);

-- Indexes for lightning queries
CREATE INDEX IF NOT EXISTS idx_lt005_funnel_stage ON lt005_funnel_states(current_stage);
CREATE INDEX IF NOT EXISTS idx_lt005_funnel_email ON lt005_funnel_states(contact_email);
CREATE INDEX IF NOT EXISTS idx_lt005_funnel_score ON lt005_funnel_states(lead_score);
CREATE INDEX IF NOT EXISTS idx_lt005_events_state ON lt005_funnel_events(funnel_state_id);
CREATE INDEX IF NOT EXISTS idx_lt005_events_type ON lt005_funnel_events(event_name);
CREATE INDEX IF NOT EXISTS idx_lt005_quote_created ON lt005_quote_requests(created_at);

-- Expose to anon and authenticated roles for client forms
GRANT SELECT, INSERT, UPDATE, DELETE ON lt005_funnel_states TO anon, authenticated, service_role;
GRANT SELECT, INSERT, UPDATE, DELETE ON lt005_funnel_events TO anon, authenticated, service_role;
GRANT SELECT, INSERT, UPDATE, DELETE ON lt005_quote_requests TO anon, authenticated, service_role;
GRANT SELECT, INSERT, UPDATE, DELETE ON lt005_account_applications TO anon, authenticated, service_role;
GRANT SELECT, INSERT, UPDATE, DELETE ON lt005_route_retainers TO anon, authenticated, service_role;

-- Enable RLS
ALTER TABLE lt005_funnel_states ENABLE ROW LEVEL SECURITY;
ALTER TABLE lt005_funnel_events ENABLE ROW LEVEL SECURITY;
ALTER TABLE lt005_quote_requests ENABLE ROW LEVEL SECURITY;
ALTER TABLE lt005_account_applications ENABLE ROW LEVEL SECURITY;
ALTER TABLE lt005_route_retainers ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Allow all operations on lt005_funnel_states" ON lt005_funnel_states FOR ALL USING (true) WITH CHECK (true);
CREATE POLICY "Allow all operations on lt005_funnel_events" ON lt005_funnel_events FOR ALL USING (true) WITH CHECK (true);
CREATE POLICY "Allow all operations on lt005_quote_requests" ON lt005_quote_requests FOR ALL USING (true) WITH CHECK (true);
CREATE POLICY "Allow all operations on lt005_account_applications" ON lt005_account_applications FOR ALL USING (true) WITH CHECK (true);
CREATE POLICY "Allow all operations on lt005_route_retainers" ON lt005_route_retainers FOR ALL USING (true) WITH CHECK (true);
