# Trading System Activation Plan

**Goal:** Complete end-to-end trading system activation (FIN-036 Arbitrage Nexus + Trading Predictor) 

**Project:** Civilization OS — Financial Trading Layer  
**Scope:** Entity formation, Crucix pipeline, knowledge graph integration, 127+ wikilinks  
**Timeline:** 15 hours → Go-live 2026-06-18  
**Created:** 2026-06-11

---

## Overview: 4 Parallel Blockers

| Blocker | Effort | Priority | Owner | Status |
|---------|--------|----------|-------|--------|
| **Phase 1: Entity Formation** | 2 hrs | 🔴 CRITICAL | Legal/Admin | `pending` |
| **Phase 2: Crucix Pipeline** | 8 hrs | 🔴 CRITICAL | Backend | `pending` |
| **Phase 3: Knowledge Graph** | 4 hrs | 🟡 HIGH | Data | `pending` |
| **Phase 4: Wikilinks & References** | 3 hrs | 🟡 HIGH | Documentation | `pending` |
| **Phase 5: Testing & Go-live** | 2 hrs | 🟡 HIGH | QA | `pending` |

---

## Phase 1: Entity Formation (2 hours) 🔴 CRITICAL

**Goal:** File FIN-036 Wyoming LLC, enable banking + contracts

**Status:** `pending`

### Tasks

- [ ] 1.1: Prepare Wyoming LLC filing documents
  - [ ] Business name: "Arbitrage Nexus Platform LLC"
  - [ ] Registered agent: Antwuan Johns / Worldwidebro
  - [ ] Address: Charlotte, NC
  - [ ] Operating agreement: Draft governance
  - Effort: 30 min

- [ ] 1.2: File at wyomingsos.gov
  - [ ] Navigate to Articles of Organization form
  - [ ] Submit filing ($100 fee)
  - [ ] Receive approval email
  - Effort: 15 min

- [ ] 1.3: Apply for EIN at IRS.gov
  - [ ] Form SS-4 (online application)
  - [ ] Use newly filed Wyoming LLC info
  - [ ] Receive EIN immediately (online confirmation)
  - Effort: 15 min

- [ ] 1.4: Open business bank account
  - [ ] Choose Mercury or Relay
  - [ ] Link Wyoming LLC EIN
  - [ ] Set up payment processing (Stripe)
  - Effort: 30 min

- [ ] 1.5: Register SAM.gov (federal contracting)
  - [ ] Create SAM.gov account
  - [ ] Complete DUNS registration (1-2 days)
  - [ ] Link to federal contracts system
  - Effort: 15 min

### Completion Criteria
- [ ] Wyoming LLC formed with EIN
- [ ] Business bank account active
- [ ] SAM.gov registration submitted
- [ ] Operating agreement signed

### Notes
- Gates everything else (no bank account = can't accept payments/grants)
- SAM.gov DUNS registration may take 1-2 days
- Parallel work: Can start Phase 2 while waiting for SAM approval

---

## Phase 2: Crucix Pipeline (8 hours) 🔴 CRITICAL

**Goal:** Wire Crucix OSINT feeds → Supabase → deal scoring agents

**Status:** `pending`

### Tasks

- [ ] 2.1: Set up Crucix API integration
  - [ ] Verify Crucix access/credentials
  - [ ] Document API endpoints (27 OSINT feeds)
  - [ ] Test 3 sample queries (AI arbitrage, construction materials, real estate)
  - Effort: 1.5 hours

- [ ] 2.2: Create PostgreSQL schema for deals
  - [ ] Table: `deals` (deal_id, venture_id, source_feed, scoring_date, score)
  - [ ] Table: `deal_scoring_logs` (for audit trail)
  - [ ] Table: `deal_routing` (deal → venture matching)
  - [ ] Add indexes for deal_id, venture_id, scoring_date
  - Effort: 1.5 hours

- [ ] 2.3: Build Crucix → Supabase ingestion pipeline
  - [ ] Python script: `ingest_crucix_deals.py`
  - [ ] Fetch from 27 Crucix feeds every 2 hours
  - [ ] Parse deal metadata (title, amount, sector, urgency)
  - [ ] Store in PostgreSQL deals table
  - [ ] Error handling + logging
  - Effort: 2 hours

- [ ] 2.4: Implement deal scoring agents
  - [ ] Create scoring prompt (use trading-predictor framework)
  - [ ] Score each deal: 1-100 (viability + fit + urgency)
  - [ ] AI agents evaluate: "Does this fit FIN-036 thesis? Route to which ventures?"
  - [ ] Store scores + routing recommendations
  - Effort: 2 hours

- [ ] 2.5: Wire deal routing to CON ventures
  - [ ] Construction materials deals → CON-001 to CON-020
  - [ ] Workforce arbitrage deals → STAFF-001
  - [ ] Real estate deals → RE-001
  - [ ] Create lead intake webhooks per venture
  - Effort: 1 hour

### Completion Criteria
- [ ] Crucix pipeline ingests 100+ deals daily
- [ ] Scoring agents assign confidence scores
- [ ] Deals route to correct ventures via webhooks
- [ ] Audit trail logged in Supabase

### Notes
- Dependencies: Phase 1 (bank account for payment processing)
- Can test against sample Crucix data while Phase 1 completes
- Scoring prompt should reference trading-predictor.md temporal advantage concepts

---

## Phase 3: Knowledge Graph Integration (4 hours) 🟡 HIGH

**Goal:** Wire FIN-036 into [[VENTURE-MASTER]], [[LOOP-FRAMEWORK]], knowledge graph

**Status:** `pending`

### Tasks

- [ ] 3.1: Add FIN-036 to ventures-master.csv
  - [ ] Add row: `FIN-036 | Arbitrage Nexus Platform | financial | growth | fin-036-arbitrage-nexus-platform`
  - [ ] Add metrics: target_mrr=$15K, revenue_stream=arbitrage_fees
  - [ ] Add status: `active` + launch_date=2026-06-18
  - Effort: 30 min

- [ ] 3.2: Add FIN-036 to LOOP-FRAMEWORK
  - [ ] Define venture loop stages: Deal Detection → Scoring → Routing → Commission
  - [ ] Map to [[EXECUTE-WORKFLOW]]: Execute deal routing daily
  - [ ] Add metrics tracking: deals_scored/day, deals_routed/day, commission_revenue/mo
  - Effort: 1 hour

- [ ] 3.3: Create graph entities + relationships
  - [ ] Entity: `FIN-036-Arbitrage-Nexus` (type=venture)
  - [ ] Entity: `Deal-Scoring-Agent` (type=agent, belongs_to=FIN-036)
  - [ ] Entity: `Crucix-Feed` (type=data_source, feeds_to=FIN-036)
  - [ ] Relationships: FIN-036→belongs_to_sector(Financial), FIN-036→executes_via([[LOOP-FRAMEWORK]])
  - [ ] 7 arbitrage verticals as sub-entities
  - Effort: 1.5 hours

- [ ] 3.4: Update Obsidian knowledge graph sync
  - [ ] Run `populate_venture_knowledge_graph.py` (adds FIN-036 + graph entities)
  - [ ] Run `obsidian_graph_sync.py` (exports to .planning/graph-data.json)
  - [ ] Verify 8 Dataview blocks render in KNOWLEDGE-GRAPH-DASHBOARD.md
  - [ ] Check FIN-036 appears with 2,538+ interconnections
  - Effort: 1 hour

### Completion Criteria
- [ ] FIN-036 in ventures-master.csv ✅
- [ ] Loop stages defined + scored by agents ✅
- [ ] Graph entities created (FIN-036, agents, feeds) ✅
- [ ] Obsidian dashboard renders FIN-036 + connections ✅

### Notes
- Depends on: Phase 2 pipeline working (to populate metrics)
- CSV files are source of truth (use populate_venture_knowledge_graph.py, not GitHub)
- Graph relationships enable agent decision-making

---

## Phase 4: Wikilinks & References (3 hours) 🟡 HIGH

**Goal:** Add standardized [[references]] to all 127 trading files

**Status:** `pending`

### Tasks

- [ ] 4.1: Create trading reference hubs
  - [ ] File: `FIN-036-ARBITRAGE-NEXUS-REFERENCE.md`
    - Definition: "Arbitrage Nexus routes deals across 7 verticals"
    - Links to: [[VENTURE-MASTER]], [[LOOP-FRAMEWORK]], [[PLAN-WORKFLOW]]
  - [ ] File: `TRADING-PREDICTOR-REFERENCE.md`
    - Definition: "Agent using temporal advantage for HFT"
    - Links to: [[trading-predictor.md]], [[PLAN-WORKFLOW]]
  - [ ] File: `PORTFOLIO-OPTIMIZATION-REFERENCE.md`
    - Definition: "AI portfolio rebalancing system"
    - Links to: [[FIN-023]], [[LOOP-FRAMEWORK]]
  - Effort: 1 hour

- [ ] 4.2: Add wikilinks to 127 trading files (batch update)
  - [ ] Script: Find all trading files + add reference header
  - Pattern for each file:
    ```yaml
    ---
    references:
      - [[VENTURE-MASTER]]
      - [[LOOP-FRAMEWORK]]
      - [[PLAN-WORKFLOW]]
      - [[FIN-036-ARBITRAGE-NEXUS]]
    ---
    ```
  - Effort: 1 hour (via sed/batch script)

- [ ] 4.3: Wire to ORB interconnections
  - [ ] FIN-036 → [[ORB-MASTER-CONNECTOR-2026-06-11.md]]
  - [ ] Add trading to ORBS-INTERCONNECTION-MAP-2026-06-11.md
  - [ ] Create "Trading ORB Integration" section showing 7 verticals → CON/RE/STAFF ventures
  - Effort: 30 min

- [ ] 4.4: Update REFERENCE-DEDUPLICATION-GUIDE-2026-06-11.md
  - [ ] Add FIN-036 trading reference patterns
  - [ ] Add deal scoring reference format
  - [ ] Example: `[[FIN-036 | Arbitrage Nexus]] → [[Deal-Scoring-Agent]] → [[CON-011 | Electrical]]`
  - Effort: 30 min

### Completion Criteria
- [ ] 3 reference hubs created ✅
- [ ] 127 trading files have [[VENTURE-MASTER]] + orb references ✅
- [ ] ORB interconnection map updated ✅
- [ ] Deduplication guide updated ✅

### Notes
- Non-blocking: Can start while Phases 2-3 complete
- Batch wikilink update will be via sed script
- References enable knowledge graph traversal

---

## Phase 5: Testing & Go-Live (2 hours) 🟡 HIGH

**Goal:** Validate deal flow end-to-end, activate trading system

**Status:** `pending`

### Tasks

- [ ] 5.1: Test Crucix → FIN-036 → CON-011 deal flow
  - [ ] Submit test deal via Crucix API
  - [ ] Verify ingestion into PostgreSQL `deals` table
  - [ ] Verify scoring agent processes it
  - [ ] Verify routing to CON-011 webhook
  - Effort: 30 min

- [ ] 5.2: Verify metrics + reporting
  - [ ] Run: `python3 populate_venture_knowledge_graph.py`
  - [ ] Check: FIN-036 shows metrics in ventures-master.csv
  - [ ] Check: Deal scoring logs appear in Supabase
  - [ ] Check: Commission revenue calculated correctly
  - Effort: 30 min

- [ ] 5.3: Activate trading loop automation
  - [ ] Schedule daily Crucix ingestion (cron job or `/schedule`)
  - [ ] Enable deal scoring agents (start subprocesses)
  - [ ] Wire webhooks to CON ventures
  - Effort: 30 min

- [ ] 5.4: Go-live checklist
  - [ ] FIN-036 LLC operational (entity + bank account)
  - [ ] Crucix pipeline ingesting deals
  - [ ] Deal scoring + routing working
  - [ ] Knowledge graph updated
  - [ ] Wikilinks live in Obsidian
  - [ ] ORB interconnections updated
  - Effort: 30 min

### Completion Criteria
- [ ] 3 test deals routed to CON-011 ✅
- [ ] Metrics dashboard shows FIN-036 revenue ✅
- [ ] Scoring agents processing deals autonomously ✅
- [ ] Trading system live + generating commission revenue ✅

### Notes
- Test against CON-011 (Electrical Services, already in production)
- Can defer full 20-venture routing to Phase 2 (post-launch optimization)

---

## Timeline

| Date | Phase | Blockers | Status |
|------|-------|----------|--------|
| **2026-06-12** | 1 (Entity) | Requires manual admin | `start` |
| **2026-06-12** | 2 (Pipeline) | Parallel with Phase 1 | `start` |
| **2026-06-13** | 3 (Knowledge Graph) | Waits for Phase 2 metrics | `start` |
| **2026-06-14** | 4 (Wikilinks) | Non-blocking, can start day 1 | `start` |
| **2026-06-18** | 5 (Testing) | Gates go-live decision | `start` |
| **2026-06-18** | **GO-LIVE** | All phases complete | `pending` |

---

## Dependencies

```
Phase 1 (Entity)
    ↓ (gates banking)
Phase 2 (Crucix Pipeline) + Phase 4 (Wikilinks) [parallel]
    ↓
Phase 3 (Knowledge Graph)
    ↓
Phase 5 (Testing)
    ↓
🚀 GO-LIVE
```

---

## Success Metrics

✅ **Phase 1:** Wyoming LLC + EIN + bank account active  
✅ **Phase 2:** 100+ deals/day ingested, scored, routed  
✅ **Phase 3:** FIN-036 visible in knowledge graph with 2,538+ interconnections  
✅ **Phase 4:** 127 trading files with [[references]] to [[ORBs]]  
✅ **Phase 5:** End-to-end deal flow validated; trading system generating revenue  

**Target Revenue:** $15K MRR by 2026-06-30 (deals routed to CON ventures earning commissions)
