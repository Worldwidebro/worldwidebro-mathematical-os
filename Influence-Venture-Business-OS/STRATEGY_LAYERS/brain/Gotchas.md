---
type: lessons-learned
date: 2026-06-19
tags: [gotchas, failures, lessons]
---

# Gotchas — Lessons Learned

## System Design

### G1: Master Index Fragmentation
**Gotcha:** Created 71 duplicate master indexes before realizing problem.  
**Lesson:** Unify references via wiki links instead of creating new masters.  
**Implication:** Always consolidate before creating (avoid "update & connect" after)

### G2: File Organization Chaos
**Gotcha:** 95+ unorganized folders made navigation impossible.  
**Lesson:** Enforce 4-layer structure from day 1 (STRATEGY, INFRASTRUCTURE, VENTURES, REFERENCE).  
**Implication:** New ventures get auto-placed in correct folder

### G3: Obsidian Plugin vs. Skill Confusion
**Gotcha:** Tried to install GitHub repos as Obsidian plugins when they were agent skills.  
**Lesson:** Classify repos by capability before installing (plugin vs. skill vs. template).  
**Implication:** Verify installation method before cloning

## Venture Execution

### G4: CON Sector Coverage Gaps
**Gotcha:** Only 4 of 20 construction sub-sectors implemented (20% coverage).  
**Lesson:** Identify full sector before launch; stagge rollout rather than surprise gaps.  
**Implication:** Map all 31 sectors + sub-sectors upfront

### G5: Repository Classification Delays
**Gotcha:** 591 unclassified repos became a blocker for venture planning.  
**Lesson:** Classify repos before designing ventures (you'll need them).  
**Implication:** Repository Intelligence must precede venture launches

## Agent Operations

### G6: Manual Skill Invocation at Scale
**Gotcha:** Manually running obsidian-second-brain commands for each venture is unsustainable.  
**Lesson:** Automate via cron jobs + SessionStart hooks from day 1.  
**Implication:** Design ventures as command chains, not manual workflows

### G7: Propagation Rule Drift
**Gotcha:** Without explicit propagation rules, daily notes + decisions + reviews get out of sync.  
**Lesson:** Define propagation rules in _CLAUDE.md upfront.  
**Implication:** Auto-save rules prevent human inconsistency

## Organizational

### G8: Team Context Loss
**Gotcha:** Without SessionStart hook, agents lose vault context between sessions.  
**Lesson:** Inject vault context automatically (SessionStart hook + QMD index).  
**Implication:** No manual context-loading needed per session

---

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>
