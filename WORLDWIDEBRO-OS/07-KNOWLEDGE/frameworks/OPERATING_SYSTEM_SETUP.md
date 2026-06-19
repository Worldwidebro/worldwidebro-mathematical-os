# 🚀 Operating System Setup & Implementation

**Everything you need to make it autonomous**

---

## What You Built

✅ **OPERATING_SYSTEM_ARCHITECTURE.md**
- 7 AI agents (3 for you, 4 for system)
- 6 delegation workflows
- 4 contractor roles
- Database schema (6 tables)

✅ **n8n_workflows.json**
- 6 automation workflows
- DuckDB queries pre-configured
- Claude agent calls wired

✅ **operating_system_schema.sql**
- All tables created
- Views for dashboards
- Indexes for performance

---

## How to Implement (5 Steps)

### Step 1: Create Database

```bash
# Create DuckDB database
duckdb /Users/acebless/Documents/worldwidebro_os.duckdb

# Import schema
duckdb /Users/acebless/Documents/worldwidebro_os.duckdb < operating_system_schema.sql

# Verify
duckdb /Users/acebless/Documents/worldwidebro_os.duckdb << 'EOF'
SELECT COUNT(*) as table_count FROM information_schema.tables;
EOF
```

### Step 2: Load Ventures

```bash
# Load 712 ventures from venture-hub CSV
python3 load_ventures_unified.py

# This automatically:
# - Inserts to DuckDB
# - Indexes to Chroma
# - Marks as validated
```

### Step 3: Wire n8n

```bash
# Install n8n
npm install -g n8n

# Start
n8n

# In web UI:
# 1. Import Workflows → n8n_workflows.json
# 2. Set credentials:
#    - DuckDB: worldwidebro_os.duckdb
#    - Claude API: your key
#    - Slack: your workspace
# 3. Enable all workflows
```

### Step 4: Create Agent Prompts

```bash
# Create prompt files for each agent
mkdir -p /Users/acebless/Documents/agents

# Agent 1.1 - Briefer
cat > agents/briefer.md << 'EOF'
You are the Briefer.
Generate daily intelligence: new ventures, sector performance, alerts.
Be direct. Keep it < 500 words.
EOF

# Agent 1.2 - Advisor
cat > agents/advisor.md << 'EOF'
You are the Advisor.
Recommend capital moves: Kill (LTV < CAC*2), Double Down (health > 70), Watch (40-70).
Rank by confidence.
EOF

# Agent 2.1 - Classifier
cat > agents/classifier.md << 'EOF'
You are the Classifier.
Classify ventures: sector, stage, business_model, layer, health_score (1-100), top_risks.
Return as JSON.
EOF

# Repeat for: Monitor, Curator, Retriever
```

### Step 5: Test the Loop

```bash
# 1. Add test venture
curl -X POST http://localhost:5678/ventures/new \
  -H "Content-Type: application/json" \
  -d '{"name":"TestVenture","sector":"tech"}'

# 2. Check classification
duckdb worldwidebro_os.duckdb << 'EOF'
SELECT name, sector, classified_by_agent FROM ventures WHERE name='TestVenture';
EOF

# 3. Approve in Slack
# (You'll get a notification)

# 4. Check indexing
duckdb worldwidebro_os.duckdb << 'EOF'
SELECT name, indexed_to_chroma FROM ventures WHERE name='TestVenture';
EOF

# 5. Check agent logs
duckdb worldwidebro_os.duckdb << 'EOF'
SELECT agent_name, action, status FROM agent_logs ORDER BY created_at DESC LIMIT 5;
EOF
```

---

## Your Daily Workflow (After Setup)

### 8:00 AM
- Briefing in Slack
- Read: new ventures, sector changes, alerts
- Time: 5-10 min

### Mondays 9:00 AM
- Weekly advisor report
- Recommendations: kill/pivot/double-down
- You decide

### Anytime (New Venture)
- Comes in via webhook
- AI classifies (automatic)
- Slack notification
- You approve (1 min)
- System indexes (automatic)

### When You Decide
- Mark decision in dashboard
- System notifies contractors
- Archives documentation
- Logs outcome tracking

### Every 6 Hours
- Exception monitoring runs
- Alerts only if important
- No noise otherwise

---

## What Changes

❌ **You Stop:**
- Manually organizing ventures
- Manually tagging documents
- Manually searching data
- Manually creating task lists
- Manually updating dashboards
- Manually logging decisions

✅ **You Focus On:**
- Thinking (what should we do?)
- Deciding (kill/pivot/double-down)
- Allocating capital (where does money go?)
- Setting priorities (what matters?)

---

## Contractor Roles to Hire

### Role 3.1 — Validator
- Approves AI classifications
- Time: 1-2 hours/day
- Pay: $20-30/hour

### Role 3.2 — Builder
- Builds features for ventures
- Time: 40 hours/week
- Pay: $3-6K/month

### Role 3.3 — Operator
- Data collection, manual tasks
- Time: 5-10 hours/week
- Pay: $15-25/hour

### Role 3.4 — Analyst
- Deep research on sectors
- Time: As needed
- Pay: $50-100/report

---

## Success Metrics

| Metric | Target |
|--------|--------|
| Classification accuracy | > 90% |
| Task completion | > 95% on-time |
| Kill accuracy | > 80% would fail |
| Double-down ROI | > 60% grew |
| Cost per venture | < $50/year |
| Agent uptime | > 99% |

---

## Troubleshooting

**Workflows not running?**
- Check n8n is running (http://localhost:5678)
- Check credentials are set
- Check DuckDB path is correct

**Classifications inaccurate?**
- Validator approves only correct ones
- Update Classifier prompt based on feedback
- Re-run on next batch

**Not getting alerts?**
- Check monitoring workflow is enabled
- Check Slack is authenticated
- Manually run query to verify data

**Contractor not completing tasks?**
- Check deadline is reasonable
- Check form is clear
- Split large tasks into smaller ones

---

## The Full Loop

```
YOU (Layer 1)
  ↓
Briefer (Agent 1.1) ← Gets data from DuckDB
  ↓
YOUR DECISION
  ↓
n8n triggers automation
  ↓
Contractors notified
  ↓
Data collection
  ↓
Validator (Contractor) approves
  ↓
Classifier (Agent 2.1) re-processes
  ↓
Indexer (Agent 2.2) stores
  ↓
Back to Briefer
  ↓
LOOP CONTINUES
```

**This is your operating system. Not a tool. Not a dashboard. A system that runs itself.**

You make decisions. Everything else is automated.
