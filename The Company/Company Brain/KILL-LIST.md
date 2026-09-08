[[STARTHERE]] | [[REALITY]] | [[STOP-DOING]] | [[PRIORITIES]]

# KILL-LIST.md — Executable Pruning Governance

> **Canonical Document ID:** `DOC-KILL-001`  
> **Authority:** Sovereign Operator & Executive Governance (CP-006)  
> **Operating Law:** [`ANTIGRAVITY.md`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/ANTIGRAVITY.md) Rule #3: *No Fake Completion. "Done" requires verifiable executable proof.*

---

## Controlled Termination Decisions

```yaml
pruning_decisions:
  - id: "DEC-PRUNE-001"
    subject: "redundant_docker_stacks"
    decision: "CONSOLIDATE"
    owner: "CP-006"
    deadline: "2026-09-05"
    rationale: "Four overlapping compose projects (civos, t7shield, spinup, buzz) violate single-source-of-truth and waste memory."
    success_condition:
      neo4j_instances: 1
      qdrant_instances: 1
      postgres_instances: 1
      redis_instances: 1
      running_compose_stacks: 1
    execution_steps:
      - "docker --context macstudio compose -f /path/to/t7shield/docker-compose.yml down"
      - "docker --context macstudio compose -f /path/to/spinup/docker-compose.yml down"
      - "docker --context macstudio compose -f /path/to/buzz/docker-compose.yml down"
    evidence_required:
      - "docker --context macstudio ps --format '{{.Names}}\t{{.Ports}}'"
      - "docker --context macstudio compose ls"
    status: "CLOSED"
    closed_at: "2026-09-05T10:48:32-04:00"
    evidence_id: "EVD-011"

  - id: "DEC-PRUNE-002"
    subject: "crash_looping_neo4j_container"
    decision: "TERMINATE"
    owner: "CP-027"
    deadline: "2026-09-05"
    rationale: "t7shield-neo4j-1 fails on invalid Neo4j 4.x setting; civos_neo4j already serves canonical graph on 7474/7687."
    success_condition:
      container_t7shield_neo4j_running: false
    execution_steps:
      - "docker --context macstudio rm -f t7shield-neo4j-1"
    evidence_required:
      - "docker --context macstudio inspect t7shield-neo4j-1 (returns No such object or exit 1)"
    status: "CLOSED"
    closed_at: "2026-09-05T10:21:24-04:00"
    evidence_id: "EVD-010"

  - id: "DEC-PRUNE-003"
    subject: "speculative_venture_catalog"
    decision: "FREEZE_AND_ARCHIVE"
    owner: "CP-006"
    deadline: "2026-09-06"
    rationale: "Tracking 700 unmonetized ventures creates metrics theater and cognitive dilution."
    success_condition:
      active_ventures_count: 3
      archived_ventures_count: 697
    execution_steps:
      - "Create _ARCHIVE/COLD_STORAGE/VENTURES_FREEZE_2026.yaml"
      - "Retain top 3 viable commercial candidates in _REGISTRIES/VENTURE_REGISTRY.yaml"
    evidence_required:
      - "grep -c '^  - id: VEN-' _REGISTRIES/VENTURE_REGISTRY.yaml (equals 3)"
    status: "CLOSED"
    closed_at: "2026-09-05T10:54:34-04:00"
    evidence_id: "EVD-013"

  - id: "DEC-PRUNE-004"
    subject: "omniroute_antigravity_mcp_authentication"
    decision: "AUTHENTICATE_OR_DISABLE"
    owner: "CP-007"
    deadline: "2026-09-05"
    rationale: "All 110 MCP tools fail with HTTP 401 Unauthorized because bearer token is missing."
    success_condition:
      mcp_tool_omniroute_get_health_status: "200_OK"
    execution_steps:
      - "omniroute tokens create antigravity --scope manage"
      - "Inject token into ~/.gemini/config/mcp_config.json under env.OMNIROUTE_API_KEY"
    evidence_required:
      - "call_mcp_tool: omniroute_get_health (returns valid uptime and version without 401)"
    status: "CLOSED"
    closed_at: "2026-09-05T10:04:46-04:00"
    evidence_id: "EVD-012"

  - id: "DEC-PRUNE-005"
    subject: "uncompressed_tool_token_waste"
    decision: "ENABLE_RTK_CAVEMAN"
    owner: "CP-007"
    deadline: "2026-09-06"
    rationale: "Raw terminal/build/git logs consume 100k+ tokens per agent turn without compression."
    success_condition:
      stacked_compression_active: true
      average_token_savings: "> 60%"
    execution_steps:
      - "Configure OmniRoute compression mode to 'stacked' (rtk -> caveman)"
    evidence_required:
      - "omniroute compression status (reports mode: stacked, rtk: active, caveman: active)"
    status: "OPEN"
```

---

## Verification Audit Policy
A pruning decision cannot be marked `CLOSED` without committing the raw shell output of `evidence_required` to [`EVIDENCE.md`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/EVIDENCE.md).
