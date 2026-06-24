---
name: tool-integration-stack
type: Systems Integration & Automation Architecture
date: 2026-06-22
purpose: Map ClickUp, Notion, Slack, Stripe, HubSpot into operating system
---

# Tool Integration Stack

## Overview

Operating system uses **Airtable as command center** but integrates with 8+ tools via **Zapier** for complete workflow automation.

**Data Flow:**
```
Ventures (Airtable)
    ↓
  Zapier (4 primary zaps)
    ├─→ ClickUp (tasks + projects)
    ├─→ Notion (documentation)
    ├─→ Slack (notifications)
    └─→ Gmail (weekly briefing)
    
Plus: Google Calendar, Clockify, Stripe, HubSpot
```

---

## Primary Integrations

### 1. Airtable ↔ ClickUp

**Zap:** "New venture → Create ClickUp task"

- **Source:** Airtable VENTURE_INVENTORY_MASTER
- **Trigger:** New venture OR status = "Operating"
- **Action:** Create ClickUp task with venture_name, owner, 90day_target
- **Frequency:** Real-time
- **Status:** ✅ Ready

**ClickUp Structure:**
```
Worldwidebro Portfolio (Space)
├── OPCO-Construction (Folder with 4-5 ventures)
├── OPCO-Staffing (Folder with 4-5 ventures)
└── ... 18 OPCOs total
```

### 2. Airtable ↔ Notion

**Zap:** "Venture updated → Sync to Notion database"

- **Source:** Airtable (revenue, status, burn)
- **Trigger:** Data updated
- **Action:** Update Notion database + regenerate dashboards
- **Frequency:** Daily sync
- **Status:** ✅ Ready

**Notion Structure:**
```
Worldwidebro Portfolio
├── Ventures Database (synced from Airtable)
├── OPCO Binders (18 copies of 18-PDF template)
├── Governance (GOVERNANCE-CHARTER.md)
└── Dashboards (Revenue, Team Health, Risk)
```

### 3. Airtable ↔ Slack

**Zaps:**
- "Status changes to Operating" → #ventures-weekly
- "Burn > Revenue" (red flag) → #worldwidebro-ops
- "Revenue target missed" → OPCO President + CEO

- **Frequency:** Real-time
- **Status:** ✅ Ready

**Channels:**
```
#worldwidebro-ops (CEO, CFO, COO)
  ├─ Daily cash balance (9am)
  ├─ Red flag alerts
  └─ Board decisions

#opco-{name} (18 channels)
  ├─ Performance updates
  ├─ Status changes
  └─ Weekly summary

#ventures-weekly (all team)
  ├─ New launches
  ├─ Revenue milestones
  └─ Team changes
```

### 4. Airtable ↔ Gmail

**Zap:** "Weekly digest → Send email to CEO, CFO, OPCO Presidents"

- **Trigger:** Monday 9am
- **Content:** Revenue overview, red flags, top performers, OPCO stats
- **Frequency:** Weekly
- **Status:** ✅ Ready

---

## Supporting Tools

### 5. Google Calendar (Scheduling)
- Weekly reviews: Monday 10am (OPCO Pres → CEO), Wednesday 2pm (VM → Pres)
- Board meeting: First Friday 2pm
- Quarterly review: Last Friday full day
- **Status:** ✅ Ready

### 6. Clockify (Time Tracking)
- Venture Managers log time by venture → feeds monthly burn rate
- **Status:** ✅ Ready (optional)

### 7. Stripe (Payments)
- Webhook → Zapier → Airtable updates revenue_ytd
- **Status:** ⏳ Config for ventures with Stripe only

### 8. HubSpot (CRM)
- Sync customer count + deal pipeline to Airtable
- **Status:** 📌 Add Phase 2 (after Sales Manager hired)

---

## Configuration Checklist (Phase 1, Week 1)

**Airtable:**
- [ ] Create workspace + import VENTURE_INVENTORY_MASTER.csv
- [ ] Set up 5 dashboard views
- [ ] Configure field definitions

**ClickUp:**
- [ ] Create Space + 18 OPCO folders
- [ ] Set up Zapier: Airtable new row → ClickUp task
- [ ] Assign Venture Managers

**Notion:**
- [ ] Create workspace + Ventures database
- [ ] Create 18 OPCO Binder page templates
- [ ] Set up daily sync Zapier zap

**Slack:**
- [ ] Create #opco-* (18 channels) + #ventures-weekly + #worldwidebro-ops
- [ ] Set up 3 alert Zaps (status, red flags, revenue miss)

**Gmail:**
- [ ] Verify Zapier integration
- [ ] Create weekly brief template
- [ ] Set Monday 9am trigger

**Google Calendar:**
- [ ] Create recurring meetings (weekly, monthly, quarterly)

---

## Cost Summary

| Tool | Cost/Month | Total |
|------|-----------|-------|
| Airtable Pro | $120 | $120 |
| ClickUp Teams | $120 | $120 |
| Notion | $120 | $120 |
| Slack Pro | $130 | $130 |
| Zapier | $200 | $200 |
| Google Workspace | $12/user × 15 | $180 |
| Stripe (2.9% + $0.30) | ~50 | $50 |
| **TOTAL** | | **~$900/mo** |

---

## Integration Testing

- [ ] Add test venture to Airtable → verify ClickUp task created (5 min)
- [ ] Update revenue in Airtable → verify Notion updated (1 hour)
- [ ] Change status to "Operating" → verify Slack alert posted (2 min)
- [ ] Monday 9am → verify email sent with correct data

---

## Tool Ownership

| Tool | Owner | Purpose |
|------|-------|---------|
| Airtable | Data Admin | Master database |
| ClickUp | Venture Managers | Task tracking |
| Notion | Data Admin | Documentation + investor deck |
| Slack | Ops team | Team communication |
| Gmail | Automation | Weekly briefing |
| Google Calendar | CEO's admin | Meeting scheduling |

---

## Success Criteria

✅ Airtable ↔ ClickUp sync working  
✅ Airtable ↔ Notion sync working  
✅ Slack alerts firing real-time  
✅ Weekly email delivered Monday 9am  
✅ All OPCO Presidents trained  
✅ All 47 priority ventures tracked across all tools

---

**Owner:** Data Admin + Ops Lead  
**Status:** Ready to configure (Week 1)
