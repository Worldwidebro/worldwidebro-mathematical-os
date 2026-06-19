---
references:
  - [[VENTURE-MASTER]]
  - [[LOOP-FRAMEWORK]]
  - [[PLAN-WORKFLOW]]
  - [[EXECUTE-WORKFLOW]]
  - [[CONTENT-TESTBED]]
---

# Repo Context Lookup Guide

**Purpose:** Help repos find their venture, sector, loop stage, and workflow context

**Status:** ✅ ACTIVE | **Repos Indexed:** 272

---

## How Repos Use This Guide

```
Repo starts execution
   ↓
1. Find repo_name in context mapping
2. Get venture_id, sector, stage
3. Load [[LOOP-FRAMEWORK]] for this venture
4. Get workflow stage from context
5. Execute via [[PLAN-WORKFLOW]] or [[EXECUTE-WORKFLOW]]
6. Validate in [[CONTENT-TESTBED]]
```

---

## Repo Context by Sector (272 repos)

### Construction (CON-001 to CON-020)
```
venture_id: CON-001
sector: construction
stage: MVP
orb: ORB1_VENTURES
loop_framework: Launch → Validation → Growth → Scale
current_stage: Validation
workflow: [[EXECUTE-WORKFLOW]]
testbed: proof-of-concept-passed
repos: [con-001-ace-construction, con-002-*, ..., con-020-*]
```

### Operations (OPS-001 to OPS-067)
```
venture_id: OPS-*
sector: operations
stage: MVP to Planned
orb: ORB1_VENTURES
loop_framework: Launch → Validation → Growth → Scale
workflow: [[PLAN-WORKFLOW]] or [[EXECUTE-WORKFLOW]] (depends on stage)
repos: [65 ops repos mapped to ventures]
```

### Emerging Tech (TECH-001 to TECH-061)
```
venture_id: TECH-*
sector: emerging
stage: Planned to Growth
orb: ORB1_VENTURES
loop_framework: [[LOOP-FRAMEWORK]]
workflow: Stage-dependent routing
repos: [50 tech repos]
```

### Professional Services (PS-001 to PS-025)
```
venture_id: PS-*
sector: professional-services
stage: MVP to Growth
orb: ORB1_VENTURES
repos: [25 ps repos]
```

### Community (COMM-001 to COMM-049)
```
venture_id: COMM-*
sector: community
stage: Planned to Validation
orb: ORB1_VENTURES
repos: [49 community repos]
```

### Specialized (SPEC-001 to SPEC-050)
```
venture_id: SPEC-*
sector: specialized
stage: Planned to MVP
orb: ORB1_VENTURES
repos: [50 specialized repos]
```

### Logistics (LT-001 to LT-030)
```
venture_id: LT-*
sector: logistics-transport
stage: MVP to Growth
orb: ORB1_VENTURES
repos: [29 logistics repos]
```

---

## Repos by Execution Stage

### Planned (229 repos) → Pre-Launch
```
workflow: [[PLAN-WORKFLOW]]
current_stage: Planning
next_action: Create execution plan
testbed: Not started
action: Route to planning agents
```

### MVP (24 repos) → Minimum Viable Product
```
workflow: [[EXECUTE-WORKFLOW]]
current_stage: MVP Implementation
next_action: Build features
testbed: Alpha testing
action: Execute with real data, validate in testbed
```

### Validation (18 repos) → Beta Testing
```
workflow: [[EXECUTE-WORKFLOW]]
current_stage: Validation/Beta
next_action: Gather user feedback
testbed: Beta proof-of-concept
action: Execute workflow, validate metrics
```

### Growth (1 repo) → Scaling
```
workflow: [[EXECUTE-WORKFLOW]]
current_stage: Growth
next_action: Scale operations
testbed: Production-ready
action: Execute with full context
```

---

## How to Query Repo Context

### By Repo Name
```
repo: con-001-ace-construction
lookup: ORB-REPOS-CONTEXT-MAPPING-2026-06-11.json
find: repo_name == "con-001-ace-construction"
result: {venture_id: "CON-001", sector: "construction", ...}
```

### By Venture ID
```
venture: CON-001
lookup: MASTER-REPO-REGISTRY.csv
find: venture_id == "CON-001"
result: [all repos for this venture]
```

### By Sector
```
sector: construction
lookup: ORB-REPOS-CONTEXT-MAPPING-2026-06-11.json
filter: sector == "construction"
result: [all repos in construction sector]
```

### By Stage
```
stage: MVP
lookup: ORB-REPOS-CONTEXT-MAPPING-2026-06-11.json
filter: stage == "MVP"
result: [24 MVP repos]
```

---

## Repo → Workflow Routing

### Repo in "Planned" Stage
→ Route to [[PLAN-WORKFLOW]]
→ Create 12-week roadmap
→ Define loop stages
→ Test in [[CONTENT-TESTBED]]

### Repo in "MVP" Stage
→ Route to [[EXECUTE-WORKFLOW]]
→ Execute loop stages with real data
→ Capture metrics
→ Validate in [[CONTENT-TESTBED]]

### Repo in "Validation" Stage
→ Route to [[EXECUTE-WORKFLOW]]
→ Execute with beta data
→ Gather validation metrics
→ Update loop config

### Repo in "Growth" Stage
→ Route to [[EXECUTE-WORKFLOW]]
→ Execute with full production context
→ Monitor KPIs
→ Feedback to [[VENTURE-MASTER]]

---

## Repo Context File Location

**Primary:** `/Users/acebless/Documents/ORB-REPOS-CONTEXT-MAPPING-2026-06-11.json`

**Backup:** `Influence-Venture-Business-OS/INFRASTRUCTURE_LAYERS/venture-hub/REPOS-CONTEXT.json`

**Format:** JSON with venture_id, sector, stage, orb, loop_framework, workflow, testbed_status

---

## Integration Points

### When Repo Starts
1. Load `ORB-REPOS-CONTEXT-MAPPING-2026-06-11.json`
2. Find repo_name entry
3. Extract venture_id, sector, stage
4. Load [[LOOP-FRAMEWORK]]
5. Check workflow routing
6. Begin execution

### During Execution
1. Follow loop stages from [[LOOP-FRAMEWORK]]
2. Route to [[PLAN-WORKFLOW]] or [[EXECUTE-WORKFLOW]]
3. Capture metrics
4. Store in context

### After Execution
1. Validate in [[CONTENT-TESTBED]]
2. Update context with results
3. Feedback to [[VENTURE-MASTER]]
4. Next repo uses improved config

---

**Context Lookup Ready. All 272 repos now know which ORB, venture, sector, stage, and workflow they belong to.**
