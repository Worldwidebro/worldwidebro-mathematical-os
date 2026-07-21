# Framework Analysis: pm-skills vs agency-agents vs loop-engineering

## 1. LOOP ENGINEERING
**Repo:** cobusgreyling/loop-engineering  
**Status:** Production (13K stars, active)  
**Purpose:** Design the system that prompts agents (not prompt each time manually)

### What It Does
```bash
npx @cobusgreyling/loop-init .
```
Scaffolds:
- `LOOP.md` — describe your automation loops
- `STATE.md` — track state, metrics, run logs
- `loop-budget.md` — track token costs
- `loop-constraints.md` — define boundaries
- Grades your loop readiness (0-100 score)

### For CON-001
✅ **Use for:** Defining the 8 loops (Lead Intake, Estimator, Bid Coord, etc.)  
✅ **Gives:** Structured loop design + state tracking + budget visibility  
✅ **Effort:** Low (just documentation, not code)

### Example Output
```
LOOP Ready Score: 45/100
├─ Loop design: ✅ Complete
├─ State tracking: ⚠️ Partial (need STATE.md)
├─ Budget: ⚠️ Missing (need loop-budget.md)
├─ Constraints: ⚠️ Missing
└─ Automation: ⚠️ Not deployed yet
```

---

## 2. PM-SKILLS
**Repo:** phuryn/pm-skills  
**Status:** Active (23.7K stars)  
**Purpose:** 100+ agentic skills for product/project management

### What It Does
Provides **skills** (reusable operations) for:
- Discovery (user research, competitor analysis)
- Strategy (roadmapping, prioritization)
- Execution (sprint planning, backlog grooming)
- Launch (go-to-market, measurement)
- Growth (retention, monetization)

### For CON-001
❓ **Use for:** General agentic commands?  
❌ **Problem:** Designed for product/software, not construction operations  
❌ **Gap:** No skills for: lead intake, estimating, subcontractor bidding, job costing

### What's Missing
```
pm-skills has:
✅ Backlog prioritization
✅ User story generation
✅ Launch planning

But NOT:
❌ Lead scoring for construction
❌ Blueprint estimation
❌ Subcontractor bid coordination
❌ Project profitability tracking
❌ Lien waiver automation
```

**Verdict:** Useful for other ventures (SaaS, content, marketplace), but not for CON-001's specific needs.

---

## 3. AGENCY-AGENTS
**Repo:** msitarzewski/agency-agents (131K stars)  
**Status:** Very active, production-grade  
**Purpose:** Pre-built AI agents with personalities and specialized workflows

### Available Agents (15+ roles)
- **Briefer** — Daily summaries, reports
- **Classifier** — Categorization, scoring
- **Monitor** — Anomaly detection, alerts
- **Curator** — Content generation, summaries
- **Frontend Wizard** — UI building
- **Reality Checker** — QA validation
- **Whimsy Injector** — Creative features
- (+ 8 more)

### For CON-001
✅ **Use Briefer for:** Daily team briefing (leads, projects, revenue)  
✅ **Use Classifier for:** Lead scoring (budget, timeline, complexity)  
✅ **Use Monitor for:** Anomaly detection (overdue projects, unpaid invoices)  
✅ **Use Curator for:** Proposal generation (scope, pricing summary)

### How to Invoke
```bash
# agency-agents gives you a pre-built agent with personality
# You wire it into your loop via n8n webhook

POST /webhook/classifier
{
  "email": "Customer inquiry about roofing...",
  "context": "CON-001 lead intake"
}
→ Returns: {priority: "high", budget: "$50K", timeline: "2 weeks", complexity: "medium"}
```

**Verdict:** EXCELLENT. These 4 agents directly map to 4 of your 8 loops.

---

## Integration Strategy

```
Loop Engineering (design)
         ↓
Define 8 loops in LOOP.md
         ↓
Agency-Agents (execute)
         ↓
Wire 4 agents (Classifier, Briefer, Monitor, Curator)
         ↓
N8n (automate)
         ↓
Procore/QB APIs
         ↓
CON-001 revenue
```

---

## What's Working in CON-001 RIGHT NOW?

| Component | Status | Evidence |
|-----------|--------|----------|
| Next.js app | ✅ Deployed | repo on main, clean git status |
| Vercel hosting | ✅ Live | .vercel/ exists, next.config.mjs |
| Supabase connection | ⚠️ Unknown | venture.json says "yes" but not confirmed |
| Stripe integration | ❌ Pending | venture.json: "stripe-pending" |
| Forms/UI | ⚠️ Unknown | Need to check pages/ directory |
| ClickUp integration | ❌ Nope | No mention in venture.json |

---

## TEST PLAN (This Hour)

### Phase 1: Test CON-001 App
```bash
cd CON-001-Ace-Construction
npm install
npm run build
npm run dev
# Visit http://localhost:3000
# Test: Can you submit a lead form?
# Test: Does it hit Supabase?
```

### Phase 2: Test Loop Engineering Scaffold
```bash
cd /Users/acebless/Documents
npx @cobusgreyling/loop-init CON-001-loops --tool claude
# Generates:
#   - LOOP.md (describe 8 loops)
#   - STATE.md (track state)
#   - loop-budget.md (token costs)
# Gives: Loop Ready score
```

### Phase 3: Test Agency-Agents
```bash
# Clone repo, read the agent specs
# Test: Can we invoke Classifier agent on a sample email?
# Test: Can we wire response into n8n?
```

### Phase 4: Test PM-Skills
```bash
# Read pm-skills repo
# Check: Is there anything for construction operations?
# Verdict: Keep or skip
```

---

## Execution Order

1. **RUN TESTS** (30 min)
   - [ ] Test CON-001 app (forms, Supabase)
   - [ ] Test Loop Engineering scaffold (LOOP.md generation)
   - [ ] Test agency-agents (invoke 1 agent)

2. **PLAN** (30 min)
   - [ ] Define 8 loops in LOOP.md (using Loop Engineering)
   - [ ] Map 4 agency-agents to loops
   - [ ] Create state tracking (STATE.md)

3. **EXECUTE** (2-3 days)
   - [ ] Week 1: Deploy Loop 1 (Lead Intake) with Classifier agent
   - [ ] Week 2-3: Deploy 7 remaining loops
   - [ ] Week 4: Full testing + production

---

## Decision Matrix

| Framework | Use for CON-001? | Why |
|-----------|------------------|-----|
| **Loop Engineering** | ✅ YES | Design system for 8 loops, state tracking |
| **Agency-Agents** | ✅ YES | 4 pre-built agents (Classifier, Briefer, Monitor, Curator) |
| **PM-Skills** | ❌ SKIP | Designed for software/product, not construction ops |

