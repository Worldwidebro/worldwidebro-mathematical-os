# PEOPLE + ROLES INFRASTRUCTURE BRIDGE

**Date:** 2026-09-23  
**Status:** PHASE 0 COMPLETE — Skeleton registries created  
**Next:** PHASE 1 — Verify actual people data + wire to agent system

---

## THE COMPLETE STACK (Now Connected)

```
LAYER 1: LEGAL/FINANCIAL STRUCTURE
  ├── 150 Legal Entities (Trust, OpCos, LLCs, etc.)
  ├── 789 Ventures (businesses operating in 36 sectors)
  └── Maps to: ECOSYSTEM_150_ENTITY_REGISTRY.yaml + ALL_789_VENTURES_36_SECTOR_ALIGNMENT.csv

LAYER 2: DOMAIN/OPERATING STRUCTURE (NEW)
  ├── 35 Bases (1 per sector, knowledge + operations)
  └── Maps to: BASES-CANONICAL-DEFINITION.md

LAYER 3: PEOPLE + ROLES (JUST CREATED)
  ├── PEOPLE-REGISTRY.yaml (21 key people identified, [TO_VERIFY])
  ├── ROLES-REGISTRY.yaml (40+ standard roles)
  ├── RESPONSIBILITY-MATRIX.csv (entity → role → person)
  └── AUTHORITY-MATRIX.yaml (approval thresholds)

LAYER 4: AGENT SYSTEM (Ready to wire)
  ├── 318 agents scoped to Bases
  ├── Agent routing via RESPONSIBILITY-MATRIX
  └── Agent authority gating via AUTHORITY-MATRIX

LAYER 5: KNOWLEDGE GRAPH (Ready to query)
  ├── Neo4j (20,363+ edges, expandable)
  ├── Query: "Who is CFO of Master Holdco?"
  └── Result: PERSON-004 + authority limits + escalation path
```

---

## WHAT JUST GOT CREATED (4 Files)

### 1. PEOPLE-REGISTRY.yaml
**Purpose:** Master list of all actual people in the ecosystem  
**Current State:** Skeleton with 21 key positions  
**Status:** All marked [TO_VERIFY]  
**Fields:** person_id, name, title, organization, email, phone, authority_level, status

**Example:**
```yaml
- person_id: PERSON-004
  name: "[FAMILY OFFICE CFO - TO_VERIFY]"
  title: "Family Office CFO"
  authority_level: "EXECUTIVE"
  status: "UNKNOWN"
  role_ids: [ROLE-FOE-CFO]
```

**What needs to happen:** Verify actual names and emails from venture repos + family office records

---

### 2. ROLES-REGISTRY.yaml
**Purpose:** Define every role and its authority  
**Current State:** 40+ standard roles fully documented  
**Status:** Complete, ready to use  
**Fields:** role_id, title, entity_type, authority_level, responsibilities, approval_authority, approval_limits

**Example:**
```yaml
- role_id: ROLE-FOE-CFO
  title: "Family Office CFO"
  authority_level: "EXECUTIVE"
  approval_authority:
    - "Can approve: Capital allocations up to $500K"
    - "Cannot approve: Unlimited capital (requires founder)"
  approval_limits:
    capital_allocation_limit: 500000
```

**What this enables:** Agents know what decisions each role can make

---

### 3. RESPONSIBILITY-MATRIX.csv
**Purpose:** Show which people fulfill which roles in which entities  
**Current State:** ~25 rows mapping 3 revenue-ready ventures + family office core  
**Status:** Template complete, needs population  
**Fields:** entity_id, entity_name, role_id, role_title, person_id, person_name, status, evidence_doc

**Example:**
```csv
LT-005,Medical Courier,ROLE-VENTURE-CEO,Venture CEO,PERSON-020,[LT-005 FOUNDER - TO_VERIFY],UNKNOWN,[TO_VERIFY]
```

**Gaps Highlighted:**
```
[PROPERTY-LLC-002],PROPERTY-LLC-CHARLOTTE,[EMPTY],Property Manager,[EMPTY],[TO_VERIFY],UNKNOWN,*** GAP ***
[PROPERTY-LLC-002],PROPERTY-LLC-CHARLOTTE,[EMPTY],Insurance Coverage,[EMPTY],[TO_VERIFY],UNKNOWN,*** GAP ***
```

**What this enables:** Agents see "who does what" + immediately spot gaps

---

### 4. AUTHORITY-MATRIX.yaml
**Purpose:** Define approval thresholds and decision routing  
**Current State:** 15+ decision types with thresholds  
**Status:** Complete, ready for agent routing logic  
**Fields:** decision_type, approvers, thresholds, escalation

**Example:**
```yaml
capital_allocation:
  100k_to_500k:
    approvers:
      all_of: ["ROLE-FOE-CFO", "ROLE-FOUNDER"]
  over_500k:
    approvers:
      role: ["ROLE-FOUNDER"]
```

**What this enables:** Agents route decisions to correct people based on amount + authority

---

## HOW AGENTS USE THIS (The Bridge)

### Example 1: Revenue Agent Routing

```
Agent task: "Get approval for $200K marketing spend for LT-005"

Step 1: Query AUTHORITY-MATRIX
  "What approval needed for $200K capital decision?"
  → 100k_to_500k threshold
  → Requires: ROLE-FOE-CFO + ROLE-FOUNDER

Step 2: Query RESPONSIBILITY-MATRIX
  "Who has ROLE-FOE-CFO for Master Holdco?"
  → PERSON-004 (person_name: [FAMILY OFFICE CFO - TO_VERIFY])
  → PERSON-001 (ROLE-FOUNDER)

Step 3: Query PEOPLE-REGISTRY
  "Who is PERSON-004?"
  → Email: [TO_VERIFY]
  → Authority level: EXECUTIVE
  → Status: UNKNOWN (not yet verified)
  
Step 4: Agent decision
  ✅ Has responsible people identified
  ⚠️ People not yet verified (status = UNKNOWN)
  → Route to CFO + Founder for approval (with note: verify identities)
  → Log: "Waiting for PERSON-004 (CFO) + PERSON-001 (Founder) approval"

Step 5: Decision recorded
  → Approval chain: [PERSON-004] → [PERSON-001]
  → Amount: $200K
  → Decision: APPROVED or ESCALATED
  → Logged in audit trail
```

### Example 2: Gap Detection

```
Agent task: "Ensure all properties have insurance coverage"

Step 1: Query RESPONSIBILITY-MATRIX
  "Which people have ROLE-INSURANCE-BROKER for properties?"
  
Step 2: Agent finds
  PROPERTY-LLC-001: ✅ PERSON-016 (broker assigned)
  PROPERTY-LLC-002: ❌ NO ONE ASSIGNED (GAP)
  
Step 3: Agent action
  → Flag: "Property LLC-2 missing insurance broker"
  → Create task: "Assign insurance broker to [PROPERTY-LLC-2]"
  → Escalate to: PERSON-004 (CFO)
  → Tag: HIGH PRIORITY (uninsured asset)
  
Step 4: Result
  Responsibility-Matrix updated → PERSON-016 assigned to PROPERTY-LLC-2
```

### Example 3: Succession Backup

```
Agent task: "Who is backup if PERSON-004 (CFO) is unavailable?"

Step 1: Query RESPONSIBILITY-MATRIX
  "Who has ROLE-FOE-CFO or related roles?"
  → PERSON-004 (primary CFO)
  → PERSON-003 (FOE CEO - can escalate to)
  
Step 2: Agent logic
  If PERSON-004 cannot approve in time:
    → Route to PERSON-003 (FOE CEO)
    → Send escalation notice
    → Log: "CFO backup routed to FOE CEO"
```

---

## CURRENT STATE: SKELETON + [TO_VERIFY]

| Registry | Records | Status | Next Action |
|----------|---------|--------|-------------|
| PEOPLE-REGISTRY.yaml | 21 entries | [TO_VERIFY] | Audit venture repos + family office records |
| ROLES-REGISTRY.yaml | 40+ roles | COMPLETE | Ready to use |
| RESPONSIBILITY-MATRIX.csv | ~25 rows | PARTIAL | Map remaining entities + ventures |
| AUTHORITY-MATRIX.yaml | 15+ decisions | COMPLETE | Ready for agent routing |

---

## IMMEDIATE NEXT STEPS (Phase 1)

### This Week (Sep 23-27)

**Step 1: Verify 3 Revenue-Ready Ventures (4 hours)**
- OPS-001: Find founder name + contact
- LT-005: Find founder name + contact (probably Acc Bless based on code)
- CALLCENTER: Find founder name + contact

**Step 2: Audit 50 Venture Repos (8 hours)**
- Search README.md for "Founder", "Creator", "CEO"
- Search CLAUDE.md for person names
- Search .github/CODEOWNERS for team
- Extract: name, email, title
- Update: PEOPLE-REGISTRY.yaml with actual data

**Step 3: Consolidate People Data (3 hours)**
- Update PEOPLE-REGISTRY status from [TO_VERIFY] → PENDING_VERIFICATION
- Fill email + phone fields
- Identify which people need background verification

**Step 4: Wire to Agents (2 hours)**
- Create AGENT-ROUTING-LOGIC.md (how agents query registries)
- Write pseudocode for approval routing
- Write pseudocode for gap detection

**Total: ~17 hours — Fits in Week 3 parallel with BASE instantiation**

---

## NEXT WEEK (Sep 30 - Oct 6)

### Phase 1B: Verification + Agent Integration

**Step 1: Verify People (2 hours)**
- Email each person to confirm role + contact info
- Update PEOPLE-REGISTRY status → VERIFIED
- Document evidence (confirmation email)

**Step 2: Complete Responsibility Matrix (4 hours)**
- Map all 36 OpCos to people
- Map all property entities to people
- Identify ALL gaps (missing roles)

**Step 3: Build Agent Routing Logic (6 hours)**
- Wire agents to query RESPONSIBILITY-MATRIX
- Implement approval chain logic
- Implement gap detection + alerting

**Step 4: Test with 3 Scenarios (3 hours)**
- Test 1: Route $200K decision to CFO + Founder ✅
- Test 2: Detect missing property manager ✅
- Test 3: Escalate to founder when CFO unavailable ✅

**Total: ~15 hours — Runs parallel with BASE scale-out (BASE-001 through BASE-035)**

---

## SUCCESS METRICS

### By Oct 6 (Phase 1 Complete)

- ✅ All 21 key people verified (status = VERIFIED)
- ✅ All [TO_VERIFY] fields populated with real data
- ✅ Responsibility Matrix covers 150+ entities
- ✅ 50+ venture founders/CEOs documented
- ✅ Gap detection shows missing coverage
- ✅ Agents can route decisions by authority
- ✅ Approval chain works for 3 revenue ventures
- ✅ Escalation logic tested + live

### By Dec 31 (Full Ecosystem)

- ✅ 200+ people across family office + advisors + venture teams
- ✅ 100% of 789 ventures have CEO + key roles assigned
- ✅ 100% of 150 entities have coverage (no gaps)
- ✅ Agents autonomous on 250+ decisions per week
- ✅ Control planes fully integrated with authority matrix

---

## THE BRIDGE IN ACTION

```
ORGANIZATIONAL STRUCTURE
  (200 entity types × 150 instances)
           ↓
PEOPLE ROLES LAYER
  (41 key people × 40+ roles)
           ↓
RESPONSIBILITY MATRIX
  (entity → role → person)
           ↓
APPROVAL AUTHORITY
  (who can approve what)
           ↓
AGENT ROUTING
  (agents query + route decisions)
           ↓
DECISION EXECUTION
  (revenue agents make calls, construction agents schedule projects, etc.)
           ↓
AUDIT TRAIL
  (all decisions logged + traceable)
           ↓
LEARNING FEEDBACK
  (memory updates for next decisions)
```

---

## FILES & LOCATIONS

**Registry Files:**
- `/Users/acebless/Documents/The\ Company/Company\ Brain/_REGISTRIES/CANONICAL/PEOPLE-REGISTRY.yaml`
- `/Users/acebless/Documents/The\ Company/Company\ Brain/_REGISTRIES/CANONICAL/ROLES-REGISTRY.yaml`
- `/Users/acebless/Documents/The\ Company/Company\ Brain/_REGISTRIES/CANONICAL/RESPONSIBILITY-MATRIX.csv`
- `/Users/acebless/Documents/The\ Company/Company\ Brain/_REGISTRIES/CANONICAL/AUTHORITY-MATRIX.yaml`

**Supporting Docs:**
- [[BASES-CANONICAL-DEFINITION]] — Layer 2 (domains)
- [[BASE-INSTANTIATION-AGENTIC-PLAN]] — Phase 1 roadmap
- [[PEOPLE-ROLES-INFRASTRUCTURE-BRIDGE]] (this file) — Layer 3 bridge

**Agent Integration (TBD):**
- `AGENT-ROUTING-LOGIC.md` (to create Week 3)
- `AGENT-AUTHORITY-TESTS.yaml` (to create Week 3)

---

## ONE THING THIS SOLVES

**Before this:**
- Agents knew entities + ventures but not who operates them
- Agents couldn't route decisions (no approval authority)
- Agents couldn't detect gaps (missing people/roles)
- Approval chains were ad-hoc, not traceable

**After this:**
- Agents know exactly who does what in every entity
- Agents route decisions by authority + amount
- Agents detect gaps and alert for filling
- Approval chains are automated, auditable, traceable

**Result:** Agents can actually RUN the estate + family office, not just report on it.

---

**Status:** PHASE 0 COMPLETE ✅  
**Next:** PHASE 1 (Verify + Integrate) — Starting Oct 1  
**Owner:** CP-001 (Enterprise) + CP-027 (Infrastructure)  
**Commit:** 5af7f6e4

---

## Control Base Reference

This document is mapped to [[B100|Control Base]] in the Company Brain.

**Wiki Link:** [[CBP_REGISTRY|_REGISTRIES/CANONICAL/CBP_REGISTRY.yaml#B100]]