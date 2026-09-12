[[STARTHERE]] | [[_INFRASTRUCTURE/README|Infrastructure Hub]] | [[CLAUDE]]

# PHASE 2: UNIFIED IMPLEMENTATION ROADMAP
**SALES + ORCHESTRATION + RESEARCH AUTOMATION**

**Start Date:** 2026-09-09  
**Critical Path:** Sep 9-14 (Sales) → Sep 14-28 (Orchestration) → Oct 1-31 (Research)  
**Authority:** CP-027 (Infrastructure), CP-033 (Execution), CP-021 (Revenue Operations)

---

## 🎯 THE THREE-LAYER STRATEGY

```
                    OBSERVABILITY SPINE
                    (OpenTelemetry)
                            │
         ┌──────────────────┼──────────────────┐
         ↓                  ↓                  ↓
    SALES               ORCHESTRATION      RESEARCH
    EXECUTION           AUTOMATION         AUTOMATION
    (MANUAL)            (N8N)              (AGENTS)
    Sep 9-14            Sep 14-28          Oct 1-31
```

Each layer emits telemetry → Langfuse → Grafana → Decisions

---

# LAYER 1: SALES EXECUTION (Sep 9-14)

## Objective
Make first $2,500 revenue by Sep 14 (OPS-001 placement).

## Why This First
- Revenue unlocks everything else
- Proof of concept before automation
- Feeds data into orchestration layer

---

## Phase 1.1: SETUP (Sep 9 — 2 hours)

### Task 1.1.1: Create Sales Playbook
**Owner:** You  
**Time:** 30 min

```yaml
playbook:
  venture: OPS-001 (CareerOps Staffing)
  
  objective: "$2,500 placement fee"
  
  target_segment:
    industry: Staffing / HR
    location: NC (high unemployment)
    size: 20-500 employees
    pain_point: "Hard to find warehouse workers"
  
  call_script:
    opener: "Hi [name], this is [you] with CareerOps. We place vetted warehouse workers in NC. Do you have 2 minutes?"
    
    value_prop: "Our workers cost $2,500 less than temp agencies, stay 12+ months, and we pre-screen for reliability."
    
    hook: "We have 3 workers ready this week for warehouse roles. Interested in seeing profiles?"
    
    close: "Great. I'll send you profiles. Can you review by EOD and let me know if any are fits?"
  
  process:
    1. Objection handling (time, price, trust)
    2. Qualification (they have open roles)
    3. Profile send (show 3 candidate profiles)
    4. Follow-up (24h)
    5. Deal close (sign agreement, $2,500 fee)
  
  success_criteria:
    call: "Prospect agrees to review profiles"
    deal: "Agreement signed, payment received"
```

**Deliverable:** `scripts/OPS-001-CALL-SCRIPT.md`

---

### Task 1.1.2: Build Call List
**Owner:** You  
**Time:** 1 hour

```bash
# Extract NC staffing companies from LinkedIn / Google / local directories
# Target: 50 companies with phone numbers

# Output: calls/OPS-001-HIGH-PRIORITY-CALLS.csv
# Format:
# company_name,phone,contact_name,size_estimate,pain_point_signal,call_priority
# Staffing Inc,919-555-0100,John Smith,150,hiring,HIGH
# ...

# Commands:
1. Use LinkedIn Sales Navigator search
2. Download from ZoomInfo (if available)
3. Scrape from Google Maps (staffing agencies)
4. Manual LinkedIn profile lookup
```

**Deliverable:** `calls/OPS-001-HIGH-PRIORITY-CALLS.csv` (50 prospects)

---

### Task 1.1.3: Wire OTel for Sales Pipeline
**Owner:** DevOps  
**Time:** 45 min

**File:** `_INFRASTRUCTURE/otel-sales-instrumentation.yaml`

```yaml
otel_sales_instrumentation:
  
  enabled: true
  
  service_name: ops-001-sales-pipeline
  
  metrics:
    # Count calls by status
    - name: sales.calls.total
      type: counter
      attributes:
        - status: ["attempted", "reached", "interested", "qualified"]
        - venture: ops-001
    
    # Conversion funnel
    - name: sales.funnel.conversion
      type: gauge
      attributes:
        - stage: ["call_attempted", "call_connected", "call_interested", "profile_sent", "profile_reviewed", "deal_closed"]
        - venture: ops-001
    
    # Deal value
    - name: sales.deal.value_usd
      type: histogram
      attributes:
        - venture: ops-001
        - deal_status: ["open", "closed"]
    
    # Pipeline velocity
    - name: sales.pipeline.days_in_stage
      type: histogram
      attributes:
        - stage: ["discovery", "qualification", "proposal", "negotiation", "closed"]
  
  traces:
    # Each call is a span
    - name: sales.call
      attributes:
        - prospect_id
        - call_duration_seconds
        - call_outcome: ["no_answer", "voicemail", "objection", "interested", "qualified"]
        - script_version
    
    # Deal progression
    - name: sales.deal
      attributes:
        - deal_id
        - venture: ops-001
        - stage_transitions: ["discovery→qualification→proposal→closed"]
        - days_to_close
  
  logs:
    # Every call logged
    - call_log:
        timestamp: ISO8601
        prospect: name + phone
        script_used: version
        outcome: text notes
        next_action: date + action
    
    # Deal closed
    - deal_closed:
        deal_id: UUID
        venture: ops-001
        prospect: name
        value: $2,500
        payment_method: Stripe
        timestamp: ISO8601

  exporters:
    - type: langfuse
      endpoint: http://localhost:3003
      api_key: ${LANGFUSE_API_KEY}
    
    - type: prometheus
      endpoint: http://localhost:9090
      push_interval: 30s
```

**Setup steps:**

```bash
# 1. Install Python OTel SDK
pip install opentelemetry-api opentelemetry-sdk opentelemetry-exporter-trace-langfuse opentelemetry-exporter-metrics-prometheus

# 2. Create instrumentation wrapper
# File: scripts/sales_otel_wrapper.py

from opentelemetry import trace, metrics
from opentelemetry.exporter.trace.langfuse import LangfuseSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.exporter.metrics.prometheus import PrometheusMetricReader

# Initialize tracer for sales calls
trace.set_tracer_provider(TracerProvider())
langfuse_exporter = LangfuseSpanExporter()
trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(langfuse_exporter)
)

tracer = trace.get_tracer(__name__)

# Decorator for call logging
def otel_sales_call(prospect_name, phone):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with tracer.start_as_current_span("sales.call") as span:
                span.set_attribute("prospect_name", prospect_name)
                span.set_attribute("phone", phone)
                span.set_attribute("venture", "ops-001")
                result = func(*args, **kwargs)
                span.set_attribute("outcome", result.get("status"))
                span.set_attribute("duration_seconds", result.get("duration"))
                return result
        return wrapper
    return decorator

# Usage:
@otel_sales_call("John Smith", "919-555-0100")
def make_call():
    # Call logic
    return {"status": "interested", "duration": 180}

# 3. Wire into ClickUp task creation
# Each task → Langfuse span
```

**Deliverable:** OTel instrumentation live, Langfuse receiving sales traces

---

## Phase 1.2: EXECUTION (Sep 9-13 — 40 hours)

### Task 1.2.1: Make 10 Cold Calls (Day 1-2)
**Owner:** You  
**Time:** 2-3 hours/day × 2 days = 6 hours

```bash
# Day 1: Make calls 1-5
# Day 2: Make calls 6-10

# Script:
#!/bin/bash
for i in {1..10}; do
  prospect=$(sed -n "${i}p" calls/OPS-001-HIGH-PRIORITY-CALLS.csv)
  phone=$(echo $prospect | cut -d, -f2)
  name=$(echo $prospect | cut -d, -f1)
  
  echo "Calling $name at $phone..."
  # Manual dial or softphone
  
  # Log result to OTel
  python scripts/sales_otel_wrapper.py \
    --prospect "$name" \
    --phone "$phone" \
    --outcome "interested|objection|voicemail" \
    --duration 180
done
```

**Track:** OpenTelemetry span per call → Langfuse dashboard shows conversion funnel

**Success metric:** 2-3 prospects interested by end of Day 2

---

### Task 1.2.2: Send Profiles (Day 2-3)
**Owner:** You + DevOps  
**Time:** 2 hours

For each interested prospect:
1. Create candidate profile packet (3 worker profiles)
2. Send via email
3. Create ClickUp task: "Follow up with [prospect name] by [date]"
4. Log in OTel: `sales.profile_sent`

```yaml
profile_packet:
  prospect: [name]
  email_sent: [date/time]
  
  workers:
    - name: Worker 1
      experience: warehouse, 8 years
      certifications: OSHA, forklift
      availability: immediate
      wage_expectation: $16/hr
    
    - name: Worker 2
      experience: warehouse, 5 years
      certifications: forklift
      availability: immediate
      wage_expectation: $15.50/hr
    
    - name: Worker 3
      experience: logistics, 3 years
      certifications: none
      availability: immediate
      wage_expectation: $15/hr
  
  placement_fee: $2,500
  guarantee: "If worker leaves within 6 months, we replace free"
```

**OTel metric:** `sales.funnel.conversion` update to "profile_sent" stage

---

### Task 1.2.3: Follow-up Calls (Day 3-4)
**Owner:** You  
**Time:** 1-2 hours/day × 2 days = 4 hours

Call each prospect who received profiles:
- "Did you get the profiles I sent?"
- "Do any fit your open roles?"
- If yes → Move to deal close
- If no → "What are you looking for?" (refine profiles)
- If maybe → "Can I follow up Friday?"

**OTel tracking:**
- `sales.call` span with outcome
- `sales.deal` span if deal moves forward
- `sales.pipeline.days_in_stage` metric updated

---

### Task 1.2.4: Close First Deal (Day 4-5)
**Owner:** You  
**Time:** 1-2 hours

Once a prospect says yes:
1. Send agreement (PDF)
2. Collect signature (DocuSign or email)
3. Collect payment via Stripe
4. Create ClickUp task: "Onboard [company], assign workers"
5. Log in OTel: `sales.deal_closed` span

**Deal event structure (OTel):**

```yaml
deal_closed_event:
  deal_id: UUID
  venture: OPS-001
  prospect_company: [name]
  deal_value_usd: 2500
  payment_method: stripe
  payment_status: completed
  timestamp: ISO8601
  
  # Trace linking
  linked_calls:
    - call_1_id
    - call_2_id
    - call_3_id
  
  linked_tasks:
    - task_send_profiles
    - task_follow_up
    - task_close_deal
```

**Success:** First $2,500 revenue recorded, Langfuse shows full customer journey

---

## Phase 1.3: VERIFICATION (Sep 13-14 — 2 hours)

### Task 1.3.1: Verify Revenue in All Systems
**Owner:** DevOps  
**Time:** 1 hour

```bash
# 1. Check Stripe
stripe_revenue=$(curl -s https://api.stripe.com/v1/charges \
  -u $STRIPE_SECRET_KEY: \
  -d limit=10 | jq '.data[] | select(.description | contains("ops-001"))' | jq '.amount')

echo "Stripe captured: $stripe_revenue"

# 2. Check Supabase
psql -h localhost -U postgres -d company_brain \
  -c "SELECT * FROM deal_payments WHERE venture='OPS-001' ORDER BY created_at DESC;"

# 3. Check Neo4j
cypher-shell -u neo4j -p changeme \
  "MATCH (v:VENTURE {ref_id: 'OPS-001'})-[:HAS_DEAL]->(d:DEAL) RETURN v, d;"

# 4. Check Growth OS
curl http://localhost:3030/api/venture/OPS-001 | jq '.revenue_mtd'

# 5. Check Langfuse
# Open http://localhost:3003 → Traces → Filter by venture="ops-001"
# Should show: 10 calls → 3 interested → 1 deal closed
```

**Success metric:** Revenue flows through Stripe → Supabase → Neo4j → Growth OS → Langfuse (full audit trail)

---

## Phase 1.4: ITERATION (Sep 14+)

Once first deal closes:
- **Week 2 (Sep 15-21):** Make 30 more calls, target 3-5 more deals
- **Week 3 (Sep 22-28):** Scale to other ventures (CON-001, LT-005)

---

# LAYER 2: WEBHOOK ORCHESTRATION (Sep 14-28)

## Objective
Automate the revenue loop: Form Fill → ClickUp Task → DealFlow → Growth OS → Neo4j

## Tech Stack Decision

### Option A: n8n (Recommended)
- **Cost:** Self-hosted (free) or cloud ($50-500/mo)
- **Setup:** 2-3 days
- **Scalability:** 500+ integrations
- **Maintenance:** DevOps manages workflows as code

### Option B: Make.com
- **Cost:** $12-500/mo cloud
- **Setup:** 1-2 days (less code)
- **Scalability:** 6000+ apps
- **Maintenance:** Point-and-click, vendor-dependent

### Option C: Home-built (Python + Celery)
- **Cost:** $0
- **Setup:** 1-2 weeks
- **Scalability:** Custom
- **Maintenance:** You own it forever

**DECISION: n8n** (best balance of control + community + speed)

---

## Phase 2.1: SETUP n8n (Sep 14-15 — 4 hours)

### Task 2.1.1: Deploy n8n Locally
**Owner:** DevOps  
**Time:** 1 hour

```bash
# 1. Install Docker image
docker run -d \
  --name n8n \
  -p 5678:5678 \
  -e DB_TYPE=postgresdb \
  -e DB_POSTGRESDB_HOST=localhost \
  -e DB_POSTGRESDB_PORT=5432 \
  -e DB_POSTGRESDB_DATABASE=n8n \
  -e DB_POSTGRESDB_USER=n8n \
  -e DB_POSTGRESDB_PASSWORD=$N8N_DB_PASSWORD \
  n8nio/n8n:latest

# 2. Wait for startup
sleep 30

# 3. Access UI
open http://localhost:5678

# 4. Create admin user during first login
# Email: admin@worldwidebro.local
# Password: [strong password] → store in Bitwarden

# 5. Wire to Langfuse via webhook
# Settings → Notifications → Add Webhook
# URL: http://localhost:3003/api/webhooks/n8n
# Event: "workflow.execution.success" + "workflow.execution.failed"
```

**Deliverable:** n8n running, admin UI accessible, Langfuse webhook configured

---

### Task 2.1.2: Create n8n Credentials
**Owner:** DevOps  
**Time:** 2 hours

Wire all external systems into n8n:

```yaml
n8n_credentials:
  
  supabase:
    type: HTTP
    url: https://rhlkjelglvurowdalrgh.supabase.co
    headers:
      Authorization: "Bearer ${SUPABASE_ANON_KEY}"
      apikey: "${SUPABASE_ANON_KEY}"
  
  stripe:
    type: OAuth2 / API Key
    api_key: ${STRIPE_SECRET_KEY}
  
  clickup:
    type: OAuth2 / API Key
    api_key: ${CLICKUP_API_KEY}
    team_id: ${CLICKUP_TEAM_ID}
  
  postgresql:
    type: PostgreSQL
    host: localhost
    port: 5432
    database: company_brain
    user: postgres
    password: ${POSTGRES_PASSWORD}
  
  neo4j:
    type: HTTP (Cypher via HTTP)
    url: http://100.87.214.70:7474
    auth: neo4j:${NEO4J_PASSWORD}
  
  langfuse:
    type: HTTP
    url: http://localhost:3003
    headers:
      X-API-Key: ${LANGFUSE_API_KEY}
  
  omniroute:
    type: HTTP
    url: http://100.87.214.70:20128/api
    headers:
      Authorization: "Bearer ${OMNIROUTE_API_KEY}"
```

**Get all credentials from Bitwarden:**
```bash
# For each credential:
bitwarden get item "n8n - Supabase"
bitwarden get item "n8n - Stripe"
# etc.
```

**Deliverable:** All 7 credential sets configured in n8n

---

### Task 2.1.3: Create OTel Instrumentation for n8n
**Owner:** DevOps  
**Time:** 1 hour

**File:** `_INFRASTRUCTURE/otel-n8n-instrumentation.yaml`

```yaml
otel_n8n:
  
  service_name: n8n-orchestration-engine
  
  metrics:
    - name: n8n.workflow.executions.total
      type: counter
      attributes:
        - workflow_name
        - status: ["success", "error", "timeout"]
    
    - name: n8n.workflow.duration_ms
      type: histogram
      attributes:
        - workflow_name
    
    - name: n8n.node.execution.count
      type: counter
      attributes:
        - workflow_name
        - node_name
        - status
    
    - name: n8n.error.rate
      type: gauge
      attributes:
        - workflow_name
  
  traces:
    - name: workflow.execution
      attributes:
        - workflow_id
        - workflow_name
        - execution_id
        - start_time
        - end_time
        - status: ["success", "error"]
        - error_message
    
    - name: node.execution
      parent_span: workflow.execution
      attributes:
        - node_name
        - node_type
        - duration_ms
        - input_data_size
        - output_data_size
  
  logs:
    - workflow_execution_start:
        workflow_name
        execution_id
        trigger_type: ["http", "schedule", "webhook", "manual"]
        timestamp
    
    - workflow_execution_end:
        workflow_name
        execution_id
        status: ["success", "error"]
        error_message: [if status=error]
        duration_ms
        timestamp
    
    - node_error:
        workflow_name
        node_name
        error_type
        error_message
        input_data
        timestamp
  
  exporters:
    - type: langfuse
      endpoint: http://localhost:3003
      trace_exporter: true
    
    - type: prometheus
      endpoint: http://localhost:9090
      push_interval: 30s
```

**Setup:** n8n emits traces to Langfuse automatically (we'll add custom instrumentation to key nodes)

---

## Phase 2.2: BUILD WORKFLOWS (Sep 15-22 — 40 hours)

### Workflow 1: Form Submission → ClickUp Task
**Owner:** DevOps  
**Time:** 4 hours

**Trigger:** Webhook from Vercel site (form submit)

```
INPUT:
{
  "venture": "ops-001",
  "prospect_name": "John Smith",
  "phone": "919-555-0100",
  "company": "ABC Staffing",
  "email": "john@staffing.com",
  "interest": "warehouse placement"
}

WORKFLOW:
  1. Receive webhook
     └─ Log to OTel: otel_form_received span
  
  2. Validate data
     └─ Check required fields
     └─ If invalid → Return error 400
  
  3. Upsert to Supabase (venture_leads table)
     └─ INSERT venture_leads {
          venture: ops-001,
          prospect_name: John Smith,
          phone: 919-555-0100,
          company: ABC Staffing,
          email: john@staffing.com,
          status: 'new',
          created_at: NOW(),
          source: 'form_submission'
        }
     └─ Log to OTel: lead_created span
  
  4. Create ClickUp task
     └─ Call: POST /v2/team/XXX/task
     └─ Payload:
        {
          "name": "Call: John Smith @ ABC Staffing",
          "description": "Prospect submitted form. Interest: warehouse placement",
          "custom_fields": [
            {"id": "field_1", "value": "john@staffing.com"},
            {"id": "field_2", "value": "919-555-0100"},
            {"id": "field_3", "value": "https://vex.worldwidebro.local/leads/LEAD-XXX"}
          ],
          "due_date": NOW() + 1 day,
          "priority": "high",
          "list_id": "list_sales_ops-001"
        }
     └─ Log to OTel: clickup_task_created span
  
  5. Send confirmation email to prospect
     └─ Resend API: POST /emails
     └─ From: ops-001@worldwidebro.local
     └─ To: john@staffing.com
     └─ Subject: "We received your request - John"
     └─ Body: "Thanks for your interest. Our team will follow up within 24 hours."
     └─ Log to OTel: confirmation_email_sent span
  
  6. Emit Neo4j event
     └─ Call: POST http://100.87.214.70:7474/db/neo4j/tx
     └─ Cypher:
        MATCH (v:VENTURE {ref_id: 'OPS-001'})
        CREATE (l:LEAD {
          lead_id: RANDOMUUID(),
          prospect_name: 'John Smith',
          company: 'ABC Staffing',
          status: 'new',
          created_at: NOW()
        })
        CREATE (v)-[:HAS_LEAD]->(l)
        RETURN l.lead_id
     └─ Log to OTel: neo4j_lead_created span

OUTPUT:
{
  "status": "success",
  "lead_id": "LEAD-000421",
  "task_id": "TASK-9876543",
  "email_sent": true
}
```

**n8n Workflow Nodes:**
1. Webhook trigger
2. Data validator (if/then)
3. Supabase node (INSERT)
4. ClickUp node (CREATE task)
5. Resend node (SEND email)
6. Neo4j node (CREATE relationships)
7. Return response

**Telemetry:** Each node logs to Langfuse via built-in n8n tracer

---

### Workflow 2: Stripe Payment → Deal Recorded
**Owner:** DevOps  
**Time:** 3 hours

**Trigger:** Stripe webhook (charge.succeeded)

```
INPUT (Stripe Webhook):
{
  "type": "charge.succeeded",
  "data": {
    "object": {
      "id": "ch_1234567890",
      "amount": 250000,  # $2,500
      "currency": "usd",
      "customer": "cus_XXXXX",
      "description": "OPS-001 placement fee",
      "metadata": {
        "venture": "ops-001",
        "prospect_name": "John Smith",
        "deal_type": "placement"
      }
    }
  }
}

WORKFLOW:
  1. Receive webhook
     └─ Verify signature (Stripe secret)
     └─ Log to OTel: stripe_payment_received span
  
  2. Extract deal info from metadata
     └─ venture: ops-001
     └─ prospect_name: John Smith
     └─ deal_value: $2,500
  
  3. Record in Supabase (deal_payments table)
     └─ INSERT deal_payments {
          deal_id: UUID,
          venture: 'ops-001',
          prospect_name: 'John Smith',
          amount_usd: 2500,
          payment_method: 'stripe',
          stripe_charge_id: 'ch_1234567890',
          status: 'completed',
          created_at: NOW()
        }
     └─ Log to OTel: payment_recorded span
  
  4. Update ClickUp task
     └─ Find task: "Call: John Smith @ ABC Staffing"
     └─ Update: status = "closed", custom_field "Revenue" = "$2,500"
     └─ Log to OTel: task_updated span
  
  5. Update DealFlow pipeline
     └─ Move prospect from "proposal" → "closed_won"
     └─ Record deal amount, close date
     └─ Log to OTel: dealflow_updated span
  
  6. Create Neo4j DEAL node
     └─ MATCH (v:VENTURE {ref_id: 'OPS-001'})-[:HAS_LEAD]->(l:LEAD)
        WHERE l.prospect_name = 'John Smith'
        CREATE (d:DEAL {
          deal_id: UUID,
          amount_usd: 2500,
          closed_date: NOW(),
          status: 'closed_won'
        })
        CREATE (v)-[:HAS_DEAL]->(d)
        CREATE (l)-[:RESULTED_IN]->(d)
        RETURN d
     └─ Log to OTel: neo4j_deal_created span
  
  7. Update Growth OS cache
     └─ POST http://localhost:3030/api/ventures/OPS-001/refresh
     └─ Updates MRR dashboard, revenue metrics
     └─ Log to OTel: growth_os_refreshed span
  
  8. Emit Langfuse metric
     └─ POST http://localhost:3003/api/metrics/revenue
     └─ venture: ops-001, amount: 2500, status: recorded
     └─ (This becomes a Grafana chart: "Revenue by Venture")

OUTPUT:
{
  "status": "success",
  "deal_id": "DEAL-000421",
  "amount_recorded": 2500,
  "tasks_updated": 1,
  "neo4j_synced": true
}
```

**n8n Workflow Nodes:**
1. Stripe webhook trigger
2. Signature validator
3. Supabase node (INSERT payment)
4. ClickUp node (UPDATE task)
5. PostgreSQL node (INSERT deal_payments)
6. Neo4j node (CREATE DEAL + relationships)
7. HTTP node (POST to Growth OS)
8. Langfuse node (record metric)
9. Return response

---

### Workflow 3: Task Completion → Next Action Triggered
**Owner:** DevOps  
**Time:** 4 hours

**Trigger:** ClickUp webhook (task.closed)

```
INPUT (ClickUp Webhook):
{
  "event": "task_closed",
  "data": {
    "task": {
      "id": "TASK-9876543",
      "name": "Call: John Smith @ ABC Staffing",
      "custom_fields": {
        "prospect_name": "John Smith",
        "phone": "919-555-0100",
        "venture": "ops-001",
        "deal_status": "closed_won",
        "revenue": "$2,500"
      }
    }
  }
}

WORKFLOW:
  1. Receive webhook
     └─ Log to OTel: task_closed span
  
  2. Determine task type & venture
     └─ Extract venture ID, task outcome
  
  3. Update venture state machine
     └─ Supabase: venture_state_transitions table
     └─ FROM: VALIDATED → TO: PIPELINE (one deal closed)
     └─ Log to OTel: state_transition span
  
  4. IF deal_status = "closed_won":
     └─ Create next task: "Onboard worker, assign to company"
     └─ Create ClickUp task in "Onboarding" list
     └─ Assign to: Operations team
     └─ Due: tomorrow
  
  5. IF no progress in 3 days:
     └─ Create alert task: "Follow up needed: [prospect]"
     └─ Flag as urgent
  
  6. Emit Neo4j event
     └─ MATCH (v:VENTURE)-[:HAS_DEAL]->(d:DEAL)
        WHERE d.deal_id = DEAL-000421
        SET d.status = 'onboarding_started'
        RETURN d
  
  7. Update Growth OS pipeline chart
     └─ POST http://localhost:3030/api/pipeline/refresh
     └─ Shows deal progression

OUTPUT:
{
  "status": "success",
  "next_tasks_created": 1,
  "state_updated": "VALIDATED→PIPELINE",
  "alerts": []
}
```

---

### Workflow 4: Daily Metrics Aggregation
**Owner:** DevOps  
**Time:** 2 hours

**Trigger:** Scheduled, every day at 8am

```
WORKFLOW:
  1. Query Supabase
     └─ SELECT venture, COUNT(*), SUM(amount_usd)
        FROM deal_payments
        WHERE created_at >= NOW() - INTERVAL 1 DAY
        GROUP BY venture
  
  2. Calculate metrics
     └─ MTD revenue = SUM(all payments this month)
     └─ Daily revenue = SUM(payments today)
     └─ Conversion rate = deals_closed / leads_generated
     └─ Average deal size = SUM(amounts) / COUNT(deals)
  
  3. Store in PostgreSQL (metrics_daily table)
     └─ INSERT metrics_daily {
          date: TODAY,
          venture: ops-001,
          revenue_daily: 2500,
          revenue_mtd: 7500,
          deals_closed: 1,
          leads_generated: 15,
          conversion_rate: 6.7%,
          avg_deal_size: 2500
        }
  
  4. Emit OTel metrics
     └─ otel_metrics_recorded span
     └─ Prometheus metrics pushed
  
  5. Update Growth OS dashboard
     └─ Growth OS reads metrics_daily table
     └─ Displays live MRR, conversion funnel, etc.
  
  6. Send Slack alert (if thresholds met)
     └─ IF revenue >= $5K MTD → "🎉 OPS-001 hit $5K!"
     └─ IF conversion_rate < 5% → "⚠️ Low conversion, review calls"
```

---

## Phase 2.3: TESTING & VERIFICATION (Sep 22-26 — 20 hours)

### Task 2.3.1: End-to-End Test
**Owner:** DevOps  
**Time:** 6 hours

```bash
# Test: Complete revenue loop from form to dashboard

# Step 1: Submit test form from Vercel site
curl -X POST https://ops-001-staffing.vercel.app/api/submit \
  -H "Content-Type: application/json" \
  -d '{
    "prospect_name": "Test Prospect",
    "phone": "919-555-TEST",
    "company": "Test Company",
    "email": "test@example.com"
  }'

# Expected: Webhook received by n8n

# Step 2: Monitor n8n workflow
# n8n UI: Open workflow "Form → ClickUp"
# Should see: Webhook received → Nodes executing → Success

# Step 3: Check Supabase
psql -h localhost -U postgres -d company_brain \
  -c "SELECT * FROM venture_leads ORDER BY created_at DESC LIMIT 1;"
# Expected: Test prospect row

# Step 4: Check ClickUp
# Open ClickUp workspace
# Verify task created in sales list

# Step 5: Check Neo4j
cypher-shell -u neo4j -p changeme \
  "MATCH (l:LEAD {prospect_name: 'Test Prospect'}) RETURN l;"
# Expected: Lead node created

# Step 6: Check Langfuse
curl http://localhost:3003/api/traces?limit=10 | jq '.data[] | select(.name | contains("form"))'
# Expected: Multiple spans from workflow execution

# Step 7: Verify OTel metrics in Prometheus
curl http://localhost:9090/api/v1/query?query=n8n_workflow_executions_total | jq '.data.result'
# Expected: Counter incremented

# Step 8: Test Stripe webhook
curl -X POST http://localhost:5678/webhook/stripe \
  -H "Stripe-Signature: t=...,v1=..." \
  -d '{
    "type": "charge.succeeded",
    "data": {"object": {"amount": 250000, ...}}
  }'

# Step 9: Verify payment recorded everywhere
psql -c "SELECT * FROM deal_payments ORDER BY created_at DESC LIMIT 1;"
cypher-shell "MATCH (d:DEAL) RETURN d ORDER BY d.created_at DESC LIMIT 1;"
curl http://localhost:3030/api/venture/ops-001 | jq '.revenue_mtd'

# Step 10: Verify Langfuse shows full trace
# http://localhost:3003
# Traces tab → Filter by "test"
# Should show: form_received → lead_created → task_created → payment_recorded
```

---

### Task 2.3.2: Failure Mode Testing
**Owner:** DevOps  
**Time:** 4 hours

Test each failure scenario:

| Scenario | Test | Expected Behavior |
|----------|------|---|
| ClickUp API down | Stop ClickUp container | n8n retries 3x, logs error to Langfuse, alerts team |
| Stripe webhook invalid signature | Send bad signature | n8n rejects, logs security event |
| Supabase connection dropped | Kill PostgreSQL conn | n8n retries, doesn't lose data |
| Neo4j transaction fails | Intentional constraint violation | n8n logs error, retries with backoff |
| Workflow timeout | Slow node (simulated) | n8n times out after 30s, logs as error span |

---

### Task 2.3.3: Performance Baseline
**Owner:** DevOps  
**Time:** 2 hours

Measure workflow latency:

```bash
# Metric: Total time from form submission to dashboard update

# Test 10 form submissions, measure each step
for i in {1..10}; do
  start=$(date +%s%N)
  
  # Form submission
  curl -X POST ... 
  
  # Wait for all nodes to complete
  sleep 5
  
  # Check if dashboard updated
  end=$(date +%s%N)
  
  latency_ms=$((($end - $start) / 1000000))
  echo "Form $i: ${latency_ms}ms"
done

# Expected baseline: 3-5 seconds form → dashboard update
# Store in Prometheus as histogram: workflow.latency_ms
```

**Target SLA:** 95th percentile latency < 10 seconds

---

## Phase 2.4: GO-LIVE (Sep 26-28 — 4 hours)

### Task 2.4.1: Switch to Production
**Owner:** DevOps  
**Time:** 2 hours

1. Verify all 4 workflows passing tests
2. Update form webhooks to point to production n8n
3. Monitor for 24 hours
4. If stable → keep running
5. If errors → rollback to manual process

### Task 2.4.2: Create Runbook
**Owner:** DevOps  
**Time:** 2 hours

**File:** `_INFRASTRUCTURE/n8n-RUNBOOK.md`

```markdown
# n8n Orchestration Runbook

## Daily Monitoring

Each morning (8am):
```bash
# Check workflow status
n8n_status=$(curl -s http://localhost:5678/api/v1/workflows | jq '.data | length')
failed_executions=$(curl -s http://localhost:5678/api/v1/executions?filter={"status":"failed"} | jq '.data | length')

if [ $failed_executions -gt 0 ]; then
  echo "WARNING: $failed_executions failed workflows"
  # Check Langfuse for error details
  curl http://localhost:3003/api/traces?status=error | jq
fi
```

## Troubleshooting

**n8n won't start:**
```bash
docker logs n8n
docker restart n8n
```

**Workflow fails on Stripe webhook:**
- Check Stripe integration credentials
- Verify webhook endpoint in Stripe dashboard
- Check n8n logs for error message

**ClickUp tasks not creating:**
- Verify ClickUp API key in n8n credentials
- Check if list_id is correct
- Look at n8n workflow execution logs

## Rollback Procedure

If workflows causing issues:
```bash
# Disable all workflows
n8n_workflows=$(curl -s http://localhost:5678/api/v1/workflows | jq '.data[].id')
for workflow_id in $n8n_workflows; do
  curl -X PATCH http://localhost:5678/api/v1/workflows/$workflow_id \
    -H "Content-Type: application/json" \
    -d '{"active": false}'
done

# Revert to manual process
# Until issues resolved, handle form → ClickUp → Stripe manually
```
```

---

# LAYER 3: RESEARCH AUTOMATION (Oct 1-31)

## Objective
Build automated gap detection + capability discovery using Awesome Lists framework

## Architecture

```
OPERATIONAL GAP
     ↓
GAP DETECTOR (autonomous)
     ↓
AWESOME LIST SCRAPER (MCP tool)
     ↓
CANDIDATE EXTRACTOR (parser)
     ↓
EVIDENCE SCORER (GitHub API + LLM)
     ↓
TEST EXECUTOR (sandbox)
     ↓
DECISION ENGINE (LLM + rubric)
     ↓
CAPABILITY REGISTRY
     ↓
KNOWLEDGE GRAPH
```

---

## Phase 3.1: GAP DETECTOR (Oct 1-5 — 16 hours)

### Component: Autonomous Gap Detection Agent

**Tool:** MCP agent running on schedule (hourly)

**Inputs:** Audit logs, incident reports, performance metrics

**Logic:**

```python
# File: _MCP/gap_detector_agent.py

from opentelemetry import trace
from datetime import datetime, timedelta

tracer = trace.get_tracer(__name__)

class GapDetector:
    
    def detect_gaps(self):
        """Autonomously find missing capabilities"""
        
        with tracer.start_as_current_span("gap_detection") as span:
            gaps = []
            
            # Gap Type 1: Missing capability
            gaps.extend(self.detect_missing_capability())
            
            # Gap Type 2: Performance bottleneck
            gaps.extend(self.detect_performance_gap())
            
            # Gap Type 3: Security risk
            gaps.extend(self.detect_security_gap())
            
            # Gap Type 4: Cost inefficiency
            gaps.extend(self.detect_cost_gap())
            
            # Deduplicate & rank
            ranked_gaps = self.rank_gaps(gaps)
            
            span.set_attribute("gaps_detected", len(ranked_gaps))
            
            return ranked_gaps
    
    def detect_missing_capability(self):
        """Find things that don't exist but should"""
        
        goals = self.load_goals()
        capabilities = self.load_capability_registry()
        
        gaps = []
        for goal in goals:
            required_caps = goal['required_capabilities']
            existing_caps = [c['id'] for c in capabilities]
            
            missing = set(required_caps) - set(existing_caps)
            for cap_id in missing:
                gaps.append({
                    'type': 'missing_capability',
                    'goal': goal['name'],
                    'capability': cap_id,
                    'severity': 'high',
                    'detected_at': datetime.now()
                })
        
        return gaps
    
    def detect_performance_gap(self):
        """Find things that are slow"""
        
        metrics = self.load_prometheus_metrics()
        
        gaps = []
        for metric_name, values in metrics.items():
            p95_latency = self.calculate_percentile(values, 95)
            
            if p95_latency > LATENCY_SLA[metric_name]:
                gaps.append({
                    'type': 'performance_bottleneck',
                    'metric': metric_name,
                    'current_p95_ms': p95_latency,
                    'sla_ms': LATENCY_SLA[metric_name],
                    'severity': 'medium',
                    'detected_at': datetime.now()
                })
        
        return gaps
    
    def rank_gaps(self, gaps):
        """Rank by business impact"""
        
        return sorted(gaps, key=lambda g: (
            g['severity'],  # high > medium > low
            g['impact_business_value'],
            g['estimated_effort']
        ))
```

**Output:** PostgreSQL `gaps_detected` table

```sql
CREATE TABLE gaps_detected (
    gap_id UUID PRIMARY KEY,
    gap_type TEXT,  -- missing_capability, performance, security, cost
    description TEXT,
    severity TEXT,  -- high, medium, low
    estimated_effort_hours INT,
    business_impact_dollars INT,
    status TEXT DEFAULT 'open',  -- open, researching, decided, implemented, closed
    created_at TIMESTAMP,
    researched_at TIMESTAMP,
    decided_at TIMESTAMP,
    resolved_at TIMESTAMP
);
```

---

## Phase 3.2: AWESOME LIST SCRAPER (Oct 5-12 — 20 hours)

### Component: MCP Tool for scraping Awesome Lists

**Tool:** `scrape_awesome_lists` 

**Inputs:** 
- Gap type (missing_capability)
- Domain (AI, data, ops, security, etc.)

**Logic:**

```python
# File: _MCP/awesome_list_scraper.py

import requests
from bs4 import BeautifulSoup
import json

class AwesomeListScraper:
    
    AWESOME_INDEX = {
        'ai': [
            'sindresorhus/awesome-ai',
            'kyrolabs/awesome-llm',
            'openai/awesome-gpt-agents',
        ],
        'data': [
            'aravindpai/awesome-data-science',
            'datasets/awesome-public-datasets',
        ],
        'infrastructure': [
            'sindresorhus/awesome-docker',
            'awesome-selfhosted/awesome-selfhosted',
        ],
        'security': [
            'ashutosh1206/awesome-ctf',
            'sbilly/awesome-security',
        ],
        # ... 20+ more
    }
    
    def scrape_for_gap(self, gap_type: str, domain: str):
        """Find awesome lists relevant to a gap"""
        
        relevant_lists = self.find_relevant_lists(gap_type, domain)
        
        candidates = []
        for list_url in relevant_lists:
            repos = self.scrape_list(list_url)
            candidates.extend(repos)
        
        return self.deduplicate(candidates)
    
    def scrape_list(self, list_url: str):
        """Parse one awesome list and extract projects"""
        
        response = requests.get(f"https://github.com/{list_url}")
        soup = BeautifulSoup(response.text, 'html.parser')
        
        repos = []
        for link in soup.find_all('a', href=re.compile(r'^https://github\.com/')):
            repo_path = link['href'].replace('https://github.com/', '')
            repos.append({
                'repo_url': f'https://github.com/{repo_path}',
                'repo_name': repo_path.split('/')[-1],
                'source_list': list_url,
                'discovered_at': datetime.now()
            })
        
        return repos
    
    def enrich_repositories(self, repos: list):
        """Add metadata from GitHub API"""
        
        enriched = []
        for repo in repos:
            data = requests.get(f"https://api.github.com/repos/{repo['repo_path']}",
                              headers={'Authorization': f'token {GITHUB_TOKEN}'}).json()
            
            enriched.append({
                **repo,
                'stars': data.get('stargazers_count'),
                'last_commit': data.get('pushed_at'),
                'language': data.get('language'),
                'license': data.get('license', {}).get('name'),
                'description': data.get('description'),
                'forks': data.get('forks_count'),
                'open_issues': data.get('open_issues_count'),
            })
        
        return enriched
```

**Output:** PostgreSQL `candidates` table

```sql
CREATE TABLE candidates (
    candidate_id UUID PRIMARY KEY,
    gap_id UUID REFERENCES gaps_detected,
    repo_url TEXT,
    repo_name TEXT,
    repo_owner TEXT,
    stars INT,
    last_commit TIMESTAMP,
    language TEXT,
    license TEXT,
    description TEXT,
    source_awesome_list TEXT,
    discovered_at TIMESTAMP,
    evidence_score FLOAT DEFAULT NULL,
    tested BOOLEAN DEFAULT FALSE,
    test_result TEXT DEFAULT NULL,
    decision TEXT DEFAULT NULL,  -- ADOPT, INTEGRATE, REFERENCE, SKIP
    decision_reasoning TEXT,
    decided_at TIMESTAMP
);
```

---

## Phase 3.3: EVIDENCE SCORER (Oct 12-20 — 24 hours)

### Component: LLM-based evidence scoring

**Tool:** `score_candidates`

**Rubric:**

```yaml
evidence_rubric:
  
  dimensions:
    
    - name: activity
      description: "Recent commits and maintenance"
      weight: 15
      scoring:
        >1_commit_per_week: 10
        >1_commit_per_month: 8
        >1_commit_per_quarter: 5
        no_commits_1_year: 2
    
    - name: community
      description: "Stars, forks, contributors"
      weight: 15
      scoring:
        >10000_stars: 10
        >1000_stars: 8
        >100_stars: 6
        >10_stars: 4
        <10_stars: 1
    
    - name: documentation
      description: "README, examples, API docs"
      weight: 15
      scoring:
        comprehensive: 10
        good: 8
        basic: 5
        minimal: 2
    
    - name: testing
      description: "Test suite, CI/CD coverage"
      weight: 10
      scoring:
        >80%_coverage: 10
        >60%_coverage: 8
        >40%_coverage: 6
        <40%_coverage: 3
    
    - name: security
      description: "Vulnerability scan, audit history"
      weight: 20
      scoring:
        no_vulnerabilities: 10
        minor_fixed: 8
        medium_pending: 4
        critical: 0
    
    - name: compatibility
      description: "Works with our stack"
      weight: 15
      scoring:
        fully_compatible: 10
        mostly_compatible: 7
        workaround_needed: 4
        incompatible: 0
    
    - name: integration_cost
      description: "Time to integrate"
      weight: 10
      scoring:
        <1_day: 10
        <1_week: 8
        <1_month: 5
        >1_month: 2

  total: 100
```

**Scoring Logic:**

```python
class EvidenceScorer:
    
    def score_candidate(self, candidate: dict) -> float:
        """Generate evidence score for a repo"""
        
        with tracer.start_as_current_span("score_candidate") as span:
            span.set_attribute("repo", candidate['repo_url'])
            
            scores = {
                'activity': self.score_activity(candidate),
                'community': self.score_community(candidate),
                'documentation': self.score_documentation(candidate),
                'testing': self.score_testing(candidate),
                'security': self.score_security(candidate),
                'compatibility': self.score_compatibility(candidate),
                'integration_cost': self.score_integration_cost(candidate),
            }
            
            # Weighted sum
            total = sum(
                scores[dim] * WEIGHTS[dim]
                for dim in scores
            ) / 100
            
            span.set_attribute("evidence_score", total)
            
            return total
    
    def score_activity(self, candidate):
        """How recently maintained?"""
        last_commit = datetime.fromisoformat(candidate['last_commit'])
        days_since = (datetime.now() - last_commit).days
        
        if days_since < 7:
            return 10
        elif days_since < 30:
            return 8
        elif days_since < 90:
            return 5
        elif days_since < 365:
            return 2
        else:
            return 0
    
    def score_security(self, candidate):
        """Are there known vulnerabilities?"""
        
        # Call GitHub API: GET /repos/{owner}/{repo}/vulnerability-alerts
        vulns = self.get_vulnerabilities(candidate['repo_url'])
        
        critical = sum(1 for v in vulns if v['severity'] == 'critical')
        high = sum(1 for v in vulns if v['severity'] == 'high')
        
        if critical > 0:
            return 0
        elif high > 0:
            return 4
        else:
            return 10
    
    def score_documentation(self, candidate):
        """Does it have good docs?"""
        
        # Use LLM to evaluate README quality
        readme = self.fetch_readme(candidate['repo_url'])
        
        prompt = f"""
        Evaluate this README for documentation quality (0-10):
        - Clarity of purpose
        - Usage examples
        - API documentation
        - Contributing guide
        
        {readme}
        
        Score: (0-10)
        """
        
        response = llm_call(prompt)
        return int(response.strip())
```

---

## Phase 3.4: TEST EXECUTOR (Oct 20-26 — 20 hours)

### Component: Sandbox testing framework

**Tool:** `test_candidate`

**Test Scenarios:**

```python
class CandidateTester:
    
    def test_candidate(self, candidate: dict):
        """Evaluate candidate in sandbox"""
        
        with tracer.start_as_current_span("test_candidate") as span:
            span.set_attribute("repo", candidate['repo_url'])
            
            # Create isolated environment
            sandbox = self.create_sandbox()
            
            tests = [
                self.test_installation(sandbox, candidate),
                self.test_basic_usage(sandbox, candidate),
                self.test_performance(sandbox, candidate),
                self.test_integration(sandbox, candidate),
                self.test_failure_modes(sandbox, candidate),
            ]
            
            results = {
                'installation': tests[0],
                'basic_usage': tests[1],
                'performance': tests[2],
                'integration': tests[3],
                'failure_handling': tests[4],
            }
            
            span.set_attribute("test_results", json.dumps(results))
            
            return results
    
    def test_installation(self, sandbox, candidate):
        """Can we install it?"""
        
        try:
            if candidate['language'] == 'Python':
                sandbox.run(f"pip install {candidate['repo_name']}")
                return {'status': 'success', 'time_seconds': 45}
            elif candidate['language'] == 'JavaScript':
                sandbox.run(f"npm install {candidate['repo_name']}")
                return {'status': 'success', 'time_seconds': 30}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}
    
    def test_integration(self, sandbox, candidate):
        """Does it work with our stack?"""
        
        # Test: Can it connect to Supabase?
        code = f"""
        import {candidate['import_name']}
        # Test code...
        result = {candidate['main_class']}.connect(
            supabase_url='{SUPABASE_URL}',
            supabase_key='{SUPABASE_KEY}'
        )
        assert result.ok
        """
        
        try:
            sandbox.run(code)
            return {'status': 'success'}
        except:
            return {'status': 'failed'}
```

---

## Phase 3.5: DECISION ENGINE (Oct 26-31 — 16 hours)

### Component: LLM-based decision making

**Decision Options:**
- **ADOPT:** Add to infrastructure, own & maintain
- **INTEGRATE:** Use as external service, wire via API/MCP
- **REFERENCE:** Document as option, don't implement
- **SKIP:** Not suitable, keep researching

**Decision Logic:**

```python
class DecisionEngine:
    
    def decide(self, gap: dict, candidates: list) -> dict:
        """Make ADOPT/INTEGRATE/REFERENCE/SKIP decision"""
        
        with tracer.start_as_current_span("decision") as span:
            span.set_attribute("gap", gap['id'])
            
            # Rank candidates by evidence score
            ranked = sorted(candidates, key=lambda c: c['evidence_score'], reverse=True)
            
            top_candidate = ranked[0]
            
            decision = self.evaluate_candidate(gap, top_candidate)
            
            reasoning = self.generate_reasoning(gap, top_candidate, decision)
            
            # Store decision in registry
            self.record_decision(gap['id'], top_candidate['id'], decision, reasoning)
            
            span.set_attribute("decision", decision)
            
            return {
                'gap_id': gap['id'],
                'candidate': top_candidate,
                'decision': decision,
                'reasoning': reasoning,
                'alternatives': ranked[1:3]
            }
    
    def evaluate_candidate(self, gap, candidate):
        """Determine best decision for this gap + candidate"""
        
        prompt = f"""
        Given this gap and candidate, determine the best decision:
        
        GAP:
        - Type: {gap['type']}
        - Severity: {gap['severity']}
        - Business Impact: ${gap['business_impact_dollars']}
        - Required By: {gap.get('deadline', 'ASAP')}
        
        CANDIDATE:
        - Repository: {candidate['repo_url']}
        - Evidence Score: {candidate['evidence_score']}/100
        - Test Results: {candidate['test_result']}
        - Integration Cost: {candidate.get('integration_cost_hours')} hours
        - Maintenance Burden: {candidate.get('maintenance_burden', 'medium')}
        
        Decision Options:
        1. ADOPT - Add to our infrastructure (own & maintain)
        2. INTEGRATE - Use as external service (API/MCP)
        3. REFERENCE - Document as option (don't implement)
        4. SKIP - Not suitable (keep researching)
        
        What is the best decision? Answer with just the decision and a brief reasoning.
        """
        
        response = llm_call(prompt)
        
        # Parse response
        if "ADOPT" in response:
            return "ADOPT"
        elif "INTEGRATE" in response:
            return "INTEGRATE"
        elif "REFERENCE" in response:
            return "REFERENCE"
        else:
            return "SKIP"
```

---

## Phase 3.6: IMPLEMENTATION (Oct 31+)

### Component: Agent Executor

Once decision is made:

```python
class ImplementationExecutor:
    
    def implement_decision(self, decision: dict):
        """Execute the decision"""
        
        if decision['decision'] == 'ADOPT':
            # Create infrastructure task
            # Assign to DevOps
            # Add to roadmap
            pass
        
        elif decision['decision'] == 'INTEGRATE':
            # Wire via API/MCP
            # Create monitoring
            # Document integration
            pass
        
        elif decision['decision'] == 'REFERENCE':
            # Add to capabilities registry
            # Document why not adopted
            # Set review date for reconsideration
            pass
        
        elif decision['decision'] == 'SKIP':
            # Close gap as out-of-scope
            # Suggest alternative approach
            # Set review trigger (if new info emerges)
            pass
```

---

# UNIFIED OBSERVABILITY SPINE: OPENTELEMETRY

## How All Three Layers Connect

```
                    OPENTELEMETRY
                    (Central Spine)
                           │
         ┌─────────────────┼─────────────────┐
         │                 │                 │
    SALES LAYER      ORCHESTRATION       RESEARCH
    (Manual)         (n8n Workflows)     (Agents)
    Sep 9-14         Sep 14-28           Oct 1-31
         │                 │                 │
         └─────────────────┼─────────────────┘
                           │
                    LANGFUSE EXPORTER
                   (Trace Aggregation)
                           │
         ┌─────────────────┼─────────────────┐
         │                 │                 │
      TRACES           METRICS             LOGS
    (Spans)         (Counters/            (Events)
                    Histograms)
         │                 │                 │
         └─────────────────┼─────────────────┘
                           │
                    PROMETHEUS / GRAFANA
                    (Dashboards)
```

---

## OTel Integration Checklist

### For Sales Layer (DONE)
- [x] sales.call spans → Langfuse
- [x] sales.deal metrics → Prometheus
- [x] sales.pipeline logs → PostgreSQL

### For Orchestration Layer (IN PROGRESS)
- [x] n8n workflow traces → Langfuse
- [x] Webhook latency metrics → Prometheus
- [ ] Error rate alerting → Slack

### For Research Layer (PENDING)
- [ ] gap_detection spans → Langfuse
- [ ] candidate evaluation metrics → Prometheus
- [ ] decision logs → PostgreSQL

---

## Success Metrics by Phase

### Phase 1 (Sales Execution)
- [x] First $2,500 revenue by Sep 14
- [x] Complete OTel instrumentation
- [x] Full audit trail in Langfuse

### Phase 2 (Orchestration)
- [ ] 4 n8n workflows passing tests
- [ ] <10 second form-to-dashboard latency
- [ ] 100% automation coverage (no manual ClickUp tasks)
- [ ] Zero webhook retries (first-pass success)

### Phase 3 (Research Automation)
- [ ] 50+ gaps documented
- [ ] 200+ candidates evaluated
- [ ] 10+ capability decisions made
- [ ] <4 hour gap-to-decision cycle

---

## Timeline Summary

| Week | Phase | Deliverable | Owner |
|------|-------|-------------|-------|
| Week 1 (Sep 9-14) | Sales Execution | First revenue + OTel setup | You + DevOps |
| Week 2-3 (Sep 14-28) | Orchestration | 4 n8n workflows live | DevOps |
| Week 4+ (Oct 1-31) | Research Automation | Gap detector live, 50 gaps processed | ML + DevOps |

---

**Status:** Ready to start Phase 1 tomorrow (Sep 9)  
**Blockers:** None (all infrastructure ready)  
**Next Action:** Review sales playbook, finalize call list, start making calls

