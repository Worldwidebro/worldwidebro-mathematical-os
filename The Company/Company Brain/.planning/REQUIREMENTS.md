# Requirements: Company Brain — Gap Closure & Infrastructure Hardening

**Defined:** 2026-09-05
**Core Value:** Every claim in the vault should be verifiable against real state — no domain folder without a README, no infrastructure claim without a live check, no credential left in plaintext git history.

## v1 Requirements

### Structure

- [ ] **STRU-01**: Every domain folder (00-67) has a README.md — write the 15 missing ones (51-CONSTRUCTION, 53-TEAMS, 54-FINANCIAL, 55-LOOP-ENGINEERING, 57-CODE-INTELLIGENCE, 58-LOGISTICS, 59-MCP, 60-APIS, 61-KNOWLEDGE-SOURCES, 62-TECHNOLOGY, 63-CHANGE-MANAGEMENT, 64-RELATIONSHIPS, 65-SYNERGIES, 66-OPPORTUNITIES-ALT, 67-EVOLUTION-ALT)
- [ ] **STRU-02**: Domain READMEs are meaningfully cross-linked (target: 10+ real `[[wikilinks]]` each, not 3-6 breadcrumbs) for the ~53 domains that already have a README
- [ ] **STRU-03**: `66-OPPORTUNITIES-ALT` reconciled with canonical `38-OPPORTUNITIES` — either merged or the distinction documented and justified
- [ ] **STRU-04**: `67-EVOLUTION-ALT` reconciled with canonical `45-EVOLUTION` — either merged or the distinction documented and justified
- [ ] **STRU-05**: `CAMPAIGNS/` (223 files) and `COMMERCIAL/` (2 files) have an explicit placement decision relative to the numbered domain scheme (merge in, or documented as an intentional non-numbered structure like `SECTORS/`)

### Security

- [ ] **SECU-01**: Bitwarden CLI authenticated (`bw login` completed by user) and vault items created for OmniRoute and Mac Studio SSH credentials
- [ ] **SECU-02**: Both exposed passwords (OmniRoute, SSH) rotated after Bitwarden items exist
- [ ] **SECU-03**: `~/.claude/CLAUDE.md` (global instructions, outside this repo) has plaintext passwords removed, matching the fix already applied to the project CLAUDE.md
- [ ] **SECU-04**: Decision made and documented on whether `git filter-repo` history purge is needed (only required if the `~/Documents` repo is ever pushed to a remote)

### Observability

- [ ] **OBSV-01**: A Grafana instance exists and is reachable — live-verified 2026-09-05 that none currently exists on Mac Studio at all
- [ ] **OBSV-02**: Langfuse receives real traffic — `success_callback: ["langfuse"]` wired into `civos_litellm` config, verified by checking Langfuse UI shows traces after a test call

### Model Routing

- [ ] **MODL-01**: `civos_litellm`'s `model_list` has real distinct entries for `qwen-fast` and `qwen-heavy` (currently both alias the same single exo model as an unresolved 2026-08-12 stopgap)
- [ ] **MODL-02**: At least a meaningful subset of exo's other 119 catalog models are registered in LiteLLM (currently only 1 of 120 is reachable via OmniRoute)
- [ ] **MODL-03**: Ollama's `embed` route is re-enabled and verified working (currently disabled on a stale "Ollama is down" assumption that live checks disproved)
- [ ] **MODL-04**: OmniRoute's own provider config confirmed to correctly reach `civos_litellm` across the Docker network split (bridge vs. civos-network) — verified via the OmniRoute dashboard provider list, not assumed

## Out of Scope

Explicitly excluded. Documented to prevent scope creep.

| Feature | Reason |
|---------|--------|
| Lifecycle-stage taxonomy redesign (IDEA→OPPORTUNITY→...→PORTFOLIO) | Would add a third competing organizational scheme on top of the two just reconciled this session (50-domain grid + 36-fabric-base) — revisit only as a deliberate full replacement, not an addition |
| Capability Router, Agent Router, Policy Engine, bitemporal Routing Knowledge Graph | Real architectural gaps in CLAUDE.md's OmniRoute Routing Gaps table, but each is a standalone build decision requiring its own scoping, not a hardening/documentation fix |
| Individual venture work (SEC-NNN sectors, LT-005, CON-001, etc.) | This project is about the Company Brain shell itself, not the ventures it tracks |
| `fractal` submodule code changes | Confirmed to be a consumed third-party tool (`plasma-ai/fractal`), not something this project writes into |

## Traceability

Populated during roadmap creation.

| Requirement | Phase | Status |
|-------------|-------|--------|
| STRU-01 | TBD | Pending |
| STRU-02 | TBD | Pending |
| STRU-03 | TBD | Pending |
| STRU-04 | TBD | Pending |
| STRU-05 | TBD | Pending |
| SECU-01 | TBD | Pending |
| SECU-02 | TBD | Pending |
| SECU-03 | TBD | Pending |
| SECU-04 | TBD | Pending |
| OBSV-01 | TBD | Pending |
| OBSV-02 | TBD | Pending |
| MODL-01 | TBD | Pending |
| MODL-02 | TBD | Pending |
| MODL-03 | TBD | Pending |
| MODL-04 | TBD | Pending |

**Coverage:**
- v1 requirements: 15 total
- Mapped to phases: 0
- Unmapped: 15 ⚠️ (roadmap not yet created)

---
*Requirements defined: 2026-09-05*
*Last updated: 2026-09-05 after initial definition*
