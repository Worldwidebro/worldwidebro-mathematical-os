-- Real Estate OS - Supabase Schema

-- Users (landlords + tenants)
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email TEXT UNIQUE NOT NULL,
  full_name TEXT NOT NULL,
  role TEXT CHECK (role IN ('landlord', 'tenant')) NOT NULL,
  phone TEXT,
  created_at TIMESTAMP DEFAULT now(),
  updated_at TIMESTAMP DEFAULT now()
);

-- Properties
CREATE TABLE properties (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  created_by UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  address TEXT NOT NULL,
  city TEXT,
  state TEXT,
  zip_code TEXT,
  units_count INT DEFAULT 1,
  created_at TIMESTAMP DEFAULT now(),
  updated_at TIMESTAMP DEFAULT now()
);

CREATE INDEX idx_properties_created_by ON properties(created_by);

-- Units (apartments/rooms within properties)
CREATE TABLE units (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  property_id UUID NOT NULL REFERENCES properties(id) ON DELETE CASCADE,
  unit_number TEXT NOT NULL,
  rent_amount DECIMAL(10,2) NOT NULL,
  tenant_id UUID REFERENCES users(id) ON DELETE SET NULL,
  created_at TIMESTAMP DEFAULT now(),
  updated_at TIMESTAMP DEFAULT now(),
  UNIQUE(property_id, unit_number)
);

CREATE INDEX idx_units_property_id ON units(property_id);
CREATE INDEX idx_units_tenant_id ON units(tenant_id);

-- Leases
CREATE TABLE leases (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  unit_id UUID NOT NULL REFERENCES units(id) ON DELETE CASCADE,
  tenant_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  terms JSONB,
  document_url TEXT,
  created_at TIMESTAMP DEFAULT now(),
  updated_at TIMESTAMP DEFAULT now()
);

CREATE INDEX idx_leases_unit_id ON leases(unit_id);
CREATE INDEX idx_leases_tenant_id ON leases(tenant_id);

-- Rent Payments
CREATE TABLE rent_payments (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  unit_id UUID NOT NULL REFERENCES units(id) ON DELETE CASCADE,
  month DATE NOT NULL,
  amount DECIMAL(10,2) NOT NULL,
  paid_date TIMESTAMP,
  status TEXT CHECK (status IN ('pending', 'paid', 'late')) DEFAULT 'pending',
  stripe_payment_id TEXT,
  created_at TIMESTAMP DEFAULT now(),
  updated_at TIMESTAMP DEFAULT now(),
  UNIQUE(unit_id, month)
);

CREATE INDEX idx_rent_payments_unit_id ON rent_payments(unit_id);
CREATE INDEX idx_rent_payments_status ON rent_payments(status);

-- Maintenance Requests
CREATE TABLE maintenance_requests (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  property_id UUID NOT NULL REFERENCES properties(id) ON DELETE CASCADE,
  tenant_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  description TEXT NOT NULL,
  photo_url TEXT,
  status TEXT CHECK (status IN ('open', 'assigned', 'in_progress', 'completed')) DEFAULT 'open',
  assigned_to UUID REFERENCES users(id) ON DELETE SET NULL,
  completed_date TIMESTAMP,
  created_at TIMESTAMP DEFAULT now(),
  updated_at TIMESTAMP DEFAULT now()
);

CREATE INDEX idx_maintenance_requests_property_id ON maintenance_requests(property_id);
CREATE INDEX idx_maintenance_requests_tenant_id ON maintenance_requests(tenant_id);
CREATE INDEX idx_maintenance_requests_status ON maintenance_requests(status);

-- RLS Policies
ALTER TABLE properties ENABLE ROW LEVEL SECURITY;
ALTER TABLE units ENABLE ROW LEVEL SECURITY;
ALTER TABLE leases ENABLE ROW LEVEL SECURITY;
ALTER TABLE rent_payments ENABLE ROW LEVEL SECURITY;
ALTER TABLE maintenance_requests ENABLE ROW LEVEL SECURITY;

-- Properties: Only landlord can see their properties
CREATE POLICY properties_select ON properties
  FOR SELECT USING (auth.uid() = created_by);

CREATE POLICY properties_insert ON properties
  FOR INSERT WITH CHECK (auth.uid() = created_by);

CREATE POLICY properties_update ON properties
  FOR UPDATE USING (auth.uid() = created_by);

-- Units: Landlord sees all; tenant sees their unit
CREATE POLICY units_select ON units
  FOR SELECT USING (
    EXISTS(SELECT 1 FROM properties WHERE properties.id = units.property_id AND properties.created_by = auth.uid())
    OR units.tenant_id = auth.uid()
  );

-- Leases: Landlord sees all; tenant sees their lease
CREATE POLICY leases_select ON leases
  FOR SELECT USING (
    EXISTS(SELECT 1 FROM units u JOIN properties p ON u.property_id = p.id WHERE u.id = leases.unit_id AND p.created_by = auth.uid())
    OR leases.tenant_id = auth.uid()
  );

-- Rent Payments: Landlord and tenant can view
CREATE POLICY rent_payments_select ON rent_payments
  FOR SELECT USING (
    EXISTS(SELECT 1 FROM units u JOIN properties p ON u.property_id = p.id WHERE u.id = rent_payments.unit_id AND p.created_by = auth.uid())
    OR EXISTS(SELECT 1 FROM units WHERE units.id = rent_payments.unit_id AND units.tenant_id = auth.uid())
  );

-- Maintenance Requests: Landlord and tenant can view
CREATE POLICY maintenance_requests_select ON maintenance_requests
  FOR SELECT USING (
    EXISTS(SELECT 1 FROM properties WHERE properties.id = maintenance_requests.property_id AND properties.created_by = auth.uid())
    OR maintenance_requests.tenant_id = auth.uid()
  );

CREATE POLICY maintenance_requests_insert ON maintenance_requests
  FOR INSERT WITH CHECK (maintenance_requests.tenant_id = auth.uid());

-- Email Deliveries Log Table
CREATE TABLE email_deliveries (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  template TEXT NOT NULL,
  recipient TEXT NOT NULL,
  subject TEXT NOT NULL,
  status TEXT CHECK (status IN ('pending', 'sent', 'failed')) DEFAULT 'pending',
  retry_count INT DEFAULT 0,
  last_error TEXT,
  metadata JSONB,
  created_at TIMESTAMP DEFAULT now(),
  updated_at TIMESTAMP DEFAULT now()
);

CREATE INDEX idx_email_deliveries_status ON email_deliveries(status);
CREATE INDEX idx_email_deliveries_template ON email_deliveries(template);
CREATE INDEX idx_email_deliveries_recipient ON email_deliveries(recipient);
CREATE INDEX idx_email_deliveries_created_at ON email_deliveries(created_at);

-- Stripe Webhooks (idempotent event tracking)
CREATE TABLE stripe_webhooks (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  event_id TEXT UNIQUE NOT NULL,
  event_type TEXT NOT NULL,
  event_data JSONB NOT NULL,
  status TEXT CHECK (status IN ('pending', 'processed', 'failed')) DEFAULT 'pending',
  retry_count INT DEFAULT 0,
  last_error TEXT,
  created_at TIMESTAMP DEFAULT now(),
  processed_at TIMESTAMP
);

CREATE INDEX idx_stripe_webhooks_event_id ON stripe_webhooks(event_id);
CREATE INDEX idx_stripe_webhooks_status ON stripe_webhooks(status);
CREATE INDEX idx_stripe_webhooks_created_at ON stripe_webhooks(created_at);

-- Stripe Disputes (for dispute resolution)
CREATE TABLE stripe_disputes (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  rent_payment_id UUID NOT NULL REFERENCES rent_payments(id) ON DELETE CASCADE,
  stripe_dispute_id TEXT UNIQUE NOT NULL,
  reason TEXT,
  amount DECIMAL(10,2),
  status TEXT CHECK (status IN ('warning_under_review', 'under_review', 'warning_closed', 'lost', 'won')) DEFAULT 'under_review',
  resolved_at TIMESTAMP,
  created_at TIMESTAMP DEFAULT now(),
  updated_at TIMESTAMP DEFAULT now()
);

CREATE INDEX idx_stripe_disputes_rent_payment_id ON stripe_disputes(rent_payment_id);
CREATE INDEX idx_stripe_disputes_status ON stripe_disputes(status);

-- Admin Actions Log (audit trail)
CREATE TABLE admin_actions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  admin_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  action_type TEXT NOT NULL CHECK (action_type IN ('user_created', 'user_suspended', 'user_role_changed', 'payment_disputed', 'payment_resolved')),
  target_user_id UUID REFERENCES users(id) ON DELETE SET NULL,
  target_payment_id UUID REFERENCES rent_payments(id) ON DELETE SET NULL,
  notes TEXT,
  metadata JSONB,
  created_at TIMESTAMP DEFAULT now()
);

CREATE INDEX idx_admin_actions_admin_id ON admin_actions(admin_id);
CREATE INDEX idx_admin_actions_action_type ON admin_actions(action_type);
CREATE INDEX idx_admin_actions_target_user_id ON admin_actions(target_user_id);
CREATE INDEX idx_admin_actions_created_at ON admin_actions(created_at);

-- Payment Disputes (for dispute resolution)
CREATE TABLE payment_disputes (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  payment_id UUID NOT NULL REFERENCES rent_payments(id) ON DELETE CASCADE,
  tenant_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  reason TEXT NOT NULL,
  status TEXT CHECK (status IN ('pending', 'under_review', 'resolved', 'rejected')) DEFAULT 'pending',
  admin_notes TEXT,
  resolved_by UUID REFERENCES users(id) ON DELETE SET NULL,
  resolved_at TIMESTAMP,
  created_at TIMESTAMP DEFAULT now(),
  updated_at TIMESTAMP DEFAULT now()
);

CREATE INDEX idx_payment_disputes_payment_id ON payment_disputes(payment_id);
CREATE INDEX idx_payment_disputes_tenant_id ON payment_disputes(tenant_id);
CREATE INDEX idx_payment_disputes_status ON payment_disputes(status);

-- User suspension tracking
ALTER TABLE users ADD COLUMN IF NOT EXISTS is_suspended BOOLEAN DEFAULT FALSE;
ALTER TABLE users ADD COLUMN IF NOT EXISTS suspension_reason TEXT;

-- Enable RLS on new tables
ALTER TABLE admin_actions ENABLE ROW LEVEL SECURITY;
ALTER TABLE payment_disputes ENABLE ROW LEVEL SECURITY;

-- Admin Actions: Only admins can read/write their own audit logs
CREATE POLICY admin_actions_select ON admin_actions
  FOR SELECT USING (TRUE);

CREATE POLICY admin_actions_insert ON admin_actions
  FOR INSERT WITH CHECK (auth.uid() = admin_id);

-- Payment Disputes: Tenants see their own, admins see all
CREATE POLICY payment_disputes_select ON payment_disputes
  FOR SELECT USING (
    payment_disputes.tenant_id = auth.uid()
    OR TRUE
  );

CREATE POLICY payment_disputes_insert ON payment_disputes
  FOR INSERT WITH CHECK (payment_disputes.tenant_id = auth.uid());

CREATE POLICY payment_disputes_update ON payment_disputes
  FOR UPDATE USING (TRUE);
