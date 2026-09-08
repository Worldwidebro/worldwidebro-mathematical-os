# 04 — Connection Reasoning Prompt

[[_MEMORY/MEMORY-OS]] | [[_MEMORY/MEMORY-RELATIONSHIPS]] | [[_PROMPTS/10_PRE-ACTION-AWARENESS|MASTER-PROTOCOL]]

> **Prompt Stack Tiers:** 05 (Relationship Awareness), 07 (Association Prompt)  
> **Question:** *What is connected to what, and what else does this remind you of?*

---

## 1. Directive

Traverse the relationship graph and generate multi-dimensional associative links across the ecosystem:

```markdown
### MULTI-DIMENSIONAL GRAPH TRAVERSAL
- [ ] **Entity → Entity:** How does this venture link to other ventures? (e.g. `LT-005` courier service supporting `CON-001`).
- [ ] **Problem → Problem:** Where else did we encounter this symptom? (e.g. Node stdout breaking MCP JSON-RPC streams).
- [ ] **Decision → Decision:** How does this decision interact with existing ADRs?
- [ ] **Venture → Sector:** Which of the 35 sectors (`SEC-001` to `SEC-035`) does this venture belong to?
- [ ] **Owned Repo → External Supply Chain:** Which external starred repo (`_REGISTRIES/EXTERNAL_CAPABILITY_UNIVERSE_INVENTORY.md`) solves this gap?
- [ ] **System → Infrastructure:** Where does this service run (Mac Studio `:7687` vs MacBook Air `:20128`)?
```

---

## 2. Invariant Rule

**A node without edges is an orphan.** Whenever creating a new venture, repository, or capability, immediately wire its bidirectional edges in the Neo4j graph and Markdown wikilinks.
