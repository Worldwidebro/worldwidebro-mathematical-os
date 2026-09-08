# 02 — Current-State Awareness Prompt

[[STARTHERE]] | [[REALITY]] | [[_MEMORY/MEMORY-OS]] | [[_PROMPTS/10_PRE-ACTION-AWARENESS|MASTER-PROTOCOL]]

> **Prompt Stack Tier:** 02 (Current-State Awareness / Working Memory)  
> **Question:** *What is happening right now?*

---

## 1. Directive

Establish working memory by auditing the live situation before proposing or changing anything:

```markdown
### CURRENT-STATE WORKING AUDIT
- [ ] **Current Task:** Exactly what is being requested in the user's prompt?
- [ ] **Current Operating State:**
  - Git branch, status, uncommitted modifications (`git status -s`).
  - Active daemon processes (`omniroute` on `:20128`, `ollama` on `:11434`, `exo` on `:52415`).
  - Active mounts (`/Volumes/T7 Shield`, `/Volumes/LaCie`).
- [ ] **Current Priority:** Consult [[PRIORITIES.md]] (Revenue engine, infrastructure consolidation).
- [ ] **Active Blockers:** Any missing tokens, permissions, or failed tests?
- [ ] **Active Dependencies:** What upstream services or files are being touched?
- [ ] **Recent Changes:** What changed in the last turn or session? Consult [[UPDATE.md]].
```

---

## 2. Invariant Rule

**Do not assume state from memory when an empirical test can verify it in 50 milliseconds.**  
If you believe a port is open, check it. If you believe a file exists, view it.
