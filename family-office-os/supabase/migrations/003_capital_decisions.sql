-- Migration: Create capital_decisions table
-- Purpose: Decision log with complete reasoning traces for capital allocation
-- Date: 2026-07-28

BEGIN;

-- Create capital_decisions table
CREATE TABLE IF NOT EXISTS public.capital_decisions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  decision_type TEXT NOT NULL CHECK (decision_type IN ('allocation', 'deployment', 'rebalance', 'emergency', 'tier_change')),
  opco_name TEXT NOT NULL,
  amount DECIMAL(15,2) NOT NULL,
  decision_maker TEXT NOT NULL,
  decision_date TIMESTAMP NOT NULL DEFAULT NOW(),
  reasoning TEXT,
  approval_status TEXT NOT NULL DEFAULT 'pending' CHECK (approval_status IN ('auto', 'pending', 'approved', 'rejected')),
  approver_id TEXT,
  approval_timestamp TIMESTAMP,
  created_at TIMESTAMP NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- Create indexes for common queries
CREATE INDEX idx_capital_decisions_opco_name ON public.capital_decisions(opco_name);
CREATE INDEX idx_capital_decisions_decision_type ON public.capital_decisions(decision_type);
CREATE INDEX idx_capital_decisions_decision_maker ON public.capital_decisions(decision_maker);
CREATE INDEX idx_capital_decisions_decision_date ON public.capital_decisions(decision_date);
CREATE INDEX idx_capital_decisions_approval_status ON public.capital_decisions(approval_status);
CREATE INDEX idx_capital_decisions_approver_id ON public.capital_decisions(approver_id);

-- Create composite index for audit queries
CREATE INDEX idx_capital_decisions_opco_date_type ON public.capital_decisions(opco_name, decision_date, decision_type);

-- Create audit trigger to update updated_at
CREATE OR REPLACE FUNCTION public.update_capital_decisions_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_capital_decisions_updated_at
  BEFORE UPDATE ON public.capital_decisions
  FOR EACH ROW
  EXECUTE FUNCTION public.update_capital_decisions_updated_at();

-- Create view for pending approvals (SLA tracking)
CREATE OR REPLACE VIEW public.capital_decisions_pending_approvals AS
SELECT
  id,
  decision_type,
  opco_name,
  amount,
  decision_maker,
  decision_date,
  CASE
    WHEN amount < 50000 THEN '< 50K (auto-approved)'
    WHEN amount < 100000 THEN '50K-100K (2h SLA)'
    WHEN amount < 500000 THEN '100K-500K (2h SLA)'
    WHEN amount < 1000000 THEN '500K-1M (6h SLA)'
    ELSE '> 1M (24h SLA)'
  END AS approval_tier,
  CASE
    WHEN amount < 50000 THEN '00:00:00'::INTERVAL
    WHEN amount < 100000 THEN '02:00:00'::INTERVAL
    WHEN amount < 500000 THEN '02:00:00'::INTERVAL
    WHEN amount < 1000000 THEN '06:00:00'::INTERVAL
    ELSE '24:00:00'::INTERVAL
  END AS sla_window,
  NOW() - decision_date AS time_pending,
  CASE
    WHEN amount >= 50000 AND amount < 100000 AND (NOW() - decision_date) > '02:00:00'::INTERVAL THEN 'BREACH'
    WHEN amount >= 100000 AND amount < 500000 AND (NOW() - decision_date) > '02:00:00'::INTERVAL THEN 'BREACH'
    WHEN amount >= 500000 AND amount < 1000000 AND (NOW() - decision_date) > '06:00:00'::INTERVAL THEN 'BREACH'
    WHEN amount >= 1000000 AND (NOW() - decision_date) > '24:00:00'::INTERVAL THEN 'BREACH'
    ELSE 'OK'
  END AS sla_status,
  approval_status,
  reasoning
FROM public.capital_decisions
WHERE approval_status IN ('pending', 'auto')
ORDER BY decision_date ASC;

-- Create view for decision audit trail
CREATE OR REPLACE VIEW public.capital_decisions_audit_trail AS
SELECT
  id,
  decision_type,
  opco_name,
  amount,
  decision_maker,
  decision_date,
  approval_status,
  approver_id,
  approval_timestamp,
  CASE
    WHEN approval_status = 'auto' THEN 0
    WHEN approval_status IN ('pending', 'approved', 'rejected') AND approval_timestamp IS NOT NULL
    THEN EXTRACT(EPOCH FROM (approval_timestamp - decision_date)) / 3600
    ELSE NULL
  END AS approval_hours,
  created_at,
  updated_at
FROM public.capital_decisions
ORDER BY decision_date DESC;

-- Create view for SLA metrics (aggregate)
CREATE OR REPLACE VIEW public.capital_decisions_sla_metrics AS
SELECT
  DATE_TRUNC('day', decision_date)::DATE AS date,
  COUNT(*) AS total_decisions,
  COUNT(*) FILTER (WHERE approval_status = 'auto') AS auto_approved,
  COUNT(*) FILTER (WHERE approval_status = 'approved') AS approved,
  COUNT(*) FILTER (WHERE approval_status = 'rejected') AS rejected,
  SUM(amount) FILTER (WHERE approval_status IN ('auto', 'approved')) AS total_approved_amount,
  COUNT(*) FILTER (WHERE approval_status = 'pending') AS still_pending,
  AVG(EXTRACT(EPOCH FROM (approval_timestamp - decision_date)) / 3600)
    FILTER (WHERE approval_status IN ('approved', 'rejected') AND approval_timestamp IS NOT NULL) AS avg_approval_hours,
  MAX(EXTRACT(EPOCH FROM (approval_timestamp - decision_date)) / 3600)
    FILTER (WHERE approval_status IN ('approved', 'rejected') AND approval_timestamp IS NOT NULL) AS max_approval_hours
FROM public.capital_decisions
GROUP BY DATE_TRUNC('day', decision_date)::DATE
ORDER BY date DESC;

-- Enable RLS (Row Level Security)
ALTER TABLE public.capital_decisions ENABLE ROW LEVEL SECURITY;

-- Create RLS policies
-- Allow authenticated users to read decisions (audit trail)
CREATE POLICY "Allow authenticated users to read capital_decisions"
  ON public.capital_decisions
  FOR SELECT
  USING (auth.role() = 'authenticated');

-- Allow agents and finance users to insert decisions
CREATE POLICY "Allow agents and finance to insert capital_decisions"
  ON public.capital_decisions
  FOR INSERT
  WITH CHECK (
    auth.role() = 'authenticated'
    AND (
      EXISTS (
        SELECT 1 FROM public.agent_credentials
        WHERE agent_id = auth.uid()
        AND status = 'active'
      )
      OR EXISTS (
        SELECT 1 FROM public.user_roles
        WHERE user_id = auth.uid()
        AND role IN ('admin', 'analyst')
      )
    )
  );

-- Allow finance users to update approval status
CREATE POLICY "Allow finance users to update capital_decisions"
  ON public.capital_decisions
  FOR UPDATE
  USING (
    auth.role() = 'authenticated'
    AND EXISTS (
      SELECT 1 FROM public.user_roles
      WHERE user_id = auth.uid()
      AND role IN ('admin', 'analyst')
    )
  )
  WITH CHECK (
    auth.role() = 'authenticated'
    AND EXISTS (
      SELECT 1 FROM public.user_roles
      WHERE user_id = auth.uid()
      AND role IN ('admin', 'analyst')
    )
  );

-- Create table comments
COMMENT ON TABLE public.capital_decisions IS 'Decision log tracking all capital allocation, deployment, rebalance, emergency, and tier-change decisions. Each record includes the reasoning trace (reasoning field in JSON) for full transparency and auditability.';
COMMENT ON VIEW public.capital_decisions_pending_approvals IS 'Pending approval queue with SLA tracking. Shows decisions that need human approval and whether SLA is being met.';
COMMENT ON VIEW public.capital_decisions_audit_trail IS 'Complete audit trail of all decisions with approval times and status history.';
COMMENT ON VIEW public.capital_decisions_sla_metrics IS 'Daily aggregate SLA metrics: approval times, approval rates, pending count.';

COMMIT;
