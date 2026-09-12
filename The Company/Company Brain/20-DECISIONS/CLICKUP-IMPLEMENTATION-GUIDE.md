[[STARTHERE]] | [[20-DECISIONS/README|Decisions Index]] | [[REALITY]]

# ClickUp Implementation Guide — CSV → Tasks (Sep 9-10)

**Status:** Correlation map identified ✅ | Script ready ✅ | **Ready to deploy** ⏳

---

## 📊 VENTURE ↔ CLICKUP CORRELATION MATRIX

This is the **authoritative mapping** that connects your 5 ventures to their ClickUp locations.

| Venture | Name | Workspace | Folder ID | Folder Name | Control Planes | Prospects |
|---------|------|-----------|-----------|-------------|---|---|
| **OPS-001** | CareerOps Staffing | Antwuan Johns (9013677375) | 1000210000000685 | Staffing Operations | CP-023, CP-025, CP-026 | 48 |
| **CON-001** | ACE Construction | Antwuan Johns (9013677375) | 901318114591 | 🏗️ Construction | CP-026, CP-012 | 48 |
| **LT-005** | HealthRoute Medical | Medical Courier (90141555791) | 901411978075 | 01. Lead Gen & Outreach | CP-023, CP-026, CP-020 | 30 |
| **LT-011** | CarrierDispatch TMS | Antwuan Johns (9013677375) | 901317788910 | 🚚 Logistics & Transport | CP-026, CP-023 | 25 |
| **RE-001** | WorldwideBro RE | Antwuan Johns (9013677375) | 901318114592 | 🏠 Real Estate | CP-001, CP-020, CP-023 | 15 |
| **TOTAL** | — | — | — | — | — | **166** |

---

## 🔗 WHY THESE ALIASES?

Each mapping respects **existing ClickUp structure**:

- **OPS-001 → Staffing Operations** (SEC-014): Folder already exists for HR/People ops (CP-025 People)
- **CON-001 → Construction** (SEC-002): Dedicated sector folder in primary workspace
- **LT-005 → Medical Courier Workspace**: Already live with 33 folders, Lead Gen folder exists
- **LT-011 → Logistics & Transport** (SEC-017): Shared sector folder with LT-005 (different folder, same sector)
- **RE-001 → Real Estate** (SEC-020): Dedicated sector folder, can tie into Phase 1 income targets

---

## 🚀 THREE STEPS TO DEPLOY

### Step 1: Verify CLICKUP_API_TOKEN

```bash
# Check if token is set
echo $CLICKUP_API_TOKEN

# If empty, get token from:
# 1. ClickUp workspace settings → API
# 2. Create a Personal API token
# 3. Set it:
export CLICKUP_API_TOKEN='pk_...'
```

### Step 2: Preview What Will Be Created

```bash
cd ~/Documents/The\ Company/Company\ Brain

python3 scripts/csv_to_clickup_converter.py --list-only
```

**Output shows:**
- 5 new lists (one per venture)
- 166 total tasks
- Folder locations
- Ready to deploy ✅

### Step 3: Deploy to ClickUp (One Command)

```bash
python3 scripts/csv_to_clickup_converter.py --create
```

**What happens:**
1. Reads all 5 CSVs (48+48+30+25+15 = 166 prospects)
2. Creates a new list per venture (or finds existing)
3. Creates one task per prospect
4. Sets custom fields:
   - Pipeline Stage: `Prospect`
   - Deal Value: $2,500 (OPS-001), $299 (CON-001), etc.
   - Pain Signal: Extracted from CSV
   - Venture: OPS-001 / CON-001 / etc.
   - Call Outcome: `Not Called`
5. Due date: Sep 11 (tomorrow)
6. Priority: High
7. Description: Company name, contact, phone, pain signal

---

## 📋 WHAT EACH TASK LOOKS LIKE (After Deploy)

**Title:** "Call Bradley Personnel — Temp agency markup 40-60%"

**Description:**
```
Prospect: Bradley Personnel
Contact: John Smith
Phone: (919) 555-0100
Pain: Temp agency markup 40-60%
Venture: OPS-001
```

**Custom Fields:**
- Pipeline Stage: `Prospect` (drag to Called → Interested → Proposal → Closed)
- Deal Value: `$2,500`
- Pain Point: `Temp agency markup 40-60%`
- Venture: `OPS-001`
- Call Outcome: `Not Called` → `Connected` / `Interested` / etc. (you fill after call)
- Call Date: Empty (filled after call)

**Due Date:** Sep 11 (tomorrow)  
**Priority:** High  
**Folder:** Staffing Operations (mapped to CP-023 Sales)

---

## 🎯 AFTER DEPLOYMENT: YOUR WORKFLOW

### Sep 11 Morning (Start Calling)

1. **Open ClickUp** → Go to your venture folder
2. **See your list**: "Sep 11-14 Cold Calls (OPS-001)" with 48 tasks
3. **Kanban board** shows 4 columns: `Prospect | Called | Interested | Proposal | Closed`
4. **Pick first task**, open it, click phone number
5. **Make call** (use script from task description or link)
6. **After call**, update:
   - Pipeline Stage: Move to `Called`
   - Call Outcome: `Connected` / `Voicemail` / `Declined` / `Interested`
   - Call Date: Today
   - If interested: Add follow-up date

### Dashboard Views (Auto-Generated)

**View 1: Daily Call List**
- Shows: 50 tasks due today
- Sorted by: Best Time to Call
- Columns: Company | Phone | Pain Signal | Script Link

**View 2: Pipeline Board (Kanban)**
- Columns: Prospect (48) | Called | Interested | Proposal | Closed
- Drag task as you progress
- See revenue value per card ($2,500 OPS-001, $299 CON-001, etc.)

**View 3: Metrics Dashboard**
- Calls Made: 0 / 50 (updates as you log)
- Connected Rate: 0%
- Interested Rate: 0%
- Revenue Projected: $0 (updates as you move to Interested)
- Revenue Closed: $0 (updates as you move to Closed)

---

## 🔄 SYNC INTEGRATION (Automatic After Deployment)

Once tasks are created in ClickUp, these automations kick in:

```
ClickUp Task Created
    ↓
ClickUp → Supabase (webhook)
    ├─ clickup_tasks table
    ├─ deal_leads table
    └─ deal_pipeline table
    ↓
ClickUp → Neo4j (webhook)
    ├─ CREATE :Task node
    ├─ CREATE relationships (Task → Prospect → Venture)
    └─ UPDATE pipeline stage
    ↓
Growth OS Dashboard (real-time)
    ├─ Calls Made: Updated live
    ├─ Revenue Projected: Updated live
    ├─ Revenue Closed: Updated live
    └─ Pipeline by venture: Updated live
```

**Result:** Every task you update in ClickUp automatically reflects in:
- Growth OS dashboard (localhost:3030)
- Neo4j knowledge graph
- Supabase database (for reporting)

---

## 🛠️ CUSTOM FIELD REFERENCE

Each task has these fields. Update them as you progress.

| Field | Type | Options | Notes |
|-------|------|---------|-------|
| Pipeline Stage | Dropdown | Prospect → Called → Interested → Proposal → Closed | Drag card to update |
| Deal Value | Currency | $299-$25,000 | Venture-specific, read-only |
| Pain Point | Text | [extracted from CSV] | Read-only reference |
| Venture | Link | OPS-001 / CON-001 / LT-005 / LT-011 / RE-001 | Links to venture folder |
| Call Outcome | Dropdown | Not Called / Connected / Voicemail / Interested / Objection / Declined | Update after call |
| Call Date | Date | (empty) | Fill after call |
| Follow-up Date | Date | (empty) | If interested, set for Sep 12 or later |

---

## ⚠️ EDGE CASES & TROUBLESHOOTING

### "API Error 401: Unauthorized"
→ `CLICKUP_API_TOKEN` is wrong or expired
→ Get new token from ClickUp workspace settings
→ Re-run script with correct token

### "API Error 404: Folder not found"
→ Folder ID in config is wrong
→ Check ClickUp folder → Settings → Copy folder ID
→ Update config and re-run

### "No new list was created, tasks went to existing list"
→ Script found existing list with same name
→ This is OK — tasks appended to existing list
→ Check ClickUp folder to verify

### "Tasks created but custom fields are empty"
→ ClickUp custom field IDs in script don't match your workspace
→ Get field IDs from ClickUp API → workspace → custom fields
→ Update script custom_fields section and re-run

---

## 📈 REVENUE MATH (What Success Looks Like)

After deploying 166 tasks:

**Conservative (Sep 14):**
- 95 calls made
- 15 connected calls (15% connection rate)
- 3-4 interested prospects (20-25% of connected)
- 1-2 closed deals
- Revenue: $2,500 (OPS-001 placement) + $299 (CON-001 consultation) = **$2,799**

**Aggressive (Sep 14):**
- 95 calls made
- 25 connected calls (25% connection rate)
- 5-7 interested prospects (20-30% of connected)
- 2-3 closed deals
- Revenue: $2,500 + $299 + $500 (LT-011 trial) = **$3,299+**

**Target:** $5,300+ by Sep 14

---

## 🎬 NEXT ACTIONS (Right Now)

1. ✅ **Verify token**: `echo $CLICKUP_API_TOKEN`
2. ⏳ **Preview**: `python3 scripts/csv_to_clickup_converter.py --list-only`
3. ⏳ **Deploy**: `python3 scripts/csv_to_clickup_converter.py --create`
4. ⏳ **Check ClickUp**: See 5 new lists with 166 tasks
5. ⏳ **Sep 11, 9 AM**: Start calling first prospect

---

## 📞 QUICK REFERENCE: Venture Details

### OPS-001 (CareerOps Staffing)
- **Call list**: 48 staffing agencies
- **Deal value**: $2,500 per placement
- **Cycle**: 3-7 days
- **Script**: `/scripts/OPS-001-SALES-COACH.md`
- **Pain signal**: "Temp agency markup 40-60%"

### CON-001 (ACE Construction)
- **Call list**: 48 NC general contractors
- **Deal value**: $299 per consultation
- **Cycle**: 2-5 days
- **Script**: `/scripts/CON-001-SALES-COACH.md`
- **Pain signal**: "$50-100K field efficiency loss"
- **VIP**: Bob Marolf (704-563-7410) — CALL FIRST

### LT-005 (HealthRoute Medical)
- **Call list**: 30 medical facilities
- **Deal value**: $2K-5K/month (MRR)
- **Cycle**: 14-21 days
- **Script**: `/scripts/LT-005-SALES-COACH.md`
- **Pain signal**: "HIPAA compliance + route optimization"

### LT-011 (CarrierDispatch TMS)
- **Call list**: 25 freight companies
- **Deal value**: $500-2K/month (MRR)
- **Cycle**: 14-30 days
- **Script**: `/scripts/LT-011-SALES-COACH.md`
- **Pain signal**: "15-25% routing inefficiency"
- **URGENT**: Carolina Logistics — RFP window open now

### RE-001 (WorldwideBro RE)
- **Call list**: 15 accredited investor networks
- **Deal value**: $5K-25K per deal
- **Cycle**: 60-90 days (long sales cycle)
- **Script**: `/scripts/RE-001-SALES-COACH.md`
- **Pain signal**: "12-15% transparent returns"

---

**Authority:** CP-023 (Sales) + CP-026 (Operations) + CP-012 (Project Management)  
**Status:** Ready to deploy  
**Timeline:** Deploy Sep 9 evening, start calling Sep 11

