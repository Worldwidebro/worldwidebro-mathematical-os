-- Deal Ecosystem Schema
-- Referral economy with 4 roles: Originator, Operator, Capital, Platform

-- 1. REFERRAL AGREEMENTS (Network Layer)
CREATE TABLE IF NOT EXISTS referral_agreements (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  referrer_id UUID NOT NULL REFERENCES contacts(id),
  deal_type TEXT NOT NULL,
  referral_fee_percent DECIMAL(5,2) NOT NULL,
  active BOOLEAN DEFAULT TRUE,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- 2. DEALS (Core tracking)
CREATE TABLE IF NOT EXISTS deals (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  deal_id TEXT UNIQUE NOT NULL,
  title TEXT NOT NULL,
  description TEXT,
  originator_id UUID REFERENCES contacts(id),
  operator_id UUID REFERENCES contacts(id),
  capital_provider_id UUID REFERENCES contacts(id),
  deal_value DECIMAL(15,2) NOT NULL,
  deal_status TEXT DEFAULT 'intake',
  cost_percent DECIMAL(5,2) DEFAULT 40,
  referral_percent DECIMAL(5,2) DEFAULT 10,
  operator_percent DECIMAL(5,2) DEFAULT 35,
  platform_percent DECIMAL(5,2) DEFAULT 10,
  profit_buffer_percent DECIMAL(5,2) DEFAULT 5,
  venture_id UUID REFERENCES ventures(id),
  repo_id TEXT,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- 3. DEAL CONTRACTS (Legal layer)
CREATE TABLE IF NOT EXISTS deal_contracts (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  deal_id UUID NOT NULL REFERENCES deals(id),
  contract_type TEXT NOT NULL,
  contract_template JSONB,
  contract_status TEXT DEFAULT 'draft',
  signed_at TIMESTAMP,
  created_at TIMESTAMP DEFAULT NOW()
);

-- 4. DEAL PAYMENTS (Financial execution)
CREATE TABLE IF NOT EXISTS deal_payments (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  deal_id UUID NOT NULL REFERENCES deals(id),
  recipient_id UUID NOT NULL REFERENCES contacts(id),
  recipient_role TEXT NOT NULL,
  amount DECIMAL(15,2) NOT NULL,
  payment_status TEXT DEFAULT 'pending',
  scheduled_date TIMESTAMP,
  completed_at TIMESTAMP,
  created_at TIMESTAMP DEFAULT NOW()
);

-- 5. REPUTATION SCORES (Trust layer)
CREATE TABLE IF NOT EXISTS reputation_scores (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  contact_id UUID NOT NULL REFERENCES contacts(id),
  role TEXT NOT NULL,
  reliability_score INT DEFAULT 50,
  quality_score INT DEFAULT 50,
  payment_history_score INT DEFAULT 50,
  deals_completed INT DEFAULT 0,
  deals_failed INT DEFAULT 0,
  overall_score INT GENERATED ALWAYS AS ((reliability_score + quality_score + payment_history_score) / 3) STORED,
  updated_at TIMESTAMP DEFAULT NOW()
);

-- 6. DEAL AUDIT TRAIL (Compliance)
CREATE TABLE IF NOT EXISTS deal_audit_log (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  deal_id UUID NOT NULL REFERENCES deals(id),
  action TEXT NOT NULL,
  actor_id UUID REFERENCES contacts(id),
  details JSONB,
  timestamp TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_deals_status ON deals(deal_status);
CREATE INDEX idx_deals_originator ON deals(originator_id);
CREATE INDEX idx_payments_status ON deal_payments(payment_status);
