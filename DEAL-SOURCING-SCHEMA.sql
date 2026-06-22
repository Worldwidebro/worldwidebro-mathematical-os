-- =====================================================================
-- DEAL-SOURCING-SCHEMA.sql   (APPLIED to CivilizationOS 2026-06-20)
-- The deal-INTAKE side of the venture factory. Feeds VENTURE-FACTORY-MAP
-- (the 712-venture production lines) via deal_pipeline.venture_id.
--
-- RECONCILED against existing Supabase tables — only NEW tables are below.
-- The 7-database model maps as:
--   1 Business owner/company .... deal_companies            (NEW - this file)
--   2 Government contracts ....... gov_opportunities + gov_awards (EXISTS, reuse)
--   3 Acquisition targets ........ deal_acquisition_targets  (NEW - this file)
--   4 Commercial real estate ..... deal_properties (sourcing, NEW) +
--                                  real_estate_properties (owned, EXISTS)
--   5 Recruiter/talent ........... leads / contacts / staffing_prospects (EXISTS, reuse)
--   6 Investor/family office ..... investors                 (EXISTS, reuse)
--   7 Supplier/vendor ............ vendors                   (EXISTS, reuse)
--   + lineage .................... deal_sources              (NEW)
--   + connective funnel .......... deal_pipeline             (NEW; existing `deals`
--                                  is an unrelated arbitrage table, left untouched)
-- =====================================================================

create extension if not exists "pgcrypto";

create table if not exists deal_sources (
  id            uuid primary key default gen_random_uuid(),
  source_name   text not null,
  source_type   text not null,
  source_url    text,
  pulled_at     timestamptz default now(),
  record_count  int default 0,
  notes         text
);

create table if not exists deal_companies (
  id               uuid primary key default gen_random_uuid(),
  source_id        uuid references deal_sources(id),
  legal_name       text not null,
  dba              text,
  entity_type      text,
  state            text,
  registry_id      text,
  status           text,
  officers         jsonb,
  registered_agent text,
  formed_on        date,
  contact          jsonb,
  raw              jsonb,
  created_at       timestamptz default now()
);

create table if not exists deal_acquisition_targets (
  id              uuid primary key default gen_random_uuid(),
  source_id       uuid references deal_sources(id),
  listing_id      text,
  title           text,
  industry        text,
  location        text,
  asking_price    numeric,
  revenue_usd     numeric,
  cash_flow_usd   numeric,
  multiple        numeric,
  url             text,
  raw             jsonb,
  created_at      timestamptz default now()
);

create table if not exists deal_properties (
  id              uuid primary key default gen_random_uuid(),
  source_id       uuid references deal_sources(id),
  parcel_id       text,
  address         text,
  county          text,
  property_type   text,
  owner_name      text,
  assessed_value  numeric,
  list_price      numeric,
  sqft            numeric,
  cap_rate        numeric,
  url             text,
  raw             jsonb,
  created_at      timestamptz default now()
);

-- entity_id is text so it can reference uuid PKs (deal_*) and bigint PKs (gov_*)
create table if not exists deal_pipeline (
  id              uuid primary key default gen_random_uuid(),
  deal_layer      text not null,
  entity_table    text not null,
  entity_id       text not null,
  venture_id      text,
  stage           text default 'intake',
  value_usd       numeric,
  owner           text,
  next_action     text,
  updated_at      timestamptz default now(),
  created_at      timestamptz default now()
);

create index if not exists idx_dealco_state    on deal_companies(state);
create index if not exists idx_dealprop_county  on deal_properties(county);
create index if not exists idx_dealpipe_stage   on deal_pipeline(stage);
create index if not exists idx_dealpipe_venture on deal_pipeline(venture_id);
create index if not exists idx_dealpipe_layer   on deal_pipeline(deal_layer);
create index if not exists idx_dealpipe_entity  on deal_pipeline(entity_table, entity_id);
