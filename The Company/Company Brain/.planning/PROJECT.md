# Company Brain — Gap Closure & Infrastructure Hardening

## What This Is

Company Brain is an Obsidian markdown vault + light infrastructure (Python FastMCP server, bash CLI, Docker-based Neo4j/Qdrant/Postgres/LiteLLM/Langfuse stack on a remote Mac Studio) that acts as Worldwidebro Holdings' organizational knowledge base and control plane. This GSD project doesn't build new product — it tracks closing the gap between what the vault *claims* (a complete 20-layer/50-domain/500-control-point cognitive architecture) and what's *actually true*, across both the documentation/structure layer and the live infrastructure it describes.

## Core Value

Every claim in the vault should be verifiable against real state — no domain folder without a README, no infrastructure claim without a live check, no credential left in plaintext git history.

## Requirements

### Validated

- ✓ Domain-folder numbering collisions resolved — 17 folders that collided across two competing schemes (the 50-domain grid vs. a 36-fabric-base alt scheme) renumbered into a 51-67 extension range; zero duplicate prefixes remain — 2026-09-05
- ✓ `RESEARCH/` merged into `37-RESEARCH/`, all internal links repaired — 2026-09-05
- ✓ Two stray sync-duplicate directories (`_REGISTRIES 1/`, `graft 1/`) confirmed as zero-unique-content and deleted — 2026-09-05
- ✓ Orphaned root file `START-HERE-RESEARCH.md` wikilinked back into `STARTHERE.md`; 3 dated session artifacts archived to `_ARCHIVE/session-artifacts/` — 2026-09-05
- ✓ Full codebase map generated (`.planning/codebase/`: STACK, ARCHITECTURE, STRUCTURE, CONVENTIONS, TESTING, INTEGRATIONS, CONCERNS) — 2026-09-05
- ✓ Plaintext OmniRoute/SSH passwords removed from `CLAUDE.md`, replaced with Bitwarden item pointers (Bitwarden CLI installed, login pending) — 2026-09-05
- ✓ Live infra re-audit corrected several stale claims in CLAUDE.md: Ollama is actually running (not dead), exo has 120 models in its catalog (not 1), LiteLLM's routing strategy is already `usage-based-routing-v2` (not `simple-shuffle`) — 2026-09-05
- ✓ Live `docker ps` check confirmed the duplicate-Docker-stack problem CLAUDE.md described (2x Neo4j/Qdrant/etc.) is already resolved — only one instance of each core service runs now; `t7shield-neo4j-1` no longer exists at all — 2026-09-05
- ✓ Core services verified healthy via live checks: OmniRoute, Neo4j, Qdrant, LiteLLM, Langfuse, exo, Ollama (all responding) — 2026-09-05

### Active

- [ ] Write README.md for the 15 domain folders that still have none (51-CONSTRUCTION, 53-TEAMS, 54-FINANCIAL, 55-LOOP-ENGINEERING, 57-CODE-INTELLIGENCE, 58-LOGISTICS, 59-MCP, 60-APIS, 61-KNOWLEDGE-SOURCES, 62-TECHNOLOGY, 63-CHANGE-MANAGEMENT, 64-RELATIONSHIPS, 65-SYNERGIES, 66-OPPORTUNITIES-ALT, 67-EVOLUTION-ALT)
- [ ] Deepen wikilinks in domain READMEs that only carry 3-6 shallow breadcrumb links (most of the ~53 existing READMEs)
- [ ] Resolve `66-OPPORTUNITIES-ALT` vs. canonical `38-OPPORTUNITIES`, and `67-EVOLUTION-ALT` vs. canonical `45-EVOLUTION` — merge-candidates, not yet reconciled
- [ ] Decide placement of `CAMPAIGNS/` (223 files) and `COMMERCIAL/` (2 files) relative to the numbered domain scheme
- [ ] Complete Bitwarden login and create vault items for OmniRoute and Mac Studio SSH credentials; rotate both passwords once stored
- [ ] Purge exposed credentials from git history (`git filter-repo`) if this repo (rooted at `~/Documents`) is ever pushed to a remote
- [ ] Deploy/restore a Grafana instance — live-verified 2026-09-05 that none exists at all right now (not on :3010, not on :3011); observability has no dashboard, only Langfuse tracing (which itself receives zero traffic, see below)
- [ ] Wire Langfuse callback into `civos_litellm` config so observability actually captures traffic
- [ ] Register exo's other 119 models and Ollama's 6 live models into LiteLLM's `model_list` (currently only 1 of 120 exo models and 0 of 6 Ollama models are reachable via OmniRoute)
- [ ] Confirm whether OmniRoute's provider config crosses its Docker network gap to `civos_litellm` (bridge vs. civos-network) via the OmniRoute dashboard

### Out of Scope

- Full lifecycle-stage taxonomy redesign (IDEA→OPPORTUNITY→...→PORTFOLIO, a third organizational scheme proposed 2026-09-05) — would recreate the exact multi-scheme collision problem just resolved; revisit only as a deliberate full replacement of the 50-domain scheme, not an addition alongside it
- Capability Router, Agent Router, Policy Engine, bitemporal Routing Knowledge Graph (the 4 "High effort, architecture decision" gaps in CLAUDE.md's OmniRoute Routing Gaps table) — real gaps, but each is a standalone build decision, not a documentation/hardening fix
- Any venture-specific work (individual SEC-NNN sectors, LT-005, CON-001, etc.) — this project is about the Company Brain shell itself, not the ventures it tracks

## Context

- This is a **nested subdirectory inside a much larger git repo** — `git rev-parse --show-toplevel` resolves to `/Users/acebless/Documents`, not this folder. GSD commits here land in that outer repo.
- CLAUDE.md (project root) is the vault's own living "verified state" ledger — it already practices the pattern this project formalizes (correct stale claims in-place, cite live checks). Treat it as a primary source, but verify before trusting any un-dated claim in it.
- `.planning/codebase/CONCERNS.md` is the fullest single inventory of known gaps as of 2026-09-05 — read it before planning phases.
- Two competing organizational schemes were both partially materialized as real folders before this session (the 50-domain grid from README.md/INDEX.md, and a 36-fabric-base scheme from `_ONTOLOGY/FABRICS.yaml`) — this caused the 17-folder renumbering. Any future structural work should check both schemes before assuming a folder is orphaned scatter.
- Credentials workflow: Bitwarden CLI (`bw`) is installed but unauthenticated on this machine — login requires the user to run `bw login` themselves (master password should never pass through chat).

## Constraints

- **Repo topology**: All git operations happen inside a repo rooted at `~/Documents`, not this vault folder — be deliberate about what gets committed and staged.
- **No destructive infra changes without live verification**: per the vault's own "ONE RULE" (CLAUDE.md) — verify via `docker ps`, actual CLI output, or live queries before claiming any infra fix landed.
- **Credentials**: never handle master passwords or raw secrets through chat; use `bw` CLI session tokens once the user authenticates, or ask the user to perform the sensitive step directly.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Renumber duplicate-numbered domain folders into 51-67 rather than pick-and-delete | Both competing schemes had real, non-trivial content (e.g. `13_ENGINEERING`→`56-ENGINEERING` had 266 files, 43 inbound references) — deletion would have destroyed real work | ✓ Good |
| Credentials move to Bitwarden, not deleted outright | User has an existing Bitwarden setup; pointer-based references in CLAUDE.md keep the doc useful without holding secrets | — Pending (blocked on `bw login`) |
| Project scope includes live infrastructure, not just vault docs | User explicitly chose "Both" when asked — the CONCERNS.md findings and CLAUDE.md's own fresh audit are inseparable from the documentation gaps | ✓ Good |
| Third "lifecycle taxonomy" reorg proposal deferred, not adopted | Would add a third competing organizational scheme on top of the two just reconciled | — Pending (user has not ruled it out for later) |

## Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition** (via `/gsd-transition`):
1. Requirements invalidated? → Move to Out of Scope with reason
2. Requirements validated? → Move to Validated with phase reference
3. New requirements emerged? → Add to Active
4. Decisions to log? → Add to Key Decisions
5. "What This Is" still accurate? → Update if drifted

**After each milestone** (via `/gsd-complete-milestone`):
1. Full review of all sections
2. Core Value check — still the right priority?
3. Audit Out of Scope — reasons still valid?
4. Update Context with current state

---
*Last updated: 2026-09-05 after initialization*
