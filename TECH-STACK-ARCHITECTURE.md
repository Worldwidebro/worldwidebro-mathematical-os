# Tech Stack Architecture — Tools → Layers → OPCOs → Ventures

**Status:** Audit of current tool usage vs optimal configuration

---

## Tool Responsibility Matrix (Current)

| Tool | Layer | Responsibility | Status | OPCOs Using | Readiness |
|------|-------|-----------------|--------|------------|-----------|
| **LiteLLM** | Intelligence | Model routing + fallback | ✅ Running | All | 90%+ |
| **Ollama** | Intelligence | Local inference (qwen2.5:32b) | ✅ Running (Mac Studio) | All | 85% |
| **Neo4j** | Knowledge Graph | Venture/agent/capability graph | ✅ Container | All | 80% |
| **Qdrant** | Semantic Memory | Vector embeddings (repos, notes) | ✅ Container | All | 85% |
| **PostgreSQL** | Records | Supabase + T7 native | ✅ Running | All | 95%+ |
| **Langfuse** | Observability | LLM tracing | ✅ Container (fixed 07/13) | All | 70% (no app instrumentation) |
| **Prometheus** | Observability | Metrics collection | ✅ Container | All | 40% (only self-scraping) |
| **Grafana** | Visualization | Dashboards | ✅ Container | All | 30% (login broken) |
| **n8n** | Automation | Workflow orchestration | ✅ Mac Studio | CON, STA | 80% |
| **CrewAI** | Agent Orchestration | Multi-agent workflows | ⏳ Not integrated | All | 0% |
| **RepoMix** | Context Packaging | AI context generation | ⏳ Available | All | 0% |
| **Graphify** | Repository Graph | Repo dependency mapping | ✅ Available | All | 60% |
| **SocratiCode** | Impact Analysis | Code change impact | ✅ MCP available | All | 50% |
| **Stirling PDF** | Document Processing | PDF → markdown | ⏳ Available | All | 0% |
| **Public APIs** | Service Discovery | External service lookup | ✅ Available | All | 0% |
| **Warp** | Terminal | Fast shell | ✅ Installed | All | 100% |
| **tmux** | Session Management | Terminal multiplexing | ✅ Installed | All | 80% |

---

## 16-Layer Company Brain OS → Tools Mapping

```
Layer 0: Being (Soul, Identity)
  └─ Tools: None yet (needs wisdom capture)

Layer 1: Mind (Knowledge, Understanding, Wisdom)
  └─ Tools: Neo4j (knowledge graph), Qdrant (semantic memory), Obsidian (capture)

Layer 2: Trivium (Grammar, Logic, Rhetoric)
  └─ Tools: Stirling PDF (grammar/extraction), SocratiCode (logic analysis), RepoMix (rhetoric)

Layer 3: Quadrivium (Arithmetic, Geometry, Music, Astronomy)
  └─ Tools: PostgreSQL (arithmetic/data), Neo4j (geometry/relationships), LiteLLM (patterns)

Layer 4: Creation (Writing, Design, Engineering)
  └─ Tools: Graphify (engineering visualization), LiteLLM (generation), Ollama (local creation)

Layer 5: Society (Economics, Business, Finance, Law, Politics, HR)
  └─ Tools: PostgreSQL (ERP records), n8n (business workflows), Neo4j (org structure)

Layer 6: Civilization (Ethics, Governance, Culture, Long-term)
  └─ Tools: Langfuse (audit trail), Prometheus (measurement), Grafana (transparency)

Layer 7: Infrastructure (Data Layer)
  └─ Tools: PostgreSQL, Qdrant, Neo4j, MinIO

Layer 8: Automation (Workflow Layer)
  └─ Tools: n8n, CrewAI (pending), Langfuse

Layer 9: Intelligence (LLM Layer)
  └─ Tools: LiteLLM, Ollama, Colibri (pending)

Layer 10: Observability (Monitoring Layer)
  └─ Tools: Langfuse, Prometheus, Grafana, Warp

Layer 11: Agency (Agent Layer)
  └─ Tools: CrewAI (pending), n8n, LiteLLM routing

Layer 12: Integration (External Services)
  └─ Tools: Public APIs, Stirling PDF, RepoMix

Layer 13: Context (Knowledge Retrieval)
  └─ Tools: Qdrant, Neo4j, RepoMix, Graphify

Layer 14: Learning (Continuous Improvement)
  └─ Tools: Langfuse (feedback loops), Prometheus (metrics)

Layer 15: Measurement (KPIs, Success Metrics)
  └─ Tools: Prometheus, Grafana, PostgreSQL (query), Langfuse (cost/token tracking)
```

---

## OPCO → Tool Dependencies

| OPCO | Critical Tools | In Use | Missing | Readiness |
|------|-----------------|--------|---------|-----------|
| **CON** | LiteLLM, Ollama, Neo4j, PostgreSQL, n8n | 5/5 | — | 95% |
| **STA** | LiteLLM, Qdrant, PostgreSQL, n8n | 4/5 | Neo4j candidate matching | 80% |
| **RE** | LiteLLM, Qdrant (similarity), PostgreSQL | 3/5 | n8n workflows, Neo4j | 70% |
| **EDU** | LiteLLM, Ollama, Neo4j (course graph), PostgreSQL | 4/5 | Stirling PDF (content atomization) | 80% |
| **FIN** | PostgreSQL, Neo4j (risk graph), Prometheus | 3/5 | LiteLLM (risk calc), Langfuse (audit) | 75% |
| **LOG** | LiteLLM, Neo4j (routes), PostgreSQL, Qdrant | 4/5 | n8n (optimization workflows) | 80% |
| **IZA OS** | All (infrastructure) | 12/15 | CrewAI, Colibri | 85% |

---

## Integration Gaps (Blocking Full Potential)

| Gap | Impact | Fix | Effort | Priority |
|-----|--------|-----|--------|----------|
| CrewAI not wired to agents | Agents can't coordinate | Create agent-team supervisor | 4h | TIER 1 |
| Langfuse no app instrumentation | Observability blind | Add instrumentation to 4 live CON agents | 2h | TIER 1 |
| Grafana login broken | Can't see dashboards | Reset admin password via docker | 0.5h | TIER 1 |
| Prometheus only scraping itself | No real metrics | Add otel-collector + service targets to prometheus.yml | 1h | TIER 2 |
| n8n not on Mac Studio → Air sync | Workflows siloed | Wire Tailscale + PostgreSQL replication | 2h | TIER 2 |
| Stirling PDF not integrated | No document ingestion | Create PDF → markdown workflow in n8n | 2h | TIER 2 |
| RepoMix not used for context | Context generation manual | Integrate into agent preamble | 1h | TIER 2 |
| exo (distributed inference) idle | GPU not shared | Activate Mac Studio GPU → MacBook Air | 3h | TIER 3 |

---

## What's Working Well

✅ **PostgreSQL** — All transactional data (ventures, contacts, products, decisions)  
✅ **Neo4j** — 2,273 IMPLEMENTS edges (repo→capability), 6,542 NEEDS edges (venture→capability)  
✅ **Qdrant** — 1,648 repo vectors, 15,558 note vectors (Ollama nomic-embed)  
✅ **LiteLLM** — Routing qwen2.5:32b on Mac Studio, fallback to Claude API  
✅ **Ollama** — 5 models loaded on Mac Studio (qwen2.5:32b, qwen3:8b, nomic-embed-text, kimi, minimax)  
✅ **n8n** — 3 Zapier zaps replacing complex workflows (form→task, app→CRM, payment→invoice)  
✅ **Langfuse** — Fixed 07/13, now captures traces (no apps instrumented yet)  

---

## What's Half-Baked

⚠️ **Grafana** — Dashboards defined but login broken (credentials unknown)  
⚠️ **Prometheus** — Running but only self-scraping; otel-collector not in targets  
⚠️ **SocratiCode** — MCP available but not integrated into code review workflow  
⚠️ **Graphify** — Repo graph generation works but not fed to Neo4j or visualized  
⚠️ **RepoMix** — Context packaging available but not used in agent preambles  

---

## What's Missing (But Tools Exist)

❌ **CrewAI integration** — Multi-agent orchestration (tool exists, not wired)  
❌ **Colibri integration** — High-performance inference (tool exists, not wired)  
❌ **exo clustering** — Distributed inference (installed on Mac Studio, not running)  
❌ **Stirling PDF** — Document processing (not in any workflow)  
❌ **Public APIs** — External service discovery (no integration)  

---

## Next: Create Interactive Tech Stack Diagram

Should show:
1. **Clickable layers** (Being → Civilization)
2. **Expandable tool nodes** (LiteLLM → shows model routing, latency, cost)
3. **OPCO dependencies** (click CON → shows which tools it uses)
4. **Status indicators** (green = ready, yellow = partial, red = missing)
5. **Phase assignments** (TIER 1 = do this week, TIER 2 = next 2 weeks, TIER 3 = month)

