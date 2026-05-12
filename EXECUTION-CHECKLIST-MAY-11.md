# Execution Checklist — Start Today

## 🚀 TODAY (May 11, Friday)

- [ ] **Email CPA** (5 min)
  - Use template from CPA-REVIEW-BRIEFING.md
  - Target: Schedule for Mon-Tue
  
- [ ] **Review BLOCKER-EXECUTION-2026-05-11.md**
  - Print the parallel timeline table
  - Assign tasks to team
  
- [ ] **OpenVolo API Access Check**
  - Do you have OpenVolo credentials?
  - Can you run a query? (Test query: construction + CA + 20-150 emp)
  - If not: Get API key from OpenVolo admin

---

## 📅 MONDAY (May 12, Start of Week)

**Morning**:
- [ ] CPA call (if scheduled)
- [ ] Pull top 20 leads from OpenVolo
  - Export to CSV: Name, Title, Email, Phone, Company, Employees
  - Share with #sales in Slack
- [ ] Create Calendly link for 30-min discovery calls
  - Add to Calendly: Recurring slots Mon-Fri, 10am/2pm PT
  - Copy link to clipboard

**Afternoon**:
- [ ] Send first 4 discovery call emails (use script from BLOCKER-EXECUTION)
  - "Hi [Name], quick 15-min call about your payroll process?"
  - Link: [Calendly link]
  - Target: Schedule calls for Tue/Wed/Thu/Fri
- [ ] Fork Mission Control repo
  - Create new repo: `hrms-saas-mvp`
  - Copy Mission Control code + config
  - Update README with "HRMS MVP — Payroll for field service companies"
  - Set up Node dependencies (npm install)

---

## 💻 CODING TIMELINE (Parallel to Blockers)

**Mon 5/12**: Fork + setup  
**Tue 5/13**: Database schema (companies, employees, payroll_runs, tax_settings)  
**Wed 5/14**: Employee CRUD endpoints + frontend  
**Thu 5/15**: Payroll calculation logic (tax withholding)  
**Fri 5/16**: Pay stub generation + Stripe integration  
**Mon 5/19**: Onboarding flow + demo  
**Tue 5/20**: Internal testing  
**Wed 5/21**: First beta customer starts trial  

---

## 📞 DISCOVERY CALLS (Mon-Thu)

| Day | Time | Company | Contact | Goal |
|-----|------|---------|---------|------|
| Mon 5/12 | 10am PT | [Construction] | [Finance Dir] | Pain points + tier sizing |
| Tue 5/13 | 2pm PT | [Logistics] | [HR Manager] | Multi-state + feature validation |
| Wed 5/14 | 10am PT | [Field Services] | [Finance Dir] | Switching cost + benefits |
| Thu 5/15 | 2pm PT | [Construction] | [CEO/Finance] | Enterprise scope + API needs |

**Script**: Use BLOCKER-EXECUTION-2026-05-11.md "Discovery Call Script"  
**Outcome**: 4 call notes + findings file  
**Target**: 2-3 customers interested in beta trial

---

## ✅ SUCCESS = First Call Completed

Everything else flows from getting the first discovery call on the calendar Monday morning.

Don't overthink it. Just send the email.
