---
references:
  - [[OBSIDIAN-GRAPH-STATUS]]
  - [[OBSIDIAN-LINKING-STRATEGY-2026-06-11]]
  - [[Influence-Venture-Business-OS/INFRASTRUCTURE_LAYERS/venture-hub/]]
  - [[ORB-MASTER-CONNECTOR-2026-06-11]]
created: 2026-06-19T10:44:00Z
updated: 2026-06-19T10:51:00Z
status: PLANNING
---

# Obsidian Alignment Plan: 3 GitHub Repos + 4-Orb System

**Purpose:** Integrate obsidian-mind, obsidian-skills, and obsidian-second-brain plugins with existing Worldwidebro Obsidian setup to create comprehensive knowledge + memory system.

**Current State:**
- ✅ 4-orb system live (STRATEGY ↔ INFRASTRUCTURE ↔ VENTURES ↔ REFERENCE)
- ✅ 51 internal connections established
- ✅ Knowledge graph visible in Obsidian (Cmd+Shift+G)
- ⚠️ 150+ orphaned files need linking
- ⚠️ Missing: mind mapping, skills taxonomy, memory system

---

## Executive Summary

### 3 GitHub Repos — What They Do

| Repo | Purpose | Use For | Adds |
|------|---------|---------|------|
| **obsidian-mind** | Visual mind mapping + tree structure | Venture ideation, sector relationships, strategic planning | Non-linear thinking, radial maps, brainstorm→structure |
| **obsidian-skills** | Skills taxonomy + capability tracking | Agent capabilities, venture requirements, learning paths | Skill hierarchy, capability matching, learning visualization |
| **obsidian-second-brain** | Personal knowledge system + lifecycle | Venture memory, decision logs, knowledge retention | Permanent notes, literature notes, review cycles, archives |

### Integration Strategy

```
LAYER 0: 4-ORB FOUNDATION (Current)
  STRATEGY ↔ INFRASTRUCTURE ↔ VENTURES ↔ REFERENCE

LAYER 1: MIND MAPS (obsidian-mind)
  └─ Visual strategizing for sectors + ventures
  └─ Linked to: STRATEGY-HUB + REFERENCE-HUB

LAYER 2: SKILLS TAXONOMY (obsidian-skills)
  └─ Capability mapping + agent/venture matching
  └─ Linked to: INFRASTRUCTURE-HUB + VENTURES-HUB

LAYER 3: SECOND BRAIN (obsidian-second-brain)
  └─ Venture memories + decision logs + review cycles
  └─ Linked to: ALL 4 HUBS + lifelong memory

RESULT: 3-layer memory system on top of 4-orb knowledge graph
```

---

## Implementation Plan (Sequential Phases)

### PHASE 1: Install & Configure Plugins (4-6 hours)
**Goal:** All 3 plugins functioning in Obsidian vault

1. Clone/download obsidian-mind plugin
   - Copy to `.obsidian/plugins/obsidian-mind/`
   - Enable in Obsidian settings
   - Test: Create test mind map in STRATEGY-HUB

2. Clone/download obsidian-skills plugin
   - Copy to `.obsidian/plugins/obsidian-skills/`
   - Enable in Obsidian settings
   - Test: Create test skills taxonomy

3. Clone/download obsidian-second-brain plugin
   - Copy to `.obsidian/plugins/obsidian-second-brain/`
   - Enable in Obsidian settings
   - Test: Create test permanent note + daily entry

4. Update obsidian_graph_sync.py to recognize all 3 plugin types
   - Scan for mind maps, skills, second brain notes
   - Export plugin data to JSON layers
   - Test sync end-to-end

**Deliverable:** All 3 plugins enabled + basic features tested

---

### PHASE 2: Link 150+ Orphaned Files (8-10 hours)
**Goal:** All orphaned files properly linked to 4 hubs via skills taxonomy

**Strategy:**
1. Use obsidian-skills to classify orphaned files by capability
   - Read OBSIDIAN-LINKING-STRATEGY-2026-06-11.md
   - Map 150 files → 5 categories
   - Tag files with [[STRATEGY-HUB]], [[INFRASTRUCTURE-HUB]], etc.

2. Create linking dashboard in REFERENCE-HUB
   - "Orphaned Files Classifier" (mind map of categories)
   - "Skills Used Across Files" (taxonomy view)
   - "Files to Archive" (second brain archive workflow)

3. Link systematically:
   - Analysis files → REFERENCE-HUB
   - Strategy files → STRATEGY-HUB
   - Code files → INFRASTRUCTURE-HUB
   - Venture-specific → VENTURES-HUB
   - Archives → Second Brain archive folder

**Deliverable:** 150+ files linked + no orphans in graph view

---

### PHASE 3: Create Layer-Specific Dashboards (4-6 hours)
**Goal:** 3 visualization layers + 4 canonical orbs visible

**1. STRATEGY Layer Dashboard (mind maps)**
   - File: `Influence-Venture-Business-OS/STRATEGY_LAYERS/STRATEGY-MIND-MAPS.md`
   - Content:
     ```
     # Sector Mind Maps (31 sectors)
     - 31 interactive mind maps (one per sector)
     - Ventures in each sector (tree view)
     - Cross-sector connections
     
     # Strategic Brainstorms (quarterly)
     - Current brainstorms (active planning)
     - Archived brainstorms (reference)
     - Ideas → ventures mapping
     ```
   - Linked to: STRATEGY-HUB

**2. INFRASTRUCTURE Layer Dashboard (skills taxonomy)**
   - File: `Influence-Venture-Business-OS/INFRASTRUCTURE_LAYERS/SKILLS-TAXONOMY.md`
   - Content:
     ```
     # Agent Capabilities (by skill)
     - 20+ core capabilities
     - Which agents have each skill
     - Skill proficiency levels
     
     # Venture Requirements (what each needs)
     - marketplace-core: [authentication, payments, deployment]
     - con-009: [marketplace-core deps + roofing specifics]
     - ...
     
     # Skill→Venture Matching
     - Find agents for CON-009
     - Find ventures needing "payment processing"
     - Training paths
     ```
   - Linked to: INFRASTRUCTURE-HUB

**3. VENTURES Layer Dashboard (memories)**
   - File: `Influence-Venture-Business-OS/VENTURES/VENTURE-MEMORIES.md`
   - Content:
     ```
     # Permanent Notes (per venture)
     - marketplace-core permanent notes
     - con-009 permanent notes
     - ...
     
     # Decision Logs (what was decided + why)
     - marketplace-core decisions
     - Critical path choices
     - Why each was chosen
     
     # Weekly Reviews (what happened + lessons)
     - This week's progress
     - Blockers resolved
     - Lessons for next week
     ```
   - Linked to: VENTURES-HUB

**4. REFERENCE Layer Dashboard (unified)**
   - File: `Influence-Venture-Business-OS/REFERENCE/UNIFIED-SEARCH.md`
   - Content:
     ```
     # Multi-Layer Search
     - Search across all 3 layers + 4 hubs
     - Find decisions by keyword
     - Find capabilities by venture
     - Find files by skill
     
     # Archive & History
     - Completed ventures
     - Graduated skills
     - Old decisions
     - Lessons learned
     ```
   - Linked to: All hubs + all layers

**Deliverable:** 4 dashboards visible in Obsidian + 3 layer visualizations

---

### PHASE 4: Automation & Syncing (6-8 hours)
**Goal:** Daily auto-sync + scheduled review workflows

**1. Update obsidian_graph_sync.py**
   ```python
   # Export to 3 layers
   exports:
     - mind-maps.json (all sector maps)
     - skills-taxonomy.json (capabilities + venture requirements)
     - venture-memories.json (permanent notes + decisions + reviews)
     - archive.json (completed, old, archived)
   ```

**2. Create Daily Sync Automation**
   - Script: `WORLDWIDEBRO-OS/07_AUTOMATIONS/Scripts/obsidian-daily-sync.py`
   - Runs: 6:00 AM daily
   - Exports: Graph data → all 3 layers
   - Updates: Dashboard counts (X permanent notes, Y skills, Z ventures)

**3. Create Weekly Review Workflow**
   - Day: Sunday 5:00 PM
   - Opens: Weekly review template
   - Prompts: What happened? What learned?
   - Stores: In venture-memories.json

**4. Create Quarterly Brainstorm Workflow**
   - Day: First Monday of quarter
   - Creates: New mind map
   - Location: STRATEGY-MIND-MAPS.md
   - Prompts: New ventures? Sector shifts? Strategic pivots?

**Deliverable:** All 3 layers auto-sync daily + review cycles automated

---

## Execution Options

### OPTION A: Full Integration (20-24 hours)
**What:** Install all 3 plugins + link 150 files + create 4 dashboards + automation

**Timeline:**
- Phase 1 (plugins): 4-6h
- Phase 2 (linking): 8-10h
- Phase 3 (dashboards): 4-6h
- Phase 4 (automation): 6-8h

**Best for:** Want complete system immediately

**Outcome:**
- Complete Obsidian ecosystem
- All 150 orphaned files linked
- Full memory system live
- Automated daily/weekly/quarterly reviews

---

### OPTION B: Memory-First (6-8 hours)
**What:** Install obsidian-second-brain only, link files using that system

**Timeline:**
- Install plugin: 1h
- Create permanent note structure: 1-2h
- Link 150 files as permanent/literature notes: 3-4h
- Basic automation: 1h

**Best for:** Solve the orphaned files problem first, add layers later

**Outcome:**
- Venture memory system live
- All files organized in permanent note structure
- Foundation for Phase 3 + 4

**Then:** Can add obsidian-mind (Phase 1 part 2) + obsidian-skills (Phase 1 part 3) separately

---

### OPTION C: Skills-First (6-8 hours)
**What:** Install obsidian-skills only, use to classify + link files + match to ventures

**Timeline:**
- Install plugin: 1h
- Create skills taxonomy: 2-3h
- Classify 150 files by skill: 2-3h
- Link to capabilities: 1h

**Best for:** Solve capability matching problem, help venture decisions

**Outcome:**
- Skills taxonomy visible
- Files classified by capability
- Can query: "Which files relate to payments?" → find all payment-related files
- Can query: "What does con-009 need?" → see all required capabilities

**Then:** Can add obsidian-second-brain (Phase 1 part 3) + obsidian-mind (Phase 1 part 2) separately

---

### OPTION D: Strategic-First (4-6 hours)
**What:** Install obsidian-mind only, use for sector planning + venture ideation

**Timeline:**
- Install plugin: 1h
- Create sector mind maps: 2-3h
- Create venture relationship maps: 1-2h

**Best for:** Visualize 712 ventures + 31 sectors at once

**Outcome:**
- 31 sector mind maps (tree view)
- Venture hierarchy visible
- Strategic brainstorms mapped
- Non-linear planning possible

**Then:** Can add obsidian-second-brain + obsidian-skills separately

---

## Recommendation

**Start with OPTION B (Memory-First)**

**Reasoning:**
1. Solves immediate problem (150 orphaned files)
2. Simplest to implement (1 plugin = 1 concern)
3. Creates foundation for other layers
4. Can add A/D in parallel later (mind maps + skills don't depend on memory system)
5. Venture memory system is strategic for 712-venture holding company

**Timeline to Complete System:**
- Week 1: Option B (memory-first) — 6-8h work
- Week 2: Add Option C (skills) + Option D (mind maps) in parallel — 6-8h each
- Week 3: Option A integration (if needed) — 2-4h

---

## File Structure (After Implementation)

```
/Users/acebless/Documents/

├── .obsidian/
│   └── plugins/
│       ├── obsidian-mind/
│       ├── obsidian-skills/
│       └── obsidian-second-brain/
│
├── Influence-Venture-Business-OS/
│
│   ├── STRATEGY_LAYERS/
│   │   ├── STRATEGY-HUB.md
│   │   └── STRATEGY-MIND-MAPS.md          ← NEW (mind maps)
│   │
│   ├── INFRASTRUCTURE_LAYERS/
│   │   ├── INFRASTRUCTURE-HUB.md
│   │   └── SKILLS-TAXONOMY.md             ← NEW (skills)
│   │
│   ├── VENTURES/
│   │   ├── VENTURES-HUB.md
│   │   └── VENTURE-MEMORIES.md            ← NEW (second brain)
│   │
│   └── REFERENCE/
│       ├── REFERENCE-HUB.md
│       └── UNIFIED-SEARCH.md              ← NEW (unified dashboard)
│
├── .obsidian.linked/                      ← NEW (150 linked files)
│   ├── strategy-analysis/
│   ├── infrastructure-code/
│   ├── venture-specific/
│   └── archives/
│
├── OBSIDIAN-ALIGNMENT-PLAN.md             ← THIS FILE
├── KNOWLEDGE-GRAPH-DASHBOARD.md
└── obsidian_graph_sync.py                 ← UPDATED for 3 layers
```

---

## Success Criteria

**Phase 1 (Install):** ✅ All 3 plugins appear in Obsidian settings, can create test content in each
**Phase 2 (Link):** ✅ 0 orphaned files, all 150 files in graph + visible in one of 4 hubs
**Phase 3 (Dashboards):** ✅ Can search across all 3 layers, find decisions/capabilities/memories by keyword
**Phase 4 (Automation):** ✅ Daily sync runs without errors, weekly template appears Sunday 5pm, quarterly template appears monthly

---

## Next Step

Choose your path:
- **OPTION A** — Do everything now (20-24h)
- **OPTION B** — Memory-first, add layers later (6-8h, RECOMMENDED)
- **OPTION C** — Skills-first, add memory later (6-8h)
- **OPTION D** — Strategic mind maps first, add others later (4-6h)

Once you choose, I'll create detailed phase checklists + execute.

---

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>
