# CLAUDE.md — Company Brain Session Guidance

**Master Navigation:**
- **[[STARTHERE|STARTHERE.md]]** ← Read first (mandatory orientation)
- **[[INDEX|_REGISTRIES/CANONICAL/INDEX.md]]** ← Master catalog (all sectors, ventures, registries, legal entities)
- **[[DOMAIN-MAP|_REGISTRIES/CANONICAL/DOMAIN-MAP.md]]** ← All 71 domains + wiring structure
- **[[LOG|_REGISTRIES/CANONICAL/LOG.md]]** ← Timeline of work + discoveries

**Scope:** Live session infrastructure state + links to operational docs  
**Updated:** 2026-09-23 (wiki wiring complete: STARTHERE → INDEX → DOMAIN-MAP → Domain INDEXes → Files)  
**Authority:** CP-001/CP-027 (sovereign governance) | [[ANTIGRAVITY|ANTIGRAVITY.md]] (45 rules) | [[REALITY|REALITY.md]] (verified truth)

**Status:** Week 3 Bases Instantiation + Data Reconciliation (Sep 23–30) | 5-phase Supabase reconciliation starting Sep 26

---

## STATUS SNAPSHOT — Sep 25, 2026 (GROUND TRUTH DIVERGENCE CRITICAL)

✅ **Phase 1 LOCKED** (Sep 6-15) — Agent Enablement complete, audit system operational  
✅ **Phase 2 LAUNCHED** (Sep 16-30) — Graph-native refactor (Neo4j schema deployment Sep 18)  
✅ **Phase 2a DESIGNED** (Sep 23) — Agentic scaling with people+roles bridge (30-50 functional agents, not 318)
✅ **Bases Architecture DEFINED** (Sep 22) — 35 bounded knowledge/operating domains, standard schema
✅ **People + Roles LAYER CREATED** (Sep 23) — 4 master registries + onboarding system
✅ **Infrastructure LIVE** — Neo4j (20,363 edges), Qdrant (17,236 vectors), OmniRoute, Ollama  
✅ **Canonical Registries FROZEN** (Sep 24) — SECTOR-REGISTRY.yaml, OPCO-REGISTRY.yaml, BASE-REGISTRY.yaml, VENTURE-REGISTRY.yaml
✅ **6 Tier-0 Ventures EXECUTING** — OPS-001, LT-005, CALLCENTER (revenue-ready)

🚨 **CRITICAL DISCOVERY (Sep 25) — BASE GATE EVALUATION PAUSED**
- **Manual registries claim:** 36 sectors, 35 OpCos, 789 ventures (in YAML)
- **Supabase ground truth shows:** 25 sector categories, 5 OpCos, 580 ventures (verified live)
- **Phase 2 audit findings:** 3 catastrophic misclassifications (LT-005/LT-011, venture counts 82-90% wrong, SEC-012 unmapped)
- **Impact:** Cannot evaluate Base gates until venture assignments verified correct
- **Status:** AWAITING 4 FOUNDER DECISIONS before Supabase schema expansion
- **References:** [[SUPABASE-RECONCILIATION-PLAN-2026-09-25|_REGISTRIES/CANONICAL/SUPABASE-RECONCILIATION-PLAN-2026-09-25.md]] + [[AUDIT-PHASE2-FINDINGS-2026-09-25|_REGISTRIES/CANONICAL/AUDIT-PHASE2-FINDINGS-2026-09-25.md]]

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
- **Neo4j**: 35 Base node clusters + 789 venture nodes + 300+ capability nodes (in progress)
- **Qdrant**: Semantic search over Base knowledge + venture insights
- **Supabase** ⭐: **OPERATIONAL GROUND TRUTH** — 25 sector categories, 5 OpCos, 580 real ventures, live state
- **Registries**: [[ALL_789_VENTURES_36_SECTOR_ALIGNMENT|_REGISTRIES/CANONICAL/ALL_789_VENTURES_36_SECTOR_ALIGNMENT.csv]] (PENDING RECONCILIATION)

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

## 🛑 CRITICAL: PENDING FOUNDER DECISIONS (Sep 25–26)

**Context:** Phase 2 audit revealed ground truth divergence. Supabase is operational reality (580 ventures, 25 sectors); manual registries claim 789 ventures across 36 sectors. Before proceeding with Supabase schema expansion or Base gate evaluation, these 4 decisions must be made.

### Decision 1: Venture Count Reality
- **In Supabase:** 580 real ventures (verified)
- **In our registry:** 789 ventures claimed
- **Gap:** 209 ventures (26.5% missing)
- **Question:** Are the 209 missing ventures phantom duplicates, real ventures not yet in Supabase, planned ventures, or misclassified in CSV?
- **Impact:** Venture counts wrong by 82-90% in some sectors (SEC-014, SEC-024, SEC-029); Base gate evaluation invalid until resolved
- **See:** AUDIT-PHASE2-FINDINGS #2 (venture count discrepancies)

### Decision 2: Sector Model Direction
- **Option A:** Expand Supabase sectors from 25 categories → 36 SEC-XXX codes (adds complexity, matches our model)
- **Option B:** Simplify to 25-category Supabase model (less opinionated, but loses sector granularity)
- **Option C:** Create mapping layer (both models coexist, more maintenance)
- **Recommended:** Option A (we've already built the 36-sector model; expand Supabase to match it)
- **Impact:** Determines entire Phase 2-3 infrastructure build

### Decision 3: Bases Table Location
- **Option A:** Create `bases` table in Supabase (makes gate tracking queryable, centralizes data)
- **Option B:** Keep in YAML registries, sync via API (keeps flexibility, more manual)
- **Recommended:** Option A (queryable state is essential for observability)
- **Impact:** Where BASE-001 to BASE-036 live and how gate evaluation queries them

### Decision 4: Entities Registry Verification
- **Finding:** `legal_entities` table exists in Supabase (682 records)
- **Question:** Is this the entities registry? Does it have correct schema (entity_id, legal_name, entity_type, owner, etc.)?
- **Impact:** Determines whether we expand it or create separate entities_v2 table
- **Action:** Query schema: `SELECT column_name, data_type FROM information_schema.columns WHERE table_name='legal_entities';`

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

## RECONCILIATION ROADMAP (Sep 25–30)

**Phase 1: Data Mapping (Sep 26)** — List existing Supabase data, create mapping document  
**Phase 2: Infrastructure Build (Sep 27–28)** — Update schemas, create bases table, populate missing data  
**Phase 3: Verification (Sep 29–30)** — Run audit queries, sync local registries from Supabase  

**Blocker:** Phase 2 audit paused. No Base gate evaluation until venture assignments verified.  
**Next action:** Founder decisions on 4 critical questions above. Then query Supabase to determine truth.

---

**Updated:** 2026-09-25 | **Version:** 4.3 (Ground truth divergence detected Sep 25, 4 founder decisions pending, reconciliation plan created, Phase 2 audit paused)

---

## Control Base Reference

This document is mapped to [[B100|Control Base]] in the Company Brain.

**Wiki Link:** [[CBP_REGISTRY|_REGISTRIES/CANONICAL/CBP_REGISTRY.yaml#B100]]