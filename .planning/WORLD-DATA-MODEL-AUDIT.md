# WORLD DATA MODEL AUDIT
**Date:** August 4, 2026 | **Status:** Analysis Complete  
**Infrastructure:** All 5 core databases running ✅

---

## EXECUTIVE SUMMARY

You have **60% of the World Data Model infrastructure built**. The substrate exists; it needs integration and data ingestion.

```
HAVE (Working)
├── Infrastructure ✅ (Docker, Neo4j, Postgres, Qdrant, Redis, Langfuse)
├── Neo4j schema ✅ (Agent, Task, Capability, Tool, Workflow, Venture, OPCO, Metric)
├── Supabase tables ✅ (venture_leads table created)
├── Registry schemas ✅ (registry.schema.yaml exists)
├── Venture scorecard ✅ (712 ventures × 20 attributes)
└── Repository registry ✅ (237 repos tracked)

MISSING (Needs data ingestion or schema)
├── Customer/Account entity model
├── Transaction ledger (orders, payments, expenses)
├── Market/opportunity data model
├── Risk/compliance registry
├── Decision history (decisions → outcomes)
├── Knowledge/document inventory
├── Agent execution logs (Langfuse → Neo4j bridge)
└── Infrastructure inventory (physical/cloud assets)
```

---

## WHAT YOU HAVE BY DOMAIN

### ✅ 1. IDENTITY DATA
**Status:** Partial

| Entity | Source | Coverage | Gaps |
|--------|--------|----------|------|
| Ventures | VENTURE-READINESS-SCORECARD-V2.csv | 712 ventures w/ sector, stage, readiness | No legal entity info, no owner |
| Repositories | REPOSITORY-REGISTRY.json | 237 repos (17 archived) | No ownership, no capability mapping |
| People | CONTACTS-INITIAL.csv | ~50 people | No roles, authority, teams |
| Organizations | Implicit in ventures | Not modeled | Must create OPCO table |
| Agents | Neo4j schema exists | 0 agents ingested | Need agent_registry.csv |
| Skills | registry.schema.yaml | Listed but not mapped | Need skill_registry.csv |
| Tools/MCPs | registry.schema.yaml | Listed but not mapped | Need tool_registry.csv |

---

### ✅ 2. INFRASTRUCTURE DATA
**Status:** Running but not modeled

| Asset | Status | Coverage |
|-------|--------|----------|
| Docker | Running ✅ | 8 containers live |
| Machines | Mac Air + Mac Studio | Implicit |
| Storage | 96% full | Total/used/free tracked |
| Networks | Not tracked | Need network_inventory |
| Domains | Not tracked | Need domain_registry |

---

### ✅ 3. SOFTWARE/REPOSITORY DATA
**Status:** Partial inventory

| Item | Source | Coverage | Gap |
|------|--------|----------|-----|
| Repo count | REPOSITORY-REGISTRY.json | 237 local + 500 GitHub | No dependencies |
| Repo→Venture | Implicit | ~50 wired | 187 repos unconnected |
| Repo→Capability | Not mapped | 0% | Need bridge table |
| Commits | In .git | Raw Git data | Not indexed |

---

### ✅ 4. VENTURE DATA
**Status:** Metadata complete, operations empty

| Attribute | Source | Coverage | Gap |
|-----------|--------|----------|-----|
| Venture ID | SCORECARD | 712 | ✅ |
| Name, sector | SCORECARD | 712 | ✅ |
| Stage, readiness | SCORECARD | 712 | ✅ |
| Revenue model | SCORECARD | flagged | ❌ No amounts |
| Customers | venture_leads | CON-001 only | 0 ventures live |
| Transactions | None | 0 | Need order, payment tables |
| Competitors | Not tracked | 0 | Need competitor table |
| Risks | Not tracked | 0 | Need risk_register |
| Market | Not tracked | 0 | Need market_data |

---

### ✅ 5. CUSTOMER/TRANSACTION DATA
**Status:** Schema created, zero data

| Entity | Status | Tables | Rows |
|--------|--------|--------|------|
| Leads | ✅ Schema | venture_leads | 0 live |
| Customers | ❌ | None | 0 |
| Orders | ❌ | None | 0 |
| Invoices | ❌ | None | 0 |
| Payments | ❌ | None | 0 (webhooks built) |
| Contracts | ❌ | None | 0 |

---

### ✅ 6. AGENT/CAPABILITY DATA
**Status:** Schema exists, no data

| Item | Source | Ingested |
|------|--------|----------|
| Agent schema | Neo4j schema.cypher | No |
| Skill schema | registry.schema.yaml | No |
| Tool schema | registry.schema.yaml | No |
| Agent→Skill | HAS_CAPABILITY rel | No |
| Executions | Langfuse running | No (needs bridge) |

---

### ✅ 7. KNOWLEDGE/MEMORY DATA
**Status:** Partially organized

| Source | Type | Coverage |
|--------|------|----------|
| Obsidian vault | Documents | 15K+ notes |
| Memory YAML | Structured | ~50 memories |
| Git commits | Change log | 237 repos |
| Langfuse traces | Execution log | Live |
| Decisions | Planning files | Sparse |

---

### ✅ 8. OBSERVABILITY DATA
**Status:** Collection running, not integrated

| Signal | Source | Status |
|--------|--------|--------|
| Metrics | Prometheus | Not running |
| Logs | Various | Scattered |
| Traces | Langfuse | ✅ Live |
| Events | Docker, Git | Implicit |
| Alerts | None | Not configured |
| Cost | None | Not tracked |

---

## THE MINIMAL REGISTRY (Start Here)

**8 core tables:**

```sql
-- Identity
CREATE TABLE person (
  id UUID PRIMARY KEY,
  name TEXT NOT NULL,
  role TEXT,
  email TEXT UNIQUE,
  authority_level INT,
  created_at TIMESTAMP
);

-- Organization
CREATE TABLE organization (
  id UUID PRIMARY KEY,
  canonical_name TEXT NOT NULL,
  type TEXT, -- 'company','team','service','venture'
  parent_id UUID REFERENCES organization(id),
  status TEXT,
  created_at TIMESTAMP
);

-- Ventures
CREATE TABLE venture (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  sector TEXT,
  stage TEXT,
  owner_id UUID REFERENCES person(id),
  readiness_pct NUMERIC,
  revenue_ytd_cents BIGINT DEFAULT 0,
  expense_ytd_cents BIGINT DEFAULT 0,
  created_at TIMESTAMP
);

-- Customers
CREATE TABLE customer (
  id UUID PRIMARY KEY,
  venture_id TEXT REFERENCES venture(id),
  name TEXT NOT NULL,
  email TEXT,
  phone TEXT,
  stage TEXT, -- 'lead','prospect','customer','churned'
  value_cents BIGINT,
  created_at TIMESTAMP
);

-- Transactions
CREATE TABLE transaction (
  id UUID PRIMARY KEY,
  venture_id TEXT REFERENCES venture(id),
  customer_id UUID REFERENCES customer(id),
  type TEXT, -- 'lead','sale','order','invoice','payment','refund','expense'
  amount_cents BIGINT,
  status TEXT,
  verified BOOLEAN,
  created_at TIMESTAMP
);

-- Capabilities
CREATE TABLE capability (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  category TEXT,
  owner_id UUID REFERENCES person(id),
  agents TEXT[], -- JSON array
  tools TEXT[], -- JSON array
  created_at TIMESTAMP
);

-- Decisions
CREATE TABLE decision (
  id UUID PRIMARY KEY,
  venture_id TEXT REFERENCES venture(id),
  goal TEXT NOT NULL,
  options JSONB, -- {name, expected_outcome, cost, risk}
  selected_option TEXT,
  reason TEXT,
  actual_outcome TEXT,
  created_at TIMESTAMP,
  outcome_at TIMESTAMP
);

-- Knowledge
CREATE TABLE knowledge (
  id UUID PRIMARY KEY,
  type TEXT, -- 'fact','document','procedure','lesson','decision'
  title TEXT NOT NULL,
  source TEXT,
  confidence TEXT, -- 'high','medium','low'
  valid_from TIMESTAMP,
  valid_until TIMESTAMP,
  created_at TIMESTAMP
);
```

---

## INGEST ORDER

1. Person (from contacts-extracted.csv)
2. Organization (from ventures)
3. Venture (from VENTURE-READINESS-SCORECARD-V2.csv)
4. Customer (from venture_leads + Stripe API)
5. Transaction (from Stripe webhooks + expenses)
6. Capability (from agents.csv + skills.csv)
7. Decision (from planning docs)
8. Knowledge (from Obsidian + memory YAML)

---

## GAPS BY PRIORITY

### 🔴 CRITICAL (This week)
- [ ] Customer/transaction tables (blocks revenue data)
- [ ] Agent execution → Neo4j (blocks observability)
- [ ] Decision history table (blocks learning)

### 🟡 HIGH (Week 2-3)
- [ ] Infrastructure inventory
- [ ] Risk register
- [ ] Market data
- [ ] Competitor analysis

### 🟢 MEDIUM (Week 4+)
- [ ] Policy/compliance tables
- [ ] Knowledge extraction
- [ ] Cost ledger

---

## THIS WEEK'S PARALLEL WORK

1. Deploy CON-001 (20 min)
2. Create 8-table schema (1 hour)
3. Backfill from Stripe (30 min)
4. Wire Neo4j sync (1 hour)

**Result: 4 hours → Live transactional truth + graph model**
