# CURSOR DELEGATION & ROUTING SYSTEM
**Generated:** 2026-06-05  
**Purpose:** Enable Cursor to intelligently route work across 855 repos, 18 sectors, 712 ventures, 9 layers

## THE PROBLEM

You have **855 repos** across **18 sectors**. When Cursor gets a prompt, it needs to know:
1. Which repo owns this?
2. What other repos depend on it?
3. Should I write code or delegate?
4. How do repos collaborate?

---

## QUICK REFERENCE: SECTOR → PREFIX → REPOS

| Sector | Prefix | Repos | Example |
|--------|--------|-------|---------|
| e-commerce | EC | 110 | ec-045-shopify |
| operations | OPS | 67 | ops-012-supply-chain |
| technology | TECH | 61 | tech-021-ai |
| specialized | SPEC | 50 | spec-018-concierge |
| emerging | EM | 50 | em-025-fusion |
| community | COMM | 50 | comm-031-coaching |
| education | EDU | 40 | edu-015-bootcamp |
| beauty-wellness | BW | 40 | bw-028-makeup |
| financial | FIN | 41 | fin-019-bank |
| food-hospitality | FH | 35 | fh-012-chef |
| software-tech | ST | 30 | st-008-saas |
| logistics-transport | LT | 30 | lt-014-dispatch |
| professional-services | PS | 25 | ps-009-consulting |
| fitness-sports | FS | 25 | fs-011-gym |
| media-content | MC | 21 | mc-007-youtube |
| construction | CON | 20 | con-003-build |
| education-training | ET | 16 | et-005-tutoring |
| real-estate | RE | 1 | re-001-real-estate |

---

## 3-STEP ROUTING LOGIC

### Step 1: Identify Sector From Prompt
```
"Add checkout to e-commerce ventures"
  → Sector: e-commerce
  → Prefix: EC-*
  → Affects: 110 ventures (EC-001 to EC-110)

"Add metric tracking to knowledge graph"
  → Sector: infrastructure
  → Prefix: IZA-*
  → Affects: ALL 712 ventures (Layer 2 dependency)
```

### Step 2: Map to Repos & Check Dependencies
```
EC-045 depends on:
  ├─ Layer 2: iza-os-rag-system (context)
  ├─ Layer 6: thunderbolt (execution)
  ├─ Layer 6: mission-control (orchestration)
  └─ Layer 7: MC-OPERATIONS (metrics)

If I modify iza-os-rag-system:
  → ALL 668 ventures affected
  → Must coordinate with Layer 6 & 7
```

### Step 3: Decide Execution Type
```
SINGLE VENTURE
  Prompt: "Add feature to EC-045 only"
  Action: Write directly to ec-045 repo
  Coordination: Check Layer 2/6/7 compatibility

SECTOR-WIDE
  Prompt: "Payment system for all EC-* ventures"
  Action: Create INFRA-TEMPLATE-Payment
  Coordination: Each EC-* imports and customizes

CROSS-LAYER
  Prompt: "New capability in knowledge graph"
  Action: Modify iza-os-rag-system
  Coordination: Notify all 668 ventures + Layer 6/7

MULTI-VENTURE COLLAB
  Prompt: "EC-045 and TECH-021 integrate"
  Action: Modify both repos + coordinate via Layer 2/6/7
  Coordination: Bilateral API setup + orchestration
```

---

## WHEN TO WRITE VS. DELEGATE

**WRITE LOCALLY (Single Venture)**
```
"Add coupon code to EC-045"
  → Modify: ec-045-* repo
  → No delegation
  → Update: MASTER-REPO-REGISTRY.csv
```

**CREATE SHARED COMPONENT (Sector-Wide)**
```
"Payment system for all EC-* ventures"
  → Create: INFRA-TEMPLATE-Payment-System
  → Each EC-* imports it
  → Maintain once, use by 110 ventures
  → Document: How each EC-* customizes
```

**DELEGATE TO INFRASTRUCTURE (Cross-Layer)**
```
"New metric type for knowledge graph"
  → Modify: iza-os-rag-system
  → Notify: mission-control (orchestration)
  → Notify: MC-OPERATIONS (metrics)
  → Notify: All 668 ventures
```

**COORDINATE INTEGRATION (Multi-Venture)**
```
"EC-045 ← → TECH-021 integration"
  → Modify: ec-045 API endpoint
  → Modify: tech-021 client connection
  → Coordinate: Via iza-os-rag-system (context)
  → Coordinate: Via mission-control (orchestration)
  → Test: Both sides work together
```

---

## COMPONENT REUSE PATTERNS

### Shared Across Sector (INFRA-TEMPLATE-*)
```
Payment System
  ├─ Used by: EC-045, EC-046, ... EC-154 (110 ventures)
  ├─ Maintained in: INFRA-TEMPLATE-Payment-System
  ├─ Each EC-* customizes for its business
  └─ Update once → all 110 ventures get improvement

Authentication
  ├─ Used by: PS-*, FIN-*, EC-* (180+ ventures)
  ├─ Maintained in: INFRA-FRAMEWORK-Auth
  └─ Update once → 180+ ventures secured
```

### Shared Across All Ventures (INFRA-CENTRALIZED)
```
Knowledge Graph
  ├─ All 712 ventures depend on: iza-os-rag-system
  ├─ Maintained in: Layer 2 (one source)
  └─ Update once → all ventures have new context

Metrics Collection
  ├─ All 712 ventures report to: MC-OPERATIONS
  ├─ Maintained in: Layer 7 (one dashboard)
  └─ Update once → all ventures tracked correctly

Orchestration
  ├─ All 712 ventures use: mission-control
  ├─ Maintained in: Layer 6 (one orchestrator)
  └─ Update once → all workflows coordinated
```

### Venture-Specific (NOT Shared)
```
EC-045 Business Logic
  ├─ ONLY in: ec-045-* repo
  ├─ NOT shared with EC-046
  └─ Each venture owns its logic

OPS-023 Workflows
  ├─ ONLY in: ops-023-* repo
  ├─ NOT shared with OPS-024
  └─ Each sector owns workflows
```

---

## CURSOR RULES (Always Follow)

✅ **ALWAYS:**
- Identify sector from prompt
- Map sector → prefix → repos
- Check layer dependencies before writing
- Create shared components instead of duplicating
- Coordinate across layers when needed
- Update MASTER-REPO-REGISTRY.csv after changes

❌ **NEVER:**
- Write without knowing the repo name
- Duplicate code across multiple repos
- Modify Layer 2 without notifying all ventures
- Change infrastructure without coordination
- Scatter related code across different repos

---

## TESTING AFTER CHANGES

**Single Venture:**
1. Test EC-045 works standalone
2. Verify Layer 2 (knowledge graph) connection
3. Verify Layer 6 (orchestration) works
4. Verify Layer 7 (metrics) capture data

**Shared Component:**
1. Build INFRA-TEMPLATE-Payment once
2. Test 3-5 EC-* ventures use it
3. Verify all 110 EC-* can import
4. Run integration suite

**Cross-Layer:**
1. Modify Layer 2 (iza-os-rag-system)
2. Update Layer 6 (mission-control)
3. Update Layer 7 (MC-OPERATIONS)
4. Test all layers communicate
5. Verify dashboard displays correctly

---

## FILES TO ALWAYS CHECK

1. **DATA-SOURCES.md** — Where does data live?
2. **COMPLETE-855-GITHUB-REPOS-MAPPING.md** — What does each repo do?
3. **MASTER-REPO-REGISTRY.csv** — What repos exist?
4. **ventures-master.csv** — What ventures exist?
5. **REPO-NAMING-STANDARD-AND-FIXES.md** — Naming convention

