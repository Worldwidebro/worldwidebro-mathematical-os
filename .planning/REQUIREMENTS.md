# Requirements: Worldwidebro OS Alignment

**Defined:** 2026-07-03
**Core Value:** If everything else in this project fails, the repository↔venture join in `REPOSITORY-REGISTRY.json` must be fixed and verified — every later consolidation, report, and capability-matching effort in this OS depends on being able to trust that file.

## v1 Requirements

Requirements for initial release. Each maps to roadmap phases.

### Registry (repo↔venture data integrity + registry consolidation)

- [ ] **REGISTRY-01**: `scan_repositories.py`'s `get_starred_repos()` field-name bug (camelCase `--jq` keys requested against the GitHub REST v3 API's snake_case response for `gh api user/starred`) is corrected, and `REPOSITORY-REGISTRY.json` is rescanned so `related_ventures` coverage rises meaningfully above the current 14/1,597 (0.9%)
- [ ] **REGISTRY-02**: `MASTER-REPO-REGISTRY.csv`, `MASTER_REPO_REGISTRY_COMPLETE.csv`, and the empty `REPO_REGISTRY.json` (venture-hub/) are archived, leaving `REPOSITORY-REGISTRY.json` (REFERENCE/) and `GITHUB-REPOSITORIES-MASTER-LIST.md` as the only two canonical repo-registry files
- [ ] **REGISTRY-03**: Venture-specific `REPO_REGISTRY.json` files (HRMS/, Automations/) are replaced by a `REPO-QUERY-FILTER.py` script that generates subsets (by venture_id, category, capabilities) from the canonical registry on demand

### Navigation (index & workflow master consolidation)

- [ ] **NAV-01**: General navigation indexes (`00-MASTER-INDEX.md`, `000-OBSIDIAN-MASTER-INDEX.md`, and the CEO Command Center's former `MASTER-INDEX.md`) collapse into the single `/Users/acebless/Documents/MASTER-INDEX.md` entry point linking all 4 hubs (STRATEGY, INFRASTRUCTURE, VENTURES, REFERENCE) plus resource inventory and architecture
- [ ] **NAV-02**: Resource indexes (`COMPLETE-RESOURCE-INDEX.md`, `DASHBOARD-INDEX.md`, `ARTIFACT-INDEX.md`) collapse into a new `RESOURCE-INVENTORY.md`
- [ ] **NAV-03**: `00-MASTER-INDEX.md` (research copy), `000-OBSIDIAN-MASTER-INDEX.md`, `COMPLETE-RESOURCE-INDEX.md`, `DASHBOARD-INDEX.md`, and `ARTIFACT-INDEX.md` are archived after their content is migrated (closing the gap noted in INGEST-CONFLICTS.md — `00-MASTER-INDEX.md` was scheduled for Week-2 archival but is still live)
- [ ] **NAV-04**: Task/workflow master files resolve to whichever of `COMPLETE-MASTER-PLAYBOOK.md` or `ORB-MASTER-CONNECTOR-2026-06-11.md` is most current/complete; `TODO-MASTER-CHECKLIST.md`, `WAVE_FINAL_MASTER_PREP.md`, and other superseded dated playbooks are archived

### Architecture (folder-structure documentation consolidation)

- [ ] **ARCH-01**: A new `MASTER-ARCHITECTURE.md` is created containing the 4-layer structure (STRATEGY, INFRASTRUCTURE, VENTURES, REFERENCE), folder hierarchy with purpose, cross-references to all hubs, a gaps-analysis section, and tech stack by layer
- [ ] **ARCH-02**: `MASTER-FOLDER-STRUCTURE.md`, `MASTER-FOLDER-MAP.md`, `COS-MASTER-ARCHITECTURE.md`, `MASTER-OS-ARCHITECTURE-AND-GAPS.md`, and `STRUCTURE-INDEX.md` are archived, superseded by `MASTER-ARCHITECTURE.md`

### Master (venture & agent registry audit)

- [ ] **MASTER-01**: `712-VENTURE-WORKFORCE-PLANNING-MASTER.md`, `CONSTRUCTION-SECTOR-BANKABILITY-MASTER.md`, and `SECTOR_FUNDING_STAFFING_MASTER_PLAN.md` are each confirmed current or archived; if all current, all 3 are kept as sector-specific; if overlapping, they're consolidated into a single `VENTURES-MASTER-PLAN.md`
- [ ] **MASTER-02**: `MASTER_AGENT_REGISTRY.md`, `DECISION-RECORD-REGISTRY.md`, `MASTER-AGENT-SPEC.md`, and `AI-BOSS-HOLDINGS-REPO-OS-INDEX.md` are each checked for freshness; overlapping agent registries are consolidated; `DECISION-RECORD-REGISTRY.md` is kept separate regardless (audit-trail requirement)

## v2 Requirements

Deferred to future release. Tracked but not in current roadmap.

### Data Quality

- **DATA-01**: Capability-vocabulary mismatch between repo capabilities and venture `required_capabilities` is resolved beyond the `scan_repositories.py` field-name fix (deeper semantic matching, full repo↔venture join accuracy)
- **DATA-02**: The 3 sectors with no OPCO mapping and the 5 OPCOs with zero ventures (both flagged in `08-DATA/portfolio-reports/README.md`) are resolved via Board decision

### Governance

- **GOV-01**: The canonical location of `GOVERNANCE-CHARTER.md` is confirmed (the `_superseded/` copy ingested in this batch vs. the copy referenced by `README-START-HERE.md`) and the two are reconciled or the stale one is formally retired

## Out of Scope

Explicitly excluded. Documented to prevent scope creep.

| Feature | Reason |
|---------|--------|
| Governance Charter policy implementation (Board structure, OPCO leadership appointments, compensation, escalation matrix) | Organizational policy, not a documentation/data consolidation deliverable — unrelated to this project's file/data scope |
| New dashboard or reporting UI | Target runtime is Claude Code (file/script work); no UI phase is planned |
| Deep capability-vocabulary rebuild for full repo↔venture semantic matching | Larger initiative beyond the specific field-name bug fix; tracked as v2 DATA-01 |
| Reconciling `_superseded` vs. live `GOVERNANCE-CHARTER.md` copies | Requires user confirmation outside this project's scope; tracked as v2 GOV-01 |

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| REGISTRY-01 | Phase 1 | Pending |
| REGISTRY-02 | Phase 1 | Pending |
| REGISTRY-03 | Phase 1 | Pending |
| NAV-01 | Phase 2 | Pending |
| NAV-02 | Phase 2 | Pending |
| NAV-03 | Phase 2 | Pending |
| NAV-04 | Phase 2 | Pending |
| ARCH-01 | Phase 3 | Pending |
| ARCH-02 | Phase 3 | Pending |
| MASTER-01 | Phase 4 | Pending |
| MASTER-02 | Phase 4 | Pending |

**Coverage:**
- v1 requirements: 11 total
- Mapped to phases: 11
- Unmapped: 0 ✓

---
*Requirements defined: 2026-07-03*
*Last updated: 2026-07-03 after initial roadmap creation*
