# MEMORY-AWARENESS — The 20-Point Pre-Response Awareness Protocol

[[_MEMORY/MEMORY-OS|MEMORY-OS]] | [[_PROMPTS/10_PRE-ACTION-AWARENESS|10_PRE-ACTION-AWARENESS]] | [[STARTHERE]] | [[ANTIGRAVITY]]

> **Canonical Document ID:** `MEM-AWA-001`  
> **Authority:** System Architecture & Infrastructure Control Plane (CP-027)

---

## 1. The Pre-Response Check

Before answering a prompt, making a code modification, or running an infrastructure command, an agent must traverse this 20-point protocol:

```text
IDENTITY CHECK ──> CURRENT STATE ──> RELEVANT MEMORY ──> RELATED ENTITIES
      │                                                         │
      ▼                                                         ▼
PRIOR DECISIONS ──> PROCEDURES ──> CONTRADICTIONS ──> PROVENANCE / TEMPORAL
      │                                                         │
      ▼                                                         ▼
GOAL ALIGNMENT ──> UNKNOWNS AUDIT ──> PREDICT IMPACT ──> EXECUTE ACTION
```

### The 20 Inquiries:
1. **WHO am I?** (Role, persona, tool permissions, limitations).
2. **WHO is the user?** (Sovereign Operator, privileges, preferences).
3. **WHAT system am I operating within?** (Company Brain, host node, active runtime).
4. **WHAT is the current task?** (Immediate operational objective).
5. **WHAT is the current state?** (Working memory, uncommitted diffs, active ports).
6. **WHAT is the overarching goal?** (North Star, commercial priority).
7. **WHAT happened previously?** (Episodic history, prior session attempts).
8. **WHAT facts are relevant?** (Semantic facts about involved ventures, repos, systems).
9. **WHAT entities are connected?** (Neo4j graph associations, dependencies).
10. **WHAT decisions already exist?** (Settled ADRs, locked designs — do not reopen).
11. **WHAT procedures already exist?** (Relevant skills in `.agents/skills/`, 45 ANTIGRAVITY rules).
12. **WHAT preferences are known?** (User explicit preferences vs inferred assumptions).
13. **WHAT evidence supports these memories?** (Provenance check — reject ungrounded claims).
14. **WHAT has changed?** (State diff since last session or execution).
15. **WHAT is stale?** (Facts exceeding validity windows needing live probes).
16. **WHAT conflicts?** (Contradictions between documentation and runtime reality).
17. **WHAT patterns resemble this situation?** (Historical incidents, recurring bottlenecks).
18. **WHAT dependencies exist?** (Upstream prerequisites, downstream consumers).
19. **WHAT consequences could this action create?** (Blast radius, side-effects, rollback plan).
20. **WHAT should be remembered afterward?** (Learnings, new facts, consolidated procedures).

---

## 2. Distinction of Knowledge Types

Never confuse these categories:
- **FACT**: Empirically verified observation supported by runtime proof.
- **OBSERVATION**: Raw measurement or telemetry output.
- **CLAIM**: Assertion made in chat or unstaged documentation awaiting verification.
- **ASSUMPTION**: Declared design intention or hypothesis; unproven.
- **INFERENCE**: Deduction drawn by LLM reasoning. Must not be treated as permanent fact.
- **DECISION**: Formally accepted architectural consensus.
- **PREFERENCE**: Explicit user requirement for formatting, style, or workflows.
- **PATTERN**: Recurrent observation across multiple distinct episodes.
- **PROCEDURE**: Validated sequence of executable steps to produce an outcome.
- **UNKNOWN**: Explicitly acknowledged lack of empirical data.
