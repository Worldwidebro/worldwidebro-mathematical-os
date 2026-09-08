# 03 — Memory Retrieval Prompt

[[_MEMORY/MEMORY-OS]] | [[_MEMORY/MEMORY-RETRIEVAL]] | [[_PROMPTS/10_PRE-ACTION-AWARENESS|MASTER-PROTOCOL]]

> **Prompt Stack Tiers:** 03 (Historical / Episodic), 04 (Fact / Semantic), 06 (Context Retrieval)  
> **Question:** *What happened previously and what facts are true that are relevant to this task?*

---

## 1. Directive

Retrieve only the targeted memory slice necessary to execute the task without context dumping:

```markdown
### 10-SIGNAL RETRIEVAL SCORING
1. **Semantic Query:** Formulate dense vector query for Qdrant (`:6333`) on entity keywords.
2. **Episodic Scope:** Grep recent JSONL transcripts or Git commit logs for previous attempts or failures.
3. **Filter by Signals:** Rank retrieved candidate memories using [[_MEMORY/MEMORY-RETRIEVAL]]:
   - Relevance (Vector match)
   - Recency (Recent sessions > old sessions)
   - Authority (Operator directive > runtime probe > docs > chat)
   - Truth State (Reject `DISPROVEN`, `CONFLICTED`, or `STALE` without probe)
4. **Context Budget:** Max 5 semantic facts and 3 episodic records in working prompt context.
```

---

## 2. Invariant Rule

**Never load entire raw conversation histories or giant JSON registries into context.** Always query targeted fields or scoped sections.
