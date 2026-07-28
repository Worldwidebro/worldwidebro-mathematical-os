# Monitoring & Observability Setup Guide

Production monitoring for Ace Construction (CON-001) payment pipeline. Two layers:

1. **Langfuse** — LLM trace tracking (costs, latency, quality)
2. **Prometheus** — System metrics (request rate, errors, latency)

---

## Part 1: Langfuse Setup (LLM Observability)

Langfuse tracks every Hermes agent call: prompt, model, cost, latency, token usage.

### 1.1 Docker Setup (Already Running)

Langfuse runs in Docker (see docker-compose.yml):

```bash
# Already running on localhost:3003
curl http://localhost:3003/api/health
# Returns: {"status":"ok"}
```

### 1.2 Create Project & Get API Keys

1. Open Langfuse UI: http://localhost:3003
2. Sign up or log in (local Langfuse instance)
3. Create new project: "Ace Construction"
4. Get API keys:
   - **Public Key:** `pk_xxx`
   - **Secret Key:** `sk_xxx`
5. Save to `.env`:
   ```
   LANGFUSE_PUBLIC_KEY=pk_xxx
   LANGFUSE_SECRET_KEY=sk_xxx
   LANGFUSE_HOST=http://localhost:3003
   ```

### 1.3 Instrument Hermes Agent

Add Langfuse tracing to `runtime_agent_runtime.py`:

```python
from langfuse import Langfuse

langfuse = Langfuse(
    public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
    host=os.getenv("LANGFUSE_HOST", "http://localhost:3003"),
)

async def execute_action(agent_id: str, action: str, params: dict, venture_id: str):
    # Create trace
    with langfuse.trace(
        name=f"{agent_id}:{action}",
        metadata={"venture_id": venture_id, "action": action},
        input=params,
    ) as trace:
        # ... execute action ...
        trace.generation(
            name=f"stripe_charge",
            input={"amount_cents": params.get("amount_cents")},
            output=result,
            model="stripe",
            usage={"input": 1, "output": 1},
        )
        return result
```

### 1.4 Monitor in Langfuse Dashboard

Langfuse dashboard shows:
- **Traces** — every agent call with full context
- **Cost analysis** — aggregate spend by model/agent/action
- **Latency** — p50/p95/p99 response times
- **Token usage** — input/output tokens per call

---

## Part 2: Prometheus Setup (System Metrics)

Prometheus scrapes metrics from the application and infrastructure.

### 2.1 Docker Setup (Already Running)

Prometheus runs in Docker (see docker-compose.yml):

```bash
# Already running on localhost:9090
curl http://localhost:9090/api/v1/query?query=up
# Returns: metrics data
```

### 2.2 Update prometheus.yml

Current config only scrapes Prometheus itself. Update `/Users/acebless/Documents/prometheus.yml`:

```yaml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  # Prometheus self-monitoring
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  # Application metrics (Hermes agent)
  - job_name: 'hermes-agent'
    static_configs:
      - targets: ['localhost:8000']
    metrics_path: '/metrics'

  # OpenTelemetry Collector (forwards traces)
  - job_name: 'otel-collector'
    static_configs:
      - targets: ['localhost:9464']
```

### 2.3 Add Prometheus to Application

Instrument the runtime with Prometheus metrics:

```python
from prometheus_client import Counter, Histogram, start_http_server
import time

# Metrics
stripe_charges_total = Counter(
    'stripe_charges_total',
    'Total Stripe charges processed',
    ['venture_id', 'status'],
)
stripe_charge_amount_usd = Histogram(
    'stripe_charge_amount_usd',
    'Stripe charge amounts (USD)',
    buckets=[10, 50, 100, 500, 1000],
)
action_latency_seconds = Histogram(
    'action_latency_seconds',
    'Agent action latency (seconds)',
    ['agent_id', 'action'],
)

# In handler
async def handle_payment_succeeded(...):
    start = time.time()
    try:
        # ... execute ...
        stripe_charges_total.labels(
            venture_id=venture_id,
            status='success'
        ).inc()
        stripe_charge_amount_usd.observe(amount_cents / 100)
    except Exception as e:
        stripe_charges_total.labels(
            venture_id=venture_id,
            status='error'
        ).inc()
        raise
    finally:
        duration = time.time() - start
        action_latency_seconds.labels(
            agent_id='hermes',
            action='charge'
        ).observe(duration)

# Start metrics server
if __name__ == '__main__':
    start_http_server(8000)  # /metrics on port 8000
```

### 2.4 Configure Grafana Dashboards

Grafana (localhost:3001) visualizes Prometheus data:

1. Add Prometheus datasource:
   - Data source name: "Prometheus"
   - URL: `http://localhost:9090`
   - Save & test

2. Create dashboard for payment pipeline:
   - **Panels:**
     - Stripe charges per hour (Counter)
     - Average charge amount (Histogram)
     - Error rate (%)
     - Agent latency p95 (Histogram)
     - Venture MRR (running sum)

3. Save dashboard as "Ace Construction - Payments"

---

## Part 3: Alert Rules

Create Prometheus alert rules (`prometheus-rules.yml`):

```yaml
groups:
  - name: hermes-alerts
    rules:
      # High error rate
      - alert: HighPaymentErrorRate
        expr: |
          (
            sum(rate(stripe_charges_total{status="error"}[5m]))
            /
            sum(rate(stripe_charges_total[5m]))
          ) > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "Stripe payment error rate > 5% for 5m"

      # Slow agent
      - alert: SlowHermesAgent
        expr: |
          histogram_quantile(0.95, action_latency_seconds) > 10
        for: 10m
        labels:
          severity: warning
        annotations:
          summary: "Hermes agent latency p95 > 10s"

      # No revenue
      - alert: NoRevenueDetected
        expr: |
          increase(stripe_charges_total[1h]) == 0
        for: 2h
        labels:
          severity: warning
        annotations:
          summary: "No Stripe charges in last 2 hours"
```

Load rules into Prometheus:

```yaml
# In prometheus.yml
rule_files:
  - 'prometheus-rules.yml'

alerting:
  alertmanagers:
    - static_configs:
        - targets: ['localhost:9093']
```

---

## Part 4: Deployment Checklist

**Pre-launch:**
- [ ] Langfuse running and accessible
- [ ] Prometheus scraping application metrics
- [ ] Grafana dashboard created for payment pipeline
- [ ] Alert rules loaded (high error rate, slow agent, no revenue)
- [ ] Integration tests pass

**Post-launch:**
- [ ] Monitor Langfuse dashboard for first payments
- [ ] Check Prometheus metrics for baseline
- [ ] Verify Grafana dashboard renders live data
- [ ] Test alert firing

---

## Quick Reference

| Service | URL | Purpose |
|---------|-----|---------|
| Langfuse | http://localhost:3003 | LLM traces (costs, latency) |
| Prometheus | http://localhost:9090 | Metrics scraper |
| Grafana | http://localhost:3001 | Dashboards & alerts |
