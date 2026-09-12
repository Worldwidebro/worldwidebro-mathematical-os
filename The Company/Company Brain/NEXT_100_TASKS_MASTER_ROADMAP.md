[[STARTHERE]] | [[REALITY]] | [[50-MASTER-CONTROL|Master Roadmap]] | [[INDEX]]

# Next 100+ Tasks — Company Brain Master Roadmap

**Authority:** CP-027 (Infrastructure) + CP-006 (Agents) + CP-028 (Collaboration)  
**Timeline:** Sep 6 - Dec 31, 2026 (16 weeks)  
**Total Tasks:** 127 structured across 10 phases  
**Last Updated:** 2026-09-08

---

## 🚀 PRIORITY TIERS

- 🔴 **CRITICAL PATH** (blocks everything)
- 🟠 **HIGH** (start within 2 weeks)
- 🟡 **MEDIUM** (start within 4 weeks)
- 🟢 **LOW** (start after core systems)

---

---

## PHASE 1: KNOWLEDGE GRAPH AGENT ENABLEMENT (Week 1-2) — 15 Tasks

**Goal:** Enable agents to query Company Brain intelligently  
**Authority:** CP-027 (Infrastructure) + CP-008 (Graph Architecture)

### 1.1 Hybrid Search (KG-017) — 🔴 CRITICAL PATH

| ID | Task | Owner | Effort | Blocking | Status |
|---|------|-------|--------|----------|--------|
| **1.1.1** | Complete `_PIPELINES/retrieval/hybrid_query.py` | Engineer | 4h | 1.1.2 | 🟡 Ready |
| **1.1.2** | Create `cypher_patterns.yaml` (graph queries) | Architect | 2h | 1.1.3 | 🟡 Ready |
| **1.1.3** | Implement `fusion_algorithm.py` (result ranking) | Engineer | 3h | 1.1.4 | 🟡 Ready |
| **1.1.4** | Test hybrid queries against Neo4j + Qdrant | QA | 2h | 1.1.5 | ⏳ Blocked |
| **1.1.5** | Performance optimization (target <500ms) | Engineer | 2h | None | ⏳ Blocked |

### 1.2 Agent Context Assembly (KG-028) — 🔴 CRITICAL PATH

| ID | Task | Owner | Effort | Blocking | Status |
|---|------|-------|--------|----------|--------|
| **1.2.1** | Design agent profiles (`agent_profiles.yaml`) | Architect | 2h | 1.2.2 | 🟡 Ready |
| **1.2.2** | Build `agent_context_builder.py` | Engineer | 4h | 1.2.3 | ⏳ Blocked on 1.2.1 |
| **1.2.3** | Implement distance policies (1/2/3-hop) | Engineer | 2h | 1.2.4 | ⏳ Blocked on 1.2.2 |
| **1.2.4** | Test context building (staffing, medical, RE ventures) | QA | 2h | 1.2.5 | ⏳ Blocked on 1.2.3 |
| **1.2.5** | Confidence scoring for context relevance | Engineer | 2h | None | ⏳ Blocked on 1.2.4 |

### 1.3 Graph API Endpoint (KG-048) — 🔴 CRITICAL PATH

| ID | Task | Owner | Effort | Blocking | Status |
|---|------|-------|--------|----------|--------|
| **1.3.1** | Create FastAPI server (`60-APIS/graph_api.py`) | Engineer | 3h | 1.3.2 | 🟡 Ready |
| **1.3.2** | Wire endpoints to KG-017 + KG-028 | Engineer | 2h | 1.3.3 | ⏳ Blocked on 1.3.1 |
| **1.3.3** | Add authentication layer (API keys) | Security | 1h | 1.3.4 | ⏳ Blocked on 1.3.2 |
| **1.3.4** | Deploy locally + test E2E | DevOps | 2h | 1.3.5 | ⏳ Blocked on 1.3.3 |
| **1.3.5** | Document API (Swagger/OpenAPI) | Tech Writer | 1h | None | ⏳ Blocked on 1.3.4 |

---

## PHASE 2: REPOSITORY INTELLIGENCE (Week 1-4) — 32 Tasks

**Goal:** Ingest, normalize, classify, and map 904 external repos to Company Brain  
**Authority:** CP-027 + AGT-013/014/015

### 2.1 Inventory & Ingestion — 🔴 CRITICAL PATH (4 tasks)

| ID | Task | Agent | Effort | Blocking | Status |
|---|------|-------|--------|----------|--------|
| **2.1.1** | Create GitHub API script (fetch 904 starred repos) | AGT-003 | 30m | 2.1.2 | ⏳ Ready |
| **2.1.2** | Ingest repos into `/Volumes/LaCie/repositories/raw/` | repo-ingestion-agent | 90m | 2.1.3 | ⏳ Blocked on 2.1.1 |
| **2.1.3** | Verify ingestion completeness (904 repos) | AGT-003 | 15m | 2.1.4 | ⏳ Blocked on 2.1.2 |
| **2.1.4** | Document ingestion metadata (timestamp, version) | Tech Writer | 15m | None | ⏳ Blocked on 2.1.3 |

### 2.2 Normalization & Deduplication — 🟠 HIGH (5 tasks)

| ID | Task | Agent | Effort | Blocking | Status |
|---|------|-------|--------|----------|--------|
| **2.2.1** | Detect duplicate entries (same GitHub URL) | repo-normalizer-agent | 10m | 2.2.2 | ⏳ Blocked on 2.1.4 |
| **2.2.2** | Check for archived/deleted repos, 404s | repo-normalizer-agent | 10m | 2.2.3 | ⏳ Blocked on 2.2.1 |
| **2.2.3** | Follow GitHub redirects (renamed repos) | repo-normalizer-agent | 5m | 2.2.4 | ⏳ Blocked on 2.2.2 |
| **2.2.4** | Remove forks, stubs, spam | repo-normalizer-agent | 5m | 2.2.5 | ⏳ Blocked on 2.2.3 |
| **2.2.5** | Output deduplicated set (880-900 repos) | repo-normalizer-agent | 5m | None | ⏳ Blocked on 2.2.4 |

### 2.3 Enrichment — 🟠 HIGH (6 tasks)

| ID | Task | Agent | Effort | Blocking | Status |
|---|------|-------|--------|----------|--------|
| **2.3.1** | Collect GitHub metadata (stars, forks, issues) | repo-enricher-agent | 2h | 2.3.2 | ⏳ Blocked on 2.2.5 |
| **2.3.2** | Extract README content (first 2000 chars) | repo-enricher-agent | 1h | 2.3.3 | ⏳ Blocked on 2.3.1 |
| **2.3.3** | Parse dependency manifests (package.json, Cargo.toml) | repo-enricher-agent | 1h | 2.3.4 | ⏳ Blocked on 2.3.2 |
| **2.3.4** | Classify architecture (monolith/microservices/lib/tool) | repo-enricher-agent | 30m | 2.3.5 | ⏳ Blocked on 2.3.3 |
| **2.3.5** | Detect test/CI/security scanning | repo-enricher-agent | 30m | 2.3.6 | ⏳ Blocked on 2.3.4 |
| **2.3.6** | Store enriched metadata (one JSON per repo) | repo-enricher-agent | 30m | None | ⏳ Blocked on 2.3.5 |

### 2.4 Classification — 🟠 HIGH (7 tasks)

| ID | Task | Layer | Agent | Effort | Blocking | Status |
|---|------|-------|-------|--------|----------|--------|
| **2.4.1** | Setup Classification Agent (repo-classifier) | L2 | AGT-003 | 1h | 2.4.2 | ⏳ Blocked on 2.3.6 |
| **2.4.2** | Classify repos into ontology (8h agent time) | L2 | AGT-013 | 8h | 2.4.3 | ⏳ Blocked on 2.4.1 |
| **2.4.3** | Detect secondary capabilities | L2 | AGT-013 | 2h | 2.4.4 | ⏳ Blocked on 2.4.2 |
| **2.4.4** | Map industry + venture applicability | L2 | AGT-013 | 1h | 2.4.5 | ⏳ Blocked on 2.4.3 |
| **2.4.5** | Output classifications by category | L2 | AGT-013 | 30m | 2.4.6 | ⏳ Blocked on 2.4.4 |
| **2.4.6** | Human review (edge cases via repo-advisor) | L1 | repo-advisor | 1h | 2.4.7 | ⏳ Blocked on 2.4.5 |
| **2.4.7** | Update classifications based on review | L2 | AGT-013 | 30m | None | ⏳ Blocked on 2.4.6 |

### 2.5 Scoring & Disposition — 🟠 HIGH (5 tasks)

| ID | Task | Agent | Effort | Blocking | Status |
|---|------|-------|--------|----------|--------|
| **2.5.1** | Score repos on 10 dimensions (code quality, docs, activity) | AGT-014 | 6h | 2.5.2 | ⏳ Blocked on 2.4.7 |
| **2.5.2** | Assign disposition (ADOPT/INTEGRATE/FORK/REFERENCE/MONITOR) | AGT-015 | 3h | 2.5.3 | ⏳ Blocked on 2.5.1 |
| **2.5.3** | Flag security/license risks | AGT-014 | 2h | 2.5.4 | ⏳ Blocked on 2.5.2 |
| **2.5.4** | Create adoption roadmap (top 20 ADOPT candidates) | repo-advisor | 2h | 2.5.5 | ⏳ Blocked on 2.5.3 |
| **2.5.5** | Output final registry (880-900 repos scored) | AGT-003 | 30m | None | ⏳ Blocked on 2.5.4 |

### 2.6 Graph Integration — 🟡 MEDIUM (5 tasks)

| ID | Task | Owner | Effort | Blocking | Status |
|---|------|-------|--------|----------|--------|
| **2.6.1** | Merge repo classifications into Neo4j | Engineer | 2h | 2.6.2 | ⏳ Blocked on 2.5.5 |
| **2.6.2** | Create REPO→VENTURE relationships | Engineer | 1h | 2.6.3 | ⏳ Blocked on 2.6.1 |
| **2.6.3** | Create REPO→CAPABILITY relationships | Engineer | 1h | 2.6.4 | ⏳ Blocked on 2.6.2 |
| **2.6.4** | Index repositories in Qdrant (embeddings) | Engineer | 1h | 2.6.5 | ⏳ Blocked on 2.6.3 |
| **2.6.5** | Verify graph connectivity (sample queries) | QA | 30m | None | ⏳ Blocked on 2.6.4 |

---

## PHASE 3: DEALFLOW OS ENHANCEMENTS (Week 2-3) — 18 Tasks

**Goal:** Connect DealFlowOS to live Cake Equity + multi-venture deal tracking  
**Authority:** CP-027 (Infrastructure) + DealFlow team

### 3.1 Cap Table Integration — 🟠 HIGH (6 tasks)

| ID | Task | Owner | Effort | Blocking | Status |
|---|------|-------|--------|----------|--------|
| **3.1.1** | Load real CAP-TABLE.json data per venture | Engineer | 2h | 3.1.2 | ⏳ Blocked on Phase 1 API |
| **3.1.2** | Build equity calculator (dilution modeling) | Engineer | 2h | 3.1.3 | ⏳ Blocked on 3.1.1 |
| **3.1.3** | Create multi-venture equity dashboard | Frontend | 1h | 3.1.4 | ⏳ Blocked on 3.1.2 |
| **3.1.4** | Cake Equity API integration (OAuth + sync) | Engineer | 3h | 3.1.5 | ⏳ Blocked on 3.1.3 |
| **3.1.5** | Sync Cake Equity data → DealFlowOS (bi-directional) | Engineer | 2h | 3.1.6 | ⏳ Blocked on 3.1.4 |
| **3.1.6** | Test cap table updates + vesting schedules | QA | 1h | None | ⏳ Blocked on 3.1.5 |

### 3.2 Deal Room File Management — 🟠 HIGH (4 tasks)

| ID | Task | Owner | Effort | Blocking | Status |
|---|------|-------|--------|----------|--------|
| **3.2.1** | Add file upload to Deal Room (PDFs, docs) | Frontend | 2h | 3.2.2 | ⏳ Ready |
| **3.2.2** | Create file versioning + history | Backend | 2h | 3.2.3 | ⏳ Blocked on 3.2.1 |
| **3.2.3** | Add document OCR + full-text search | Backend | 2h | 3.2.4 | ⏳ Blocked on 3.2.2 |
| **3.2.4** | Wire file storage to PostgreSQL + S3 | DevOps | 1h | None | ⏳ Blocked on 3.2.3 |

### 3.3 Deal Notifications — 🟡 MEDIUM (3 tasks)

| ID | Task | Owner | Effort | Blocking | Status |
|---|------|-------|--------|----------|--------|
| **3.3.1** | Implement real-time WebSocket for deal updates | Backend | 2h | 3.3.2 | ⏳ Ready |
| **3.3.2** | Create notification templates (stage changes, alerts) | Backend | 1h | 3.3.3 | ⏳ Blocked on 3.3.1 |
| **3.3.3** | Wire notifications to Slack + email | Backend | 1h | None | ⏳ Blocked on 3.3.2 |

### 3.4 Multi-Venture Reporting — 🟡 MEDIUM (5 tasks)

| ID | Task | Owner | Effort | Blocking | Status |
|---|------|-------|--------|----------|--------|
| **3.4.1** | Create portfolio view (all 5 focus ventures) | Frontend | 1h | 3.4.2 | ⏳ Ready |
| **3.4.2** | Build consolidated funnel chart (cross-venture) | Frontend | 1h | 3.4.3 | ⏳ Blocked on 3.4.1 |
| **3.4.3** | Add deal velocity comparison (venture vs venture) | Backend | 1h | 3.4.4 | ⏳ Blocked on 3.4.2 |
| **3.4.4** | Create revenue projections (sum across deals) | Backend | 2h | 3.4.5 | ⏳ Blocked on 3.4.3 |
| **3.4.5** | Export reports to PDF/CSV | Backend | 1h | None | ⏳ Blocked on 3.4.4 |

---

## PHASE 4: BUZZ COLLABORATION LAYER DEPLOYMENT (Week 2-3) — 12 Tasks

**Goal:** Deploy Buzz as CP-028 for human-AI deal collaboration  
**Authority:** CP-028 (Collaboration Control Plane)

### 4.1 Infrastructure Setup — 🔴 CRITICAL PATH (4 tasks)

| ID | Task | Owner | Effort | Blocking | Status |
|---|------|-------|--------|----------|--------|
| **4.1.1** | Deploy Buzz relay + PostgreSQL + Redis | DevOps | 2h | 4.1.2 | ⏳ Ready |
| **4.1.2** | Setup MinIO for file storage | DevOps | 1h | 4.1.3 | ⏳ Blocked on 4.1.1 |
| **4.1.3** | Configure Buzz webhooks for agent events | Engineer | 1h | 4.1.4 | ⏳ Blocked on 4.1.2 |
| **4.1.4** | Verify Buzz is accessible (http://localhost:3000) | QA | 30m | None | ⏳ Blocked on 4.1.3 |

### 4.2 Agent Integration — 🔴 CRITICAL PATH (4 tasks)

| ID | Task | Owner | Effort | Blocking | Status |
|---|------|-------|--------|----------|--------|
| **4.2.1** | Create Buzz channel for each agent type (#research, #outreach, etc.) | Engineer | 1h | 4.2.2 | ⏳ Blocked on 4.1.4 |
| **4.2.2** | Build MCP bridge (buzz_publish_event, buzz_read_channel) | Engineer | 2h | 4.2.3 | ⏳ Blocked on 4.2.1 |
| **4.2.3** | Rewire AGT-013/014/015 to publish to Buzz channels | Engineer | 2h | 4.2.4 | ⏳ Blocked on 4.2.2 |
| **4.2.4** | Test agent→Buzz publish + human response flow | QA | 1h | None | ⏳ Blocked on 4.2.3 |

### 4.3 Sync & Persistence — 🟠 HIGH (4 tasks)

| ID | Task | Owner | Effort | Blocking | Status |
|---|------|-------|--------|----------|--------|
| **4.3.1** | Create buzz-sync-agent (AGT-019) | Engineer | 2h | 4.3.2 | ⏳ Blocked on 4.2.4 |
| **4.3.2** | Build event thread → Neo4j merger | Engineer | 2h | 4.3.3 | ⏳ Blocked on 4.3.1 |
| **4.3.3** | Add cryptographic audit trail (sign events) | Security | 1h | 4.3.4 | ⏳ Blocked on 4.3.2 |
| **4.3.4** | Test Buzz→Neo4j persistence (full cycle) | QA | 1h | None | ⏳ Blocked on 4.3.3 |

---

## PHASE 5: AGENT ENABLEMENT & ORCHESTRATION (Week 3-4) — 20 Tasks

**Goal:** Activate 6 specialized agents + OmniRoute routing  
**Authority:** CP-006 (Agent Control Plane)

### 5.1 Agent Activation — 🔴 CRITICAL PATH (6 tasks)

| ID | Task | Agent | Effort | Blocking | Status |
|---|------|-------|--------|----------|--------|
| **5.1.1** | Activate Research Agent (AGT-010) | Engineer | 1h | 5.1.2 | ⏳ Blocked on Phase 1 API |
| **5.1.2** | Activate Lead Qualification Agent (AGT-011) | Engineer | 1h | 5.1.3 | ⏳ Blocked on 5.1.1 |
| **5.1.3** | Activate Outreach Agent (AGT-012) | Engineer | 1h | 5.1.4 | ⏳ Blocked on 5.1.2 |
| **5.1.4** | Activate Prospect Sourcing Agent (AGT-016) | Engineer | 1h | 5.1.5 | ⏳ Blocked on 5.1.3 |
| **5.1.5** | Activate Deal Analysis Agent (AGT-017) | Engineer | 1h | 5.1.6 | ⏳ Blocked on 5.1.4 |
| **5.1.6** | Activate Outreach Optimization Agent (AGT-018) | Engineer | 1h | None | ⏳ Blocked on 5.1.5 |

### 5.2 Agent Prompting & Tuning — 🟠 HIGH (5 tasks)

| ID | Task | Owner | Effort | Blocking | Status |
|---|------|-------|--------|----------|--------|
| **5.2.1** | Write research agent prompt (context assembly + search) | Prompt Engineer | 2h | 5.2.2 | ⏳ Blocked on 5.1.1 |
| **5.2.2** | Write qualification agent prompt (scoring logic) | Prompt Engineer | 2h | 5.2.3 | ⏳ Blocked on 5.2.1 |
| **5.2.3** | Write outreach agent prompt (email + LinkedIn templates) | Prompt Engineer | 2h | 5.2.4 | ⏳ Blocked on 5.2.2 |
| **5.2.4** | Write deal analysis agent prompt (financial modeling) | Prompt Engineer | 1h | 5.2.5 | ⏳ Blocked on 5.2.3 |
| **5.2.5** | Tune agent parameters (temperature, top_p, frequency penalties) | ML Engineer | 1h | None | ⏳ Blocked on 5.2.4 |

### 5.3 Agent Routing & Fallbacks — 🟠 HIGH (4 tasks)

| ID | Task | Owner | Effort | Blocking | Status |
|---|------|-------|--------|----------|--------|
| **5.3.1** | Configure OmniRoute routing rules per agent | DevOps | 1h | 5.3.2 | ⏳ Blocked on Phase 1 API |
| **5.3.2** | Add model fallback chains (main → backup → fallback) | DevOps | 1h | 5.3.3 | ⏳ Blocked on 5.3.1 |
| **5.3.3** | Implement agent retry logic + exponential backoff | Backend | 1h | 5.3.4 | ⏳ Blocked on 5.3.2 |
| **5.3.4** | Test agent dispatch under load (latency, error rates) | QA | 1h | None | ⏳ Blocked on 5.3.3 |

### 5.4 Agent Observability — 🟡 MEDIUM (5 tasks)

| ID | Task | Owner | Effort | Blocking | Status |
|---|------|-------|--------|----------|--------|
| **5.4.1** | Wire Langfuse to agent outputs (tracing) | Backend | 2h | 5.4.2 | ⏳ Blocked on Phase 1 API |
| **5.4.2** | Create agent performance dashboard (Grafana) | DevOps | 2h | 5.4.3 | ⏳ Blocked on 5.4.1 |
| **5.4.3** | Set up alerting for agent failures | DevOps | 1h | 5.4.4 | ⏳ Blocked on 5.4.2 |
| **5.4.4** | Create agent audit log (Neo4j) | Backend | 1h | 5.4.5 | ⏳ Blocked on 5.4.3 |
| **5.4.5** | Document agent observability runbook | Tech Writer | 30m | None | ⏳ Blocked on 5.4.4 |

---

## PHASE 6: REVENUE OPERATIONS (Week 3-5) — 20 Tasks

**Goal:** Activate revenue loops (lead gen → sales → collection)  
**Authority:** CP-020 (Financial Control Plane)

### 6.1 Pipeline Intelligence — 🟠 HIGH (5 tasks)

| ID | Task | Owner | Effort | Blocking | Status |
|---|------|-------|--------|----------|--------|
| **6.1.1** | Load live deal pipeline from PostgreSQL | Backend | 1h | 6.1.2 | ⏳ Blocked on DealFlowOS wiring |
| **6.1.2** | Build pipeline velocity model (deal cycle time) | Analytics | 2h | 6.1.3 | ⏳ Blocked on 6.1.1 |
| **6.1.3** | Create forecast model (deals won by month) | Analytics | 2h | 6.1.4 | ⏳ Blocked on 6.1.2 |
| **6.1.4** | Wire forecast to revenue dashboard | Backend | 1h | 6.1.5 | ⏳ Blocked on 6.1.3 |
| **6.1.5** | Test forecast accuracy (compare actuals monthly) | QA | 1h | None | ⏳ Blocked on 6.1.4 |

### 6.2 Lead Quality Scoring — 🟠 HIGH (4 tasks)

| ID | Task | Owner | Effort | Blocking | Status |
|---|------|-------|--------|----------|--------|
| **6.2.1** | Define lead scoring model (50-point scale) | Product | 2h | 6.2.2 | ⏳ Ready |
| **6.2.2** | Implement scoring via AGT-011 (qualification agent) | Backend | 2h | 6.2.3 | ⏳ Blocked on 6.2.1 |
| **6.2.3** | Create lead routing by score (hot → urgent, cold → nurture) | Backend | 1h | 6.2.4 | ⏳ Blocked on 6.2.2 |
| **6.2.4** | Test scoring against historical conversions | QA | 1h | None | ⏳ Blocked on 6.2.3 |

### 6.3 Revenue Recognition — 🟡 MEDIUM (5 tasks)

| ID | Task | Owner | Effort | Blocking | Status |
|---|------|-------|--------|----------|--------|
| **6.3.1** | Wire deal_payments table to PostgreSQL | Backend | 1h | 6.3.2 | ⏳ Ready |
| **6.3.2** | Implement payment webhook handler (Stripe) | Backend | 2h | 6.3.3 | ⏳ Blocked on 6.3.1 |
| **6.3.3** | Create revenue dashboard (MRR by venture) | Frontend | 1h | 6.3.4 | ⏳ Blocked on 6.3.2 |
| **6.3.4** | Build ARR projection (trailing 12-month) | Analytics | 1h | 6.3.5 | ⏳ Blocked on 6.3.3 |
| **6.3.5** | Export revenue reports (monthly/quarterly) | Backend | 30m | None | ⏳ Blocked on 6.3.4 |

### 6.4 Collections & Retention — 🟡 MEDIUM (6 tasks)

| ID | Task | Owner | Effort | Blocking | Status |
|---|------|-------|--------|----------|--------|
| **6.4.1** | Build payment reminder workflow (2/7/14 days overdue) | Backend | 1h | 6.4.2 | ⏳ Blocked on 6.3.1 |
| **6.4.2** | Create dunning email sequences | Backend | 1h | 6.4.3 | ⏳ Blocked on 6.4.1 |
| **6.4.3** | Implement churn prediction model | Analytics | 2h | 6.4.4 | ⏳ Blocked on 6.4.2 |
| **6.4.4** | Create at-risk customer alerts | Backend | 1h | 6.4.5 | ⏳ Blocked on 6.4.3 |
| **6.4.5** | Build customer health dashboard | Frontend | 1h | 6.4.6 | ⏳ Blocked on 6.4.4 |
| **6.4.6** | Test retention workflows (full cycle) | QA | 1h | None | ⏳ Blocked on 6.4.5 |

---

## PHASE 7: VENTURE ACCELERATION (Week 4-6) — 25 Tasks

**Goal:** Activate revenue loops for 5 focus ventures  
**Authority:** CP-020 (Financial) + Venture leads

### 7.1 Venture-Specific Wiring (5 ventures × 2 tasks) — 🟠 HIGH (10 tasks)

For each venture (CON-001, LT-005, LT-011, OPS-001, RE-001):

| ID | Venture | Task | Owner | Effort | Blocking | Status |
|---|---------|------|-------|--------|----------|--------|
| **7.1.1** | CON-001 | Wire ClickUp tasks + PostgreSQL sync | Backend | 1h | 7.1.11 | ⏳ Blocked on Phase 5 |
| **7.1.2** | CON-001 | Create Slack notifications (daily pipeline digest) | Backend | 1h | 7.1.11 | ⏳ Blocked on 7.1.1 |
| **7.1.3** | LT-005 | Wire ClickUp + sync | Backend | 1h | 7.1.11 | ⏳ Blocked on Phase 5 |
| **7.1.4** | LT-005 | Slack notifications | Backend | 1h | 7.1.11 | ⏳ Blocked on 7.1.3 |
| **7.1.5** | LT-011 | Wire ClickUp + sync | Backend | 1h | 7.1.11 | ⏳ Blocked on Phase 5 |
| **7.1.6** | LT-011 | Slack notifications | Backend | 1h | 7.1.11 | ⏳ Blocked on 7.1.5 |
| **7.1.7** | OPS-001 | Wire ClickUp + sync | Backend | 1h | 7.1.11 | ⏳ Blocked on Phase 5 |
| **7.1.8** | OPS-001 | Slack notifications | Backend | 1h | 7.1.11 | ⏳ Blocked on 7.1.7 |
| **7.1.9** | RE-001 | Wire ClickUp + sync | Backend | 1h | 7.1.11 | ⏳ Blocked on Phase 5 |
| **7.1.10** | RE-001 | Slack notifications | Backend | 1h | 7.1.11 | ⏳ Blocked on 7.1.9 |

### 7.2 Lead Generation Activation (5 ventures × 1 task) — 🟠 HIGH (5 tasks)

| ID | Venture | Task | Owner | Effort | Blocking | Status |
|---|---------|------|-------|--------|----------|--------|
| **7.2.1** | CON-001 | Launch paid acquisition campaign (Google, LinkedIn) | Growth | 2h | 7.1.2 | ⏳ Blocked on Phase 6.2 |
| **7.2.2** | LT-005 | Launch paid acquisition campaign | Growth | 2h | 7.1.4 | ⏳ Blocked on Phase 6.2 |
| **7.2.3** | LT-011 | Launch paid acquisition campaign | Growth | 2h | 7.1.6 | ⏳ Blocked on Phase 6.2 |
| **7.2.4** | OPS-001 | Launch paid acquisition campaign | Growth | 2h | 7.1.8 | ⏳ Blocked on Phase 6.2 |
| **7.2.5** | RE-001 | Launch paid acquisition campaign | Growth | 2h | 7.1.10 | ⏳ Blocked on Phase 6.2 |

### 7.3 Sales Enablement (5 ventures × 1 task) — 🟠 HIGH (5 tasks)

| ID | Venture | Task | Owner | Effort | Blocking | Status |
|---|---------|------|-------|--------|----------|--------|
| **7.3.1** | CON-001 | Create sales playbook (targeting, objection handling) | Sales | 2h | 7.2.1 | ⏳ Blocked on Phase 6.2 |
| **7.3.2** | LT-005 | Create sales playbook | Sales | 2h | 7.2.2 | ⏳ Blocked on Phase 6.2 |
| **7.3.3** | LT-011 | Create sales playbook | Sales | 2h | 7.2.3 | ⏳ Blocked on Phase 6.2 |
| **7.3.4** | OPS-001 | Create sales playbook | Sales | 2h | 7.2.4 | ⏳ Blocked on Phase 6.2 |
| **7.3.5** | RE-001 | Create sales playbook | Sales | 2h | 7.2.5 | ⏳ Blocked on Phase 6.2 |

---

## PHASE 8: OBSERVABILITY & MONITORING (Week 3-6) — 15 Tasks

**Goal:** Full-stack observability for all systems  
**Authority:** CP-027 (Infrastructure)

### 8.1 Logging & Tracing — 🟠 HIGH (5 tasks)

| ID | Task | Owner | Effort | Blocking | Status |
|---|------|-------|--------|----------|--------|
| **8.1.1** | Wire Langfuse to all agents (KG-017/028, Neo4j, etc.) | Backend | 2h | 8.1.2 | ⏳ Blocked on Phase 1 API |
| **8.1.2** | Setup structured logging (JSON format) | DevOps | 1h | 8.1.3 | ⏳ Blocked on 8.1.1 |
| **8.1.3** | Route logs to ELK stack / Grafana Loki | DevOps | 1h | 8.1.4 | ⏳ Blocked on 8.1.2 |
| **8.1.4** | Create log aggregation dashboards | DevOps | 1h | 8.1.5 | ⏳ Blocked on 8.1.3 |
| **8.1.5** | Setup retention policies (30 days hot, 1 year archive) | DevOps | 30m | None | ⏳ Blocked on 8.1.4 |

### 8.2 Metrics & Alerting — 🟠 HIGH (5 tasks)

| ID | Task | Owner | Effort | Blocking | Status |
|---|------|-------|--------|----------|--------|
| **8.2.1** | Define SLOs (API <200ms, agents <5min per task) | Product | 1h | 8.2.2 | ⏳ Ready |
| **8.2.2** | Setup Prometheus metrics exporters | DevOps | 2h | 8.2.3 | ⏳ Blocked on 8.2.1 |
| **8.2.3** | Build SLO dashboards (Grafana) | DevOps | 1h | 8.2.4 | ⏳ Blocked on 8.2.2 |
| **8.2.4** | Configure PagerDuty alerts (critical SLO breaches) | DevOps | 1h | 8.2.5 | ⏳ Blocked on 8.2.3 |
| **8.2.5** | Test alerting (simulate failures, verify paging) | QA | 1h | None | ⏳ Blocked on 8.2.4 |

### 8.3 Infrastructure Health — 🟡 MEDIUM (5 tasks)

| ID | Task | Owner | Effort | Blocking | Status |
|---|------|-------|--------|----------|--------|
| **8.3.1** | Monitor Neo4j health (heap, query time, deadlocks) | DevOps | 1h | 8.3.2 | ⏳ Ready |
| **8.3.2** | Monitor Qdrant health (memory, latency, index size) | DevOps | 1h | 8.3.3 | ⏳ Blocked on 8.3.1 |
| **8.3.3** | Monitor PostgreSQL (connections, lock contention, slow queries) | DevOps | 1h | 8.3.4 | ⏳ Blocked on 8.3.2 |
| **8.3.4** | Monitor OmniRoute (model queue, latency, errors) | DevOps | 1h | 8.3.5 | ⏳ Blocked on 8.3.3 |
| **8.3.5** | Create infrastructure dashboard (all systems) | DevOps | 1h | None | ⏳ Blocked on 8.3.4 |

---

## PHASE 9: DOCUMENTATION & KNOWLEDGE TRANSFER (Week 5-6) — 15 Tasks

**Goal:** Complete documentation for all systems  
**Authority:** CP-027 (Infrastructure)

### 9.1 API Documentation — 🟡 MEDIUM (5 tasks)

| ID | Task | Owner | Effort | Blocking | Status |
|---|------|-------|--------|----------|--------|
| **9.1.1** | Document Graph API (KG-048) with OpenAPI spec | Tech Writer | 2h | 9.1.2 | ⏳ Blocked on Phase 1 |
| **9.1.2** | Document Neo4j query patterns (Cypher examples) | Tech Writer | 1h | 9.1.3 | ⏳ Blocked on 9.1.1 |
| **9.1.3** | Document OmniRoute agent routing | Tech Writer | 1h | 9.1.4 | ⏳ Blocked on 9.1.2 |
| **9.1.4** | Document PostgreSQL schema (deals, notes, runs) | Tech Writer | 1h | 9.1.5 | ⏳ Blocked on 9.1.3 |
| **9.1.5** | Create API playground / sandbox | Engineer | 1h | None | ⏳ Blocked on 9.1.4 |

### 9.2 Operator Runbooks — 🟡 MEDIUM (5 tasks)

| ID | Task | Owner | Effort | Blocking | Status |
|---|------|-------|--------|----------|--------|
| **9.2.1** | Write incident response runbook (how to troubleshoot) | DevOps | 1h | 9.2.2 | ⏳ Ready |
| **9.2.2** | Write database maintenance runbook (backups, tuning) | DBA | 1h | 9.2.3 | ⏳ Blocked on 9.2.1 |
| **9.2.3** | Write agent troubleshooting guide (failed runs, errors) | Support | 1h | 9.2.4 | ⏳ Blocked on 9.2.2 |
| **9.2.4** | Write deployment runbook (how to deploy updates) | DevOps | 1h | 9.2.5 | ⏳ Blocked on 9.2.3 |
| **9.2.5** | Create video tutorials (onboarding new team members) | Content | 2h | None | ⏳ Blocked on 9.2.4 |

### 9.3 Architecture Documentation — 🟡 MEDIUM (5 tasks)

| ID | Task | Owner | Effort | Blocking | Status |
|---|------|-------|--------|----------|--------|
| **9.3.1** | Update CLAUDE.md with Phase 1 results | Architect | 1h | 9.3.2 | ⏳ Blocked on Phase 1 |
| **9.3.2** | Update system architecture diagram (Mermaid) | Architect | 1h | 9.3.3 | ⏳ Blocked on 9.3.1 |
| **9.3.3** | Document data flow (lead → deal → revenue) | Architect | 1h | 9.3.4 | ⏳ Blocked on 9.3.2 |
| **9.3.4** | Create control plane governance doc | Architect | 1h | 9.3.5 | ⏳ Blocked on 9.3.3 |
| **9.3.5** | Document decision log (why we chose X over Y) | Architect | 1h | None | ⏳ Blocked on 9.3.4 |

---

## PHASE 10: TESTING & LAUNCH PREP (Week 6-7) — 12 Tasks

**Goal:** Comprehensive testing + go-live readiness  
**Authority:** CP-027 (Infrastructure)

### 10.1 Integration Testing — 🔴 CRITICAL PATH (6 tasks)

| ID | Task | Owner | Effort | Blocking | Status |
|---|------|-------|--------|----------|--------|
| **10.1.1** | E2E test: Lead discovery → score → DealFlowOS | QA | 2h | 10.1.2 | ⏳ Blocked on Phase 6.2 |
| **10.1.2** | E2E test: Neo4j query → agent routing → response | QA | 1h | 10.1.3 | ⏳ Blocked on 10.1.1 |
| **10.1.3** | E2E test: DealFlowOS deal update → PostgreSQL → Slack | QA | 1h | 10.1.4 | ⏳ Blocked on 10.1.2 |
| **10.1.4** | Stress test: 100 concurrent deals, agent queries | QA | 2h | 10.1.5 | ⏳ Blocked on 10.1.3 |
| **10.1.5** | Load test: OmniRoute at 10 req/sec | QA | 1h | 10.1.6 | ⏳ Blocked on 10.1.4 |
| **10.1.6** | Chaos test: Simulate Neo4j/Qdrant outage, verify fallbacks | QA | 1h | None | ⏳ Blocked on 10.1.5 |

### 10.2 Security & Compliance — 🟠 HIGH (4 tasks)

| ID | Task | Owner | Effort | Blocking | Status |
|---|------|-------|--------|----------|--------|
| **10.2.1** | Audit API key rotation policy | Security | 1h | 10.2.2 | ⏳ Ready |
| **10.2.2** | Verify data encryption (in transit + at rest) | Security | 1h | 10.2.3 | ⏳ Blocked on 10.2.1 |
| **10.2.3** | Run OWASP security scan (SQL injection, XSS, etc.) | Security | 1h | 10.2.4 | ⏳ Blocked on 10.2.2 |
| **10.2.4** | Audit access logs (who accessed what, when) | Compliance | 1h | None | ⏳ Blocked on 10.2.3 |

### 10.3 Launch Checklist — 🟠 HIGH (2 tasks)

| ID | Task | Owner | Effort | Blocking | Status |
|---|------|-------|--------|----------|--------|
| **10.3.1** | Verify all 5 focus ventures are live + generating leads | Product | 1h | 10.3.2 | ⏳ Blocked on Phase 7 |
| **10.3.2** | Go-live approval + postmortem prep | Leadership | 1h | None | ⏳ Blocked on 10.3.1 |

---

## SUMMARY TABLE

| Phase | Timeline | Tasks | Goal | Status |
|-------|----------|-------|------|--------|
| **Phase 1** | Week 1-2 | 15 | KG Agent Enablement | ⏳ Ready to start |
| **Phase 2** | Week 1-4 | 32 | Repository Intelligence | ⏳ Blocked on Phase 1 |
| **Phase 3** | Week 2-3 | 18 | DealFlowOS Enhancements | ⏳ Blocked on Phase 1 |
| **Phase 4** | Week 2-3 | 12 | Buzz Collaboration | ⏳ Blocked on Phase 1 |
| **Phase 5** | Week 3-4 | 20 | Agent Orchestration | ⏳ Blocked on Phase 1 |
| **Phase 6** | Week 3-5 | 20 | Revenue Operations | ⏳ Blocked on Phase 5 |
| **Phase 7** | Week 4-6 | 25 | Venture Activation | ⏳ Blocked on Phase 6 |
| **Phase 8** | Week 3-6 | 15 | Observability | ⏳ Blocked on Phase 1 |
| **Phase 9** | Week 5-6 | 15 | Documentation | ⏳ Blocked on Phases 1-7 |
| **Phase 10** | Week 6-7 | 12 | Launch Prep | ⏳ Blocked on Phase 9 |
| **TOTAL** | 7 weeks | **184** | Production Ready | 🟡 In Planning |

---

## CRITICAL PATH TO GO-LIVE

```
Phase 1 (KG) → Phase 5 (Agents) → Phase 6 (Revenue) → Phase 7 (Ventures) → Phase 10 (Launch)
    ↓              ↓                  ↓                   ↓                    ↓
  (Week 2)     (Week 4)            (Week 5)           (Week 6)            (Week 7)
  
Parallel:
- Phase 2 (Repo Intelligence) runs in parallel with Phase 1-5
- Phase 3 (DealFlowOS) can start Week 2 after Phase 1 API
- Phase 4 (Buzz) can start Week 2 after Phase 1 API
- Phase 8 (Observability) can start Week 3 with Phase 1
- Phase 9 (Docs) starts Week 5 as phases complete
```

---

## RESOURCE ALLOCATION

| Role | Phase 1 | Phase 2 | Phase 3 | Phase 4 | Phase 5 | Total |
|------|---------|---------|---------|---------|---------|-------|
| Engineer | 10h | 12h | 8h | 6h | 12h | 48h |
| Architect | 4h | 2h | 2h | 1h | 2h | 11h |
| DevOps | 2h | 1h | 1h | 3h | 4h | 11h |
| QA | 2h | 2h | 1h | 1h | 2h | 8h |
| Product/Growth | 1h | — | 2h | — | 5h | 8h |
| **TOTAL** | **19h** | **17h** | **14h** | **11h** | **25h** | **86h** |

---

## DEPENDENCIES & UNBLOCKING

**Phase 1 is the CRITICAL BLOCKER for Phases 2-8.**
- All agent orchestration depends on KG-017/028/048
- DealFlowOS enrichment depends on API endpoints
- Buzz integration depends on MCP tools
- Revenue operations depends on agent activation

**To unblock Phase 2-7 in parallel:**
- Start Phase 1 immediately (Week 1, Sep 6)
- Phase 1 should complete by Week 2 (Sep 12)
- All downstream phases start Week 2 (Sep 13)

---

**Generated:** 2026-09-08  
**Last Updated:** 2026-09-08  
**Next Review:** 2026-09-15 (mid-Phase 1)  
**Authority:** CP-027 (Infrastructure Control Plane)
