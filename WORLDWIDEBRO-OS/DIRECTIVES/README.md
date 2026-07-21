# Directive Layer: AI Boss OS Operating Constitution

**Purpose:** Translate executive intent into rules, priorities, constraints, and actions

**Audience:** All agents, all ventures, all operators

**Authority:** Set by Executive Layer, enforced by Operating Systems

**Mirror of:** `github.com/Worldwidebro/worldwidebro-directives` (source of truth)

---

## What This Layer Does

Directives are the **operating manual** every venture inherits:

1. **How decisions are made** — Approval matrix, authority tiers
2. **What builds what** — Building standards, deployment rules
3. **What succeeds** — Metrics, KPIs
4. **What's sacred** — Non-negotiable constraints
5. **What's prioritized** — Resource allocation
6. **What's allowed** — Scope boundaries

---

## Structure

```
DIRECTIVES/
├── README.md (this)
├── NORTH-STAR-DIRECTIVE.md
├── STRATEGIC-DIRECTIVES/
│   ├── GROWTH-DIRECTIVE.md
│   ├── REVENUE-DIRECTIVE.md
│   ├── INNOVATION-DIRECTIVE.md
│   ├── AI-DIRECTIVE.md
│   └── SCALE-DIRECTIVE.md
├── OPERATING-DIRECTIVES/
│   ├── BUILD-RULES.md
│   ├── DEPLOYMENT-RULES.md
│   ├── QUALITY-STANDARDS.md
│   ├── SECURITY-RULES.md
│   ├── DOCUMENTATION-RULES.md
│   └── OBSERVABILITY-DIRECTIVE.md
├── VENTURE-DIRECTIVES/
│   ├── VENTURE-CREATION-RULES.md
│   ├── MARKET-SELECTION.md
│   ├── VALIDATION-RULES.md
│   ├── FUNDING-RULES.md
│   └── EXIT-RULES.md
├── AI-DIRECTIVES/
│   ├── AGENT-BEHAVIOR.md
│   ├── MODEL-SELECTION.md
│   ├── TOOL-USAGE.md
│   ├── MEMORY-POLICY.md
│   └── SAFETY-CONSTRAINTS.md
├── PRIORITY/
│   ├── CURRENT-PRIORITIES.md
│   ├── BACKLOG-RANKING.md
│   ├── RESOURCE-ALLOCATION.md
│   └── TRADEOFF-RULES.md
└── DECISIONS/
    ├── DECISION-PROTOCOL.md
    ├── APPROVAL-MATRIX.md
    ├── ESCALATION-RULES.md
    └── DECISION-HISTORY.md
```

---

## Example: OBSERVABILITY-DIRECTIVE

This directive fixes the "needs attention" items:

```yaml
id: AIBOS-DIR-OBS-001
name: Observability Directive
objective: Complete real-time visibility into all systems
priority: P1 (Critical)
owner: CTO

rules:
  # Prometheus Wiring
  - Prometheus MUST scrape all services in real-time
  - Every tool/agent/service must expose /metrics endpoint
  - Prometheus targets updated quarterly
  
  # Grafana Dashboards
  - Grafana login credentials reset (admin password managed by CTO)
  - CEO dashboard MUST show: ventures, revenue, health, risks
  - CFO dashboard MUST show: MRR, ARR, runway, unit economics
  - CTO dashboard MUST show: deployment success, error rates, latency
  
  # LiteLLM Routing
  - LiteLLM health checked every 5 minutes
  - All agent calls traced via Langfuse
  - Cost tracking per venture, per agent, per model
  
  # exo Clustering
  - exo cluster MUST connect Mac Studio + MacBook Air
  - Distributed inference routing per task complexity
  - Fallback to cloud (Claude) if exo unavailable

metrics:
  - Prometheus targets healthy: 5/5
  - Grafana dashboards live: 3/3
  - Langfuse traces per day: 10,000+
  - Agent latency p95: <3 seconds
  - System uptime: 99.9%

deadline: 2026-07-30
```

---

## How Directives Flow Down

```
EXECUTIVE LAYER
   "Make all systems observable"
         ↓
OBSERVABILITY-DIRECTIVE
   "Wire Prometheus, Grafana, fix auth, cluster exo"
         ↓
OPERATING-DIRECTIVES (CTO)
   "Every tool MUST expose /metrics"
   "Dashboard must show venture health"
         ↓
AI-DIRECTIVES (Agents)
   "All LLM calls trace to Langfuse"
   "Route to exo if available"
         ↓
TOOL-INTEGRATION-ARCHITECTURE
   "Map all services to their metrics endpoints"
         ↓
AGENT EXECUTION
   "Implement metrics collection per directive"
         ↓
ALL 712 VENTURES
   "Inherit observability rules"
```

---

## Directive Types

| Type | Horizon | Owner | Example |
|---|---|---|---|
| Strategic | 1-3 years | CEO | Growth Directive |
| Operating | Ongoing | CTO/COO | Build Rules, Deployment Rules |
| Venture | Lifecycle | Portfolio Manager | Market Selection |
| AI | Ongoing | CTO | Agent Behavior, Safety |
| Priority | Current quarter | CEO + CFO | Current Priorities |
| Decision | Ongoing | Each role | Approval Matrix |

---

## Authority Matrix

| Decision | Authority | Process |
|---|---|---|
| <$5K | Venture founder | Direct execute |
| $5K-$25K | Director | Request + approval |
| >$25K | Hermes + CEO | Reasoning + approval |
| Irreversible | CEO | Full authority |
| Strategic | Board | Quarterly |
| Directive changes | Executive team | Approved + synced |

---

## This Is The Constitution

Changes here cascade to all 712 ventures automatically.

When you update a Directive, all ventures inherit it.

This is how 712 separate ventures act as **one unified system**.

---

## How to Use

1. **Know your directive** — Find it in the structure above
2. **Understand your role** — What's YOUR responsibility?
3. **Follow the rules** — Execute per directive
4. **Escalate if unclear** — Use DECISION-PROTOCOL.md
5. **Log outcomes** — Contribute to DECISION-HISTORY.md

---

*Source of truth: github.com/Worldwidebro/worldwidebro-directives*  
*This is your operating manual. All 712 ventures follow it equally.*
