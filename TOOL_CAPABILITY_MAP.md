---
name: tool-capability-map
type: Business Goals to MCP Mapping
date: 2026-06-22
source: MCP_REGISTRY.json
---

# Tool Capability Map

**Reference:** MCP_REGISTRY.json (source of truth) | **Use this. Don't search for tools.**

**Purpose:** Map business goals → available MCPs. Check this before asking "do we have a tool for X?"

---

## Phase 1 Execution Goals

### Goal: Create Airtable Dashboard for 700 Ventures

| Need | MCP | Status | Effort | Notes |
|------|-----|--------|--------|-------|
| Create workspace | airtable | ✅ Ready | 10 min | Follow AIRTABLE_DASHBOARD_BLUEPRINT.md |
| Import venture CSV | airtable | ✅ Ready | 5 min | From ventures_16sector_classification.csv |
| Set up 5 views | airtable | ✅ Ready | 30 min | Views: Executive, OPCO, Status, Revenue, Red Flags |
| **PROCEED?** | | **✅ YES** | **45 min** | **All ready** |

---

### Goal: Create 18 Slack Channels (#opco-*)

| Need | MCP | Status | Effort |
|------|-----|--------|--------|
| create_channel | slack | ✅ Ready | 10 min |
| set_topic | slack | ✅ Ready | 5 min |
| add_members | slack | ✅ Ready | 10 min |
| **PROCEED?** | | **✅ YES** | **25 min** |

---

### Goal: Set Up ClickUp Task Management

| Need | MCP | Status | Effort |
|------|-----|--------|--------|
| create_space | clickup | ✅ Ready | 5 min |
| create_folder | clickup | ✅ Ready | 10 min |
| create_list | clickup | ✅ Ready | 5 min |
| auto_create_tasks | zapier | ✅ Ready | 30 min |
| **PROCEED?** | | **✅ YES** | **50 min** |

---

### Goal: Create Notion Documentation Hub

| Need | MCP | Status | Effort |
|------|-----|--------|--------|
| create_workspace | notion | ✅ Ready | 10 min |
| create_database | notion | ✅ Ready | 10 min |
| create_pages | notion | ✅ Ready | 30 min |
| daily_sync | zapier | ✅ Ready | 30 min |
| **PROCEED?** | | **✅ YES** | **80 min** |

---

### Goal: Populate 700 Ventures in Airtable

| Need | MCP | Status | Effort |
|------|-----|--------|--------|
| Query ventures | supabase | ✅ Ready | 5 min |
| Export CSV | native | ✅ Ready | 2 min |
| Bulk import | airtable | ✅ Ready | 10 min |
| **PROCEED?** | | **✅ YES** | **17 min** |

---

### Goal: Configure 4 Zapier Automation Zaps

| Zap | MCPs | Status | Effort |
|-----|------|--------|--------|
| Airtable → ClickUp | zapier | ✅ Ready | 15 min |
| Airtable → Notion | zapier | ✅ Ready | 15 min |
| Airtable → Slack | zapier | ✅ Ready | 15 min |
| Airtable → Gmail | zapier | ✅ Ready | 15 min |
| **PROCEED?** | | **✅ YES** | **60 min** |

---

### Goal: Schedule Weekly & Monthly Meetings

| Meeting | MCP | Status | Effort |
|---------|-----|--------|--------|
| OPCO Pres → CEO (Mon 10am) | google_calendar | ✅ Ready | 5 min |
| VM → OPCO Pres (Wed 2pm) | google_calendar | ✅ Ready | 5 min |
| Board meeting (Fri 2pm) | google_calendar | ✅ Ready | 5 min |
| Quarterly review (Last Fri) | google_calendar | ✅ Ready | 5 min |
| **PROCEED?** | | **✅ YES** | **20 min** |

---

### Goal: Send Weekly Executive Briefing (Monday 9am)

| Component | MCP | Status |
|-----------|-----|--------|
| Query data | airtable | ✅ Ready |
| Format email | gmail | ✅ Ready |
| Send email | gmail | ✅ Ready |
| Automate | zapier | ✅ Ready |
| **PROCEED?** | | **✅ YES** |

---

## All MCPs: Status Dashboard

| MCP | Priority | Status | Purpose | Last Tested |
|-----|----------|--------|---------|-------------|
| **airtable** | 🔴 CRITICAL | ✅ | Venture DB + dashboard | 2026-06-22 |
| **supabase** | 🔴 CRITICAL | ✅ | Data source + knowledge graph | 2026-06-22 |
| **clickup** | 🟠 HIGH | ✅ | Task management | 2026-06-22 |
| **notion** | 🟠 HIGH | ✅ | Documentation + binders | 2026-06-22 |
| **slack** | 🟠 HIGH | ✅ | Real-time alerts | 2026-06-22 |
| **zapier** | 🟠 HIGH | ✅ | Automation (4 zaps) | 2026-06-22 |
| **gmail** | 🟠 HIGH | ✅ | Weekly briefings | 2026-06-22 |
| **github** | 🟠 HIGH | ✅ | Code deployment | 2026-06-22 |
| **graphify** | 🟠 HIGH | ✅ | Knowledge graph | 2026-06-22 |
| **memory** | 🟠 HIGH | ✅ | Persistent context | 2026-06-22 |
| google_calendar | 🟡 MEDIUM | ✅ | Meeting scheduling | 2026-06-22 |
| stripe | 🟡 MEDIUM | ✅ | Payment capture | 2026-06-22 |
| hubspot | 🟡 MEDIUM | ✅ | CRM (Phase 2) | 2026-06-22 |

---

## How to Use

**When asked to do something:**

1. **State the goal:** "Create 18 Slack channels"
2. **Look it up here:** Find "Goal: Create 18 Slack Channels"
3. **Check status:** All ✅? **Proceed immediately**
4. **Use the MCP:** Execute Slack commands
5. **No searching. No re-discovering. Just execute.**

---

## Key Rule

**Whenever you need a tool, FIRST check this map. If it's ✅ Ready, use it. If it's not in the map, ask me to check MCP_REGISTRY.json.**

Don't rely on memory or assumptions about what we have. This map is the truth.

---

**Source:** MCP_REGISTRY.json | **Updated:** 2026-06-22
