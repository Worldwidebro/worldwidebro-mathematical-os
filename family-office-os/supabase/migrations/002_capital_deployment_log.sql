-- Migration: Create capital_deployment_log table
-- Purpose: Immutable audit log of all capital deployments to ventures
-- Date: 2026-07-28

BEGIN;

-- Create capital_deployment_log table
CREATE TABLE IF NOT EXISTS public.capital_deployment_log (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  opco_name TEXT NOT NULL,
  venture_id TEXT NOT NULL,
  amount_deployed DECIMAL(15,2) NOT NULL,
  deployment_date DATE NOT NULL,
  predicted_roi_pct DECIMAL(5,2),
  actual_roi_pct DECIMAL(5,2),
  formula_used TEXT,
  created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- Create indexes for common queries
CREATE INDEX idx_capital_deployment_log_opco_name ON public.capital_deployment_log(opco_name);
CREATE INDEX idx_capital_deployment_log_venture_id ON public.capital_deployment_log(venture_id);
CREATE INDEX idx_capital_deployment_log_deployment_date ON public.capital_deployment_log(deployment_date);
CREATE INDEX idx_capital_deployment_log_created_at ON public.capital_deployment_log(created_at);

-- Create composite index for OPCO + deployment date (monthly reports)
CREATE INDEX idx_capital_deployment_log_opco_date ON public.capital_deployment_log(opco_name, deployment_date);

-- Create view for ROI reconciliation (predicted vs actual)
CREATE OR REPLACE VIEW public.capital_deployment_roi_reconciliation AS
SELECT
  opco_name,
  venture_id,
  amount_deployed,
  deployment_date,
  predicted_roi_pct,
  actual_roi_pct,
  CASE
    WHEN actual_roi_pct IS NOT NULL THEN (actual_roi_pct - predicted_roi_pct)
    ELSE NULL
  END AS roi_variance_pct,
  CASE
    WHEN actual_roi_pct IS NOT NULL AND predicted_roi_pct != 0
    THEN ((actual_roi_pct - predicted_roi_pct) / predicted_roi_pct * 100)::DECIMAL(5,2)
    ELSE NULL
  END AS roi_variance_percentage,
  formula_used,
  created_at
FROM public.capital_deployment_log
ORDER BY deployment_date DESC;

-- Create view for OPCO monthly deployment summary
CREATE OR REPLACE VIEW public.opco_monthly_deployment_summary AS
SELECT
  opco_name,
  DATE_TRUNC('month', deployment_date)::DATE AS month,
  COUNT(*) AS deployment_count,
  SUM(amount_deployed) AS total_deployed,
  AVG(predicted_roi_pct) AS avg_predicted_roi,
  CASE
    WHEN COUNT(*) FILTER (WHERE actual_roi_pct IS NOT NULL) > 0
    THEN AVG(actual_roi_pct) FILTER (WHERE actual_roi_pct IS NOT NULL)
    ELSE NULL
  END AS avg_actual_roi,
  MAX(deployment_date) AS last_deployment_date
FROM public.capital_deployment_log
GROUP BY opco_name, DATE_TRUNC('month', deployment_date)::DATE
ORDER BY month DESC, opco_name;

-- Create view for 12-month rolling ROI by OPCO
CREATE OR REPLACE VIEW public.opco_12mo_rolling_roi AS
SELECT
  opco_name,
  COUNT(*) AS deployment_count_12mo,
  SUM(amount_deployed) AS total_deployed_12mo,
  AVG(predicted_roi_pct) AS avg_predicted_roi_12mo,
  CASE
    WHEN COUNT(*) FILTER (WHERE actual_roi_pct IS NOT NULL) > 0
    THEN AVG(actual_roi_pct) FILTER (WHERE actual_roi_pct IS NOT NULL)
    ELSE NULL
  END AS avg_actual_roi_12mo,
  MIN(deployment_date) AS earliest_deployment,
  MAX(deployment_date) AS latest_deployment
FROM public.capital_deployment_log
WHERE deployment_date >= (CURRENT_DATE - INTERVAL '1 year')
GROUP BY opco_name
ORDER BY avg_actual_roi_12mo DESC NULLS LAST;

-- Enable RLS (Row Level Security)
ALTER TABLE public.capital_deployment_log ENABLE ROW LEVEL SECURITY;

-- Create RLS policies
-- Allow authenticated users to read (audit log is read-only)
CREATE POLICY "Allow authenticated users to read capital_deployment_log"
  ON public.capital_deployment_log
  FOR SELECT
  USING (auth.role() = 'authenticated');

-- Allow authenticated users with 'admin' or 'analyst' role to insert
-- (only inserts allowed, no updates/deletes for immutable audit log)
CREATE POLICY "Allow finance users to insert capital_deployment_log"
  ON public.capital_deployment_log
  FOR INSERT
  WITH CHECK (
    auth.role() = 'authenticated'
    AND EXISTS (
      SELECT 1 FROM public.user_roles
      WHERE user_id = auth.uid()
      AND role IN ('admin', 'analyst')
    )
  );

-- Allow agents to insert deployment records
CREATE POLICY "Allow agents to insert capital_deployment_log"
  ON public.capital_deployment_log
  FOR INSERT
  WITH CHECK (
    auth.role() = 'authenticated'
    AND EXISTS (
      SELECT 1 FROM public.agent_credentials
      WHERE agent_id = auth.uid()
      AND status = 'active'
    )
  );

-- Create table comments
COMMENT ON TABLE public.capital_deployment_log IS 'Immutable audit log of all capital deployments to ventures. Records deployment date, amount, predicted ROI, and actual ROI (once available). This table is append-only (no updates/deletes allowed).';
COMMENT ON VIEW public.capital_deployment_roi_reconciliation IS 'ROI reconciliation view showing predicted vs actual outcomes across all deployments.';
COMMENT ON VIEW public.opco_monthly_deployment_summary IS 'Monthly summary of deployment activity by OPCO, including count, total amount, and ROI metrics.';
COMMENT ON VIEW public.opco_12mo_rolling_roi IS 'Rolling 12-month ROI performance by OPCO, used for tier reclassification decisions.';

COMMIT;
