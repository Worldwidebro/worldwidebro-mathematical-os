# HRMS — Composio AI Automation Opportunities
**Status**: Planning  
**Composio Framework**: 91 commands available  
**Target**: 3-5 AI automations in MVP, 10+ post-launch

---

## 🤖 AI Automation Opportunities (Prioritized)

### Priority 1: Auto-Generate Payroll Reports (Week 2)
**What**: When payroll run is approved, AI generates compliance docs
**Composio Commands Used**: 
- `documents_create` (GitHub) — create files
- `email_send` (Gmail) — send to accountant/lawyer for review
- `slack_message` (Slack) — notify CFO "Payroll ready for filing"

**Flow**:
1. User approves payroll run (clicks "Approve")
2. Trigger: POST /api/payroll/{id}/approve
3. Composio automation:
   - `payroll_to_w2_format(payroll_run)` → generates W-2 XML
   - `payroll_to_941_format(payroll_run)` → generates Form 941 JSON
   - `documents_create` → stores in GitHub `/payroll-docs/{company}/{year}/`
   - `email_send` → "Payroll approved, W-2s ready for filing" to company contact
   - `slack_message` → "#operations: Payroll run for [Company] approved"
4. CFO can download, review, file manually

**Effort**: 1 day (Composio routing + template)  
**Impact**: Eliminates 1 hour/payroll of manual report generation

---

### Priority 2: Tax Law Updates & Compliance Alerts (Week 3)
**What**: AI monitors tax law changes, alerts on deadline misses
**Composio Commands Used**:
- `web_search` (Brave) — monitor IRS, state tax agency updates
- `email_send` (Gmail) — send compliance alerts
- `notion_page_create` (Notion) — log compliance checklist

**Flow**:
1. Daily scheduled job: Check for tax law changes
2. Composio automation:
   - `web_search` "IRS Form 941 deadline 2026" → extracts deadline
   - Compare to company's last filing → alert if due within 7 days
   - `email_send` → "Q1 941 filing due April 30, 2026. Status: Not submitted"
   - `slack_message` → CFO with link to file
3. Company CFO sees alert, knows exactly what to do

**Effort**: 2 days (scheduler setup + search/alert logic)  
**Impact**: Zero missed compliance deadlines

---

### Priority 3: Direct Deposit Auto-Sync (Week 4, Post-MVP)
**What**: Payroll payments auto-sync to banking system
**Composio Commands Used**:
- `banking_api_create_transfer` (if available in Composio)
- Or: Export ACH file to Slack, employee downloads & uploads to bank

**Flow**:
1. User clicks "Process Payroll" on approved run
2. Composio automation:
   - Validate all employees have bank account info
   - Generate ACH file (standardized bank format)
   - Email to company: "ACH file ready. Download → upload to your bank"
   - `slack_message` → "ACH ready for [Company], 500 employees"
3. Company uploads ACH to their bank (no additional work)

**Effort**: 2 days (ACH format + bank file generation)  
**Impact**: Eliminates manual direct deposit setup

---

### Priority 4: Employee Benefits Auto-Enrollment (Week 4, Post-MVP)
**What**: New employees auto-enrolled in health/401k based on company rules
**Composio Commands Used**:
- `email_send_template` (Gmail) — automated benefits election email
- `form_create` (Google Forms via Composio) — benefits election form
- `slack_message` — notify HR when employee completes enrollment

**Flow**:
1. Employee added to company
2. Trigger: POST /api/employees (new hire)
3. Composio automation:
   - Fetch company benefits rules (health insurance, 401k, etc)
   - `email_send` to new employee: "Welcome! Complete your benefits enrollment"
   - Link to benefits election form (hosted in Pitch Kit or Typeform)
   - `slack_message` to HR: "New hire [Name] needs benefits enrollment"
4. Employee completes form online
5. Trigger: form submission → auto-record in database

**Effort**: 2 days (form integration + email templates)  
**Impact**: Zero manual benefits paperwork

---

### Priority 5: Turnover Audit & Offboarding Checklist (Week 5, Post-MVP)
**What**: When employee marked inactive, AI creates offboarding tasks
**Composio Commands Used**:
- `paperclip_task_create` (Paperclip) — queue offboarding tasks
- `email_send` (Gmail) — offboarding checklist to HR
- `slack_message` — alert HR/Finance

**Flow**:
1. HR marks employee as "inactive" (termination/resignation)
2. Trigger: PATCH /api/employees/{id} (status = inactive)
3. Composio automation:
   - `paperclip_task_create` → Queue offboarding tasks:
     - [ ] Recover equipment (laptop, badge, etc)
     - [ ] Cancel access (email, VPN, payroll system)
     - [ ] Final paycheck calculation (final payment, unused PTO)
     - [ ] COBRA letter (if eligible)
     - [ ] W-4 final payroll run
   - `email_send` to HR: "Offboarding checklist for [Employee]"
   - `slack_message` → "Employee [Name] marked inactive, offboarding tasks queued"
4. HR works through checklist, marks done when complete

**Effort**: 1 day (Paperclip task templating)  
**Impact**: Zero forgotten offboarding tasks

---

## 🔌 Composio Command Mapping

### Email Commands (Priority 1, 4, 5)
- `email_send(to, subject, body)` — send alert/reminder
- `email_send_template(to, template_id, variables)` — branded email
- `email_attach_file(email_id, file_path)` — attach payroll docs

### Document/File Commands (Priority 1, 3)
- `documents_create(repo, path, content)` — create W-2/941 files
- `file_download(url)` — fetch IRS forms
- `file_generate_pdf(html)` — convert HTML payroll reports to PDF

### Task/Workflow Commands (Priority 5)
- `paperclip_task_create(company_id, task_name, assignee, due_date)` — queue offboarding tasks
- `paperclip_task_update(task_id, status)` — mark complete
- `paperclip_task_list(filter)` — show open tasks

### Search/Knowledge Commands (Priority 2)
- `web_search(query)` — find IRS/tax updates
- `documents_search(query, repo)` — search compliance docs
- `knowledge_graph_query(query)` — query venture metrics

### Communication Commands (All priorities)
- `slack_message(channel, message)` — alert ops/finance
- `slack_thread_reply(message_ts, reply)` — ongoing conversation
- `slack_scheduled_message(channel, message, time)` — defer alerts

### Integration Commands (Future)
- `github_pr_create(repo, branch, title)` — auto-create PR for new features
- `github_issue_create(repo, title, body)` — log bugs from customer feedback
- `banking_api_transfer()` — direct ACH creation (if available in Composio)

---

## 📋 Implementation Plan

### MVP (Week 2-3)
- ✅ Priority 1: Payroll report generation
- ✅ Priority 2: Tax deadline alerts

### Phase 2 (Week 4-5, Post-MVP)
- ✅ Priority 3: Direct deposit auto-sync
- ✅ Priority 4: Benefits auto-enrollment
- ✅ Priority 5: Offboarding checklist

### Phase 3 (Month 2+)
- Quarterly compliance filing automation (AI fills out 941, state quarterly, etc)
- Payroll analytics (AI generates insights: "Payroll cost per employee increased 15% YoY")
- Vendor coordination (AI alerts when health insurance renewals due)
- Customer analytics (AI tells us: "Customers on Professional tier with 20+ employees have 5x lower churn")

---

## 🎯 Composio Command Count

**Current usage**: 5 Composio commands (out of 91 available)
- `documents_create`, `documents_search`
- `email_send`, `email_send_template`
- `slack_message`
- `web_search`
- `paperclip_task_create`

**Available for future**: 84 commands remaining
- GitHub (PR/issue creation, code review)
- Linear (bug tracking)
- Notion (documentation)
- Google Workspace (Forms, Drive, Sheets)
- Stripe (invoice management)
- And 70+ others

**Strategy**: Use 10-15 Composio commands in first 3 months, expand to 40+ by month 6

