# 08 — Memory Consolidation Prompt

[[_MEMORY/MEMORY-OS]] | [[_MEMORY/MEMORY-CONSOLIDATION]] | [[_PROMPTS/10_PRE-ACTION-AWARENESS|MASTER-PROTOCOL]]

> **Prompt Stack Tiers:** 16 (Goal Awareness), 17 (Learning Prompt), 18 (Memory Consolidation)  
> **Questions:**
> - *How does this relate to the North Star and current priority?*
> - *What did we learn from this action?*
> - *Should this experience become long-term knowledge?*

---

## 1. Directive

Execute institutional learning after completing work or encountering a blocker:

```markdown
### POST-ACTION LEARNING RECORD
- [ ] **Task Alignment:** Did this action advance the North Star or current tactical priority?
- [ ] **What Worked:** Identify tools, patterns, or commands that produced verified success.
- [ ] **What Failed:** Identify failed commands, unexpected errors, and time wasted.
- [ ] **Root Cause:** Why did the failure occur?
- [ ] **Unexpected Results:** What surfaced that was surprising or undocumented?
- [ ] **New Procedural Rule:** Can this workflow be codified into an automated script or `.agents/skills/` runbook?
- [ ] **Consolidation Target:**
  - Semantic Fact → Upsert point in Qdrant / `_REGISTRIES/`
  - Relational Edge → Merge relationship in Neo4j
  - Procedural SOP → Update `.agents/skills/` or `_CLI/`
```

---

## 2. Invariant Rule

**Transform every non-trivial failure into a permanent guardrail so no agent in the fleet repeats it.**
