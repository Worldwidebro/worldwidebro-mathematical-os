# 06 — Decision Memory Prompt

[[_MEMORY/MEMORY-OS]] | [[_MEMORY/MEMORY-MODEL]] | [[_PROMPTS/10_PRE-ACTION-AWARENESS|MASTER-PROTOCOL]]

> **Prompt Stack Tiers:** 09 (Procedural Recall), 10 (Preference Recall), 11 (Decision Memory)  
> **Questions:**
> - *How have we successfully handled this before?* (Procedural)
> - *What does the user/system consistently prefer?* (Preference)
> - *What decisions have already been made, and why?* (Decision)

---

## 1. Directive

Prevent circular reasoning and reopening settled architecture questions:

```markdown
### DECISION & PREFERENCE CHECKLIST
1. **Locate Prior Decision:** Check `20-DECISIONS/` and `_DOCS/ADR/` for locked architectural records.
2. **Review Rationale & Trade-offs:** Understand why alternative approaches were rejected.
3. **Audit Current Validity:** Has empirical reality changed to invalidate the decision? If not, maintain the decision.
4. **Retrieve Explicit Preferences:**
   - Communication style: Concise, evidence-grounded, Markdown links with file:// schemes.
   - Engineering style: Reusable first, zero mock data, local-first sovereignty.
   - Distinguish: Explicit user directives vs weak agent inferences. Never treat an inference as an established preference.
5. **Procedural Recall:** Look up corresponding standard runbook in `.agents/skills/*/SKILL.md` before writing ad-hoc scripts.
```

---

## 2. Invariant Rule

**Do not reopen settled architectural decisions without new empirical evidence or explicit operator direction.**
