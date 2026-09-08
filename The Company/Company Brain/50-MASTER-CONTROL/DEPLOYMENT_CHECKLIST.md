---
id: CTRL-DEP-001
title: "Deployment Checklist: Graft + Fractal + herdr"
aliases: ["DEPLOYMENT_CHECKLIST", "Execution Stack Deployment Checklist", "50-MASTER-CONTROL/DEPLOYMENT_CHECKLIST"]
tags: ["deployment", "checklist", "graft", "fractal", "herdr", "verification"]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[50-MASTER-CONTROL/50-MASTER-CONTROL|50-MASTER-CONTROL]] | [[50-MASTER-CONTROL/EXECUTION_STACK|EXECUTION_STACK]] | [[50-MASTER-CONTROL/WORKFLOW_TEST_RESULTS|WORKFLOW_TEST_RESULTS]] | [[REALITY]]

# Deployment Checklist: Graft + Fractal + herdr

> **Authority:** Master Control Plane (CP-050)  
> **Status:** ✅ ALL TOOLS INSTALLED & VERIFIED  
> **Date:** 2026-09-01 (Reconciled: 2026-09-06)

---

## Installation Summary

### Graft 0.16.0
```bash
npm install -g @nanonets/graft
graft build --dir <output-path>
```
**Status:** ✅ Installed | ✅ Verified | ✅ Working

### Fractal 1.2.0
```bash
git clone https://github.com/plasma-ai/fractal
cd fractal
/opt/homebrew/bin/python3.12 -m pip install --break-system-packages -e .
```
**Status:** ✅ Installed | ✅ Verified | ✅ Working  
**Note:** Requires Python 3.12+ (available at `/opt/homebrew/bin/python3.12`)

### herdr 0.7.5
```bash
# Already installed at /Users/acebless/.local/bin/herdr
herdr server &
herdr status
```
**Status:** ✅ Installed | ✅ Verified | ✅ Ready

---

## Verification Commands

```bash
# Graft
graft --version
graft build --dir /tmp/test

# Fractal
/opt/homebrew/bin/python3.12 -m fractal.cli.main --version
/opt/homebrew/bin/python3.12 -m fractal.cli.main --help

# herdr
herdr --version
herdr status
herdr server &
herdr create-session test
herdr list-panes
```

---

## Known Issues & Workarounds

| Issue | Workaround |
|---|---|
| Fractal requires Python 3.12+ | Use `/opt/homebrew/bin/python3.12` explicitly |
| herdr server not running by default | Start manually: `herdr server &` |
| Tree-sitter version conflicts (npm) | Normal warnings, safe to ignore |

---

## Next Steps for L1 (Report-Only) Loops

1. **Create first L1 loop:**
   - Goal: "Audit repository quality"
   - Agent: Read-only (no commits)
   - Output: Report only

2. **Run loop manually once:**
   - Spawn Fractal agent
   - Load Graft context
   - Execute in herdr session
   - Capture output

3. **Schedule loop (L1):**
   - Define cadence (daily/weekly)
   - Set cost limits ($5/run)
   - No approval needed
   - Report to human

4. **Graduate to L2 (Assisted):**
   - After 10 successful L1 runs
   - Adds write capability (branches only)
   - Still requires approval for merge
   - Cost limits: $10/run

---

## Architecture Verification

```
✅ Ontology extended (CODE_INTELLIGENCE + EXECUTION_RUNTIME types)
✅ Registries updated (TOL-000001, TOL-000002, TOL-000003)
✅ Relationships defined (~20 new types)
✅ Wiki links added (INDEX.md, EXECUTION_STACK.md, etc.)
✅ Documentation created (6 new docs)
✅ Tools integration verified
```

---

## Blockers

**None identified.** All systems operational.

---

**See also:** [[50-MASTER-CONTROL/WORKFLOW_TEST_RESULTS|WORKFLOW_TEST_RESULTS]] | [[50-MASTER-CONTROL/EXECUTION_STACK|EXECUTION_STACK]] | [[50-MASTER-CONTROL/INTEGRATION_SUMMARY|INTEGRATION_SUMMARY]]
