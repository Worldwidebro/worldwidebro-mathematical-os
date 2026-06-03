# HRMS Blocker 1: Payroll Compliance Review

**Timeline**: May 22, 2026 (OVERDUE - was May 12-13)  
**Objective**: Get CPA sign-off on payroll tax calculation logic  
**Outcome**: Tax compliance checklist + support documentation for HRMS MVP

---

## Pre-Consultation Preparation

### What You're Building (3-min summary for CPA)
HRMS (Human Resource Management System) — SaaS for small businesses (20-200 employees).

**MVP Scope**:
- Employee management (name, DOB, tax ID, address, bank account)
- Timesheet entry (hours/week, overtime tracking)
- Payroll calculation (gross pay, deductions, net pay)
- Tax withholding (federal + state income tax, FICA)
- Paycheck generation + direct deposit

**Target Markets**: Construction, logistics, field services, manufacturing  
**Pricing**: $199/month (startup), $499/month (growth), $999/month (enterprise)  
**Compliance Scope**: Single-state payroll (start with CA, TX, NY)

---

## Tax Calculation Logic (Show This to CPA)

### Inputs Required
```
Employee:
- Gross hourly rate: $18/hour
- Federal withholding: W-4 (standard deduction, 2 allowances)
- State: CA (example)
- Tax ID (SSN)
- Filing status: Single
- Bank account (for direct deposit)

Timesheet:
- Regular hours: 40/week
- Overtime: 8 hours (1.5x multiplier)
- Exceptions: Unpaid leave, paid time off
```

### Calculation Steps (Week Pay)
```
1. Gross Pay Calculation
   - Regular pay = 40 hrs × $18 = $720
   - Overtime = 8 hrs × $27 = $216
   - Gross = $936

2. Pre-tax Deductions (401k, health insurance)
   - Assume none for MVP ($0)
   - Taxable gross = $936

3. Federal Income Tax (FIT)
   - 2026 tax tables (weekly): ~15% for single, $0 allowance
   - FIT = $140

4. Federal Payroll Taxes
   - FICA (Social Security): 6.2% × $936 = $58
   - Medicare: 1.45% × $936 = $14
   - Total FICA = $72

5. State Income Tax (CA Example)
   - CA rate: ~9.3% (simplified, actual is progressive)
   - CA SIT = $87

6. Post-tax Deductions (voluntary)
   - Assume none for MVP ($0)

7. Net Pay
   - $936 - $140 - $72 - $87 = $637

8. Employer Taxes (Not deducted from employee)
   - FICA employer match: $72
   - CA unemployment: 3.4% × $936 = $32
   - Total employer: $104
```

---

## Questions for CPA (30 minutes)

### Question Set 1: Tax Calculation Accuracy

**Q1.1**: "Is our FIT calculation correct? We're using 2026 IRS weekly tax tables with standard deduction."
- ✓ Will provide: Our formula + screenshot of IRS table lookup
- Expected answer: Confirm method is sound or suggest adjustment

**Q1.2**: "Is 6.2% Social Security + 1.45% Medicare the right withholding? Any edge cases for 2026?"
- ✓ Will provide: FICA rate calculation
- Expected answer: Confirm rates are current, note if limits apply (earnings caps)

**Q1.3**: "Our CA tax is simplified (9.3% flat). For MVP, is this acceptable, or do we need progressive brackets?"
- ✓ Will provide: CA tax table
- Expected answer: Guidance on whether progressive brackets required for compliance vs. simplified acceptable for MVP

**Q1.4**: "What about overtime rules? We're using 1.5x multiplier for hours >40/week. Any tax implications?"
- Expected answer: Confirm overtime doesn't trigger special tax treatment (it's just higher gross)

---

### Question Set 2: Withholding Accuracy

**Q2.1**: "We're ignoring pre-tax 401k and post-tax voluntary deductions in MVP. Is that OK for compliance?"
- Expected answer: Confirm MVP can ship without these

**Q2.2**: "Employees provide W-4, but we haven't implemented W-4 form parsing. Can we ask them to just tell us 'allowances' and 'filing status'?"
- Expected answer: Confirm that employee-reported info is acceptable (they're responsible for accuracy)

**Q2.3**: "We're calculating federal tax using single year (2026). What happens in 2027? Do we need to update our tax tables?"
- Expected answer: Guidance on when/how to update tables

---

### Question Set 3: Edge Cases & Compliance

**Q3.1**: "What do we do if an employee has multiple jobs? W-4 allows for that. Is our system supposed to handle it?"
- Expected answer: For MVP, likely "employee's responsibility" — document in FAQ

**Q3.2**: "What about new employees mid-pay-period? Do we prorate or use full weekly calculation?"
- Expected answer: Confirm prorating is correct approach

**Q3.3**: "Do we need to file payroll tax electronically (EFTPS)? Or can customers do it themselves?"
- Expected answer: For MVP, customers file themselves. Scope this as Phase 2.

**Q3.4**: "Are there state-specific requirements we're missing for CA, TX, NY? Any different from federal?"
- Expected answer: Brief summary of state-specific rules

---

## Compliance Checklist for MVP (What to Document)

### In HRMS MVP Code/Docs
- [ ] Tax year hardcoded (2026) with comment: "Update annually for IRS table changes"
- [ ] W-4 form fields captured (filing status, allowances)
- [ ] FIT, FICA, state tax calculated with documented formulas
- [ ] Overtime rule documented (1.5x after 40 hours)
- [ ] Rounding rule (cents) documented
- [ ] Edge cases noted: new employees, multiple jobs, W-4 changes

### In HRMS Customer Docs
- [ ] "Employee Responsibility" section: "HRMS calculates withholding based on W-4. Employees are responsible for W-4 accuracy."
- [ ] Tax table update notice: "Tax tables updated annually (January). Check for updates."
- [ ] State-specific guidance for CA, TX, NY (3 docs, 1 page each)
- [ ] FAQ: Multiple jobs, mid-period hires, W-4 changes

---

## Success Criteria for CPA Sign-Off

- [ ] **Calculation accuracy**: "Yes, this approach is compliant for 2026"
- [ ] **Withholding logic**: "Yes, W-4 parsing is acceptable"
- [ ] **MVP scope**: "Yes, you can ship MVP without 401k/deductions"
- [ ] **Edge cases**: CPA confirms which are out-of-scope for V1.0
- [ ] **Documentation**: CPA confirms customer-facing docs are clear

---

## What to Send to CPA (Email Before Call)

```
Subject: Quick payroll tax logic review — 30 min call?

Hi [CPA Name],

We're building an HRMS (small business payroll SaaS) and want a quick compliance review on our tax calculation logic before we ship the MVP.

MVP scope:
- Federal income tax (FIT) + FICA (Social Security/Medicare) + CA/TX/NY state income tax
- W-4 based withholding
- Direct deposit + weekly pay
- Employees: 20-200 person companies

I've attached:
1. Our tax calculation formula (step-by-step, with example)
2. Key questions (30 min conversation)
3. What we're asking for: Confirmation that approach is compliant for 2026

Are you available for a 30-minute call [DATE RANGE]? Usual rate is fine.

Thanks,
[Your Name]
```

---

## CPA Outreach (Find Someone)

### Ideal CPA Profile
- **Experience**: Payroll processing, small business tax
- **Availability**: 1-2 weeks for initial review, ongoing support
- **Location**: CA preferred (handles CA specifics), but remote OK
- **Cost**: $500-1K for initial review, $200-300/hour for ongoing support

### Where to Find
- [ ] Referrals: Ask construction/logistics business owner you know
- [ ] LinkedIn: Search "CPA payroll consultant" + location
- [ ] Avvo/Justia: Legal directories with CPA listings
- [ ] Local business associations: Chamber of Commerce referrals

### What to Say
"We're building HRMS software (payroll for small businesses). Need a CPA to review our tax logic—30 min initial call, then ongoing support as we add features. Are you available?"

---

## Post-Call: Documentation Action Items

Once CPA approves, create:
1. **HRMS-TAX-RULES.md** — CPA-approved formulas with notes
2. **HRMS-MVP-SCOPE.md** — What's in V1.0, what's Phase 2+
3. **HRMS-CUSTOMER-COMPLIANCE.md** — What customers need to know
4. **Code comments** — Add CPA name + "approved [DATE]" to every tax calculation

---

## Timeline to Unblock Task 9

- **Today (May 22)**: Send to CPA, schedule call
- **May 23**: CPA call + approval
- **May 24**: Document in code, move to Task 9 (Financial Analyst Agent)

**Blocking**: Tasks 9, 10, 11 (all depend on compliance sign-off)
