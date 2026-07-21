---
name: Code Consolidation & Venture Template Scaffold
date: 2026-07-21
status: Ready for Wave 2
part_of: 5-Wave Execution Plan
---

# Code Consolidation & Venture Template Scaffold

**Purpose:** Extract 380+ duplicated implementations across the 712-venture portfolio into a shared library, then create an automated scaffold system so new ventures wire cleanly without copy-paste debt.

## Core Value

~40% of venture code is manual copy-paste from the CON-001 template. This project eliminates that waste and cuts new venture setup from manual templating to 30-second scaffold generation.

## Requirements

### Active

- [ ] **CONS-01**: Extract duplicated Supabase CRUD patterns (150+ implementations) into `shared-venture-lib/supabase_client.py`
- [ ] **CONS-02**: Extract n8n webhook handlers (80+ implementations) into `shared-venture-lib/n8n_webhooks.py`
- [ ] **CONS-03**: Extract Neo4j graph sync logic (50+ implementations) into `shared-venture-lib/graph_sync.py`
- [ ] **CONS-04**: Extract CSV↔Supabase loaders (40+ implementations) into `shared-venture-lib/csv_loader.py`
- [ ] **CONS-05**: Extract Stripe webhook handling (20+ implementations) into `shared-venture-lib/stripe_webhook.py`
- [ ] **CONS-06**: Extract risk scoring logic (15+ implementations) into `shared-venture-lib/risk_calc.py`
- [ ] **CONS-07**: Create `venture-template-scaffold.sh` that generates a new venture directory with imports wired to `shared-venture-lib`
- [ ] **CONS-08**: Update CON-001 to import from `shared-venture-lib` and smoke-test to verify no breakage
- [ ] **CONS-09**: Document module interfaces and reuse patterns in `shared-venture-lib/README.md`

### Out of Scope

- Rewriting sector-specific business logic (stays in individual ventures)
- Migrating existing 710 ventures to use the new library (automatic on next rebuild)
- Building a GUI venture creator (shell script is sufficient)

## Deliverables

1. **`WORLDWIDEBRO-OS/06-TECHNOLOGY/shared-venture-lib/`** — Python package with 6 modules
2. **`venture-template-scaffold.sh`** — Bash script that generates venture skeleton in 30 seconds
3. **`CONSOLIDATION-AUDIT.md`** — Before/after line counts and duplication metrics
4. **Updated CON-001** — Running cleanly on imports from shared lib

## Timeline

Part of Wave 2 (Parallel with Wave 3 topology docs).

**Estimated effort:** 3-4 hours (extraction is mechanical).

---

## Related Files

- Serena duplication analysis: `S630` (40% copy-paste finding)
- Consolidation roadmap: Seeded from Wave 1 analysis agents
- Venture template requirements: Per-sector stubs in `WORLDWIDEBRO-OS/03-PORTFOLIO/ventures/active/`

## Status

🟡 Planned. Depends on Wave 0 disk cleanup.
