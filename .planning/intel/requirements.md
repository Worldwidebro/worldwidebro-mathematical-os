# Requirements (from PRDs)

Source PRD: `/Users/acebless/Documents/WORLDWIDEBRO-OS/07-KNOWLEDGE/research/MASTER-INDEX-CONSOLIDATION-PLAN.md` ("Master Index Consolidation Plan", analysis date 2026-06-13, precedence 1)

Only one PRD was present in this ingest batch, so no cross-PRD competing-acceptance-variant conflicts exist for this run (that check requires 2+ PRDs on the same scope).

---

## REQ-consolidate-repo-registries
- **source:** MASTER-INDEX-CONSOLIDATION-PLAN.md
- **description:** Consolidate 7 duplicate/overlapping repository registry files down to 2 canonical files.
- **scope:** repository registries
- **acceptance criteria:**
  - `REPOSITORY-REGISTRY.json` (1,592 repos, REFERENCE/) kept as single source of truth
  - `GITHUB-REPOSITORIES-MASTER-LIST.md` kept as human-readable index
  - `MASTER-REPO-REGISTRY.csv`, `MASTER_REPO_REGISTRY_COMPLETE.csv`, empty `REPO_REGISTRY.json` (venture-hub/) archived/deleted
  - Venture-specific `REPO_REGISTRY.json` (HRMS/, Automations/) replaced by a `REPO-QUERY-FILTER.py` script that generates subsets from the main registry (by venture_id, category, capabilities)

## REQ-consolidate-index-masters
- **source:** MASTER-INDEX-CONSOLIDATION-PLAN.md
- **description:** Consolidate 8 overlapping index files down to 3 unified masters.
- **scope:** master/navigation indexes
- **acceptance criteria:**
  - General indexes (`00-MASTER-INDEX.md`, `MASTER-INDEX.md`, `000-OBSIDIAN-MASTER-INDEX.md`) collapse into a single `MASTER-INDEX.md` entry point linking all 4 hubs (STRATEGY, INFRASTRUCTURE, VENTURES, REFERENCE) plus resource inventory and architecture
  - Resource indexes (`COMPLETE-RESOURCE-INDEX.md`, `DASHBOARD-INDEX.md`, `ARTIFACT-INDEX.md`) collapse into new `RESOURCE-INVENTORY.md`
  - Session/temporal indexes (e.g. `SESSION-INDEX-2026-06-11.md`) archived when session ends
  - `00-MASTER-INDEX.md`, `000-OBSIDIAN-MASTER-INDEX.md`, `COMPLETE-RESOURCE-INDEX.md`, `DASHBOARD-INDEX.md`, `ARTIFACT-INDEX.md` deleted (archived) by Week 2
- **note:** See INGEST-CONFLICTS.md [INFO] — as of this ingest, `00-MASTER-INDEX.md` (classified in this same batch, source `WORLDWIDEBRO-OS/07-KNOWLEDGE/research/00-MASTER-INDEX.md`) is still live and shows no archive marker, so this requirement's acceptance criteria appear only partially executed. `/Users/acebless/Documents/MASTER-INDEX.md` does now function as a single broad entry point (consistent with the intent here), though its current content describes a "4-Orb" model rather than the specific "CEO Command Center entry point" framing this PRD used in 2026-06-13.

## REQ-consolidate-architecture-masters
- **source:** MASTER-INDEX-CONSOLIDATION-PLAN.md
- **description:** Merge 5 overlapping architecture/structure files into 1 unified master.
- **scope:** architecture/folder-structure documentation
- **acceptance criteria:**
  - New `MASTER-ARCHITECTURE.md` created containing: 4-layer structure (STRATEGY, INFRASTRUCTURE, VENTURES, REFERENCE), folder hierarchy with purpose, cross-references to all hubs, gaps analysis section, tech stack by layer
  - `MASTER-FOLDER-STRUCTURE.md`, `MASTER-FOLDER-MAP.md`, `COS-MASTER-ARCHITECTURE.md`, `MASTER-OS-ARCHITECTURE-AND-GAPS.md`, `STRUCTURE-INDEX.md` deleted (superseded by the new file)

## REQ-consolidate-task-workflow-masters
- **source:** MASTER-INDEX-CONSOLIDATION-PLAN.md
- **description:** Resolve 5+ overlapping task/workflow master files down to whichever is current.
- **scope:** task/workflow/playbook documentation
- **acceptance criteria:**
  - Keep the most recent/complete of `COMPLETE-MASTER-PLAYBOOK.md` or `ORB-MASTER-CONNECTOR-2026-06-11.md`
  - Archive `TODO-MASTER-CHECKLIST.md` (if superseded), `WAVE_FINAL_MASTER_PREP.md`, and any other dated playbooks

## REQ-verify-venture-project-masters
- **source:** MASTER-INDEX-CONSOLIDATION-PLAN.md
- **description:** Verify currency of 3 venture/project-specific master files; consolidate only if they overlap.
- **scope:** venture-specific master plans
- **acceptance criteria:**
  - `712-VENTURE-WORKFORCE-PLANNING-MASTER.md`, `CONSTRUCTION-SECTOR-BANKABILITY-MASTER.md`, `SECTOR_FUNDING_STAFFING_MASTER_PLAN.md` each confirmed current or archived
  - If all current: keep all 3 (sector-specific). If overlapping: consolidate into 1 `VENTURES-MASTER-PLAN.md`

## REQ-verify-registry-agent-masters
- **source:** MASTER-INDEX-CONSOLIDATION-PLAN.md
- **description:** Verify authoritative status of 4 agent/registry master files; consolidate duplicates, preserve audit trail.
- **scope:** agent registries, decision records
- **acceptance criteria:**
  - `MASTER_AGENT_REGISTRY.md`, `DECISION-RECORD-REGISTRY.md`, `MASTER-AGENT-SPEC.md`, `AI-BOSS-HOLDINGS-REPO-OS-INDEX.md` each checked for freshness
  - Overlapping agent registries consolidated
  - `DECISION-RECORD-REGISTRY.md` kept separate regardless (audit trail requirement)
