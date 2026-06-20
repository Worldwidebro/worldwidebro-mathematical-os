# REGISTRY Integration Roadmap

## Status
✅ **Phase 1**: registry_loader.py and monitoring_engine.py completed and tested (2026-06-02)

---

## Phase 2: Agent Integration (Next)

### Step 1: Support Agent (hrms-support-ai-001)
- Import registry_loader at boot
- Validate decision authority before escalating
- Check SLA targets for escalation type (4h, 8h, 24h, 48h)
- Log decision to Supabase with SLA tracking

### Step 2: Sales Agent (hrms-sales-ai-001)
- Query venture-hub availability before deal routing
- Validate Stripe integration before payment processing
- Check con-001 construction portal status before lead assignment

### Step 3: Operations Agent (hrms-operations-ai-001)
- Hourly health report to Supabase `cluster_health` table
- Post Slack message to #hrms with deployment gate status
- Alert on SLA breach (escalation within 80% of threshold)

### Step 4: Product Agent (hrms-product-ai-001)
- Query lt-009 dispatch engine availability
- Validate Google Maps integration before route calculation
- Monitor technician portal real-time sync latency

---

## Phase 3: Dashboard Integration

### Step 1: venture-hub Cluster Dashboard
Import monitoring_engine and display:
- Real-time tier health (Tier 0-3)
- 4 deployment gate status
- Agent authority matrix (RACI roles)
- Shared services coverage map
- SLA compliance per agent

### Step 2: Supabase Tables
Create/update:
- `cluster_health` (health reports, one row per hourly check)
- `deployment_gates` (gate unlock criteria, gate status, timestamp)
- `agent_sla_compliance` (agent, decision_type, sla_target, resolution_time, on_time)

---

## Phase 4: Boot Validation

### Step 1: Repo startup scripts
Each repo loads REPO_REGISTRY.json at boot:
```bash
python3 -c "from registry_loader import RegistryLoader; loader = RegistryLoader(); checks = loader.get_repo_boot_checks('$(git rev-parse --abbrev-ref HEAD)');"
```

### Step 2: Dependency validation
Before Tier 1+ repos start, validate all dependencies are available:
- Build dependencies deployed
- Runtime dependencies accessible
- Shared services responding to health checks

---

## Testing Checklist

- [x] registry_loader loads REPO_REGISTRY.json without errors
- [x] get_repos_by_tier returns correct repos per tier
- [x] get_agent_repos uses "agent_repo_assignments" key correctly
- [x] get_repo_boot_checks returns string-based checks
- [x] monitoring_engine generates health report with all 4 tiers
- [x] check_agent_authority uses "agent_repo_assignments" correctly
- [x] export_for_slack formats message for #hrms channel
- [ ] hrms-support-ai-001 imports registry_loader without import errors
- [ ] hrms-sales-ai-001 validates access before processing deals
- [ ] hrms-operations-ai-001 posts hourly report to #hrms
- [ ] venture-hub dashboard imports monitoring_engine and renders tier health
- [ ] Supabase cluster_health table receives hourly reports
- [ ] Each repo validates boot checks at startup

---

## Files Modified

**Created**:
- registry_loader.py (280 lines, 15 query methods)
- monitoring_engine.py (215 lines, 7 health check methods)

**To modify**:
- hrms-support-ai-001 (agent decision flow)
- hrms-sales-ai-001 (agent decision flow)
- hrms-operations-ai-001 (hourly check, Slack posting)
- hrms-product-ai-001 (agent decision flow)
- venture-hub dashboard (import monitoring_engine, render SLA display)
- Supabase schema (add cluster_health, deployment_gates, agent_sla_compliance tables)
- Each repo boot script (validate REPO_REGISTRY.json dependencies)

---

## Success Criteria

1. ✅ registry_loader and monitoring_engine tested and committed
2. ⏳ At least one agent (hrms-operations-ai-001) imports registry_loader
3. ⏳ venture-hub dashboard displays real-time SLA metrics from monitoring_engine
4. ⏳ Supabase receives hourly cluster health reports
5. ⏳ All repos validate boot checks at startup

---

## Owner
hrms-operations-ai-001 (primary), hrms-founder-001 (oversight)

**Last Updated**: 2026-06-02
