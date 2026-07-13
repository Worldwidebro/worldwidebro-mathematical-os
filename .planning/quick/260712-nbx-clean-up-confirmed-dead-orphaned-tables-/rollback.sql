-- rollback.sql
-- Reversible DDL capture for quick task 260712-nbx (clean-up-confirmed-dead-orphaned-tables)
-- Project: cyhzilqldouzgynacqpe (CivilizationOS)
-- Captured: 2026-07-13T (immediately before DROP, in the same audit session)
--
-- Purpose: recreate the 20 confirmed-dead, zero-row, zero-code-reference orphaned
-- tables that were dropped from the public schema. All 20 tables were re-verified
-- at n_live_tup = 0 immediately before capture and immediately before the DROP.
--
-- The 20 tables (3 clusters):
--   joos_* (8): joos_ai_decisions, joos_clients, joos_cost_tracking, joos_job_assignments,
--               joos_job_events, joos_job_stages, joos_jobs, joos_vendors
--   folder_* + genius_agents (5): folder_categories, folder_metrics, folder_monetization,
--               folder_value_propositions, genius_agents
--   dead per-venture trackers (7): con_001_leads, con_001_outreach, con_001_qualified_leads,
--               fin_001_leads, fin_001_outreach, mc_001_potential_sponsors, mc_001_sponsorships
--
-- To roll back: re-run this entire file against project cyhzilqldouzgynacqpe via
-- `supabase db query --linked -f rollback.sql` (or the Supabase MCP execute_sql/apply_migration
-- tool). All CREATE TABLE statements use IF NOT EXISTS, and are followed by their
-- constraints (PK/UNIQUE/FK) in a second pass so forward-referencing FKs resolve safely.
-- Recreated tables will be EMPTY (no data existed to restore -- all 20 were 0 rows).
-- RLS policies, if any existed on these tables, are NOT captured here (none were found
-- attached to these 20 tables at capture time) and would need to be reapplied separately
-- if discovered missing after rollback.

BEGIN;

-- ============================================================
-- Cluster 1: joos_* (8 tables)
-- ============================================================

CREATE TABLE IF NOT EXISTS public.joos_clients (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    org_id uuid NOT NULL,
    external_ref text,
    display_name text NOT NULL,
    metadata jsonb DEFAULT '{}'::jsonb,
    created_at timestamp with time zone NOT NULL DEFAULT now(),
    updated_at timestamp with time zone NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS public.joos_vendors (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    org_id uuid NOT NULL,
    affiliate_external_id text,
    trade_type text,
    display_name text NOT NULL,
    rating numeric(4,2),
    cost_rate numeric(14,2),
    reliability_score numeric(5,4),
    availability jsonb DEFAULT '{}'::jsonb,
    metadata jsonb DEFAULT '{}'::jsonb,
    created_at timestamp with time zone NOT NULL DEFAULT now(),
    updated_at timestamp with time zone NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS public.joos_jobs (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    org_id uuid NOT NULL,
    client_id uuid,
    code text,
    title text NOT NULL,
    status text NOT NULL DEFAULT 'draft'::text,
    budget_amount numeric(14,2),
    budget_currency text NOT NULL DEFAULT 'USD'::text,
    start_date date,
    end_date date,
    current_stage text,
    risk_state text,
    health_score smallint,
    metadata jsonb DEFAULT '{}'::jsonb,
    created_at timestamp with time zone NOT NULL DEFAULT now(),
    updated_at timestamp with time zone NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS public.joos_ai_decisions (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    job_id uuid NOT NULL,
    decision_type text NOT NULL,
    reasoning text,
    action_taken text,
    payload jsonb DEFAULT '{}'::jsonb,
    confidence numeric(5,4),
    status text NOT NULL DEFAULT 'recorded'::text,
    applied_at timestamp with time zone,
    superseded_by uuid,
    created_at timestamp with time zone NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS public.joos_cost_tracking (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    job_id uuid NOT NULL,
    period_start date,
    period_end date,
    estimated_cost numeric(14,2),
    actual_cost numeric(14,2),
    variance numeric(14,2) DEFAULT (COALESCE(actual_cost, (0)::numeric) - COALESCE(estimated_cost, (0)::numeric)),
    currency text NOT NULL DEFAULT 'USD'::text,
    metadata jsonb DEFAULT '{}'::jsonb,
    created_at timestamp with time zone NOT NULL DEFAULT now(),
    updated_at timestamp with time zone NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS public.joos_job_assignments (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    job_id uuid NOT NULL,
    vendor_id uuid NOT NULL,
    role text NOT NULL,
    assigned_at date NOT NULL DEFAULT CURRENT_DATE,
    performance_score numeric(5,4),
    metadata jsonb DEFAULT '{}'::jsonb,
    created_at timestamp with time zone NOT NULL DEFAULT now(),
    updated_at timestamp with time zone NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS public.joos_job_events (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    job_id uuid NOT NULL,
    event_type text NOT NULL,
    source text NOT NULL DEFAULT 'system'::text,
    occurred_at timestamp with time zone NOT NULL DEFAULT now(),
    correlation_id text,
    idempotency_key text,
    metadata jsonb DEFAULT '{}'::jsonb
);

CREATE TABLE IF NOT EXISTS public.joos_job_stages (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    job_id uuid NOT NULL,
    stage_name text NOT NULL,
    status text NOT NULL DEFAULT 'pending'::text,
    sort_order integer NOT NULL DEFAULT 0,
    entered_at timestamp with time zone NOT NULL DEFAULT now(),
    exited_at timestamp with time zone,
    metadata jsonb DEFAULT '{}'::jsonb
);

-- ============================================================
-- Cluster 2: folder_* + genius_agents (5 tables)
-- ============================================================

CREATE TABLE IF NOT EXISTS public.folder_categories (
    category_id text NOT NULL,
    category_name text NOT NULL,
    folder_range text,
    description text,
    typical_revenue_model text,
    typical_monetization_potential text,
    analysis_priority integer DEFAULT 50
);

CREATE TABLE IF NOT EXISTS public.folder_metrics (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    folder_id text NOT NULL,
    folder_name text NOT NULL,
    category text,
    files_count integer DEFAULT 0,
    files_modified_last_24h integer DEFAULT 0,
    files_modified_last_7d integer DEFAULT 0,
    total_size_mb numeric DEFAULT 0,
    last_activity timestamp with time zone,
    value_score numeric DEFAULT 0,
    monetization_potential text DEFAULT 'low'::text,
    revenue_generated_usd numeric DEFAULT 0,
    cost_savings_usd numeric DEFAULT 0,
    efficiency_gain_percent numeric DEFAULT 0,
    access_count_24h integer DEFAULT 0,
    automation_runs integer DEFAULT 0,
    api_calls integer DEFAULT 0,
    llm_queries integer DEFAULT 0,
    workflow_executions integer DEFAULT 0,
    capabilities jsonb,
    dependencies jsonb,
    integrations jsonb,
    tools_used jsonb,
    documentation_coverage numeric DEFAULT 0,
    test_coverage numeric DEFAULT 0,
    code_quality_score numeric DEFAULT 0,
    "timestamp" timestamp with time zone DEFAULT now()
);

CREATE TABLE IF NOT EXISTS public.folder_monetization (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    folder_id text NOT NULL,
    revenue_type text NOT NULL,
    revenue_amount_usd numeric NOT NULL,
    revenue_date date DEFAULT CURRENT_DATE,
    revenue_source text,
    payment_status text DEFAULT 'pending'::text,
    customer_id text,
    customer_name text,
    customer_count integer DEFAULT 1,
    active_users integer,
    churn_count integer DEFAULT 0,
    product_sold text,
    product_type text,
    units_sold integer DEFAULT 1,
    unit_price_usd numeric,
    marketing_channel text,
    conversion_source text,
    is_recurring boolean DEFAULT false,
    recurring_frequency text,
    subscription_tier text,
    mrr_contribution numeric,
    notes text,
    "timestamp" timestamp with time zone DEFAULT now()
);

CREATE TABLE IF NOT EXISTS public.folder_value_propositions (
    folder_id text NOT NULL,
    folder_number integer,
    folder_name text NOT NULL,
    category text,
    primary_capability text NOT NULL,
    value_statement text NOT NULL,
    target_audience text,
    pain_point_solved text,
    revenue_model text,
    pricing_tier text,
    price_point_usd numeric,
    estimated_revenue_potential numeric,
    time_to_monetization text,
    productized_offerings jsonb,
    product_status text,
    minimum_viable_product text,
    market_size text,
    market_description text,
    competition_level text,
    competitors jsonb,
    unique_differentiator text,
    competitive_advantage text,
    enabling_folders text[],
    enabled_folders text[],
    required_integrations text[],
    priority_level text DEFAULT 'medium'::text,
    implementation_complexity text,
    required_resources jsonb,
    created_at timestamp with time zone DEFAULT now(),
    updated_at timestamp with time zone DEFAULT now(),
    last_reviewed timestamp with time zone,
    reviewed_by text
);

CREATE TABLE IF NOT EXISTS public.genius_agents (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    name text NOT NULL,
    slug text NOT NULL,
    domain_id uuid,
    folder text,
    description text,
    capabilities text[] DEFAULT '{}'::text[],
    dimension integer,
    status text DEFAULT 'active'::text,
    parent_genius_id uuid,
    metadata jsonb DEFAULT '{}'::jsonb,
    config jsonb DEFAULT '{}'::jsonb,
    created_at timestamp with time zone DEFAULT now(),
    updated_at timestamp with time zone DEFAULT now()
);

-- ============================================================
-- Cluster 3: dead per-venture trackers (7 tables)
-- ============================================================

CREATE TABLE IF NOT EXISTS public.con_001_leads (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    venture_id text NOT NULL DEFAULT 'CON-001'::text,
    generic_lead_id uuid,
    name text NOT NULL,
    title text,
    company_name text,
    company_size text,
    location text,
    linkedin_url text,
    email text,
    construction_focus text,
    company_revenue_estimate numeric(12,2),
    recent_projects jsonb,
    decision_maker_level text,
    fit_score integer,
    fit_reason text,
    status text DEFAULT 'new'::text,
    contacted boolean DEFAULT false,
    contacted_at timestamp with time zone,
    created_at timestamp with time zone DEFAULT now(),
    updated_at timestamp with time zone DEFAULT now()
);

CREATE TABLE IF NOT EXISTS public.con_001_outreach (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    lead_id uuid,
    email_sequence integer,
    subject_line text,
    body text,
    cta text,
    sent_at timestamp with time zone,
    opened_at timestamp with time zone,
    replied_at timestamp with time zone,
    replied_text text,
    open_rate_percent numeric(5,2),
    click_rate_percent numeric(5,2),
    status text,
    created_at timestamp with time zone DEFAULT now(),
    updated_at timestamp with time zone DEFAULT now()
);

CREATE TABLE IF NOT EXISTS public.con_001_qualified_leads (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    lead_id uuid,
    call_date timestamp with time zone,
    qualification_score integer,
    budget_capability text,
    timeline_urgency text,
    pain_level integer,
    decision_authority boolean,
    call_notes text,
    category text,
    next_action text,
    demo_scheduled boolean DEFAULT false,
    demo_date timestamp with time zone,
    created_at timestamp with time zone DEFAULT now(),
    updated_at timestamp with time zone DEFAULT now()
);

CREATE TABLE IF NOT EXISTS public.fin_001_leads (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    venture_id text NOT NULL DEFAULT 'FIN-001'::text,
    name text NOT NULL,
    title text,
    company_name text,
    company_size text,
    location text,
    linkedin_url text,
    email text,
    business_age_years integer,
    estimated_annual_revenue numeric(12,2),
    credit_repair_fit_score integer,
    financing_interest boolean,
    pain_signals jsonb,
    engagement_level text,
    status text DEFAULT 'new'::text,
    created_at timestamp with time zone DEFAULT now(),
    updated_at timestamp with time zone DEFAULT now()
);

CREATE TABLE IF NOT EXISTS public.fin_001_outreach (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    lead_id uuid,
    email_sequence integer,
    subject_line text,
    body text,
    sent_at timestamp with time zone,
    opened_at timestamp with time zone,
    replied_at timestamp with time zone,
    replied_text text,
    reply_sentiment text,
    consultation_booked boolean DEFAULT false,
    consultation_date timestamp with time zone,
    status text,
    created_at timestamp with time zone DEFAULT now()
);

CREATE TABLE IF NOT EXISTS public.mc_001_potential_sponsors (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    venture_id text NOT NULL DEFAULT 'MC-001'::text,
    brand_name text NOT NULL,
    contact_name text,
    contact_title text,
    contact_email text,
    company_website text,
    linkedin_url text,
    estimated_marketing_budget numeric(12,2),
    past_sponsorship_history jsonb,
    audience_fit_score integer,
    sponsorship_interest_level text,
    estimated_monthly_value numeric(12,2),
    status text DEFAULT 'new'::text,
    created_at timestamp with time zone DEFAULT now(),
    updated_at timestamp with time zone DEFAULT now()
);

CREATE TABLE IF NOT EXISTS public.mc_001_sponsorships (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    sponsor_id uuid,
    pitch_number integer,
    subject_line text,
    pitch_text text,
    sent_at timestamp with time zone,
    opened_at timestamp with time zone,
    replied_at timestamp with time zone,
    sponsorship_package text,
    monthly_rate numeric(12,2),
    contract_signed boolean DEFAULT false,
    contract_date timestamp with time zone,
    status text,
    created_at timestamp with time zone DEFAULT now(),
    updated_at timestamp with time zone DEFAULT now()
);

-- ============================================================
-- Constraints (added after all 20 CREATE TABLEs so forward FK
-- references resolve). Applied only if the constraint does not
-- already exist (guarded with DO blocks for idempotency).
-- ============================================================

DO $$
BEGIN
  -- joos_clients
  IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'joos_clients_pkey') THEN
    ALTER TABLE public.joos_clients ADD CONSTRAINT joos_clients_pkey PRIMARY KEY (id);
  END IF;

  -- joos_vendors
  IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'joos_vendors_pkey') THEN
    ALTER TABLE public.joos_vendors ADD CONSTRAINT joos_vendors_pkey PRIMARY KEY (id);
  END IF;

  -- joos_jobs
  IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'joos_jobs_pkey') THEN
    ALTER TABLE public.joos_jobs ADD CONSTRAINT joos_jobs_pkey PRIMARY KEY (id);
  END IF;
  IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'joos_jobs_client_id_fkey') THEN
    ALTER TABLE public.joos_jobs ADD CONSTRAINT joos_jobs_client_id_fkey FOREIGN KEY (client_id) REFERENCES public.joos_clients(id) ON DELETE SET NULL;
  END IF;

  -- joos_ai_decisions
  IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'joos_ai_decisions_pkey') THEN
    ALTER TABLE public.joos_ai_decisions ADD CONSTRAINT joos_ai_decisions_pkey PRIMARY KEY (id);
  END IF;
  IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'joos_ai_decisions_job_id_fkey') THEN
    ALTER TABLE public.joos_ai_decisions ADD CONSTRAINT joos_ai_decisions_job_id_fkey FOREIGN KEY (job_id) REFERENCES public.joos_jobs(id) ON DELETE CASCADE;
  END IF;
  IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'joos_ai_decisions_superseded_by_fkey') THEN
    ALTER TABLE public.joos_ai_decisions ADD CONSTRAINT joos_ai_decisions_superseded_by_fkey FOREIGN KEY (superseded_by) REFERENCES public.joos_ai_decisions(id) ON DELETE SET NULL;
  END IF;

  -- joos_cost_tracking
  IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'joos_cost_tracking_pkey') THEN
    ALTER TABLE public.joos_cost_tracking ADD CONSTRAINT joos_cost_tracking_pkey PRIMARY KEY (id);
  END IF;
  IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'joos_cost_tracking_job_id_fkey') THEN
    ALTER TABLE public.joos_cost_tracking ADD CONSTRAINT joos_cost_tracking_job_id_fkey FOREIGN KEY (job_id) REFERENCES public.joos_jobs(id) ON DELETE CASCADE;
  END IF;

  -- joos_job_assignments
  IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'joos_job_assignments_pkey') THEN
    ALTER TABLE public.joos_job_assignments ADD CONSTRAINT joos_job_assignments_pkey PRIMARY KEY (id);
  END IF;
  IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'joos_job_assignments_job_id_fkey') THEN
    ALTER TABLE public.joos_job_assignments ADD CONSTRAINT joos_job_assignments_job_id_fkey FOREIGN KEY (job_id) REFERENCES public.joos_jobs(id) ON DELETE CASCADE;
  END IF;
  IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'joos_job_assignments_vendor_id_fkey') THEN
    ALTER TABLE public.joos_job_assignments ADD CONSTRAINT joos_job_assignments_vendor_id_fkey FOREIGN KEY (vendor_id) REFERENCES public.joos_vendors(id) ON DELETE RESTRICT;
  END IF;

  -- joos_job_events
  IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'joos_job_events_pkey') THEN
    ALTER TABLE public.joos_job_events ADD CONSTRAINT joos_job_events_pkey PRIMARY KEY (id);
  END IF;
  IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'joos_job_events_job_id_fkey') THEN
    ALTER TABLE public.joos_job_events ADD CONSTRAINT joos_job_events_job_id_fkey FOREIGN KEY (job_id) REFERENCES public.joos_jobs(id) ON DELETE CASCADE;
  END IF;

  -- joos_job_stages
  IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'joos_job_stages_pkey') THEN
    ALTER TABLE public.joos_job_stages ADD CONSTRAINT joos_job_stages_pkey PRIMARY KEY (id);
  END IF;
  IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'joos_job_stages_job_id_fkey') THEN
    ALTER TABLE public.joos_job_stages ADD CONSTRAINT joos_job_stages_job_id_fkey FOREIGN KEY (job_id) REFERENCES public.joos_jobs(id) ON DELETE CASCADE;
  END IF;

  -- folder_categories
  IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'folder_categories_pkey') THEN
    ALTER TABLE public.folder_categories ADD CONSTRAINT folder_categories_pkey PRIMARY KEY (category_id);
  END IF;

  -- folder_metrics
  IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'folder_metrics_pkey') THEN
    ALTER TABLE public.folder_metrics ADD CONSTRAINT folder_metrics_pkey PRIMARY KEY (id);
  END IF;

  -- folder_monetization
  IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'folder_monetization_pkey') THEN
    ALTER TABLE public.folder_monetization ADD CONSTRAINT folder_monetization_pkey PRIMARY KEY (id);
  END IF;

  -- folder_value_propositions
  IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'folder_value_propositions_pkey') THEN
    ALTER TABLE public.folder_value_propositions ADD CONSTRAINT folder_value_propositions_pkey PRIMARY KEY (folder_id);
  END IF;

  -- genius_agents (domain_id / parent_genius_id FKs reference tables OUTSIDE the
  -- 20-table allowlist; both target tables, domains and genius_agents itself,
  -- are expected to still exist since they were never dropped)
  IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'genius_agents_pkey') THEN
    ALTER TABLE public.genius_agents ADD CONSTRAINT genius_agents_pkey PRIMARY KEY (id);
  END IF;
  IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'genius_agents_slug_key') THEN
    ALTER TABLE public.genius_agents ADD CONSTRAINT genius_agents_slug_key UNIQUE (slug);
  END IF;
  IF EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema = 'public' AND table_name = 'domains')
     AND NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'genius_agents_domain_id_fkey') THEN
    ALTER TABLE public.genius_agents ADD CONSTRAINT genius_agents_domain_id_fkey FOREIGN KEY (domain_id) REFERENCES public.domains(id);
  END IF;
  IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'genius_agents_parent_genius_id_fkey') THEN
    ALTER TABLE public.genius_agents ADD CONSTRAINT genius_agents_parent_genius_id_fkey FOREIGN KEY (parent_genius_id) REFERENCES public.genius_agents(id);
  END IF;

  -- con_001_leads (generic_lead_id FK references venture_leads, OUTSIDE the
  -- 20-table allowlist; venture_leads is expected to still exist)
  IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'con_001_leads_pkey') THEN
    ALTER TABLE public.con_001_leads ADD CONSTRAINT con_001_leads_pkey PRIMARY KEY (id);
  END IF;
  IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'con_001_leads_email_unique') THEN
    ALTER TABLE public.con_001_leads ADD CONSTRAINT con_001_leads_email_unique UNIQUE (email);
  END IF;
  IF EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema = 'public' AND table_name = 'venture_leads')
     AND NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'con_001_leads_generic_lead_id_fkey') THEN
    ALTER TABLE public.con_001_leads ADD CONSTRAINT con_001_leads_generic_lead_id_fkey FOREIGN KEY (generic_lead_id) REFERENCES public.venture_leads(id) ON DELETE SET NULL;
  END IF;

  -- con_001_outreach
  IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'con_001_outreach_pkey') THEN
    ALTER TABLE public.con_001_outreach ADD CONSTRAINT con_001_outreach_pkey PRIMARY KEY (id);
  END IF;
  IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'con_001_outreach_lead_id_fkey') THEN
    ALTER TABLE public.con_001_outreach ADD CONSTRAINT con_001_outreach_lead_id_fkey FOREIGN KEY (lead_id) REFERENCES public.con_001_leads(id) ON DELETE CASCADE;
  END IF;

  -- con_001_qualified_leads
  IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'con_001_qualified_leads_pkey') THEN
    ALTER TABLE public.con_001_qualified_leads ADD CONSTRAINT con_001_qualified_leads_pkey PRIMARY KEY (id);
  END IF;
  IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'con_001_qualified_leads_lead_id_fkey') THEN
    ALTER TABLE public.con_001_qualified_leads ADD CONSTRAINT con_001_qualified_leads_lead_id_fkey FOREIGN KEY (lead_id) REFERENCES public.con_001_leads(id) ON DELETE CASCADE;
  END IF;

  -- fin_001_leads
  IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'fin_001_leads_pkey') THEN
    ALTER TABLE public.fin_001_leads ADD CONSTRAINT fin_001_leads_pkey PRIMARY KEY (id);
  END IF;
  IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'fin_001_leads_email_unique') THEN
    ALTER TABLE public.fin_001_leads ADD CONSTRAINT fin_001_leads_email_unique UNIQUE (email);
  END IF;

  -- fin_001_outreach
  IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'fin_001_outreach_pkey') THEN
    ALTER TABLE public.fin_001_outreach ADD CONSTRAINT fin_001_outreach_pkey PRIMARY KEY (id);
  END IF;
  IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'fin_001_outreach_lead_id_fkey') THEN
    ALTER TABLE public.fin_001_outreach ADD CONSTRAINT fin_001_outreach_lead_id_fkey FOREIGN KEY (lead_id) REFERENCES public.fin_001_leads(id) ON DELETE CASCADE;
  END IF;

  -- mc_001_potential_sponsors
  IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'mc_001_potential_sponsors_pkey') THEN
    ALTER TABLE public.mc_001_potential_sponsors ADD CONSTRAINT mc_001_potential_sponsors_pkey PRIMARY KEY (id);
  END IF;
  IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'mc_001_sponsors_email_unique') THEN
    ALTER TABLE public.mc_001_potential_sponsors ADD CONSTRAINT mc_001_sponsors_email_unique UNIQUE (contact_email);
  END IF;

  -- mc_001_sponsorships
  IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'mc_001_sponsorships_pkey') THEN
    ALTER TABLE public.mc_001_sponsorships ADD CONSTRAINT mc_001_sponsorships_pkey PRIMARY KEY (id);
  END IF;
  IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'mc_001_sponsorships_sponsor_id_fkey') THEN
    ALTER TABLE public.mc_001_sponsorships ADD CONSTRAINT mc_001_sponsorships_sponsor_id_fkey FOREIGN KEY (sponsor_id) REFERENCES public.mc_001_potential_sponsors(id) ON DELETE CASCADE;
  END IF;
END $$;

COMMIT;

-- ============================================================
-- NOTE: The following 5 views were dropped via CASCADE when
-- folder_categories / folder_metrics / folder_monetization /
-- folder_value_propositions / genius_agents were dropped. They
-- are NOT recreated by this rollback (out of scope per plan --
-- only the 20 base tables are covered). Their definitions were
-- captured in AUDIT-RESULT.md for reference if manual recreation
-- is ever needed:
--   agent_overview, folder_performance_summary,
--   monetization_opportunities, revenue_by_category,
--   top_revenue_folders
-- ============================================================
