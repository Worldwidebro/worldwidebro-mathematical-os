---
date: 2026-06-19
references:
  - [[OBSIDIAN-ALIGNMENT-PLAN]]
  - [[OBSIDIAN-INTEGRATION-COMPLETE]]
status: SYNTHESIS
---

# Obsidian Best Practices Synthesis — 3 Systems Unified

Extract + synthesize best practices from **obsidian-mind**, **obsidian-skills**, and **obsidian-second-brain** into Worldwidebro 4-orb system.

---

## 3 Sources → Best Practices

### 1. obsidian-mind (Vault Template: Agent Memory)
**Brain Structure (Neural Organization)**
- `brain/North Star.md` - Strategic vision + goals
- `brain/Memories.md` - Indexed memory topics
- `brain/Key Decisions.md` - Decision log with context
- `brain/Patterns.md` - Discovered patterns + rules
- `brain/Gotchas.md` - Lessons learned + warnings
- `brain/Skills.md` - Capabilities + proficiencies

**Work Organization (Activity Tracking)**
- `work/Index.md` - Master of notes (tagged, searchable)
- `work/active/` - 1-3 current projects only
- `work/archive/YYYY/` - Completed work by year
- `work/incidents/` - Incident docs + RCA
- `work/1-1/` - Weekly meeting notes

**Performance Tracking**
- `perf/Brag Doc.md` - Wins + impact log
- `perf/competencies/` - Atomic capability notes (link targets)
- `perf/evidence/` - PR deep scans, data extracts

**Automation: 18 Custom Slash Commands**
- `/om-standup` - Morning kickoff
- `/om-weekly` - Cross-session patterns + alignment
- `/om-wrap-up` - Session review + verification
- `/om-vault-audit` - Indexes, orphans, stale content
- + 14 more

---

### 2. obsidian-skills (Agent Skill: Capability Taxonomy)
**Skills Hierarchy**
- Capabilities organized by domain
- Proficiency levels (1-5)
- Link to: agents that have it, ventures needing it, learning paths

**Capability-to-Venture Mapping**
- Which agents have which skills
- What each venture requires
- Cross-venture skill sharing

**Agent Command Patterns**
- 44 slash commands for vault automation
- `/research-deep` for semantic search
- `/obsidian-connect` for link management

---

### 3. obsidian-second-brain (Dual: Agent Skill + Vault Template)
**_CLAUDE.md Operating Manual**
- Single source of truth for vault operations
- Auto-save rules (what Claude saves without asking)
- Propagation rules (keep notes in sync)
- Naming conventions (YYYY-MM-DD)
- Kanban conventions (priority emoji + links)

**Folder Structure (Executive Preset)**
- `Daily/YYYY-MM-DD.md` - Daily standups
- `People/` - One note per person
- `Meetings/` - One per meeting
- `Decisions/` - ADR-style records
- `OKRs/` - Quarterly planning
- `Projects/` - Active + archived
- `Boards/` - Kanban + timeline
- `Reviews/` - Weekly/monthly syntheses

**Propagation Rules (Auto-Sync Pattern)**
- New project → Kanban + daily note
- Task done → Board (Done) + project + daily
- Decision made → Project + daily
- Lesson learned → Knowledge/ + daily

---

## Integration into Worldwidebro 4-Orb

### STRATEGY-ORB (obsidian-mind brain/ pattern)
```
brain/
├─ North Star.md (712-venture roadmap)
├─ Key Decisions.md (strategic decisions)
├─ Patterns.md (sector insights)
├─ Gotchas.md (failure lessons)
└─ Skills.md (agent + org capabilities)
```

### INFRASTRUCTURE-ORB (obsidian-skills taxonomy)
```
├─ Skills-Taxonomy.md (296 commands → agents)
├─ Capability-to-Repos (repos per capability)
└─ Competencies/ (atomic capability notes)
```

### VENTURES-ORB (obsidian-second-brain propagation)
```
├─ Daily/ (YYYY-MM-DD standup format)
├─ Decisions/ (ADR-style + auto-link)
├─ Reviews/ (weekly/monthly)
├─ Projects/ (active + archive/YYYY/)
└─ Boards/ (OKRs, Backlog, Sprint)
```

### REFERENCE-ORB (Unified knowledge)
```
├─ People/ (contacts + involvement)
├─ Meetings/ (decisions + action items)
├─ Competencies/ (reusable capabilities)
└─ Knowledge/ (architecture, playbooks)
```

---

## Next Actions

1. ✅ Installed obsidian-second-brain (44 commands)
2. ✅ Installed obsidian-skills (5 sub-skills)
3. ⏳ Extract obsidian-mind vault practices → brain/ structure
4. ⏳ Build Skills-Taxonomy.md → map 296 commands
5. ⏳ Create _CLAUDE.md → synthesize all 3 systems
6. ⏳ Implement propagation rules → auto-sync between folders

---

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>
