-- =====================================================================
-- DEAL-SOURCING-SCHEMA.sql
-- The 7 sourcing databases = the INTAKE side of the venture factory.
-- Feeds VENTURE-FACTORY-MAP (the 712-venture production lines) via `deals`.
--
-- Apply: Supabase MCP apply_migration, or psql -f DEAL-SOURCING-SCHEMA.sql
-- Source map per user's 8-layer deal graph (SAM.gov, USAspending, Sunbiz,
-- county assessor, BizBuySell, LinkedIn, Crunchbase, etc.)
-- =====================================================================

create extension if not exists "pgcrypto";

-- ---------------------------------------------------------------------
-- 0. Lineage: every record knows which upstream source + pull it came from
-- ---------------------------------------------------------------------
create table if not exists deal_sources (
  id            uuid primary key default gen_random_uuid(),
  source_name   text not null,              -- 'SAM.gov', 'FL-Sunbiz', 'BizBuySell'...
  source_type   text not null,              -- 'government'|'registry'|'marketplace'|'enrichment'|'assessor'
  source_url    text,
  pulled_at     timestamptz default now(),
  record_count  int default 0,
  notes         text
);

-- ---------------------------------------------------------------------
-- 1. Business owner / company database  (Secretary of State, Sunbiz, ACC)
-- ---------------------------------------------------------------------
create table if not exists deal_companies (
  id              uuid primary key default gen_random_uuid(),
  source_id       uuid references deal_sources(id),
  legal_name      text not null,
  dba             text,
  entity_type     text,                     -- LLC, Corp, etc.
  state           text,                     -- FL, AZ, NC...
  registry_id     text,                     -- Sunbiz doc #, ACC file #
  status          text,                     -- active|inactive|dissolved
  officers        jsonb,                    -- [{name, role}]
  registered_agent text,
  formed_on       date,
  contact         jsonb,                    -- {email, phone, address}
  raw             jsonb,
  created_at      timestamptz default now()
);

-- ---------------------------------------------------------------------
-- 2. Government contract database  (SAM.gov, USAspending, FPDS)
-- ---------------------------------------------------------------------
create table if not exists deal_gov_contracts (
  id              uuid primary key default gen_random_uuid(),
  source_id       uuid references deal_sources(id),
  kind            text not null,            -- 'opportunity'|'award'
  notice_id       text,                     -- SAM.gov notice / award id
  title           text,
  agency          text,
  naics           text,
  set_aside       text,                     -- 8(a), SDVOSB, none...
  amount_usd      numeric,
  posted_on       date,
  response_due    date,
  place_of_perf   text,
  vendor_name     text,                     -- for awards
  url             text,
  raw             jsonb,
  created_at      timestamptz default now()
);

-- ---------------------------------------------------------------------
-- 3. Acquisition target database  (BizBuySell, Acquire.com, Flippa, Axial)
-- ---------------------------------------------------------------------
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

-- ---------------------------------------------------------------------
-- 4. Commercial real estate database  (LoopNet, Crexi, county assessor)
-- ---------------------------------------------------------------------
create table if not exists deal_properties (
  id              uuid primary key default gen_random_uuid(),
  source_id       uuid references deal_sources(id),
  parcel_id       text,                     -- assessor APN
  address         text,
  county          text,                     -- Mecklenburg first
  property_type   text,                     -- office, industrial, retail, multifamily
  owner_name      text,                     -- true ownership from assessor
  assessed_value  numeric,
  list_price      numeric,
  sqft            numeric,
  cap_rate        numeric,
  url             text,
  raw             jsonb,
  created_at      timestamptz default now()
);

-- ---------------------------------------------------------------------
-- 5. Recruiter / talent database  (LinkedIn, Indeed, Wellfound)
-- ---------------------------------------------------------------------
create table if not exists deal_talent (
  id              uuid primary key default gen_random_uuid(),
  source_id       uuid references deal_sources(id),
  full_name       text,
  headline        text,
  role_category   text,                     -- operator, recruiter, dev, sales, PM
  company         text,
  location        text,
  profile_url     text,
  skills          text[],
  contact         jsonb,
  raw             jsonb,
  created_at      timestamptz default now()
);

-- ---------------------------------------------------------------------
-- 6. Investor / family office database  (Crunchbase, PitchBook, Preqin)
-- ---------------------------------------------------------------------
create table if not exists deal_investors (
  id              uuid primary key default gen_random_uuid(),
  source_id       uuid references deal_sources(id),
  firm_name       text not null,
  investor_type   text,                     -- VC, PE, angel, family-office, LP
  focus_stages    text[],
  focus_sectors   text[],
  aum_usd         numeric,
  location        text,
  contact         jsonb,
  url             text,
  raw             jsonb,
  created_at      timestamptz default now()
);

-- ---------------------------------------------------------------------
-- 7. Supplier / vendor database  (Thomasnet, Alibaba, Panjiva, ImportGenius)
-- ---------------------------------------------------------------------
create table if not exists deal_vendors (
  id              uuid primary key default gen_random_uuid(),
  source_id       uuid references deal_sources(id),
  vendor_name     text not null,
  category        text,
  country         text,
  products        text[],
  moq             text,
  contact         jsonb,
  url             text,
  raw             jsonb,
  created_at      timestamptz default now()
);

-- ---------------------------------------------------------------------
-- PIPELINE: ties any sourced record -> a venture in VENTURE-FACTORY-MAP
-- This is the deal graph:  source -> intake -> venture -> cash flow
-- ---------------------------------------------------------------------
create table if not exists deals (
  id              uuid primary key default gen_random_uuid(),
  deal_layer      text not null,            -- L1 Talent ... L8 Capital
  entity_table    text not null,            -- which deal_* table the record lives in
  entity_id       uuid not null,            -- fk into that table
  venture_id      text,                     -- links to VENTURE-FACTORY-MAP.venture_id
  stage           text default 'intake',    -- intake|qualified|contacted|contracted|cash
  value_usd       numeric,
  owner           text,
  next_action     text,
  updated_at      timestamptz default now(),
  created_at      timestamptz default now()
);

-- ---------------------------------------------------------------------
-- Indexes for the common lookups
-- ---------------------------------------------------------------------
create index if not exists idx_companies_state    on deal_companies(state);
create index if not exists idx_gov_kind_due        on deal_gov_contracts(kind, response_due);
create index if not exists idx_props_county        on deal_properties(county);
create index if not exists idx_talent_role         on deal_talent(role_category);
create index if not exists idx_deals_stage         on deals(stage);
create index if not exists idx_deals_venture       on deals(venture_id);
create index if not exists idx_deals_layer         on deals(deal_layer);
