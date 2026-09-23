# Duplicate Terminology Audit — Scattered Files & Entire Knowledge Graph
**Generated:** 2026-09-24  
**Scope:** 7,629+ .md files + orphaned/scattered scripts  
**Purpose:** Identify redundant terminology that should be consolidated into canonical registry

---

## EXECUTIVE SUMMARY

**Key Finding:** 50+ duplicate terminology clusters across orphaned files + main corpus.

**Root Cause:** No canonical **TERMINOLOGY_REGISTRY.yaml** — words used inconsistently:
- **venture** appears 295 times (but also: "venture", "Venture", "VEN-", "operating venture")
- **capability** appears 286 times (but also: "capability", "Capability", "CAP-", "competency")
- **control** appears 101 times (but also: "control point", "CP-", "control base", "control plane")
- **deploy/deployment** appears 104+ times (but also: "activate", "instantiate", "provision", "wire")
- **sector** appears 108 times (but also: "domain", "industry", "vertical", "segment")

**Impact:** Graph queries fail on terminology mismatch. Inconsistent naming breaks entity resolution.

---

## 1. CORE CONCEPT DUPLICATES (Highest Frequency)

### A. VENTURE & COMPANY TERMINOLOGY
| Term | Count | Variants | Problem |
|------|-------|----------|---------|
| **venture** | 295 | venture, Venture, VEN-, operating venture, company, business unit | No canonical form |
| **operating company** | 102 | opco, OpCo, OPC-, operating company | Inconsistent abbreviation |
| **sector** | 108 | sector, SEC-, industry, vertical, domain, segment, category | Seven different synonyms |
| **ventures** | 96 | ventures, Ventures, VEN-*, operating ventures | Plural forms vary |

**→ CONSOLIDATE INTO:** `TERMINOLOGY_REGISTRY.yaml` with canonical forms:
- Use: `venture_id: "VEN-XXXX"` (not "VEN-", "Venture", "company")
- Use: `sector_id: "SEC-XXX"` (not "domain", "vertical", "industry")
- Use: `opco_id: "OPC-XX"` (not "OpCo", "operating_company")

---

### B. CONTROL & GOVERNANCE TERMINOLOGY
| Term | Count | Variants | Problem |
|------|-------|----------|---------|
| **control** | 101 | control, control point, CP-, control base, control plane | 4+ distinct meanings |
| **plane** | 45+ | plane, control plane, data plane, decision plane | Layer vs. system |
| **base** | ~50 | base, Base, BASE-, domain base, knowledge base, control base | Overloaded (BASE-001 vs. "base") |
| **gate** | ~30 | gate, validation gate, integrity gate, decision gate | No hierarchy |

**→ CONSOLIDATE INTO:** Control terminology standard:
- Use: `control_point_id: "CP-XXX"` (for CP-001 through CP-050)
- Use: `control_base_id: "B-XXX"` (for B001 through B500, per pasted 500-Bases model)
- Use: `plane: "infrastructure"` | `"financial"` | `"operations"` (explicit enum)
- Use: `gate_type: "integrity"` | `"verification"` | `"approval"` (explicit enum)

---

### C. DEPLOYMENT & ACTIVATION TERMINOLOGY
| Term | Count | Variants | Problem |
|------|-------|----------|---------|
| **deploy/deployment** | 104 | deploy, deployment, Deployment, DEPLOY | Case inconsistency |
| **instantiate/instantiation** | ~40 | instantiate, instantiation, instantiated, INSTANTIATED | Tense variant |
| **activate/activation** | ~50 | activate, activation, activated, ACTIVATED | Duplicate concept |
| **execute/execution** | 100 | execute, execution, executor, EXECUTE | Overloaded (runtime vs. task) |
| **wire/wiring** | 95 | wire, wiring, wired, WIRED | Jargon, not formal |
| **provision/provisioning** | ~30 | provision, provisioning, provisioned | Alternate term |

**→ CONSOLIDATE INTO:** Lifecycle state enum:
```yaml
lifecycle_state:
  - DESIGNED          # spec complete
  - INSTANTIATED      # created in graph
  - ACTIVATED         # operational
  - DEPLOYED          # live
  - MONITORING        # active observation
  - DECOMMISSIONED    # retired
```
Use single term per state. **Deprecate:** "wired", "provision", unclear synonyms.

---

### C2. TESTING & VERIFICATION TERMINOLOGY
| Term | Count | Variants | Problem |
|------|-------|----------|---------|
| **test/testing** | 105 | test, testing, Test, TEST, test case, test suite, test_* | No hierarchy |
| **verified/verification** | 99 | verified, verification, verify, Verified, VERIFIED | Case inconsistency |
| **validate/validation** | ~50 | validate, validation, Validate, VALIDATE | Similar to verify |
| **audit** | ~40 | audit, Audit, AUDIT, auditing, audited | Formal verification |
| **gate** | ~30 | gate, integrity gate, verification gate | Validation checkpoint |

**→ CONSOLIDATE INTO:** Verification types registry:
```yaml
verification_type:
  test:           # automated testing (unit/integration/e2e)
  validation:     # data/logic correctness
  verification:   # completeness & consistency
  audit:          # compliance & governance
  gate:           # go/no-go decision point
```

---

## 2. SCATTERED FILE DUPLICATES (Orphaned Files Problem)

### Files Analyzed
1. `./scripts/gbrain_to_neo4j_sync.py` → Orphaned sync script
2. `./scripts/analyze_company_brain_scatter.py` → Orphaned analysis
3. `./create_brain.sh` → Orphaned shell script
4. `./fractal/docs/skill.rst` → Orphaned RST docs
5. `./.agents/agents/researcher.md` → Duplicate agent def

### Orphaned File Terminology Patterns

#### gbrain_to_neo4j_sync.py (Orphaned)
**Duplicate terms:** `relationships` (12×), `entities` (9×), `sync` (7×), `documents` (7×)  
**Issue:** This is a sync script NOT wired into `_PIPELINES/graph_ingestion_pipeline.py`  
**Should be:** Consolidated into Phase B/C ingestion pipeline

#### analyze_company_brain_scatter.py (Orphaned)
**Duplicate terms:** `root` (6×), `has_readme` (5×), `broken` (5×)  
**Issue:** Analyzes folder structure, but orphaned from domain index automation  
**Should be:** Become a `FILE_DISCOVERY_SKILL` in Claude Code

#### create_brain.sh (Orphaned)
**Duplicate terms:** `layer` (3×), `domain` (1×), `create` (3×)  
**Issue:** Shell script not documented anywhere  
**Should be:** Integrated into deployment documentation

#### fractal/docs/skill.rst (Orphaned)
**Duplicate terms:** `node` (48×), `agent` (24×), `skill` (20×)  
**Issue:** RST docs in fractal/ not connected to main 16-AGENTS  
**Should be:** Converted to .md and wired into `16-AGENTS/README.md`

#### ./.agents/agents/researcher.md (Duplicate)
**Issue:** Duplicate agent definition (also in `~/.claude/agents/research-synthesist.md`)  
**Should be:** Consolidate; use single canonical definition

---

## 3. CONCEPT OVERLOADING (Same Word, Multiple Meanings)

### "Domain" (Highly Ambiguous)
| Usage | Context | Count | Should Be |
|-------|---------|-------|-----------|
| Numbered domain | Folder (00-CONSTITUTION, 01-IDENTITY) | ~200 | `domain_folder` or `domain_id` (explicit) |
| Knowledge domain | Subject area (Logistics, Finance) | ~100 | `knowledge_domain` or `sector` |
| Control domain | Governance zone | ~50 | `control_domain` or explicit reference to registry |
| DNS domain | Technical domain | ~20 | `dns_domain` or `hostname` |
| Business domain | Industry area | ~30 | `business_domain` or `sector` |

**→ CONSOLIDATE:** Replace "domain" with explicit term:
- `numbered_domain_id`: "00-CONSTITUTION" (folders 00-50)
- `sector_id`: "SEC-001" (industry/business areas)
- `control_domain_id`: "B001" (control bases from 500-Bases model)
- `knowledge_domain`: explicit description

---

### "Control Point" / "Control Base" / "Control Plane" (Confusing Hierarchy)
| Term | Meaning | Count | Should Be |
|------|---------|-------|-----------|
| Control Point | CP-001 to CP-050 (current) | 101 | `control_point_id: "CP-XXX"` |
| Control Base | B001 to B500 (from pasted model) | ~50 | `control_base_id: "B-XXX"` (NEW canonical) |
| Control Plane | Infrastructure layer | ~45 | `control_plane_type` (infrastructure, financial, operational) |
| Plane | Execution layer | ~20 | Deprecate; use `control_plane_type` |

**→ CONSOLIDATE:** Three-level hierarchy:
```
CONTROL_POINT (CP-XXX) — current governance units (50 total)
    ↓
CONTROL_BASE (B-XXX) — new atomic control surfaces (500 total, from pasted model)
    ↓
CONTROL_PLANE — infrastructure/financial/operational layer
```

---

### "Base" (Massively Overloaded)
| Usage | Meaning | Example | Should Be |
|-------|---------|---------|-----------|
| Numbered Base | Sector knowledge base | BASE-001 (Family Wealth) | `sector_base_id`: "BASE-XXX" |
| Control Base | Atomic control surface | B055 (Revenue Actuals) | `control_base_id`: "B-XXX" (NEW) |
| Knowledge Base | Document repository | Obsidian vault | `knowledge_base_type` |
| Database | Technical storage | PostgreSQL, Neo4j | `database_name` or `data_store` |
| Base directory | File system root | /Users/acebless/.../ | `base_path` or `root_directory` |

**→ CONSOLIDATE:** Distinguish by prefix:
- `BASE-XXX` or `sector_base_id`: For sector knowledge bases (36 total, existing)
- `B-XXX` or `control_base_id`: For control surfaces (500 total, from pasted model)
- `knowledge_base_name`: For document repositories
- `database_name`: For technical stores

---

## 4. REGISTRY TERMINOLOGY DUPLICATES

### Existing Registries (Inconsistent Naming)
| Current Name | Variants Found | Should Be | Status |
|--------------|---|---|---|
| `ventures-by-sector.yaml` | ventures_by_sector, VENTURES_BY_SECTOR | `VENTURES_REGISTRY.yaml` | ✅ Exists (orphaned naming) |
| `SECTOR_INDEX.yaml` | sector-index, SectorIndex, sector_index | `SECTOR_REGISTRY.yaml` | ✅ Exists |
| `CAPABILITY_REGISTRY.yaml` | capability-registry, CAPABILITY-REGISTRY | `CAPABILITY_REGISTRY.yaml` | ✅ Correct |
| Control Points Registry | control-points, CP_REGISTRY, CONTROL_POINTS_REGISTRY | `CONTROL_POINTS_REGISTRY.yaml` | ❌ Missing |
| Skills Registry | skill-registry, SKILLS, skills-registry | `SKILLS_REGISTRY.yaml` | ❌ Missing |
| Base Registry | base-registry, BASES, BASE_REGISTRY | `CONTROL_BASES_REGISTRY.yaml` (NEW) | ❌ Missing |

**→ CONSOLIDATE:** Rename all registries to follow pattern:
- Format: `{ENTITY_TYPE}_REGISTRY.yaml`
- Prefix enums: `VENTURES_REGISTRY`, `SECTORS_REGISTRY`, `CAPABILITIES_REGISTRY`, `CONTROL_POINTS_REGISTRY`, `CONTROL_BASES_REGISTRY`, `SKILLS_REGISTRY`

---

## 5. AGENT & SKILL TERMINOLOGY

### Duplicate Agent Definitions
| Agent Name | Locations | Status |
|---|---|---|
| **Researcher** | `./.agents/agents/researcher.md` + `~/.claude/agents/research-synthesist.md` | ❌ DUPLICATE |
| **Query Agent** | Multiple in `16-AGENTS/` + orphaned scripts | ⚠️ Scattered |
| **Venture Manager** | Defined 3 places | ⚠️ Scattered |
| **Orchestrator** | Referenced in 5+ files | ⚠️ No canonical location |

**→ ACTION:** Consolidate all agent definitions into `16-AGENTS/MASTER_AGENT_REGISTRY.md`

---

### Skill Terminology Inconsistencies
| Term | Variants | Count | Problem |
|------|----------|-------|---------|
| **skill** | skill, Skill, SKILL, SKL-, competency | ~80 | No canonical form |
| **tool** | tool, Tool, TOOL, TOL-, capability | ~100 | Overloaded (capability also means tool) |
| **agent** | agent, Agent, AGENT, AGT- | ~200 | Case inconsistency |

**→ CONSOLIDATE:** Skill/Tool/Agent hierarchy:
- `agent_id`: "AGT-XXX" (autonomous unit)
- `skill_id`: "SKL-XXX" (procedure, 100+ total)
- `tool_id`: "TOL-XXX" (external capability, 110 total)

---

## 6. STATE & STATUS TERMINOLOGY

### Overloaded "Status" Field
| Context | Status Values | Problem |
|---------|---|---|
| Venture | operating, validating, prototype, planned | No enum |
| Base | INSTANTIATED, ACTIVATED, MONITORING | Inconsistent capitalization |
| Agent | active, inactive, deployed, paused | No enum |
| Workflow | active, failed, pending, completed | No enum |
| Deployment | staging, production, active, released | Unclear |

**→ CONSOLIDATE:** Enum per entity type:
```yaml
venture_status:
  - PLANNING
  - BUILDING
  - VALIDATING
  - OPERATING
  - SCALING
  - EXITING

base_status:
  - DESIGNED
  - INSTANTIATED
  - ACTIVATED
  - MONITORING
  - DECOMMISSIONED

agent_status:
  - AVAILABLE
  - ASSIGNED
  - EXECUTING
  - PAUSED
  - RETIRED
```

---

## 7. ENVIRONMENT TERMINOLOGY

### Environment Names (Inconsistent)
| Found | Variants | Should Be |
|-------|----------|-----------|
| **local** | local, LOCAL, development, dev | `environment: "local"` |
| **staging** | staging, STAGING, test, qa | `environment: "staging"` |
| **production** | production, prod, PROD, live | `environment: "production"` |
| **Mac Studio** | macstudio, mac-studio, Mac Studio | `host: "mac-studio"` |

**→ CONSOLIDATE:** Enum: `["local", "staging", "production"]`

---

## 8. MISSING CANONICAL REGISTRIES (Causes Most Duplication)

### Registries That Should Exist But Don't
| Registry | Should Map | Purpose | Priority |
|---|---|---|---|
| **TERMINOLOGY_REGISTRY.yaml** | All 50+ duplicate terms | Canonical word list | CRITICAL |
| **CONTROL_BASES_REGISTRY.yaml** | B001-B500 (from pasted model) | Control surfaces | HIGH |
| **CONTROL_POINTS_REGISTRY.yaml** | CP-001 to CP-050 | Current governance | HIGH |
| **SKILLS_REGISTRY.yaml** | SKL-001 to SKL-250+ | All skills | MEDIUM |
| **ENVIRONMENT_REGISTRY.yaml** | Env names & configs | Deployment targets | MEDIUM |
| **LIFECYCLE_REGISTRY.yaml** | State enums per entity | Status values | MEDIUM |
| **AGENT_MASTER_REGISTRY.md** | Canonical agent defs | Dedup agents | HIGH |

---

## 9. ORPHANED FILE CONSOLIDATION PLAN

### Files to Migrate
| Current Location | Should Move To | Action |
|---|---|---|
| `./scripts/gbrain_to_neo4j_sync.py` | `_PIPELINES/graph_ingestion_pipeline.py` | Integrate as Phase D |
| `./scripts/analyze_company_brain_scatter.py` | `./.claude/skills/` | Become FILE_DISCOVERY_SKILL |
| `./create_brain.sh` | `_INFRASTRUCTURE/init/` | Document in init procedures |
| `./fractal/docs/skill.rst` | `16-AGENTS/skill-fundamentals.md` | Convert RST → MD |
| `./.agents/agents/researcher.md` | `16-AGENTS/MASTER_AGENT_REGISTRY.md` | Consolidate (dedup) |

---

## 10. ACTION PRIORITY PLAN

### Phase 1: CRITICAL (This Week)
1. ✅ Create `TERMINOLOGY_REGISTRY.yaml` — Map 50+ duplicate terms → canonical forms
2. ✅ Create `CONTROL_BASES_REGISTRY.yaml` — B001-B500 from pasted 500-Bases model
3. ✅ Create `AGENT_MASTER_REGISTRY.md` — Consolidate all 318 agents, dedup researcher
4. ✅ Rename existing registries to `{TYPE}_REGISTRY.yaml` pattern

### Phase 2: HIGH (Next 2 Weeks)
5. Migrate orphaned scripts into `_PIPELINES/` and `./.claude/skills/`
6. Create environment + lifecycle enums in registries
7. Wire all terminology changes into Neo4j schema
8. Update CLAUDE.md to mandate canonical terminology usage

### Phase 3: MEDIUM (Month 2)
9. Audit all 7,629 files for non-canonical terminology
10. Create automated linter to enforce terminology on commits (via Git hook)
11. Backfill Neo4j with corrected entity names

---

## SUMMARY: What's Causing the Duplication

| Root Cause | Impact | Fix |
|---|---|---|
| No canonical terminology registry | 50+ duplicate terms used inconsistently | Create TERMINOLOGY_REGISTRY.yaml |
| Orphaned scripts not consolidated | 5+ scattered files with their own terminology | Migrate into _PIPELINES + .claude/skills |
| No control base model implemented | "base" and "control" overloaded | Implement 500-Bases model, use B-XXX |
| Inconsistent naming conventions | venture vs Venture, SKL vs skill | Enforce via Git hook + linter |
| Multiple agent definitions | Researcher defined 2+ places | Consolidate into MASTER_AGENT_REGISTRY |
| No enum registries | Status/state values vary per file | Create LIFECYCLE_REGISTRY.yaml per entity type |

---

**Outcome:** Once these 8 new registries exist + orphaned files consolidate, terminology will be unified. Neo4j queries will resolve entities correctly by canonical ID instead of fuzzy string matching.

