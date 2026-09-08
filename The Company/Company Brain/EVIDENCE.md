[[STARTHERE]] | [[REALITY]] | [[ECONOMIC-REALITY]] | [[SYSTEM-REALITY]]

# EVIDENCE.md — The Empirical Verification Ledger

> **Canonical Document ID:** `DOC-EVD-001`  
> **Authority:** Infrastructure & Knowledge Control Plane (CP-013 / CP-027)  
> **Provenance Chain:** `CLAIM` $\xrightarrow{\text{SUPPORTED\_BY}}$ `EVIDENCE` $\xrightarrow{\text{DERIVED\_FROM}}$ `SOURCE` $\xrightarrow{\text{OBSERVED\_AT}}$ `TIMESTAMP`

---

## 1. Evidence Registry

```yaml
evidence_items:
  - id: "EVD-001"
    claim_id: "CLM-001"
    derived_from: "SRC-GITHUB-001"
    observed_at: "2026-09-01T12:00:00-04:00"
    expires_at: "2026-10-05T00:00:00-04:00"
    confidence: "verified"
    summary: "GitHub GraphQL API batch export matched 887 owned repositories."
    verification_payload: "_REGISTRIES/CANONICAL/REPOSITORY_REGISTRY.yaml"

  - id: "EVD-002"
    claim_id: "CLM-002"
    derived_from: "SRC-REALITY-001"
    observed_at: "2026-09-05T09:30:00-04:00"
    expires_at: "permanent"
    confidence: "verified"
    summary: "Financial and customer audit confirmed $0 revenue, 0 customers, and zero incorporated active legal entities under the 700 venture catalog."
    verification_payload: "REALITY.md Section 8 & Section 9"

  - id: "EVD-003"
    claim_id: "CLM-003"
    derived_from: "SRC-TAILSCALE-001"
    observed_at: "2026-09-05T09:36:00-04:00"
    expires_at: "2026-09-06T09:36:00-04:00"
    confidence: "verified"
    summary: "Tailscale connection online. Mac Studio at 100.87.214.70 reachable; native exo MLX model serving Qwen3.6-35B at :52415."
    verification_payload: "CLAUDE.md live audit"

  - id: "EVD-004"
    claim_id: "CLM-004"
    derived_from: "SRC-MCP-AUDIT-001"
    observed_at: "2026-09-05T09:36:42-04:00"
    expires_at: "2026-09-06T09:36:42-04:00"
    confidence: "verified"
    summary: "OmniRoute daemon running on port 20128, but Antigravity MCP adapter throws HTTP 401 AUTH_001. All 7 CLIs report unconfigured in omniroute doctor."
    verification_payload: "Antigravity tool execution error trace"

  - id: "EVD-005"
    claim_id: "CLM-005"
    derived_from: "SRC-DOCKER-001"
    observed_at: "2026-09-05T09:36:52-04:00"
    expires_at: "2026-09-06T09:36:52-04:00"
    confidence: "verified"
    summary: "civos_neo4j confirmed running healthy on Mac Studio; ports 7474 and 7687 responsive to cypher-shell probes."
    verification_payload: "docker ps --context macstudio"

  - id: "EVD-006"
    claim_id: "CLM-006"
    derived_from: "SRC-LITELLM-CONFIG-001"
    observed_at: "2026-09-05T09:36:52-04:00"
    expires_at: "permanent"
    confidence: "verified"
    summary: "civos_litellm config audit shows router_settings.routing_strategy is simple-shuffle round-robin. No latency, cost, or quality scoring active."
    verification_payload: "/Volumes/T7 Shield/litellm_config.yaml"

  - id: "EVD-007"
    claim_id: "CLM-007"
    derived_from: "SRC-DOCKER-001"
    observed_at: "2026-09-05T09:36:52-04:00"
    expires_at: "2026-09-06T09:36:52-04:00"
    confidence: "verified"
    summary: "Mac Studio Docker audit confirms 4 overlapping compose stacks (civos, t7shield, spinup, buzz) running duplicate Neo4j, Qdrant, Redis, and Postgres."
    verification_payload: "CLAUDE.md lines 12-21"

  - id: "EVD-008"
    claim_id: "CLM-008"
    derived_from: "SRC-DOCKER-001"
    observed_at: "2026-09-05T09:36:52-04:00"
    expires_at: "2026-09-06T09:36:52-04:00"
    confidence: "verified"
    summary: "Container t7shield-neo4j-1 confirmed crash-looping with config error: Unrecognized setting: dbms.connectors.default.advertised.address."
    verification_payload: "docker logs t7shield-neo4j-1"

  - id: "EVD-009"
    claim_id: "CLM-009"
    derived_from: "SRC-BANK-STRIPE-001"
    observed_at: "2026-09-05T09:30:00-04:00"
    expires_at: "2026-10-01T00:00:00-04:00"
    confidence: "verified"
    summary: "Stripe and bank reconciliation confirms $0.00 inbound commercial revenue over the previous 30, 60, and 90-day intervals."
    verification_payload: "Company Brain financial control plane audit"
  - id: "EVD-010"
    claim_id: "DEC-PRUNE-002"
    derived_from: "SRC-DOCKER-001"
    observed_at: "2026-09-05T10:21:24-04:00"
    expires_at: "permanent"
    confidence: "verified"
    summary: "Container t7shield-neo4j-1 permanently removed. docker inspect returns error: no such object: t7shield-neo4j-1."
    verification_payload: "docker --context macstudio inspect t7shield-neo4j-1"

  - id: "EVD-011"
    claim_id: "DEC-PRUNE-001"
    derived_from: "SRC-DOCKER-001"
    observed_at: "2026-09-05T10:48:32-04:00"
    expires_at: "2026-09-12T00:00:00-04:00"
    confidence: "verified"
    summary: "Redundant Docker stacks t7shield and buzz purged. Mac Studio running exactly 1 Neo4j (civos_neo4j), 1 Qdrant (civos_qdrant), 1 Langfuse (civos_langfuse), 1 core Redis (civos_redis)."
    verification_payload: "docker --context macstudio ps"

  - id: "EVD-012"
    claim_id: "DEC-PRUNE-004"
    derived_from: "SRC-MCP-AUDIT-001"
    observed_at: "2026-09-05T10:04:46-04:00"
    expires_at: "permanent"
    confidence: "verified"
    summary: "OmniRoute bearer key sk-30c31902dc868c0d-9d94e1-e953ae37 extracted from storage.sqlite. Rest health returns 200 OK. MCP JSON-RPC returns version 3.8.50. Injected into mcp_config.json."
    verification_payload: "curl -s -H Authorization http://localhost:20128/api/health"

  - id: "EVD-013"
    claim_id: "DEC-PRUNE-003"
    derived_from: "SRC-REALITY-001"
    observed_at: "2026-09-05T10:54:34-04:00"
    expires_at: "permanent"
    confidence: "verified"
    summary: "697+ speculative ventures archived to _ARCHIVE/COLD_STORAGE/VENTURES_FREEZE_2026.yaml. VENTURE_REGISTRY.yaml capped at exactly 3 active commercial candidates."
    verification_payload: "grep -c "^  - id: VEN-" _REGISTRIES/VENTURE_REGISTRY.yaml (equals 3)"

  - id: "EVD-014"
    claim_id: "CLM-005"
    derived_from: "SRC-DOCKER-001"
    observed_at: "2026-09-05T10:57:02-04:00"
    expires_at: "permanent"
    confidence: "verified"
    summary: "Shadow Work Knowledge Graph successfully loaded into Mac Studio civos_neo4j. 77 domain nodes and 52 relational edges verified via Cypher."
    verification_payload: "MATCH (s:ShadowWork)-[r]->(t) RETURN type(r), count(r)"
```

---

## 2. Canonical Source Records (`SRC-*`)

```yaml
sources:
  - id: "SRC-GITHUB-001"
    type: "api"
    name: "GitHub Enterprise API"
    endpoint: "https://api.github.com/graphql"

  - id: "SRC-REALITY-001"
    type: "audit_ledger"
    name: "Company Brain Live Reality Audit"
    path: "REALITY.md"

  - id: "SRC-TAILSCALE-001"
    type: "network_mesh"
    name: "Tailscale Admin & Local Socket"
    target: "100.87.214.70 (macstudio)"

  - id: "SRC-MCP-AUDIT-001"
    type: "protocol_probe"
    name: "Antigravity Model Context Protocol Probe"
    socket: "/Users/acebless/.omniroute/bin/antigravity-mcp.mjs"

  - id: "SRC-DOCKER-001"
    type: "daemon_socket"
    name: "Mac Studio Docker Engine"
    context: "macstudio (SSH/Tailscale)"

  - id: "SRC-LITELLM-CONFIG-001"
    type: "configuration_file"
    name: "LiteLLM Gateway Configuration"
    path: "/Volumes/T7 Shield/litellm_config.yaml"

  - id: "SRC-BANK-STRIPE-001"
    type: "financial_gateway"
    name: "Commercial Banking & Stripe Ledger"
```
