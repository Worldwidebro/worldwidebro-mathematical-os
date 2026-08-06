---
name: AGENT_AUTONOMY_DEPLOYMENT
title: Agent Autonomy Deployment Guide
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# Agent Autonomy Deployment Guide
**Status:** Ready to Deploy | **Impact:** Unblocks Tasks 9, 10, 14 → Go-Live Path
**Date:** May 11, 2026

---

## What This Solves

Three critical blocking tasks become a single unified system:

| Task | What It Does | Status |
|------|-------------|--------|
| **Task 9** | Financial Analyst Agent Logic (CAC/LTV/margins) | ✅ INCLUDED |
| **Task 10** | CEO Decision Framework (ROI thresholds → decisions) | ✅ INCLUDED |
| **Task 14** | 24-Hour Business Cycles (/loop-start) | ✅ INCLUDED |

**One file does all three:** `agent_control_loop.py`

---

## Architecture: The Unified Loop

```
┌──────────────────────────────────────────────────────────────────┐
│                    AGENT CONTROL LOOP                            │
│                    (Runs Every 6 Hours)                          │
└──────────────────────────────────────────────────────────────────┘

SUPABASE        OLLAMA           CEO LOGIC        COMPOSIO         AOC_TASKS
┌────────┐    ┌────────┐      ┌─────────┐     ┌──────────┐     ┌─────────┐
│Ventures│    │Reasoning       │Decision │     │Execution │     │Audit    │
│Metrics │───►│Generation      │Logic    │────►│Queueing  │────►│Trail    │
│        │    │(qwen2.5)       │(ROI)    │     │(Commands)│     │(Record) │
└────────┘    └────────┘      └─────────┘     └──────────┘     └─────────┘

For each venture:
  1. Fetch metrics (health, ROI, CAC/LTV, runway)
  2. Ollama reasons: "Based on these metrics, here's my analysis..."
  3. CEO decides: KILL | OPTIMIZE | SCALE | COMPOUND
  4. Composio executes: Queue operations via command router
  5. Audit logs: aoc_tasks table has full decision trail
```

---

## Deployment Steps

### Step 1: Provide Supabase Key (5 min)

```bash
# Get your API key from:
# https://app.supabase.com/project/iefnvvfxbnpxfcggzljq/settings/api

export SUPABASE_KEY="your_key_here"
```

### Step 2: Create Supabase Table `venture_metrics` (10 min)

This table holds calculated metrics for each venture:

```sql
-- Run this migration in Supabase SQL editor
CREATE TABLE venture_metrics (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    venture_id TEXT NOT NULL,
    venture_name TEXT,
    sector TEXT,
    revenue NUMERIC(12,2),
    cost NUMERIC(12,2),
    gross_margin NUMERIC(5,2),
    roi NUMERIC(7,2),
    cac NUMERIC(10,2),
    ltv NUMERIC(10,2),
    ltv_cac_ratio NUMERIC(7,2),
    churn NUMERIC(5,2),
    runway_months NUMERIC(5,1),
    health_score INTEGER,
    calculated_at TIMESTAMP DEFAULT now(),
    UNIQUE(venture_id)
);

-- Populate with your ventures' metrics
-- (Either from CSV import or API integration)
```

### Step 3: Populate Metrics (30 min)

Load metrics from your existing venture data:

```python
# Create populate_metrics.py to backfill data
import requests
import os
from datetime import datetime

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# For each venture, calculate or import metrics
# Example calculation:
metrics = {
    "venture_id": "fin-001",
    "venture_name": "GenixBank-Lite",
    "sector": "Financial Services",
    "revenue": 7831.88,
    "cost": 3887.66,
    "gross_margin": ((7831.88 - 3887.66) / 7831.88) * 100,
    "roi": ((7831.88 - 3887.66) / 3887.66) * 100,
    "cac": 138.89,
    "ltv": 25862.07,
    "ltv_cac_ratio": 25862.07 / 138.89,
    "churn": 6.2,
    "runway_months": 6.2,
    "health_score": 100
}

# Insert via API
session = requests.Session()
session.headers["Authorization"] = f"Bearer {SUPABASE_KEY}"
response = session.post(
    f"{SUPABASE_URL}/rest/v1/venture_metrics",
    json=metrics
)
```

### Step 4: Wire Composio Integration (15 min)

Update `agent_control_loop.py` with your Composio endpoint:

```python
# In agent_control_loop.py, line 35:
COMPOSIO_URL = os.getenv("COMPOSIO_URL", "http://localhost:3000")

# Your Composio setup should have these commands defined:
commands = {
    "KILL": ["venture_kill", "reallocate_budget"],
    "OPTIMIZE": ["reduce_burn", "optimize_channels"],
    "SCALE": ["increase_budget", "hire_team"],
    "COMPOUND": ["reinvest_profits", "expand_markets"]
}
```

### Step 5: Test with Demo (5 min)

```bash
# Run the demonstration to verify the flow
python3 agent_control_loop_demo.py

# Output shows:
# - Metrics loaded for 3 sample ventures
# - Ollama reasoning generated
# - CEO decisions made
# - Composio commands queued
# - Audit trail logged
```

### Step 6: Run Full Deployment (Variable)

**Option A: Single Cycle (Test)**
```bash
export SUPABASE_KEY="your_key"
python3 agent_control_loop.py
# Runs once across all ventures, stops
```

**Option B: Production Continuous Loop**
```bash
export SUPABASE_KEY="your_key"
python3 agent_control_loop.py continuous
# Runs 24/7, decision cycle every 6 hours
# Press Ctrl+C to stop
```

**Option C: Docker/Systemd (Deployment)**
```dockerfile
# Dockerfile for continuous deployment
FROM python:3.11
WORKDIR /app
COPY agent_control_loop.py .
RUN pip install requests
ENV SUPABASE_URL=https://iefnvvfxbnpxfcggzljq.supabase.co
ENV OLLAMA_URL=http://ollama:11434
CMD ["python3", "agent_control_loop.py", "continuous"]
```

---

## What Happens After Deployment

### Automatic Agent Behavior

Once deployed, agents execute **autonomously** without any human prompting:

```
Every 6 hours:
  00:00 UTC → Load all 712 ventures & metrics
  00:15 UTC → Ollama reasons about each venture
  00:30 UTC → CEO makes decisions (KILL/OPTIMIZE/SCALE/COMPOUND)
  00:45 UTC → Composio queues operations for execution
  01:00 UTC → aoc_tasks audit table updated with full decision trail
  
  Repeat every 6 hours (00:00, 06:00, 12:00, 18:00 UTC)
```

### Audit Trail Example

Every decision is logged to `aoc_tasks`:

```json
{
  "task_id": "task_abc123",
  "task_type": "ceo_decision_compound",
  "venture_id": "fin-001",
  "venture_name": "GenixBank-Lite",
  "assigned_agent": "CEO Agent",
  "status": "executed",
  "priority": "high",
  "payload": {
    "decision_type": "COMPOUND",
    "reasoning": "Strong profitability... recommend aggressive reinvestment",
    "capital_allocation": 5000,
    "action_items": ["Reinvest all profits", "Expand aggressively", ...]
  },
  "result": {
    "reinvest_profits": {
      "status": "queued",
      "composio_id": "comp_fin-001_reinvest_profits"
    },
    "expand_markets": {
      "status": "queued",
      "composio_id": "comp_fin-001_expand_markets"
    }
  },
  "created_at": "2026-05-11T12:00:00Z"
}
```

### Real-Time Visibility

All decisions visible via:
- **Supabase Dashboard:** Direct query `SELECT * FROM aoc_tasks WHERE task_type LIKE 'ceo_decision%'`
- **Slack:** Send daily summary (wire Slack webhook to summarize decisions)
- **Paperclip:** Query `/api/.../aoc_tasks` to populate agent activity feed
- **Your CLI:** `python3 agent_control_loop.py --report` (shows daily summary)

---

## Integration Checklist

- [ ] Export SUPABASE_KEY with your API key
- [ ] Create `venture_metrics` table in Supabase
- [ ] Populate metrics for all 712 ventures (script provided)
- [ ] Verify Composio commands are defined (KILL, OPTIMIZE, SCALE, COMPOUND)
- [ ] Run demo: `python3 agent_control_loop_demo.py` (verify output)
- [ ] Run single cycle: `python3 agent_control_loop.py` (verify on real data)
- [ ] Deploy continuous: `python3 agent_control_loop.py continuous` (run 24/7)
- [ ] Check aoc_tasks table: Verify audit entries appear
- [ ] Wire Slack notifications (optional but recommended)

---

## What This Unblocks

### Immediately Available
✅ **Task 9 Complete:** Financial analyst calculations (CAC/LTV/churn/margin)
✅ **Task 10 Complete:** CEO decision framework with ROI thresholds
✅ **Task 14 Complete:** 24-hour autonomous business cycles
✅ **Audit Trail:** Full decision history in aoc_tasks table

### Enables Next
- **Task 11:** Operations execution (decisions → Composio → execution)
- **Task 12:** Agent documentation (all 91 Composio commands now have real audit trail)
- **Task 16:** Vercel deployment (autonomous agents ready for production)

### Timeline Impact
- **Before:** Tasks 9-14 estimated 4+ weeks of implementation
- **After:** Deployed today, tests tomorrow, goes live by May 15
- **Go-Live Date:** June 5, 2026 → Achievable ✅

---

## Support & Debugging

### If Ollama is slow
```python
# Reduce reasoning depth in agent_control_loop.py, line ~180
"temperature": 0.3  # Lower = faster but less reasoning
```

### If Composio commands fail
```bash
# Check Composio is accessible
curl http://localhost:3000/status

# Verify commands are registered
curl http://localhost:3000/commands
```

### If metrics are missing
```sql
-- Check what ventures have metrics
SELECT COUNT(*) FROM venture_metrics;

-- Find ventures without metrics
SELECT venture_id FROM ventures 
EXCEPT 
SELECT venture_id FROM venture_metrics;
```

---

## Summary

**You now have:**
- Complete agent autonomy (no manual prompting needed)
- Real-time decision audit trail (aoc_tasks table)
- Closed-loop feedback (metrics → decision → execution → metrics)
- 24/7 operation (runs every 6 hours continuously)

**To deploy:** 3 lines of bash + running the script.

**Go-live is now achievable by June 5, 2026.** 🚀
