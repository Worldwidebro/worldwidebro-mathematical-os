# Three-Layer Alignment Map

**Date:** 2026-09-19  
**Purpose:** Show how Global CLAUDE.md → Project CLAUDE.md → ANTIGRAVITY.md work as an integrated system  
**Authority:** CP-027 Infrastructure + CP-033 Execution

---

## The Three Layers

```
GLOBAL CLAUDE.md (Master Blueprint)
    ↓ defines context + infrastructure
PROJECT CLAUDE.md (Session Execution)
    ↓ enforces rules + operationalizes
ANTIGRAVITY.md (Operating Discipline)
    ↑ validates every decision + execution
```

### Layer 1: GLOBAL CLAUDE.md (`~/.claude/CLAUDE.md`)

**What:** Master blueprint for ALL projects, ALL time  
**Who:** Architecture owner, infrastructure maintainer  
**When loaded:** Onboarding, new phase, infrastructure changes  
**Answers:** "What exists? Where? How is it wired? What's the master plan?"

**Content:**
- 22-stage cognitive pipeline
- 9 cognitive fabrics
- 104 folders, 50 domains, 500+ control points
- Infrastructure (Mac Studio, Mac Air, Tailscale, databases)
- 789 ventures, 35 sectors, 904 starred repos, 177 code repos
- Phase 0/1 status (locked/complete)
- Canonical registries (10 sources of truth)
- Master memory system

**Example:** "Neo4j has 20,363 edges at bolt://100.87.214.70:7687"

---

### Layer 2: PROJECT CLAUDE.md (`./CLAUDE.md`)

**What:** Session guidance for THIS week/phase  
**Who:** Active engineer/agent in this session  
**When loaded:** Session start, before executing any task  
**Answers:** "What do I do today? What's the status? What are the rules?"

**Content (Sep 19):**
- Current phase: Week 2 Revenue Scaling (Sep 16-22)
- Phase 1 locked (Sep 6-15), Phase 2 launched (Sep 16-30)
- 6 Tier-0 ventures status (which are revenue-ready now)
- Three revenue focuses for this week
- Quick commands for verification
- Git invariants (7-point protocol)
- Cross-references to ANTIGRAVITY.md rules (Rules 2, 11, 31, 34, 44)
- ONE RULE expanded with Rule 44 (9-step execution protocol)

**Example:** "This week: OPS-001 → cold call campaign (Rule 44: Execute → Observe → Verify)"

---

### Layer 3: ANTIGRAVITY.md (`./ANTIGRAVITY.md`)

**What:** Operating discipline for ALL work in Company Brain  
**Who:** Everyone building/maintaining the system (agents, engineers, architects)  
**When applied:** EVERY decision, EVERY task, EVERY execution  
**Answers:** "How should I think? What are the rules? What must I never do?"

**Content (45 Rules):**

| Rule | Name | Purpose |
|------|------|---------|
| 1-10 | Core Principles | North Star, reuse, repo intelligence, knowledge graph, OmniRoute, agents, approvals, Git, multi-agent, human approval |
| 11-20 | Infrastructure & Discipline | Git safety, artifacts, testing, verification, security, data integrity, observability, perf, context, local compute |
| 21-30 | Design & Operations | Storage, app architecture, APIs, databases, dependencies, external repos, decision logs, change mgmt, failure handling |
| 31-45 | Execution Discipline | No fake completion (Rule 31), no placeholders (Rule 32), business-first (Rule 33), **reuse-first (Rule 34)**, source of truth (Rule 35), documentation (Rule 36), workflows (Rule 37-39), **multi-repo orchestration (Rule 40)**, artifact-first (Rule 41), continuous improvement (Rule 42), priority order (Rule 43), **default agent protocol (Rule 44)**, final rule (Rule 45) |

**Most Critical Rules Enforced in Week 2:**
- **Rule 2:** Every decision: problem → user → outcome → existing → reuse → dependencies → systems → risks → success → verification
- **Rule 31:** Only report: IMPLEMENTED | TESTED | VERIFIED | DEPLOYED | OBSERVED
- **Rule 34:** MANDATORY starred repo search (904 repos) BEFORE building
- **Rule 44:** 9-step protocol (Understand → Inspect → Reuse → Plan → Execute → Test → Verify → Document → Report)

**Example:** "Rule 44 says: Don't just code. Understand the problem, inspect existing, search 904 repos first, then execute."

---

## How They Interlock

### Scenario: "Build a new feature for OPS-001"

**Step 1 — Know context (GLOBAL CLAUDE.md):**
- OPS-001 is a staffing placement venture (deployed, Vercel, HTTP 200)
- Repos: `worldwidebro/ops-staff-001-*`
- Capabilities used: CAP-SCHEDULING, CAP-CRM, CAP-MESSAGING
- 177 code repos available for reuse

**Step 2 — Know the plan (PROJECT CLAUDE.md):**
- Week 2 focus: Cold call campaign + lead follow-up (Sep 16-22)
- Rule to apply: ANTIGRAVITY Rule 44 (9-step protocol)
- Rule to remember: ANTIGRAVITY Rule 34 (search 904 repos first)

**Step 3 — Execute discipline (ANTIGRAVITY.md):**
1. **Understand** (Rule 44): What's the feature? Who needs it? What outcome?
2. **Inspect**: Read OPS-001 code, schema, API contracts
3. **Reuse** (Rule 34): Query 904 starred repos for scheduling/CRM/messaging libraries
   - Found: APScheduler (20K stars), python-crm (1.2K), sendgrid-python
4. **Plan**: Design minimal integration (Rule 2: Determine dependencies)
5. **Execute**: Code the feature
6. **Test**: Unit + integration tests (Rule 14: Testing mandated)
7. **Verify** (Rule 31): Report: IMPLEMENTED (not tested), → TESTED (tests pass), → VERIFIED (E2E works), → DEPLOYED (live), → OBSERVED (metrics confirm)
8. **Document**: Update REPOSITORY_REGISTRY.yaml + capabilities
9. **Report**: Summary of changes + tests + verification

**Result:** Feature ships with full audit trail, no fake completion, reuse maximized.

---

## Verification Checklist

**Before claiming any work is "done":**

- [ ] Did I follow ANTIGRAVITY Rule 44 (9-step protocol)?
- [ ] Did I search 904 starred repos first (Rule 34)?
- [ ] Did I report correct state: IMPLEMENTED/TESTED/VERIFIED/DEPLOYED/OBSERVED (Rule 31)?
- [ ] Did I determine the real problem + outcome (Rule 2)?
- [ ] Did I verify with actual CLI output, not documentation (PROJECT CLAUDE: ONE RULE)?
- [ ] Did I follow Git safety (Rule 11: pre/post-change protocol)?
- [ ] Did I update registries (Rule 35: canonical sources)?
- [ ] Did I document for the next agent (Rule 41: artifact-first)?
- [ ] Did I test at the right level (Rule 14: lint → type → unit → integration → E2E)?
- [ ] Did I update memory or decision log if something surprising happened (Rule 42)?

---

## When Each Layer Changes

| File | Frequency | Trigger | Authority |
|------|-----------|---------|-----------|
| **GLOBAL CLAUDE.md** | Quarterly / Major phase | New phase, new infrastructure, new sector | Architecture CP-027 |
| **PROJECT CLAUDE.md** | Weekly | New week, status changes, phase changes | Execution CP-033 |
| **ANTIGRAVITY.md** | Never (canonical) | Rare: core operating principle changes | Engineering Discipline (all) |

---

## Sep 19 State Summary

✅ **GLOBAL CLAUDE.md:**
- Phase 1 locked (Sep 6-15)
- Phase 2 launched (Sep 16-30, Neo4j schema deployed Sep 18)
- 6 Tier-0 ventures live
- Infrastructure stable

✅ **PROJECT CLAUDE.md:**
- Updated to Week 2 (Sep 16-22)
- Three revenue focuses + parallel Phase 2 graph work
- All ANTIGRAVITY rules cross-referenced
- ONE RULE expanded with Rule 44 (9-step protocol)

✅ **ANTIGRAVITY.md:**
- 45 rules canonical and enforced
- Rules 2, 11, 31, 34, 44 explicitly cited in PROJECT CLAUDE.md
- Rule 34 (starred repo search) is MANDATORY before any build

---

## Next Checkpoints

| Date | Checkpoint | Owner |
|------|-----------|-------|
| **Sep 22** | Week 2 revenue audit (ANTIGRAVITY Rule 31: verify DEPLOYED state) | Execution CP-033 |
| **Sep 30** | Phase 2 handoff (Neo4j migration Sep 17–Oct 1 complete) | Infrastructure CP-027 |
| **Oct 1** | Phase 2a agents deployed (graph-native + agentic engineering) | Agents CP-029 |
| **Oct 31** | Phase 2a completion (50 agents, $1.35M capital attributed) | Revenue CP-021 |

---

**Alignment Status:** ✅ COMPLETE (Sep 19, 2026)  
**All three layers operational and cross-referenced**
