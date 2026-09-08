# MEMORY-PROVENANCE — Traceability and Lineage Standards

[[_MEMORY/MEMORY-OS|MEMORY-OS]] | [[_MEMORY/MEMORY-QUALITY|MEMORY-QUALITY]] | [[_PROMPTS/07_PROVENANCE-VERIFICATION|07_PROVENANCE-VERIFICATION]] | [[STARTHERE]]

> **Canonical Document ID:** `MEM-PRV-001`  
> **Authority:** System Architecture & Infrastructure Control Plane (CP-027)

---

## 1. The Core Standard

Every non-ephemeral memory item must answer:
> **“Why do you believe that?”**

If an agent or system cannot produce the exact provenance chain for a claim, the claim is demoted to `ASSUMED` or `UNKNOWN`.

---

## 2. Provenance Metadata Schema

All memory nodes must be annotated with this metadata payload:

```yaml
provenance:
  source_id: "SESSION-59e824c1-3b2a-48b7-9b62-d499546cadce"
  source_type: "RUNTIME_PROBE" # [RUNTIME_PROBE, OPERATOR_DIRECTIVE, GIT_COMMIT, CANONICAL_REGISTRY, THIRD_PARTY_API]
  created_at: "2026-09-05T10:45:00Z"
  observed_at: "2026-09-05T10:45:00Z"
  verified_at: "2026-09-05T10:46:12Z"
  author: "Antigravity-Agent-01"
  confidence: 0.98
  evidence: "curl -s http://localhost:20128/api/v1/health returned status 200 OK"
  derived_from:
    - "LAUNCHAGENT-com.omniroute.server.plist"
    - "SCRIPT-/Users/acebless/.omniroute/bin/antigravity-mcp.mjs"
```

---

## 3. Provenance Hierarchy

When two memories conflict, authority is resolved strictly by this hierarchy:
1. **Sovereign Operator Direct Order** (Highest authority).
2. **Empirical Runtime Probe** (e.g. active curl, docker ps, live test exit code).
3. **Canonical Registry File** (`_REGISTRIES/CANONICAL/*.yaml`).
4. **Git Versioned Markdown Specification**.
5. **Session Transcripts / Historical Episodic Logs**.
6. **Inferred Agent Deduction** (Lowest authority).
