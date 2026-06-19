# Free Claude Code Proxy Integration Plan

**Goal:** Integrate free-claude-code proxy into Worldwidebro OS for cost optimization, multi-provider routing, and local fallback

**Project:** Worldwidebro OS — Infrastructure Layer  
**Scope:** Agent backend, venture routing, local Ollama fallback  
**Created:** 2026-06-05

---

## Strategic Overview

Three parallel integration paths:
1. **Cost Optimization Layer** — Route all venture agent requests through proxy (reduce API spend)
2. **Multi-Provider Venture Backend** — Different ventures use different providers by complexity/budget
3. **Local Ollama Fallback** — Graceful degradation when hitting rate limits

---

## Parallel Blockers (Phase 0)

### Blocker A: Proxy Setup & Provider Registry
**Status:** `pending`  
**Deadline:** Day 1

- [ ] A.1: Clone free-claude-code repo to ~/Documents/claude-code-proxy/
- [ ] A.2: Extract provider list (17 providers) + capabilities matrix
- [ ] A.3: Create `PROVIDER-REGISTRY.json` with cost/latency/capabilities for each
- [ ] A.4: Document provider tiers (free: Ollama/llama.cpp, paid: Claude/DeepSeek, etc.)
- [ ] A.5: Set up local proxy server on port 8000 (or configurable)

### Blocker B: Venture Provider Mapping
**Status:** `pending`  
**Deadline:** Day 1-2

- [ ] B.1: Load ventures from Supabase (712 ventures)
- [ ] B.2: Classify ventures by complexity (MVP/alpha/prod)
- [ ] B.3: Create `ventures-provider-mapping.json` (venture_id → preferred_provider)
- [ ] B.4: Define routing rules (MVP→free Gemini, alpha→DeepSeek, prod→Claude)
- [ ] B.5: Build cost projection model (spend reduction %)

### Blocker C: Ollama Local Setup
**Status:** `pending`  
**Deadline:** Day 1

- [ ] C.1: Install/verify Ollama locally (llama2, mistral, neural-chat)
- [ ] C.2: Create Ollama model registry in config
- [ ] C.3: Configure fallback chain (fast→slow: neural-chat→mistral→llama2)
- [ ] C.4: Test latency & quality on sample requests
- [ ] C.5: Document model selection per venture type

---

## Phases

### Phase 1: Infrastructure Setup
**Status:** `pending`  
**Duration:** 1-2 days

#### 1A: Proxy Installation & Configuration
- [ ] 1A.1: Clone free-claude-code repo
- [ ] 1A.2: Review server.py, api/, providers/ structure
- [ ] 1A.3: Create `config/providers.json` from PROVIDER-REGISTRY
- [ ] 1A.4: Set up local proxy (test with curl)
- [ ] 1A.5: Verify routing works: request to proxy → different provider response

#### 1B: Venture Routing Engine
- [ ] 1B.1: Create Python script: `route_venture_request.py`
- [ ] 1B.2: Load ventures-provider-mapping.json
- [ ] 1B.3: Implement routing logic: venture_id + task_type → provider
- [ ] 1B.4: Add fallback chain (preferred → secondary → Ollama)
- [ ] 1B.5: Unit tests for routing (10+ test cases)

#### 1C: Ollama Integration
- [ ] 1C.1: Verify Ollama running locally
- [ ] 1C.2: Register models in proxy as provider
- [ ] 1C.3: Benchmark latency (baseline for fallback)
- [ ] 1C.4: Create model selection logic (venture type → best model)
- [ ] 1C.5: Test end-to-end: request → fallback to Ollama

**Files Created:**
- `claude-code-proxy/config/worldwidebro-providers.json` — Provider registry + costs
- `claude-code-proxy/config/ventures-routing.json` — venture_id → provider mapping
- `route_venture_request.py` — Routing engine
- `ollama-integration.py` — Local fallback logic

---

### Phase 2: Agent Backend Integration
**Status:** `pending`  
**Duration:** 1-2 days

#### 2A: Claude Code CLI Integration
- [ ] 2A.1: Point Claude Code to local proxy (config/settings.json)
- [ ] 2A.2: Test: `claude-code` commands route through proxy
- [ ] 2A.3: Verify thinking blocks + tool use still work
- [ ] 2A.4: Document setup for future agents

#### 2B: Venture Agent Wiring
- [ ] 2B.1: Update agent spawn logic to use proxy
- [ ] 2B.2: Pass venture_id in request → gets routed to correct provider
- [ ] 2B.3: Log routing decisions (vendor, cost, latency)
- [ ] 2B.4: Test with 5 sample ventures (different tiers)

#### 2C: Cost Tracking Dashboard
- [ ] 2C.1: Create `cost-tracking.py` (polls proxy logs)
- [ ] 2C.2: Extract: provider, latency, cost per request
- [ ] 2C.3: Aggregate by venture/sector
- [ ] 2C.4: Dashboard file: `CLAUDE-CODE-PROXY-METRICS.md` (real-time)

**Files Created:**
- `agent-routing-config.json` — Agent backend settings
- `cost-tracking.py` — Metrics collection
- `CLAUDE-CODE-PROXY-METRICS.md` — Live dashboard

---

### Phase 3: Multi-Provider Routing Optimization
**Status:** `pending`  
**Duration:** 2-3 days

#### 3A: Provider Quality/Cost Matrix
- [ ] 3A.1: Benchmark each provider (10 sample prompts)
- [ ] 3A.2: Grade output quality (1-5 scale)
- [ ] 3A.3: Measure latency (p50, p95, p99)
- [ ] 3A.4: Record cost per request
- [ ] 3A.5: Create `PROVIDER-PERFORMANCE-MATRIX.md`

#### 3B: Dynamic Routing Rules
- [ ] 3B.1: Load performance matrix
- [ ] 3B.2: Implement scoring: quality × (1 - cost_factor) × (1 - latency_factor)
- [ ] 3B.3: Select best provider for request type (code gen, analysis, planning)
- [ ] 3B.4: A/B test: static routing vs. dynamic
- [ ] 3B.5: Update ventures-routing.json with optimal assignments

#### 3C: Request-Type Specialization
- [ ] 3C.1: Classify requests (code_gen, analysis, planning, refactor)
- [ ] 3C.2: Create provider affinity map (type → best_provider)
- [ ] 3C.3: Override venture-level routing based on request type
- [ ] 3C.4: Test: complex request → specialized provider

**Files Created:**
- `PROVIDER-PERFORMANCE-MATRIX.md` — Benchmarks
- `dynamic-routing.py` — Smart provider selection
- `request-type-routing.json` — Type → provider affinity

---

### Phase 4: Cost Optimization & Budget Controls
**Status:** `pending`  
**Duration:** 1-2 days

#### 4A: Spend Analysis
- [ ] 4A.1: Current spending (Anthropic API baseline)
- [ ] 4A.2: Project spending with proxy (free providers prioritized)
- [ ] 4A.3: Calculate ROI by venture (high-spend ventures save most)
- [ ] 4A.4: Create `SPEND-ANALYSIS.md`

#### 4B: Budget Guardrails
- [ ] 4B.1: Set monthly budget cap per venture
- [ ] 4B.2: Implement rate limiting (requests/min per venture)
- [ ] 4B.3: Alert when venture approaches budget
- [ ] 4B.4: Graceful degradation (drop to cheaper provider or Ollama)

#### 4C: Cost Reporting
- [ ] 4C.1: Daily cost report (venture, provider, requests, spend)
- [ ] 4C.2: Monthly savings projection
- [ ] 4C.3: Dashboard integration (Grafana or markdown)

**Files Created:**
- `budget-guardrails.py` — Spend enforcement
- `SPEND-ANALYSIS.md` — ROI & projections
- `cost-report-daily.py` — Reporting

---

### Phase 5: Testing & Validation
**Status:** `pending`  
**Duration:** 2-3 days

#### 5A: Integration Tests
- [ ] 5A.1: End-to-end: venture request → correct provider → response
- [ ] 5A.2: Fallback chain: primary provider down → secondary → Ollama
- [ ] 5A.3: Cost tracking accuracy (reported vs. actual)
- [ ] 5A.4: Routing decision logging (audit trail)
- [ ] 5A.5: 50+ integration test cases

#### 5B: Performance Tests
- [ ] 5B.1: Latency: proxy adds <50ms overhead
- [ ] 5B.2: Throughput: proxy handles 100+ concurrent requests
- [ ] 5B.3: Ollama fallback: graceful under load
- [ ] 5B.4: Cost: verify savings vs. baseline

#### 5C: Chaos Tests
- [ ] 5C.1: Provider outage simulation (forced fallback)
- [ ] 5C.2: Rate limit handling (backoff + retry)
- [ ] 5C.3: Ollama OOM/crash (switch to other models)
- [ ] 5C.4: Network partition (timeout + fallback)

**Files Created:**
- `tests/integration_tests.py` (50+ tests)
- `tests/performance_tests.py`
- `tests/chaos_tests.py`
- `TEST-RESULTS.md` — Full report

---

### Phase 6: Documentation & Deployment
**Status:** `pending`  
**Duration:** 1 day

- [ ] 6.1: Create `CLAUDE-CODE-PROXY-README.md` (setup, config, operations)
- [ ] 6.2: Document provider matrix (when to use each)
- [ ] 6.3: Venture routing guide (how to assign providers)
- [ ] 6.4: Cost monitoring playbook
- [ ] 6.5: Fallback troubleshooting guide
- [ ] 6.6: Create `/agents/claude-code-proxy.md` skill documentation

---

## Phase Completion Summary

| Phase | Status | Key Deliverable | Deadline |
|-------|--------|-----------------|----------|
| 0. Parallel Blockers | ⏳ Pending | Provider registry + venture mapping + Ollama | Day 1 |
| 1. Infrastructure | ⏳ Pending | Proxy running locally + routing engine | Day 1-2 |
| 2. Agent Integration | ⏳ Pending | Claude Code → proxy wired + metrics | Day 2-3 |
| 3. Optimization | ⏳ Pending | Dynamic routing + provider scoring | Day 3-5 |
| 4. Cost Controls | ⏳ Pending | Budget guardrails + spend reporting | Day 5-6 |
| 5. Testing | ⏳ Pending | 50+ tests + performance benchmarks | Day 6-8 |
| 6. Documentation | ⏳ Pending | Setup guides + operational playbooks | Day 8-9 |

---

## Critical Files to Create

```
claude-code-proxy/
├── config/
│   ├── worldwidebro-providers.json      # Provider registry + costs
│   ├── ventures-routing.json            # venture_id → provider
│   └── ollama-integration.json          # Local model config
├── route_venture_request.py             # Routing engine
├── cost-tracking.py                     # Metrics collection
├── dynamic-routing.py                   # Smart provider selection
├── budget-guardrails.py                 # Spend enforcement
├── tests/
│   ├── integration_tests.py
│   ├── performance_tests.py
│   └── chaos_tests.py
└── docs/
    ├── CLAUDE-CODE-PROXY-README.md
    ├── PROVIDER-REGISTRY.md
    ├── PROVIDER-PERFORMANCE-MATRIX.md
    ├── SPEND-ANALYSIS.md
    └── VENTURE-ROUTING-GUIDE.md
```

---

## Errors Encountered

| Error | Attempt | Resolution |
|-------|---------|------------|
| — | — | — |

---

## Decisions

| Decision | Rationale |
|----------|-----------|
| Proxy on localhost:8000 | Local control, no external calls for routing |
| Venture_id-based routing | Enables per-venture cost optimization |
| Ollama as primary fallback | No dependency on external providers, fast local inference |
| Dynamic routing phase (Phase 3) | Requires benchmarks first; static routing simpler to test |
| Test-heavy (Phase 5) | Multi-provider routing has edge cases; chaos tests reveal failures early |

---

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Provider API rate limits | Venture blocked | Implement queue + backoff; fallback to Ollama |
| Ollama model size | Disk space | Keep models small (7B-13B); lazy load |
| Routing decision latency | Slow requests | Cache routing decisions (venture_id → provider) |
| Cost overruns | Budget exceeded | Implement spending guardrails (Phase 4) |
| Provider data breach | PHI leakage | Use local Ollama for sensitive requests |

---

## Success Metrics

- [ ] **Cost reduction:** ≥50% lower API spend vs. baseline (Claude only)
- [ ] **Availability:** Fallback success rate ≥99%
- [ ] **Latency:** Proxy adds <50ms overhead
- [ ] **Accuracy:** Routing decisions correct for 95%+ requests
- [ ] **Observability:** All routing decisions logged + auditable
