# CON OS — Construction Deal Execution System

**Status:** MVP Build in Progress  
**Target Ship Date:** 2026-06-27 (14 days)  
**First Revenue Milestone:** $1K/week by Week 2

---

## What This Is

A **deal-to-payout system** that converts construction leads → contracts → executed work → automated splits → reputation graph.

```
Lead → Classify → Contract → Assign → Execute → Pay → Learn
```

---

## Folder Structure

```
CON-OS-BUILD/
├── services/                    # Core MCP microservices
│   ├── deal_intake/            # Lead classification + intake
│   ├── contract_generator/     # Auto-generate agreements
│   ├── payout_engine/          # Split calculation + distribution
│   ├── orchestrator/           # Agent routing (COO/Ops/Finance/Legal)
│   └── graph_memory/           # Reputation + deal learning
├── config/                      # Configuration + schemas
│   ├── deal_schema.json        # Deal structure
│   ├── contract_templates/     # Agreement templates
│   └── split_model.json        # Revenue split rules
├── docs/                        # Documentation
│   ├── ARCHITECTURE.md
│   ├── MVP-PLAN.md
│   └── MCP-ENDPOINTS.md
├── tests/                       # Test suites
├── scripts/                     # Deployment + automation
└── [SERVICE_NAME]/
    ├── service.py              # Service code
    ├── routes.py               # MCP endpoints
    └── tests/
```

---

## Services (What Gets Built)

### 1. Deal Intake Service
**Receives:** Referral submission (contact, job, budget, urgency)  
**Does:** Classifies deal, estimates profit, assigns score  
**Outputs:** Deal record + contract trigger

### 2. Contract Generator Service
**Receives:** Classified deal + contractor list  
**Does:** Auto-generates 4 contract types (client, contractor, referral, platform)  
**Outputs:** Signed contract PDFs + split model metadata

### 3. Payout Engine
**Receives:** Completed job + invoice  
**Does:** Splits payment per model (40% labor, 20% subs, 10% referral, 12% platform, 8% reserve)  
**Outputs:** Payment routing + ledger entries

### 4. Orchestrator
**Receives:** Deal event (submission, completion, payment)  
**Does:** Routes to correct agent (COO, Field Ops, Finance, Legal)  
**Outputs:** Agent task + decision log

### 5. Graph Memory
**Receives:** Deal completion + metrics  
**Does:** Updates contractor reputation, deal metrics, referrer scoring  
**Outputs:** Neo4j/ChromaDB updated entities + similarity search results

---

## Build Timeline (7-14 Days)

**Week 1 (Days 1-7):**
- [ ] Day 1: Deal intake service (receives + classifies)
- [ ] Day 2: Contract generator (auto-builds 4 types)
- [ ] Day 3: Payout engine (splits + routing)
- [ ] Day 4: Orchestrator (agent dispatch)
- [ ] Day 5: Graph memory (learning layer)
- [ ] Day 6: Integration testing
- [ ] Day 7: First $1K deal end-to-end

**Week 2 (Days 8-14):**
- [ ] Day 8: Dashboard MVP (deal pipeline)
- [ ] Day 9: Lead generation wiring
- [ ] Day 10: Payment distribution automation
- [ ] Day 11: Reputation scoring UI
- [ ] Day 12: Stress testing ($5K deal flow)
- [ ] Day 13: Documentation + deployment
- [ ] Day 14: Ship + announce

---

## MCP Endpoints (5 Core Tools)

See `docs/MCP-ENDPOINTS.md` for full schema.

1. `/submit_referral` — Intake deal
2. `/get_contractor_score` — Lookup reputation
3. `/trigger_payment_distribution` — Distribute payment
4. `/update_graph_memory` — Learn from deals
5. `/get_deal_forecast` — Predict next deals

---

## Configuration Files

**deal_schema.json** — Defines deal structure (title, budget, urgency, sector)  
**split_model.json** — Defines payment split percentages  
**contract_templates/** — Documenso templates for all 4 contract types  

---

## Success Criteria

- ✅ Intake service receives + classifies 10 test deals
- ✅ Contract generator produces legal agreements
- ✅ Payout engine routes $1K correctly (all splits calculated)
- ✅ Orchestrator assigns agents per deal type
- ✅ Graph memory learns contractor reputation
- ✅ First real deal ships end-to-end
- ✅ Dashboard shows live deal pipeline

---

## Getting Started

```bash
# 1. Clone this repo
git clone [repo]
cd CON-OS-BUILD

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run services locally
python services/deal_intake/service.py
python services/contract_generator/service.py
python services/payout_engine/service.py
python services/orchestrator/service.py
python services/graph_memory/service.py

# 4. Test endpoints
python scripts/test_deal_flow.py

# 5. Deploy to Vercel
vercel deploy
```

---

## Next: See `docs/MVP-PLAN.md` for day-by-day breakdown

