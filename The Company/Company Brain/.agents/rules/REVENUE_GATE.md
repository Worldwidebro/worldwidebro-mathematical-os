# REVENUE_GATE — Anti-Sprawl & Business Execution Constraint

> **Scope:** Universal Agent Operational Constraint  
> **Authority:** System Architecture & Infrastructure Control Plane (CP-027) + Revenue CP-021  
> **Precedence:** Absolute. Supercedes all meta-work, indexing, and architectural scaffolding requests.  
> **Harness Lineage:** Grounded in principles from `emcie-co/parlant` (Policy Control), `coleam00/Archon` (Deterministic Gates), and `huangruiteng/loopx` (Durable State).

---

## 1. The Core Problem
Company Brain has accumulated 108,000+ graph nodes, 131,000+ links, 20,000+ Neo4j edges, 1,740 repositories, 789 ventures, and dozens of ontologies, but **current revenue is $0**. 

Agents continually default to **Infinite Meta-Work Recursion**: re-indexing, re-cataloging, re-auditing, creating new registries, adding ontologies, and refactoring schemas instead of executing real-world transactions that generate business income.

This rule enforces a strict, unbreakable operational halt to meta-work.

---

## 2. The 5 Mandatory Constraints

### Rule 1: Zero Meta-Work Moratorium (Freeze `_REGISTRIES/` and `_ONTOLOGY/`)
- **Prohibited:** Creating new YAML/JSON/CSV registries, ontology definitions, bitemporal schemas, entity taxonomies, or directory reorganizations.
- **Allowed:** Reading existing canonical registries as read-only data, or appending live transaction receipts/contracts.
- **Enforcement:** If a proposed task does not directly interact with a customer, take a payment, or send an invoice, it is disallowed.

### Rule 2: Single-Focus Lock (Only Tier-0 Ventures Permitted)
Work is strictly frozen on ventures 4 through 789. Agents are authorized to touch **ONLY the 3 Revenue-Ready Tier-0 Ventures**:
1. **OPS-001** (WorldwideBro Staffing Ops LLC — cold calls, facility staffing placements)
2. **LT-005** (HealthRoute Logistics LLC — medical courier dispatch, facility intake, Stripe billing)
3. **CALLCENTER** (Voice OS / Twilio Integration — inbound/outbound phone execution)

*All other 786 ventures remain in frozen cold-storage until these three hit their Week 1 revenue target ($7,500 - $20,000).*

### Rule 3: Deterministic Verification Gates (The Archon Principle)
- **No Fake Completion:** Never report "Done", "Fixed", or "Production Ready" in prose or with a Markdown report.
- **Verifiable Proof Required:** Every execution step must conclude with concrete, testable proof:
  - Live HTTP 200 response with verified payload
  - Live Stripe checkout / payment link tested with real payload
  - Verified outreach execution log (dialed call ID or sent message ID)

### Rule 4: Explicit Business State Machine (The Parlant Principle)
Every agent action touching a venture must directly advance an opportunity along the explicit 5-stage pipeline:
$$\text{LEAD\_IDENTIFIED} \longrightarrow \text{OUTREACH\_SENT} \longrightarrow \text{CALL\_HELD} \longrightarrow \text{CONTRACT\_DELIVERED} \longrightarrow \text{PAYMENT\_COLLECTED}$$

If a task cannot state which stage of this pipeline it moves, it must not be executed.

### Rule 5: Durable State & Ban on Re-Auditing (The LoopX Principle)
- **Anti-Amnesia:** Agents must never begin a session by re-scanning the 108,000 graph nodes, re-evaluating all repositories, or writing an audit of what is missing.
- **Resume from Checkpoint:** Agents must immediately inspect the active blockers of the 3 Tier-0 ventures in `20-DECISIONS/` and execute the next physical step.

---

## 3. The 48-Hour Distance-to-Cash Filter
Before executing any tool call or code modification, every agent must evaluate:

$$\text{DistanceToCash} \le 48\text{ hours}$$

- **YES:** The action produces an outbound lead list, configures a payment gateway, sets up an active phone script, or closes a customer deal. $\rightarrow$ **EXECUTE.**
- **NO:** The action creates internal documentation, theoretical models, unused endpoints, or semantic graphs. $\rightarrow$ **REJECT IMMEDIATELY.**
