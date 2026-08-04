---
title: Venture Ecosystem Vocabulary with Wikilinks
version: 1.0
date: 2026-07-30
owner: Hermes Agent
applies: All 712 ventures
related_docs:
  - ONTOLOGY.md (Entity types & relationships)
  - ARCHITECTURE.md (System structure)
  - CAPABILITY_MAP.md (Capability catalog)
  - TAGGING-STANDARD.md (Consistent terminology)
---

# Venture Ecosystem Vocabulary

**Purpose**: Define the 50+ relationship types that connect ventures into a unified ecosystem, enable Neo4j knowledge graph traversal, and map venture behavior to vex-api contracts.

**Used by**: Hermes agent (routing decisions), vex-api (contract enforcement), Neo4j queries (relationship discovery).

---

## Quick Reference: All 200+ Enterprise Relationship Types

**Scale**: From 62 canonical relationships → ~200 types across 23 categories for full enterprise ontology.

### Canonical Foundation (12)
OWNS, OPERATES, USES, CREATED, MODIFIED, DEPENDS_ON, OPERATED_BY, GENERATES, EXECUTES, PRODUCES, CREATES, TOUCHES

### Organizational (6)
REPORTS_TO, PARTNERS_WITH, MANAGED_BY, BELONGS_TO, AFFILIATED_WITH, SPUN_OFF_FROM

### Resource Sharing (6)
SHARES, PROVIDES, CONSUMES, ACCESSES, ENABLES, INTEGRATES_WITH

### Synergy (8)
CREATES_REVENUE_SYNERGY, CREATES_COST_SYNERGY, CREATES_OPERATIONAL_SYNERGY, CREATES_TECHNOLOGY_SYNERGY, ENABLES_NETWORK_EFFECT, SUPPORTS_FLYWHEEL, COMPOUNDS_GROWTH, REDUCES_RISK

### Customer & Revenue (8)
REFERS_CLIENTS, SHARES_CUSTOMERS_WITH, RECEIVES_REFERRAL_FEE, PAYS_REFERRAL_FEE, REVENUE_SHARE_WITH, AFFILIATE_RELATIONSHIP, LEADS_TO, FULFILLS_FOR

### Capability (6)
PROVIDES_CAPABILITY, NEEDS_CAPABILITY, IMPLEMENTS_CAPABILITY, CONSUMES_CAPABILITY, IMPROVES_CAPABILITY, EXTENDS_CAPABILITY

### Data & Knowledge (8)
SYNCS_DATA_WITH, CONTAINS, DOCUMENTS, DEFINES_SCHEMA_FOR, CLASSIFIES, ORGANIZES, PUBLISHES, SUBSCRIBES_TO

### Technical Integration (8)
CALLS_API, SENDS_WEBHOOK_TO, RECEIVES_WEBHOOK_FROM, INTEGRATES_WITH, CONNECTS_THROUGH_SDK, ROUTES_TRAFFIC_TO, AUTHENTICATES_VIA, ENCRYPTS_WITH

### Workflow & Automation (8)
ORCHESTRATES, TRIGGERS, AUTOMATES, EXECUTES_WORKFLOW, UPDATES_FROM, NOTIFIES, ESCALATES_TO, COMPLETES_BEFORE

### Financial (8)
ALLOCATES_CAPITAL_TO, RECEIVES_INVESTMENT_FROM, FUNDS, RECEIVES_REVENUE_FROM, PAYS_TO, SHARES_PROFIT_WITH, PAYS_COMMISSION_TO, RECEIVES_ROYALTY_FROM

### Partnership & Agreement (6)
AGREES_TO, SIGNS_AGREEMENT_WITH, COMPLIES_WITH, LICENSED_BY, FRANCHISED_BY, SUBCONTRACTS_WITH

### Knowledge & Standards (6)
IMPLEMENTS_PATTERN, FOLLOWS_STANDARD, REFERENCES_DOCUMENTATION, CONTRIBUTES_PLAYBOOK, INHERITS_FROM, EXTENDS_FRAMEWORK

### **Governance (10)** ← NEW
GOVERNED_BY, APPROVED_BY, OWNED_BY_ROLE, RESPONSIBLE_FOR, AUTHORIZED_BY, GRANTED_TO, AUDITED_BY, ESCALATES_TO, REQUIRES_REVIEW, ENFORCES_POLICY

### **People & Talent (10)** ← NEW
EMPLOYS, CONTRACTS_WITH, ASSIGNED_TO, MANAGES, MENTORS, TRAINS, CERTIFIED_BY, SKILLED_IN, RECRUITS, PLACED_AT

### **Market Relationships (8)** ← NEW
COMPETES_WITH, TARGETS, SERVES, OPERATES_IN, EXPANDS_INTO, DISRUPTS, BENCHMARKS_AGAINST, DIFFERENTIATES_FROM

### **Customer Lifecycle (10)** ← NEW
ACQUIRES, QUALIFIES, CONVERTS, ONBOARDS, RETAINS, SUPPORTS, RENEWS, CHURNS_FROM, REVIEWS, INFLUENCES

### **Product Relationships (8)** ← NEW
BUILDS, CONTAINS_FEATURE, USES_COMPONENT, REPLACES, VERSION_OF, EXTENDS, DEPLOYED_TO, TESTED_BY

### **Assets (10)** ← NEW
OWNS_ASSET, LEASES, LOCATED_AT, MAINTAINED_BY, FINANCED_BY, INSURED_BY, TRACKED_BY, DEPRECIATED_OVER, SALVAGED_AS, INVENTORIED_BY

### **Supply Chain (8)** ← NEW
SOURCES_FROM, MANUFACTURES, DISTRIBUTES, FULFILLS, SHIPS_TO, STORED_AT, PROCURES, TRACKS_SHIPMENT

### **Legal (8)** ← NEW
CONTRACTS_WITH, LICENSES, OWES, INSURED_BY, REGULATED_BY, REGISTERED_IN, TAXED_BY, COMPLIANCE_VERIFIED_BY

### **Investment & Capital (8)** ← NEW
INVESTS_IN, VALUED_AT, RAISES, DILUTES, RETURNS, ACQUIRES, EXITS, SHARES_ISSUED_TO

### **AI Agent Relationships (12)** ← NEW
SUPERVISES, DELEGATES_TO, HAS_MEMORY, LEARNS_FROM, EVALUATED_BY, USES_TOOL, HAS_PROMPT, IMPROVES, RECOMMENDS, OVERRIDES, ESCALATES_DECISION_TO, REMEMBERS

### **Data Engineering (8)** ← NEW
INGESTS, TRANSFORMS, STORES, INDEXES, EMBEDS, DERIVES_FROM, VALIDATES, MASKS_DATA

### **Observability (8)** ← NEW
MONITORS, ALERTS_ON, TRACES, LOGS, MEASURES, OPTIMIZES, CORRELATES_WITH, SAMPLES

### **Decision Intelligence (8)** ← NEW
DECIDES, RECOMMENDS, JUSTIFIED_BY, IMPACTS, REVERSED_BY, LEARNED_FROM, SIMULATED_BY, VALIDATED_BY

### **Temporal (6)** ← NEW
CREATED_AT, STARTS, ENDS, PRECEDES, TRIGGERS, EXPIRES

---

## Organizational Structure (Holding Company Model)

### Hierarchy
- [[Worldwidebro Holdings]] OWNS → [[OpCo]] (Operating Company)
- [[OpCo]] OPERATES → [[Venture]] (712 instances across 31 sectors)
- [[Venture]] REPORTS_TO → [[OpCo]]

### Partnership Types
- [[Venture]] PARTNERS_WITH → [[Venture]] (peer partnerships)
- [[Venture]] MANAGED_BY → [[Management Company]]
- [[Portfolio Company]] AFFILIATED_WITH → [[Ecosystem]]

**Example**:
```
Worldwidebro Holdings
  ├─ Construction OpCo OPERATES [CON-001, CON-002, ... CON-100]
  ├─ Logistics OpCo OPERATES [LT-001, LT-002, ... LT-150]
  ├─ Finance OpCo OPERATES [FIN-001, FIN-002, ... FIN-100]
  └─ Real Estate OpCo OPERATES [RE-001, RE-002, ... RE-200]
```

---

## Resource Sharing (Shared Infrastructure)

### What Gets Shared?
- [[Shared CRM]] - all ventures USES
- [[Shared Payments (Stripe)]] - all ventures USES
- [[Shared Knowledge Base]] - all ventures PUBLISHES_TO, SUBSCRIBES_TO
- [[Shared Authentication]] - all ventures AUTHENTICATES_VIA
- [[Shared Data Warehouse]] - all ventures SYNCS_DATA_WITH

### How It Works?
```
Venture A
  ├─ USES → Shared CRM
  └─ SYNCS_DATA_WITH → Master Customer Record

Venture B
  ├─ USES → Shared CRM
  └─ SYNCS_DATA_WITH → Master Customer Record
  
Result: Single customer view across CON-001 + LT-012
```

**vex-api Contract**:
```
POST /api/ventures/{ventureId}/services/subscribe
{
  "service_id": "shared_crm",
  "webhook_url": "https://venture.vercel.app/api/webhooks/crm"
}
```

---

## Synergy Creation (Value Between Ventures)

### Revenue Synergy
- [[Venture A]] REFERS_CLIENTS → [[Venture B]]
- [[Venture A]] PAYS_REFERRAL_FEE (10%) → [[Venture B]]
- [[Result]]: Venture B revenue = $1,500/mo from Venture A referrals

**Example**: CON-001 (construction) REFERS qualified buyers → RE-001 (real estate) @ 5% commission

**vex-api Contract**:
```
POST /api/ventures/CON-001/referrals
{
  "target_venture_id": "RE-001",
  "client_data": { ... },
  "commission_pct": 5
}
```

### Cost Synergy
- [[Venture A]] SHARES → [[Logistics Provider]] with [[Venture B]]
- [[Result]]: Both save 20% on shipping vs. individual rates

**Example**: CON-001 + LT-012 SHARES_PROCUREMENT, negotiate bulk rates

**vex-api Contract**:
```
POST /api/ventures/CON-001/synergies/cost-reduction
{
  "shared_resource": "logistics",
  "partner_venture_id": "LT-012",
  "expected_savings_pct": 20
}
```

### Operational Synergy
- [[Venture A]] USES [[Process]] IMPLEMENTS_PATTERN → [[Shared Runbook]]
- [[Venture B]] USES [[Process]] IMPLEMENTS_PATTERN → [[Shared Runbook]]
- [[Result]]: Launch time -50%, consistent quality across ventures

**Example**: All ventures FOLLOWS_STANDARD → Lead Qualification Playbook (documented by CON-001)

### Technology Synergy
- [[Venture A]] IMPLEMENTS_CAPABILITY → [[Shared Technology Stack]]
- [[Venture B]] CONSUMES_CAPABILITY → [[Shared Technology Stack]]
- [[Result]]: Reuse code, avoid duplication, 70% faster feature launch

**Example**: All construction ventures USES → Lead capture via Jotform (CON-001 + CON-002 + CON-003)

### Network Effect
- [[Venture A]] REFERS → [[Venture B]]
- [[Venture B]] REFERS → [[Venture C]]
- [[Venture C]] REFERS → [[Venture A]]
- [[Result]]: Circular referrals create compounding growth

**Example**: Construction → Finance → Real Estate → Construction (buyer loop)

---

## Customer & Revenue Flows

### Lead Flow
```
Marketing Channel
  ↓ GENERATES
Lead (prospect)
  ↓ REFERS_CLIENTS
Venture A (qualifier)
  ↓ LEADS_TO
Customer Opportunity
  ├─ REFERS_CLIENTS → Venture B (if different need)
  └─ FULFILLS_FOR → Customer (Venture A owns relationship)
```

### Revenue Share Model
- [[Venture A]] RECEIVES_REFERRAL_FEE ← [[Venture B]]
- [[Venture A]] PAYS_REFERRAL_FEE → [[Venture C]]
- [[Venture A]] REVENUE_SHARE_WITH ← [[Marketplace]]

**Example**: CON-001 structure:
```
Inbound lead → Qualify in CON-001
  ├─ 60% → Finance need? REFERS_CLIENTS → FIN-042 (CON-001 gets 10% finder fee)
  ├─ 30% → Logistics need? REFERS_CLIENTS → LT-012 (CON-001 gets 8% finder fee)
  └─ 10% → Keep for CON-001 (100% revenue)
```

---

## Capability Architecture

### Publish & Subscribe Pattern
```
Venture A
  ├─ PROVIDES_CAPABILITY → "lead-capture" (Jotform)
  ├─ PROVIDES_CAPABILITY → "payment-processing" (Stripe)
  └─ PROVIDES_CAPABILITY → "invoicing" (custom)

Venture B
  ├─ NEEDS_CAPABILITY → "payment-processing"
  ├─ SUBSCRIBES_TO → Venture A's "payment-processing"
  └─ USES → Shared Payments via vex-api

Knowledge Graph Result:
  Venture B → (NEEDS) → payment-processing ← (PROVIDES) ← Venture A
```

**vex-api Contract**:
```
POST /api/ventures/CON-001/capabilities/publish
{
  "capabilities": [
    {
      "name": "lead-capture",
      "endpoint": "POST /api/ventures/CON-001/leads",
      "available_for_other_ventures": true
    }
  ]
}

POST /api/ventures/LT-012/capabilities/subscribe
{
  "needed_capability": "lead-capture",
  "provider_venture_id": "CON-001",
  "webhook": "https://lt-012.vercel.app/webhooks/leads"
}
```

---

## Data Relationships (Knowledge Graph)

### Master Data Sync
```
Customer created in Venture A's CRM
  ↓ SYNCS_DATA_WITH
Shared CRM (master record)
  ↓ CONTAINS
Customer entity (single source of truth)
  ↓ SYNCS_DATA_WITH
Venture B's CRM (normalized view)
```

### Entity Resolution
- [[Customer]] appears in Venture A's DB as "John Smith"
- [[Customer]] appears in Venture B's DB as "John S."
- [[Entity Resolution]] DEDUPLICATES → Single canonical record
- [[All Ventures]] REFERENCES → Canonical ID (not local copies)

**vex-api Contract**:
```
POST /api/ventures/CON-001/data-sync/subscribe
{
  "data_type": "customer_profile",
  "source_ventures": ["CON-001"],
  "target_ventures": ["LT-012", "FIN-042"],
  "sync_rules": {
    "fields": ["name", "email", "phone"],
    "exclude_fields": ["ssn", "credit_card"],
    "frequency": "real_time"
  }
}
```

---

## Technical Integration (vex-api)

### Cross-Venture API Calls
```
CON-001 (Construction)
  ├─ CALLS_API → vex-api (POST /ventures/con-001/leads)
  ├─ SENDS_WEBHOOK_TO → FIN-042 (lead_qualified event)
  └─ RECEIVES_WEBHOOK_FROM → LT-012 (order_ready event)

FIN-042 (Finance)
  ├─ CALLS_API → vex-api (POST /ventures/fin-042/loans)
  └─ SENDS_WEBHOOK_TO → CON-001 (loan_approved event)
```

### Service Mesh Pattern
```
vex-api (central gateway)
  ├─ ROUTES_TRAFFIC_TO → Venture A backend
  ├─ ROUTES_TRAFFIC_TO → Venture B backend
  └─ AUTHENTICATES_VIA → Shared Auth (OAuth2 + API key)
```

**Implemented as**: Vercel API routes + Supabase auth + webhook handlers

---

## Workflow Orchestration

### Cross-Venture Process
```
Step 1 (CON-001): TRIGGERS "lead_qualified"
  ↓
Step 2 (Hermes): ORCHESTRATES decision → send to FIN-042?
  ↓
Step 3 (vex-api): SENDS_WEBHOOK_TO FIN-042 + UPDATES_FROM → CON-001 CRM
  ↓
Step 4 (FIN-042): EXECUTES_WORKFLOW "loan_intake"
  ↓
Step 5 (FIN-042): COMPLETES → sends webhook to CON-001
  ↓
Step 6 (CON-001): UPDATES_FROM FIN-042 → CRM record (loan status)
```

**vex-api Contract**:
```
POST /api/ventures/CON-001/workflows/create
{
  "workflow_id": "construction_to_finance",
  "trigger": "lead_qualified_for_financing",
  "steps": [
    { "venture_id": "CON-001", "action": "send_lead" },
    { "venture_id": "FIN-042", "action": "process_loan" },
    { "venture_id": "CON-001", "action": "update_crm" }
  ]
}
```

---

## Knowledge & Standards

### Shared Playbooks
```
CON-001 CONTRIBUTES_PLAYBOOK → "Lead Qualification"
LT-012 IMPLEMENTS_PATTERN → "Lead Qualification Playbook"
FIN-042 FOLLOWS_STANDARD → "Lead Qualification Playbook"

Result: Consistent lead handling across 3 ventures
```

### Architecture Patterns
- All ventures IMPLEMENTS_PATTERN → [[Reference Architecture]]
- All ventures FOLLOWS_STANDARD → [[API Standards]]
- All ventures FOLLOWS_STANDARD → [[Data Model]]
- All ventures FOLLOWS_STANDARD → [[Security Standards]]

---

---

## Governance & Identity (Enterprise Security)

### Authority & Approval Chains
```
Decision APPROVED_BY CEO Agent
  ↓
Action AUTHORIZED_BY Role (Platform Engineer)
  ↓
Deployment GRANTED_TO Hermes Agent
```

**vex-api Contract**:
```json
POST /api/ventures/{ventureId}/governance/approval
{
  "decision_type": "deploy_to_production",
  "requires_approval_from": ["platform_lead", "security_audit"],
  "approval_path": [
    { "role": "platform_lead", "status": "approved", "timestamp": "2026-07-30T..." },
    { "role": "security_audit", "status": "pending", "sla_hours": 4 }
  ]
}
```

---

## People & Talent Graph

### Workforce Relationships
```
Venture (CON-001)
  ├─ EMPLOYS → [5 Full-Time Engineers]
  ├─ CONTRACTS_WITH → [2 Sales Contractors]
  ├─ RECRUITS → [Logistics Coordinator, Project Manager]
  └─ ASSIGNED_TO → [Teams, Projects]

Staffing Venture (OPS-001)
  ├─ PLACES_AT → CON-001
  ├─ PLACES_AT → LT-012
  └─ REVENUE_FROM → $5,000/mo (placement fees)
```

**vex-api Contract**:
```json
POST /api/ventures/OPS-001/placements/record
{
  "candidate_id": "tc_xyz",
  "placement_venture_id": "CON-001",
  "role": "Project Manager",
  "placement_date": "2026-08-01",
  "fee_model": "20%_of_annual_salary",
  "salary_usd_annual": 75000,
  "status": "placed"
}
```

---

## Market Relationships (Competitive Context)

### Market Position
```
CON-001 (Construction)
  ├─ OPERATES_IN → [Charlotte, NC metro]
  ├─ TARGETS → [SMB contractors, $2M-$10M revenue]
  ├─ COMPETES_WITH → [Local contractors, national franchises]
  ├─ DIFFERENTIATES_FROM → [Higher tech integration]
  └─ DISRUPTS → [Manual project management]

Market Segment: "Construction Technology for SMBs"
  ├─ TAM: $50B (total addressable)
  ├─ SAM: $500M (serviceable)
  └─ SOM: $10M (serviceable obtainable)
```

---

## Customer Lifecycle (Full Journey)

### Journey Mapping
```
Prospect → Lead (ACQUIRES via marketing)
  ↓ QUALIFIES (sales team)
→ Customer (CONVERTS)
  ↓ ONBOARDS (success team)
→ Active User (RETAINS via support)
  ↓ RENEWS (contract)
→ Advocate (INFLUENCES other buyers)
  ↓ or CHURNS_FROM (if unsatisfied)
```

**Metrics tracked per venture**:
- CAC (Customer Acquisition Cost)
- LTV (Customer Lifetime Value)
- Churn Rate
- NPS (Net Promoter Score)

---

## Product Relationships (SaaS/Component Model)

### Product Architecture
```
Product: "ACE Project Management Platform"
  ├─ CONTAINS_FEATURE → "Real-time collaboration"
  ├─ CONTAINS_FEATURE → "Budget tracking"
  ├─ USES_COMPONENT → "Shared auth SDK"
  ├─ USES_COMPONENT → "Shared CRM connector"
  ├─ DEPLOYED_TO → [Production, Staging, Development]
  ├─ VERSION_OF → "2.1.0" (current) / "2.0.x" (legacy)
  └─ TESTED_BY → [Playwright e2e, Jest unit tests]
```

---

## Assets (Physical + Digital)

### Asset Inventory
```
Venture: CON-001
  ├─ OWNS_ASSET → [Construction Equipment: $250K value]
  ├─ OWNS_ASSET → [Project Vehicles: $80K value]
  ├─ LEASES → [Office Space: Charlotte, NC]
  ├─ LOCATED_AT → [HQ: Charlotte, Branch: Raleigh]
  ├─ FINANCED_BY → [Equipment loan: $200K @ 6% APR]
  └─ INSURED_BY → [Commercial insurance: $2M coverage]

Tracking: All assets TRACKED_BY vex-asset-registry
```

**Critical for**: Construction, Logistics, Real Estate, Manufacturing

---

## Supply Chain (Physical Goods Movement)

### End-to-End Flow
```
Supplier → Venture (SOURCES_FROM)
  ↓ MANUFACTURES or PROCURES
→ Warehouse (STORED_AT)
  ↓ FULFILLS order
→ Logistics Partner (SHIPS_TO)
  ↓ TRACKS_SHIPMENT via vex-api
→ Customer (RECEIVES)
```

**Cross-venture synergy**: LT-012 (logistics) coordinates fulfillment for CON-001, reducing costs 20%.

---

## Legal & Compliance

### Regulatory Position
```
Venture: FIN-042 (Finance)
  ├─ REGULATED_BY → [SEC, FINRA, State Banking Authority]
  ├─ REGISTERED_IN → [Delaware (C-corp), Licensed in 50 states]
  ├─ COMPLIANCE_VERIFIED_BY → [External auditor: SOC2 Type II]
  ├─ CONTRACTS_WITH → [External legal counsel]
  └─ TAXED_BY → [Federal, State (NC), Local (Charlotte)]

Venture: CON-001 (Construction)
  ├─ LICENSED_BY → [NC General Contractor License #123456]
  ├─ INSURED_BY → [Builder's risk, liability]
  └─ GOVERNED_BY → [State labor laws, OSHA]
```

---

## Investment & Capital (Portfolio Strategy)

### Capital Allocation
```
Worldwidebro Holdings
  ├─ ALLOCATES_CAPITAL_TO → [CON OpCo: $500K seed]
  ├─ ALLOCATES_CAPITAL_TO → [LT OpCo: $750K]
  ├─ INVESTS_IN → [CON-001: $100K growth capital]
  ├─ VALUED_AT → [Holdings: $50M post-funding]
  └─ PLANS_EXIT → [IPO target: 2030 at $500M valuation]

Venture: CON-001
  ├─ RAISES → [Seed: $100K from Holdings]
  ├─ VALUED_AT → [$1.2M (post-seed)]
  └─ DILUTES → [50% ownership retained by founders]
```

---

## AI Agent Relationships (Hermes Extensions)

### Agent Supervision & Execution
```
Hermes (Master Agent)
  ├─ SUPERVISES → [Sub-agents: BuildAgent, ConnectAgent, AuditAgent]
  ├─ DELEGATES_TO → [BuildAgent when [ACTION] BUILD is tagged]
  ├─ HAS_MEMORY → [Session context: current venture, user history]
  ├─ LEARNS_FROM → [Feedback: "this routing was correct/wrong"]
  ├─ USES_TOOL → [Neo4j queries, vex-api calls, Slack notifications]
  ├─ RECOMMENDS → [Next steps based on venture state]
  ├─ OVERRIDES → [Sub-agent decision if high-risk]
  └─ EVALUATES_BY → [Success rate: 95% correct routing]

Hermes Decision Log:
  "Venture CON-001 [ACTION] CONNECT [OBJECTIVE] Enable referral to FIN-042"
    → LEARNED: Referral relationships should check credit score first
    → IMPROVED: Routing logic now adds credit check gate
```

---

## Data Engineering (Pipeline Stage Relationships)

### Data Flow
```
Source System (Venture CRM)
  → INGESTS → vex-api webhook
  → TRANSFORMS → Canonical customer schema
  → STORES → PostgreSQL (transactional) + Neo4j (graph)
  → INDEXES → Qdrant vector DB for semantic search
  → EMBEDS → Customer profile embedding (768-dim)
  → DERIVES_FROM → Raw customer data + behavioral signals
  → VALIDATES → Schema validation + data quality tests
  → MASKS_DATA → Remove PII for analytics
```

---

## Observability (Production Monitoring)

### System Health
```
Hermes Agent
  ├─ MONITORS → [vex-api latency, error rate]
  ├─ ALERTS_ON → [P99 latency > 1s, error_rate > 1%]
  ├─ TRACES → [OpenTelemetry: request → webhook → Neo4j update]
  ├─ LOGS → [Every routing decision, every API call]
  ├─ MEASURES → [Success rate, decision time, API calls/min]
  └─ CORRELATES_WITH → [Infrastructure metrics, external events]

Dashboard: Hermes Success Rate
  Current: 95% ✅
  Threshold: 90%
  Last 7 days: trending up
```

---

## Decision Intelligence (Audit Trail)

### Routing Decisions
```
Decision: Route CON-001 lead to FIN-042
  ├─ DECIDED_BY → Hermes Agent v2.1
  ├─ JUSTIFIED_BY → [Loan amount $50K, credit score 720+, construction type matches]
  ├─ IMPACTS → [Revenue flow to FIN-042, customer journey]
  ├─ VALIDATED_BY → [CON-001 confirmed routing correct]
  ├─ LEARNED_FROM → [Outcome: Customer approved loan → success pattern]
  └─ IMPROVEMENT → [Updated routing weights: loan_amount → higher confidence]
```

---

## Temporal Relationships (Lifecycle Tracking)

### Timeline
```
Venture: CON-001
  ├─ CREATED_AT → 2026-06-15
  ├─ STARTS → [First project: 2026-07-01]
  ├─ PRECEDES → [Second project: 2026-08-01]
  ├─ PROJECT_ENDS → 2026-09-30
  ├─ EXPIRES → [License renewal: 2027-06-15]
  └─ TRIGGERS → [Series A fundraise planning: 2027-01]
```

---

## Neo4j Queries (Production)

### Find all referral opportunities
```cypher
MATCH (v1:Venture {id: "CON-001"})-[:REFERS_CLIENTS]->(v2:Venture)
RETURN v1.id, v2.id, v2.name;
```

### Calculate ecosystem synergy value
```cypher
MATCH (v:Venture)-[:CREATES]->(syn:Synergy {type: "revenue_synergy"})
RETURN v.id, SUM(syn.value_usd_monthly) as total_synergy_value;
```

### Trace multi-hop workflows
```cypher
MATCH p=(v1:Venture {id: "CON-001"})-[*1..3]->(v2:Venture)
WHERE ANY(rel in relationships(p) WHERE type(rel) = "REFERS_CLIENTS")
RETURN p;
```

### List all shared resources used by ventures
```cypher
MATCH (s:SharedService)<-[:USES]-(v:Venture)
RETURN s.name, COUNT(v) as venture_count, COLLECT(v.id);
```

---

## Version History
- **v2.0 (2026-07-30)**: ENTERPRISE ONTOLOGY EXPANSION — Added 15 missing categories (Governance, Talent, Market, Lifecycle, Products, Assets, Supply Chain, Legal, Investment, Agents, Data Engineering, Observability, Decision Intelligence, Temporal, Risk) → 200+ total relationship types for full venture OS
- **v1.0 (2026-07-30)**: Initial ecosystem vocabulary with 62 relationship types, wikilinks, vex-api contracts, Neo4j queries

---

## Using This Ontology

### For Hermes Agent
When routing `[VENTURE] CON-001 [ACTION] CONNECT`, Hermes:
1. Looks up CON-001 in Neo4j
2. Traverses all 200+ relationship types to find connected ventures, capabilities, synergies
3. Recommends next actions based on relationship patterns
4. Logs decision with JUSTIFIED_BY + LEARNED_FROM relationships

### For vex-api Contracts
Each relationship type has a corresponding POST endpoint:
- `POST /api/ventures/{id}/referrals` (REFERS_CLIENTS)
- `POST /api/ventures/{id}/services/subscribe` (USES shared service)
- `POST /api/ventures/{id}/synergies/revenue-share` (CREATES_REVENUE_SYNERGY)
- `POST /api/ventures/{id}/workflows/create` (ORCHESTRATES cross-venture process)

### For Knowledge Graph Queries
```cypher
// Find all ways venture A creates value for venture B
MATCH (v1:Venture {id: "CON-001"})-[r]-(v2:Venture {id: "FIN-042"})
RETURN type(r), properties(r)
```

### For Observability & Auditing
Every relationship change is logged:
```
Relationship Created: CON-001 -CREATES_REVENUE_SYNERGY-> FIN-042
  timestamp: 2026-07-30T14:32:00Z
  created_by: Hermes Agent
  value_usd_monthly: 1500
  status: active
```
