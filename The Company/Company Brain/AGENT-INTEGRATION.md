# AGENT-INTEGRATION.md — Autonomous Agent Fleet Integration & Governance

**Authority:** Multi-Agent Coordination Control Plane (CP-016)  
**Protocol:** Google Agent2Agent (A2A) v1.0 / JSON-RPC 2.0 & FastMCP  
**Status:** `VERIFIED_OPERATIONAL`  

---

## 1. Fleet Architecture

```text
                                  ┌────────────────────────┐
                                  │   ANTIGRAVITY / USER   │
                                  │     North Star Owner   │
                                  └───────────┬────────────┘
                                              │
                                              ▼
                                  ┌────────────────────────┐
                                  │ @orchestrator          │
                                  │ Leader of the Pipeline │
                                  └───────────┬────────────┘
                     ┌────────────────────────┼────────────────────────┐
                     │                        │                        │
                     ▼                        ▼                        ▼
           ┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐
           │ @architect       │     │ @qa-engineer     │     │ @deal-strategist │
           │ System Contracts │     │ Reality Auditor  │     │ MEDDPICC & Cash  │
           └──────────────────┘     └──────────────────┘     └──────────────────┘
```

---

## 2. Core Agent Roles & Capability Contracts

### 2.1 Lead Orchestrator (`@orchestrator`)
- **Purpose:** Owns the multi-step execution pipeline from requirement to production deployment.
- **Assigned Tools:** `omniroute_route_request`, `infrastructure_status`, `manage_subagents`, `run_command`.
- **Inputs:** High-level strategic directives, venture goals, revenue milestones.
- **Outputs:** Coordinated subagent tasks, verification reports, Git pull requests.
- **Approval Gate:** Human authorization required before any destructive deployment or registry overhaul.

### 2.2 Reality Auditor & Test Gatekeeper (`@qa-engineer` / `@reality-checker`)
- **Purpose:** Prevents fantasy approvals. Requires empirical proof (terminal exit codes, live HTTP payloads, screenshots).
- **Assigned Tools:** `test_e2e`, `browseros-neo` (visual audits), `run_command` (automated test runs).
- **Hard Rule:** Rejects any claim of "Done" or "Production Ready" lacking execution output.

### 2.3 Inference Router Agent (`OmniRoute A2A`)
- **Endpoint:** `POST http://localhost:20128/a2a`
- **Native Skills:**
  1. `smart-routing`: Routes coding and research requests to fastest/cheapest models.
  2. `quota-management`: Tracks API rate limits across 36+ providers with auto-fallback.
  3. `provider-discovery`: Detects active local/remote inference endpoints (Ollama, Exo, OpenAI).
  4. `cost-analysis`: Telemetry and expenditure breakdowns.
  5. `health-report`: Circuit breaker status and degraded endpoint notifications.
  6. `list-capabilities`: Service catalog discovery.

---

## 3. Escalation & Audit Rules

1. **Revenue Gate Enforcement ([`REVENUE_GATE.md`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/.agents/rules/REVENUE_GATE.md)):**
   - Agents must freeze meta-work on non-core ventures and focus exclusively on Tier-0 ventures (`OPS-001`, `LT-005`, `CALLCENTER`) with distance-to-cash <= 48 hours.
2. **Audit Logging:**
   - Every agent interaction is captured in local conversation transcripts (`transcript.jsonl`) with tool calls, latency, thinking blocks, and output payloads.
