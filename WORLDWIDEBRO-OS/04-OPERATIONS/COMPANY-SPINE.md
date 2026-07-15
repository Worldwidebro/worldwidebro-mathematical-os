---
references:
  - [[VENTURE-MASTER]]
  - [[LOOP-FRAMEWORK]]
  - [[ORB-MASTER-CONNECTOR-2026-06-11]]
---

# COMPANY SPINE — Single Structural Source of Truth

**Last fixed:** 2026-06-26
**Authority:** This file is canonical for entity structure, sector taxonomy, tool roles, and workspace folders. Slack channels, HubSpot pipelines, ClickUp spaces, and Airtable bases MUST mirror this.

---

## 1. Entity Formation (3 tiers)

```
TRUST
  └─ Worldwidebro Holdings ............ holding company / brand
       └─ Winners Circle WC LLC ....... ACTIVE operating entity (bootstrap)
            └─ 18 Sector Divisions ..... operating spine (= canonical sectors below)
                 └─ 712 Ventures ....... each files its own LLC when bankable
```

- **Current legal entity:** Winners Circle WC LLC. Rebrand to Worldwidebro Holdings DBA after $50K/mo.
- **Owner / Registered Agent:** Antwuan Johns — winnerscirclewcllc@gmail.com
- **Per-venture LLC:** Wyoming LLC + EIN + Mercury, per `PHASE-1-ENTITY-FORMATION-CHECKLIST.md`.

---

## 2. Canonical Sector Taxonomy — THE SPINE (18)

Source of truth = `VENTURES-CAPABILITIES-MAPPED.csv` **and** Neo4j (`712 IN_SECTOR` edges). These two agree exactly. Use these slugs everywhere.

| # | Sector (canonical slug) | Ventures |
|---|--------------------------|---------:|
| 1 | e-commerce | 110 |
| 2 | operations | 67 |
| 3 | technology | 61 |
| 4 | community | 50 |
| 5 | emerging | 50 |
| 6 | specialized | 50 |
| 7 | financial | 41 |
| 8 | beauty-wellness | 40 |
| 9 | education | 40 |
| 10 | food-hospitality | 35 |
| 11 | logistics-transport | 30 |
| 12 | software-technology | 30 |
| 13 | fitness-sports | 25 |
| 14 | professional-services | 25 |
| 15 | media-content | 21 |
| 16 | construction | 20 |
| 17 | education-training | 16 |
| 18 | real-estate | 1 |
| | **TOTAL** | **712** |

---

## 3. OpCo Folder Drift — FIX (crosswalk)

`03-PORTFOLIO/opcos/` uses 18 DIFFERENT names that do NOT match the data spine. Rename/realign opco folders to the canonical slugs:

| opcos/ folder (old) | → Canonical sector | Note |
|----------------------|--------------------|------|
| BEAUTY_WELLNESS | beauty-wellness | direct |
| CONSTRUCTION | construction | direct |
| EDUCATION | education (+ education-training) | merge |
| FINANCIAL | financial | direct |
| HOSPITALITY | food-hospitality | rename |
| MARKETPLACE | e-commerce | rename |
| MEDIA | media-content | rename |
| OPERATIONS | operations | direct |
| REAL_ESTATE | real-estate | direct |
| TECHNOLOGY | technology (+ software-technology) | merge |
| TRANSPORTATION | logistics-transport | rename |
| STAFFING | professional-services | remap |
| INVESTMENT | financial | merge into financial |
| RETAIL | e-commerce | merge into e-commerce |
| AGRICULTURE | specialized | no ventures yet -> park |
| ENERGY | emerging | no ventures yet -> park |
| HEALTHCARE | specialized | no ventures yet -> park |
| MANUFACTURING | specialized | no ventures yet -> park |

**Canonical sectors with NO opco folder yet (create):** community (50), emerging (50), specialized (50), fitness-sports (25).

---

## 4. Tool-Role Map (10 tools — NOT yet in the knowledge graph)

The graph models Ventures/Repos/Sectors only. These tools have NO nodes — they are the human+agent interface layer on top of the data backbone (Supabase=truth, Neo4j=graph, DuckDB=analytics, Chroma/Qdrant=semantic, Redis=cache).

| Tool | Status | Single job | Layer |
|------|--------|-----------|-------|
| **ClickUp** | live | Work execution / tasks (all ventures) | Ops |
| **HubSpot** | scopes broken | CRM — deals/contacts/pipeline | Money |
| **Notion** | live | Knowledge / SOPs / binders | Reference |
| **Airtable** | needs auth | Operational DB / intake views (syncs to Supabase) | Data front-end |
| **Slack** | live (empty) | Comms / alerts / per-sector channels | Nerve center |
| **Zapier** | live | Automation glue (connects all above) | Wiring |
| **TwentyCRM** | drop | Redundant with HubSpot | — |
| **Composio** | later | Agent tool-router (only when autonomous agents call tools) | — |
| **Zep** | later | Agent long-term memory (overlaps Chroma/Qdrant) | — |
| **Paperclip.ing** | undefined | Purpose TBD | — |

**Flow:** `Airtable/Form intake -> Zapier -> HubSpot (deal) + ClickUp (task) + Slack (alert) -> Notion (docs) -> Supabase (truth)`

---

## 5. Workspace Folder Schema (10) — status

Canonical operating workspace = `04-OPERATIONS/`. All scaffolded 2026-06-26.

| Folder | Status | Location |
|--------|--------|----------|
| executive | ✅ scaffolded | `04-OPERATIONS/executive/` — authority docs (this + Growth OS) |
| directive | ✅ scaffolded | `04-OPERATIONS/directive/` — standing system directives |
| operations | ✅ | `04-OPERATIONS/` |
| research | ✅ | `07-KNOWLEDGE/research/` |
| finance | ✅ | `09-DASHBOARDS/finance/`, `04-OPERATIONS/departments/finance/` |
| projects | ✅ scaffolded | `04-OPERATIONS/projects/` (+ `08-DATA/worldwidebro-vault/Projects/`) |
| clients | ✅ scaffolded | `04-OPERATIONS/clients/` — mirrors HubSpot CRM |
| content | ✅ scaffolded | `04-OPERATIONS/content/` — Marketing OS assets |
| queue | ✅ scaffolded | `04-OPERATIONS/queue/` — lead/task intake |
| generated | ✅ scaffolded | `04-OPERATIONS/generated/` — AI outputs pending review |

See [[VENTURE-GROWTH-OS]] for how content/queue/generated/clients feed the funnel.

---

## 6. Open fixes (require user action)

1. **Airtable** — click auth URL to connect (Zapier MCP).
2. **HubSpot** — re-grant scopes: `crm.objects.{contacts,deals,companies}.read+write`, `crm.schemas.deals.read`.
3. **Slack** — workspace is correct (Worldwidebro org) but empty; create channels off canonical 18.
4. **opcos/ rename** — execute the section 3 crosswalk to remove folder drift.
5. **Graph** — add the 10 tools as `Tool` nodes + `USES` edges to ventures (optional infra step).
