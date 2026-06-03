# HRMS — Paperclip Workflow Automation
**Status**: Ready to configure  
**Purpose**: Automate sales process, customer onboarding, and support workflows in Paperclip  
**Integration**: Paperclip + Composio + OpenVolo + Slack

---

## 🔄 Sales Pipeline Workflow

### Workflow 1: Lead → Discovery Call → Trial
**Owner**: Sales agent in Paperclip  
**Trigger**: New lead added from OpenVolo

**Steps**:
1. **Lead Discovery Task** (assigned to Sales PM)
   - Title: "Call [Company]: [Contact name] — Construction, 50 employees"
   - Context: "Pain point: Multi-location payroll. Job title: Finance Director. Phone: 555-1234"
   - Subtasks:
     - [ ] Schedule discovery call (goal: 15 min)
     - [ ] Prepare: What's their current payroll process?
     - [ ] Ask: Would you try payroll software that cuts time by 50%?
     - [ ] Outcome: Interested / Not interested / Call back later
   - Due: 2 days
   - CTA on complete: "Record outcome and next step"

2. **Demo Scheduling Task** (if interested)
   - Title: "Schedule demo for [Company]"
   - Context: "[Contact] interested in 20-minute demo"
   - Action: Send Calendly link via email (Composio email_send)
   - Subtasks:
     - [ ] Send Calendly + "Here's what you'll see in demo"
     - [ ] Confirm demo time (auto-reply adds to calendar)
     - [ ] Prepare demo environment (load [Company] data template)
   - Due: 1 day

3. **Demo Execution Task** (day of demo)
   - Title: "Demo: [Company] — 2pm PT"
   - Context: Finance Director walkthrough (40 min)
   - Sequence:
     - Show employee directory (60 sec)
     - Show payroll run (60 sec)
     - Show compliance reports (60 sec)
     - Q&A (20 min)
     - Close: "Want to try free for 14 days?"
   - Outcome: Yes / No / Maybe / Follow-up needed
   - CTA: "Create trial account OR schedule follow-up call"

4. **Trial Signup Task** (if said yes)
   - Title: "Trial: [Company] — activate account"
   - Context: "[Contact] approved for free 14-day trial"
   - Actions:
     - [ ] Create account in HRMS app (Composio app_create_account)
     - [ ] Send login credentials + welcome email (Composio email_send)
     - [ ] Schedule "Day 3 check-in call" (Composio calendar_create)
     - [ ] Send Slack notification: "[Company] on trial"
   - Success criteria: Account created + email sent
   - Next stage: Customer onboarding (see below)

5. **Trial-to-Paid Conversion Task** (day 13)
   - Title: "Conversion: [Company] — trial ends tomorrow"
   - Context: "[Company] trial ending May 25. Activate billing."
   - Subtasks:
     - [ ] Measure: Did they add employees? How many? (shows engagement)
     - [ ] Send email: "Your trial ends tomorrow. Here's why [Company] kept HRMS"
     - [ ] Add payment method option (link to billing page)
     - [ ] Schedule follow-up call if hesitant
   - Success: Subscription active OR scheduled follow-up call

---

## 🎓 Customer Onboarding Workflow

### Workflow 2: Trial Signup → First Payroll Run
**Owner**: Customer Success PM in Paperclip  
**Goal**: Customer adds first employee + runs first payroll within 48 hours

**Steps**:

1. **Welcome Sequence Task** (day 0)
   - Title: "Onboard [Company] — Day 1"
   - Email (Composio):
     ```
     Subject: Welcome to HRMS, [Name]!
     
     In the next 48 hours, do 3 things:
     1. Add your first employee (takes 5 min)
     2. Set tax settings for [State] (takes 2 min)
     3. Run a test payroll (takes 5 min)
     
     That's it! Then you'll see how easy HRMS is.
     
     Stuck? Video walkthrough: [link]
     Or reply to this email for help.
     ```
   - Subtasks:
     - [ ] Send welcome email
     - [ ] Log in HRMS to confirm account works
     - [ ] Set up Slack notification for this customer (Composio slack_subscribe)

2. **First Employee Task** (day 1)
   - Title: "Activate: [Company] — add first employee"
   - Context: "[Contact] hasn't added any employees yet. Engagement risk."
   - Trigger: If customer hasn't added employee by 24h, alert CS
   - Actions:
     - [ ] Send email: "Add your first employee now" + link to video
     - [ ] Slack message to [Contact]: "Need help adding your team?"
     - [ ] Offer: "30-min setup call with our expert"
   - Success: Employee added to system

3. **Tax Setup Task** (day 1-2)
   - Title: "Config: [Company] — set tax state"
   - Context: "Must set [State] tax settings before first payroll"
   - Subtasks:
     - [ ] Verify: Federal W-4 info (e.g., "Married, 2 allowances")
     - [ ] Verify: State W-4 info (if applicable)
     - [ ] Verify: Unemployment insurance rate (industry-specific)
   - If not completed: Send email reminder "Set your tax settings in next step"

4. **First Payroll Task** (day 2-3)
   - Title: "Execute: [Company] — first payroll run"
   - Context: "Run payroll for first employee, prove it works"
   - Subtasks:
     - [ ] Create test payroll (2 employees, 2 weeks)
     - [ ] Review calculations (should show fed/state/FICA taxes)
     - [ ] Generate pay stub (PDF download)
     - [ ] Email pay stub to employee (shows value)
   - Success criteria: Pay stub generated, taxes calculated correctly
   - CTA: "Now you know it works. Keep using it!"

5. **Success Check-In Task** (day 4)
   - Title: "Follow-up: [Company] — conversion call"
   - Context: "[Company] completed 3 onboarding steps. 80% likely to convert."
   - Call script:
     - "Hi [Name], you tried HRMS. How did it feel?"
     - "Questions about [X feature]?"
     - "Ready to keep using it? I can activate your subscription now."
   - Outcome: Convert to paid / Follow-up / Not interested
   - If convert: Create billing task (below)

---

## 💳 Billing & Subscription Workflow

### Workflow 3: Payment Setup & Renewal
**Owner**: Finance/Billing PM in Paperclip  
**Integration**: Stripe + Paperclip

**Steps**:

1. **Add Payment Task** (when customer converts)
   - Title: "Billing: [Company] — add payment method"
   - Context: "[Company] ready to subscribe at Professional tier ($499/mo)"
   - Actions:
     - [ ] Create Stripe subscription (Composio stripe_create_subscription)
     - [ ] Send receipt (Composio email_send)
     - [ ] Create calendar reminder: "First renewal in 30 days"
     - [ ] Slack: "New paying customer: [Company] at $499/mo"

2. **Monthly Renewal Task** (recurring, 1st of month)
   - Title: "Billing: [Company] — renewal processing"
   - Context: Subscription renews May 1 (every month)
   - Subtasks:
     - [ ] Verify: Payment succeeded
     - [ ] If failed: Send "Payment failed" email + retry link
     - [ ] Send monthly invoice (Composio email_send)
     - [ ] Log to CRM: Renewal successful / failed

3. **Upgrade Task** (when customer adds employees)
   - Title: "Upgrade: [Company] — from Starter to Professional"
   - Context: "[Company] now has 15 employees (was 5). Pro tier threshold is 11."
   - Trigger: Automatic when employee count crosses tier boundary
   - Actions:
     - [ ] Create Stripe subscription update (Composio stripe_update_subscription)
     - [ ] Pro-rate charges (if not month start)
     - [ ] Send email: "You've been upgraded to Professional ($499/mo). Here's what's new: [features]"
     - [ ] Log to analytics: Upgrade happened, customer expansion signal

---

## 🆘 Support & Escalation Workflow

### Workflow 4: Customer Issues → Support Ticket → Resolution
**Owner**: Customer Success PM in Paperclip  
**Integration**: Slack + Email + Paperclip

**Steps**:

1. **Support Ticket Creation** (when customer emails)
   - Title: "Support: [Company] — [issue name]"
   - Context: "[Contact] says 'Tax calculation looks wrong for employee X'"
   - Subtasks:
     - [ ] Reproduce issue (add test employee, run payroll)
     - [ ] Identify root cause (calculation bug, data entry error, etc)
     - [ ] Provide solution (manual fix + explanation, or code fix)
     - [ ] Verify fix works
     - [ ] Follow-up: "Is this resolved?"

2. **Bug Report Task** (if engineering required)
   - Title: "Bug: Tax calculation showing -$20 for FICA"
   - Context: "[Company] found edge case. Affects other customers potentially."
   - Subtasks:
     - [ ] File GitHub issue (Composio github_create_issue)
     - [ ] Assign to engineering
     - [ ] Set priority (P0: blocking customers / P1: important / P2: nice to have)
     - [ ] Update customer: "We found the bug. Fix coming in 2 days."

3. **Escalation Task** (if urgent)
   - Title: "URGENT: [Company] — can't run payroll"
   - Context: "[Company] has 500 employees due to pay today. System down."
   - Trigger: Slack alert, page on-call engineer
   - Actions:
     - [ ] Jump into Zoom call with customer
     - [ ] Troubleshoot / provide workaround
     - [ ] Keep status updated in Slack
     - [ ] Post-mortem after resolved (why did it happen?)

---

## 📊 Metrics Tracking Workflow

### Workflow 5: Weekly Metrics Review
**Owner**: CFO agent in Paperclip  
**Automation**: Daily collection, weekly analysis

**Steps**:

1. **Daily Metrics Collection** (automated)
   - Trigger: Every day at 2 AM UTC
   - Composio automation:
     - Pull from Supabase: trial signups, trial conversions, paid customers
     - Pull from Stripe: MRR, churn, upgrades
     - Pull from HRMS app: active users, payroll runs, tax filings
   - Store in Paperclip dashboard

2. **Weekly Metrics Review Task** (every Monday)
   - Title: "Metrics Review: Week of [Date]"
   - Context: Sales funnels, churn analysis, opportunity identification
   - Table:
     ```
     | Metric | Target | Actual | Status |
     |--------|--------|--------|--------|
     | Trial signups | 5 | 3 | 🟡 Below |
     | Trial-to-paid conversion | 30% | 40% | ✅ Beating |
     | MRR | $2,000 | $1,800 | 🟡 Below |
     | Churn (monthly) | <5% | 2% | ✅ Good |
     | Customer NRR | >100% | 105% | ✅ Good |
     ```
   - Subtasks:
     - [ ] Analyze: What drove low trial signups? (sales effort down?)
     - [ ] Identify: Which segment churned? (Starter tier customers?)
     - [ ] Plan: Actions to improve (increase outreach? improve onboarding?)
   - Outcomes:
     - Red (missing >20% of target): Emergency all-hands to fix
     - Yellow (missing 10-20%): Adjust tactics, report to CEO
     - Green (on track): Keep doing what works

---

## 🎯 Workflow Integration with Composio

### Critical Composio Commands Used

| Command | Workflow | Purpose |
|---------|----------|---------|
| `email_send` | All | Send emails to customers |
| `slack_message` | All | Alert team, track progress |
| `calendar_create` | Sales, Onboarding | Schedule calls/reminders |
| `openvolo_search` | Sales | Pull leads from OpenVolo |
| `stripe_create_subscription` | Billing | Create paid subscriptions |
| `stripe_update_subscription` | Billing | Upgrade/downgrade tiers |
| `github_create_issue` | Support | File bugs for engineering |
| `supabase_query` | Metrics | Pull daily metrics |
| `slack_subscribe` | Onboarding | Monitor customer activity |

---

## 📋 Paperclip Project Structure

### Company: Worldwidebro Holdings
```
├── Projects
│   └── HRMS-SaaS
│       ├── Phase: Sales & Acquisition
│       │   ├── [TASK] Blocker 1: CPA Review
│       │   ├── [TASK] Discovery Call #1 (Mon)
│       │   ├── [TASK] Discovery Call #2 (Tue)
│       │   ├── [TASK] Demo: [Company]
│       │   ├── [TASK] Trial Signup: [Company]
│       │   └── [TASK] Convert to Paid: [Company]
│       │
│       ├── Phase: Onboarding
│       │   ├── [TASK] Welcome Email: [Company]
│       │   ├── [TASK] Add First Employee: [Company]
│       │   ├── [TASK] Set Tax Config: [Company]
│       │   ├── [TASK] Run First Payroll: [Company]
│       │   └── [TASK] Conversion Call: [Company]
│       │
│       ├── Phase: Support & Operations
│       │   ├── [TASK] Support: Tax issue [Company]
│       │   ├── [TASK] Bug: FICA calculation
│       │   ├── [TASK] Metrics Review (weekly)
│       │   └── [TASK] Churn prevention [Company]
│       │
│       └── Phase: Development
│           ├── [TASK] CPA Review Blocker
│           ├── [TASK] PMF Validation (4 calls)
│           ├── [TASK] Code: Database migration
│           ├── [TASK] Code: Payroll calculation
│           ├── [TASK] Code: Stripe integration
│           └── [TASK] Code: Onboarding flow
```

### Agents/Roles
- **CEO Agent**: Reviews weekly metrics, makes capital allocation decisions
- **Sales PM Agent**: Manages lead discovery, demo scheduling, trial signup
- **Customer Success PM Agent**: Runs onboarding, handles support, tracks retention
- **Finance PM Agent**: Manages billing, subscription lifecycle, revenue tracking
- **Engineering PM Agent**: Manages bugs, code deployment, performance monitoring

---

## ⚡ Example: One Customer Journey in Paperclip

**May 12, 2026 — New Lead**
- Composio pulls 20 leads from OpenVolo
- Lead: BuildCo Contracting, 45 employees, CA, Finance Director: John Smith
- Create Task: "Call John — BuildCo (45 emp, construction)"

**May 13 — Discovery Call**
- Sales PM calls John: "How's payroll handled now?"
- John: "Excel + accountant, costs $500/month, takes 8 hours/month"
- Sales PM: "We could cut that to 1 hour. Want to try?"
- John: "Sure, free trial?"
- Task outcome: INTERESTED → Move to demo

**May 14 — Demo Scheduled**
- Create Task: "Demo: BuildCo — 2pm PT"
- Composio sends Calendly link
- John confirms

**May 14 2pm — Demo**
- Sales PM shows: Employee directory → Payroll run → Pay stub generation
- John sees: taxes calculated, compliance report generated
- Sales PM: "Can BuildCo start free trial?"
- John: "Yes, let's do it."

**May 14 5pm — Trial Activated**
- Create Task: "Trial: BuildCo — activate account"
- Composio: Create account, send credentials, schedule "Day 3 check-in"
- Slack: "#sales: BuildCo on trial!"

**May 14-15 — Onboarding**
- Create Task: "Onboard: BuildCo — Day 1"
- Composio sends: "Add your first employee + run payroll in 48h"
- John adds: 3 employees, runs sample payroll
- Sees: Taxes calculated, pay stubs generated
- John impressed: "This works!"

**May 25 — Trial Ending**
- Create Task: "Convert: BuildCo — trial ends tomorrow"
- Composio sends: "Keep using HRMS, activate subscription?"
- John clicks link, adds Stripe card
- Subscription: Professional tier ($499/mo)
- Slack: "#finance: BuildCo paid! $499/mo → $5.988K ARR"

**May 28 — First Renewal**
- Recurring Task: "Billing: BuildCo — renewal processing"
- Composio charges Stripe, sends invoice
- Task complete

**June 4 — Upgrade**
- John hires 5 more employees (now 50 total)
- Automatic Task: "Upgrade: BuildCo → Enterprise ($999/mo)"
- Composio upgrades Stripe subscription, pro-rates charge
- Slack: "#finance: BuildCo upgraded! MRR increased $500"

---

## 🎯 Success Metrics from Paperclip

By end of June, you should see in Paperclip:

- **Sales Phase**: 50 discovery tasks created, 40 scheduled demos, 15 trials activated
- **Onboarding Phase**: 10 customers completed first payroll, 8 converted to paid
- **Billing Phase**: 8 active subscriptions, $3.2K MRR, 0 refunds/cancellations
- **Support Phase**: 5 support tickets resolved, 0 critical bugs, 95%+ satisfaction
- **Metrics Phase**: 40% trial-to-paid conversion rate, <2% monthly churn, 110% NRR

Each task traces the entire customer journey, and Paperclip becomes your real-time operations center for HRMS revenue growth.

