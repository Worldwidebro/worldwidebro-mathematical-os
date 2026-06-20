# Agent Registry Usage Template

## Overview
This document shows how each agent uses `registry_loader.RegistryLoader` and `monitoring_engine.MonitoringEngine` to validate decisions, check dependencies, and track SLA compliance.

---

## Pattern 1: Support Agent Decision Flow

**Agent**: hrms-support-ai-001  
**Primary Repos**: the-office, venture-hub  
**Secondary Repos**: iza-os-rag-system  

### Decision Point: Customer Escalation

```python
from registry_loader import RegistryLoader

class SupportAgent:
    def __init__(self):
        self.loader = RegistryLoader()
        self.agent_id = "hrms-support-ai-001"
    
    def handle_escalation(self, escalation_type, ticket_id):
        # Step 1: Check if I have authority to escalate
        repos = self.loader.get_agent_repos(self.agent_id)
        authority = repos.get("decision_authority")
        
        if authority != "operational":
            # Escalate to founder
            return self.escalate_to_founder(ticket_id)
        
        # Step 2: Get SLA target for this escalation type
        agent_slas = self.loader.get_agent_sla_targets(self.agent_id)
        sla_target = self.get_sla_for_type(escalation_type)
        # e.g., "Support Escalations: 4h SLA"
        
        # Step 3: Validate dependencies before processing
        # Check if venture-hub is available for customer lookup
        access = self.loader.validate_repo_access("venture-hub", self.agent_id)
        if not access["valid"]:
            # Cannot access customer data, escalate
            return self.escalate_to_founder(ticket_id)
        
        # Step 4: Route decision
        decision = {
            "agent_id": self.agent_id,
            "decision_type": escalation_type,
            "sla_target": sla_target,
            "resolution_time": calculate_resolution_time(),
            "outcome": "escalated_to_founder",
            "ticket_id": ticket_id
        }
        
        # Log to Supabase for SLA tracking
        self.log_decision_to_supabase(decision)
        return decision
```

### SLA Targets (from STARRED-REPOS-MONITORING-WORKFLOW.md)
- Support Escalations: 4h SLA (target: 95% on-time)
- Sales Deals >$500/month: 8h SLA (target: 95% on-time)
- Payment Disputes: 24h SLA (target: 99% on-time)
- Feature Releases: 24h SLA (target: 95% on-time)
- Compliance/Audit: 48h SLA (target: 100% on-time)

---

## Pattern 2: Sales Agent Repo Access Check

**Agent**: hrms-sales-ai-001  
**Primary Repos**: venture-hub, pitch-kit, business-template-marketplace  
**Secondary Repos**: con-001-ace-construction  

### Decision Point: Process Lead Assignment

```python
from registry_loader import RegistryLoader

class SalesAgent:
    def __init__(self):
        self.loader = RegistryLoader()
        self.agent_id = "hrms-sales-ai-001"
    
    def assign_lead_to_venture(self, lead_id, venture_repo):
        # Step 1: Validate I can access this venture repo
        access = self.loader.validate_repo_access(venture_repo, self.agent_id)
        
        if not access["valid"]:
            print(f"Cannot access {venture_repo}: {access['error']}")
            # Escalate to founder with reason
            return {"outcome": "escalated", "reason": access["error"]}
        
        # Step 2: Check venture repo SLA targets
        metrics = self.loader.get_repo_monitoring_metrics(venture_repo)
        sla_targets = metrics.get("sla_targets", {})
        
        # Step 3: Check if venture portal is responding
        # (monitoring_engine would provide actual health data)
        
        decision = {
            "agent_id": self.agent_id,
            "lead_id": lead_id,
            "venture_repo": venture_repo,
            "access_tier": access["access_tier"],
            "sla_targets": sla_targets,
            "outcome": "assigned"
        }
        return decision
```

---

## Pattern 3: Operations Agent Hourly Health Check

**Agent**: hrms-operations-ai-001  
**Primary Repos**: venture-factory-core, civilization-os  
**Secondary Repos**: venture-hub  

### Scheduled Task: Hourly Cluster Health Report

```python
from registry_loader import RegistryLoader
from monitoring_engine import MonitoringEngine
import json

class OperationsAgent:
    def __init__(self):
        self.loader = RegistryLoader()
        self.engine = MonitoringEngine(self.loader)
        self.agent_id = "hrms-operations-ai-001"
    
    def hourly_health_check(self):
        # Step 1: Generate comprehensive health report
        report = self.engine.generate_health_report()
        
        # Step 2: Check for SLA breaches
        alerts = self.check_sla_breaches(report)
        
        # Step 3: Post to Slack if critical
        if alerts:
            slack_msg = self.engine.export_for_slack()
            self.post_to_slack(slack_msg, "#hrms")
        
        # Step 4: Store health report to Supabase
        self.log_health_report_to_supabase(report)
        
        return {
            "status": "completed",
            "timestamp": report["timestamp"],
            "alerts_count": len(alerts),
            "gate_status": report["checks"]["deployment_gates"]
        }
    
    def check_sla_breaches(self, report):
        breaches = []
        
        # Check Tier 0 health (no alert needed yet, just tracking)
        tier_0 = report["checks"]["tier_0_foundation"]
        
        # Check deployment gates (track progress)
        gates = report["checks"]["deployment_gates"]
        for gate_name, gate_status in gates.items():
            if gate_status["status"] == "blocked_for_2h":
                breaches.append({
                    "severity": "warning",
                    "gate": gate_name,
                    "action": "investigate_blocker"
                })
        
        return breaches
```

---

## Pattern 4: Product Agent Dispatch Validation

**Agent**: hrms-product-ai-001  
**Primary Repos**: autonomous-venture-studio, lt-009-hvac-technician-dispatch  
**Secondary Repos**: con-012-hvac-services  

### Decision Point: Route Calculation Request

```python
from registry_loader import RegistryLoader

class ProductAgent:
    def __init__(self):
        self.loader = RegistryLoader()
        self.agent_id = "hrms-product-ai-001"
    
    def calculate_dispatch_route(self, request_id, technician_id):
        # Step 1: Check dispatch engine dependencies
        dispatch_repo = "lt-009-hvac-technician-dispatch"
        
        # Get shared services required
        services = self.loader.get_repo_shared_services(dispatch_repo)
        required_services = [s["service_name"] for s in services]
        # e.g., ['Google Maps', 'Supabase', 'MCP servers']
        
        # Step 2: Validate access to con-012 (secondary repo)
        access = self.loader.validate_repo_access("con-012-hvac-services", self.agent_id)
        
        if not access["valid"]:
            return {"outcome": "failed", "reason": "Cannot access con-012"}
        
        # Step 3: Get SLA target for dispatch
        metrics = self.loader.get_repo_monitoring_metrics(dispatch_repo)
        sla_targets = metrics.get("sla_targets", {})
        # e.g., "Dispatch route calculation time: <5s"
        
        decision = {
            "agent_id": self.agent_id,
            "request_id": request_id,
            "technician_id": technician_id,
            "required_services": required_services,
            "sla_target": sla_targets.get("route_calc_time"),
            "outcome": "route_requested"
        }
        return decision
```

---

## Integration Checklist

### Per Agent
- [ ] Import registry_loader at initialization
- [ ] Get agent repos with `get_agent_repos(agent_id)`
- [ ] Validate access before accessing repos: `validate_repo_access(repo, agent_id)`
- [ ] Get SLA targets for decisions: `get_agent_sla_targets(agent_id)` or `get_repo_monitoring_metrics(repo)`
- [ ] Check dependencies: `get_repo_dependencies(repo)` and `get_repo_shared_services(repo)`
- [ ] Log decisions to Supabase with SLA tracking

### Operations Agent Only
- [ ] Import monitoring_engine at initialization
- [ ] Call `generate_health_report()` hourly
- [ ] Parse deployment gates: `report["checks"]["deployment_gates"]`
- [ ] Check agent authority: `report["checks"]["agent_authority"]`
- [ ] Post Slack message with `export_for_slack()`
- [ ] Log report to Supabase `cluster_health` table

### Dashboard Integration
- [ ] Import monitoring_engine
- [ ] Call `generate_health_report()` on page load + every 5 minutes
- [ ] Display tier health from `report["checks"]["tier_0_foundation"]` etc
- [ ] Display deployment gates from `report["checks"]["deployment_gates"]`
- [ ] Display SLA compliance trends from Supabase `agent_sla_compliance` table

---

## Supabase Tables Required

### `cluster_health`
```sql
CREATE TABLE cluster_health (
  id BIGSERIAL PRIMARY KEY,
  timestamp TIMESTAMP,
  agent_id TEXT,
  venture_id TEXT,
  tier_0_status TEXT,
  tier_1_status TEXT,
  tier_2_status TEXT,
  tier_3_status TEXT,
  gate_1_status TEXT,
  gate_2_status TEXT,
  gate_3_status TEXT,
  gate_4_status TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);
```

### `agent_sla_compliance`
```sql
CREATE TABLE agent_sla_compliance (
  id BIGSERIAL PRIMARY KEY,
  agent_id TEXT,
  decision_type TEXT,
  sla_target_hours INT,
  resolution_hours DECIMAL,
  on_time BOOLEAN,
  decision_id TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);
```

---

**Owner**: hrms-operations-ai-001  
**Last Updated**: 2026-06-02
