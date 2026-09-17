# Repo Installation Order (928 Starred Repos → Ventures)

**Strategy:** Layer-first, then venture-specific, then optional enhancements  
**Timeline:** Parallel installation across 3 phases  
**Goal:** Unblock execution, close gaps, then optimize

---

## PHASE 0: FOUNDATION (Week 1 — P0/P1 Repos)

### Layer 4: Loop Engineering (MUST HAVE FIRST)
**Why:** Orchestration foundation. Everything depends on this.

| Repo | Stars | Priority | Ventures | Action |
|------|-------|----------|----------|--------|
| **hermes-agent** | 246K | CRITICAL | All | Study architecture, use as reference |
| **n8n** | 204K | CRITICAL | OPS-001, LT-005, CALLCENTER | Deploy to Vercel, wire MCP |
| **agency-agents** | 153K | CRITICAL | CON-001, RE-001 | Reference for multi-agent patterns |
| **langgraph** | 41K | HIGH | All agents | Use for execution graphs (L1/L2/L3) |
| **hello-agents** | 79K | HIGH | Training/reference | Microsoft tutorial for best practices |

**Installation steps:**
```bash
# Day 1: n8n deployment
npm install n8n
docker run -d -p 5678:5678 n8n/n8n
# Wire Supabase + OmniRoute + 110 tools
# Test: Run 1 workflow (simple state transition)

# Day 2: langgraph integration
pip install langgraph
# Create L1/L2/L3 loop templates
# Wire to agents in Neo4j

# Day 3: agency-agents reference
# Study multi-agent orchestration
# Document patterns for Company Brain
```

**Unblocks:** OPS-001 (cold call workflow), LT-005 (dispatch loop), CALLCENTER (IVR workflow)

---

### Layer 6: Eval Engineering (CRITICAL GAP)
**Why:** Can't certify agents without evals. Do this NOW.

| Repo | Stars | Priority | Ventures | Action |
|------|-------|----------|----------|--------|
| **deepeval** | 18K | CRITICAL | All agents | Install + wire LangSmith |

**Installation steps:**
```bash
# Day 1-2: deepeval setup
pip install deepeval
# Create eval harnesses for each agent type
# Wire to evaluation_runs table (PostgreSQL)

# Wire LangSmith API
export LANGSMITH_API_KEY=<from Bitwarden>
# Create evaluator config per agent

# Test: Run 5 evals on 310 agents (sample)
# Measure: baseline pass_rate for each agent
```

**Unblocks:** Agent certification system, readiness scoring (7 dimensions)

---

## PHASE 1: SUPPORT LAYERS (Week 2 — P2 Repos)

### Layer 5: Graph Engineering
**Why:** Agents need to query what they know (Neo4j foundation + vector search).

| Repo | Stars | Priority | Ventures | Action |
|------|-------|----------|----------|--------|
| **graphify** | 118K | HIGH | All | Codebase → knowledge graph |
| **langgraph** (already installed) | 41K | HIGH | All agents | Execution graphs + state |
| **qdrant** | 34K | HIGH | All | Vector search (embeddings) |
| **neo4j** | 17K | REFERENCE | — | OSS reference (we use SaaS) |

**Installation steps:**
```bash
# Day 1: graphify for codebase indexing
pip install graphify-ai
# Index all 887 owned repos
# Create "Codebase Graph" node in Neo4j

# Day 2: qdrant integration
# Already running (docker on Mac Studio)
# Test: Index 1K documents, search latency
# Benchmark: avg search time < 100ms

# Test: Query path
# Agent asks: "What repos depend on FastMCP?"
# Neo4j returns: path graph
```

**Unblocks:** Agent context assembly, dependency queries, codebase search

---

### Layer 3: Tool Engineering
**Why:** Agents need a discoverable tool catalog.

| Repo | Stars | Priority | Ventures | Action |
|------|-------|----------|----------|--------|
| **awesome-mcp-servers** | 95K | HIGH | All | MCP discovery index |
| **fastmcp** | 27K | HIGH | OPS-001, CALLCENTER | Use to build new MCPs |
| **ToolJet** | 41K | MEDIUM | RE-001 | No-code tool builder (optional) |
| **n8n-mcp** (ref) | 22K | REFERENCE | — | n8n ↔ MCP bridge pattern |

**Installation steps:**
```bash
# Day 1: awesome-mcp-servers
# Sync registry to Neo4j
# Create Tool nodes: 110 tools + 200 MCPs
# Wire permissions per agent

# Day 2: fastmcp framework
# Build 2 custom MCPs for OPS-001
# (cold call manager + spreadsheet writer)

# Test: OmniRoute can route to 110 tools
# Measure: tool selection latency < 50ms
```

**Unblocks:** Tool discovery for agents, tool permissions, OmniRoute optimization

---

### Layer 2: Context Engineering
**Why:** Agents need context assembly (RAG + knowledge retrieval).

| Repo | Stars | Priority | Ventures | Action |
|------|-------|----------|----------|--------|
| **llama_index** | 52K | HIGH | All | RAG orchestration |
| **LightRAG** | 39K | HIGH | All | Graph-based RAG |
| **langchainjs** | 18K | MEDIUM | Web agents | JS RAG implementation |

**Installation steps:**
```bash
# Day 1: llama_index
pip install llama-index
# Create context retrievers per venture
# Test: Q&A latency < 2s

# Day 2: LightRAG
# Build graph-aware RAG
# Index: repos, ventures, financials, agent metadata
# Query: "Which repos are needed for Eval Engineering?"
# Response: Shows 4 repos + relevance scores

# Test: Hybrid retrieval (BM25 + vector)
```

**Unblocks:** Smart context for agents, venture-specific retrieval, semantic search

---

## PHASE 2: OPTIONAL/NICE-TO-HAVE (Week 3+)

### Layer 7: Harness Engineering
**Why:** Observability + monitoring. Deploy AFTER agents are stable.

| Repo | Stars | Priority | Ventures | Action |
|------|-------|----------|----------|--------|
| **sentry** | 44K | MEDIUM | All agents | Error tracking |
| **openobserve** | 22K | MEDIUM | All | Logs + traces |
| **opentelemetry** | 7K | MEDIUM | — | Instrumentation std |
| **OpenSandbox** | 15K | LOW | Advanced agents | Sandbox runtime |

**Installation:** Deploy Week 3+ (after Loop + Eval are solid)

---

### Layer 1: Prompt Engineering
**Why:** Nice templates, but lower priority than execution.

| Repo | Stars | Priority | Ventures | Action |
|------|-------|----------|----------|--------|
| **prompts.chat** | 170K | LOW | Reference | Prompt marketplace |
| **Prompt-Engineering-Guide** | 78K | LOW | Training | dair-ai guide |

**Installation:** Week 4+ (after eval baselines are set)

---

## VENTURE-SPECIFIC INSTALLATION MAP

### Tier 0 Revenue Ventures

**OPS-001 (Staffing Placements)**
```
Week 1:
  ✅ n8n (workflow orchestration)
  ✅ fastmcp (custom MCPs: call manager, spreadsheet)
  ✅ deepeval (eval for cold-call success rate)

Week 2:
  ✅ llama_index (context retrieval: company profiles)
  ✅ langgraph (L2 supervised loop: operator approval gate)

Week 3+:
  ✅ sentry (error tracking for call failures)
```

**LT-005 (Medical Logistics)**
```
Week 1:
  ✅ n8n (dispatch workflow)
  ✅ deepeval (on-time delivery evals)

Week 2:
  ✅ LightRAG (facility knowledge graph)
  ✅ langgraph (L2 supervised: route optimization)

Week 3+:
  ✅ openobserve (delivery tracking logs)
```

**CALLCENTER (Twilio Integration)**
```
Week 1:
  ✅ n8n (IVR workflow)
  ✅ fastmcp (Twilio MCP)
  ✅ deepeval (call quality evals)

Week 2:
  ✅ llama_index (customer context retrieval)
  ✅ langgraph (L1 report-only for escalations)

Week 3+:
  ✅ sentry (call failure tracking)
```

**CON-001 (Construction)**
```
Week 2: (needs assessment first)
  ✅ agency-agents (multi-agent coordination)
  ✅ langgraph (project workflow)

Week 3+:
  ✅ LightRAG (project knowledge graph)
```

**RE-001 (Real Estate)**
```
Week 2: (needs assessment first)
  ✅ hermes-agent (reference architecture)
  ✅ n8n (deal workflow)

Week 3+:
  ✅ qdrant (property vector search)
  ✅ LightRAG (deal analysis graphs)
```

---

## INSTALLATION CHECKLIST (By Week)

### Week 1 (Sep 17-22)
- [ ] **n8n** deployment (Vercel)
- [ ] **deepeval** + LangSmith API key
- [ ] **langgraph** L1/L2/L3 templates
- [ ] Test: Run 1 OPS-001 cold call workflow
- [ ] Test: Run 5 evals on sample agents

### Week 2 (Sep 23-29)
- [ ] **graphify** codebase indexing
- [ ] **qdrant** benchmark (latency, recall)
- [ ] **llama_index** + **LightRAG** RAG setup
- [ ] **awesome-mcp-servers** registry sync
- [ ] Test: Cross-venture query ("which repo solves gap X?")

### Week 3+ (Oct 1+)
- [ ] **sentry** error tracking
- [ ] **openobserve** logs + traces
- [ ] **ToolJet** for RE-001 (optional)
- [ ] Performance optimization per venture

---

## PARALLEL INSTALLATION (Fast Path)

**Can do in parallel (Week 1):**
```
Thread 1: n8n deployment
Thread 2: deepeval harnesses
Thread 3: langgraph templates (L1/L2/L3)
Thread 4: Study hermes-agent + agency-agents (reference)
```

**Can do in parallel (Week 2):**
```
Thread 1: graphify indexing
Thread 2: qdrant benchmarking
Thread 3: llama_index + LightRAG setup
Thread 4: awesome-mcp registry sync
```

---

## Success Metrics (Installation Complete When)

✅ All **Loop** repos wired (n8n, langgraph running on all Tier-0 ventures)  
✅ All **Eval** repos wired (deepeval evals passing 70%+ baseline on 310 agents)  
✅ All **Graph** repos connected (Neo4j + Qdrant querying working < 100ms)  
✅ All **Tool** repos indexed (awesome-mcp available to agents, OmniRoute < 50ms)  
✅ All **Context** repos live (RAG queries < 2s, hybrid search working)  
✅ **Harness** repos optional (error tracking + observability nice-to-have)  
✅ **Prompt** repos optional (template library reference only)  

---

## Total Installation Cost

| Layer | Repos | Effort | Timeline |
|-------|-------|--------|----------|
| Loop | 5 | 8h | Week 1 |
| Eval | 1 | 4h | Week 1 |
| Graph | 4 | 6h | Week 2 |
| Tool | 4 | 4h | Week 2 |
| Context | 3 | 5h | Week 2 |
| Harness | 4 | 4h | Week 3 |
| Prompt | 2 | 2h | Week 3 |
| **TOTAL** | **23** | **33h** | **3 weeks** |

**Parallel efficiency:** 33h → ~20h calendar time (2.5 dev weeks, 1 QA week)

---

## What NOT to Install

❌ ToolJet (optional, low priority)  
❌ OpenSandbox (advanced, not needed for MVP)  
❌ Prompt template libraries (reference only, don't install)  
❌ neo4j OSS (we use SaaS already)  

---

## What Happens After Installation

1. **Ventures pick repos from Neo4j discovery**
2. **Agents query "which repos solve my gap?"**
3. **System auto-recommends tools + wires permissions**
4. **Evals baseline each agent on new tools**
5. **Graduation:** Agent can use tool → move from L1 to L2

**Result:** 928 repos transformed from "nice to have" → "operational assets"

