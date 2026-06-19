-- FIN-036 Arbitrage Nexus — Deal Pipeline Schema
-- Supabase PostgreSQL

-- Core deals table (ingested from Crucix API)
CREATE TABLE IF NOT EXISTS deals (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  deal_id VARCHAR(100) UNIQUE NOT NULL,
  source_feed VARCHAR(100) NOT NULL,  -- Which Crucix feed
  title TEXT NOT NULL,
  description TEXT,
  amount DECIMAL(15,2),  -- Deal value
  currency VARCHAR(3) DEFAULT 'USD',
  
  -- Metadata from Crucix
  external_url TEXT,
  discovered_date TIMESTAMP DEFAULT now(),
  deal_age_days INTEGER,  -- How old is the opportunity
  
  -- FIN-036 Processing
  venture_id VARCHAR(50),  -- Target venture (initially NULL)
  vertical VARCHAR(50),  -- AI, Construction, Real Estate, etc.
  score INTEGER CHECK (score >= 0 AND score <= 100),
  scoring_date TIMESTAMP,
  confidence_level FLOAT CHECK (confidence_level >= 0 AND confidence_level <= 1),
  
  -- Routing
  routed_to_venture VARCHAR(50),
  routing_status VARCHAR(20) DEFAULT 'pending',  -- pending, sent, accepted, rejected
  webhook_sent_at TIMESTAMP,
  venture_response TEXT,
  
  -- Financial
  commission_value DECIMAL(15,2),
  commission_rate FLOAT DEFAULT 0.10,  -- 10% default
  revenue_captured BOOLEAN DEFAULT FALSE,
  
  -- Metadata
  created_at TIMESTAMP DEFAULT now(),
  updated_at TIMESTAMP DEFAULT now(),
  INDEX idx_source_feed(source_feed),
  INDEX idx_venture_id(venture_id),
  INDEX idx_routing_status(routing_status),
  INDEX idx_scoring_date(scoring_date)
);

-- Audit trail for scoring decisions
CREATE TABLE IF NOT EXISTS deal_scoring_logs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  deal_id UUID REFERENCES deals(id) ON DELETE CASCADE,
  model_used VARCHAR(50),  -- claude-opus-4-6, etc.
  scoring_prompt TEXT,
  scoring_response TEXT,
  viability_score INTEGER,
  fit_score INTEGER,
  urgency_score INTEGER,
  confidence_level FLOAT,
  recommendation VARCHAR(500),
  created_at TIMESTAMP DEFAULT now(),
  INDEX idx_deal_id(deal_id)
);

-- Webhook delivery tracking
CREATE TABLE IF NOT EXISTS webhook_deliveries (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  deal_id UUID REFERENCES deals(id) ON DELETE CASCADE,
  venture_id VARCHAR(50),
  webhook_url TEXT,
  payload JSONB,
  response_status INTEGER,
  response_body TEXT,
  retry_count INTEGER DEFAULT 0,
  delivered_at TIMESTAMP,
  failed_at TIMESTAMP,
  created_at TIMESTAMP DEFAULT now(),
  INDEX idx_deal_id(deal_id),
  INDEX idx_venture_id(venture_id)
);

-- Commission tracking
CREATE TABLE IF NOT EXISTS commissions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  deal_id UUID REFERENCES deals(id) ON DELETE CASCADE,
  venture_id VARCHAR(50),
  deal_amount DECIMAL(15,2),
  commission_rate FLOAT,
  commission_earned DECIMAL(15,2),
  payment_status VARCHAR(20) DEFAULT 'pending',  -- pending, paid, failed
  payment_date TIMESTAMP,
  notes TEXT,
  created_at TIMESTAMP DEFAULT now(),
  updated_at TIMESTAMP DEFAULT now(),
  INDEX idx_deal_id(deal_id),
  INDEX idx_venture_id(venture_id),
  INDEX idx_payment_status(payment_status)
);

-- Crucix feed tracking (which feeds we're monitoring)
CREATE TABLE IF NOT EXISTS crucix_feeds (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  feed_name VARCHAR(100) UNIQUE NOT NULL,
  vertical VARCHAR(50),  -- AI, Construction, Real Estate, etc.
  description TEXT,
  api_endpoint VARCHAR(500),
  last_ingested_at TIMESTAMP,
  next_scheduled_ingest TIMESTAMP,
  ingest_frequency_hours INTEGER DEFAULT 2,
  is_active BOOLEAN DEFAULT TRUE,
  total_deals_ingested INTEGER DEFAULT 0,
  created_at TIMESTAMP DEFAULT now(),
  INDEX idx_vertical(vertical),
  INDEX idx_is_active(is_active)
);

-- Create views for reporting

-- Daily deal summary
CREATE OR REPLACE VIEW daily_deal_summary AS
SELECT
  DATE(scoring_date) as date,
  COUNT(*) as total_deals_scored,
  COUNT(CASE WHEN routing_status = 'sent' THEN 1 END) as deals_routed,
  COUNT(CASE WHEN routing_status = 'accepted' THEN 1 END) as deals_accepted,
  SUM(commission_value) as total_commission_value,
  AVG(score) as avg_deal_score
FROM deals
WHERE scoring_date >= DATE_TRUNC('day', now())
GROUP BY DATE(scoring_date);

-- Venture deal feed
CREATE OR REPLACE VIEW venture_deal_feed AS
SELECT
  routed_to_venture as venture_id,
  COUNT(*) as deals_received,
  COUNT(CASE WHEN routing_status = 'accepted' THEN 1 END) as deals_accepted,
  SUM(commission_value) as commission_value
FROM deals
WHERE routed_to_venture IS NOT NULL
GROUP BY routed_to_venture;

-- Enable RLS (Row Level Security) if using auth
ALTER TABLE deals ENABLE ROW LEVEL SECURITY;
ALTER TABLE deal_scoring_logs ENABLE ROW LEVEL SECURITY;
ALTER TABLE webhook_deliveries ENABLE ROW LEVEL SECURITY;
ALTER TABLE commissions ENABLE ROW LEVEL SECURITY;

-- Schema is ready for Python ingestion pipeline
