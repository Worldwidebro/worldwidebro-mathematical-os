[[STARTHERE]] | [[REALITY]] | [[ASSUMPTIONS]]

# CLAIMS.md — The System Knowledge Claims Ledger

> **Canonical Document ID:** `DOC-CLM-001`  
> **Authority:** Knowledge Control Plane (CP-013) & Ontology Architecture (CP-027)  
> **Ontology Standard:** [`_ONTOLOGY/TRUTH_STATUS.yaml`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/_ONTOLOGY/TRUTH_STATUS.yaml)  
> **Rule:** *A fact is not a belief. Every assertion must have a discrete status, evidence link, and owner.*

---

## 1. Active System Claims

```yaml
claims:
  - id: "CLM-001"
    statement: "Company Brain has 887 owned repositories cataloged"
    status: "VERIFIED"
    evidence: "EVD-001"
    source: "SRC-GITHUB-001"
    observed_at: "2026-09-05"
    owner: "CP-006"
    expires_at: "2026-10-05"
    consequence: []

  - id: "CLM-002"
    statement: "We operate 700 commercial companies"
    status: "DISPROVEN"
    evidence: "EVD-002"
    source: "SRC-REALITY-001"
    observed_at: "2026-09-05"
    owner: "CP-006"
    expires_at: "permanent"
    consequence:
      - "reclassify_venture_registry"
      - "freeze_690_ventures_to_cold_storage"

  - id: "CLM-003"
    statement: "Mac Studio M4 Max is online and serving as primary inference node"
    status: "VERIFIED"
    evidence: "EVD-003"
    source: "SRC-TAILSCALE-001"
    observed_at: "2026-09-05"
    owner: "CP-027"
    expires_at: "2026-09-06"
    consequence: []

  - id: "CLM-004"
    statement: "OmniRoute actively routes requests for Antigravity and CLI agents"
    status: "CONFLICTED"
    evidence: "EVD-004"
    source: "SRC-MCP-AUDIT-001"
    observed_at: "2026-09-05"
    owner: "CP-007"
    expires_at: "2026-09-06"
    consequence:
      - "generate_antigravity_bearer_token"
      - "run_omniroute_configure_for_clis"

  - id: "CLM-005"
    statement: "civos_neo4j is healthy and serving canonical graph queries"
    status: "VERIFIED"
    evidence: "EVD-005"
    source: "SRC-DOCKER-001"
    observed_at: "2026-09-05"
    owner: "CP-013"
    expires_at: "2026-09-06"
    consequence: []

  - id: "CLM-006"
    statement: "LiteLLM utilizes intelligent scoring across cost, latency, and quality"
    status: "DISPROVEN"
    evidence: "EVD-006"
    source: "SRC-LITELLM-CONFIG-001"
    observed_at: "2026-09-05"
    owner: "CP-007"
    expires_at: "permanent"
    consequence:
      - "upgrade_litellm_routing_strategy_or_route_via_omniroute"

  - id: "CLM-007"
    statement: "Mac Studio runs 4 competing Docker compose stacks with duplicate databases"
    status: "VERIFIED"
    evidence: "EVD-007"
    source: "SRC-DOCKER-001"
    observed_at: "2026-09-05"
    owner: "CP-027"
    expires_at: "2026-09-06"
    consequence:
      - "execute_DEC_PRUNE_001"

  - id: "CLM-008"
    statement: "t7shield-neo4j-1 is crash-looping due to legacy 4.x configuration"
    status: "VERIFIED"
    evidence: "EVD-008"
    source: "SRC-DOCKER-001"
    observed_at: "2026-09-05"
    owner: "CP-027"
    expires_at: "2026-09-06"
    consequence:
      - "execute_DEC_PRUNE_002"

  - id: "CLM-009"
    statement: "Company Brain generated external revenue in the last 30 days"
    status: "DISPROVEN"
    evidence: "EVD-009"
    source: "SRC-BANK-STRIPE-001"
    observed_at: "2026-09-05"
    owner: "CP-020"
    expires_at: "2026-10-01"
    consequence:
      - "freeze_non_commercial_coding"
      - "launch_b2b_infrastructure_audit_offer"
```

---

## 2. Dynamic Truth Auditing Queries

### Query 1: Show every claim that contradicts REALITY.md
```text
STATUS == DISPROVEN OR STATUS == CONFLICTED
```
*Current count: 3 claims (`CLM-002`, `CLM-004`, `CLM-006`, `CLM-009`)*

### Query 2: Show every claim whose verification has expired
```text
EXPIRES_AT < CURRENT_TIMESTAMP
```
