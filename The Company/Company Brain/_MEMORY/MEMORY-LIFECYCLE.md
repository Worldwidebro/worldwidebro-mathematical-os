# MEMORY-LIFECYCLE — State Machine and Ingestion Pipeline

[[_MEMORY/MEMORY-OS|MEMORY-OS]] | [[_MEMORY/MEMORY-QUALITY|MEMORY-QUALITY]] | [[_MEMORY/MEMORY-DECAY|MEMORY-DECAY]] | [[STARTHERE]]

> **Canonical Document ID:** `MEM-LIF-001`  
> **Authority:** System Architecture & Infrastructure Control Plane (CP-027)

---

## 1. Memory State Machine

Every piece of information known to Company Brain progresses through an 8-state machine:

```text
[OBSERVATION / INTAKE]
          │
          ▼
     ( PROPOSED ) ───(Evidence threshold met)───> ( VALIDATED )
          │                                              │
          ▼ (No evidence)                                ▼
     ( REJECTED )                                ( CONSOLIDATED )
                                                         │
                                                         ▼
                                                    ( ACTIVE )
                                                         │
                                      ┌──────────────────┴──────────────────┐
                                      │ (Outdated / No signal)              │ (Contradicted)
                                      ▼                                     ▼
                                  ( STALE )                           ( CONFLICTED )
                                      │                                     │
                                      ▼                                     ▼
                                ( SUPERSEDED )                        ( DISPROVEN )
                                      │                                     │
                                      └──────────────────┬──────────────────┘
                                                         ▼
                                                    ( ARCHIVED )
```

---

## 2. State Definitions

1. **PROPOSED**: A newly asserted fact, relationship, or observation extracted from conversation or tool output.
2. **VALIDATED**: The proposed memory has been cross-referenced with empirical runtime evidence or authoritative documentation.
3. **CONSOLIDATED**: The memory has been integrated into the Neo4j graph or Qdrant vector index with proper schema, tags, and provenance.
4. **ACTIVE**: The current authoritative ground truth, available for context retrieval and agent routing.
5. **STALE**: The memory has exceeded its temporal validity window without re-verification. Marked for verification probe.
6. **CONFLICTED**: Direct contradiction detected between two active sources. Triggers priority reconciliation.
7. **SUPERSEDED**: Replaced by a newer, verified fact or decision (linked via `SUPERSEDED_BY` relationship).
8. **DISPROVEN**: Empirically refuted by runtime probe or operator command. Retained in historical audits with negative weight.
9. **ARCHIVED**: Cold-storage record preserved for auditability and compliance, excluded from active agent context.

---

## 3. Lifecycle Transitions & Guards

- **Guard (Proposed → Validated)**: Must possess valid `source_id`, `created_at`, and `confidence >= 0.70`.
- **Guard (Active → Stale)**: Automatic transition when `current_time - last_verified_at > validity_ttl`.
- **Guard (Any → Conflict)**: Triggered immediately by contradiction detection algorithms when semantic similarity is high but assertion values are contradictory.
