# Roadmap: Worldwidebro OS Alignment

## Overview

Worldwidebro OS Alignment closes the gap between the Worldwidebro Holdings OS's documentation/data and what's actually true. It starts with the most concrete, verifiable problem — the repository↔venture data join that's silently returning 0.9% coverage because of a field-name mismatch in `scan_repositories.py` — then works outward through the three families of duplicate/overlapping master files identified in the Master Index Consolidation Plan (indexes & workflow playbooks, architecture docs, and venture/agent registries), collapsing each family down to its canonical file(s) so the OS has one trustworthy source per concern instead of several competing copies.

## Phases

**Phase Numbering:**
- Integer phases (1, 2, 3): Planned milestone work
- Decimal phases (2.1, 2.2): Urgent insertions (marked with INSERTED)

Decimal phases appear between their surrounding integers in numeric order.

- [ ] **Phase 1: Repository Registry Integrity** - Fix the repo↔venture join bug and consolidate repo registry files down to 2 canonical ones
- [ ] **Phase 2: Index & Workflow Documentation Consolidation** - Collapse duplicate navigation indexes, resource indexes, and task/workflow playbooks into canonical files
- [ ] **Phase 3: Architecture Documentation Consolidation** - Merge 5 overlapping architecture/folder-structure files into 1 unified `MASTER-ARCHITECTURE.md`
- [ ] **Phase 4: Venture & Agent Master File Audit** - Verify freshness of venture/project and agent/registry master files, consolidating only where they overlap

## Phase Details

### Phase 1: Repository Registry Integrity
**Goal**: `REPOSITORY-REGISTRY.json` is the single trustworthy source of truth for which repos serve which ventures
**Depends on**: Nothing (first phase)
**Requirements**: REGISTRY-01, REGISTRY-02, REGISTRY-03
**Success Criteria** (what must be TRUE):
  1. Running `scan_repositories.py` produces starred-repo entries with real stars/language/forks values instead of nulls caused by the camelCase/snake_case field mismatch
  2. `REPOSITORY-REGISTRY.json`'s `related_ventures` coverage rises meaningfully above 14/1,597 (0.9%) after rescanning
  3. Only `REPOSITORY-REGISTRY.json` and `GITHUB-REPOSITORIES-MASTER-LIST.md` remain as repo-registry files; duplicate CSVs and the empty JSON are archived
  4. Venture-scoped repo subsets (e.g., for HRMS, Automations) are produced by running `REPO-QUERY-FILTER.py` against the canonical registry rather than maintaining separate hand-edited registries
**Plans**: TBD

### Phase 2: Index & Workflow Documentation Consolidation
**Goal**: Anyone opening the OS finds one obvious, current entry point and one current task/workflow playbook — no competing indexes
**Depends on**: Nothing (independent of Phase 1)
**Requirements**: NAV-01, NAV-02, NAV-03, NAV-04
**Success Criteria** (what must be TRUE):
  1. A single `MASTER-INDEX.md` links all 4 hubs (STRATEGY, INFRASTRUCTURE, VENTURES, REFERENCE) plus resource inventory and architecture
  2. `RESOURCE-INVENTORY.md` exists as the one place listing dashboards/artifacts/resources, replacing 3 separate resource indexes
  3. The superseded index files no longer exist at their old paths (archived, not left as silent duplicates) — including `00-MASTER-INDEX.md`, which the original consolidation plan flagged for Week-2 archival but which remained live as of this ingest
  4. Exactly one current task/workflow playbook remains referenced from the master index; other dated playbooks are archived
**Plans**: TBD

### Phase 3: Architecture Documentation Consolidation
**Goal**: The OS has one authoritative architecture document instead of five competing ones
**Depends on**: Phase 2 (the new `MASTER-INDEX.md` links to this document)
**Requirements**: ARCH-01, ARCH-02
**Success Criteria** (what must be TRUE):
  1. `MASTER-ARCHITECTURE.md` exists and documents the 4-layer structure, folder hierarchy with purpose, cross-references to all hubs, a gaps-analysis section, and tech stack by layer
  2. The five prior architecture/structure files are archived, with their content merged into `MASTER-ARCHITECTURE.md` first
**Plans**: TBD

### Phase 4: Venture & Agent Master File Audit
**Goal**: Every "master" file claiming authority for ventures or agents/registries is confirmed current or explicitly archived — no silent duplicates left unresolved
**Depends on**: Phase 2 (uses the consolidated master index as the place these audit results get linked from)
**Requirements**: MASTER-01, MASTER-02
**Success Criteria** (what must be TRUE):
  1. Each of the 3 venture/project master files is confirmed current, or overlapping ones are merged into a single `VENTURES-MASTER-PLAN.md`
  2. Each of the 4 agent/registry master files is confirmed fresh; overlapping ones are consolidated
  3. `DECISION-RECORD-REGISTRY.md` remains a separate, untouched audit trail regardless of what else is consolidated
**Plans**: TBD

## Progress

**Execution Order:**
Phases execute in numeric order: 1 → 2 → 3 → 4

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Repository Registry Integrity | 0/TBD | Not started | - |
| 2. Index & Workflow Documentation Consolidation | 0/TBD | Not started | - |
| 3. Architecture Documentation Consolidation | 0/TBD | Not started | - |
| 4. Venture & Agent Master File Audit | 0/TBD | Not started | - |
