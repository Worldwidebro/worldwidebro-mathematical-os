# P0: Observability Fixes — ACTION NOW

**Goal:** Get all services healthy + wired to dashboards  
**Time:** 2-3 hours  
**Owner:** CTO  
**Deadline:** 2026-07-30

---

## Quick Status Check

```bash
# See what's broken right now
./WORLDWIDEBRO-OS/scripts/check-tools.sh --verbose

# Or spot-check each service:
curl http://localhost:9090/metrics 2>&1 | head -1          # Prometheus
curl http://localhost:3001/api/health 2>&1                 # Grafana
curl http://localhost:3003/api/health 2>&1                 # Langfuse
curl http://localhost:4000/health 2>&1                     # LiteLLM
curl http://localhost:7474/browser 2>&1 | head -1          # Neo4j
```

---

## Fix 1: LiteLLM Config — 30 min ⚠️ CRITICAL

**Why:** All local model inference fails if this is wrong.

**Issue:** `litellm_config.yaml` points to `host.docker.internal:11434` (this machine) but Ollama is on Mac Studio (`100.87.214.70:11434`)

**Action:**

```bash
# 1. Edit the file
nano /Users/acebless/Documents/litellm_config.yaml

# 2. Find line ~30:
#    api_base: http://host.docker.internal:11434

# 3. Change to:
#    api_base: http://100.87.214.70:11434

# 4. Save (Ctrl+O, Enter, Ctrl+X)

# 5. Restart container
docker-compose restart litellm

# 6. Wait 10 seconds and test
sleep 10 && curl http://localhost:4000/health
```

**Expected result:**
```json
{
  "status": "ok",
  "models": ["local-reasoning", "local-large"]
}
```

---

## Fix 2: Grafana Password — 15 min

**Why:** Can't log in to configure dashboards.

**Issue:** Admin password set at startup, unknown value.

**Action:**

```bash
# Reset password
docker exec grafana grafana-cli admin reset-admin-password admin123

# Verify
curl -u admin:admin123 http://localhost:3001/api/health

# You'll see:
# {"database":"ok","version":"..."}
```

**Then login:** http://localhost:3001  
User: `admin`  
Pass: `admin123`

---

## Fix 3: Langfuse Debug — 30 min

**Why:** LLM tracing won't work. Need to see model choices + cost.

**Issue:** Container unhealthy + Internal Server Error (500).

**Action:**

```bash
# Check actual error
docker logs langfuse | tail -50

# Look for: database error, migration failure, port issue

# If DB connection issue:
docker-compose restart supabase langfuse

# Or full restart:
docker-compose down langfuse && sleep 5 && docker-compose up -d langfuse

# Wait 30 sec for startup
sleep 30

# Test
curl http://localhost:3003/api/health
```

**If still 500:**
- Check logs: `docker logs -f langfuse`
- Verify SUPABASE_URL + SUPABASE_KEY in docker-compose env
- Try: `docker-compose logs -f | grep -i langfuse`

---

## Fix 4: Prometheus Targets — 30 min

**Why:** Prometheus only scrapes itself. Need to scrape actual services for metrics.

**Issue:** `prometheus.yml` missing target configs.

**Action:**

```bash
# Edit config
nano /Users/acebless/Documents/WORLDWIDEBRO-OS/TECHNOLOGY/observability/prometheus.yml

# Add after existing "prometheus" job:

  - job_name: 'litellm'
    static_configs:
      - targets: ['localhost:4000']
    scrape_interval: 5s

  - job_name: 'otel-collector'
    static_configs:
      - targets: ['localhost:9464']
    scrape_interval: 10s

  - job_name: 'neo4j'
    static_configs:
      - targets: ['localhost:7474']
    scrape_interval: 15s

# Save and restart
docker-compose restart prometheus

# Wait 5 sec
sleep 5

# Verify targets
curl -s http://localhost:9090/api/v1/targets | jq '.data.activeTargets | length'
# Should show: 4 or 5
```

**Verify each is "up":**
```bash
curl -s http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | {job: .labels.job, health}'
```

---

## Fix 5: Build Grafana Dashboards — 1 hour

**Once logged in (admin/admin123):**

### CEO Dashboard
```
Title: CEO Portfolio Dashboard

Panel 1: Active Ventures (Gauge)
- Datasource: DuckDB
- Query: SELECT COUNT(*) as count FROM ventures WHERE status = 'active'
- Thresholds: 0 (red) → 50 (yellow) → 100 (green)

Panel 2: Total MRR (Stat)
- Query: SELECT SUM(mrr) as mRR FROM ventures
- Unit: USD
- Color: green

Panel 3: Risk Score (Gauge)
- Query: SELECT AVG(risk_score) as risk FROM ventures
- Thresholds: 0 (green) → 50 (yellow) → 75 (red)

Panel 4: Runway Distribution (Bar)
- Query: SELECT runway_months, COUNT(*) as count FROM ventures GROUP BY runway_months
```

### CFO Dashboard
```
Title: CFO Financial Dashboard

Panel 1: MRR by OPCO (Bar)
- Query: SELECT opco_id, SUM(mrr) as mRR FROM ventures GROUP BY opco_id

Panel 2: ARR 12-Month (Line)
- Query: SELECT DATE_TRUNC('month', created_at) as month, SUM(mrr) * 12 as arr FROM ventures GROUP BY DATE_TRUNC('month', created_at)

Panel 3: Unit Economics (Table)
- Columns: sector | CAC | LTV | Ratio
- Query: SELECT sector, avg_cac as CAC, avg_ltv as LTV, avg_ltv/avg_cac as ratio FROM venture_economics

Panel 4: Runway Alert (Stat)
- Query: SELECT COUNT(*) as at_risk FROM ventures WHERE runway_months < 3
- Color: red if >0
```

### CTO Dashboard
```
Title: CTO Infrastructure Dashboard

Panel 1: Deployment Success (Gauge)
- Query: SELECT success / total * 100 as pct FROM deployment_stats
- Thresholds: 95 (yellow) → 99.5 (green)

Panel 2: API Error Rate (Gauge)
- Query: SELECT errors / requests * 100 as error_pct FROM api_logs WHERE timestamp > NOW() - INTERVAL 1 hour
- Thresholds: 1 (yellow) → 5 (red)

Panel 3: Latency P50 (Stat)
- Query: SELECT QUANTILE(latency_ms, 0.50) as p50 FROM api_logs

Panel 4: Latency P95 (Stat)
- Query: SELECT QUANTILE(latency_ms, 0.95) as p95 FROM api_logs

Panel 5: Latency P99 (Stat)
- Query: SELECT QUANTILE(latency_ms, 0.99) as p99 FROM api_logs

Panel 6: Tool Health (Table)
- Columns: tool_name | status | last_check
- Data from: `tools:health:*` Redis keys (or file from check-tools.sh)
```

---

## Verification Checklist

After all fixes, run:

```bash
# Full health check
./WORLDWIDEBRO-OS/scripts/check-tools.sh --verbose

# Should see:
# ✅ Prometheus: healthy
# ✅ Grafana: healthy
# ✅ Langfuse: healthy
# ✅ LiteLLM: healthy
# ✅ Neo4j: healthy
# ✅ Qdrant: healthy
# ✅ Redis: healthy
```

**All dashboards should:**
- Load without errors
- Show data (even if 0 values initially)
- Update when you refresh

---

## If Stuck

| Issue | Debug Command |
|-------|---|
| LiteLLM not responding | `docker logs litellm \| tail -20` |
| Grafana password still wrong | `docker exec grafana grafana-cli user-list` |
| Langfuse 500 error | `docker logs langfuse \| grep -i error` |
| Prometheus targets down | `curl http://localhost:9090/api/v1/targets \| jq` |
| Dashboards show no data | Check datasource in Grafana: http://localhost:3001/admin/datasources |

---

## Next: After P0 Complete

- [ ] Instrument Hermes with Langfuse tracing (2 hours)
- [ ] Wire tool health checks to agents (1 hour)
- [ ] Scale agents to 10 ventures (3 hours)
- [ ] Execute 3 task types end-to-end (1.5 hours)

**Total from P0 to first working venture: ~8 hours**
