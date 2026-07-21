-- Writing Engine Tables for Content Drafts, Brand Voices, Compliance, & Metrics
-- Execute in Supabase SQL Editor (CivilizationOS project)

CREATE TABLE IF NOT EXISTS content_drafts (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  venture_id VARCHAR(50) NOT NULL,
  content_type VARCHAR(50) NOT NULL,
  title VARCHAR(255),
  draft_text TEXT,
  seo_keywords TEXT,
  brand_voice_override TEXT,
  status VARCHAR(20) DEFAULT 'draft',
  risk_score VARCHAR(10) DEFAULT 'low',
  requires_legal_review BOOLEAN DEFAULT FALSE,
  approved_by UUID,
  approval_date TIMESTAMP,
  published_url VARCHAR(500),
  ctr DECIMAL(5,2) DEFAULT 0,
  conversions INTEGER DEFAULT 0,
  created_at TIMESTAMP DEFAULT now(),
  updated_at TIMESTAMP DEFAULT now(),
  created_by UUID,

  CONSTRAINT valid_status CHECK (status IN ('draft', 'in_review', 'approved', 'published')),
  CONSTRAINT valid_risk CHECK (risk_score IN ('low', 'medium', 'high'))
);

ALTER TABLE content_drafts ENABLE ROW LEVEL SECURITY;
CREATE INDEX idx_content_drafts_venture ON content_drafts(venture_id);
CREATE INDEX idx_content_drafts_status ON content_drafts(status);
CREATE INDEX idx_content_drafts_type ON content_drafts(content_type);
CREATE INDEX idx_content_drafts_created ON content_drafts(created_at DESC);

CREATE TABLE IF NOT EXISTS brand_voices (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  venture_id VARCHAR(50) NOT NULL UNIQUE,
  tone VARCHAR(100),
  keywords TEXT[],
  voice_guide TEXT,
  primary_cta VARCHAR(100),
  created_at TIMESTAMP DEFAULT now(),
  updated_at TIMESTAMP DEFAULT now()
);

CREATE TABLE IF NOT EXISTS compliance_log (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  content_draft_id UUID REFERENCES content_drafts(id),
  checked_by UUID,
  checklist_items TEXT[],
  status VARCHAR(20),
  notes TEXT,
  checked_at TIMESTAMP DEFAULT now()
);

CREATE TABLE IF NOT EXISTS content_metrics (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  content_draft_id UUID REFERENCES content_drafts(id),
  platform VARCHAR(50),
  impressions INTEGER DEFAULT 0,
  clicks INTEGER DEFAULT 0,
  conversions INTEGER DEFAULT 0,
  revenue_attributed DECIMAL(10,2) DEFAULT 0,
  engagement_rate DECIMAL(5,2) DEFAULT 0,
  tracked_at TIMESTAMP DEFAULT now()
);

GRANT SELECT, INSERT, UPDATE ON content_drafts TO anon;
GRANT SELECT, INSERT, UPDATE ON brand_voices TO anon;
GRANT SELECT, INSERT ON compliance_log TO anon;
GRANT SELECT ON content_metrics TO anon;
