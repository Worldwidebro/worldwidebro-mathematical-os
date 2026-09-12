[[STARTHERE]] | [[REALITY]] | [[00-CONSTITUTION/SECTOR-TAXONOMY-MASTER|ICP Registry]] | [[INDEX]]

# Sector ICP Contact Registry — Build Plan
**Start Date**: 2026-09-08  
**Target Completion**: 2026-09-19 (2 weeks)  
**Authority**: CP-006 (Growth & Sales) + CP-027 (Infrastructure)

---

## Overview

Build a centralized, sector-organized ICP contact registry to enable data-driven outreach campaigns across all 35 sectors. Wire it to ClickUp for daily task synchronization.

### Current State
- ✅ 35 sectors defined (SEC-001 to SEC-035)
- ✅ ICP definition in place (CAMPAIGNS/ICP.md)
- ✅ Venture-level contact data (RE-001, LT-005, CON-001)
- ✅ ClickUp integration in LT-005 and OPS-001
- ❌ Centralized sector contact registry (35 sectors × N contacts)
- ❌ Unified contact database by sector

### Target State
- 35 sector contact YAML files (SEC-001.yaml through SEC-035.yaml)
- Centralized ICP qualification scoring
- ClickUp sync for daily prospect management
- Lead scoring + prioritization
- Campaign tracking per sector

---

## Phase 1: Registry Structure (2 hours)

### Task 1.1: Create Directory & Schema
```bash
mkdir -p _REGISTRIES/CANONICAL/SECTOR-CONTACTS/
# Schema created: SECTOR-ICP-CONTACTS-SCHEMA.yaml
```

**Deliverables:**
- ✅ SECTOR-ICP-CONTACTS-SCHEMA.yaml (complete)
- [ ] SECTOR-ICP-MAPPING.yaml (sector→ICP classification)
- [ ] ICP-CONTACT-INDEX.yaml (global contact index)

### Task 1.2: Create Sector Contact Templates
Generate starter YAML files for each sector:
```
SEC-001-beauty-wellness.yaml
SEC-002-construction-infrastructure.yaml
... (repeat for all 35)
SEC-035-[final].yaml
```

Each file contains:
- Sector metadata
- Empty contacts array
- ICP qualification rules
- ClickUp mapping

**Template:**
```yaml
---
sector_code: "SEC-001"
sector_name: "Beauty & Wellness"
icp_definition: "CAM-001"
contacts: []  # To be populated in Phase 2
last_updated: 2026-09-08
contact_count: 0
qualified_count: 0
```

---

## Phase 2: Contact Discovery (8 hours)

### Task 2.1: LinkedIn Research (4 hours)
For each sector:
1. Search LinkedIn for companies matching sector NAICS codes
2. Find hiring managers/founders/CTOs/VPs
3. Extract: name, title, company, email (if public)
4. Record LinkedIn URL

**Tools:**
- LinkedIn Sales Navigator (if available)
- Crunchbase API
- G2 reviews + company URLs

**Target:** 10-20 contacts per sector (350-700 total)

### Task 2.2: Data Enrichment (4 hours)
For each contact found:
1. Validate email address
2. Enrich with company data (funding, size, revenue)
3. Calculate ICP score based on criteria
4. Assign lead priority (hot/warm/cold)

**Enrichment Services:**
- Crunchbase (funding, headcount, NAICS)
- Hunter/RocketReach (email validation)
- OpenDoor (company financials)

---

## Phase 3: ICP Scoring & Qualification (4 hours)

### Task 3.1: Build Scoring Logic
```python
def calculate_icp_score(contact):
    score = 0
    
    # Team size match (25 points)
    if 10 <= contact.eng_team_size <= 60:
        score += 25
    
    # API spend proxy (25 points)
    if contact.funding_raised >= 2_000_000:  # Likely spending >$5K/mo
        score += 25
    
    # Funding stage match (20 points)
    if contact.funding_status in ["Seed", "Series A", "Series B"]:
        score += 20
    
    # Decision speed proxy (20 points)
    if contact.company_size <= 150:  # Faster decisions
        score += 20
    
    # Tool adoption (10 points) - requires verification
    if tool_adoption_verified(contact):
        score += 10
    
    return score  # 0-100

icp_qualified = score >= 70
```

### Task 3.2: Apply Scoring to All Contacts
Run enrichment script:
```bash
python scripts/score-all-sector-contacts.py
```

Outputs:
- ICP scores calculated for all 350-700 contacts
- Qualified contacts flagged (score >= 70)
- Lead priority assigned (hot/warm/cold based on score)
- Per-sector summary statistics

---

## Phase 4: ClickUp Integration (4 hours)

### Task 4.1: ClickUp Workspace Setup
**Configuration Required:**

```yaml
ClickUp Workspace: "Worldwidebro - Company Brain"

Folder Structure:
  Sales Ops/
    ├── Sector Campaigns/
    │   ├── SEC-001 Prospects  (list)
    │   ├── SEC-002 Prospects  (list)
    │   └── ... (repeat for all 35)
    │
    └── Campaign Master/ (templates)
        ├── Campaign Template
        └── Lead Status Template

Custom Fields (per list):
  - Contact Name (text)
  - Company (text)
  - Email (email)
  - Phone (phone)
  - LinkedIn URL (url)
  - ICP Score (number, 0-100)
  - Lead Priority (select: Hot / Warm / Cold)
  - Engagement Status (select: Uncontacted / Contacted / Qualified / etc)
  - Next Action (task)
  - Last Contact Date (date)
  - Campaign Assignment (select, multi)
```

### Task 4.2: Sync Script
**Create:** `scripts/sync-sector-contacts-clickup.py`

```python
#!/usr/bin/env python3
"""
Sync SECTOR-CONTACTS YAML files to ClickUp.
Runs daily via webhook or cron.
"""

def sync_contacts():
    # 1. Read all SECTOR-CONTACTS/*.yaml files
    # 2. Filter for qualified contacts (ICP >= 70)
    # 3. Create ClickUp tasks for uncontacted leads
    # 4. Update engagement status in ClickUp
    # 5. Log sync results

if __name__ == "__main__":
    sync_contacts()
```

**Integration:**
```yaml
Webhook Trigger: Daily at 9 AM
Frequency: Manual (on-demand) + Daily
Success Criteria: >95% sync rate, <5 min execution
```

### Task 4.3: Verify Existing ClickUp Connections
**Check each venture:**
- [ ] LT-005: Verify ClickUp API token + workspace ID
- [ ] OPS-001: Verify ClickUp API token + workspace ID
- [ ] CON-001: Verify CLICKUP_TASKS.csv import path
- [ ] LT-011: Set up ClickUp integration (if needed)
- [ ] RE-001: Set up ClickUp integration (if needed)

**Retrieve from Vercel:**
```bash
vercel env pull  # Get CLICKUP_API_TOKEN, CLICKUP_WORKSPACE_ID
```

---

## Phase 5: Campaign Integration (Ongoing)

### Task 5.1: Link to Outreach Campaigns
For each sector:
1. Create campaign in CAMPAIGNS/
2. Define target ICP (hot leads only initially)
3. Set sequence (email→follow-up→call)
4. Assign to ClickUp task

**Example Campaign:**
```yaml
Campaign: CAM-SEC-014-HR-STAFFING
Sector: SEC-014 (HR & Staffing)
Target: Hot leads (score >= 85)
Sequence:
  - Day 1: Intro email
  - Day 3: LinkedIn message
  - Day 5: Follow-up email
  - Day 8: Phone outreach
```

### Task 5.2: Lead Scoring Refinement
As campaigns run:
1. Track response rates by ICP score band
2. Adjust scoring weights based on actual conversions
3. Update lead priority model
4. Add tool adoption verification step

---

## Detailed Timeline

| Week | Phase | Deliverables | Owner |
|------|-------|---|---|
| **Week 1 (Sep 8-12)** | 1 | Directory + 35 templates | Claude Code |
| | 2 | LinkedIn research (rounds 1-2) | Manual + scripts |
| **Week 2 (Sep 13-19)** | 2 | Complete contact enrichment | Enrichment service |
| | 3 | ICP scoring + qualification | Python script |
| | 4 | ClickUp workspace + sync | API integration |
| | 5 | Campaign linking + go-live | Campaign ops |

---

## Success Metrics

| Metric | Target | Current | Owner |
|--------|--------|---------|-------|
| Sectors with contacts | 35/35 | 0/35 | By Sep 12 |
| Total contacts discovered | 350+ | 0 | By Sep 15 |
| Contacts qualified (ICP≥70) | 70+ | 0 | By Sep 16 |
| ClickUp sync working | 100% | N/A | By Sep 18 |
| Campaigns deployed | 10+ | 0 | By Sep 19 |

---

## Resource Requirements

### Tools Needed
- ✅ ClickUp API (already in Vercel)
- [ ] Crunchbase API key (for enrichment)
- [ ] Hunter or RocketReach API (for email validation)
- [ ] LinkedIn Sales Navigator (optional)

### Scripts to Create
- [ ] `generate-sector-contact-templates.py`
- [ ] `discover-linkedin-contacts.py`
- [ ] `enrich-contacts-crunchbase.py`
- [ ] `score-icp-contacts.py`
- [ ] `sync-sector-contacts-clickup.py`

### Personnel
- 1 person: LinkedIn research (8 hours)
- 1 person: Script development (12 hours)
- 1 person: ClickUp setup + testing (4 hours)

---

## Implementation Checklist

### Phase 1: Structure ✅ In Progress
- [ ] Directory created: `_REGISTRIES/CANONICAL/SECTOR-CONTACTS/`
- [ ] Schema file: `SECTOR-ICP-CONTACTS-SCHEMA.yaml` (✅ Done)
- [ ] Generate 35 empty YAML files (SEC-001 through SEC-035)
- [ ] Create ICP-CONTACT-INDEX.yaml template

### Phase 2: Discovery
- [ ] LinkedIn research script created
- [ ] Crunchbase integration tested
- [ ] Hunter/RocketReach API validated
- [ ] 10-20 contacts per sector (350+ total)
- [ ] Contact data imported into YAML files

### Phase 3: Scoring
- [ ] ICP scoring algorithm built
- [ ] Scoring applied to all contacts
- [ ] Lead priority assigned
- [ ] Per-sector summary statistics

### Phase 4: ClickUp
- [ ] Workspace folders created (35 × "Sector Prospects")
- [ ] Custom fields configured
- [ ] ClickUp API token verified (from Vercel env)
- [ ] Sync script created and tested
- [ ] Daily sync scheduled

### Phase 5: Campaigns
- [ ] 10+ pilot campaigns created
- [ ] Campaigns linked to sector contacts
- [ ] Outreach sequences defined
- [ ] Performance tracking enabled

---

## ClickUp Connection Status

### Currently Connected Ventures
| Venture | ClickUp Status | Integration Type | Last Sync |
|---------|---|---|---|
| LT-005 | ✅ LIVE | API integration | 2026-09-05 |
| OPS-001 | ✅ LIVE | API integration | 2026-09-05 |
| CON-001 | ✅ PARTIAL | CSV import | 2026-09-03 |
| LT-011 | ❌ NOT CONNECTED | Needs setup | N/A |
| RE-001 | ❌ NOT CONNECTED | Needs setup | N/A |

### To Enable Full Connectivity
```bash
# 1. Get ClickUp API token from Vercel
vercel env pull

# 2. Test each venture's ClickUp workspace
python scripts/test-clickup-connection.py --venture lt-011
python scripts/test-clickup-connection.py --venture re-001

# 3. Create workspace for sector contacts
python scripts/setup-clickup-sector-workspace.py
```

---

## Next Steps (Today)

1. ✅ Create registry schema (DONE)
2. [ ] Generate 35 empty YAML templates
3. [ ] Set up ClickUp workspace folders
4. [ ] Create contact discovery scripts
5. [ ] Start Phase 2 LinkedIn research

---

**Owner**: Growth & Sales Strategy (CP-006)  
**Contact**: Sales Operations Lead  
**Questions**: See CAMPAIGNS/ICP.md for ICP definition
