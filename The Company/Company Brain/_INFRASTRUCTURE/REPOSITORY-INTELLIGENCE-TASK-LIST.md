[[STARTHERE]] | [[REALITY]] | [[REPOSITORY-INTELLIGENCE-SYSTEM]] | [[DEVICE-STORAGE-TOPOLOGY]] | [[16-AGENTS]]

# Repository Intelligence System — Task List & Agent Assignments

**Authority:** CP-006 [[Agent Control Plane|16-AGENTS]] + CP-027 [[Infrastructure Control Plane|56-INFRASTRUCTURE]]

**Timeline:** Week 1-4 (Sep 6-27, 2026)  
**Total Tasks:** 32 structured tasks across 8 phases  
**New Agents Required:** 5 specialized agents (to be created)

---

## PHASE 1: INVENTORY (2h automated) — Week 1

### Tasks 1.1-1.4: GitHub Ingestion

| Task ID | Task | Agent | Effort | Status | Blocking |
|---------|------|-------|--------|--------|----------|
| **1.1** | Create GitHub API script to fetch all starred repos | AGT-003 (Technical) | 30m | 🟡 Ready | None |
| **1.2** | Ingest 904 repos + metadata into `/Volumes/LaCie/repositories/raw/github-starred.json` | AGT-003 + repo-ingestion-agent | 90m | ⏳ Blocked on 1.1 | 1.1 |
| **1.3** | Verify ingestion completeness (count, sample check) | AGT-003 | 15m | ⏳ Blocked on 1.2 | 1.2 |
| **1.4** | Document ingestion metadata (timestamp, source, version) | AGT-003 | 15m | ⏳ Blocked on 1.3 | 1.3 |

**Agent: AGT-003-technical (Infrastructure execution)**
- Responsible for: API integration, error handling, retry logic, logging
- Output: `/Volumes/LaCie/repositories/raw/github-starred.json`
- Success criteria: All 904 repos ingested, no 404s, metadata enriched

**New Agent Required: `repo-ingestion-agent`**
- Responsibility: GitHub API client, batching, rate limit handling
- Framework: FastMCP tool (OmniRoute-compatible)
- Triggers: On-demand or scheduled (weekly)

---

## PHASE 2: NORMALIZE (30m automated) — Week 1

### Tasks 2.1-2.5: Deduplication & Validation

| Task ID | Task | Agent | Effort | Status | Blocking |
|---------|------|--------|--------|--------|----------|
| **2.1** | Detect duplicate entries (same GitHub URL) | repo-normalizer-agent | 10m | ⏳ Blocked on 1.4 | 1.4 |
| **2.2** | Check for archived repos, deleted repos, 404s | repo-normalizer-agent | 10m | ⏳ Blocked on 2.1 | 2.1 |
| **2.3** | Identify renamed repos (follow GitHub redirects) | repo-normalizer-agent | 5m | ⏳ Blocked on 2.2 | 2.2 |
| **2.4** | Remove personal forks, stubs, spam | repo-normalizer-agent | 5m | ⏳ Blocked on 2.3 | 2.3 |
| **2.5** | Output deduplicated set (880-900 repos) | repo-normalizer-agent | 5m | ⏳ Blocked on 2.4 | 2.4 |

**New Agent Required: `repo-normalizer-agent`**
- Responsibility: Deduplication, archive checking, GitHub redirect following
- Framework: FastMCP + Neo4j integration
- Input: `/Volumes/LaCie/repositories/raw/github-starred.json`
- Output: `/Volumes/LaCie/repositories/normalized/deduplicated.json`
- Success criteria: 880-900 valid repos, no duplicates, all archives flagged

---

## PHASE 3: ENRICH (4-6h parallel) — Week 1-2

### Tasks 3.1-3.6: Deep Metadata Collection

| Task ID | Task | Agent | Effort | Status | Blocking |
|---------|------|--------|--------|--------|----------|
| **3.1** | Collect GitHub metadata (stars, forks, issues, activity) | repo-enricher-agent | 2h | ⏳ Blocked on 2.5 | 2.5 |
| **3.2** | Extract README content (first 2000 chars) | repo-enricher-agent | 1h | ⏳ Blocked on 3.1 | 3.1 |
| **3.3** | Parse dependency manifests (if available) | repo-enricher-agent | 1h | ⏳ Blocked on 3.2 | 3.2 |
| **3.4** | Classify architecture type (monolith/microservices/lib/tool) | repo-enricher-agent | 30m | ⏳ Blocked on 3.3 | 3.3 |
| **3.5** | Detect test/CI/security scanning presence | repo-enricher-agent | 30m | ⏳ Blocked on 3.4 | 3.4 |
| **3.6** | Store enriched metadata (one JSON per repo) | repo-enricher-agent | 30m | ⏳ Blocked on 3.5 | 3.5 |

**New Agent Required: `repo-enricher-agent`**
- Responsibility: Parallel metadata collection, REST API calls, error recovery
- Framework: FastMCP + async processing
- Input: `/Volumes/LaCie/repositories/normalized/deduplicated.json`
- Output: `/Volumes/LaCie/repositories/enriched/{repo_id}.json` (880-900 files)
- Parallelization: 10 concurrent API calls
- Success criteria: All repos enriched, no truncation, metadata complete

---

## PHASE 4: CLASSIFY (8-12h agent-driven) — Week 2

### TWO-LAYER EXECUTION

**LAYER 1: INTERACTIVE (Agency Personas)**
| Task | Persona | Purpose |
|------|---------|---------|
| **4.1a** | repo-advisor (activate in Claude Code) | Review unclear classifications, domain expertise |
| **4.1b** | repo-deep-dive (for edge cases) | Forensic code review of ambiguous repos |

**LAYER 2: AUTONOMOUS (Company Brain Agents + MCP)**
| Task ID | Task | Agent | Tools | Effort | Status | Blocking |
|---------|------|-------|-------|--------|--------|----------|
| **4.2** | Setup Classification Agent (repo-classifier) | AGT-003 (Technical) | MCP: fastmcp_server.py | 1h | ⏳ Blocked on 3.6 | 3.6 |
| **4.3** | Classify repos into Company Brain ontology (via MCP) | AGT-013 (Claude Agent) | neo4j_query_entities, omniroute_select_model | 8h | ⏳ Blocked on 4.2 | 4.2 |
| **4.4** | Detect secondary capabilities + cross-classifications | AGT-013 | neo4j_merge_classification (MCP) | 2h | ⏳ Blocked on 4.3 | 4.3 |
| **4.5** | Map industry relevance + venture applicability | AGT-013 | OmniRoute MCP (model routing) | 1h | ⏳ Blocked on 4.4 | 4.4 |
| **4.6** | Output classifications by category | AGT-013 | fastmcp_server.py (write to Neo4j) | 30m | ⏳ Blocked on 4.5 | 4.5 |
| **4.7** | Human review of edge cases (via repo-advisor) | AGT-003 + repo-advisor | Knowledge Graph Engineer MCP | 1h | ⏳ Blocked on 4.6 | 4.6 |

**MCP Tools Required:**
- `neo4j_query_entities(type: str) → [entities]` — List existing capabilities, ventures
- `neo4j_merge_classification(repo_id: str, classification: dict) → result` — Write classifications to graph
- `omniroute_select_model(task: str, complexity: int) → model_recommendation` — Route to appropriate model

**How It Works:**
1. **AGT-013 starts:** Reads enriched repo metadata
2. **AGT-013 queries MCP:** `neo4j_query_entities("Capability")` → list all 300+ capabilities
3. **AGT-013 classifies:** Maps repo to capabilities, secondary capabilities, architecture layer
4. **AGT-013 merges:** Calls `neo4j_merge_classification()` → writes to Neo4j
5. **repo-advisor persona:** Available for human questions ("Is this repo ambiguous?")
6. **repo-deep-dive persona:** Available for high-risk repos ("Should we fork or adopt?")
7. **AGT-003 validates:** All classifications landed in Neo4j

**Success criteria:** All repos classified, multi-dimensional mappings, confidence scores, MCP queries logged

---

## PHASE 5: SCORE (4-6h agent-driven) — Week 2

### Tasks 5.1-5.5: Strategic Evaluation

| Task ID | Task | Agent | Effort | Status | Blocking |
|---------|------|--------|--------|--------|----------|
| **5.1** | Setup Scoring Agent (repo-scorer) | AGT-003 (Technical) | 1h | ⏳ Blocked on 4.5 | 4.5 |
| **5.2** | Score all repos on 10 dimensions (relevance, maintenance, maturity, security, license, community, integration, performance, differentiation, viability) | repo-scorer-agent | 4h | ⏳ Blocked on 5.1 | 5.1 |
| **5.3** | Aggregate scores into STRATEGIC_SCORE (0-100) | repo-scorer-agent | 1h | ⏳ Blocked on 5.2 | 5.2 |
| **5.4** | Assign tier classification (CRITICAL/HIGH/USEFUL/REFERENCE/LOW/ARCHIVE) | repo-scorer-agent | 30m | ⏳ Blocked on 5.3 | 5.3 |
| **5.5** | Output scores organized by tier | repo-scorer-agent | 30m | ⏳ Blocked on 5.4 | 5.4 |

**Agent: AGT-003-technical (setup & monitoring)**
- Responsible for: Agent provisioning, validation criteria, tier thresholds

**New Agent Required: `repo-scorer-agent` (Claude Agent)**
- Responsibility: Score each repo on 10 strategic dimensions
- Scoring criteria: Relevance, maintenance, maturity, security, license, community, integration, performance, differentiation, viability
- Input: `/Volumes/LaCie/repositories/classified/classifications.json`
- Output: `/Volumes/LaCie/repositories/scored/scores.json` + `/Volumes/LaCie/repositories/scored/by-tier/`
- Batching: 5-10 repos/batch (reasoning-heavy)
- Success criteria: All repos scored 0-100, tier distribution reasonable (not all CRITICAL)

---

## PHASE 6: DISPOSITION (4h agent-driven + review) — Week 2

### Tasks 6.1-6.6: Decision Making

| Task ID | Task | Agent | Effort | Status | Blocking |
|---------|------|--------|--------|--------|----------|
| **6.1** | Setup Disposition Agent (repo-disposition) | AGT-003 (Technical) | 1h | ⏳ Blocked on 5.5 | 5.5 |
| **6.2** | Decide disposition for each repo (ADOPT/INTEGRATE/FORK/EXTEND/REFERENCE/LEARN/MONITOR/CONTRIBUTE/REPLACE/COMPETE/ARCHIVE/IGNORE) | repo-disposition-agent | 3h | ⏳ Blocked on 6.1 | 6.1 |
| **6.3** | Generate rationale + timeline for each decision | repo-disposition-agent | 1h | ⏳ Blocked on 6.2 | 6.2 |
| **6.4** | Assign owner (agent responsible for ongoing monitoring) | repo-disposition-agent | 30m | ⏳ Blocked on 6.3 | 6.3 |
| **6.5** | Human review of top 50 repos (CRITICAL + HIGH tiers) | AGT-001 (Venture PM) | 2h | ⏳ Blocked on 6.4 | 6.4 |
| **6.6** | Output dispositions by category | repo-disposition-agent | 30m | ⏳ Blocked on 6.5 | 6.5 |

**Agent: AGT-003-technical (setup & monitoring) + AGT-001-venture-pm (human review)**
- Responsible for: Agent provisioning, validation, stakeholder alignment

**New Agent Required: `repo-disposition-agent` (Claude Agent)**
- Responsibility: Decide what to do with each repo
- Decision tree: ADOPT (production use), INTEGRATE (with adapters), FORK (diverge), REFERENCE (study), MONITOR (watch), ARCHIVE (dormant), etc.
- Input: `/Volumes/LaCie/repositories/scored/scores.json` + Company Brain context
- Output: `/Volumes/LaCie/repositories/dispositioned/dispositions.json` + `/Volumes/LaCie/repositories/dispositioned/by-disposition/`
- Batching: 3-5 repos/batch (reasoning-heavy)
- Success criteria: All repos dispositioned, rationale clear, top 50 reviewed by humans

---

## PHASE 7: GRAPH INTEGRATION (2-4h automated) — Week 3

### Tasks 7.1-7.4: Neo4j Wiring

| Task ID | Task | Agent | Effort | Status | Blocking |
|---------|------|--------|--------|--------|----------|
| **7.1** | Create Neo4j schema for ExternalRepository nodes + relationships | AGT-003 (Technical) | 1h | ⏳ Blocked on 6.6 | 6.6 |
| **7.2** | Ingest repositories into Neo4j as nodes (880-900 repos) | repo-graph-agent | 1h | ⏳ Blocked on 7.1 | 7.1 |
| **7.3** | Create relationships (IMPLEMENTS, ENABLES, COMPLEMENTS, COMPETES_WITH, REPLACES, ARCH_LAYER, etc.) | repo-graph-agent | 1h | ⏳ Blocked on 7.2 | 7.2 |
| **7.4** | Verify graph integrity (count nodes, relationships, orphans) | AGT-003 | 30m | ⏳ Blocked on 7.3 | 7.3 |

**Agent: AGT-003-technical (implementation) + repo-graph-agent (data loading)**
- Responsible for: Neo4j schema, Cypher query execution, data validation

**New Agent Required: `repo-graph-agent`**
- Responsibility: Load repository data into Neo4j, create relationships
- Framework: FastMCP + Cypher execution
- Input: `/Volumes/LaCie/repositories/dispositioned/dispositions.json`
- Output: Neo4j nodes (ExternalRepository) + relationships
- Success criteria: All 880+ repos in graph, relationships bidirectional, no orphans

---

## PHASE 8: OPERATIONALIZE & MONITOR (Ongoing) — Week 3+

### Tasks 8.1-8.8: Production Readiness

| Task ID | Task | Agent | Effort | Status | Blocking |
|---------|------|--------|--------|--------|----------|
| **8.1** | Define adoption pipeline stages (sandbox/benchmark/security/integration/production) | AGT-003 (Technical) + AGT-001 (Venture PM) | 1h | ⏳ Blocked on 7.4 | 7.4 |
| **8.2** | Select top 5 CRITICAL/HIGH repos for immediate adoption testing | AGT-001 (Venture PM) | 30m | ⏳ Blocked on 8.1 | 8.1 |
| **8.3** | Create sandbox test environments (Docker + Mac Studio) for top 5 repos | AGT-003 (Technical) | 2h | ⏳ Blocked on 8.2 | 8.2 |
| **8.4** | Run sandbox tests + document results | repo-adoption-agent | 3h | ⏳ Blocked on 8.3 | 8.3 |
| **8.5** | Setup weekly health monitoring (repo-monitor-agent) | repo-monitor-agent | 1h | ⏳ Blocked on 7.4 | 7.4 |
| **8.6** | Run benchmark tests (performance, compatibility) for top 5 repos | repo-adoption-agent | 2h | ⏳ Blocked on 8.4 | 8.4 |
| **8.7** | Security scan all adopted repos (dependency vulnerabilities, secrets) | AGT-003 (Technical) | 1h | ⏳ Blocked on 8.6 | 8.6 |
| **8.8** | Document adoption runbooks + monitoring procedures | AGT-005 (Operations) | 2h | ⏳ Blocked on 8.7 | 8.7 |

**Agents:**
- AGT-003 (Technical): Infrastructure, sandbox setup, security scans
- AGT-001 (Venture PM): Selection criteria, business alignment
- AGT-005 (Operations): Documentation, runbook creation
- New: repo-adoption-agent, repo-monitor-agent

**New Agents Required:**
- `repo-adoption-agent`: Execute adoption pipeline (sandbox→benchmark→integration→production)
- `repo-monitor-agent`: Weekly health checks (commit activity, vulnerabilities, releases)

---

## PHASE 9: AWESOME LISTS INTEGRATION (4-6h) — Week 3-4

### Tasks 9.1-9.5: Extended Universe

| Task ID | Task | Agent | Effort | Status | Blocking |
|---------|------|--------|--------|--------|----------|
| **9.1** | Clone sindresorhus/awesome repository | repo-ingestion-agent | 15m | ⏳ Blocked on 1.4 | 1.4 |
| **9.2** | Parse all 27 category pages + extract sub-list URLs | repo-awesome-parser-agent | 2h | ⏳ Blocked on 9.1 | 9.1 |
| **9.3** | Deduplicate Awesome repos against 904 starred repos | repo-awesome-dedup-agent | 1h | ⏳ Blocked on 9.2 | 9.2 |
| **9.4** | Classify new repos (not in 904) into Company Brain ontology | repo-classifier-agent | 2h | ⏳ Blocked on 9.3 | 9.3 |
| **9.5** | Create unified registry (904 + Awesome overlap + new) | repo-graph-agent | 1h | ⏳ Blocked on 9.4 | 9.4 |

**New Agents Required:**
- `repo-awesome-parser-agent`: Parse Awesome list markdown, extract URLs
- `repo-awesome-dedup-agent`: Deduplicate against existing 904 repos

---

## DELIVERABLES SUMMARY

### By End of Week 1
- ✅ Phase 1-2 complete: 880-900 normalized repos in `/Volumes/LaCie/repositories/`
- ✅ Phase 3 in progress: Enriched metadata being collected

### By End of Week 2
- ✅ Phase 3-6 complete: Classifications, scores, dispositions ready
- ✅ Top 50 CRITICAL/HIGH repos flagged for adoption
- ✅ Neo4j loaded (Phase 7 in progress)

### By End of Week 3
- ✅ Phase 7-8 complete: Neo4j fully wired, adoption pipeline live
- ✅ 5-10 repos in sandbox testing
- ✅ Weekly monitoring active (repo-monitor-agent running)
- ✅ Phase 9 in progress: Awesome lists ingested

### By End of Week 4
- ✅ Phase 9 complete: Unified registry (1,200-1,500 repos)
- ✅ 3-5 repos adopted + deployed
- ✅ Repository Intelligence System fully operational
- ✅ Decision engine ready for capability queries

---

## AGENT ROSTER (Existing + New)

### Existing Agents (Use For Coordination)

| Agent | Role | Tasks |
|-------|------|-------|
| **AGT-001 (Venture PM)** | Project coordination, human review, business alignment | 6.5, 8.1, 8.2 |
| **AGT-003 (Technical)** | Infrastructure, deployment, security | 1.1, 2.x (monitor), 4.1, 5.1, 6.1, 7.1, 7.4, 8.1, 8.3, 8.7 |
| **AGT-005 (Operations)** | Documentation, runbooks, SLAs | 8.8 |

### New Agents to Create

| Agent ID | Name | Framework | Responsibility | Autonomy |
|----------|------|-----------|---|----------|
| **AGT-010** | repo-ingestion-agent | FastMCP + CLI | GitHub API client, batching, rate limits | L2 (assisted) |
| **AGT-011** | repo-normalizer-agent | FastMCP + Neo4j | Deduplication, archive checking, redirect following | L2 (assisted) |
| **AGT-012** | repo-enricher-agent | FastMCP + async | Parallel metadata collection, error recovery | L2 (assisted) |
| **AGT-013** | repo-classifier-agent | Claude Agent | Classify repos into ontology (10-dimensional) | L2 (assisted) |
| **AGT-014** | repo-scorer-agent | Claude Agent | Score repos on 10 dimensions (0-100) | L2 (assisted) |
| **AGT-015** | repo-disposition-agent | Claude Agent | Decide ADOPT/INTEGRATE/FORK/etc. + rationale | L2 (assisted) |
| **AGT-016** | repo-graph-agent | FastMCP + Cypher | Load Neo4j, create relationships | L2 (assisted) |
| **AGT-017** | repo-adoption-agent | FastMCP + Docker | Execute adoption pipeline (sandbox/benchmark/integration) | L2 (assisted) |
| **AGT-018** | repo-monitor-agent | FastMCP + CI | Weekly health checks (activity, vulnerabilities, releases) | L3 (autonomous) |
| **AGT-019** | repo-awesome-parser-agent | FastMCP + markdown | Parse Awesome lists, extract URLs | L2 (assisted) |
| **AGT-020** | repo-awesome-dedup-agent | FastMCP + Neo4j | Deduplicate Awesome repos against 904 starred | L2 (assisted) |

**Total New Agents:** 11 specialized agents  
**Total Active Agents:** 16 (5 existing + 11 new)  
**Autonomy Level:** L1/L2 during Phase 1-9, L3 for repo-monitor-agent ongoing

---

## EXECUTION STRATEGY

### Week 1 (Sep 6-12): Phases 1-3

**Monday-Tuesday:** Phase 1 (GitHub ingestion)  
- Launch repo-ingestion-agent
- Execute: 904 repos → /Volumes/LaCie/repositories/raw/

**Wednesday:** Phase 2 (Normalize)  
- Launch repo-normalizer-agent
- Execute: Deduplicate → 880-900 repos

**Thursday-Friday:** Phase 3 (Enrich) — parallel processing  
- Launch repo-enricher-agent
- Execute: Collect deep metadata for all repos
- Progress: 50% by Friday end

### Week 2 (Sep 13-19): Phases 4-6

**Monday-Tuesday:** Phase 4 (Classify)  
- Launch repo-classifier-agent (Claude Agent)
- Execute: Map to Company Brain ontology
- Batches: 10 repos/batch × 90 batches = 8-12h

**Wednesday-Thursday:** Phase 5 (Score)  
- Launch repo-scorer-agent (Claude Agent)
- Execute: Score on 10 dimensions
- Batches: 5 repos/batch × 180 batches = 4-6h

**Friday:** Phase 6 (Disposition) + Human Review  
- Launch repo-disposition-agent (Claude Agent)
- Execute: ADOPT/INTEGRATE/FORK decisions
- Human review: Top 50 repos (AGT-001)

### Week 3 (Sep 20-26): Phases 7-8

**Monday:** Phase 7 (Neo4j Integration)  
- Launch repo-graph-agent
- Execute: Load 880+ repos → Neo4j
- Verify graph integrity

**Tuesday-Thursday:** Phase 8 (Adopt Pipeline)  
- Select top 5 CRITICAL repos
- Sandbox test (Docker on Mac Studio)
- Benchmark performance
- Security scan

**Friday:** Activate repo-monitor-agent (weekly autonomous)

### Week 4 (Sep 27-Oct 3): Phase 9

**Monday-Wednesday:** Awesome Lists Integration  
- Parse 27 categories
- Extract ~1,500 URLs
- Deduplicate against 904 starred

**Thursday-Friday:** Unified Registry  
- Merge: 904 starred + Awesome overlap + new repos
- Result: 1,200-1,500 repos mapped to Company Brain

---

## SUCCESS CRITERIA

✅ **Phase 1:** 904 repos ingested, raw data complete  
✅ **Phase 2:** 880-900 deduplicated repos, no duplicates  
✅ **Phase 3:** All repos enriched with deep metadata  
✅ **Phase 4:** All repos classified into 5+ dimensions  
✅ **Phase 5:** All repos scored 0-100, tier distribution healthy  
✅ **Phase 6:** All repos dispositioned, top 50 human-reviewed  
✅ **Phase 7:** All repos in Neo4j, relationships verified  
✅ **Phase 8:** 3-5 repos adopted, monitoring active  
✅ **Phase 9:** Awesome lists ingested, unified registry complete  

**Final State:** Repository Intelligence System operational, feeding Company Brain decision engine

---

## COST & TIMELINE

| Phase | Duration | Agent Cost (Est.) | Total Effort | Critical Path |
|-------|----------|---|---|---|
| 1-3 | Week 1 (3d) | $50 API calls | 8h | 8h (parallel) |
| 4-6 | Week 2 (5d) | $200 Claude tokens | 16h | 16h (sequential reasoning) |
| 7-8 | Week 3 (3d) | $50 Neo4j + Docker | 10h | 10h (parallel testing) |
| 9 | Week 4 (2d) | $100 parsing | 6h | 6h (Awesome parsing) |
| **Total** | **4 weeks** | **~$400** | **~40h** | **4 weeks critical** |

**Note:** Most work is parallel (agents run concurrently). Actual wall-clock time: 4 weeks with proper automation.

---

## RELATED DOCUMENTS

- [[REPOSITORY-INTELLIGENCE-SYSTEM]] — Architecture & phases
- [[DEVICE-STORAGE-TOPOLOGY]] — Storage paths for all outputs
- [[16-AGENTS]] — Agent control plane
- [[_REGISTRIES/EXTERNAL_CAPABILITY_UNIVERSE.yaml]] — Starting point (904 repos)
- [[OMNIROUTE-STATUS]] — Infrastructure available for testing

---

**Generated:** 2026-09-06  
**Authority:** CP-006 (Agent Control Plane) + CP-027 (Infrastructure)  
**Review:** AGT-001 (Venture PM), AGT-003 (Technical)
