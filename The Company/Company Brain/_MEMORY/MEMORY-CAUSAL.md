# MEMORY-CAUSAL — Causal Chains and Consequence Modeling

[[_MEMORY/MEMORY-OS|MEMORY-OS]] | [[_MEMORY/MEMORY-RELATIONSHIPS|MEMORY-RELATIONSHIPS]] | [[ANTIGRAVITY]] | [[STARTHERE]]

> **Canonical Document ID:** `MEM-CAU-001`  
> **Authority:** System Architecture & Infrastructure Control Plane (CP-027)

---

## 1. Causal Reasoning vs Correlation

Simple semantic retrieval surfaces items that "look alike." Causal memory models *why* things happen, tracking:
> **`CAUSE ──> EVENT ──> DECISION ──> ACTION ──> OUTCOME ──> CONSEQUENCE`**

And reverse traversal:
> **`OUTCOME <── ACTION <── DECISION <── CAUSE`**

---

## 2. Pre-Action Causal Modeling

Before executing any modifying tool, file write, or shell command:
1. **Identify Upstream Drivers**: What goal, rule, or failure prompted this action?
2. **Predict First-Order Effects**: What file, database record, or service changes directly?
3. **Predict Second-Order Effects**: What downstream repositories, subagents, or users depend on that state?
4. **Evaluate Blast Radius**: If this action fails, what breaks? Can it be safely reverted?

---

## 3. Post-Action Causal Attribution

When a failure or success occurs:
1. **Do not blame symptoms**: If a build fails, do not merely report "build error"; trace back to the exact code mutation, dependency version drift, or environment difference that caused it.
2. **Record Causal Link in Neo4j**:
   ```cypher
   CREATE (f:Failure {id: 'FAIL-001', desc: 'JSON-RPC parse error'})
   CREATE (c:RootCause {desc: 'better-sqlite3 logged debug message to stdout'})
   CREATE (f)-[:CAUSED_BY]->(c)
   CREATE (s:Solution {desc: 'Filtered stdout in antigravity-mcp.mjs'})
   CREATE (s)-[:RESOLVED]->(f);
   ```
