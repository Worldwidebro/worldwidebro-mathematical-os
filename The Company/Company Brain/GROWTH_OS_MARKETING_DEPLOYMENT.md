# Growth OS → Marketing Site Deployment

**Current state:**
- ✅ Growth OS live at `localhost:3030` (Python http.server, real data)
- ✅ Repo: https://github.com/Worldwidebro/worldwidebro-marketing-os
- ✅ Wired to: 5 ventures (CON-001, OPS-001, LT-005, LT-011, RE-001)

**Target state:**
- Deploy to Vercel as public marketing dashboard
- Show pipeline visibility (real revenue in real-time)
- Integrate with VEX Hero (portfolio site)

---

## DEPLOYMENT (Sep 15-16, 4 hours)

### Step 1: Convert to Vercel-Ready (1 hour)
**Current:** Python http.server + local file serving  
**Target:** Next.js or static HTML + API routes

**Option A: Keep as static + API (Fastest)**
```bash
# Commit current build to Vercel
cd worldwidebro-marketing-os
vercel deploy

# Vercel will serve static HTML
# Add env vars: DEALFLOW_API, GROWTH_OS_API
```

**Option B: Convert to Next.js (Better)**
```bash
# Move HTML to public/
# Create API routes → /api/ventures, /api/pipeline
# Deploy to Vercel
vercel deploy
```

### Step 2: Wire Real Data (2 hours)
**Add API endpoints:**

```python
# In _MCP/growth_os_api.py (new)

@app.get("/api/ventures")
def get_ventures():
    """Return all 5 ventures with live pipeline"""
    return {
        "ventures": [
            {
                "id": "OPS-001",
                "name": "CareerOps Staffing",
                "pipeline": 2500,
                "monthly_target": 50000,
                "status": "active"
            },
            # ... 4 more ventures
        ]
    }

@app.get("/api/pipeline/{venture_id}")
def get_pipeline(venture_id):
    """Return deal pipeline for venture"""
    return {
        "prospecting": 2500,
        "proposal": 1200,
        "closed_won": 0,
        "closed_lost": 0
    }
```

### Step 3: Integrate with VEX Hero (1 hour)
**Add to vex-hero-site (Vercel):**

```html
<!-- In vex-hero/pages/growth-os.tsx -->

<iframe
  src="https://growth-os.vercel.app"
  width="100%"
  height="1200"
  title="Growth OS — Real-time Pipeline"
/>
```

---

## DEPLOYMENT CHECKLIST (Sep 15)

- [ ] Convert Growth OS to Vercel-ready (static + API routes)
- [ ] Add API endpoints: /api/ventures, /api/pipeline
- [ ] Wire DealFlow API for real deal data
- [ ] Deploy to Vercel (`vercel deploy`)
- [ ] Add to VEX Hero as embedded dashboard
- [ ] Test live: make a test call, see pipeline update in real-time
- [ ] Add to marketing site: "Live Pipeline" link

---

## RESULT

**Public URL:** https://growth-os.vercel.app  
**Embedded in:** https://vex-hero-site-sigma.vercel.app/growth-os  

**Shows:**
- Real-time deal pipeline (updated by agent executions)
- Venture status + revenue targets
- Monthly progress (MTD, YTD)
- Agent activity log

**Marketing value:** "See your venture operations live. Real-time pipeline visibility. Powered by AI agents."

---

## TIMELINE

- Sep 15 morning: Deploy to Vercel
- Sep 15 afternoon: Wire to DealFlow
- Sep 16: Test + integrate with VEX Hero
- Sep 19: Live + visible in growth projections

