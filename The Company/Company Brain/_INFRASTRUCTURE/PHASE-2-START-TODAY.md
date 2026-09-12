[[STARTHERE]] | [[_INFRASTRUCTURE/README|Infrastructure Hub]] | [[CLAUDE]]

# PHASE 2: START TODAY (Sep 9)

**Goal:** Make first $2,500 revenue by Sep 14  
**Owner:** You + DevOps  
**Time Investment:** 20 hours (Sep 9-14)

---

## ✅ TODAY (Sep 9) — 4 hours

### Task 1: Create Call List
**Time:** 1 hour  
**Output:** `calls/OPS-001-HIGH-PRIORITY-CALLS.csv`

```bash
# Sources:
# 1. LinkedIn Sales Navigator: Search "staffing manager" + "North Carolina" + "20-500 employees"
# 2. Google Maps: Search "staffing agency near Charlotte, NC"
# 3. ZoomInfo / Hunter.io (if available)

# Required columns:
company_name,phone,contact_name,title,company_size,pain_point_signal,source

# Target: 50 companies with verified phone numbers
# Priority: HIGH = hiring freeze, growing, seasonal surge

# Save to: calls/OPS-001-HIGH-PRIORITY-CALLS.csv
```

**Delivery checklist:**
- [ ] 50 companies listed
- [ ] Phone numbers verified (call and verify it's staffing company)
- [ ] Contact names where possible
- [ ] Saved to CSV

---

### Task 2: Write Call Script
**Time:** 30 min  
**Output:** `scripts/OPS-001-CALL-SCRIPT.md`

```markdown
# OPS-001 Call Script (CareerOps Staffing)

## Opener (15 seconds)
"Hi [name], this is [you] with CareerOps Staffing. Do you have 2 minutes?"

*If yes → proceed. If no → "Can I call you back [day/time]?"*

## Value Prop (30 seconds)
"We place vetted warehouse workers in North Carolina. Our workers:
- Cost 40% less than temp agencies ($X vs Agency $Y)
- Stay 12+ months (not temp)
- Pre-screened for reliability and background"

## Hook (30 seconds)
"We have 3 workers ready this week. Do you have open warehouse roles?"

*If yes → proceed. If no → "When would you have openings?"*

## Close
"Perfect. I'll send you their profiles with wage expectations and certifications. You can review today?

If they're a fit, the placement fee is $2,500 one-time. No success, no charge."

## Objection Handling

**"We use a temp agency."**
Response: "Many do — but they're paying 40% more and workers leave every 90 days. Our guarantee: if they leave in 6 months, we replace free."

**"$2,500 is expensive."**
Response: "What does it cost you to recruit and train one warehouse worker? Typically $3-5K. We're a fixed fee that saves you time."

**"Let me check with management."**
Response: "Perfect. How about we connect [day] when you have an answer? I'll have profiles ready."

## Closing Questions
1. "Do you have open warehouse roles right now?"
2. "What's your typical wage for warehouse?" (to customize profiles)
3. "Can you review profiles today?" (set follow-up)

## If Interested: Next Steps
1. Send profile packet (3 workers) via email
2. Create ClickUp task: "Follow up with [company] by [date]"
3. Call back in 24-48 hours
```

**Delivery checklist:**
- [ ] Script written and practiced (read aloud 3x)
- [ ] Saved to scripts/OPS-001-CALL-SCRIPT.md
- [ ] Objection handling covers top 5 objections

---

### Task 3: Wire OTel for Sales
**Time:** 2.5 hours  
**Owner:** DevOps

```bash
# Step 1: Create OTel instrumentation wrapper
cat > scripts/sales_otel_wrapper.py << 'EOF'
from opentelemetry import trace, metrics
from opentelemetry.exporter.trace.langfuse import LangfuseSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
import json
from datetime import datetime

# Initialize
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

# Configure Langfuse export
try:
    langfuse_exporter = LangfuseSpanExporter()
    trace.get_tracer_provider().add_span_processor(
        BatchSpanProcessor(langfuse_exporter)
    )
    print("✅ Langfuse exporter configured")
except Exception as e:
    print(f"⚠️ Langfuse exporter failed: {e}")

def log_call(prospect_name, phone, outcome, duration_seconds):
    """Log a sales call to Langfuse"""
    with tracer.start_as_current_span("sales.call") as span:
        span.set_attribute("prospect_name", prospect_name)
        span.set_attribute("phone", phone)
        span.set_attribute("outcome", outcome)
        span.set_attribute("duration_seconds", duration_seconds)
        span.set_attribute("venture", "ops-001")
        span.set_attribute("timestamp", datetime.now().isoformat())
    print(f"✅ Logged call: {prospect_name} ({outcome})")

def log_profile_sent(prospect_name, email):
    """Log when profiles sent"""
    with tracer.start_as_current_span("sales.profile_sent") as span:
        span.set_attribute("prospect_name", prospect_name)
        span.set_attribute("email", email)
    print(f"✅ Logged profile sent to {prospect_name}")

def log_deal_closed(prospect_name, company, amount_usd):
    """Log when deal closes"""
    with tracer.start_as_current_span("sales.deal_closed") as span:
        span.set_attribute("prospect_name", prospect_name)
        span.set_attribute("company", company)
        span.set_attribute("amount_usd", amount_usd)
    print(f"✅ Logged deal closed: {prospect_name} ({company}) = ${amount_usd}")

if __name__ == "__main__":
    # Test
    log_call("John Smith", "919-555-0100", "interested", 300)
    log_profile_sent("John Smith", "john@staffing.com")
EOF

# Step 2: Install dependencies
pip install opentelemetry-api opentelemetry-sdk opentelemetry-exporter-trace-langfuse

# Step 3: Test it
python scripts/sales_otel_wrapper.py

# Expected output:
# ✅ Langfuse exporter configured
# ✅ Logged call: John Smith (interested)
# ✅ Logged profile sent to John Smith
```

**Delivery checklist:**
- [ ] OTel wrapper script created
- [ ] Dependencies installed
- [ ] Test run successful
- [ ] Langfuse dashboard shows test traces (check http://localhost:3003)

---

## ✅ DAY 1-2 (Sep 9-10) — 6 hours

### Make First 10 Cold Calls

**Script:**
```bash
#!/bin/bash

# Load call list
CALLS="calls/OPS-001-HIGH-PRIORITY-CALLS.csv"

# Make calls 1-10
for i in {1..10}; do
  prospect=$(sed -n "$((i+1))p" $CALLS)  # Skip header
  company=$(echo $prospect | cut -d, -f1)
  phone=$(echo $prospect | cut -d, -f2)
  contact=$(echo $prospect | cut -d, -f3)
  
  echo ""
  echo "📞 Call $i: $contact @ $company"
  echo "   Phone: $phone"
  echo ""
  read -p "Press ENTER to dial, then enter outcome (interested/objection/voicemail/declined):"
  read outcome
  read -p "Duration (seconds):"
  read duration
  
  # Log to OTel
  python -c "
from scripts.sales_otel_wrapper import log_call
log_call('$contact', '$phone', '$outcome', $duration)
"
  
  # Log locally
  echo "$i,$company,$contact,$phone,$outcome,$duration,$(date)" >> calls/OPS-001-CALL-LOG.csv
done

echo ""
echo "✅ Calls complete. Check Langfuse: http://localhost:3003"
```

**Delivery checklist:**
- [ ] 10 calls made
- [ ] Call log CSV created
- [ ] Outcomes recorded (1 in Langfuse, 1 in CSV)
- [ ] **Target:** 2-3 prospects "interested" by end Day 2

---

## ✅ DAY 3-4 (Sep 11-12) — 4 hours

### Send Profiles & Follow Up

**For each "interested" prospect:**

1. **Create profile packet** (PDF or email)
   ```markdown
   # Worker Profiles — [Company Name]
   
   ## Worker 1: [Name]
   - Experience: Warehouse, 8 years
   - Certifications: OSHA, Forklift
   - Availability: Immediate
   - Wage expectation: $16/hour
   
   [Similar for Worker 2 & 3]
   
   **Placement Fee:** $2,500 (one-time)
   **Guarantee:** If worker leaves within 6 months, we replace free
   ```

2. **Send email**
   ```
   To: [prospect email]
   Subject: 3 Warehouse Workers Ready This Week — [Company]
   
   Hi [name],
   
   Following up from our call yesterday. I've attached profiles for 3 warehouse workers 
   ready to start this week.
   
   Can you review today and let me know if any are a fit?
   
   [Your name]
   [Your phone]
   ```

3. **Log in OTel**
   ```bash
   python -c "
from scripts.sales_otel_wrapper import log_profile_sent
log_profile_sent('[prospect name]', '[email]')
"
   ```

4. **Create ClickUp task**
   - Title: "Follow up with [prospect] re: profiles"
   - Due: tomorrow
   - List: "Sales Pipeline"
   - Custom fields: prospect email, phone, company

---

## ✅ DAY 5 (Sep 13) — 2 hours

### Close First Deal (or Schedule Follow-up)

**If prospect says "yes" to a profile:**

1. **Send agreement** (Google Doc or PDF)
   ```markdown
   # Staffing Placement Agreement
   
   Company: [company name]
   Contact: [prospect name]
   Worker: [worker name]
   Start Date: [date]
   
   Placement Fee: $2,500 (due upon acceptance)
   
   [Standard T&Cs]
   ```

2. **Collect payment via Stripe**
   ```bash
   # Option A: Send Stripe invoice link
   # Option B: Take payment directly (quickest)
   # Option C: Wire (slowest but acceptable)
   ```

3. **Log deal closed**
   ```bash
   python -c "
from scripts.sales_otel_wrapper import log_deal_closed
log_deal_closed('[prospect name]', '[company]', 2500)
"
   ```

4. **Create ClickUp task: Onboard**
   - Title: "Onboard worker: [worker] → [company]"
   - Assign to: Operations
   - Due: start date

5. **Verify revenue in all systems**
   ```bash
   # Stripe
   curl https://api.stripe.com/v1/charges -u $STRIPE_KEY: | grep "ops-001"
   
   # Supabase
   psql -h localhost -c "SELECT * FROM deal_payments WHERE venture='OPS-001';"
   
   # Langfuse
   # Open http://localhost:3003 → Traces
   # Filter: "sales"
   # Should see complete journey: call → profile_sent → deal_closed
   ```

---

## ✅ DAY 5-6 (Sep 13-14) — Verification

### Verify Revenue Flows Through All Systems

```bash
#!/bin/bash

echo "🔍 Verifying revenue pipeline..."

# 1. Stripe
echo ""
echo "1️⃣ Checking Stripe..."
stripe_charges=$(curl -s https://api.stripe.com/v1/charges \
  -u $STRIPE_SECRET_KEY: \
  --data-urlencode "limit=20" | jq '.data | length')
echo "   Charges captured: $stripe_charges"

# 2. Supabase
echo ""
echo "2️⃣ Checking Supabase..."
psql -h localhost -U postgres -d company_brain \
  -c "SELECT COUNT(*) as deal_count FROM deal_payments WHERE venture='OPS-001';" \
  -c "SELECT SUM(amount_usd) as total_revenue FROM deal_payments WHERE venture='OPS-001';"

# 3. Neo4j
echo ""
echo "3️⃣ Checking Neo4j..."
cypher-shell -u neo4j -p changeme \
  "MATCH (v:VENTURE {ref_id: 'OPS-001'})-[:HAS_DEAL]->(d:DEAL) 
   RETURN COUNT(d) as deal_count, SUM(d.amount_usd) as total_usd;"

# 4. Langfuse
echo ""
echo "4️⃣ Checking Langfuse..."
langfuse_traces=$(curl -s http://localhost:3003/api/traces?limit=100 | jq '.data | length')
echo "   Traces recorded: $langfuse_traces"

# 5. Grafana
echo ""
echo "5️⃣ Checking Grafana..."
echo "   Open: http://localhost:3011"
echo "   Dashboard: OPS-001 Revenue"
echo "   Should show: MTD revenue = [total from Supabase]"

echo ""
echo "✅ Verification complete!"
echo ""
echo "🎉 If all systems show $2,500+, PHASE 1 SUCCESS!"
```

**Success Criteria:**
- [ ] Stripe shows payment captured
- [ ] Supabase shows deal_payments row
- [ ] Neo4j shows DEAL node linked to VENTURE
- [ ] Langfuse shows complete trace (call → profile → deal)
- [ ] Grafana dashboard updated

---

## 📊 Tracking

### Call Log (Track Manually)
```csv
# calls/OPS-001-CALL-LOG.csv
call_num,company,contact,phone,outcome,duration_sec,timestamp
1,ABC Staffing,John Smith,919-555-0100,interested,180,2026-09-09T10:30:00Z
2,XYZ HR,Sarah Johnson,919-555-0101,voicemail,0,2026-09-09T10:45:00Z
3,Staffing Plus,Tom Wilson,919-555-0102,interested,240,2026-09-09T11:00:00Z
...
```

### Conversion Funnel (Tracked in Langfuse)
```
Calls Made: 10
├─ Connected: 8 (80%)
├─ Interested: 2-3 (20-30%)
├─ Profiles Sent: 2-3
├─ Deal Closed: 1
└─ Revenue: $2,500
```

---

## If Something Goes Wrong

**OTel not working?**
```bash
# Check if Langfuse is running
curl http://localhost:3003/health

# If not, start it
docker-compose -f _INFRASTRUCTURE/docker-compose.yml up langfuse -d

# Check logs
docker logs civos_langfuse
```

**Supabase query failing?**
```bash
# Test connection
psql -h localhost -U postgres -d company_brain -c "SELECT 1;"

# If fails, check Docker
docker ps | grep postgres
docker logs civos_postgres
```

**Stripe payment not showing?**
```bash
# Check Stripe API key
echo $STRIPE_SECRET_KEY

# Test API call
curl https://api.stripe.com/v1/charges \
  -u $STRIPE_SECRET_KEY: \
  --data-urlencode "limit=1"
```

---

## Next: Phase 2 (Sep 14)

Once first deal closes and revenue confirmed:
- DevOps starts setting up n8n (see PHASE-2-IMPLEMENTATION-ROADMAP.md)
- Goal: Automate form → ClickUp → DealFlow by Sep 28

---

**Timeline:**
- Sep 9: Setup (4 hours)
- Sep 9-10: Calls 1-10 (6 hours)
- Sep 11-12: Profiles & follow-up (4 hours)
- Sep 13-14: Close deals (2 hours)
- **Total: 16 hours**

**Success Metric:** First $2,500 revenue by EOD Sep 14 ✅

