-- Add 14-Layer Influence Model Fields to Ventures Table
-- Enables systematic messaging, script generation, influence tracking

ALTER TABLE ventures ADD COLUMN IF NOT EXISTS customer_segment VARCHAR(255);
ALTER TABLE ventures ADD COLUMN IF NOT EXISTS customer_pain_point TEXT;
ALTER TABLE ventures ADD COLUMN IF NOT EXISTS customer_desired_outcome TEXT;
ALTER TABLE ventures ADD COLUMN IF NOT EXISTS value_driver VARCHAR(100);
ALTER TABLE ventures ADD COLUMN IF NOT EXISTS offer_positioning TEXT;
ALTER TABLE ventures ADD COLUMN IF NOT EXISTS vision_statement TEXT;
ALTER TABLE ventures ADD COLUMN IF NOT EXISTS trust_signals TEXT;
ALTER TABLE ventures ADD COLUMN IF NOT EXISTS case_studies TEXT;
ALTER TABLE ventures ADD COLUMN IF NOT EXISTS proof_metrics TEXT;
ALTER TABLE ventures ADD COLUMN IF NOT EXISTS authority_credentials TEXT;
ALTER TABLE ventures ADD COLUMN IF NOT EXISTS leadership_direction TEXT;
ALTER TABLE ventures ADD COLUMN IF NOT EXISTS referral_percentage INT DEFAULT 0;
ALTER TABLE ventures ADD COLUMN IF NOT EXISTS community_engagement TEXT;
ALTER TABLE ventures ADD COLUMN IF NOT EXISTS influence_layers_complete INT DEFAULT 0;
ALTER TABLE ventures ADD COLUMN IF NOT EXISTS influence_last_updated TIMESTAMP;
ALTER TABLE ventures ADD COLUMN IF NOT EXISTS messaging_templates_generated BOOLEAN DEFAULT FALSE;
ALTER TABLE ventures ADD COLUMN IF NOT EXISTS script_count INT DEFAULT 0;

CREATE INDEX IF NOT EXISTS idx_ventures_customer_segment ON ventures(customer_segment);
CREATE INDEX IF NOT EXISTS idx_ventures_value_driver ON ventures(value_driver);
CREATE INDEX IF NOT EXISTS idx_ventures_influence_complete ON ventures(influence_layers_complete);

-- View for influence-ready ventures (can generate scripts)
CREATE OR REPLACE VIEW influence_ready_ventures AS
SELECT
  venture_id, name, sector, stage,
  customer_segment, customer_pain_point, value_driver, offer_positioning,
  CASE
    WHEN customer_segment IS NOT NULL AND customer_pain_point IS NOT NULL
      AND value_driver IS NOT NULL AND offer_positioning IS NOT NULL
    THEN TRUE ELSE FALSE
  END as ready_for_scripts
FROM ventures WHERE status = 'active';

-- View for influence impact (results, reputation, community)
CREATE OR REPLACE VIEW influence_impact_ventures AS
SELECT
  venture_id, name,
  COALESCE(proof_metrics, '{}') as proof_metrics,
  referral_percentage,
  community_engagement,
  (CASE WHEN proof_metrics IS NOT NULL THEN 1 ELSE 0 END +
   CASE WHEN referral_percentage > 0 THEN 1 ELSE 0 END +
   CASE WHEN community_engagement IS NOT NULL THEN 1 ELSE 0 END) as reputation_score
FROM ventures WHERE status = 'active'
ORDER BY reputation_score DESC;
