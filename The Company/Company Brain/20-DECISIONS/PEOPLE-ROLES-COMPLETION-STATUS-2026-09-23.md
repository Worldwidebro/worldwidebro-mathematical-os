---
title: People + Roles Layer — Completion Status & Next Steps
date: 2026-09-23
status: Phase 1 (Skeleton) Complete | Phase 2 (Verification) In Progress
authority: CP-001 (Enterprise) + CP-027 (Infrastructure)
---

# PEOPLE + ROLES COMPLETION STATUS — Sep 23, 2026

## EXECUTIVE SUMMARY

| Component | Status | % Complete | Owner | Timeline |
|-----------|--------|------------|-------|----------|
| **Founder Identity** | ✅ CREATED | 100% | WHO-I-AM-ANTWUAN-JOHNS.md | Done |
| **Role Definitions** | ✅ COMPLETE | 100% | ROLES-REGISTRY.yaml | Done |
| **Authority Matrix** | ✅ COMPLETE | 100% | AUTHORITY-MATRIX.yaml | Done |
| **People Verification** | 🟡 SKELETON | 0% | PEOPLE-REGISTRY.yaml | 3-4 hours |
| **Role Requirements** | 🟡 PARTIAL | 5% | ROLE-REQUIREMENTS.yaml | 4-5 hours |
| **Onboarding Templates** | 🟡 STRUCTURE | 10% | ONBOARDING-TEMPLATES.yaml | 6-8 hours |
| **Neo4j Integration** | ⏳ PLANNED | 0% | CYPHER scripts | 3-4 hours |
| **Agent Wiring** | ⏳ PLANNED | 0% | Decision routing logic | 4-6 hours |
| **TOTAL PROJECT** | 🟡 **25%** | | **Week 3-4** | **22-31 hours** |

---

## WHAT'S DONE ✅

### 1. WHO-I-AM-ANTWUAN-JOHNS.md (NEW)
**Status:** ✅ CREATED  
**Purpose:** Founder identity document establishing authority + values  
**Contents:**
- Legal identity (Antwuan Johns confirmed from OPS-001 contracts)
- Sovereign authority level established
- Philanthropic mission framework (awaiting user confirmation)
- Decision-making framework template
- Financial threshold guidance
- Key relationships structure
- Integration points to PERSON-001

**What needs from you:** Complete [TO_VERIFY] fields (email, phone, address, mission statement, advisory team)

**Next action:** Review + sign off on WHO-I-AM.md

---

### 2. ROLES-REGISTRY.yaml (COMPLETE)
**Status:** ✅ COMPLETE + READY TO USE  
**Contents:** 40+ roles fully documented with:
- Role definitions (title, entity type, authority level)
- Responsibilities (what each role does)
- Approval authority (what they can approve)
- Approval limits (amounts + scope)
- Required evidence (documents needed to activate role)

**Roles included:**
- Family & Governance (FOUNDER, TRUSTEES, PROTECTOR)
- Family Office Executives (CEO, CFO, COO, CIO)
- Professional Advisors (Lawyers, CPAs, Auditors, Bankers, Insurance)
- Real Estate (Property Manager, Developer)
- Venture Operations (Venture CEO, Venture CFO)
- Control Plane Members
- Board Members

**What's complete:** 100% — No additional work needed

---

### 3. AUTHORITY-MATRIX.yaml (COMPLETE)
**Status:** ✅ COMPLETE + READY TO USE  
**Contents:** Decision approval workflows
- Capital allocation ($100K, $500K, $1M+ thresholds)
- Trust modifications (beneficiary, trustee, terms)
- Property transactions (acquisition, sale, renovation)
- Contracts ($100K, $500K+ thresholds)
- Debt & borrowing ($250K, $1M thresholds)
- Tax planning (annual, significant transactions)
- Insurance decisions
- Venture CapEx (operating ventures)
- Personnel & compensation
- Beneficiary distributions

**Decision thresholds:** All configured with approval chains + required evidence

**What's complete:** 100% — Agents can use immediately

---

## WHAT'S PARTIAL 🟡

### 4. PEOPLE-REGISTRY.yaml (SKELETON — 0% VERIFIED)
**Status:** 🟡 SKELETON — All names marked [TO_VERIFY]  
**Current:** 21 people slots defined, zero verified

**People needing verification:**

| Person ID | Slot | Current Status | Data Source |
|-----------|------|---|---|
| PERSON-001 | Founder | ✅ Antwuan Johns confirmed | OPS-001 contracts |
| PERSON-002 | Spouse/Partner | [TO_VERIFY] | Family records |
| PERSON-003 | Family Office CEO | [TO_VERIFY] | ? |
| PERSON-004 | Family Office CFO | [TO_VERIFY] | ? |
| PERSON-005 | Family Office COO | [TO_VERIFY] | ? |
| PERSON-006 | Family Office CIO | [TO_VERIFY] | ? |
| PERSON-007 | Primary Trustee | [TO_VERIFY] | ? |
| PERSON-008 | Co-Trustee | [TO_VERIFY] | ? |
| PERSON-009 | Trust Protector | [TO_VERIFY] | ? |
| PERSON-010 | Estate Attorney | [TO_VERIFY] | ? |
| PERSON-011 | Corporate Attorney | [TO_VERIFY] | ? |
| PERSON-012 | Tax Advisor/CPA | [TO_VERIFY] | ? |
| PERSON-013 | Auditor | [TO_VERIFY] | ? |
| PERSON-014 | Banker | [TO_VERIFY] | ? |
| PERSON-015 | Investment Manager | [TO_VERIFY] | ? |
| PERSON-016 | Insurance Broker | [TO_VERIFY] | ? |
| PERSON-017 | Real Estate Attorney | [TO_VERIFY] | ? |
| PERSON-018 | Property Manager | [TO_VERIFY] | ? |
| PERSON-019 | OPS-001 CEO | [TO_VERIFY] | OPS-001 repo |
| PERSON-020 | LT-005 CEO | [TO_VERIFY] | LT-005 repo |
| PERSON-021 | CALLCENTER CEO | [TO_VERIFY] | CALLCENTER repo |

**What needs to happen:**
- Search venture repos for actual people names + emails
- Search OPS-001 GUIDE.md (Antwuan Johns confirmed as admin)
- Search family office records for executive names
- Search advisors contact list / engagement letters
- Update registry with verified names
- Change status from UNKNOWN → PENDING_VERIFICATION

**Estimated effort:** 3-4 hours (parallel search + data entry)

---

### 5. RESPONSIBILITY-MATRIX.csv (PARTIAL — 0% VERIFIED)
**Status:** 🟡 PARTIAL — Structure complete, data all [TO_VERIFY]  
**Current:** 30 entity→role→person mappings, all person names marked [TO_VERIFY]

**Dependencies:** Waits on PEOPLE-REGISTRY verification (Phase 2)

**What needs to happen:**
- Once PEOPLE-REGISTRY is verified, update RESPONSIBILITY-MATRIX with confirmed person IDs
- Identify gaps (entities with no assigned roles)
- Document "no one assigned yet" vs. "need to find person" 

**Estimated effort:** 1 hour (auto-generated after people verification)

---

### 6. ROLE-REQUIREMENTS.yaml (PARTIAL — 5% COMPLETE)
**Status:** 🟡 PARTIAL — 2 roles detailed (ROLE-FOUNDER, ROLE-TRUSTEE-PRIMARY), 38+ incomplete  
**Current:** ~100 lines out of ~3,900 needed

**What's done:**
- ROLE-FOUNDER (50% done) — Structure exists, some details filled in
- ROLE-TRUSTEE-PRIMARY (100% done) — Complete example

**What's missing:**
- ROLE-FOE-CEO — 100 lines (identity, documents, access, training, workflows)
- ROLE-FOE-CFO — 100 lines
- ROLE-FOE-COO — 100 lines
- ROLE-FOE-CIO — 100 lines
- [30 more roles] — 100 lines each

**What needs to happen:**
- For each of 40 roles, document:
  - What credentials/documents are required to activate
  - What systems access the role needs
  - What training is required
  - What workflows they operate in
  - What approval limits apply
  - What evidence they must produce

**Estimated effort:** 4-5 hours (template-based, ~100 lines per role)

---

### 7. ONBOARDING-TEMPLATES.yaml (STRUCTURE ONLY — 10% COMPLETE)
**Status:** 🟡 STRUCTURE DEFINED — 8 sections outlined, ~5-10% filled  
**Current:** ~100 lines out of ~5,000 needed

**Sections defined but incomplete:**
1. Welcome section (template drafted)
2. Identity verification (template drafted)
3. Document collection (template drafted, ~100 lines)
4. Systems access — NOT STARTED
5. Training — NOT STARTED
6. Workflow assignment — NOT STARTED
7. First deliverable — NOT STARTED
8. Activation — NOT STARTED

**What needs to happen:**
- For each section + each role type, generate automated checklist
- Define document collection workflows (e.g., "collect estate attorney's bar license")
- Map systems access requirements to IT provisioning
- Create training module lists for each role
- Define approval gates for each section

**Estimated effort:** 6-8 hours (workflow mapping + template generation)

---

## WHAT'S PLANNED ⏳

### 8. PEOPLE-VERIFICATION-AUDIT-PLAN.md (NOT REVIEWED)
**Status:** ⏳ CREATED but not reviewed  
**Purpose:** Step-by-step audit methodology  
**Next:** Review file + execute Phase 2 people verification

---

### 9. 200-NODE-FAMILY-OFFICE-TAXONOMY.md (NOT REVIEWED)
**Status:** ⏳ CREATED but not reviewed  
**Purpose:** Entity types for family office  
**Next:** Review file + map to existing entity taxonomy

---

### 10. Neo4j Integration (NOT STARTED)
**Status:** ⏳ PLANNED  
**What needs to happen:**
- Create PERSON nodes (21 entries) — linked to PEOPLE-REGISTRY
- Create PERSON_HAS_ROLE edges — links PERSON → ROLE → ENTITY
- Create PERSON_AUTHORIZED_FOR edges — links PERSON → approval limits
- Create Cypher query patterns for agent context assembly

**Example Queries:**
```cypher
// Find CFO of Master Holdco
MATCH (e:Entity {entity_id: "ENT-002"})
    -[:HAS_ROLE]->(r:Role {role_id: "ROLE-FOE-CFO"})
    <-[:HAS_PERSON]-(p:Person)
RETURN p.person_id, p.name, r.approval_limits;

// Find all people approved for decisions over $500K
MATCH (p:Person)-[:AUTHORIZED_FOR]->(a:Authority {threshold_over: 500000})
RETURN p.person_id, p.name, a.approval_authority;
```

**Estimated effort:** 3-4 hours (schema + 20-30 Cypher templates)

---

### 11. Agent Decision Routing Integration (NOT STARTED)
**Status:** ⏳ PLANNED  
**What needs to happen:**
- Wire PEOPLE-REGISTRY to agent dispatch logic
- Check authority limits before routing decisions
- Flag gaps (required role not assigned to any person)
- Create audit trail (who approved what)

**Example Agent Flow:**
```
Decision: Capital allocation $750,000
Threshold: Requires ROLE-FOE-CFO + ROLE-FOUNDER
Query PEOPLE-REGISTRY:
  ✅ ROLE-FOE-CFO → PERSON-004 (found, authority $500K limit — exceeds threshold!)
  ✅ ROLE-FOUNDER → PERSON-001 (found, authority UNLIMITED)
Route to: PERSON-001 (founder must approve)
Escalation: If founder unreachable in 24h → escalate to co-principal
```

**Estimated effort:** 4-6 hours (integration + testing)

---

## CRITICAL PATH TO MVP (Minimum Viable)

**Goal:** Enable agent system to route decisions with human authority checks

**Sequence:**
1. **Hour 1-2:** Verify WHO-I-AM.md with founder (Antwuan Johns)
2. **Hour 3-6:** Search repos + verify 21 people (parallel work possible)
3. **Hour 7-10:** Update PEOPLE-REGISTRY + RESPONSIBILITY-MATRIX
4. **Hour 11-15:** Create Neo4j PERSON nodes + edges
5. **Hour 16-20:** Wire agent routing logic to query PEOPLE-REGISTRY
6. **Hour 21-22:** Test end-to-end (agent routes decision → checks authority → escalates if needed)

**MVP Completion:** 22 hours = 2-3 working days

**Timeline:** Sep 23 → Sep 25 (if parallel work possible)

---

## SIGN-OFF CHECKLIST

**Before activating agent system, verify all items:**

### People Verification
- [ ] WHO-I-AM-ANTWUAN-JOHNS.md reviewed + signed by founder
- [ ] All 21 people identified + verified (or documented as "no one assigned yet")
- [ ] PEOPLE-REGISTRY status changed from UNKNOWN → VERIFIED where possible
- [ ] RESPONSIBILITY-MATRIX updated with confirmed person IDs
- [ ] Gap report generated (which roles have no person assigned?)

### Role Requirements
- [ ] All 40+ roles have documented requirements
- [ ] Each role's credentials, documents, access, training defined
- [ ] ONBOARDING-TEMPLATES auto-generates checklists for each role

### Authority Wiring
- [ ] AUTHORITY-MATRIX linked to PEOPLE-REGISTRY
- [ ] Agents can query "Who can approve $X decision?" and get correct person
- [ ] Escalation paths defined (what if person unreachable?)
- [ ] Audit trail enabled (log who approved what)

### System Integration
- [ ] Neo4j PERSON nodes indexed (21 entries)
- [ ] Cypher queries tested (can find people by role, entity, authority level)
- [ ] Agent routing logic wired (decisions routed to correct approver)
- [ ] End-to-end test passed (decision → routing → approval → execution)

---

## NEXT STEPS (FOR YOU)

### Immediate (Today/Sep 23)
1. **Read WHO-I-AM-ANTWUAN-JOHNS.md** — Confirm this represents you
2. **Complete [TO_VERIFY] fields** — Provide missing identity info (email, phone, mission statement, advisory team)
3. **Confirm authority limits** — Review financial thresholds and approve

### Short-term (Sep 24-25)
4. **Approve people verification plan** — Should we search repos? Should we ask others?
5. **Provide missing people information** — Give names/contacts for:
   - Spouse/partner
   - Family office executives (if hired)
   - Professional advisors (lawyers, CPAs, banker, insurance broker)
   - Venture CEO names (OPS-001, LT-005, CALLCENTER)

### Medium-term (Sep 26-30)
6. **Review ROLE-REQUIREMENTS + ONBOARDING-TEMPLATES** — Approve content
7. **Test Neo4j integration** — Verify person lookups work
8. **Activate agent routing** — Start routing real decisions through approval chain

---

## QUESTIONS FOR CLARIFICATION

1. **Should we auto-search venture repos for people names?** (Yes/No)
2. **Who is your co-principal / spouse?** [Name/Email/Phone]
3. **Do you have a family office CEO/CFO yet?** (Yes/No/TBD)
4. **Who are your key professional advisors?** (List lawyers, CPAs, banker, insurance broker)
5. **What's your philanthropic mission statement?** (1-2 paragraphs)
6. **What financial thresholds require YOUR personal review?** (e.g., <$10K = auto, $10K-$100K = CFO review, >$500K = you)
7. **Who can make decisions if you're unavailable?** (Spouse? Co-trustee? CFO?)
8. **Do you want monthly reporting on who approved what?** (Yes/No)

---

## ATTACHMENTS

- WHO-I-AM-ANTWUAN-JOHNS.md (Founder identity document)
- PEOPLE-ROLES-INFRASTRUCTURE-BRIDGE.md (Architecture guide)
- PEOPLE-VERIFICATION-AUDIT-PLAN.md (Verification methodology)
- PEOPLE-ROLES-COMPLETION-AUDIT.md (This document — full audit)

---

**Status:** ✅ Phase 1 (Structure) Complete | 🟡 Phase 2 (Verification) Ready to Start  
**Last Updated:** 2026-09-23  
**Next Review:** 2026-09-25 (after founder verification)
---

## Control Base Reference

This document is mapped to [[B201|Control Base]] in the Company Brain.

**Wiki Link:** [[CBP_REGISTRY|_REGISTRIES/CANONICAL/CBP_REGISTRY.yaml#B201]]
