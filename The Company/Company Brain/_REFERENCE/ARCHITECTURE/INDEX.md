# ARCHITECTURE — Foundation Documents Index

**Version:** 1.0  
**Status:** Foundation Layer Complete  
**Authority:** [[STARTHERE|STARTHERE.md]]  
**Last Updated:** 2026-09-18

> **The Foundation.** Five documents describe the complete Master Orchestrator system — the organizational operating system coordinating Company Brain (intelligence), Agents (execution), Capabilities (inventory), and Results (feedback).

---

## Quick Navigation

| Document | Purpose | Read Time | Entry Point |
|----------|---------|-----------|-------------|
| [[01-COMPANY-BRAIN\|01 — The Company Brain]] | Organizational intelligence layer (Neo4j, Qdrant, Registries, Memory) | 15 min | "What does the organization know?" |
| [[02-MASTER-ORCHESTRATOR\|02 — The Master Orchestrator]] | 13-stage decision loop (Observe→Learn→UpdateBrain) | 15 min | "How does the organization act?" |
| [[03-AGENT-SYSTEM\|03 — The Agent System]] | Workers characterized by capabilities, performance, autonomy, capacity | 15 min | "Who does the work?" |
| [[04-CAPABILITY-SYSTEM\|04 — The Capability System]] | Inventory of what's possible (Gap analysis, acquisition strategies) | 15 min | "Can we do this?" |
| [[05-EXECUTION-LOOP\|05 — The Execution Loop]] | Complete flow from objective to outcome (14 stages, decision gates) | 20 min | "How do we turn decisions into results?" |

---

## How They Connect

```
START: Business Objective
  ↓
01. COMPANY BRAIN reads organizational state
  ↓
02. MASTER ORCHESTRATOR makes decision
  ↓
03. AGENT SYSTEM matches workers to tasks
  ↓
04. CAPABILITY SYSTEM ensures capability exists
  ↓
05. EXECUTION LOOP drives work from start to finish
  ↓
RESULT: Outcome reported back to Company Brain (feedback loop)
```

---

## Reading Sequence

### First-Time Orientation (60 minutes)
1. **[[01-COMPANY-BRAIN]]** (15 min) — Understand the intelligence layer
2. **[[02-MASTER-ORCHESTRATOR]]** (15 min) — Understand the decision loop
3. **[[03-AGENT-SYSTEM]]** (15 min) — Understand who executes
4. **[[04-CAPABILITY-SYSTEM]]** (10 min) — Understand capability inventory
5. **[[05-EXECUTION-LOOP]]** (10 min) — Understand end-to-end flow

### Deep Dive by Role

**System Architects:** 01 → 02 → 05 (understand flow)  
**Agent Builders:** 03 → 04 → 05 (understand capability matching)  
**Operations:** 02 → 05 → 01 (understand decision flow)  
**Strategy:** 04 → 02 → 01 (understand capability-driven planning)

### Troubleshooting

**"How do I know what we know?"** → [[01-COMPANY-BRAIN]]  
**"How do I delegate work?"** → [[02-MASTER-ORCHESTRATOR]] + [[03-AGENT-SYSTEM]]  
**"Do we have this capability?"** → [[04-CAPABILITY-SYSTEM]]  
**"Is this task actually complete?"** → [[05-EXECUTION-LOOP|Evaluation & Verification sections]]

---

## References

**Root Documents:**
- [[STARTHERE|STARTHERE.md]] — Master orientation legend
- [[REALITY|REALITY.md]] — Verified truth ledger
- [[ANTIGRAVITY|ANTIGRAVITY.md]] — Operating rules

**Related Architecture:**
- [[ORCHESTRATOR-MASTER-SPECIFICATION|ORCHESTRATOR-MASTER-SPECIFICATION.md]] — Implementation details (API specs, database schema, endpoints)
- [[RUNBOOKS|_REFERENCE/RUNBOOKS/README.md]] — Incident response guides

**Registries:**
- [[AGENT_REGISTRY|_REGISTRIES/CANONICAL/AGENT_REGISTRY.yaml]] — 318 agents with capabilities
- [[CAPABILITY_REGISTRY|_REGISTRIES/CANONICAL/CAPABILITY_REGISTRY.yaml]] — Capability inventory
- [[NAVIGATION_ALIASES|_REGISTRIES/CANONICAL/NAVIGATION_ALIASES.yaml]] — All wiki link aliases

---

**Purpose of this document:** Navigation hub for the 5 foundation architecture documents. Links each document to its primary use case and shows how they connect end-to-end.

**Next step after reading:** Return to [[STARTHERE]] or choose your role-specific deep dive above.

---

**Last Updated:** 2026-09-18 | **Architecture Version:** 1.0
