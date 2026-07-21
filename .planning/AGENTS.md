---
references:
  - [[unified-os-architecture]]
  - [[REPOSITORY-INTELLIGENCE-SYSTEM]]
  - [[agent-alignment-observability]]
---

# AGENTS.md — Decision Authority & Agent Roster

## Principles (Applied from 100+ Framework)

**Chain of Thought:** Each agent's decision chain is logged and traceable (Supabase → Neo4j → Grafana).
**Mapping:** Agent success rate directly maps to decision autonomy.
**Roadmapping:** Agent capability roadmap: MVP (<70% success) → Growth (70–89%) → Autonomous (90%+).
**Planning:** POLC framework per agent: Plan decisions, Organize context, Lead execution, Control outcomes.

---

## Decision Authority Thresholds

| Success Rate | Authority | Approval Required | Escalation |
|--------------|-----------|-------------------|------------|
| **90%+** | **AUTONOMOUS** | None | Blocked decisions only |
| **80–89%** | **SUPERVISED** | Team lead approval ($1K+) | Manager sign-off ($5K+) |
| **70–79%** | **MONITORED** | Manager approval all decisions | Director escalation |
| **<70%** | **TRAINING** | 100% human approval | Pull from production |

---

## Agent Roster by OPCO

### Construction (CON)

| Agent | Role | Success Rate | Authority | Capability | Depends On |
|-------|------|--------------|-----------|-----------|-----------|
| **venture_classifier** | Intake router | 94% | AUTONOMOUS | Classify leads by venture type | PostgreSQL, Neo4j |
| **estimator_gen1** | Cost estimation | 88% | SUPERVISED | Generate bid estimates | Qdrant, PostgreSQL |
| **project_scheduler** | Resource allocation | 75% | MONITORED | Schedule work + equipment | Supabase |
| **risk_assessor** | Risk identification | 91% | AUTONOMOUS | Flag compliance/safety risks | Neo4j, PostgreSQL |

**Target:** 4 ventures at 90%+ autonomy by Q3 end.

---

### Staffing (STA)

| Agent | Role | Success Rate | Authority | 
|-------|------|--------------|-----------|
| **candidate_matcher** | Match skills to roles | TBD | TRAINING |
| **availability_tracker** | Shift scheduling | TBD | TRAINING |
| **rate_optimizer** | Dynamic pay rates | TBD | TRAINING |

**Target:** 1 live by Q3 end.

---

### Real Estate (RE)

| Agent | Role | Success Rate | Authority |
|-------|------|--------------|-----------|
| **property_valuer** | Market valuation | TBD | TRAINING |
| **listing_categorizer** | Property tagging | TBD | TRAINING |
| **lead_qualifier** | Lead scoring | TBD | TRAINING |

**Target:** 1 live by Q4.

---

### Education (EDU)

| Agent | Role | Success Rate | Authority |
|-------|------|--------------|-----------|
| **student_tracker** | Progress monitoring | TBD | TRAINING |
| **content_atomizer** | 50-asset generation | TBD | TRAINING |
| **enrollment_optimizer** | Course recommendations | TBD | TRAINING |

**Target:** 1 live by Q4.

---

### Finance (FIN)

| Agent | Role | Success Rate | Authority |
|-------|------|--------------|-----------|
| **transaction_processor** | GL categorization | TBD | TRAINING |
| **risk_calculator** | Portfolio risk | TBD | TRAINING |
| **compliance_checker** | Regulatory monitoring | TBD | TRAINING |

**Target:** 1 live by Q4.

---

### Logistics (LOG)

| Agent | Role | Success Rate | Authority |
|-------|------|--------------|-----------|
| **route_optimizer** | Route optimization | TBD | TRAINING |
| **shipment_tracker** | Status tracking | TBD | TRAINING |
| **cost_calculator** | Shipping estimation | TBD | TRAINING |

**Target:** 1 live by Q4.

---

### IZA OS (Infrastructure)

| Agent | Role | Success Rate | Authority |
|-------|------|--------------|-----------|
| **infra_health_monitor** | Service health | TBD | TRAINING |
| **cost_tracker** | Execution cost logging | TBD | TRAINING |
| **capacity_planner** | Disk/memory forecasting | TBD | TRAINING |

**Target:** 3 live by Q3 end.

---

## Autonomy Model: Chain-of-Thought Decision Flow

1. **Trigger:** Data arrives (lead, invoice, shipment, enrollment)
2. **Reason:** Agent traces decision (logged to Neo4j)
3. **Check:** Success rate ≥90%? → Autonomous. Else → Escalate
4. **Execute:** Write decision (venture_leads, ledger, shipment, enrollment)
5. **Log:** Supabase (agent_executions): status, tokens, cost, latency, machine
6. **Feedback:** Recalculate success rate weekly; adjust autonomy if needed

---

## File-Scoped Commands

```bash
# Test individual agent locally
python3 /WORLDWIDEBRO-OS/05-AGENTS/{agent_name}.py --test

# Deploy single workflow to n8n
n8n workflow import --file /WORLDWIDEBRO-OS/04-OPERATIONS/IZA-OS/workflows/{workflow_name}.json

# Load org.yaml into Neo4j
python3 /WORLDWIDEBRO-OS/05-AGENTS/neo4j_graph_loader.py /WORLDWIDEBRO-OS/04-OPERATIONS/IZA-OS/organization.yaml

# Check agent execution log
psql -h localhost -d civilization_os -c "SELECT * FROM agent_executions ORDER BY created_at DESC LIMIT 10;"

# Trace decision flow (Neo4j)
echo "MATCH (h:Hermes)-[:ROUTES_TO]->(d:Department) RETURN h, d;" | cypher-shell -u neo4j -p {password}
```

---

## Path to Income (6-Week Execution)

| Week | Task | Blocker Clears | Revenue Impact |
|------|------|---|---|
| W1 | 1. Implement `hermes.py` + 2. Deploy decision-routing n8n + 3. Load org.yaml to Neo4j | Agents can coordinate | $0 |
| W2 | 4. Wire vex → capability-request webhook + 5. Execute OPS-001 end-to-end | Ventures execute decisions | $1-3K/week (OPS-001) |
| W3-4 | 6-11. Implement Finance, Tech, Ops depts | 6 departments operational | $3-10K/week |
| W5 | 12-13. Activate 10 ventures in parallel | Parallel execution | $10-30K/week |
| W6 | 14-15. Hermes auto-scaling loop | Self-optimizing | $20-50K/week |

**Current state:** $0/week (no agents running)  
**After W2:** $1-3K/week  
**Target Month 12:** $57K-$135K/month (all 4 capital layers)

---

## Roadmap

**W1-2 (This Week):** Bridge YAML→Code gap. First venture generates income.  
**W3-4:** Scale to 6 departments. Parallel execution.  
**W5-6:** Autonomy model active. Hermes makes resource decisions.  
**Q3 (Jul–Sep):** 4–6 agents live (CON focus). Infra observability complete.  
**Q4 (Oct–Dec):** 2–3 agents per OPCO at >90%. Autonomous decision audit.  
**Q1 2027:** Hiring decision based on agent capacity vs. human labor cost.

---

## Creating a New Agent

1. **Create implementation:** `touch /WORLDWIDEBRO-OS/05-AGENTS/{department}/{agent_name}.py`
2. **Define authority:** Reference `/WORLDWIDEBRO-OS/04-OPERATIONS/IZA-OS/organization.yaml` for thresholds
3. **Add to registry:** Update `/WORLDWIDEBRO-OS/05-AGENTS/agent_registry.yaml` with success_rate = TBD
4. **Test locally:** `python3 {agent_name}.py --test` (mock decision, check logs)
5. **Deploy to n8n:** Create workflow node that calls agent via HTTP
6. **Wire execution log:** Agent writes to `agent_executions` table on Supabase

---

## Commit Attribution

AI commits MUST include:
```
Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>
```

---

Related: [[TEAMS.md]], [[DEPARTMENTS.md]], [[agent-alignment-observability]]
