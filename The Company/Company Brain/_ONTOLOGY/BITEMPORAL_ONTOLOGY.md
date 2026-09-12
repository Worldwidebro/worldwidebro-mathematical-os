---
id: ONT-BITEMPORAL-001
title: Bitemporal Knowledge Graph Ontology & Execution Gates
aliases: ["BITEMPORAL_ONTOLOGY", "Bitemporal Graph", "CAP-TEMPORAL-KNOWLEDGE", "Utopia Ontology"]
tags: [ontology, bitemporal, neo4j, knowledge-graph, utopia]
status: ACTIVE
updated: 2026-09-12
---

[[STARTHERE]] | [[REALITY]] | [[08-KNOWLEDGE-GRAPH]] | [[_ONTOLOGY/OBJECT_TYPES|OBJECT_TYPES]] | [[INDEX]]

# ⏳ Bitemporal Knowledge Graph Ontology & Execution Gates

**Authority:** CP-004 (Data & Knowledge) & CP-027 (Infrastructure)  
**Status:** ✅ `EXTRACTED & ACTIVE`  
**Gap Resolution:** Resolves `CAP-TEMPORAL-KNOWLEDGE` utilizing starred repository [`deeplethe/utopia`](https://github.com/deeplethe/utopia) (1,240 ★).

---

## 1. Bitemporal Coordinate System
To prevent financial and audit hallucinations, every entity state in Company Brain's Neo4j graph is tracked across two independent time axes:
1. **Valid Time ($T_v$):** When the event actually occurred in the real world (e.g. effective date of a commercial contract or loan draw).
2. **Transaction Time ($T_t$):** When the record was ingested into Company Brain (e.g. database commit timestamp).

```text
               Transaction Time (Record Ingestion)
                     ▲
                     │     State B (Modified record)
                     │     [valid_from, valid_to]
                     │
                     │     State A (Original record)
                     │     [valid_from, valid_to]
                     └────────────────────────────────► Valid Time (Real World Reality)
```

---

## 2. Neo4j Cypher Implementation
All temporal nodes (`VentureState`, `FinancialLedger`, `ContractExecution`) adhere to bitemporal properties:

```cypher
// Bitemporal constraint verification
CREATE CONSTRAINT venture_state_temporal IF NOT EXISTS
FOR (s:VentureState) REQUIRE (s.valid_from, s.valid_to, s.system_from, s.system_to) IS NOT NULL;

// Querying the true state of a venture as of an audit date:
MATCH (v:Venture {id: "LT-005"})-[:HAS_STATE]->(s:VentureState)
WHERE s.valid_from <= datetime("2026-09-01T00:00:00Z") < s.valid_to
  AND s.system_from <= datetime("2026-09-12T00:00:00Z") < s.system_to
RETURN s.revenue, s.active_fleet, s.compliance_status;
```

---

## 3. Financial Agent Execution Gates
Before any agent (Hermes or OpenHands) triggers a payout, bank transfer, or capital commitment:
- **Gate 1 (Temporal Precedence):** The transaction valid-time must match current or historical time ($T_v \le \text{now}$).
- **Gate 2 (Dual Approval):** Commitments exceeding \$10,000 require human-in-the-loop co-signing recorded in Neo4j.
