---
references:
  - [[unified-os-architecture]]
  - [[AGENTS.md]]
  - [[DEPARTMENTS.md]]
---

# TEAMS.md — Team Structure & Escalation Paths

## Principles

**Mapping:** Each team's roles and escalation paths are explicit and traceable.
**Planning:** Team structure follows POLC: Planning authority (manager), Organizing resources (team lead), Leading execution (agent leads), Controlling outcomes (weekly reviews).
**Roadmapping:** Teams grow as agent success rates increase; hiring follows autonomous capacity.

---

## Team Structure by OPCO

### Construction (CON)

| Role | Name | Reports To | Authority | Team Size |
|------|------|-----------|-----------|-----------|
| **Director** | TBD | CEO | $150K/mo revenue goal | 1 |
| **Operations Manager** | TBD | Director | Venture execution, agent oversight | 1 |
| **Lead Estimator** | TBD (human or agent) | Ops Manager | estimator_gen1 supervision, bid review | 1 |
| **Venture Lead** | varies | Ops Manager | Project delivery per venture | 2–4 |

**Escalation Path:** Venture Lead → Ops Manager → Director

**Decision Authority:**
- **Lead Estimator:** Approve estimates <$50K (without estimator_gen1)
- **Ops Manager:** Approve ventures <$10K MRR, escalate >$10K to Director
- **Director:** Approve new ventures, staffing decisions

---

### Staffing (STA)

| Role | Name | Reports To | Authority | Team Size |
|------|------|-----------|-----------|-----------|
| **Director** | TBD | CEO | $100K/mo revenue goal | 1 |
| **Operations Manager** | TBD | Director | Contractor supply, agent training | 1 |
| **Matching Lead** | TBD (human) | Ops Manager | candidate_matcher supervision | 1 |
| **Availability Coordinator** | TBD (human or agent) | Ops Manager | Shift scheduling, conflict resolution | 1 |

**Escalation Path:** Availability Coordinator → Matching Lead → Ops Manager → Director

**Decision Authority:**
- **Matching Lead:** Approve matches <$20/hr rate difference
- **Ops Manager:** Approve contractors <$5K/mo, escalate >$5K to Director
- **Director:** Approve new contractor tiers, partnership decisions

---

### Real Estate (RE)

| Role | Name | Reports To | Authority | Team Size |
|------|------|-----------|-----------|-----------|
| **Director** | TBD | CEO | $120K/mo revenue goal | 1 |
| **Sales Manager** | TBD | Director | Lead pipeline, closing | 1 |
| **Valuation Specialist** | TBD (human or agent) | Sales Manager | property_valuer supervision | 1 |
| **Lead Qualifier** | TBD (human or agent) | Sales Manager | lead_qualifier supervision, outreach | 1 |

**Escalation Path:** Lead Qualifier → Valuation Specialist → Sales Manager → Director

**Decision Authority:**
- **Valuation Specialist:** Approve valuations <$500K
- **Sales Manager:** Approve deals <$50K commission, escalate >$50K to Director
- **Director:** Approve new market entry, partnership terms

---

### Education (EDU)

| Role | Name | Reports To | Authority | Team Size |
|------|------|-----------|-----------|-----------|
| **Director** | TBD | CEO | $80K/mo revenue goal | 1 |
| **Content Manager** | TBD | Director | Curriculum development, QA | 1 |
| **Content Atomizer Lead** | TBD (human or agent) | Content Manager | content_atomizer supervision, output QA | 1 |
| **Student Success Lead** | TBD (human or agent) | Content Manager | student_tracker, enrollment optimization | 1 |

**Escalation Path:** Student Success Lead → Content Atomizer Lead → Content Manager → Director

**Decision Authority:**
- **Content Atomizer Lead:** Approve asset packs, quality gates
- **Content Manager:** Approve new course launches, instructor hiring
- **Director:** Approve curriculum changes, pricing decisions

---

### Finance (FIN)

| Role | Name | Reports To | Authority | Team Size |
|------|------|-----------|-----------|-----------|
| **CFO** | TBD | CEO | Consolidated financial health | 1 |
| **Controller** | TBD | CFO | GL integrity, reporting | 1 |
| **Transaction Processor** | TBD (human or agent) | Controller | transaction_processor supervision | 1 |
| **Compliance Officer** | TBD (human) | CFO | compliance_checker supervision | 1 |

**Escalation Path:** Transaction Processor → Controller → CFO (or Compliance Officer → CFO for violations)

**Decision Authority:**
- **Transaction Processor:** Post transactions <$10K
- **Controller:** Post transactions <$100K, reconcile variances
- **CFO:** Approve >$100K transactions, audit decisions, policy changes

---

### Logistics (LOG)

| Role | Name | Reports To | Authority | Team Size |
|------|------|-----------|-----------|-----------|
| **Director** | TBD | CEO | $80K/mo revenue goal | 1 |
| **Operations Manager** | TBD | Director | Fleet, routes, vendor mgmt | 1 |
| **Route Optimization Lead** | TBD (human or agent) | Ops Manager | route_optimizer supervision | 1 |
| **Shipment Coordinator** | TBD (human or agent) | Ops Manager | shipment_tracker, delivery confirmation | 1 |

**Escalation Path:** Shipment Coordinator → Route Lead → Ops Manager → Director

**Decision Authority:**
- **Route Lead:** Approve routes impacting <10 shipments
- **Ops Manager:** Approve vendor changes, cost optimization <5%
- **Director:** Approve new geographies, carrier partnerships >$50K/mo

---

### IZA OS (Infrastructure, Cost Center)

| Role | Name | Reports To | Authority | Team Size |
|------|------|-----------|-----------|-----------|
| **VP Infrastructure** | TBD | CEO | 99.9% uptime SLA | 1 |
| **Site Reliability Engineer (SRE)** | TBD | VP Infra | Service health, incident response | 1 |
| **Platform Engineer** | TBD | VP Infra | Agent automation, scaling, tooling | 1 |

**Escalation Path:** Platform Engineer/SRE → VP Infra → CTO/CEO (for budget allocation)

**Decision Authority:**
- **SRE:** Restart services, patch vulnerabilities, alert thresholds
- **Platform Engineer:** Deploy new agents, allocate compute, code reviews
- **VP Infra:** Vendor selection, capital expense >$10K, SLA negotiation

---

## Weekly Review Cadence

**Monday 9am:** OPCO director + team lead sync (15 min)
- Agent success rates from prior week
- Escalations requiring director approval
- Forecast upcoming weeks

**Wednesday 2pm:** Cross-OPCO sync (30 min)
- IZA OS infrastructure health report
- Cost tracker review (token/USD spend by OPCO)
- Capacity planning (agent load vs. human overhead)

**Friday 4pm:** Executive review (all directors + CEO)
- Revenue progress vs. $150K/mo goals (CON), $100K/mo (STA), etc.
- Autonomous agent decision audit (% decisions made without escalation)
- Hiring recommendations (if agent autonomy >90%, can we reduce headcount?)

---

## Related Contexts

[[AGENTS.md]] (agent roster, autonomy thresholds)
[[DEPARTMENTS.md]] (OPCO operating principles, Ray Dalio framework)
[[agent-alignment-observability]] (observability dashboard, 4-layer stack)
