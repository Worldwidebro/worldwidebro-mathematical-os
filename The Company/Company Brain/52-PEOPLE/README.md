# BASE — People

**Authoritative registry of individuals** in the Company Brain ecosystem.

**Connects to:** [[16-AGENTS]] (who manages/approves each agent)

---

## Contains

[[Person]]
[[Founder]]
[[Owner]]
[[Executive]]
[[Employee]]
[[Contractor]]
[[Advisor]]
[[Investor]]
[[Customer Contact]]
[[Partner Contact]]
[[Vendor Contact]]
[[Candidate]]

---

## Every Person Links To

[[Team]]
[[Organization]]
[[Role]]
[[Responsibilities]]
[[Skills]]
[[Capabilities]]
[[Projects]]
[[Tasks]]
[[16-AGENTS]] ← **NEW: Agent assignments & approvals**
[[Decisions]]
[[Approvals]]
[[Goals]]
[[Performance]]
[[Relationships]]

---

## Key Relationships

- [[Person]] → MEMBER_OF → [[Team]]
- [[Person]] → WORKS_FOR → [[Organization]]
- [[Person]] → HAS_ROLE → [[Role]]
- [[Person]] → HAS_SKILL → [[Skill]]
- [[Person]] → MANAGES → [[16-AGENTS]] ← **NEW**
- [[Person]] → APPROVES → [[16-AGENTS]] ← **NEW**
- [[Person]] → EXECUTES_VIA → [[16-AGENTS]] ← **NEW**
- [[Person]] → COLLABORATES_WITH → [[Person]]
- [[Person]] → SUPERVISES → [[Person]]
- [[Person]] → APPROVES → [[Decision]]
- [[Person]] → OWNS → [[Venture]]
- [[Person]] → LEADS → [[Team]]
- [[Person]] → PARTICIPATES_IN → [[Project]]

---

## Agent Governance

Each [[16-AGENTS]] agent has assigned:
- **Manager** (Person who oversees agent)
- **Approvers** (People who approve L1 → L2 → L3 escalations)
- **Executors** (People who can invoke agent)
- **Watchers** (Teams monitoring agent decisions)

---

## Governance

- Every person has an identity (see [[27-SECURITY]])
- Every person belongs to at least one team
- Every person has defined roles and responsibilities
- Every person's relationships with agents are recorded ← **NEW**

**Status:** Active | **Last Updated:** 2026-09-02
