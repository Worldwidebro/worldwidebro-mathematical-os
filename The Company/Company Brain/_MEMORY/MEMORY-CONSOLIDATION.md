# MEMORY-CONSOLIDATION — Consolidation and Learning Engine

[[_MEMORY/MEMORY-OS|MEMORY-OS]] | [[_MEMORY/MEMORY-LIFECYCLE|MEMORY-LIFECYCLE]] | [[_PROMPTS/08_MEMORY-CONSOLIDATION|08_MEMORY-CONSOLIDATION]] | [[STARTHERE]]

> **Canonical Document ID:** `MEM-CON-001`  
> **Authority:** System Architecture & Infrastructure Control Plane (CP-027)

---

## 1. The Consolidation Pipeline

Not every chat message or shell output deserves permanent storage. Consolidation is the process of extracting high-value, reusable knowledge from ephemeral working sessions and crystallizing it into semantic facts and procedural rules.

```text
┌────────────────────────────────────────────────────────┐
│ 1. RAW INTERACTION                                     │
│    User prompts, tool outputs, terminal logs           │
└───────────────────────────┬────────────────────────────┘
                            ▼
┌────────────────────────────────────────────────────────┐
│ 2. EPISODE                                             │
│    Structured narrative: goal, action, outcome         │
└───────────────────────────┬────────────────────────────┘
                            ▼
┌────────────────────────────────────────────────────────┐
│ 3. OBSERVATION                                         │
│    Specific delta finding (e.g. "port 20128 is open")  │
└───────────────────────────┬────────────────────────────┘
                            ▼
┌────────────────────────────────────────────────────────┐
│ 4. PATTERN                                             │
│    Repeated occurrence across 2+ episodes              │
└───────────────────────────┬────────────────────────────┘
                            ▼
┌────────────────────────────────────────────────────────┐
│ 5. FACT                                                │
│    Verified truth about an entity, system, or repo     │
└───────────────────────────┬────────────────────────────┘
                            ▼
┌────────────────────────────────────────────────────────┐
│ 6. RULE / PROCEDURE                                    │
│    Codified standard in .agents/skills/ or ANTIGRAVITY │
└────────────────────────────────────────────────────────┘
```

---

## 2. Post-Action Consolidation Criteria

An event is eligible for consolidation into long-term memory if it satisfies at least one of these criteria:

1. **Resolution of an Incident**: A root cause was identified and remediated.
2. **Infrastructure Mutation**: A service was deployed, updated, moved, or decommissioned.
3. **Registry Update**: A venture status, repository dependency, or capability link changed.
4. **Architectural Decision (ADR)**: A significant design decision was locked with trade-offs.
5. **Operator Preference**: The Sovereign Operator explicitly corrected an assumption or expressed a workflow rule.

---

## 3. Consolidation Payload Schema

When an agent triggers consolidation at the end of a milestone or turn, it emits:

```json
{
  "consolidation_id": "CONSOL-20260905-001",
  "source_session": "59e824c1-3b2a-48b7-9b62-d499546cadce",
  "facts_established": [
    {
      "entity_id": "SYS-OMNIROUTE-001",
      "fact": "OmniRoute daemon runs locally on port 20128 via com.omniroute.server.plist",
      "truth_state": "VERIFIED",
      "confidence": 1.0
    }
  ],
  "procedural_rules_learned": [
    {
      "rule": "OmniRoute FastMCP wrapper must filter console.debug lines from stdout to prevent JSON-RPC parse errors",
      "target_file": "/Users/acebless/.omniroute/bin/antigravity-mcp.mjs"
    }
  ],
  "graph_mutations": [
    "MERGE (a:System {id: 'SYS-OMNIROUTE-001'})-[:CONNECTS_TO]->(b:Provider {id: 'OLLAMA-LOCAL'})"
  ]
}
```
