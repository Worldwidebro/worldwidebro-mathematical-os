# 30-Day Sprint: AI Boss OS Core Platform Foundation

**Date:** 2026-07-20  
**Sprint Length:** 30 days (2026-07-21 to 2026-08-20)  
**Objective:** Complete the foundational AI Boss OS that 712 ventures inherit  
**Exit Criteria:** Core platform documented, bootstraps from one command, knowledge + AI + venture factory operational

---

## Strategic Rationale

**NOT:** Optimize for "build 3 sectors quickly" (vendor-first)  
**YES:** Optimize for "build the OS foundation that will scale to 712 ventures" (platform-first)

Every venture built after Day 30 will inherit:
- Unified architecture
- Shared knowledge platform
- AI agent infrastructure
- Governance + permissions
- Observability + dashboards
- Venture factory templates

This prevents 712 ventures from being 712 custom implementations. Build once. Inherit 712 times.

---

## Week 1 — Foundation & Architecture (Days 1-7)

**Goal:** Define the platform before writing more code.

### Deliverables (7 markdown files)

1. **OPERATING-SYSTEM.md**
   - 4 layers: Foundation (Neo4j, Qdrant, Supabase) → Intelligence (LLMs, routing) → Automation (n8n, agents) → Execution (ventures)
   - 15 subsystems (payments, auth, logging, etc.)
   - Dependency graph (what depends on what)
   - Example: Finance ventures depend on Supabase (ledger) + Neo4j (risk graph) + Hermes (decisions)

2. **ARCHITECTURE.md**
   - C4 diagrams (Context, Container, Component, Code level)
   - System boundaries
   - Integration points
   - Deployment topology

3. **SYSTEM-LAYERS.md**
   - Layer 0: Legal Entity (Worldwidebro Holdings)
   - Layer 1: Infrastructure OS (IZA OS)
   - Layer 2: Operations (6 OPCOs)
   - Layer 3: Ventures (712 units)
   - Layer 4: Products (revenue-generating)

4. **DEPENDENCY-GRAPH.md**
   - Which systems depend on which
   - Build order (what must exist first)
   - Fallback paths (if X fails, use Y)
   - Example: CON ventures need Supabase before n8n workflows

5. **GOVERNANCE.md**
   - Decision authority model (Hermes routing <$5K → director → human)
   - Risk boundaries
   - Compliance requirements
   - Change control process

6. **REPOSITORY-STANDARDS.md**
   - Folder structure (all ventures inherit this)
   - Naming conventions (CON-001, STA-050, etc.)
   - File ownership (who can edit what)
   - Code review process

7. **BUILD-ORDER.md**
   - Sequential steps to stand up the platform
   - Infrastructure first (databases, auth)
   - Knowledge next (indexing, search)
   - AI next (agents, workflows)
   - Ventures last (spawn from template)

### Success Criteria (Day 7)
- ✅ Architecture approved and documented
- ✅ Dependency graph complete (no circular dependencies)
- ✅ Build order verified (each layer independent until integrated)
- ✅ Governance model defined
- ✅ New developers can understand the system from docs alone

### Time Budget
- Architecture: 12 hours
- Diagrams + documentation: 8 hours
- Review + iteration: 4 hours
- **Total: 24 hours across 7 days**

---

## Week 2 — Knowledge Platform (Days 8-14)

**Goal:** Build the organization's shared knowledge layer that all agents can search.

### Deliverables (13 markdown files + infrastructure)

**Documentation Files:**
1. **KNOWLEDGE-ARCHITECTURE.md** — Layers, ingestion pipeline, search interface
2. **KNOWLEDGE-GRAPH.md** — Neo4j schema (Ventures, Repos, Capabilities, Teams, Decisions)
3. **INGESTION.md** — How data enters the system (GitHub, Supabase, manual)
4. **INDEXING.md** — How documents are vectorized and stored (Qdrant)
5. **SEARCH.md** — Query patterns (semantic, keyword, faceted)
6. **MEMORY.md** — Agent memory layer (Qdrant collections per agent type)
7. **SYNCHRONIZATION.md** — How to keep 3 data sources in sync (GitHub → Neo4j → Qdrant)

**Infrastructure Setup:**

| System | Task | Owner | Status |
|--------|------|-------|--------|
| **Neo4j** | Load org hierarchy + venture registry | You | ⏳ |
| **Qdrant** | Index 1,639 repos + README corpus | You | ⏳ |
| **Graphify** | Map repo dependencies | You | ⏳ |
| **Gittodoc** | Extract documentation from 50 key repos | You | ⏳ |
| **LightRAG** | Enable multimodal knowledge (PDF, images, tables) | You | ⏳ |
| **Repository Indexing** | Create search API | You | ⏳ |

### Success Criteria (Day 14)
- ✅ Neo4j loaded with 712 ventures + org hierarchy
- ✅ Qdrant indexed with all 1,639 repos (semantic vectors)
- ✅ Agents can query "find repos that support staffing" → get top 10 matches
- ✅ Agents can query "what risks exist for CON-001?" → get Neo4j subgraph
- ✅ Search API exposed (agents can call it, get results in <1s)

### Time Budget
- Documentation: 8 hours
- Neo4j schema + load: 12 hours
- Qdrant indexing: 12 hours
- Integration + testing: 12 hours
- **Total: 44 hours across 7 days**

### Code Baseline (Reuse Existing)
- `populate_venture_knowledge_graph.py` (445 lines) — already exists
- `build_repo_rag.py` — already exists
- Neo4j Cypher queries — write 10 canonical ones

---

## Week 3 — AI Platform (Days 15-21)

**Goal:** Create the reusable AI platform that agents can discover tools, models, prompts, and workflows.

### Deliverables (11 markdown files + registry files)

**Documentation:**
1. **AGENT-REGISTRY.md** — How agents self-register, discover roles
2. **MODEL-REGISTRY.md** — Available LLMs (Opus, Sonnet, Haiku, local Ollama)
3. **PROMPT-REGISTRY.md** — Canonical prompts (CEO, CTO, CFO personas)
4. **TOOL-REGISTRY.md** — All tools (Stripe, Slack, n8n, GitHub, etc.)
5. **WORKFLOW-REGISTRY.md** — Reusable workflows (outreach, matching, approval)
6. **CAPABILITY-REGISTRY.md** — What each venture needs (25 canonical capabilities)
7. **MCP-REGISTRY.md** — All MCPs (servers) + connection strings
8. **CONTEXT.md** — Context optimization (Headroom + token budgeting)
9. **MEMORY.md** — Agent memory persistence (which data goes in long-term memory)
10. **POLICY.md** — What agents can/cannot do (agent policies in code)
11. **PERMISSIONS.md** — Role-based access (CEO can approve >$25K, CTO can't)

**Registry Files (JSON/YAML):**
```
registries/
  agent_registry.yaml          # All agent types + roles
  model_registry.json          # Models + endpoints
  prompt_registry.json         # Canonical prompts
  tool_registry.json           # All tools + MCP servers
  workflow_registry.json       # Reusable workflows
  capability_registry.json     # 25 capabilities
  mcp_registry.json            # All MCPs + configs
  policy_engine.yaml           # What agents can do
```

### Success Criteria (Day 21)
- ✅ Agent can query tool registry → find all Stripe-connected tools
- ✅ Agent can query capability registry → find which repos support "payment processing"
- ✅ Agent can query workflow registry → fetch "approval workflow" and run it
- ✅ New MCP can be registered in 2 lines (added to mcp_registry.json)
- ✅ New prompt can be added in 1 line (added to prompt_registry.json)
- ✅ Policies are enforced (e.g., only AG-CEO can approve >$25K)

### Time Budget
- Documentation: 12 hours
- Registry files: 16 hours
- Policy engine integration: 12 hours
- Testing + iteration: 8 hours
- **Total: 48 hours across 7 days**

### Code Baseline (Reuse/Build)
- `agent_factory.py` (160 lines) — loads registries
- `hermes.py` (95 lines) — enforces policies
- New: Registry loaders + API (100 lines)

---

## Week 4 — Venture Factory (Days 22-30)

**Goal:** Make it possible to launch a new venture from a template in <5 minutes.

### Deliverables (9 markdown files + factory code)

**Documentation:**
1. **VENTURE-FACTORY.md** — How to spawn a venture
2. **VENTURE-TEMPLATE.md** — What every venture inherits (structure, agents, dashboards)
3. **INDUSTRY-TEMPLATES.md** — Construction, Staffing, Real Estate templates (pre-wired)
4. **SHARED-SERVICES.md** — Payment, auth, CRM, analytics (all ventures use these)
5. **PROVISIONING.md** — What gets created (folder, database schema, agent registry, dashboard)
6. **DEPLOYMENT.md** — How ventures are deployed (Vercel, Supabase projects, n8n workflows)
7. **AUTOMATION.md** — How tasks are executed (agent orchestration, approval flows)
8. **UPGRADES.md** — How to update all 712 ventures in parallel
9. **LIFECYCLE.md** — Venture stages (Idea → MVP → Growth → Scale → Mature → Sunset)

**Factory Code (Enhanced):**
- `venture_factory.py` (expand from 160 lines to ~500 lines)
  - Spawn venture folder structure
  - Create Supabase project (new)
  - Create n8n workspace (new)
  - Create Grafana dashboard (new)
  - Assign agent team (new)
  - Wire approval flows (new)

**Templates:**
```
templates/
  construction/
    venture-template.yaml       # Inherit CON config
    agent-team.yaml             # CEO + CTO + CFO
    workflows.yaml              # Job → Estimate → Contract → Payment
    dashboards.json             # KPI dashboard
  
  staffing/
    venture-template.yaml
    agent-team.yaml
    workflows.yaml
    dashboards.json
  
  real-estate/
    venture-template.yaml
    agent-team.yaml
    workflows.yaml
    dashboards.json
```

### Success Criteria (Day 30)
- ✅ One command: `venture create --template construction --name "ABC Builders"`
- ✅ Results: Folder created + Supabase project provisioned + n8n workflows deployed + Grafana dashboard + agents assigned
- ✅ New venture is immediately operational (can receive jobs/leads)
- ✅ Venture inherits knowledge platform (can query repos, docs, risks)
- ✅ Venture has access to shared AI platform (agents, tools, workflows, prompts)
- ✅ CEO dashboard shows all 9 (or N) ventures + consolidated health

### Time Budget
- Documentation: 10 hours
- Expand venture_factory.py: 20 hours
- Templates + provisioning: 16 hours
- Integration testing: 8 hours
- **Total: 54 hours across 9 days**

### Code Baseline (Build on Existing)
- `agent_factory.py` (160 lines)
- New: Supabase project creation (50 lines)
- New: n8n workflow deployment (50 lines)
- New: Grafana dashboard provisioning (40 lines)
- New: Agent team assignment (30 lines)

---

## Definition of Done (End of Day 30)

By Day 30, you should be able to answer "yes" to these:

- ✅ **Architecture:** Can a new developer understand the entire system from documentation alone?
- ✅ **Bootstrap:** Can the platform be deployed from one command?
- ✅ **Knowledge:** Are 712 ventures + 1,639 repos searchable?
- ✅ **AI:** Do agents have access to shared registries (models, tools, prompts, workflows)?
- ✅ **Governance:** Is there a single permission model (Hermes routing, policies)?
- ✅ **Factory:** Can a new venture be scaffolded in <5 minutes?
- ✅ **Observability:** Is there a single executive dashboard showing platform health?
- ✅ **Inheritance:** Does every venture inherit the same infrastructure and OS?

---

## Day-by-Day Breakdown

### Week 1: Architecture (7 days)
| Day | Deliverable | Time | Owner |
|-----|-------------|------|-------|
| 1 | OPERATING-SYSTEM.md + ARCHITECTURE.md | 6h | You |
| 2 | SYSTEM-LAYERS.md + DEPENDENCY-GRAPH.md | 4h | You |
| 3 | GOVERNANCE.md + REPOSITORY-STANDARDS.md | 4h | You |
| 4 | BUILD-ORDER.md + diagrams | 5h | You |
| 5 | Review + architecture approval | 2h | You |
| 6 | Iterate based on feedback | 2h | You |
| 7 | Final documentation polish | 1h | You |
| **Week 1 Total** | **7 files, architecture frozen** | **24h** | |

### Week 2: Knowledge Platform (7 days)
| Day | Deliverable | Time | Owner |
|-----|-------------|------|-------|
| 8 | KNOWLEDGE-ARCHITECTURE.md + Neo4j schema | 6h | You |
| 9 | Run populate_venture_knowledge_graph.py | 4h | You |
| 10 | Run build_repo_rag.py (Qdrant indexing) | 5h | You |
| 11 | Graphify + Gittodoc integration | 6h | You |
| 12 | Search API + query testing | 6h | You |
| 13 | INGESTION.md + SYNCHRONIZATION.md | 4h | You |
| 14 | Integration testing + verification | 4h | You |
| **Week 2 Total** | **7 files, knowledge platform live** | **44h** | |

### Week 3: AI Platform (7 days)
| Day | Deliverable | Time | Owner |
|-----|-------------|------|-------|
| 15 | AGENT-REGISTRY.md + agent_registry.yaml | 6h | You |
| 16 | MODEL-REGISTRY.md + PROMPT-REGISTRY.md | 6h | You |
| 17 | TOOL-REGISTRY.md + WORKFLOW-REGISTRY.md | 6h | You |
| 18 | CAPABILITY-REGISTRY.md + MCP-REGISTRY.md | 6h | You |
| 19 | Policy engine + PERMISSIONS.md | 8h | You |
| 20 | Registry loaders + API | 8h | You |
| 21 | Integration testing + agent discovery | 6h | You |
| **Week 3 Total** | **11 files, AI platform operational** | **48h** | |

### Week 4: Venture Factory (9 days)
| Day | Deliverable | Time | Owner |
|-----|-------------|------|-------|
| 22 | VENTURE-FACTORY.md + VENTURE-TEMPLATE.md | 6h | You |
| 23 | Expand venture_factory.py (50 lines) | 8h | You |
| 24 | Supabase provisioning (50 lines) | 6h | You |
| 25 | n8n deployment (50 lines) | 6h | You |
| 26 | Grafana provisioning (40 lines) | 6h | You |
| 27 | INDUSTRY-TEMPLATES.md + templates/ | 8h | You |
| 28 | Agent team assignment + AUTOMATION.md | 6h | You |
| 29 | E2E testing: spawn venture → verify | 8h | You |
| 30 | CEO dashboard + final docs | 6h | You |
| **Week 4 Total** | **9 files, venture factory operational** | **54h** | |

---

## Total Time Budget

| Week | Phase | Hours | Focus |
|------|-------|-------|-------|
| 1 | Architecture | 24 | Documentation (no code)
| 2 | Knowledge | 44 | Infrastructure (Neo4j, Qdrant)
| 3 | AI Platform | 48 | Registries (agent discovery)
| 4 | Venture Factory | 54 | Provisioning (spawn ventures)
| **Total** | **30-day sprint** | **170 hours** | **4 layers complete**

**Roughly:** 6 hours/day (manageable, leaves time for firefighting)

---

## What Success Looks Like (End of Day 30)

### Snapshot 1: New Developer Onboarding
```
$ git clone https://github.com/Worldwidebro/ai-boss-os
$ cd ai-boss-os
$ make bootstrap  # Single command
# 45 minutes later...
$ make status
✅ Architecture: Frozen (OPERATING-SYSTEM.md)
✅ Knowledge: Live (Neo4j 712 ventures, Qdrant 1,639 repos)
✅ AI Platform: Operational (agents can discover tools, prompts, workflows)
✅ Venture Factory: Ready (can spawn ventures)
```

### Snapshot 2: Spawn a New Venture
```
$ venture create --template construction --name "Smith Construction"
✅ Folder created: ventures/CON-999-smith-construction/
✅ Supabase project provisioned
✅ n8n workflows deployed
✅ Grafana dashboard: smith-construction@grafana.internal
✅ Agent team assigned: CEO (AG-CEO), CTO (AG-CTO), CFO (AG-CFO)
✅ Knowledge platform: Accessible (search repos, docs, risks)

# Result: New venture is immediately operational
# Can accept jobs, route through Hermes, process payments
```

### Snapshot 3: Executive Dashboard
```
$ open https://vex-hero-site/dashboard/ceo
# Shows:
- 712 ventures (9 active, 703 templates)
- Platform health (Neo4j ✅, Qdrant ✅, Supabase ✅, n8n ✅)
- Revenue this week: $0 (first ventures just launched)
- Agent execution: 47 tasks completed
- Decision routing: 3 approvals (all <$5K, auto-approved)
- Knowledge platform: 1,639 repos indexed, searchable
```

---

## After Day 30: Next Programs

**Do NOT start these during the 30-day sprint. These depend on the core platform.**

1. **Days 31–60: Department Operating Systems**
   - Sales OS (lead intake, CRM, pipeline)
   - Marketing OS (content, campaigns, analytics)
   - Finance OS (accounting, FP&A, forecasting)
   - HR OS (recruiting, payroll, benefits)
   - Engineering OS (code quality, deployment, observability)

2. **Days 61–90: Venture Implementations**
   - CON-001: Production operations (10 jobs/week)
   - STA-001: Production operations (20 placements/week)
   - RE-001: Production operations (5 listings/week)
   - Measure revenue + unit economics

3. **Days 91–180: Scale to 100 Ventures**
   - Automate everything (no manual work)
   - Hit $50K/month revenue (all 100 combined)
   - Document what works, what doesn't
   - Update templates based on learnings

---

## How to Start (Right Now)

1. **Approve the 30-day plan** (this document)
2. **Day 1 morning:** Outline OPERATING-SYSTEM.md (2 hours)
3. **Day 1 afternoon:** Outline ARCHITECTURE.md + diagrams (2 hours)
4. **Publish to GitHub:** Make it visible to all future developers

**First milestone:** Architecture frozen by Day 7.

---

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Architecture changes mid-sprint | Rework weeks 2-4 | Freeze architecture by Day 7 (documented review) |
| Infrastructure fails | Can't test | Use mock data, docker-compose, local Ollama |
| Registries grow too large | Slow queries | Implement caching (Redis), pagination |
| 712 ventures overload dashboard | Performance | Paginate by sector, use time-based filtering |

---

*This sprint builds the OS foundation. Every venture launched after Day 30 inherits everything. Platform-first, not vendor-first.*
