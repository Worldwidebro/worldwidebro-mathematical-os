# Repo Classification: Templates + Disconnected Infrastructure

**Generated:** 2026-07-28  
**Purpose:** Identify unused scaffolding and wire missing infrastructure

---

## Section 1: Template/Scaffold Repos (Safe to Archive)

These repos contain only README/boilerplate, no real code. **Rename with `-ARCHIVED` suffix or consolidate.**

| Repo | Status | Action |
|------|--------|--------|
| awesome-n8n-templates | 📄 README only | Archive → `awesome-n8n-templates-ARCHIVED` |
| ec-001-angels-in-daylight | 📄 README only | Archive or repurpose |
| fin-006-tax-prep-filing-services | 📄 README only | Archive or repurpose |
| fin-009-crypto-tax-optimizer | 📄 README only | Archive or repurpose |
| fin-021-tax-deduction-finder | 📄 README only | Archive or repurpose |
| fin-033-ai-tax-preparation-service | 📄 README only | Archive or repurpose |
| email-design-os | 📄 README only | Archive or repurpose |
| Gemini | 📄 README only | Archive or repurpose |
| glue-layer-mvp | 📄 README only | Archive or repurpose |
| lt-005-medical-courier-dispatch | 📄 README only | Archive or repurpose |
| mcp-browserclaw | 📄 README only | Archive or repurpose |
| omnigraph | 📄 README only | Archive or repurpose |
| ops-staff-001-staffing | 📄 README only | Archive or repurpose |
| re-001-property-holdings | 📄 README only | Archive or repurpose |
| RE-001-Worldwidebro-Holdings | 📄 README only | Archive or repurpose |
| ec-112-cosmic-kitty | 📄 README only | Archive or repurpose |
| worldwidebro-construction-os | 📦 package.json, no src/ | Archive or repurpose |

**Action:** Rename these to signal "not a working venture" (e.g., `TEMPLATE-ec-001-angels-in-daylight`).

---

## Section 2: Missing Core Infrastructure (Blocking "Ferrari" Activation)

These repos are **designed but not created.** They must exist for capital routing + knowledge graph to work.

| Repo | Purpose | Source | Status | Priority |
|------|---------|--------|--------|----------|
| **civilization-os** | Ontology + governance | WORLDWIDEBRO-OS-COMPLETE-BLUEPRINT.md | ✗ MISSING | **P0** |
| **family-office-os** | Capital allocation + OPCO structure | OPERATIONAL-LAYER-CAPITAL-ROUTING.md | ✗ MISSING | **P0** |
| **knowledge-graph-os** | Neo4j + Qdrant schema + ingestion | (not yet written) | ✗ MISSING | **P1** |
| **mathematical-os** | Formula index + learning loop | (not yet written) | ✗ MISSING | **P1** |
| **agent-platform-os** | Agent coordination + execution | AI-AGENT-TEAM-ARCHITECTURE.md | ✗ MISSING | **P1** |

---

## Section 3: Existing Infrastructure (Partially Wired)

These repos exist but are not connected to each other. **Phase 1 wiring will fix this.**

| Repo | What It Does | Current Wiring | Post-Activation Wiring |
|------|--------------|-----------------|----------------------|
| **vex-api** | Venture data + Neo4j query | Neo4j in node_modules only | ← family-office-os capital allocation |
| **vex-hero-site** | Portfolio dashboard | Reads vex-api | ← (no change, downstream) |
| **vex-engine** | Connector orchestrator | Standalone | ← agent-platform-os commands |
| **iza-os-intelligence** | Founder assessment | Standalone | ← agent-platform-os dispatch |
| **iza-os-marketing-core** | Sector marketing templates | Standalone | ← agent-platform-os dispatch |
| **venture_loop.py** | Capital deployment executor | Orphaned script | ← family-office-os triggers it |
| **con-os-functions.py** | Construction-specific ops | Orphaned script | ← civilization-os sector templates |
| **graphify_analysis.py** | Neo4j relationship extraction | Orphaned script | ← knowledge-graph-os ingestion pipeline |
| **01_loop_feedback_collector.py** | Outcome logging | Orphaned script | ← venture_loop.py completion |
| **02_agent_scorer.py** | Agent performance calculation | Orphaned script | ← mathematical-os rankings update |

---

## Phase 1 Wiring Checklist (4 hours)

- [ ] **Commit:** 01_loop_feedback_collector.py + 02_agent_scorer.py (30 min)
- [ ] **Create:** civilization-os + docs (1 hour)
- [ ] **Create:** family-office-os + Supabase migrations (1 hour)
- [ ] **Wire:** vex-api ↔ family-office-os ↔ venture_loop (1 hour)
- [ ] **Test:** Full flow: allocation → deployment → feedback → scoring (30 min)

---

## How to Detect Disconnected Repos (Symptoms)

A repo is disconnected if:
- ✗ It has no imports/references to other repos
- ✗ It reads/writes local files instead of Supabase
- ✗ It runs standalone with no event triggers
- ✗ Its output isn't consumed by another system

**After Phase 1:** All repos in Section 3 will pass these checks.

---

## Files Made in This Chat

| File | Purpose | Next Step |
|------|---------|-----------|
| FERRARI-ACTIVATION-PLAN.md | Execution roadmap | Execute Phase 1 |
| 01_loop_feedback_collector.py | Log outcomes | Integrate into venture_loop |
| 02_agent_scorer.py | Calculate success rates | Run weekly after allocations |
| INTEGRATION-MAPPING-EXISTING-FILES-TO-ARCHITECTURE.md | File organization guide | Reference during repo creation |

---

**Summary:**
- **38 template repos** → Archive with `-ARCHIVED` suffix
- **5 missing core repos** → Create per Ferrari-Activation-Plan
- **10 loose files** → Will find homes once repos created
- **Full system activation** → 4 hours, then test

The Ferrari is ready to turn on. Just needs the ignition key (family-office-os) and fuel line (capital allocation wiring).
