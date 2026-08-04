# venture.json Schema Unification

## Three Conflicting Systems (Current State)

### System 1: Phase 1 Ontology (Template)
**Used by:** Neo4j routing, agent context loading, capability discovery  
**Schema focus:** Minimal identity + routing  
**Fields:**
```json
{
  "id": "CON-001",
  "name": "Ace Construction",
  "sector": "construction",
  "agent_id": "agent-ceo",
  "skills": ["skill-stripe-payment", "skill-send-email"],
  "created_date": "2026-07-29",
  "ontology_version": "2.1"
}
```

### System 2: Operations/Completion Tracking
**Used by:** venture-completion-ledger.py, build_venture_completion_rank.py, vex-hero-site dashboard  
**Schema focus:** Technical state + completion %  
**Fields:** (CON-001 example)
```json
{
  "venture_id": "CON-001",
  "name": "Ace Construction",
  "sector": "construction",
  "status": "validation",
  "category": "general-contracting",
  "specialties": ["residential-renovation"],
  "completion_percent": 60,
  "has_code": true,
  "has_dashboard": true,
  "has_payments": true,
  "automation_level": 0.25,
  "github_repo": "https://github.com/...",
  "infrastructure": ["nextjs-app", "vercel", "supabase"],
  "priority": "high",
  "next_action": "Wire Stripe checkout..."
}
```

### System 3: Business/Financial
**Used by:** investor relations, funding applications, entity formation  
**Schema focus:** Legal entity + funding + catalog  
**Fields:** (EC-001 example)
```json
{
  "business_id": "EC-001",
  "business_name": "Angels In Daylight",
  "sector": "e-commerce",
  "development_stage": "validation",
  "business_type": "streetwear apparel brand",
  "entity": {
    "name": "Angels In Daylight LLC",
    "type": "LLC",
    "state": "WY",
    "ein": null,
    "status": "pending_formation"
  },
  "catalog": {
    "sku_count": 121,
    "categories": ["Tops", "Bottoms", ...],
    "source_file": "catalog/AID-MASTER-SKU-LIST.csv"
  },
  "icp": {
    "title": "Streetwear/fashion-forward buyer, 18-34",
    "pain_point": "Wants distinctive, limited-drop apparel",
    "platform": "Instagram, TikTok"
  },
  "revenue": {
    "monthly_target": 7000,
    "model": "Direct-to-consumer apparel sales"
  },
  "tax": {
    "classification": "LLC_sole",
    "return_type": "Schedule_C",
    "estimated_annual": 19750
  },
  "grants": [
    {"program": "SBA Microloan", "max": 50000, "status": "identified"}
  ],
  "agents": {
    "primary": "qwen-agent",
    "tech": "claude-code",
    "approval": "human-antwuan"
  }
}
```

---

## The Unified Schema

All three systems consolidated into **one canonical venture.json**.

```json
{
  "# Core Identity (REQUIRED — all systems)",
  "id": "CON-001",
  "_id_comment": "Normalized venture ID: {SECTOR}-{NUMBER} (e.g., CON-001, FIN-042)",
  
  "name": "Ace Construction",
  "_name_comment": "Human-readable venture name",
  
  "sector": "construction",
  "_sector_comment": "Sector slug: construction | finance | real-estate | etc.",
  
  "created_date": "2026-03-15",
  "_created_date_comment": "ISO 8601 date when venture was created",

  "# Routing & Context (Phase 1 Ontology)",
  "agent_id": "agent-ace-ceo",
  "_agent_id_comment": "Primary owning agent (from Neo4j Agent entity)",
  
  "agents": {
    "_comment": "Multi-agent structure for large ventures",
    "primary": "agent-ace-ceo",
    "tech": "claude-code",
    "approval": "human-antwuan",
    "marketing": null
  },
  "_agents_comment": "Additional agents by role (optional, for complex ventures)",
  
  "skills": ["skill-stripe-payment", "skill-jotform-webhook"],
  "_skills_comment": "Skill IDs this venture uses (from skills_index.csv)",
  
  "ontology_version": "2.1",
  "_ontology_version_comment": "DO NOT EDIT — tracks docs/ONTOLOGY.md version",

  "# Operational Status (Completion Tracking)",
  "status": "validation",
  "_status_comment": "planned | validation | mvp | scaling | mature | sunset",
  
  "development_stage": "mvp",
  "_development_stage_comment": "Alternative stage descriptor (maps to status)",
  
  "completion_percent": 60,
  "_completion_percent_comment": "Percent complete (0-100), used by dashboards",
  
  "has_code": true,
  "_has_code_comment": "Does this venture have a live codebase?",
  
  "has_dashboard": true,
  "_has_dashboard_comment": "Does this venture have an admin/founder dashboard?",
  
  "has_payments": true,
  "_has_payments_comment": "Does this venture accept payments (Stripe/PayPal)?",
  
  "automation_level": 0.25,
  "_automation_level_comment": "0-1 scale: how much is automated vs manual",
  
  "priority": "high",
  "_priority_comment": "high | medium | low — for CEO routing",
  
  "next_action": "Wire Stripe checkout, deploy to production, connect ClickUp",
  "_next_action_comment": "Next critical milestone for this venture",

  "# Technical Infrastructure",
  "category": "general-contracting",
  "_category_comment": "Sub-category within sector (e.g., residential-renovation for construction)",
  
  "specialties": ["residential-renovation", "light-commercial-build-outs"],
  "_specialties_comment": "List of specialized services/products this venture offers",
  
  "business_type": "construction services",
  "_business_type_comment": "Business model descriptor",
  
  "revenue_model": "services",
  "_revenue_model_comment": "services | products | subscriptions | marketplace | hybrid",
  
  "business_model": "time-and-materials",
  "_business_model_comment": "Detailed business model (used by TwentyHQ sync)",
  
  "opco": "CON-Holdings",
  "_opco_comment": "Operational holding company (used by TwentyHQ sync)",
  
  "owner_id": "agent-ace-ceo",
  "_owner_id_comment": "Owner/founder ID (used by analytics sync)",
  
  "staff_count": 5,
  "_staff_count_comment": "Number of staff/contractors (used by Supabase sync)",
  
  "github_repo": "https://github.com/Worldwidebro/ace-construction",
  "_github_repo_comment": "Primary GitHub repository URL",
  
  "dashboard_url": "https://vex-hero-site.vercel.app/ventures/con-001",
  "_dashboard_url_comment": "Public-facing venture dashboard URL",
  
  "infrastructure": ["nextjs-app", "vercel", "supabase", "stripe-pending"],
  "_infrastructure_comment": "Tech stack: frameworks, platforms, services used",

  "# Legal & Financial (Entity/Funding)",
  "entity": {
    "_comment": "Legal entity formation status",
    "name": "Ace Construction LLC",
    "type": "LLC",
    "state": "NC",
    "ein": null,
    "status": "active"
  },
  
  "revenue": {
    "_comment": "Financial targets and actuals (used by TwentyHQ, Supabase sync)",
    "monthly_target": 15000,
    "monthly_current": 8500,
    "revenue_ytd": 102000,
    "_revenue_ytd_comment": "Year-to-date revenue (required by load_ventures_unified.py)",
    "costs_mom": 4200,
    "_costs_mom_comment": "Month-over-month costs (required by load_ventures_unified.py)",
    "model": "Time & materials + markup"
  },
  
  "tax": {
    "_comment": "Tax classification for this venture",
    "classification": "LLC_sole",
    "return_type": "Schedule_C",
    "estimated_annual": 180000
  },
  
  "grants": [
    {
      "program": "SBA 7(a) Loan",
      "agency": "SBA",
      "max": 5000000,
      "status": "identified",
      "due_date": "2026-08-01"
    }
  ],
  "_grants_comment": "Available funding programs and status",

  "# Product/Catalog (E-commerce ventures)",
  "catalog": {
    "_comment": "For product-based ventures",
    "sku_count": 0,
    "categories": [],
    "source_file": null
  },

  "# Customer/Market (B2C ventures)",
  "icp": {
    "_comment": "Ideal Customer Profile",
    "title": null,
    "pain_point": null,
    "platform": null
  },

  "# Metadata",
  "last_updated": "2026-07-29T11:30:00Z",
  "_last_updated_comment": "ISO 8601 timestamp of last modification"
}
```

---

## Migration Path (Phase 1B → Unified)

### For existing ventures with Schema 2 (CON-001, RE-001):
1. Read existing `venture.json`
2. Map: `venture_id` → `id`, preserve all operational fields
3. Add: `agent_id`, `skills[]`, `ontology_version` (from ONTOLOGY.md)
4. Add: `agents{}` if not present (optional)
5. Standardize: `created_date` format to ISO 8601

### For existing ventures with Schema 3 (EC-001, FIN-006):
1. Read existing `venture.json`
2. Map: `business_id` → `id`, `business_name` → `name`, preserve all business fields
3. Add: `agent_id`, `skills[]`, `ontology_version`
4. Add: operational fields (`status`, `completion_percent`, `has_code`, etc.) with sensible defaults
5. Merge: `agents{}` (business may already have this)

### For new ventures (use template):
- Copy unified schema template
- Fill in required fields (id, name, sector, agent_id, created_date)
- Leave optional fields blank or null
- Set `ontology_version` to match live ONTOLOGY.md version

---

## Code Changes Required (Read-Side)

Systems that read venture.json must be updated to handle unified schema:

### 1. **moneyprinter_v2_batch_generator.py** (Lines 45, 52, 58, 71, 82)
```python
# Before: venture['venture_id'], venture['venture_name']
# After: venture['id'], venture['name']
```

### 2. **venture_script_engine.py** (Lines 38, 42)
```python
# Before: venture["venture_id"], venture["venture_name"]
# After: venture["id"], venture["name"]
```

### 3. **populate_twenty_ventures.py** (All references)
```python
# Already expects: name, venture_id, sector, stage, status, opco, business_model
# Add fallback: venture.get("id") or venture.get("venture_id") as venture_id
```

### 4. **con-001-agent.py** (Already correct)
```python
# Already queries Neo4j with id field — no changes needed
```

### 5. **load_ventures_unified.py** (Lines 45, 48, 51, 65)
```python
# Already expects: revenue_ytd, costs_mom, staff_count, health_score, status, stage
# Now available in unified schema — no changes needed
```

---

## Dependency Matrix: Files → Fields → Systems

### By Field (What accesses what):

| Field | Files That Read | Read Count | Critical? |
|-------|-----------------|-----------|-----------|
| **id / venture_id / business_id** | moneyprinter_v2, venture_script_engine, stripe_webhook, populate_twenty, con-001-agent, completion_ledger | 13 | 🔴 YES |
| **name / venture_name / business_name** | moneyprinter_v2, venture_script_engine, populate_twenty, load_ventures, test_notion | 8 | 🔴 YES |
| **sector** | moneyprinter_v2, populate_twenty, load_ventures, con-001-agent, vex-hero-site | 7 | 🔴 YES |
| **agent_id** | con-001-agent, Neo4j Router | 2 | 🟡 MEDIUM |
| **status / development_stage** | populate_twenty, load_ventures, completion_ledger, vex-hero-site | 5 | 🟡 MEDIUM |
| **completion_percent** | completion_ledger, vex-hero-site dashboard | 3 | 🟡 MEDIUM |
| **has_code / has_dashboard / has_payments** | completion_ledger, vex-hero-site | 4 | 🟡 MEDIUM |
| **revenue_ytd / revenue.monthly_target** | load_ventures, populate_twenty, Investor Relations | 4 | 🟡 MEDIUM |
| **entity{} / entity_type** | Entity Formation, populate_twenty (opco field) | 2 | 🟢 LOW |
| **skills[]** | Neo4j Router only | 1 | 🟢 LOW |
| **github_repo** | populate_twenty, vex-hero-site | 2 | 🟢 LOW |
| **next_action** | completion_ledger, vex-hero-site | 2 | 🟢 LOW |
| **icp / catalog / grants** | Investor Relations only | 1 | 🟢 LOW |

### By System (What each system needs):

| System | File(s) | Required Fields | Optional Fields | Conflict Risk |
|--------|---------|-----------------|-----------------|---------------|
| **Stripe Webhook Handler** | stripe_webhook_handler.py | id | — | ✅ None (only reads id from metadata) |
| **Moneyprinter Batch Generator** | moneyprinter_v2_batch_generator.py | id, name, sector | — | ✅ None |
| **Venture Script Engine** | venture_script_engine.py | id, name | — | ✅ None |
| **Neo4j Router** | con-001-agent.py | id, agent_id, sector | skills[], ontology_version | ✅ None |
| **Completion Dashboard** | build_venture_completion_ledger.py | id, name, status, completion_percent, has_code, has_dashboard, has_payments | next_action, priority | ✅ None |
| **TwentyHQ Sync** | populate_twenty_ventures.py | name, id, sector, stage, status, opco, business_model, owner_id, revenue_ytd, costs_mom | — | ⚠️ MEDIUM: expects `opco` & `business_model` fields not in current schemas |
| **Supabase Sync** | load_ventures_unified.py | name, status, stage, revenue_ytd, costs_mom, staff_count, health_score | sector, owner_id, business_model | ⚠️ MEDIUM: expects `revenue_ytd`, `costs_mom`, `staff_count`, `health_score` not in current schemas |
| **vex-hero-site** | vex/pages/ventures | id, name, sector, status, dashboard_url | revenue.monthly_target, icp, completion_percent, has_code, has_dashboard | ✅ None (all optional) |
| **Investor Relations** | Various funding scripts | id, name, entity{}, revenue{}, tax{}, grants[] | — | ✅ None |
| **Entity Formation** | LLC creation scripts | id, name, entity{} | tax{} | ✅ None |

### Circular Dependencies & Conflicts:

1. **ID Field Name Inconsistency** 🔴 BLOCKER
   - moneyprinter_v2, venture_script_engine, populate_twenty expect: `venture_id`
   - con-001-agent.py expects: `id` (from Neo4j)
   - EC-001 has: `business_id`
   - **Resolution:** Unify on `id`, add aliases in code that reads venture.json

2. **TwentyHQ Expects `opco` & `business_model`** 🟡 MEDIUM
   - populate_twenty_ventures.py reads `opco` (operational company) and `business_model`
   - Not in any existing schema
   - **Resolution:** Add optional fields to unified schema

3. **Supabase Sync Expects Financial Fields** 🟡 MEDIUM
   - load_ventures_unified.py reads: `revenue_ytd`, `costs_mom`, `staff_count`, `health_score`
   - Not in business schema (EC-001)
   - **Resolution:** Extend revenue{} object to include YTD and monthly cost fields

4. **No Circular Dependencies Found** ✅
   - All systems are read-only from venture.json
   - No system writes back to venture.json (good)
   - Clear one-way dependency flow

---

## Systems That Read venture.json

| System | Required Fields | Optional Fields | Uses For |
|--------|-----------------|-----------------|----------|
| **Neo4j Router** | id, agent_id, sector | skills[], ontology_version | Agent selection, context loading |
| **Stripe Webhook** | id | — | Payment metadata, venture tracking |
| **Completion Dashboard** | id, name, completion_percent, status, has_code, has_dashboard | next_action, priority | Progress tracking, venture status |
| **Investor Relations** | id, entity{}, revenue{}, tax{}, grants[] | — | Funding applications, cap table |
| **vex-hero-site** | id, name, sector, dashboard_url | revenue{}, icp | Marketplace display, filtering |
| **Venture Ledger Scripts** | id, completion_percent, has_code, has_dashboard, has_payments, status | next_action | Aggregation, rankings |
| **Entity Formation** | id, name, entity{} | tax{} | LLC creation, EIN application |
| **TwentyHQ Sync** | id, name, sector, stage, status, opco, business_model, revenue_ytd, costs_mom | owner_id | CRM/ERP integration |
| **Supabase Sync** | id, name, status, revenue_ytd, costs_mom, staff_count, health_score | sector, stage, owner_id | Analytics + dashboards |

---

## Action Items

1. ✅ Create unified schema (above)
2. ⏳ Update venture-template/venture.json to use unified schema
3. ⏳ Create migration script for existing ventures (2 and 3 → unified)
4. ⏳ Apply migration to 6 pilot ventures
5. ⏳ Verify all systems still read correctly
6. ⏳ Bulk deploy with unified schema

---

**Last Updated:** 2026-07-29 (2300 UTC)  
**Approval Status:** Awaiting user confirmation to proceed with unified deployment
