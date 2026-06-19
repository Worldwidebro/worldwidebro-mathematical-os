# CON OS MVP Build Plan — 7-14 Day Execution

**Start Date:** 2026-06-16  
**Ship Date:** 2026-06-27  
**First Revenue:** $1K/week by Day 14

---

## WEEK 1: Core Services (Days 1-7)

### Day 1: Deal Intake Service ✅
**Goal:** Receive + classify referral submissions  
**Deliverable:** 
- `services/deal_intake/service.py` (Flask/FastAPI)
- Receives: `{contact_id, job_title, budget, urgency, sector}`
- Returns: `{deal_id, estimated_profit, deal_score, status}`

**Test:** 
```bash
curl -X POST http://localhost:8001/submit_referral \
  -d '{"contact_id": "ref_123", "job_title": "Roof repair", "budget": 5000, "urgency": "high"}'
# Returns: {"deal_id": "deal_001", "estimated_profit": 1200, "score": 8.5, "status": "pending_contract"}
```

**Success:** Service receives 5 test deals, classifies correctly

---

### Day 2: Contract Generator Service ✅
**Goal:** Auto-generate 4 contract types from deal  
**Deliverable:**
- `services/contract_generator/service.py`
- Receives: `{deal_id, contractor_ids, split_model}`
- Generates: 4 contracts (client, contractor, referral, platform)
- Integrates: Documenso API for PDF generation

**Contracts:**
1. **Client Contract** — Scope + timeline + price
2. **Contractor Agreement** — Labor + materials rates
3. **Referral Agreement** — Referrer commission + terms
4. **Platform Terms** — Fee structure + dispute resolution

**Test:**
```bash
curl -X POST http://localhost:8002/generate_contracts \
  -d '{"deal_id": "deal_001"}'
# Returns: {"contracts": [4 PDF URLs], "status": "ready_for_signing"}
```

**Success:** Generate 3 test deal contracts, all PDFs valid

---

### Day 3: Payout Engine ✅
**Goal:** Calculate splits + route payments  
**Deliverable:**
- `services/payout_engine/service.py`
- Receives: `{deal_id, total_payment, invoice_date}`
- Calculates: All 5 splits (labor 40%, subs 20%, referral 10%, platform 12%, reserve 8%)
- Routes: Payment to 5 destinations

**Splits Model (Example: $85K job):**
```
Total: $85,000
├── Labor/Materials: $34,000 (40%)
├── Subcontractors: $17,000 (20%)
├── Referral Fee: $8,500 (10%)
├── Platform Fee: $10,200 (12%)
└── Reserve: $6,800 (8%)
```

**Test:**
```bash
curl -X POST http://localhost:8003/trigger_payment_distribution \
  -d '{"deal_id": "deal_001", "total_payment": 85000}'
# Returns: {"splits": [5 payment records], "status": "routing"} 
```

**Success:** Split $85K correctly across 5 parties, payments route

---

### Day 4: Orchestrator Service ✅
**Goal:** Route deals to correct agents  
**Deliverable:**
- `services/orchestrator/service.py`
- Receives: `{deal_id, event_type}`
- Routes to agents: COO (management), Ops (execution), Finance (payment), Legal (contracts)
- Tracks: Agent decisions + decision log

**Event Types:**
- `deal_submitted` → COO (decision on acceptance)
- `job_started` → Ops (execution oversight)
- `job_completed` → Finance (payment trigger)
- `dispute` → Legal (resolution)

**Test:**
```bash
curl -X POST http://localhost:8004/route_deal \
  -d '{"deal_id": "deal_001", "event": "deal_submitted"}'
# Returns: {"agent_assigned": "coo_agent_1", "task_id": "task_001"}
```

**Success:** Route 5 test deals to correct agents, tasks created

---

### Day 5: Graph Memory Service ✅
**Goal:** Learn from deals + update reputation  
**Deliverable:**
- `services/graph_memory/service.py`
- Receives: `{deal_id, completion_data, metrics}`
- Updates: Contractor reputation, deal patterns, referrer scoring
- Stores: Neo4j + ChromaDB

**Learning Model:**
- Contractor reputation = f(quality_score, speed, compliance, efficiency, communication)
- Referrer score = f(deal_quality, conversion_rate, network_value)
- Deal patterns = Vector embeddings for similarity matching

**Test:**
```bash
curl -X POST http://localhost:8005/update_graph_memory \
  -d '{"deal_id": "deal_001", "contractor_score": 91.4, "referrer_id": "ref_123"}'
# Returns: {"entities_updated": 3, "relationships_created": 2}
```

**Success:** Update 5 deals to graph, reputation scores calculated

---

### Day 6: Integration Testing ✅
**Goal:** Test full flow end-to-end  
**Deliverable:**
- `scripts/test_deal_flow.py`
- Runs complete flow: intake → contract → payout → graph
- Tests: 10 deal scenarios (different sizes, urgencies, contractors)
- Validates: All 5 services communicate correctly

**Test Scenarios:**
1. $5K small repair (1 contractor)
2. $85K major project (3 contractors, referral bonus)
3. $250K complex job (government contract, compliance heavy)
4. Payment split accuracy
5. Graph reputation updates

**Success:** 10/10 test deals complete end-to-end

---

### Day 7: First $1K Deal ✅
**Goal:** Run real deal through system  
**Deliverable:**
- Live deal (contact + job + payment flow)
- All 5 services process it
- Contracts signed
- Payment distributed
- Reputation updated

**Success:** $1K deal shipped end-to-end with no manual steps

---

## WEEK 2: Integration + Scale (Days 8-14)

### Day 8: Dashboard MVP
**Goal:** Real-time deal pipeline visibility  
**Deliverable:**
- Vercel-deployed dashboard
- Shows: Deal pipeline (5 stages), contractor panel, cashflow

**Stages:**
1. Intake (new deals)
2. Contract (awaiting signature)
3. Active (work in progress)
4. Complete (invoiced)
5. Paid (closed)

---

### Day 9: Lead Generation Wiring
**Goal:** Auto-trigger deal intake from real sources  
**Deliverable:**
- Connect: Job boards, marketplace APIs, manual submissions
- Auto-classify: Incoming leads
- Deduplicate: Same job from multiple referrers

---

### Day 10: Payment Distribution Automation
**Goal:** Automatic payment routing (no manual intervention)  
**Deliverable:**
- Stripe integration
- Automated splits
- Notifications to each party

---

### Day 11: Reputation Scoring UI
**Goal:** Contractor reputation dashboard  
**Deliverable:**
- Show contractor scores (S/A/B/C/D tier)
- Past deals + metrics
- Auto-assign high-tier contractors

---

### Day 12: Stress Testing ($5K Deal Flow)
**Goal:** Verify system handles scale  
**Deliverable:**
- Run 50+ deals through system
- Measure: Response times, error rates, accuracy
- Load test: 100 concurrent submissions

---

### Day 13: Documentation + Deployment
**Goal:** Fully documented, deployable system  
**Deliverable:**
- API docs (Swagger)
- Architecture diagram
- Deployment guide
- Runbook (how to operate)

---

### Day 14: Ship + Announce
**Goal:** Public launch  
**Deliverable:**
- Deploy to production
- Announce to referral network
- Accept first $5K-$10K deals
- Live contractor matching

---

## Revenue Milestones

| Week | Target | Deals | Revenue |
|------|--------|-------|---------|
| Week 1 | MVP shipped | 1 | $1K |
| Week 2 | Scale tested | 10-15 | $10K-$15K |
| Week 3 | Live operations | 20+ | $20K+ |
| Week 4 | $1K/week run rate | 50+ | $50K+ |

---

## Daily Standup Template

```
Day X: [Service Name]
✅ Completed:
- [Task 1]
- [Task 2]

🔧 Blocked:
- [If any]

📊 Metrics:
- [Tests passed: X/Y]
- [Response time: Xms]
```

---

## How to Stay on Track

- **Each day = 1 service + tests**
- **End of day = deployable, tested code**
- **Week 1 = all 5 services working**
- **Week 2 = scale + monetization**
- **Day 14 = public revenue-generating system**

**If behind:** Cut scope (e.g., skip Day 13 docs, deploy Day 12)  
**If ahead:** Add enhancements (scoring UI, advanced routing)
