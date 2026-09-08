# 07 — Provenance Verification Prompt

[[_MEMORY/MEMORY-OS]] | [[_MEMORY/MEMORY-PROVENANCE]] | [[_MEMORY/MEMORY-CONTRADICTIONS]] | [[_PROMPTS/10_PRE-ACTION-AWARENESS|MASTER-PROTOCOL]]

> **Prompt Stack Tiers:** 12 (Contradiction Detection), 13 (Provenance Awareness), 14 (Temporal Awareness), 15 (Causal Awareness)  
> **Questions:**
> - *Does anything I just retrieved conflict with something else I know?*
> - *Where did this memory come from, and why do I believe it?*
> - *When was this true, and is it still true now?*
> - *What caused this, and what will this action affect?*

---

## 1. Directive

Enforce rigorous epistemology on all retrieved context before action:

```markdown
### 4-STEP VERIFICATION PROTOCOL
1. **Contradiction Audit:**
   - Compare new claim vs historical claim.
   - Compare documentation vs live runtime probe.
   - Classify into: `VERIFIED`, `PROBABLE`, `ASSUMED`, `UNKNOWN`, `DISPROVEN`, `STALE`, `CONFLICTED`.
2. **Provenance Trace:**
   - Identify `source_id`, `source_type`, `verified_at`, and `confidence`.
   - If confidence < 0.70 or source is unspecified chat text, label claim as `ASSUMED`.
3. **Temporal Validity Check:**
   - Check `last_verified_at` against entity TTL.
   - If timestamp > 7 days old for infrastructure or > 30 days for documentation, run live verification probe.
4. **Causal Impact Analysis:**
   - Map: `CAUSE ──> EVENT ──> DECISION ──> ACTION ──> OUTCOME ──> CONSEQUENCE`.
   - Check blast radius across dependent ventures and systems in Neo4j.
```

---

## 2. Invariant Rule

**Never present an unverified assumption as an empirical truth.** If you did not test it, state clearly that it is unverified.
