# CLAUDE.md — Company Brain (Session Guidance)

**Scope:** Active session instructions + Bases architecture integration  
**Updated:** 2026-09-22 (AUDIT + BASES DEFINITION COMPLETE)  
**Authority:** Infrastructure CP-027 + Execution CP-033 + Revenue CP-021 + [[STARTHERE|STARTHERE.md]] (master orientation)  
**Architecture Layers (Complete Stack):**
  1. Legal Structure (200 entity types × 150 instances × 789 ventures)
  2. Bases (35 knowledge/operating domains per sector)
  3. People + Roles + Onboarding ← NEW (41 people × 40+ roles × entity assignments)
  4. Company Brain (Neo4j graph, Qdrant vectors, Supabase state, Registries)
  5. Agent System (30-50 functional agents with 100+ skills, 3 autonomy levels)
  6. Workflows (sequences + orchestration)
  7. Loops (recurring control systems + observability)
  8. Execution Loop (14-stage work completion + evidence generation)
  9. VEX CommandCenter (public front door + real-time dashboard)

**Current Phase:** Week 3 Bases Instantiation + Agentic Scaling (Sep 23–30) | [[ANTIGRAVITY|ANTIGRAVITY.md]] (45 operating rules) + [[BASES-CANONICAL-DEFINITION|_ONTOLOGY/BASES-CANONICAL-DEFINITION.md]] (new layer)

---

## STATUS SNAPSHOT — Sep 23, 2026 (UPDATED)

✅ **Phase 1 LOCKED** (Sep 6-15) — Agent Enablement complete, audit system operational  
✅ **Phase 2 LAUNCHED** (Sep 16-30) — Graph-native refactor (Neo4j schema deployment Sep 18)  
✅ **Phase 2a DESIGNED** (Sep 23) — Agentic scaling with people+roles bridge (30-50 functional agents, not 318)
✅ **Bases Architecture DEFINED** (Sep 22) — 35 bounded knowledge/operating domains, standard schema
✅ **People + Roles LAYER CREATED** (Sep 23) — 4 master registries + onboarding system
  - PEOPLE-REGISTRY.yaml (21 key people identified)
  - ROLES-REGISTRY.yaml (40+ standard roles)
  - RESPONSIBILITY-MATRIX.csv (entity → role → person mappings)
  - AUTHORITY-MATRIX.yaml (approval thresholds + decision routing)
  - ROLE-REQUIREMENTS.yaml (what each role needs)
  - ONBOARDING-TEMPLATES.yaml (automated onboarding packages)
✅ **Infrastructure LIVE** — Neo4j (20,363 edges), Qdrant (17,236 vectors), OmniRoute, Ollama  
✅ **Folder Structure AUDITED** — 132 directories, 36 sectors, 789 ventures, 59 canonical registries
✅ **6 Tier-0 Ventures Executing** — OPS-001, LT-005, CALLCENTER (revenue-ready)

📊 **Week 3 Schedule (Sep 23–30):**
- BASE Phase 1 instantiation (BASE-009, BASE-012, BASE-014) ← Parallel
- People verification + agent system design (people audit + functional agent framework) ← Parallel
- **Target:** 3 production-ready Bases + 18+ people VERIFIED + Agent system designed by Oct 6

---

## WEEK 3 EXECUTION FOCUS (Sep 23–30)

**Master plan:** [[WEEK1-EXECUTION-PLAN|20-DECISIONS/WEEK1-EXECUTION-PLAN.md]] + [[PHASE-2A-AGENTIC-ENGINEERING-PLAN|20-DECISIONS/PHASE-2A-AGENTIC-ENGINEERING-PLAN.md]]

### Three Revenue-Ready Ventures (Continued Scaling)
1. **OPS-001** → Cold call campaign + lead follow-up (ANTIGRAVITY Rule 44: Execute → Observe → Verify)
2. **LT-005** → B2B outreach scaling + booking automation (Rule 2: Determine problem, user, outcome)
3. **CALLCENTER** → Live call routing + quality scoring (Rule 18: Observability mandated)

### Graph-Native Phase 2 Deployment (Sep 18–30)
- **Neo4j Schema:** Deployed Sep 18 (constraints, indexes, integrity gates live)
- **YAML→Graph Pipeline:** 14-day migration (Sep 17–Oct 1) — query new 36-sector model via Cypher
- **Agent Context Assembly:** Subgraph queries for L2/L3 autonomy via portfolio horizons + archetypes

**See also:** [[VENTURE-AUDIT-FRAMEWORK|20-DECISIONS/VENTURE-AUDIT-FRAMEWORK.md]] (12-layer, Rule 2 enforced) + [[PHASE-2-PHASE-2A-INTEGRATION-MAP|20-DECISIONS/PHASE-2-PHASE-2A-INTEGRATION-MAP.md]] + [[AUDIT-2026-09-22|_REFERENCE/AUDIT-2026-09-22.md]]

---

## ARCHITECTURE LAYERS (Complete Stack)

```
WORLDWIDEBRO GROUP (Holding Company)
    │
    ├── VEX CommandCenter (Public Portal)
    │   ├── Hero experience + showcase
    │   ├── Real-time Supabase dashboard
    │   └── Public portfolio.public.json
    │
    ├── BASES LAYER (35 Domain Systems)
    │   ├── BASE-001 to BASE-036 (1 per sector)
    │   ├── Knowledge/Ontology/Ventures/Agents per Base
    │   └── Standard schema (Identity → Outputs)
    │
    ├── COMPANY BRAIN (Intelligence)
    │   ├── Neo4j (20,363+ edges, 35 Base node clusters)
    │   ├── Qdrant (17,236+ vectors, semantic search)
    │   ├── Supabase/PostgreSQL (operational state)
    │   └── Registries (789 ventures, 300+ capabilities, 150 entities)
    │
    ├── MASTER ORCHESTRATOR (Coordination)
    │   ├── 13-stage decision loop
    │   ├── Continuous observation → learning
    │   └── Multi-Base coordination
    │
    ├── AGENT SYSTEM (Workers)
    │   ├── 318 agents + 16 routing agents
    │   ├── L1/L2/L3 autonomy levels
    │   └── Per-Base agent scoping
    │
    ├── CAPABILITY SYSTEM (Inventory)
    │   ├── 300+ capabilities
    │   ├── Sector-mapped coverage analysis
    │   └── Repository + Tool + Skill registries
    │
    ├── EXECUTION LOOP (Action)
    │   ├── 14-stage work completion
    │   ├── Failure handling + rollback
    │   └── Revenue attribution
    │
    └── LEGAL/FINANCIAL STRUCTURE
        ├── Family Trust (Principal)
        ├── 150 Legal Entities (Trusts, HoldCos, OpCos)
        ├── 36 Operating Companies (OpCos)
        └── 789 Ventures (mapped to OpCos + Sectors)
```

---

## ECOSYSTEM ALIGNMENT: Bases ↔ VEX ↔ Worldwidebro ↔ 789 Ventures

### Layer 1: Legal Structure (Bottom)
- **150 Legal Entities** (Family Trust → Asset LLCs → Operating C-Corp)
- **36 Operating Companies** (opco_id per venture)
- **789 Ventures** (mapped to OpCos + 36 Sectors + 4 archetypes)
- See: [[FAMILY_OFFICE_ECOSYSTEM_ALIGNMENT_MASTER|_REGISTRIES/CANONICAL/FAMILY_OFFICE_ECOSYSTEM_ALIGNMENT_MASTER.csv]]

### Layer 2: Knowledge/Operating Domains (NEW)
- **35 Bases** (BASE-001 to BASE-036, one per sector)
- Each Base contains: ventures, ontology, knowledge, agents, operations
- Standard schema: Identity → Knowledge → Market → Ventures → Operations → Technology → Agents → Decisions → Experiments → Outputs
- See: [[BASES-CANONICAL-DEFINITION|_ONTOLOGY/BASES-CANONICAL-DEFINITION.md]]

### Layer 3: Intelligence Graph (Middle)
- **Neo4j**: 35 Base node clusters + 789 venture nodes + 300+ capability nodes
- **Qdrant**: Semantic search over Base knowledge + venture insights
- **Supabase**: Real-time state (venture metrics, agent performance, revenue)
- **Registries**: [[ALL_789_VENTURES_36_SECTOR_ALIGNMENT|_REGISTRIES/CANONICAL/ALL_789_VENTURES_36_SECTOR_ALIGNMENT.csv]] (CURRENT TRUTH)

### Layer 4: Coordination & Execution (Middle)
- **Master Orchestrator**: 13-stage loop (Observe → Understand → Discover → Plan → Decompose → Match → Delegate → Execute → Monitor → Evaluate → Verify → Learn → UpdateBrain)
- **Agent System**: 318 agents scoped to Bases + OpCos + ventures
- **Capability System**: 300+ capabilities mapped to sectors and Bases
- **Execution Loop**: 14-stage work flow (objective → outcome + feedback)

### Layer 5: Public Portal (Top)
- **VEX CommandCenter**: Real-time dashboard (Supabase-backed)
  - Portfolio metrics (revenue, active agents, running tasks)
  - Venture showcase (hero experience)
  - Founder advisory path
- **Deployment**: vex-hero-site-sigma.vercel.app (live)
- See: [[VEX|VEX.md]] + [[VEX-DEPLOYMENT-READY|VEX-DEPLOYMENT-READY.md]]

### How They Connect

```
USER (Founder/Operator/Investor)
    ↓
VEX CommandCenter (Portal)
    ↓ (Query: "Show me medical logistics ventures")
Bases Layer (BASE-009: Logistics)
    ↓ (Find ventures in domain)
Neo4j Graph (LT-005, LT-011 nodes)
    ↓ (Retrieve metadata)
Supabase (Revenue, status, agents)
    ↓ (Agent assigned)
Agent (Dispatch Agent in BASE-009)
    ↓ (Execute action)
Result (Delivery scheduled)
    ↓ (Measure)
Memory (Learning → future decisions)
```

---

## NAMING CONSOLIDATION

**Unified ecosystem: VEX + Worldwidebro + Bases + Ventures**

| Layer | Name | GitHub | Deployed | Status |
|-------|------|--------|----------|--------|
| **Public Portal** | VEX CommandCenter | Worldwidebro/Worldwidebro-Vex | vex-hero-site-sigma.vercel.app | ✅ Live |
| **Holding Co.** | Worldwidebro Holdings | — | — | ✅ Operating (789 ventures) |
| **Domains** | Bases (35 systems) | Company Brain | — | ✅ In framework (instantiating) |
| **Ventures** | 789 companies | Worldwidebro/* repos | Multiple Vercel deploys | ✅ Mapped (ALL_789_VENTURES_36_SECTOR_ALIGNMENT.csv) |
| **Dashboard** | Growth OS | worldwidebro-marketing-os | localhost:3030 | ✅ Testing |

**Removed terminology:** "Venture Portal", "Hermes Command Center" (superseded by VEX)

---

## MASTER ORIENTATION (Read in Order)

**STARTHERE.md Sequence (Non-negotiable):**
1. [[STARTHERE|STARTHERE.md]] — Master orientation + architecture layers (Company Brain, Master Orchestrator, Agent System, Capability System, Execution Loop)
2. [[REALITY|REALITY.md]] — Verified truth (what is actually happening)
3. [[00_RESPECT/RESPECT|RESPECT.md]] — 20 governance rules
4. [[ANTIGRAVITY|ANTIGRAVITY.md]] — 45 operating rules (zero fake completion)
5. [[CLAUDE.md]] (this file) — Infrastructure + Bases + session guidance

**NEW:** Bases Architecture Sequence
1. [[BASES-CANONICAL-DEFINITION|_ONTOLOGY/BASES-CANONICAL-DEFINITION.md]] — What are Bases? (35 knowledge/operating domains, NOT databases)
2. [[BASE-INSTANTIATION-AGENTIC-PLAN|20-DECISIONS/BASE-INSTANTIATION-AGENTIC-PLAN.md]] — How to build Bases? (6-week agentic plan, 15-min units, eval-first)
3. [[VEX|VEX.md]] — How does VEX query Bases? (CommandCenter dashboard + portfolio)
4. [[ALL_789_VENTURES_36_SECTOR_ALIGNMENT|_REGISTRIES/CANONICAL/ALL_789_VENTURES_36_SECTOR_ALIGNMENT.csv]] — Current venture alignment (which ventures live in which Bases)

**QUICK REFERENCE**

**WHO AM I:** [[WHO-I-AM-ANTWUAN-JOHNS|00-CONSTITUTION/WHO-I-AM-ANTWUAN-JOHNS.md]] (Founder identity + authority + philanthropic mission) — **START HERE for founder context**  
**PEOPLE + ROLES:** [[PEOPLE-ROLES-INFRASTRUCTURE-BRIDGE|_REFERENCE/PEOPLE-ROLES-INFRASTRUCTURE-BRIDGE.md]] (21 people, 40+ roles, approval chains)  
**BASES Architecture:** [[BASES-CANONICAL-DEFINITION|_ONTOLOGY/BASES-CANONICAL-DEFINITION.md]] (35 governed knowledge/operating domains, Sep 22)  
**BASE Instantiation Plan:** [[BASE-INSTANTIATION-AGENTIC-PLAN|20-DECISIONS/BASE-INSTANTIATION-AGENTIC-PLAN.md]] (agentic engineering, 6 weeks, Sep 23 kickoff)  
**VEX Ecosystem:** [[VEX|VEX.md]] (public CommandCenter + real-time dashboard)  
**Venture Alignment:** [[ALL_789_VENTURES_36_SECTOR_ALIGNMENT|_REGISTRIES/CANONICAL/ALL_789_VENTURES_36_SECTOR_ALIGNMENT.csv]] (all 789 ventures → OpCos → Bases)

**Audit Trail:** [[AUDIT-2026-09-22|_REFERENCE/AUDIT-2026-09-22.md]] (verified folder structure, sector count, registries, dual naming conflicts)  
**Logic Architecture:** [[_DOCS/LOGIC-ARCHITECTURE-FRAMEWORK.md]] (72 logic layers, 12 executive divisions, 250+ control points, autonomous loop patterns) — [[_REGISTRIES/CANONICAL/LOGIC_LAYERS_REGISTRY.yaml|Master Registry]]  
**Infrastructure Status:** [[INFRASTRUCTURE-STATUS-2026-09|_REFERENCE/INFRASTRUCTURE-STATUS-2026-09.md]]  
**Venture Roadmap:** [[VENTURE-ROADMAP-2026-09|_REFERENCE/VENTURE-ROADMAP-2026-09.md]]  
**36-Sector Model:** [[ALL_789_VENTURES_36_SECTOR_ALIGNMENT|_REGISTRIES/CANONICAL/ALL_789_VENTURES_36_SECTOR_ALIGNMENT.csv]] (Sep 22) — SECTOR mapping  
**Family Office Architecture:** [[FAMILY_OFFICE_ECOSYSTEM_ALIGNMENT_MASTER|_REGISTRIES/CANONICAL/FAMILY_OFFICE_ECOSYSTEM_ALIGNMENT_MASTER.csv]] (Sep 22)

**Quick Commands:**
```bash
docker --context macstudio ps              # Verify all services
curl http://100.87.214.70:6333/health     # Check Qdrant
curl http://100.87.214.70:7474            # Check Neo4j browser
ssh macstudio                               # Connect to Mac Studio
```

**Dashboard Access:**
| Service | URL | Auth |
|---------|-----|------|
| OmniRoute | http://100.87.214.70:20128 | Bitwarden "OmniRoute — Company Brain" |
| Neo4j | http://100.87.214.70:7474 | neo4j / changeme |
| Growth OS | localhost:3030 | No auth |
| VEX | vex-hero-site-sigma.vercel.app | No auth |

---

## ONE RULE (ANTIGRAVITY Rules 31 + 44)

**Verify before claiming it works.** → Report truthful states only: `IMPLEMENTED` | `TESTED` | `VERIFIED` | `DEPLOYED` | `OBSERVED`

**Default Agent Behavior Protocol (ANTIGRAVITY Rule 44):**
1. **Understand**: Determine the real problem and outcome
2. **Inspect**: Examine code, configuration, dependencies, registries
3. **Reuse**: Identify existing capabilities (ANTIGRAVITY Rule 34: MANDATORY starred repo search)
4. **Plan**: Formulate an implementation plan appropriate to scope
5. **Execute**: Make smallest coherent, atomic changes
6. **Test**: Execute tests across relevant levels
7. **Verify**: Inspect concrete, observable results (see docker, queries below)
8. **Document**: Record changes in registries and artifacts
9. **Report**: Summary, Changes, Tests, Verification, Known Issues, Next Steps

**Quick verification:**
- ✅ Check: `docker --context macstudio ps`, actual CLI output, live queries
- ❌ Never: Trust documentation, commit messages, "should be working"
- 🛑 Always: Ask before retrying if uncertain — don't loop blindly

---

## GIT INVARIANTS (ANTIGRAVITY Rule 11: Git Safety)

1. All venture changes → Git + PR (never direct DB edits)
2. Commit messages include venture ID when applicable
3. Tests must pass before merge
4. **Never:** Delete unrelated work, rewrite history, force-push, destroy uncommitted work
5. **Pre-change:** `git status && git branch && git diff`
6. **Post-change:** `git diff && git status && <run tests>`
7. Attribution: `Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>`

---

## WHAT I MUST NEVER DO (ANTIGRAVITY Rules Enforced)

1. **Claim infrastructure works without verification** (Rule 31: No fake completion)
2. **Invent or guess credentials** (Rule 16: Zero trust; use Bitwarden or MCP auth)
3. **Modify production without approval gate** (Rule 10: High-risk actions need explicit approval)
4. **Duplicate existing infrastructure/capability** (Rule 2: Prefer reuse over duplication)
5. **Create ventures outside Git + Supabase PR flow** (Rule 11: Git safety)
6. **Ignore ANTIGRAVITY Rule 34** — MANDATORY starred repo search BEFORE custom implementation
   - Search: 904 starred repos (`_REGISTRIES/EXTERNAL_CAPABILITY_UNIVERSE_INVENTORY.md`)
   - Search: 177 owned code repos (`_REGISTRIES/CANONICAL/REPOSITORY_REGISTRY.yaml`)
   - Search: 300 canonical capabilities (`_REGISTRIES/CANONICAL/CAPABILITY_REGISTRY.yaml`)
   - Build/adopt/integrate only if <70% gap exists
7. **Engage in infinite meta-work** instead of executing revenue ventures ([`REVENUE_GATE.md`](.agents/rules/REVENUE_GATE.md))

---

## REFERENCE FILES (Moved from CLAUDE.md)

**Infrastructure & Systems:**
- `_REFERENCE/INFRASTRUCTURE-STATUS-2026-09.md` — Services, hardware, credentials, routing gaps
- `_REFERENCE/VENTURE-ROADMAP-2026-09.md` — 7 Tier-1 ventures, critical blockers, timeline
- `_REFERENCE/DIGITAL-LIBRARIAN-ARCHITECTURE.md` — 5-layer research OS (OSS candidate evaluation)
- `_REFERENCE/OPERATIONAL-STATE-2026-09.md` — What's working vs. NOT wired

**Capital & Holding Company Architecture:**
- `INSTITUTIONAL-VENTURE-ARCHITECTURE.md` — **MASTER MAP: All 789 ventures mapped to family office structure + repos + OSS deps + inter-venture trading**
- `WORLDWIDEBRO-HOLDINGS-MASTER-OPERATING-MANUAL.md` — 789-venture holding company framework (portfolio strategy, governance, capital allocation, exits)
- `BUSINESS-CAPITAL-DATA-ROOM/00_ENTERPRISE_BLUEPRINT.md` — Family office structure (Family Trust → Asset/IP/Admin LLCs → Operating C-Corp)
- `CAPITAL-READINESS-ENGINE.md` — 5-venture capital readiness matrix + $4.5M capital sources
- `BUSINESS-CAPITAL-DATA-ROOM/FINANCIAL-ECOSYSTEM-MAPPING.md` — 12-layer financial OS (banking, credit, debt, investment, payments, insurance, government, infrastructure, marketplaces)

**Master Orientation (Root Docs):**
- [[STARTHERE]] — Phase 0 locked, Phase 1 execution
- [[REALITY]] — Verified truth ledger
- [[ANTIGRAVITY]] — 45 operating rules
- [[RESPECT]] — 20 governance rules
- [[INDEX]] — Master navigation

---

## ALIGNMENT TO ANTIGRAVITY.md

**This file operationalizes ANTIGRAVITY.md rules for weekly execution:**

| ANTIGRAVITY Rule | Applied Here | Week 2 Checkpoint |
|------------------|--------------|------------------|
| Rule 2: Core Operating Principle | Every decision requires: problem→user→outcome→existing→reuse→dependencies→systems→risks→success→verification | Sep 22 |
| Rule 11: Git Safety | 7-point protocol (pre/post-change) | Enforced on all PRs |
| Rule 31: No Fake Completion | State: IMPLEMENTED/TESTED/VERIFIED/DEPLOYED/OBSERVED | Weekly audit Sep 22 |
| Rule 34: Reuse-First (MANDATORY) | Search 904+177+300 sources before building | Before any feature |
| Rule 44: Default Agent Behavior | 9-step protocol (Understand→Report) | Every task execution |

---

## SESSION START CHECKLIST

✅ Load **CLAUDE.md** (this file) — Week 2 execution guide  
✅ Load **ANTIGRAVITY.md** — 45 operating rules (enforced on all work)  
✅ Load [[STARTHERE]] (orientation)  
✅ Verify services: `docker --context macstudio ps`  
✅ Identify context (venture? sector? phase?)  
✅ Load relevant reference docs

---

## GBrain Configuration (Setup Sep 19, 2026)

<!-- gstack-gbrain-configuration:start -->

**Status:** ✅ LIVE — local PGLite brain running, Claude Code MCP registered

| Component | Status | Details |
|-----------|--------|---------|
| **CLI** | ✅ Installed | gbrain v0.51.0.0 at `/Users/acebless/.bun/bin/gbrain` |
| **Engine** | ✅ PGLite | `/Users/acebless/.gbrain/brain.pglite` (local, ~1,600 pages indexed) |
| **MCP** | ✅ Connected | `gbrain serve` registered in Claude Code (user scope) |
| **Doctor** | ✅ OK | Schema v159, all migrations applied |
| **Repo Code** | ✅ Indexed | Company Brain codebase: 1,611 pages, 4,899 chunks |
| **Repo Policy** | ✅ Read-Write | Code from `origin` (Github) auto-indexed |
| **Trust Model** | ✅ Personal | Local brain (single-tenant), auto-push mode enabled |
| **Sync Artifacts** | ✅ Configured | Artifacts-only mode (plans, designs, retros) |
| **Transcripts** | ✅ Enabled | Session transcripts will be indexed for memory continuity |

**Quick usage:**
```bash
gbrain search "query terms"        # Semantic search
gbrain code-def MyFunction         # Find symbol definition
gbrain code-refs MyFunction        # Where is it used
gbrain doctor --json               # Health check
```

**In Claude Code:** The `mcp__gbrain__*` tools are now available. Restart Claude Code to load them. Use them for semantic code search, context assembly, and memory queries across the Company Brain.

**Cloud sync (if needed later):** To share this brain with other machines, run `gbrain sources add --path --federated ~/.gstack` after setting up a Supabase connection. Local PGLite brains cannot have remote replicas — upgrade to Supabase for that.

<!-- gstack-gbrain-configuration:end -->

---

**Updated:** 2026-09-19 | **Version:** 4.2 (Phase 2 launched, aligned to ANTIGRAVITY.md, Week 2 execution active, gbrain configured Sep 19)
