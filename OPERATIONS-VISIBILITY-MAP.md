---
name: OPERATIONS-VISIBILITY-MAP
title: Operations Visibility Map
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# Operations Visibility Map

**Question:** "Shouldn't I see all this from my phone or local server? What's continuously updated?"

**Answer:** Three truth sources. View any, edit only one. Everything else syncs automatically.

---

## Three Data Sources (Use These)

### Source 1: ClickUp (Real-time, Mobile-Ready)
**Ground truth for:** Calls, prospects, jobs, candidates, placements  
**Access:** Desktop (clickup.com) + Mobile (app) + Web

| List Name | List ID | Data | Updated By | View |
|-----------|---------|------|-----------|------|
| Target Accounts | 1000210000002320 | Prospects + call outcomes | Call center (daily) | Real-time |
| Client Job Orders | 1000210000002235 | JO-001, JO-002, etc. | Ops manager | Real-time |
| Candidate Pipeline | 1000210000002236 | Candidates (sourced → placed) | Recruiter | Real-time |
| Placements & Billing | 1000210000002237 | Closed placements + invoices | Finance | Real-time |

**Mobile:** Download ClickUp app → log in → same data as desktop

### Source 2: Weekly Dashboard (STAFFING-AGENCY-STATUS.md)
**Ground truth for:** Weekly metrics, trends, by-sector performance  
**Updated:** Friday 4pm (manual) + auto-timestamp daily 8am  
**Access:** Phone (text editor) + Desktop (GitHub + local)

| Section | Data | Updated | Frequency |
|---------|------|---------|-----------|
| Weekly Metrics | Calls, jobs, candidates, revenue | Friday 4pm (ops mgr) | Weekly |
| By-Sector Performance | Conversion % per sector | Friday 4pm (ops mgr) | Weekly |
| Historical | Last 8 weeks trend | Friday 4pm (ops mgr) | Weekly |
| Blockers | What's slowing us down | Friday 4pm (ops mgr) | Weekly |

**Mobile:** iCloud Drive / Google Drive → open file in text editor

### Source 3: Deployment Status (VENTURES-REMOTE-ENV.md)
**Ground truth for:** Which ventures are live, env vars, blockers  
**Updated:** Auto-synced daily 8am (GitHub Actions)  
**Access:** Phone (text) + Desktop (GitHub)

| Venture | Status | Vercel URL | Updated | Blocker |
|---------|--------|-----------|---------|---------|
| CON-001 | ✅ Live | con-001-ace-construction.vercel.app | 8am daily | None |
| LT-005 | 🟡 Ready | (pending deploy) | 8am daily | Stripe keys |
| STA-001 | 🟢 Executing | (HTML forms only) | 8am daily | None |

**Mobile:** View in GitHub app or browser

---

## What Continuously Updates (No Manual Work)

### Auto-Sync: Daily 8am UTC
**System:** GitHub Actions (`.github/workflows/venture-env-sync.yml`)  
**Runs:** Automatically every day at 8am + on-demand

| File | Updates | Source | Lag |
|------|---------|--------|-----|
| VENTURES-REMOTE-ENV.md | Timestamp + status | Vercel API | Same-day |
| STAFFING-AGENCY-STATUS.md | Timestamp only | Clock | Instant |

**You don't touch these — just view them.**

### Auto-Sync: Real-time (Webhooks)
**System:** Supabase webhooks → Stripe → Zapier

| Flow | Trigger | Updates | Visible In |
|------|---------|---------|-----------|
| Client fills form | Form submit | Supabase `venture_leads` | ClickUp (if webhook active) |
| Payment received | Stripe webhook | Supabase `deal_payments` | ClickUp "Placements & Billing" |
| Job captured | Form submit | Supabase `ventures` | ClickUp "Client Job Orders" |

**You fill the form once. It appears everywhere.**

---

## ClickUp Workspace Structure

**Current:** One workspace = "Staffing Agency"  
**Workspace ID:** 9013677375  
**Space:** "STA-001"

```
Staffing Agency Workspace
└── STA-001 Space
    ├── Target Accounts List (prospects to call)
    ├── Client Job Orders List (companies with open jobs)
    ├── Candidate Pipeline List (candidates in process)
    └── Placements & Billing List (closed deals)
```

**Why one workspace?**
- Week 1: Only STA-001 is live
- Easier to see all activity (calls → jobs → placements → revenue)
- All team shares same view

**When do we separate?** (Aug 15+)
- Once LT-005 + EC-111 launch
- Each venture gets separate ClickUp space
- OR: Separate workspaces (Staffing vs Construction vs Logistics)
- Platform team tracks all ventures from Platform workspace

**Decision:** Keep one workspace for now. Migrate when 3+ ventures are active simultaneously.

---

## Files: Manual vs Auto

| File | Who Enters | When | Frequency | Visible On |
|------|-----------|------|-----------|-----------|
| WEEKLY-CALL-SHEET.md | Call center | Daily 9am-5pm | Real-time | Desktop + phone |
| ClickUp "Target Accounts" | Call center | Daily | Real-time | Phone app (best) |
| ClickUp "Client Job Orders" | Ops mgr | On conversion | Real-time | Phone app |
| ClickUp "Candidate Pipeline" | Recruiter | Daily | Real-time | Phone app |
| ClickUp "Placements & Billing" | Finance | Friday | Real-time | Phone app |
| STAFFING-AGENCY-STATUS.md | Ops mgr | Friday 4pm | Weekly | Phone text editor |
| VENTURES-REMOTE-ENV.md | GitHub Actions | 8am daily | Auto | Phone + desktop |

**Rule:**
- ✅ Enter once (ClickUp or form)
- ✅ View in multiple places (phone + desktop + dashboard)
- ❌ Don't copy-paste between systems (syncs automatically)

---

## Phone Access (Right Now, No Setup)

### ClickUp (Best for Real-time)
1. Download: ClickUp app (iOS / Android)
2. Login: Same email as desktop
3. View: All lists, search, update status
4. No lag: Real-time updates

**Use for:** Daily call logging, checking conversion funnel, spotting blockers

### Text Files (Quick Overview)
1. Sync: iCloud Drive / Google Drive / GitHub app
2. View: Any text editor
3. No lag: Updates as you pull latest

**Use for:** Weekly metrics, deployment status, blockers review

### Dashboard (Coming Aug 5)
1. Download: None needed (web-based)
2. URL: https://vex-dashboard.vercel.app
3. Install: "Add to Home Screen" (PWA)
4. Works: Online + offline (data cached)

**Use for:** Morning check-in (revenue, calls, by-sector breakdown, blockers)

---

## Nextcloud Setup (Optional, $0 Self-Hosted)

**Current state:** Files live in GitHub  
**If you want offline mobile access:**

### Install Nextcloud (Self-hosted)
```bash
# On Mac Studio (has 3TB, perfect for this)
# Or rent $5/mo instance (Hetzner, Linode)

docker run -d -v nextcloud_data:/data:Z \
  -p 8080:80 \
  -e NEXTCLOUD_ADMIN_USER=admin \
  -e NEXTCLOUD_ADMIN_PASSWORD=secure \
  nextcloud

# Access: http://localhost:8080 (or your server IP)
```

### Sync GitHub → Nextcloud (Auto)
```bash
# Use rclone or rsync
rclone sync github:Documents /mnt/nextcloud/Documents \
  --update --delete -v
```

### View on Phone
1. Download: Nextcloud app
2. Add server: URL + login
3. Sync: STAFFING-AGENCY-STATUS.md + VENTURES-REMOTE-ENV.md
4. Edit: Offline, syncs when online

**Pros:** Full offline access, no cloud dependency, complete control  
**Cons:** Hosting cost ($0-5/mo), maintenance  

**Decision:** Build ClickUp + dashboard first (simpler). Nextcloud later if needed.

---

## What Stays Out of ClickUp (Stays in Files)

These are **reference + strategy**, not **execution tasks:**

- Architecture docs (CLAUDE.md, SYSTEM-ARCHITECTURE-MAP.md)
- Playbooks (SOP templates, call scripts)
- Roadmaps (6-month plans)
- Venture specs (requirements, scope)
- Financial models (revenue projections)
- Learning (what worked, what didn't)

**Rule:** ClickUp = tasks + execution. Markdown files = reference + strategy.

---

## Mobile-First Workflow (Aug 5+)

### Morning (9am)
1. Open ClickUp app
2. "Target Accounts" → Today's call list (who to call)
3. Dashboard → This week's metrics (are we on track?)
4. Done → Start calling

### During Day (9am-5pm)
1. Call someone
2. Log in ClickUp (outcome: Interested / Not / Callback)
3. If INTERESTED → Fill client-intake.html form (2 min)
4. Done → Next call
5. (Everything else auto-syncs)

### Friday (4pm)
1. Open STAFFING-AGENCY-STATUS.md
2. Copy 4 numbers from ClickUp
3. Paste into file
4. Done → Leadership sees metrics

### Monday (9am)
1. Dashboard shows updated metrics
2. Call team briefed on priorities
3. Start Week 2

---

## Summary: Visibility by Person

**Call Center Employee:**
- Uses: ClickUp app + client-intake form
- Views: None (just execute)
- Time: 5 min/day setup (opens app, dials)

**Ops Manager:**
- Uses: ClickUp desktop + markdown file
- Views: Daily (ClickUp), Friday (fill file), Monday (review)
- Time: 30 min/week

**Leadership:**
- Views: Dashboard (daily) + STAFFING-AGENCY-STATUS.md (Friday)
- Uses: None (read-only)
- Time: 10 min/day

**Finance:**
- Views: ClickUp "Placements & Billing" + Stripe dashboard
- Uses: Log invoice amount (Friday)
- Time: 5 min/week

**DevOps:**
- Views: VENTURES-REMOTE-ENV.md (daily 8am auto)
- Uses: Deploy + configure (on-demand)
- Time: Variable (deploy: 30 min, then monitor)

---

## System Principle

> **Humans enter data once in one place. AI syncs it everywhere else.**

- Call center fills form → auto-appears in ClickUp + Supabase
- Finance enters payment → auto-appears in dashboard + spreadsheet
- Ops pulls metrics Friday → auto-publishes to leadership Monday

**No copy-pasting. No spreadsheets. No manual syncing.**

---

**Last Updated:** 2026-08-01  
**Next Update:** 2026-08-02 (auto-sync timestamp)  
**Questions?** See CLAUDE.md or ask your AI Chief of Staff
