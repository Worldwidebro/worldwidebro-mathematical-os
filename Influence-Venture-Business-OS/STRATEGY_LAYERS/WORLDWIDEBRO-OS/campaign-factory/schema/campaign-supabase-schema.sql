-- Campaign Factory Schema Addition
-- Integrates with existing Supabase ventures database

-- ============================================================================
-- TABLE: CAMPAIGNS (Campaign instances)
-- ============================================================================

CREATE TABLE IF NOT EXISTS campaigns (
  campaign_id VARCHAR(100) PRIMARY KEY,
  venture_id VARCHAR(50) NOT NULL REFERENCES ventures(venture_id),
  template_id VARCHAR(50) NOT NULL,

  -- Campaign metadata
  name VARCHAR(255) NOT NULL,
  description TEXT,
  status VARCHAR(50) DEFAULT 'planning', -- planning|active|paused|completed|archived

  -- Timeline
  start_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  end_date TIMESTAMP,
  current_stage INT DEFAULT 1,

  -- Budget
  total_budget FLOAT DEFAULT 0,
  spent_budget FLOAT DEFAULT 0,

  -- Results
  total_reach INT DEFAULT 0,
  total_leads INT DEFAULT 0,
  total_conversions INT DEFAULT 0,
  total_revenue FLOAT DEFAULT 0,
  roas FLOAT,

  -- Metadata
  created_by VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  orchestrated_by_agent BOOLEAN DEFAULT FALSE,

  INDEX idx_venture_id (venture_id),
  INDEX idx_status (status),
  INDEX idx_current_stage (current_stage)
);

-- ============================================================================
-- TABLE: CAMPAIGN_STAGES (Progress tracking)
-- ============================================================================

CREATE TABLE IF NOT EXISTS campaign_stages (
  stage_id VARCHAR(100) PRIMARY KEY,
  campaign_id VARCHAR(100) NOT NULL REFERENCES campaigns(campaign_id),
  stage_number INT NOT NULL,
  stage_name VARCHAR(100) NOT NULL,

  -- Status
  status VARCHAR(50) DEFAULT 'pending', -- pending|in_progress|completed|blocked

  -- Execution
  started_at TIMESTAMP,
  completed_at TIMESTAMP,
  duration_hours INT,

  -- Deliverables
  deliverables_due INT DEFAULT 0,
  deliverables_completed INT DEFAULT 0,

  -- Agent orchestration
  orchestrated_by VARCHAR(100),
  orchestration_notes TEXT,

  -- Results
  quality_score INT,
  blockers TEXT,

  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  INDEX idx_campaign_id (campaign_id),
  INDEX idx_stage_number (stage_number),
  INDEX idx_status (status)
);

-- ============================================================================
-- TABLE: CAMPAIGN_DELIVERABLES (Asset tracking)
-- ============================================================================

CREATE TABLE IF NOT EXISTS campaign_deliverables (
  deliverable_id VARCHAR(100) PRIMARY KEY,
  stage_id VARCHAR(100) NOT NULL REFERENCES campaign_stages(stage_id),
  campaign_id VARCHAR(100) NOT NULL REFERENCES campaigns(campaign_id),

  -- Deliverable info
  name VARCHAR(255) NOT NULL,
  type VARCHAR(100), -- document|image|video|code|data|other
  description TEXT,

  -- Status
  status VARCHAR(50) DEFAULT 'pending', -- pending|in_progress|completed|approved|rejected

  -- Storage
  file_path VARCHAR(500),
  file_url VARCHAR(500),
  file_size_bytes INT,

  -- Quality
  created_by VARCHAR(100),
  reviewed_by VARCHAR(100),
  quality_score INT,
  review_notes TEXT,

  -- Metadata
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  approved_at TIMESTAMP,

  INDEX idx_stage_id (stage_id),
  INDEX idx_campaign_id (campaign_id),
  INDEX idx_status (status)
);

-- ============================================================================
-- TABLE: CAMPAIGN_CHANNELS (Channel assignments)
-- ============================================================================

CREATE TABLE IF NOT EXISTS campaign_channels (
  channel_assignment_id VARCHAR(100) PRIMARY KEY,
  campaign_id VARCHAR(100) NOT NULL REFERENCES campaigns(campaign_id),
  channel_id VARCHAR(50) NOT NULL, -- twitter|email|youtube|instagram|linkedin

  -- Configuration
  enabled BOOLEAN DEFAULT TRUE,
  posting_frequency VARCHAR(100),
  monthly_volume INT,

  -- Tracking
  content_posted INT DEFAULT 0,
  reach INT DEFAULT 0,
  engagement INT DEFAULT 0,
  conversions INT DEFAULT 0,

  -- Scheduling
  scheduled_by VARCHAR(100),
  scheduler_config TEXT, -- JSON cron config

  -- Results
  channel_roas FLOAT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  INDEX idx_campaign_id (campaign_id),
  INDEX idx_channel_id (channel_id),
  INDEX idx_enabled (enabled)
);

-- ============================================================================
-- TABLE: CAMPAIGN_CONTENT (Content pieces)
-- ============================================================================

CREATE TABLE IF NOT EXISTS campaign_content (
  content_id VARCHAR(100) PRIMARY KEY,
  campaign_id VARCHAR(100) NOT NULL REFERENCES campaigns(campaign_id),
  channel_id VARCHAR(50) NOT NULL,

  -- Content
  title VARCHAR(255),
  content TEXT,
  content_type VARCHAR(100), -- post|email|video|image|article

  -- Status
  status VARCHAR(50) DEFAULT 'draft', -- draft|approved|scheduled|published|archived

  -- Scheduling
  published_at TIMESTAMP,
  scheduled_for TIMESTAMP,

  -- Performance
  impressions INT DEFAULT 0,
  clicks INT DEFAULT 0,
  conversions INT DEFAULT 0,
  engagement_rate FLOAT,

  -- Metadata
  created_by VARCHAR(100),
  approved_by VARCHAR(100),
  ai_generated BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

  INDEX idx_campaign_id (campaign_id),
  INDEX idx_channel_id (channel_id),
  INDEX idx_status (status),
  INDEX idx_published_at (published_at)
);

-- ============================================================================
-- TABLE: CAMPAIGN_METRICS (Real-time KPI tracking)
-- ============================================================================

CREATE TABLE IF NOT EXISTS campaign_metrics (
  metric_id VARCHAR(100) PRIMARY KEY,
  campaign_id VARCHAR(100) NOT NULL REFERENCES campaigns(campaign_id),

  -- Metric definition
  metric_name VARCHAR(100) NOT NULL, -- impressions|reach|clicks|conversions|revenue
  metric_value FLOAT,
  metric_unit VARCHAR(50), -- count|dollars|percentage|hours

  -- Tracking
  measured_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  measured_from VARCHAR(50), -- organic|paid|combined
  channel_id VARCHAR(50),

  -- Comparison
  target_value FLOAT,
  performance_vs_target FLOAT, -- percentage vs target

  INDEX idx_campaign_id (campaign_id),
  INDEX idx_metric_name (metric_name),
  INDEX idx_measured_at (measured_at)
);

-- ============================================================================
-- TABLE: CAMPAIGN_AGENT_LOGS (Agent orchestration audit)
-- ============================================================================

CREATE TABLE IF NOT EXISTS campaign_agent_logs (
  log_id VARCHAR(100) PRIMARY KEY,
  campaign_id VARCHAR(100) NOT NULL REFERENCES campaigns(campaign_id),
  stage_id VARCHAR(100) REFERENCES campaign_stages(stage_id),

  -- Agent info
  agent_name VARCHAR(100),
  action VARCHAR(255),

  -- Execution
  started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  completed_at TIMESTAMP,
  duration_ms INT,

  -- Results
  status VARCHAR(50), -- success|partial|failed|blocked
  output_summary TEXT,
  error_message TEXT,

  -- Audit
  input_config TEXT, -- JSON of inputs
  quality_assessment TEXT,

  INDEX idx_campaign_id (campaign_id),
  INDEX idx_agent_name (agent_name),
  INDEX idx_status (status)
);
