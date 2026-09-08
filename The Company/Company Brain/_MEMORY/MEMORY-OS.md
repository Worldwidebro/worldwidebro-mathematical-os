# MEMORY-OS — The Memory Operating System Contract

[[STARTHERE]] | [[10-MEMORY]] | [[_MEMORY/MEMORY-ARCHITECTURE|MEMORY-ARCHITECTURE]] | [[_MEMORY/MEMORY-POLICY|MEMORY-POLICY]] | [[INDEX]]

> **Canonical Document ID:** `MEM-OS-001`  
> **Authority:** System Architecture & Infrastructure Control Plane (CP-027)  
> **Status:** ACTIVE OPERATIONAL CONTRACT — Established 2026-09-05  
> **Target Runtimes:** OmniRoute (:20128), Antigravity IDE, FastMCP Server, Neo4j Graph (:7687), Qdrant (:6333)

---

## 1. Executive Mission

**Memory is not a conversation log; memory is an active, structured, associative, self-correcting operating system.**

The goal of Company Brain Memory-OS is to provide continuous, high-fidelity context, cross-venture association, and institutional learning across distributed nodes (Mac Studio M4 Max, MacBook Air, mobile edge).

Memory must answer:
> **“What is connected to what, what changed, why does it matter, what did we learn, and what should I do differently now?”**

---

## 2. The 10-Stage Cognitive Flow

Every interaction, tool execution, and decision across the Company Brain traverses this 10-stage loop:

```text
OBSERVE ──> IDENTIFY ──> CONNECT ──> REMEMBER ──> RETRIEVE
   │                                                 │
   ▼                                                 ▼
VERIFY  <── CONSOLIDATE <── LEARN <── APPLY <── UNDERSTAND
```

1. **OBSERVE**: Capture raw inputs, signals, telemetry, tool outputs, and runtime state.
2. **IDENTIFY**: Resolve identities, ventures, repositories, users, permissions, and active control planes.
3. **CONNECT**: Traverse the Neo4j relational graph to map associations between entities.
4. **REMEMBER**: Access working, episodic, semantic, and procedural stores without context pollution.
5. **RETRIEVE**: Score and rank candidate memories using the 10-signal heuristic.
6. **UNDERSTAND**: Synthesize context against current goals, constraints, and operational rules.
7. **APPLY**: Execute targeted actions, edits, or commands with minimal blast radius.
8. **LEARN**: Extract delta findings, unexpected results, failure root causes, and success patterns.
9. **CONSOLIDATE**: Graduate verified patterns from transient working memory into permanent facts/procedures.
10. **VERIFY**: Empirically validate the final state against the 7-tier Truth Model before recording.

---

## 3. Four-Layer Memory Model

Company Brain operationalizes four distinct memory layers across specialized infrastructure backends:

```text
┌─────────────────────────────────────────────────────────────────────────┐
│                       WORKING MEMORY (Session Context)                   │
│  Active task, priorities, active blockers, uncommitted diffs, scratch   │
└────────────────────────────────────┬────────────────────────────────────┘
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                     EPISODIC MEMORY (Event History)                     │
│  Interaction trajectories, git commit history, execution transcripts    │
│  Backend: JSONL Transcripts, Git Log, OpenObserve (:5080) Traces        │
└────────────────────────────────────┬────────────────────────────────────┘
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                     SEMANTIC MEMORY (Entity Knowledge)                  │
│  713 ventures, 893 owned repos, 904 external repos, ontology, facts     │
│  Backend: Qdrant Vector DB (:6333), Wikidata/Wikipedia QID groundings   │
└────────────────────────────────────┬────────────────────────────────────┘
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    PROCEDURAL MEMORY (Operational SOPs)                 │
│  45 ANTIGRAVITY rules, skills (.agents/skills/), runbooks, schemas      │
│  Backend: Canonical Registries (_REGISTRIES/), Markdown Playbooks       │
└─────────────────────────────────────────────────────────────────────────┘
                                     ▲
                                     │
┌────────────────────────────────────┴────────────────────────────────────┐
│                  RELATIONSHIP GRAPH LAYER (Graph Memory)                │
│  Entity connections, causal chains, venture ownership, dependency trees │
│  Backend: Neo4j Relational Graph (:7687 / :7474)                        │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Operational Invariants

1. **Runtime Evidence Outranks Memory**: If an entity memory asserts a service is running, but a live port probe fails, the memory is immediately tagged `DISPROVEN` or `STALE`.
2. **No Context Flooding**: Agents must never dump unranked memory dumps into prompt context. Retrieval must be scoped by the 10-signal scoring formula in [[_MEMORY/MEMORY-RETRIEVAL]].
3. **Zero-Trust Credential Security**: Secrets and API keys must NEVER be stored in memory nodes, embeddings, or logs. All credentials resolve dynamically via Bitwarden CLI (`bw` / `SEC-BITWARDEN-001`).
4. **Mandatory Provenance**: Every permanent memory item must carry provenance metadata (`source_id`, `verified_at`, `confidence`, `author`). Unverified claims remain strictly marked `ASSUMED`.
5. **Continuous Decay & Consolidation**: Transient session data decays after 7 days unless graduated by [[_MEMORY/MEMORY-CONSOLIDATION]] into a verified semantic fact or procedural rule.

---

## 5. Subsystem Map

- Architecture & Infrastructure: [[_MEMORY/MEMORY-ARCHITECTURE]]
- Governance & Security Policy: [[_MEMORY/MEMORY-POLICY]]
- 4-Tier Memory Formal Model: [[_MEMORY/MEMORY-MODEL]]
- Lifecycle & State Machine: [[_MEMORY/MEMORY-LIFECYCLE]]
- Context Retrieval & Ranking: [[_MEMORY/MEMORY-RETRIEVAL]]
- Consolidation Engine: [[_MEMORY/MEMORY-CONSOLIDATION]]
- Decay, Forgetting, & Pruning: [[_MEMORY/MEMORY-DECAY]]
- Truth & Quality Assurance: [[_MEMORY/MEMORY-QUALITY]]
- Provenance & Traceability: [[_MEMORY/MEMORY-PROVENANCE]]
- Contradiction Detection: [[_MEMORY/MEMORY-CONTRADICTIONS]]
- Graph & Relationship Schema: [[_MEMORY/MEMORY-RELATIONSHIPS]]
- Temporal Awareness: [[_MEMORY/MEMORY-TEMPORAL]]
- Causal Reasoning: [[_MEMORY/MEMORY-CAUSAL]]
- Pre-Response Awareness Protocol: [[_MEMORY/MEMORY-AWARENESS]]
- Active Registry: [[_MEMORY/MEMORY-REGISTRY.json]]
- Prompt Stack: [[_PROMPTS/10_PRE-ACTION-AWARENESS]]
