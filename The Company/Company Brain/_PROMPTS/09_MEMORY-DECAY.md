# 09 — Memory Decay & Pruning Prompt

[[_MEMORY/MEMORY-OS]] | [[_MEMORY/MEMORY-DECAY]] | [[_PROMPTS/10_PRE-ACTION-AWARENESS|MASTER-PROTOCOL]]

> **Prompt Stack Tier:** 19 (Forget / Supersede Prompt)  
> **Question:** *What should no longer be trusted or kept in working memory?*

---

## 1. Directive

Actively detect and prune obsolete, superseded, or polluting memory artifacts:

```markdown
### PRUNING & FORGETTING AUDIT
- [ ] **Obsolete Facts:** Flag facts invalidated by newer runtime evidence.
- [ ] **Superseded Decisions:** Identify retired ADRs replaced by new architectural consensus.
- [ ] **Decommissioned Infrastructure:** Purge dead container definitions, old IP addresses, and deprecated ports.
- [ ] **Completed Ephemeral Tasks:** Clean up scratch scripts, temporary artifacts, and transient subagent contexts.
- [ ] **Duplicate Records:** Deduplicate vector embeddings with cosine similarity >= 0.96.
- [ ] **Execution Action:**
  - Mark node as `SUPERSEDED` or `ARCHIVED`
  - Remove from active Qdrant retrieval collections
  - Move physical notes to `_ARCHIVE/` if applicable
```

---

## 2. Invariant Rule

**Memory quality degrades through unchecked accumulation.** Forgetting and superseding are required to maintain high precision and low token overhead.
