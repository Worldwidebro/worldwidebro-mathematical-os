# Business Artifact Ontology — Quick Start Guide

**For venture teams closing deals**

[[STARTHERE|STARTHERE.md]] | [[CAPITAL-READINESS-ENGINE|CAPITAL-READINESS-ENGINE.md]] | [[SECTOR-TAXONOMY-MASTER|SECTOR-TAXONOMY-MASTER.md]]

---

## You Have a New Deal

Your venture is raising capital, acquiring another company, or doing a partnership. You need to know:

1. **What documents do I need?**
2. **In what order?**
3. **What's blocking me?**
4. **When is it due?**

This system answers all four.

---

## TL;DR: 3-Step Process

### Step 1: Query Your Requirements (2 minutes)

Run this command:

```bash
cb document-requirements [VENTURE_ID]
```

Example:
```bash
cb document-requirements CON-001
```

**Output:**
```
╔════════════════════════════════════════╗
║     CON-001 DEAL REQUIREMENTS          ║
╠════════════════════════════════════════╣
║ Deal Type: Construction Acquisition    ║
║ Sector: SEC-002                        ║
║ Jurisdiction: North Carolina           ║
║ Deal Size: $5.2M                       ║
║                                        ║
║ Required Documents: 48                 ║
║ Critical Path Documents: 12            ║
║ Timeline: 63 days                      ║
║ Current Status: In Diligence (64%)     ║
║                                        ║
║ Next Milestone:                        ║
║ → Environmental approval (Due Sep 20)  ║
║ → Ready for Definitive Docs (Sep 25)   ║
║                                        ║
║ Blockers: None                         ║
║ At-Risk Items: 0                       ║
╚════════════════════════════════════════╝
```

### Step 2: Open Your Deal Project in ClickUp (1 minute)

Your deal already has a ClickUp project with all 48 tasks:

```
ClickUp: "CON-001 Deal Closure"
├─ Phase 1 (Discovery): 3 tasks, all complete
├─ Phase 2 (Qualification): 8 tasks, 7 complete, 1 in review
├─ Phase 3 (Term Sheet): 12 tasks, 11 complete, 1 awaiting signature
├─ Phase 4 (Diligence): 15 tasks, 11 complete, 4 in progress
├─ Phase 5 (Definitive Docs): 10 tasks, not started (blocked by Phase 4)
└─ Phase 6 (Closing): 0 tasks, not started (blocked by Phase 5)

Next Due:
  ▶ "Environmental Assessment Complete" (Sep 20)
  ▶ "Officer Certificates Ready" (Sep 23)
  ▶ "Cap Table Signed" (Sep 25)
```

Assigned tasks show:
- **Who's responsible** (your counsel, CFO, advisor, etc.)
- **When it's due**
- **What blocks it** (dependencies)
- **What it unblocks** (what comes next)

### Step 3: Check Dashboard Status (30 seconds)

**One-page view of where you are:**

```
CON-001 Deal Progress

Stage: Diligence (Week 10 of 9 planned) ⚠️ 1 week slip
Progress: 64% (31 of 48 documents complete)

Document Status:
  ✅ Financial: 8/8 complete
  ✅ Legal: 12/15 complete
  ⚠️  Tax: 5/6 complete (1 in review)
  ✅ HR: 8/8 complete
  🛑 Environmental: 3/4 complete (1 BLOCKED)
  ⏳ Regulatory: 6/9 in progress

Blockers:
  🛑 Phase I Environmental Assessment (due Sep 20)
     └─ Delays Diligence approval gate
     └─ Impacts close date: Now Dec 7 (was Nov 30)
     └─ Responsible: Environmental consultant
     └─ Status: Report in review, expecting Sep 20

Next Gate: Diligence Complete (Sep 25)
  → Ready to move to Definitive Docs
  → Unblocks SPA negotiation

Approval Status:
  ✅ Deal economics approved by CFO
  ✅ Financing pre-approval in place
  ✅ Regulatory permits path clear
  ⏳ Board approval scheduled Sep 23

Close Target: Dec 7, 2026 (target $5.2M)
```

---

## Detailed Workflows

### I'm Starting a New Deal

```
1. Contact: CP-032 (Business Operations)
   Email: [venture-lead]@worldwidebro.com
   Slack: @venture-lead

2. Provide:
   - Venture ID (e.g., CON-001)
   - Deal type (Acquisition, Financing, Partnership, Real Estate, Licensing)
   - Sector (SEC-###)
   - Deal size ($$$)
   - Jurisdiction (North Carolina, Federal, etc.)
   - Target close date

3. System auto-creates:
   ✅ ClickUp project with all required docs + timeline
   ✅ Dashboard tracking
   ✅ Buzz channel (#con-001-deal)
   ✅ Neo4j graph nodes + relationships

4. You get:
   - ClickUp project link
   - Dashboard link
   - Document requirement summary
```

### I'm in Middle of a Deal (like CON-001)

```
ClickUp Project URL: [provided by CP-032]

Today's Task:
1. Open ClickUp "CON-001 Deal Closure"
2. Look at "In Progress" and "Awaiting Signature" tasks
3. Update status as docs move forward
4. Alert CP-032 if any blockers or delays

ClickUp automations handle:
✅ Updating dashboard when status changes
✅ Notifying Buzz when milestone hits
✅ Flagging at-risk items (overdue docs)
✅ Enabling next phase tasks when gate is cleared
```

### I'm Blocked on a Document

**Example: "Environmental Assessment report delayed"**

```
In ClickUp, update task: "Phase I Environmental Assessment Complete"
  Status: "Blocked — Report delayed until Sep 20"
  Comment: "@jane_smith Consultant says report pushes to Sep 20. 
            Impacts close timeline by 7 days."
  
Automation triggers:
  ✅ Dashboard updates: "Environmental: BLOCKED"
  ✅ Close date recalculates: Nov 30 → Dec 7
  ✅ Buzz notifies #deals-at-risk: "CON-001 blocked on environmental (7-day slip)"
  ✅ Dependent tasks ("Diligence Approval") pause until unblocked

To unblock:
  When report arrives:
    ✅ Update task: "Phase I Complete, Approved"
    ✅ Dependent tasks resume
    ✅ Close date updates back
    ✅ Buzz notifies: "CON-001 environmental blocker cleared"
```

### I Want to Know: "Can We Close This Quarter?"

```bash
cb query-deals "closing_date <= 2026-12-31"

Results:
  ✅ LT-005 — closing Dec 15 (100% ready)
  ✅ CON-001 — closing Dec 7 (blockers cleared)
  ⚠️  RE-001 — closing Dec 28 (at risk, 5 docs pending)
  ❌ OPS-001 — closing Jan 15 (2+ months away)

Summary: 2 deals close this quarter, 1 at risk, 1 next quarter
```

### I Want to Know: "What's Blocking Me?"

```bash
cb query-deals "status = BLOCKED"

Results:
  🛑 OPS-001
     ├─ Blocker: Cap Table not final (CEO sign-off pending)
     ├─ Impact: Can't finalize investor agreements
     ├─ Days overdue: 2
     ├─ Responsible: John Davis (CFO)
     └─ Action: @john Urgent — cap table needs CEO sign-off today

  🛑 RE-001
     ├─ Blocker: Title search incomplete
     ├─ Impact: Can't order title insurance
     ├─ Days overdue: 3
     ├─ Responsible: Title company
     └─ Action: @jane_smith Follow up with title company — expedite please
```

### I'm Handing Off to Another Team

**Example: "We acquired CON-001, now we need to close the financing deal for integrating it."**

```
1. ClickUp task: "Acquisition Closed" marked complete
2. Dashboard shows: CON-001 stage = "Post-Closing"
3. New deal starts: CON-002 (Financing Integration)
4. CP-032 auto-creates:
   ✅ New ClickUp project for financing (30-doc requirement)
   ✅ New dashboard tracking
   ✅ Buzz channel #con-002-financing-deal
   ✅ Neo4j: Links CON-001 → CON-002 (successor deal)

Handoff meeting:
  - Previous deal lead walks through CON-001 post-close items
  - New deal lead gets CON-002 ClickUp project + timeline
  - Both teams coordinate on transition (30 days)
```

---

## Common Questions

### Q: "I don't see my deal in the system yet"

**A:** Your deal is in one of two states:

1. **Planned but not started** 
   - Contact CP-032 to activate
   - They'll create your ClickUp project + dashboard

2. **Started but not yet in system**
   - CP-032 backlogs deals in order of close date
   - If urgent, email CP-032 to prioritize

### Q: "How do I update the dashboard?"

**A:** You don't — ClickUp updates are automatic.

```
Your workflow:
  1. ClickUp task status changes (Not Started → In Progress → etc.)
  2. Automation watches ClickUp
  3. Dashboard auto-updates
  4. Buzz notified
  5. Neo4j graph synced

You never manually edit the dashboard.
```

### Q: "What if our deal is non-standard?"

**A:** Template covers:
- ✅ Acquisitions
- ✅ Financing (SAFE + Term Sheet)
- ✅ Partnerships
- ✅ Employment (exec hiring)
- ✅ Real Estate
- ✅ Licensing

**If your deal is different:**
  - Contact CP-032 (Business Operations)
  - They'll create a custom template
  - Estimate: 1-2 hours

### Q: "Can I see other ventures' deals?"

**A:** Yes, with permissions.

**Read-only access:**
  - Dashboard shows all deals (status, progress, blockers)
  - ClickUp projects viewable if you're team member

**Full access:**
  - Only if you're deal lead or on deal team
  - Contact CP-032 for permissions

### Q: "How do I integrate the prospectus with deal tracking?"

**A:** Automatic via wiki links.

```
Your prospectus (CON-001/INSTITUTIONAL-PROSPECTUS.md) links to:
  → CAPITAL-READINESS-ENGINE.md
  → Deal Status Dashboard (CON-001 section)
  → Requirement summary

Your ClickUp project links to:
  → Prospectus (document source of truth)
  → Dashboard (real-time status)
  → Requirement engine (what's needed)

Everything connected bidirectionally.
```

---

## For Executives: Real-Time Deal Status

**CEO Dashboard (30-second view):**

```
PORTFOLIO STATUS
═══════════════════════════════════════════

Deals in Motion: 5
├─ Closing this quarter: 2
├─ On track: 3
├─ At risk: 1 (OPS-001 blocker)

Capital Impact: $24.3M pipeline
├─ Ready to wire: $8M (LT-005 + CON-001)
├─ 30 days out: $12M (RE-001)
├─ 60+ days out: $4.3M (OPS-001, LT-011)

Critical Blockers: 1
  🛑 OPS-001 — Cap Table sign-off (John Davis, 2 days overdue)
     → Action: Board approval scheduled Sep 23

Document Completion: 78% average
├─ LT-005: 100% (ready to close)
├─ CON-001: 64% (1-week slip due to environmental)
├─ RE-001: 71% (on track)
├─ OPS-001: 58% (blocker, recovering)
└─ LT-011: 37% (early, on track)

Next Approval Gate: CON-001 Diligence (Sep 25)
Next Close: LT-005 (Sep 28)
```

**Real-time queries:**
```
"Show me all at-risk items across the portfolio"
→ 1 blocker (OPS-001 cap table)

"Which ventures need board approval this month?"
→ CON-001 (Sep 23), OPS-001 (Sep 30)

"What's our close revenue this quarter?"
→ $8M+ (LT-005 + CON-001)
```

---

## Support & Escalation

**For questions about:**
- Document requirements → CP-032 (Business Operations)
- ClickUp setup/changes → CP-033 (Execution)
- Dashboard/Neo4j access → CP-013 (Knowledge Graph)
- Buzz notifications → CP-028 (Collaboration)

**Email:** [venture-lead]@worldwidebro.com  
**Slack:** #deals-operations

**Escalations:** If you're blocked and need immediate help:
```
1. Post in Buzz: @venture-lead "Urgent: [blocker description]"
2. Email: [venture-lead]@worldwidebro.com with subject "BLOCKED: [deal] [doc]"
3. Call: [venture-lead] (direct number in directory)
```

---

**Authority:** CP-032 (Business Operations Control Plane)  
**Governed by:** [[ANTIGRAVITY|ANTIGRAVITY.md]] Rules #3 (Clear Processes) + #15 (Real-Time Visibility)

