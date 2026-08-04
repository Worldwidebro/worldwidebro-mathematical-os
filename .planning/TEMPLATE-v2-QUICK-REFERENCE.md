# Template v2 Quick Reference Card

Use these templates for all venture requests. Each has a specific purpose and expected output.

---

## [VENTURE STATUS] — Current State Assessment

**Use**: Understanding where a venture stands before taking action.

```
Input:
[VENTURE STATUS]
Ventures: CON-001, LT-005
Source: Supabase, GitHub, Vercel
Check: deployment, code state, integrations, testing

Output:
| Current state (narrative)
| Blockers (1-5 bullets)
| Dependencies
| Next milestone
| Launch readiness (%)
| Days to launch (int)
| Priority (P0-P4)
```

---

## [ACTION] — Execute a Task

**Use**: Build, deploy, fix, or test something specific.

```
Input:
[ACTION]
Venture: CON-001
Objective: Deploy production website
Tasks: [list]
Success Criteria: [checklist]
Priority: P0
Deadline: Today

Output:
| ✓ Task completed OR ✗ Task blocked (reason)
| Evidence: GitHub / Vercel / Supabase
| Next step if blocked
```

---

## [DECISION] — Choose Between Options

**Use**: Multiple valid paths exist; you need a recommendation.

```
Input:
[DECISION]
Topic: ConstructionOS MVP strategy
Decision: Launch single product vs build platform first?
Constraints: [budget/time/revenue]
Success Metric: [goal]

Output:
| Recommendation: [A/B/C with rationale]
| Trade-offs: what you're giving up
| Timeline: when it matters
| Next action: 1 concrete step
```

---

## [PARALLEL] — Multiple Ventures + Multiple Tracks

**Use**: Coordinating work across ventures or domains.

```
Input:
[PARALLEL]
Ventures: CON-001, LT-005, OPS-STAFF-001
Tracks: Revenue, Deployment, Code, Acquisition, Infrastructure
Output: Status grid, Critical path, Blockers, Risk flags, Ready to ship?

Output:
| Status grid (venture × track matrix)
| Critical path (dependency order)
| Blockers per venture
| Risk level: HIGH/MEDIUM/LOW
| Ready to ship: YES/MAYBE/NO
```

---

## [AUDIT] — Inspect Before Changing

**Use**: Understanding current state before modifications.

```
Input:
[AUDIT]
Venture: CON-001
Audit: Repository, Supabase, Vercel, Env vars, Integrations, DB
Return: Missing, Broken, Incomplete, Duplicate

Output:
| Finding: [Missing/Broken/Incomplete/Duplicate]
| Location: [file/field/service]
| Impact: [critical/high/medium/low]
| Recommendation: [action]
```

---

## [ROADMAP] — Plan Execution

**Use**: Breaking complex goal into day-by-day tasks.

```
Input:
[ROADMAP]
Venture: LT-005
Goal: Launch in production
Time: 14 days
Return: Day-by-day tasks, Dependencies, Critical path, Deliverables

Output:
Day 1: [Task] → Deliverable: [X]
Day 2: [Task] → Deliverable: [Y]
...
Day 14: [Task] → Deliverable: [Production URL]

Critical path: [what can't slip]
Risk flags: [blockers]
Confidence: [HIGH/MEDIUM/LOW]
```

---

## PRIORITY FRAMEWORK

| P0 | Revenue blocker; if not done, business doesn't work |
|----|-----|
| P1 | Launch blocker; can't go live without this |
| P2 | Important; valuable but not critical |
| P3 | Nice to have; backlog |
| P4 | Speculative; doesn't impact current goal |

---

## EVIDENCE & CONFIDENCE

```
Source               Confidence  Verify With
─────────────────────────────────────────────
✓ GitHub code/config     HIGH     gh api repos/...
✓ Vercel deployment      HIGH     vercel list
✓ Supabase schema        HIGH     psql -d ventures
✗ Not deployed          MEDIUM    Manual check
? Documentation only     LOW       Verify in running system
? Assumption/estimate    LOW       Requires confirmation
```

---

## STANDARD RESPONSE FORMAT

```
Template: [TYPE]

Venture: [ID]

Current State:
[1-2 sentence summary]

Status Grid (if multiple):
[Table]

Blockers:
[1-5 bullets, ranked by impact]

Critical Path:
[Dependency order]

Next Action:
[1 specific thing]

Evidence: [Source]
Confidence: [HIGH/MEDIUM/LOW]
Priority: [P0-P4]
Timeline: [When matters]
```

---

## COMMON MISTAKES

❌ "It should work"  
✅ "GitHub repo has package.json + vercel.json (verified)"

❌ Guess launch dates  
✅ "2 days (env vars) + 1 day testing"

❌ Mix decisions and status  
✅ Use [DECISION] for choices, [VENTURE STATUS] for assessment

❌ Forget evidence  
✅ "Confidence: HIGH (Vercel deployment verified)"

❌ No deadline/priority  
✅ "P0 | Deadline: Today"

---

**Version**: v2.0  
**Created**: 2026-07-30  
**Companion**: VENTURE-AUDIT-2026-07-30.md
