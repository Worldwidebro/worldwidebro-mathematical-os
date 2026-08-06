---
name: CPA-REVIEW-BRIEFING
title: CPA Review Briefing — HRMS Payroll SaaS
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# CPA Review Briefing — HRMS Payroll SaaS

**Goal**: 2-hour consultation to validate tax withholding logic for MVP launch

**Email Template for CPA**:

---

Hi [CPA Name],

I'm building payroll software for construction/field service companies (20-150 employees). We want to launch an MVP in 2 weeks that handles payroll + tax compliance for three states (California, Texas, New York).

I need a 2-hour consultation to review our tax calculation logic. Here's what we'd cover:

**In Scope (Must Support V1.0)**:
- Federal income tax withholding (2026 IRS tables, single/married/head of household)
- State income tax withholding (CA, TX, NY only)
- FICA deductions (6.2% Social Security + 1.45% Medicare)
- FUTA (0.6%) and SUTA (state unemployment rates)
- W-2 and 941 compliance form generation

**Out of Scope (V1.0 Limitations)**:
- 1099 contractors
- International payroll
- Multi-state companies with employees in other states
- Local income taxes
- Complex benefits/deductions beyond standard W-4

**Questions for You**:
1. Is our MVP scope realistic to launch in 2 weeks?
2. What's the minimum compliance checklist we must have?
3. Are there state-specific gotchas in CA/TX/NY we should know?
4. If our calculations are wrong, what's the liability risk?

**When**: This week (May 12-15), 2 hours, Zoom or in-person  
**Rate**: I'll pay your standard consulting rate ($X/hour or $X flat)

Can you help?

Thanks,  
Ace

---

**For Ace's Conversation**:
- Confirm CPA is familiar with modern payroll (e.g., has done Gusto/ADP integrations)
- Ask about their experience with startup payroll products (they'll have realistic expectations)
- Record key findings in spreadsheet:
  - Federal logic: Approved? ✅/❌
  - State logic (CA/TX/NY): Approved? ✅/❌
  - FICA/FUTA: Approved? ✅/❌
  - Gap areas to watch: [list]
  - Recommended scope cuts: [list]
- Get written confirmation email from CPA (not just verbal)

**Typical Cost**: $500-1,500 for 2-hour consultation  
**Typical Timeline**: Can schedule within 3 days if you're flexible on time

---

**After CPA Call**:
Document their feedback in HRMS-BUSINESS-LOGIC.md under "Blocker 1: CPA Review" with ✅ status + key findings.

This is your legal/compliance checkpoint. Don't skip it.
