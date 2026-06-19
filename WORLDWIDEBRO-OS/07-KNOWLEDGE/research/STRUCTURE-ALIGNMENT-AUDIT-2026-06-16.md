---
title: Structure Alignment Audit
date: 2026-06-16
status: CURRENT STATE ANALYSIS
---

# Do We Have Aligned Folder Structure?

**SHORT ANSWER:** ❌ NO. Current folders don't show clear info flow or tool alignment.

---

## PART 1: WHAT EXISTS (Current Inventory)

```
/Documents/
├── 00-OPERATING-SYSTEM/          ← Partially structured
│   ├── 01-CORE-SYSTEMS/
│   ├── 02-ECOSYSTEM-MAP/
│   ├── 03-VENTURES-BY-LAYER/
│   ├── 04-EXECUTION/
│   └── 05-DOCUMENTATION/
├── 01-ACTIVE-PROJECTS/
├── 02-INFRASTRUCTURE/            ← EMPTY
├── 03-KNOWLEDGE-BASE/            ← EMPTY
├── 04-ARCHIVED/
├── 05-TEMP-AND-INBOX/
├── 06-12: Topic .md files        ← Scattered docs
└── WORLDWIDEBRO-OS/
    ├── 10_VENTURES/
    └── REGISTRIES/               ← Repo intelligence
```

**PROBLEM:** Numbered folders exist, but they're NOT functional layers. They're topic-based.

---

## PART 2: NEURAL-OS BLUEPRINT (What We Need)

```
neural-os/
├── 00-meta-registry/        ← VENTURE + REPO INDEX
├── 01-identity-governance/  ← ROLES + ACCESS RULES
├── 02-people-network/       ← CONTACTS + CONTRACTORS
├── 03-contracts/            ← LEGAL TEMPLATES
├── 04-mcp-servers/          ← TOOL BRIDGES (Supabase, ClickUp, etc)
├── 05-agents/               ← AI WORKERS (CEO/COO/CFO)
├── 06-repo-intelligence/    ← STARRED REPOS MAPPED
├── 07-workflows/            ← n8n EXECUTION
├── 08-finance-engine/       ← MONEY SYSTEM
├── 09-ventures/             ← 1,308 VENTURES
├── 10-knowledge-graph/      ← RELATIONSHIPS
├── 11-data-layer/           ← SUPABASE SCHEMA
├── 12-interfaces/           ← DASHBOARDS
└── README.md (MASTER)
```

---

## PART 3: GAP ANALYSIS (What's Missing or Scattered)

| Neural-OS Layer | Function | Current Location | Status |
|---|---|---|---|
| 00-meta-registry | Venture index | WORLDWIDEBRO-OS/10_VENTURES | ⚠️ Scattered |
| 00-meta-registry | Repo catalog | WORLDWIDEBRO-OS/REGISTRIES | ⚠️ Scattered |
| 01-identity-governance | Role definitions | DOESN'T EXIST | ❌ MISSING |
| 02-people-network | Contacts schema | DOESN'T EXIST | ❌ MISSING |
| 03-contracts | Legal templates | DOESN'T EXIST | ❌ MISSING |
| 04-mcp-servers | MCP config | .claude/CLAUDE.md (text only) | ⚠️ Undocumented |
| 05-agents | Agent prompts | .agents/ + agents/ | ⚠️ Undocumented |
| 06-repo-intelligence | Repo classification | WORLDWIDEBRO-OS/REGISTRIES | ⚠️ Scattered |
| 07-workflows | n8n workflows | make-workflows/ | ⚠️ Scattered |
| 08-finance-engine | Financial model | Documents/ (multiple .md files) | ⚠️ Scattered |
| 09-ventures | Venture details | Multiple locations | ⚠️ DISPERSED |
| 10-knowledge-graph | Graph schema | .planning/ (partial) | ⚠️ Partial |
| 11-data-layer | DB schema | operating_system_schema.sql | ⚠️ Undocumented |
| 12-interfaces | Dashboards | Obsidian / Notion | ⚠️ Undocumented |

---

## PART 4: TOOLS MENTIONED BUT NOT ORGANIZED

**What exists:**
- ✅ Supabase MCP (documented in CLAUDE.md)
- ✅ ClickUp MCP (documented, now building integration)
- ✅ GitHub MCP (documented)
- ✅ Slack MCP (documented)
- ✅ Notion MCP (documented)
- ✅ n8n (workflows folder exists)
- ✅ Neo4j/Chroma (knowledge graph infrastructure)
- ✅ Agents (partially documented)

**Problem:** No unified folder showing:
- What tools exist
- What each tool CAN do
- What each tool SHOULD do
- How they're connected

---

## PART 5: CURRENT INFORMATION FLOW (ACTUAL, Not Documented)

```
SUPABASE (source of truth)
    ↓
    ├→ Python scripts (populate_venture_knowledge_graph.py)
    │  └→ Obsidian dashboards (KNOWLEDGE-GRAPH-DASHBOARD.md)
    │     └→ Display (no action)
    │
    └→ [NO DOCUMENTED FLOW TO:]
       ├ ClickUp (we're building this now)
       ├ Notion (sync_ventures_to_notion.py exists, undocumented)
       ├ Finance engine
       └ Agent decision system

GITHUB REPOS
    ↓
    ├→ scan_repositories.py
    │  └→ REGISTRIES/ (classified repos)
    │     └→ repo_venture_mapping.py (incomplete)
    │        └→ [BROKEN - mapping incomplete]

AGENTS
    ↓
    ├→ Prompts (.agents/)
    │  └→ [NO DOCUMENTED TOOL ASSIGNMENT]
    │
    └→ MCP tools (documented only in CLAUDE.md)
       └→ [NO CLEAR PERMISSION MATRIX]

CONTRACTS
    ↓
    └→ [DOESN'T EXIST - not gating any workflows]

PEOPLE/CONTACTS
    ↓
    └→ [SCATTERED - no unified directory]
```

---

## PART 6: INFO FLOW GAPS (Why It's Not Clear)

1. **No Tool Registry** — Which MCP does what? Who can call it?
2. **No Agent Registry** — What agents exist? What are they allowed to do?
3. **No Venture Flow** — Where does a venture come from? Who owns it? How does it change?
4. **No Workflow Visibility** — Which n8n workflows exist? When do they run?
5. **No Contract Linkage** — Are contracts gating any execution?
6. **No People Assignment** — Who does what work? How are tasks routed?
7. **No Finance Tracking** — How much did each venture spend/earn?

---

## PART 7: CURRENT STATE SUMMARY

| Aspect | Status | Severity |
|---|---|---|
| Folder structure exists | ✅ Yes (00-12) | Info |
| Folders aligned to neural-os | ❌ No | HIGH |
| Info flow documented | ❌ No | CRITICAL |
| Tools organized | ❌ No | HIGH |
| MCPs mapped to folders | ❌ No | HIGH |
| Agents registered | ⚠️ Partially | MEDIUM |
| Venture tracking clear | ⚠️ Partially (scattered) | MEDIUM |
| Contracts integrated | ❌ No | MEDIUM |

---

## DECISION: What Do We Do?

**Option A: Build Neural-OS (Clean Start)**
- Create /neural-os/ folder in Documents/
- Reorganize into 13 functional layers
- Map all tools + agents + workflows
- Migrate 1,308 ventures to new structure
- Time: 2-3 hours

**Option B: Align In-Place (Fast)**
- Rename/reorganize current 00-12 folders
- Add missing folders (contracts, people, etc)
- Map tools and agents into structure
- Import ventures into sector folders
- Time: 1-2 hours

**Option C: Hybrid (Pragmatic)**
- Create neural-os/ as control plane
- Current Documents/ stays as archive
- All NEW work goes into neural-os/
- Migration happens gradually
- Time: 30 min to start, ongoing

---

## RECOMMENDATION

**Go with Option C (Hybrid):**

This allows:
1. ✅ Immediate execution (no disruption)
2. ✅ Clean new structure going forward
3. ✅ Gradual migration of old content
4. ✅ Both systems coexist during transition

**Then execute in order:**
1. Create neural-os/ structure (10 min)
2. Map tools → 04-mcp-servers/ (5 min)
3. Map agents → 05-agents/ (5 min)
4. Batch import 1,308 ventures → 09-ventures/ (5 min)
5. Create unified info flow diagram (10 min)
6. **System is immediately operational**

---

## ANSWER TO YOUR QUESTION

**"Do we have the current folders structured to understand info flow + tool alignment?"**

- **Current state:** ❌ NO
- **Can we fix it:** ✅ YES (Option C = 35 minutes)
- **Should we do it:** ✅ YES (enables execution)
- **When:** **NOW** (before batch importing 1,308 ventures)

---

## IMMEDIATE NEXT STEP

Should we execute Option C now?

If YES:
- I build neural-os/ structure
- Map tools + agents into it
- Then finish ClickUp batch import into proper folders
- System is clean + operational

If you want details on what neural-os/ will look like before we build, I can show the exact folder structure + key files first.

Which?
