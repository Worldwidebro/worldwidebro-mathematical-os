# Worldwidebro OS Alignment

## What This Is

Worldwidebro OS Alignment is a documentation-and-data integrity pass over the Worldwidebro Holdings operating system. It fixes the broken repository↔venture data join in `REPOSITORY-REGISTRY.json`, then consolidates the OS's duplicate index, architecture, and workflow/master files down to the canonical set the Master Index Consolidation Plan called for.

## Core Value

If everything else in this project fails, the repository↔venture join in `REPOSITORY-REGISTRY.json` must be fixed and verified — every later consolidation, report, and capability-matching effort in this OS depends on being able to trust that file.

## Requirements

### Validated

(None yet — ship to validate)

### Active

- [ ] **REGISTRY-01**: `scan_repositories.py`'s starred-repo field-name bug is fixed and `REPOSITORY-REGISTRY.json` is rescanned so `related_ventures` coverage rises meaningfully above 14/1,597 (0.9%)
- [ ] **REGISTRY-02**: Duplicate repo registry files are archived, leaving `REPOSITORY-REGISTRY.json` + `GITHUB-REPOSITORIES-MASTER-LIST.md` as the only canonical pair
- [ ] **REGISTRY-03**: Venture-specific `REPO_REGISTRY.json` files are replaced by a `REPO-QUERY-FILTER.py` script that generates subsets from the canonical registry
- [ ] **NAV-01**: General navigation indexes collapse into a single `MASTER-INDEX.md` entry point linking all 4 hubs
- [ ] **NAV-02**: Resource indexes collapse into a new `RESOURCE-INVENTORY.md`
- [ ] **NAV-03**: Superseded index files are archived/deleted after content migration
- [ ] **NAV-04**: Task/workflow master files resolve to a single current playbook; superseded playbooks archived
- [ ] **ARCH-01**: A new `MASTER-ARCHITECTURE.md` documents the 4-layer structure, folder hierarchy, cross-references, gaps analysis, and tech stack by layer
- [ ] **ARCH-02**: Superseded architecture/structure files are archived
- [ ] **MASTER-01**: Venture/project master files are each confirmed current or consolidated if overlapping
- [ ] **MASTER-02**: Agent/registry master files are each checked for freshness and consolidated if overlapping, with `DECISION-RECORD-REGISTRY.md` kept separate as an audit trail

### Out of Scope

- Governance Charter policy implementation (Board structure, OPCO leadership appointments, compensation, escalation matrix) — organizational policy, not a documentation/data consolidation deliverable; unrelated to this project's file/data scope
- New dashboard or reporting UI — target runtime is Claude Code (file/script work); no UI phase is planned
- Deep capability-vocabulary rebuild for full repo↔venture semantic matching beyond the specific field-name fix — larger initiative, tracked as v2 (see REQUIREMENTS.md)
- Reconciling the `_superseded` vs. live copy of `GOVERNANCE-CHARTER.md` — flagged as a WARNING during doc ingestion, requires user confirmation outside this project's scope

## Context

This project sits inside the broader Worldwidebro Holdings OS (712 ventures, 18 OPCOs, 1,597 repos tracked in `REPOSITORY-REGISTRY.json`). It operationalizes two things surfaced during doc ingestion:

1. `MASTER-INDEX-CONSOLIDATION-PLAN.md` (2026-06-13, PRD) — calls for collapsing duplicate registries, indexes, architecture docs, playbooks, and master files down to canonical versions. Partially executed as of this ingest: `00-MASTER-INDEX.md` (research copy) was scheduled for Week-2 archival but is still live with no archive marker.
2. A known data-quality defect disclosed in `08-DATA/portfolio-reports/README.md`: only 14 of 1,597 repos (0.9%) carry a `related_ventures` link. Traced to `scan_repositories.py`'s `get_starred_repos()` (lines 40-41), which requests camelCase field names (`stargazerCount`, `primaryLanguage`, `forkCount`, `updatedAt`) via `gh api user/starred --jq`, when GitHub's REST v3 API actually returns snake_case fields for that endpoint (`stargazers_count`, `language`, `forks_count`, `updated_at`) — so those fields silently resolve to `null`/default instead of erroring, for all 734 starred repos. Confirmed directly in the script during roadmap creation.

A WARNING surfaced during doc ingestion: the ingested `GOVERNANCE-CHARTER.md` lives at a `_superseded/` path; a second, non-superseded copy is referenced elsewhere (`README-START-HERE.md`) but wasn't part of this ingest batch. This project's phases don't depend on governance-charter content, so it's non-blocking here — but the discrepancy should be resolved by the user independently (see `.planning/INGEST-CONFLICTS.md`).

## Constraints

- **Tech stack**: Target runtime is Claude Code (CLI agent) — deliverables are markdown files, a JSON registry, and Python scripts; no application UI is in scope.
- **Data integrity**: `gh api user/starred` returns GitHub REST v3 snake_case fields, while `gh repo list --json` uses its own camelCase field names — any repo-scanning script's `--jq`/`--json` field selectors must match the correct convention per command, or fields silently resolve to `null` instead of erroring.
- **Process**: Consolidation archives duplicate/superseded files rather than deleting outright — preserves an audit trail, consistent with the original PRD's own precedent of keeping `DECISION-RECORD-REGISTRY.md` separate for this reason.
- **Scope boundary**: Governance Charter content (Board structure, compensation, escalation matrix, etc.) is background context only, not a v1 requirement source — see Context above for the `_superseded` path conflict this ingest surfaced.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Exclude Governance Charter protocol/nfr content from v1 requirements | It's organizational policy (board, compensation, escalation), not a doc/data consolidation deliverable; also sourced from a `_superseded/` path per INGEST-CONFLICTS.md WARNING, so treating it as binding scope risks enshrining stale rules | ⚠️ Revisit — confirm with user whether the non-superseded charter copy should be ingested separately |
| Sequence the repo↔venture join fix (scan_repositories.py) as Phase 1, ahead of the ingested PRD's own file-consolidation ordering | It's the explicit user-supplied developer-facing success metric for this project and unblocks trustworthy data for every later consolidation/report | — Pending (validate after Phase 1 ships) |

---
*Last updated: 2026-07-03 after initial roadmap creation*
