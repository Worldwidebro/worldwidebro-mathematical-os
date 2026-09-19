# CLAUDE.md — Company Brain (Session Guidance)

**Scope:** Active session instructions only; reference docs in `_REFERENCE/` and master plan in global ~/.claude/CLAUDE.md  
**Updated:** 2026-09-19  
**Authority:** Infrastructure CP-027 + Execution CP-033 + Revenue CP-021  
**Current Phase:** Week 2 Revenue Scaling (Sep 16–22) | [[ANTIGRAVITY|ANTIGRAVITY.md]] (45 operating rules)

---

## STATUS SNAPSHOT — Sep 19, 2026

✅ **Phase 1 LOCKED** (Sep 6-15) — Agent Enablement complete, audit system operational  
✅ **Phase 2 LAUNCHED** (Sep 16-30) — Graph-native refactor (Neo4j schema deployment Sep 18)  
✅ **Infrastructure LIVE** — Neo4j (20,363 edges, constraints deployed), Qdrant (17,236 vectors), OmniRoute, Ollama  
✅ **6 Tier-0 Ventures Verified** — All deployed and HTTP 200:
- **OPS-001, LT-005, CALLCENTER** (Revenue-Ready) → Making revenue calls Week 2
- **CON-001, RE-001** (Demo-Ready) → API/engine builds Week 2-3
- **LT-011** (Skeleton) → Assessment Week 2

📊 **Week 1 Result:** TBD (Sep 10-15 execution) | **Week 2 Target:** $10K–$25K (scaling)

---

## WEEK 2 EXECUTION FOCUS (Sep 16–22)

**Master plan:** [[WEEK1-EXECUTION-PLAN|20-DECISIONS/WEEK1-EXECUTION-PLAN.md]] + [[PHASE-2A-AGENTIC-ENGINEERING-PLAN|20-DECISIONS/PHASE-2A-AGENTIC-ENGINEERING-PLAN.md]]

### Three Revenue-Ready Ventures (Scaling Week 2)
1. **OPS-001** → Cold call campaign + lead follow-up (ANTIGRAVITY Rule 44: Execute → Observe → Verify)
2. **LT-005** → B2B outreach scaling + booking automation (Rule 2: Determine problem, user, outcome)
3. **CALLCENTER** → Live call routing + quality scoring (Rule 18: Observability mandated)

### Parallel: Graph-Native Phase 2 (Sep 18–30)
- **Neo4j Schema:** Deployed Sep 18 (constraints, indexes, integrity gates live)
- **YAML→Graph Pipeline:** 14-day migration (Sep 17–Oct 1)
- **Agent Context Assembly:** Subgraph queries for L2/L3 autonomy

**See also:** [[VENTURE-AUDIT-FRAMEWORK|20-DECISIONS/VENTURE-AUDIT-FRAMEWORK.md]] (12-layer, Rule 2 enforced) + [[PHASE-2-PHASE-2A-INTEGRATION-MAP|20-DECISIONS/PHASE-2-PHASE-2A-INTEGRATION-MAP.md]]

---

## NAMING CONSOLIDATION

**One system, one name: VEX**

| What | GitHub | Deployed | Status |
|------|--------|----------|--------|
| **VEX** | Worldwidebro/Worldwidebro-Vex | vex-hero-site-sigma.vercel.app | ✅ Portfolio live |
| Growth OS | Worldwidebro/worldwidebro-marketing-os | localhost:3030 | ✅ Dashboard live |

**Removed:** "Venture Portal", "Hermes Command Center" (old naming)

---

## QUICK REFERENCE

**Logic Architecture:** [[_DOCS/LOGIC-ARCHITECTURE-FRAMEWORK.md]] (72 logic layers, 12 domains, 72 control points, autonomous loop patterns) — [[_REGISTRIES/CANONICAL/LOGIC_LAYERS_REGISTRY.yaml|Master Registry]]  
**Infrastructure Status:** [[INFRASTRUCTURE-STATUS-2026-09|_REFERENCE/INFRASTRUCTURE-STATUS-2026-09.md]]  
**Venture Roadmap:** [[VENTURE-ROADMAP-2026-09|_REFERENCE/VENTURE-ROADMAP-2026-09.md]]  
**Digital Librarian:** [[DIGITAL-LIBRARIAN-ARCHITECTURE|_REFERENCE/DIGITAL-LIBRARIAN-ARCHITECTURE.md]]

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
