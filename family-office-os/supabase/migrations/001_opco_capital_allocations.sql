-- Migration: Create opco_capital_allocations table
-- Purpose: Track approved capital allocations to each OPCO
-- Date: 2026-07-28

BEGIN;

-- Create opco_capital_allocations table
CREATE TABLE IF NOT EXISTS public.opco_capital_allocations (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  opco_name TEXT NOT NULL,
  allocation_date DATE NOT NULL,
  approved_amount DECIMAL(15,2) NOT NULL,
  allocated_amount DECIMAL(15,2),
  status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'approved', 'deployed', 'returned')),
  approved_by TEXT,
  approval_date TIMESTAMP,
  created_at TIMESTAMP NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- Create indexes for common queries
CREATE INDEX idx_opco_capital_allocations_opco_name ON public.opco_capital_allocations(opco_name);
CREATE INDEX idx_opco_capital_allocations_allocation_date ON public.opco_capital_allocations(allocation_date);
CREATE INDEX idx_opco_capital_allocations_status ON public.opco_capital_allocations(status);
CREATE INDEX idx_opco_capital_allocations_approved_by ON public.opco_capital_allocations(approved_by);

-- Create audit trigger to update updated_at
CREATE OR REPLACE FUNCTION public.update_opco_capital_allocations_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_opco_capital_allocations_updated_at
  BEFORE UPDATE ON public.opco_capital_allocations
  FOR EACH ROW
  EXECUTE FUNCTION public.update_opco_capital_allocations_updated_at();

-- Enable RLS (Row Level Security)
ALTER TABLE public.opco_capital_allocations ENABLE ROW LEVEL SECURITY;

-- Create RLS policies
-- Allow authenticated users to read
CREATE POLICY "Allow authenticated users to read opco_capital_allocations"
  ON public.opco_capital_allocations
  FOR SELECT
  USING (auth.role() = 'authenticated');

-- Allow authenticated users with 'admin' or 'analyst' role to insert
CREATE POLICY "Allow finance users to insert opco_capital_allocations"
  ON public.opco_capital_allocations
  FOR INSERT
  WITH CHECK (
    auth.role() = 'authenticated'
    AND EXISTS (
      SELECT 1 FROM public.user_roles
      WHERE user_id = auth.uid()
      AND role IN ('admin', 'analyst')
    )
  );

-- Allow finance users to update
CREATE POLICY "Allow finance users to update opco_capital_allocations"
  ON public.opco_capital_allocations
  FOR UPDATE
  USING (
    auth.role() = 'authenticated'
    AND EXISTS (
      SELECT 1 FROM public.user_roles
      WHERE user_id = auth.uid()
      AND role IN ('admin', 'analyst')
    )
  );

-- Create table comment
COMMENT ON TABLE public.opco_capital_allocations IS 'Tracks approved capital allocations to OPCOs from the holding company pool. Weekly rebalances update this table based on deployment velocity and ROI performance.';

COMMIT;
