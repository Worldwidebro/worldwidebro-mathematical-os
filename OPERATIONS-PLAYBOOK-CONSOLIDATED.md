---
title: Worldwidebro Operations Playbook — Consolidated Living Reference
date: 2026-07-20
status: Production (Living Document)
---

# OPERATIONS PLAYBOOK — CONSOLIDATED REFERENCE

**This is your operational bible.** References existing playbooks + adds executable procedures.

**Related Documents:**
- Strategic: [MASTER-EXECUTION-PLAN.md](MASTER-EXECUTION-PLAN.md) (6-week roadmap)
- Navigation: [MASTER-INDEX.md](MASTER-INDEX.md) (4 Orbs)
- Specific: [VEX-OPERATIONS-DEPLOYMENT.md](VEX-OPERATIONS-DEPLOYMENT.md) (vex /operations route)

---

# PART 1: DEPLOYMENT CHECKLIST (Copy-Paste Ready)

## Pre-Deployment: Health Check All Systems

```bash
# Verify all 12+ containers healthy
docker-compose ps

# Test database connectivity
docker exec postgres pg_isready -U postgres && echo "✅ PostgreSQL"
docker exec redis redis-cli PING && echo "✅ Redis"

# Test graph + vector DBs
curl -s http://localhost:7474 > /dev/null && echo "✅ Neo4j"
curl -s http://localhost:6333/readiness > /dev/null && echo "✅ Qdrant"
```

## Deploy Sector Pages (14 live + 6 hero pages)

```bash
cd /Users/acebless/Documents/vex-hero-site

# Build + deploy
npm run build
vercel deploy --prod

# Verify all 14 sectors respond
for sector in transportation education real-estate financial operations staffing technology marketplace media healthcare hospitality investment construction beauty-wellness; do
  status=$(curl -s -o /dev/null -w "%{http_code}" "https://vex-hero-site-sigma.vercel.app/sectors/$sector")
  echo "$sector: HTTP $status"
done
```

## Post-Deployment Validation

```bash
# 1. Test lead capture (manual submission)
# Open: https://vex-hero-site-sigma.vercel.app/sectors/construction
# Fill form → Submit

# 2. Verify in database
psql -h localhost -U postgres << 'SQL'
SELECT COUNT(*) as new_leads FROM venture_leads 
WHERE created_at > NOW() - INTERVAL '5 minutes';
SQL

# 3. Monitor agent execution
psql -h localhost -U postgres << 'SQL'
SELECT agent_name, status, COUNT(*) as count FROM agent_executions 
WHERE created_at > NOW() - INTERVAL '1 hour' 
GROUP BY agent_name, status;
SQL
```

---

# PART 2: DAILY/WEEKLY OPERATIONS

## Daily (15 min, 9am)

```bash
# Health check
docker-compose ps | grep -v healthy && echo "⚠️ Unhealthy containers found"

# Recent deployments
vercel logs --limit 10 | grep -i error && echo "⚠️ Deployment errors found"

# Overnight leads
psql -h localhost -U postgres << 'SQL'
SELECT COUNT(*) as new_leads, 
       COUNT(DISTINCT venture_id) as unique_ventures
FROM venture_leads WHERE created_at > NOW() - INTERVAL '24 hours';
SQL
```

## Weekly (1 hour, Monday 9am)

```bash
# Agent success rates
psql -h localhost -U postgres << 'SQL'
SELECT agent_name, 
       ROUND(100 * SUM(CASE WHEN status='success' THEN 1 ELSE 0 END) / COUNT(*), 1) as success_rate,
       COUNT(*) as total_executions
FROM agent_executions 
WHERE created_at > NOW() - INTERVAL '7 days'
GROUP BY agent_name
ORDER BY success_rate DESC;
SQL

# Sector page traffic (Vercel analytics)
vercel analytics

# Venture leads by sector
psql -h localhost -U postgres << 'SQL'
SELECT venture_id, COUNT(*) as leads FROM venture_leads 
WHERE created_at > NOW() - INTERVAL '7 days'
GROUP BY venture_id ORDER BY leads DESC LIMIT 20;
SQL
```

## Monthly (3 hours, 1st of month)

```bash
# Update venture registry
cd /Users/acebless/Documents && python3 populate_venture_knowledge_graph.py

# Financial snapshot
psql -h localhost -U postgres << 'SQL'
SELECT 
  COUNT(DISTINCT venture_id) as ventures_active,
  COUNT(*) as total_leads_month,
  COUNT(DISTINCT venture_id) FILTER (WHERE status='closed') as closed_deals
FROM venture_leads 
WHERE created_at > date_trunc('month', NOW());
SQL

# Disaster recovery drill (test backup restoration)
# See: Backup & Recovery section below
```

---

# PART 3: AGENT EXECUTION SCHEDULE & OPCO ASSIGNMENTS

## Live Agents (Production Now)

### CON (Construction) — 4 Live Agents

| Agent ID | Name | Autonomy | Success Rate | Execution | Owner |
|----------|------|----------|--------------|-----------|-------|
| **CON-001** | venture_classifier | 90%+ Autonomous | 94% | Form submit → webhook | COO |
| **CON-002** | estimator_gen1 | 80-89% Supervised | 88% | After classify | CON Lead |
| **CON-003** | risk_assessor | 90%+ Autonomous | 91% | After estimate | Risk Lead |
| **CON-004** | project_scheduler | 70-79% Monitored | 75% | After risk | PM Lead |

**Execution Flow:**
```
Lead Form → Supabase INSERT venture_leads → n8n webhook fires
  ↓
CON-001 classify (routes to CON-001 through CON-012)
  ↓
CON-002 estimate (generates cost breakdown)
  ↓
CON-003 risk assess (flags OSHA/safety issues)
  ↓
CON-004 schedule (reserves crew + equipment)
  ↓
Output Actions:
  ✓ CRM update (TwentyHQ)
  ✓ Calendar invite (Founder)
  ✓ Proposal PDF (Email)
  ✓ Invoice (Stripe)
  ✓ Notification (Slack)
```

**Real Example:** Lead "Downtown Renovations LLC" submits form at 2:30pm
- CON-001: Routes to CON-005 (Commercial Renovation venture) — 94% confidence
- CON-002: Estimates $150K project (materials $60K, labor $80K, contingency $10K)
- CON-003: Flags: electrical permit required, 4-week timeline needed
- CON-004: Schedules: Crew meeting Wed 10am, project starts Mon
- Result: Founder receives email + proposal PDF + calendar invites within 5 min

---

## Future Agents (Building Q3-Q4)

| OPCO | Agent Count | Status | Launch |
|------|------------|--------|--------|
| **STA** (Staffing) | 3 agents | Building | Q3 2026 |
| **RE** (Real Estate) | 2 agents | Building | Q3 2026 |
| **EDU** (Education) | 2 agents | Building | Q4 2026 |
| **FIN** (Finance) | 1 agent | Building | Q4 2026 |
| **LOG** (Logistics) | 2 agents | Building | Q4 2026 |

---

# PART 4: QUICK TROUBLESHOOTING

## Container Unhealthy?

```bash
# Restart specific container
docker-compose restart neo4j  # example

# Nuclear option (fresh start)
docker-compose down && docker-compose up -d

# Wait 30 seconds, verify
sleep 30 && docker-compose ps
```

## Form Not Capturing Leads?

```bash
# 1. Check table exists
psql -h localhost -U postgres -c "\dt venture_leads;"

# 2. Verify webhook in n8n
# Open: http://localhost:5678 → Workflows → venture_leads → status should be "Active"

# 3. Check error logs
docker logs n8n | tail -50 | grep -i error
```

## Agent Execution Failed?

```bash
# View error
psql -h localhost -U postgres << 'SQL'
SELECT agent_name, error FROM agent_executions 
WHERE status='failed' 
ORDER BY created_at DESC LIMIT 5;
SQL

# Restart orchestrator
pkill -f crewai-agent-orchestrator.py
python3 /Users/acebless/Documents/crewai-agent-orchestrator.py &
```

## Vercel Deployment Stuck?

```bash
# Check status
vercel logs --limit 50

# Rollback
vercel rollback

# Or clear cache + redeploy
rm -rf .next && npm run build && vercel deploy --prod
```

---

# PART 5: BACKUP & DISASTER RECOVERY

## Automated Daily Backup

T7 Shield runs automatic nightly snapshots to `/Volumes/T7\ Shield/14_INFRASTRUCTURE/backups/`

## Manual Backup (Any Time)

```bash
# Backup PostgreSQL
pg_dump postgresql://postgres@localhost:5432/postgres > backup-$(date +%Y%m%d_%H%M%S).sql

# Verify
ls -lh backup-*.sql
```

## Restore from Backup

```bash
# 1. Stop services
docker-compose down

# 2. Restore database
psql postgresql://postgres@localhost:5432/postgres < backup-20260720_090000.sql

# 3. Restart services
docker-compose up -d

# 4. Verify
docker-compose ps  # wait for all healthy
psql -h localhost -U postgres -c "SELECT COUNT(*) FROM venture_leads;"
```

## Test Restore Procedure (Monthly Drill)

```bash
# 1. On 1st of month, test restoration
cd /Volumes/T7\ Shield/14_INFRASTRUCTURE/backups/

# 2. Find latest backup
ls -lrt | tail -1

# 3. Follow "Restore from Backup" steps above

# 4. Log test completion
echo "✅ Disaster recovery tested $(date)" >> /Volumes/T7\ Shield/14_INFRASTRUCTURE/backups/test-log.txt
```

---

# QUICK COMMAND CHEAT SHEET

| Task | Command |
|------|---------|
| Health check all | `docker-compose ps` |
| Deploy sectors | `cd vex-hero-site && npm run build && vercel deploy --prod` |
| View agent stats | `psql -h localhost -U postgres -c "SELECT agent_name, status, COUNT(*) FROM agent_executions GROUP BY agent_name, status;"` |
| Check recent leads | `psql -h localhost -U postgres -c "SELECT COUNT(*) FROM venture_leads WHERE created_at > NOW() - INTERVAL '24 hours';"` |
| View deployment logs | `vercel logs --limit 50` |
| Restart service | `docker-compose restart [service-name]` |
| Backup database | `pg_dump postgresql://postgres@localhost:5432/postgres > backup-$(date +%Y%m%d_%H%M%S).sql` |
| Monitor agent execution | `psql -h localhost -U postgres -c "SELECT * FROM agent_executions WHERE created_at > NOW() - INTERVAL '1 hour' ORDER BY created_at DESC;"` |

---

**Owner:** CTO / COO  
**Last Updated:** 2026-07-20  
**Next Review:** 2026-07-27
