# CON-001 Automation Deployment Plan

## Templates to Adapt (5 core workflows)

### 1. LEAD INTAKE (Gmail → Supabase)
**Template:** Gmail_and_Email_Automation / Auto-label incoming Gmail messages
**Adapt for:** Construction inquiry emails
**Output:** Create lead in Supabase venture_leads table
**Agency Agent:** Classifier (rank by complexity/budget)

### 2. LEAD CLASSIFICATION (AI-powered)
**Template:** OpenAI_and_LLMs / [AI classification]
**Adapt for:** Extract project type, budget, timeline from email
**Output:** Score and tag in CRM
**Agency Agent:** Classifier → route to PM or sales

### 3. PROPOSAL GENERATION (OpenAI + PDF)
**Template:** PDF_and_Document_Processing / [template generation]
**Adapt for:** Auto-generate electrical scope + pricing proposal
**Output:** PDF email to customer
**Agency Agent:** Curator (generate summary + next steps)

### 4. PAYMENT PROCESSING (Stripe webhook)
**Template:** Other_Integrations_and_Use_Cases / [payment automation]
**Adapt for:** Invoice sent → Stripe link → payment captured → status update
**Output:** Update Supabase venture_projects.status → "paid"
**Agency Agent:** Monitor (detect payment delays)

### 5. TEAM NOTIFICATION (Slack + Notion)
**Template:** Slack / [notification templates]
**Adapt for:** Daily standup (new leads, completed projects, revenue)
**Output:** Slack message + Notion database update
**Agency Agent:** Briefer (generate summary)

## Implementation Order
1. Lead intake (Gmail → classify → Supabase)
2. Proposal generation (OpenAI + PDF email)
3. Payment processing (Stripe webhook → status)
4. Team notifications (Slack daily briefing)
5. Exception monitoring (Monitor anomalies)

## Deployment Target
**N8n:** Render (Docker, $7-15/mo) or Railway ($5-20/mo)
**N8n is NOT on Vercel** — Vercel is for frontend/API only. N8n needs a full Node runtime.

**CON-001 backend:** Already on Vercel (if applicable), this is separate.

## Setup Checklist
- [ ] Clone awesome-n8n-templates
- [ ] Extract 5 template JSONs
- [ ] Adapt for CON-001 (Supabase credentials, Stripe key, OpenAI key, Slack webhook)
- [ ] Deploy n8n to Render
- [ ] Import workflows into n8n
- [ ] Test end-to-end (form → lead → proposal → payment → notification)
- [ ] Wire agency-agents into decision nodes

## Time Estimate
- Template adaptation: 3-4 hours
- N8n deployment: 30 min
- Testing: 1-2 hours
- **Total: ~1 day**
