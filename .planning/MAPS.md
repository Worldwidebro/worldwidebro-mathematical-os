# WORLDWIDEBRO HOLDINGS - ENTITY RELATIONSHIP MAPS

**Last Updated:** 2026-07-21
**Version:** 1.0

---

## 1. GLOBAL ID MAPPING (URN System)

Every entity is resolvable via URN. This is the "DNS" of the entire operation.

| Entity Type | URN Pattern | Example |
|-------------|-------------|---------|
| **OPCO** | `urn:ww:opco:{id}` | `urn:ww:opco:OPCO-004` |
| **Venture** | `urn:ww:venture:{id}` | `urn:ww:venture:RE-001` |
| **Repository** | `urn:ww:repo:{id}` | `urn:ww:repo:lt-005-medical-courier` |
| **Agent** | `urn:ww:agent:{type}:{id}` | `urn:ww:agent:finance:invoice-bot-01` |
| **Task** | `urn:ww:task:{uuid}` | `urn:ww:task:550e8400-e29b-41d4-a716-446655440000` |
| **Event** | `urn:ww:event:{type}:{id}` | `urn:ww:event:invoice:INV-2026-001` |

---

## 2. VENTURE ↔ OPCO MAPPING (712 Ventures → 18 OPCOs)

**Current State:**
- 712 ventures distributed across 18 OPCOs
- Tier-based rollout (Tier 1: Jul 22, Tier 2: Jul 23, Tier 3: Jul 24-28)
- Critical path: RE-001 @ 90% ready ($49.7K MRR target)

| OPCO ID | Sector | Status | Ventures | Example |
|---------|--------|--------|----------|---------|
| OPCO-001 | Commerce | 25% ready | 100+ | ec-001-angels-in-daylight |
| OPCO-002 | Beauty & Wellness | 20% ready | 40+ | bw-001-lash-extension-studio |
| OPCO-003 | Finance | 30% ready | 60+ | fin-001-genixbank-lite |
| OPCO-004 | Construction & Real Estate | 90% ready | 30+ | con-001-ace-construction, RE-001 |
| OPCO-005 | Education | 15% ready | 40+ | edu-001-youth-entrepreneurship |
| OPCO-006-018 | Other Sectors | 15% avg | 350+ | TECH-040, OPS-001, EC-111 (live) |

---

## 3. REPOSITORY ↔ VENTURE MAPPING (1,661 Repos → 712 Ventures)

**Live Status:**
- 1,661 repos indexed
- 1,046 repos with capabilities
- 414 repos linked to ventures
- 60% code reuse potential (shared-venture-lib extract)

**Capability Backfill:** 71% coverage via `repo-capabilities-backfill.json`

---

## 4. AGENT ↔ CAPABILITY MAPPING (150+ Agents)

| Capability | Agent | OPCO Scope | Status |
|------------|-------|-----------|--------|
| Legal Document Analysis | legal-discovery-bot | All | ✅ Active |
| Financial Invoice Generation | finance-invoicing-bot | OPCO-003 | ✅ Active |
| Candidate Matching | hr-matcher-bot | OPCO-004 | ✅ Active |
| Market Research | research-scraper-bot | All | ✅ Active |
| Code Generation (Python) | dev-coder-bot | All | ✅ Active |
| Sales Automation | sales-automation-bot | All | ✅ Active |
| Payment Processing | payment-processor-bot | OPCO-003, OPCO-001 | ✅ Active |

**Agent Routing:**
- Least-busy agent picked from capability pool
- Redis tracks agent utilization (key: `agent:{id}:busy_count`)
- Fallback to generic bot if specialized agent at capacity

---

## 5. EVENT FLOW MAPPING (Kafka Event Bus)

**8 Core Topics (Real-Time):**

| Topic | Producer | Consumer | Example Event |
|-------|----------|----------|----------------|
| `tasks.started` | Orchestrator | Langfuse, Prometheus | `{"task_id": "t123", "agent": "finance-01", "timestamp": "2026-07-21T10:00:01Z"}` |
| `tasks.completed` | Agent Workers | UI Dashboard, Prometheus | `{"task_id": "t123", "status": "success", "duration_ms": 4500}` |
| `ventures.classified` | RIE Scanner | Neo4j Writer, **vex News Feed** | `{"venture_id": "RE-001", "stage": "Growth", "revenue": 7455000}` |
| `invoices.generated` | Finance Bot | Stripe API, Audit Log | `{"invoice_id": "INV-2026-001", "amount": 7455000}` |
| `approvals.required` | Compliance Bot | Slack, Dashboard | `{"approval_type": "VENTURE_LAUNCH", "venture": "CON-012"}` |
| `risk.flagged` | Analysis Bot | Alerts, CEO Dashboard | `{"risk_type": "CAC_TOO_HIGH", "venture": "FIN-012"}` |
| `revenue.captured` | Payment Gateway | Dashboard, Neo4j | `{"venture": "CON-001", "amount": 8200}` |
| `errors.critical` | Any System | PagerDuty, Ops | `{"error": "Neo4j timeout", "severity": "CRITICAL"}` |

---

## 6. SECTOR-READINESS TRACKER ↔ VEX MARKETPLACE

**Flow:** Sector Operations (internal) → Supabase `vex_published` → vex Dashboard (external)

- **Sector Readiness:** Operational command center (28% → 100% by 2026-08-04)
- **Vex Marketplace:** Public venture directory (displays live ventures only)
- **Sync Point:** Supabase `ventures` table with `vex_published` boolean
- **News Feed:** Real-time event stream from Kafka → vex

---

## 7. TASK ↔ WORKFLOW MAPPING (n8n Automation)

| Trigger Event | n8n Workflow | Description | Status |
|---------------|--------------|-------------|--------|
| `github:commit` | `workflow-rie-scan` | RIE scanner triggered | ✅ Live |
| `manual:approve_venture` | `workflow-venture-approval` | 7-file Path A | ✅ Ready |
| `schedule:monthly_close` | `workflow-finance-close` | P&L per OPCO | ✅ Scheduled |
| `vex:bid_won` | `workflow-construction-allocate` | Material allocation | ✅ Ready |
| `invoicing` | `workflow-invoice-payment` | Invoice → Stripe | ✅ Live |

---

## 8. REMAINING CHECKLIST (Wave-by-Wave)

### WAVE 0: DISK RECOVERY (Blocking)
- ✅ Partial cleanup done (10GB freed)
- ⏳ **TODO:** Complete cleanup to 30GB+ free
- ⏳ **TODO:** Verify Docker stack can start safely

### WAVE 1: REPOSITORY INTELLIGENCE (Parallel to Waves 2-4)
- ⏳ CrewAI pilot on 5 sample repos
- ⏳ Portfolio Runner on all 1,661 repos
- ⏳ Consolidation roadmap (380+ duplication targets)

### WAVE 2: CODE CONSOLIDATION (Parallel)
- ⏳ Extract 6 modules into `shared-venture-lib/`
- ⏳ Verify CON-001 imports from shared lib
- ⏳ Build `venture-template-scaffold.sh`

### WAVE 3: TOPOLOGY DOCUMENTATION (Parallel)
- ✅ TOPOLOGY.md created (v1.0 now v2.0 operational)
- ✅ MAPS.md created (this document)
- ⏳ SERVICE_TOPOLOGY.md (Docker services map)
- ⏳ DATA_FLOW_MAP.md (Supabase→Neo4j→Qdrant→Ollama)
- ⏳ AGENT_COMMUNICATION_MAP.md (Hermes + 232 agents)
- ⏳ SECURITY_ACCESS_MAP.md (Approval thresholds + audit)

### WAVE 4: NEO4J SCHEMA + MCP (Parallel)
- ⏳ Extend Neo4j: 9 new entity types, 8 relationships
- ⏳ Seed with real data (2 Hardware, 1 Storage, live services)
- ⏳ Write 3-4 example Cypher queries (CEO, CTO, Finance views)
- ⏳ MCP Ollama config wiring + verification

### WAVE 5: VEX VERIFICATION (Depends on 2-4)
- ⏳ Rebuild vex-hero-site (`npm install && npm run build`)
- ⏳ Verify all 16 sector pages render
- ⏳ Test Neo4j queries live
- ⏳ Integration test report

---

## 9. VEX NEWS FEED (CRITICAL)

**Purpose:** Real-time visibility into what's being completed across 712 ventures + 1,661 repos + 150 bots.

**Source:** Kafka event bus → vex React dashboard

**What shows up:**
```
[Today 10:23 AM] 🎯 Venture Launched: RE-001 Harbor View (OPCO-004)
[Today 10:22 AM] 💰 Revenue Captured: CON-001 +$8.2K (MTD: $14.5K)
[Today 10:20 AM] ✅ Invoice Generated: INV-2026-001 $7.455K (FIN-001)
[Today 10:15 AM] ⚠️ Risk Flagged: FIN-012 CAC Too High (HIGH severity)
[Today 10:10 AM] 🤖 Approval Required: CON-012 Launch (waiting CEO sign-off)
[Today 10:05 AM] 📊 Classified: EC-111 MVP → Growth Stage
[Today 10:00 AM] 🔴 Critical Error: Neo4j connection timeout (auto-recovery)
```

**Architecture:** WebSocket → vex React component ← Kafka consumer

---

**Last Verified:** 2026-07-21  
**Next Audit:** 2026-07-28
