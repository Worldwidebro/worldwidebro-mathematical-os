# VENTURE HANDOFF TEMPLATE
## How to Replicate WORLDWIDEBRO-OS Structure for New Ventures

**Purpose**: Standardize folder structure across all 712 ventures for automation, handoff, and agent execution.

**Last Updated**: 2026-06-04

---

## THE PROBLEM

Each venture needs a **consistent operating system** so that:
- Agents can find files in predictable locations
- Handoffs to teams don't require re-organization
- Workflows work across all ventures
- Supabase syncs metrics consistently
- Obsidian dashboards work uniformly

---

## THE SOLUTION: 15-Folder Venture Template

Every venture should follow this structure:

```
VENTURE_NAME/
├── 01_STRATEGY (Vision, KPIs, Milestones)
├── 02_RESEARCH (Market, Competitors, Customer)
├── 03_FINANCE (Cap Table, Budget, Forecasts)
├── 04_MARKETING (Positioning, Campaigns, Content)
├── 05_SALES (Pipeline, Proposals, Contracts, Invoices)
├── 06_OPERATIONS (Roadmap, Infrastructure, Vendors)
├── 07_PRODUCTS_SERVICES (Roadmap, Features, Pricing)
├── 08_SOPs (Onboarding, Support, QA, Handoff)
├── 09_AUTOMATION (Agent Manifests, n8n Workflows)
├── 10_EQUIPMENT (Licenses, Infrastructure, Contracts)
├── 11_LEGAL (ToS, Privacy, Agreements, IP)
├── 12_ANALYTICS (Dashboard, Metrics, Reports)
├── 13_DOCUMENTS (Deck, Case Studies, Press)
├── 14_EXIT_PREPARATION (Valuation, M&A, Due Diligence)
├── 15_PEOPLE_OPERATIONS (Team Roster, Skills, RACI)
├── VENTURE.json (Metadata: id, type, status, stage, founder)
├── metrics.json (KPIs synced daily from Supabase)
└── README.md (Venture overview)
```

---

## THE CRITICAL FILE: VENTURE.json

Every venture **must** have `VENTURE.json` in its root:

```json
{
  "id": "venture-001",
  "name": "Venture Name",
  "type": "ent|ops|con|re|med|fin",
  "status": "planned|validation|build|launch|growth|scale|exit",
  "stage": "MVP|Beta|Launch|Growth|Scale",
  "created": "2026-06-04",
  "updated": "2026-06-04",
  "founder": "Name",
  "founder_email": "email@example.com",
  "sector": "SaaS|Services|Physical",
  "vertical": "Vertical",
  "target_mrr": 5000,
  "current_mrr": 0,
  "team_size": 2,
  "funding_raised": 0,
  "next_milestone": "First 5 customers",
  "slack_channel": "#venture-name",
  "critical_path_item": "MVP by 2026-06-27",
  "linked_ventures": ["venture-002"],
  "dependencies": [
    {"system": "Supabase", "criticality": "high"},
    {"system": "Stripe", "criticality": "high"}
  ]
}
```

---

## AUTOMATION & HANDOFF CHECKLIST

Each venture's `08_SOPs/Handoff_Checklist.md` must include:

```markdown
## Venture Handoff Checklist

### WEEK 1: Knowledge Transfer
- [ ] Share all 15 folders
- [ ] Review VENTURE.json (metrics, milestones, dependencies)
- [ ] Review 09_AUTOMATION/Agent_Manifests.json (which agents run)
- [ ] Show Obsidian dashboard for this venture

### WEEK 2: Decision Authority
- [ ] Clarify approval authority (hiring, spend, pivot)
- [ ] Review 05_SALES/Pipeline.json (deal routing)
- [ ] Review 03_FINANCE/Budget.csv (spending limits)
- [ ] Setup Slack notifications

### WEEK 3: Daily Operations
- [ ] Confirm daily standups
- [ ] Setup weekly metrics sync
- [ ] Test n8n workflows
- [ ] Confirm agent assignments

### WEEK 4: Independence
- [ ] Operator updates metrics.json independently
- [ ] Workflows run without intervention
- [ ] Slack alerts configured
- [ ] Supabase permissions set
```

---

## AGENT MANIFEST (for automation)

In each venture's `09_AUTOMATION/Agent_Manifests.json`:

```json
{
  "venture_id": "venture-001",
  "agents": [
    {
      "agent_id": "venture-001-sales",
      "role": "Sales Pipeline Manager",
      "tasks": [
        "Pull leads from Supabase",
        "Update Pipeline.json daily",
        "Send Slack alerts on new deals"
      ],
      "triggers": ["daily at 9am", "on new_lead webhook"],
      "decision_authority": ["Stage advancement up to $50K ACV"],
      "escalation_to": "founder"
    },
    {
      "agent_id": "venture-001-support",
      "role": "Customer Success",
      "tasks": [
        "Monitor support requests",
        "Update customer status",
        "Generate weekly report"
      ],
      "triggers": ["on customer_message", "weekly at 5pm"],
      "decision_authority": ["Refund requests up to $200"],
      "escalation_to": "founder"
    }
  ]
}
```

---

## SUPABASE SYNC

Daily automation:
```
8:00 AM → Supabase ventures table → VENTURE.json (each venture)
8:15 AM → Supabase metrics table → metrics.json (each venture)
9:00 AM → metrics.json → Obsidian Dataview → Update dashboards
9:30 AM → Slack: "MRR: $0 → Target $5K"
```

---

## OBSIDIAN DASHBOARD (Venture View)

Each venture gets: `Obsidian/Ventures/VENTURE_NAME/Dashboard.md`

```markdown
# Venture Name Dashboard

## Status
- **Stage**: MVP
- **Next Milestone**: First 5 customers
- **Critical Path**: MVP by 2026-06-27

## KPIs (Auto-updated)
| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| MRR | $0 | $5,000 | 🔴 |
| Customers | 0 | 5 | 🔴 |

## Agent Status
- Sales Agent: ✅ Running
- Support Agent: ✅ Running

## Dependencies
- Supabase: ✅ Connected
- Stripe: ⏳ Pending
```

---

## INTAKE LAYER (Optional per Venture)

Each venture can have its own `00_INTAKE_LAYER/`:

```
VENTURE_NAME/
├── 00_INTAKE_LAYER/
│   ├── Instagram_Screenshots/
│   ├── DM_Conversations/
│   ├── Voice_Notes/
│   └── Meeting_Notes/
├── 01_STRATEGY/
...
```

Use when venture has own social accounts, investor meetings, board calls.

---

## IMPLEMENTATION ROADMAP

### Phase 1: Template Adoption (This Week)
- [ ] Create `generate_venture_folder.py` script
- [ ] Populate 08_SOPs/Handoff_Checklist.md in all ventures
- [ ] Document in each venture's README.md

### Phase 2: Automation Integration (Next Week)
- [ ] Wire Supabase → metrics.json daily sync
- [ ] Create n8n workflow for metrics aggregation
- [ ] Build Obsidian Dataview queries per venture

### Phase 3: Agent Manifest Standardization (2 Weeks)
- [ ] Define standard agent roles
- [ ] Create Agent_Manifests.json for all ventures
- [ ] Test agent execution

### Phase 4: Handoff Automation (3 Weeks)
- [ ] Build handoff workflow automation
- [ ] Test with first venture
- [ ] Document onboarding

---

## NEXT STEPS

1. **Today**: Apply template to HRMS venture (test)
2. **Tomorrow**: Create `generate_venture_folder.py` script
3. **Day 3**: Wire first Supabase → metrics.json sync
4. **Day 5**: Create Obsidian dashboards for 5 ventures
5. **Day 10**: Handoff HRMS to operator

---

**This template enables**: Scalable operations × 712 ventures + smooth handoffs + agent automation + consistent KPI tracking.

