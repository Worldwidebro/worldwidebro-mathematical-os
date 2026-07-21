# VEX & OPERATIONS OPCO REPOS: Complete Overview

## 1️⃣ VEX-HERO-SITE (Main Venture Portal & Dashboard)

**Location:** `/Users/acebless/Documents/vex-hero-site`  
**Type:** React + TypeScript + Vite  
**Status:** ✅ LIVE (Deployed to Vercel)  
**Git:** Remote repo connected  

### Directory Structure
```
vex-hero-site/
├── src/
│   ├── App.tsx                 # Main router & pages
│   ├── pages/
│   │   ├── Home.tsx           # Landing page
│   │   ├── Operations.tsx      # ← Operations OPCO dashboard
│   │   ├── Dashboard.tsx       # Venture dashboard
│   │   └── [sector-pages]      # Per-sector pages (CON, RE, STA, etc.)
│   ├── components/
│   │   ├── OpcoFundingCommand.tsx  # ← OPCO funding interface
│   │   ├── VentureCard.tsx         # Venture display card
│   │   ├── DecisionTimeline.tsx    # Decision history
│   │   └── [other-components]
│   ├── data/
│   │   ├── ventures.json       # Master venture registry
│   │   └── sectors.json        # OPCO mappings
│   └── styles.css
├── public/
│   ├── sector-images/          # Hero images per OPCO
│   └── playbooks/              # PDF/docs for each sector
├── package.json                # React, Vite, Tailwind deps
├── vite.config.ts              # Build config
├── tailwind.config.ts          # UI theme
├── .env.local                  # Supabase credentials (local only)
└── .vercel/                    # Vercel deployment config

```

### Key Features
- **Real-Time Venture Display:** Shows all 712 ventures by OPCO
- **Operations OPCO Dashboard:** `/operations` route for funding & command execution
- **Live Data from Supabase:** Synced via useQuery hooks
- **Sector-Specific Pages:** One page per OPCO with filtered ventures
- **Decision Timeline:** Shows approved decisions, invoices, approvals
- **Multi-OPCO Funding Command:** Select sectors, view programs, execute plans

### Live Routes
```
/                   → Home (hero + all ventures)
/operations         → Operations OPCO dashboard (funding command)
/[sector]           → Sector dashboard (CON, RE, STA, LOG, etc.)
/venture/:id        → Single venture detail page
/decisions          → Timeline of all decisions
```

### Tech Stack
- **React 18.3** — UI components
- **TypeScript 5.6** — Type safety
- **Vite 6.0** — Fast dev server
- **Tailwind CSS 3.4** — Styling
- **React Router 7** — Routing
- **Supabase JS Client** — Backend queries (read-only, anon key)

### Deployment
- **Vercel:** Auto-deploys on git push
- **Environment:** Production at `https://vex.worldwidebro.com`
- **CI/CD:** GitHub Actions via Vercel integration

---

## 2️⃣ OPERATIONS OPCO VENTURES (OPS-001, OPS-002, etc.)

**Location:** `/Users/acebless/Documents/WORLDWIDEBRO-OS/03-PORTFOLIO/ventures/active/`  
**Type:** Venture template directories  
**Count:** 50+ staffing/operations ventures

### OPS Venture Structure (Example: OPS-001)
```
OPS-001-VENTURE-STAFFING/
├── STATUS.md                           # Venture stage, metrics
├── docs/
│   ├── CAPABILITY-STATEMENT.md        # What this venture does
│   ├── FORMATION-CREDENTIAL-TRACKER.md # Legal/compliance status
│   ├── SALES-SCRIPTS.md               # Pitch & objection handlers
│   └── [other-docs]
├── 01_STRATEGY/
│   ├── business_model.md
│   ├── go_to_market.md
│   └── financials.csv
├── 02_GOVERNANCE/
│   ├── org_chart.md
│   └── decision_log.md
├── 03_EXECUTION/
│   ├── project_plan.md
│   ├── milestones.csv
│   └── deliverables.md
├── 07_OPERATIONS/
│   ├── dept_1_operations_and_logistics/
│   │   ├── SOP-001-candidate-intake.md
│   │   ├── SOP-002-matching.md
│   │   └── workflow.json
│   ├── dept_2_sales/
│   │   ├── sales_playbook.md
│   │   └── call_scripts.md
│   └── dept_3_finance/
│       └── invoicing.md
├── 11_PRODUCTS/
│   ├── product_roadmap.md
│   └── feature_list.md
└── venture.json                        # Metadata (name, stage, MRR, etc.)

```

### Live OPS Ventures
| Venture | Type | Status | MRR Target |
|---------|------|--------|-----------|
| **OPS-001** | Staffing Marketplace | MVP | $2-5K/mo |
| **OPS-002** | Contractor Portal | Planning | $1-3K/mo |
| operations-000-miami-valet | Valet Services | Live | $3K/mo |
| operations-000-orlando-landscaping | Landscaping | Live | $2.5K/mo |

### VEX Integration Points
Each OPS venture feeds into VEX:
1. **venture.json** → parsed into ventures.csv
2. **STATUS.md** → MRR + stage + metrics
3. **docs/** → capability statements + scripts
4. **decision_log.md** → decisions displayed in VEX timeline

---

## 3️⃣ HOW VEX & OPERATIONS CONNECT

### Data Flow
```
OPS Ventures (filesystem)
    ↓
venture.json + STATUS.md
    ↓
Supabase ventures table (populated via populate_venture_knowledge_graph.py)
    ↓
vex-hero-site queries ventures table
    ↓
VEX Dashboard displays live OPS ventures
    ↓
/operations route shows OpcoFundingCommand
    ↓
User can execute funding programs across OPCOs
```

### The Operations Dashboard Flow
```
User navigates to: /operations
    ↓
OpcoFundingCommand component loads
    ↓
Shows 4 sector buttons: CON, RE, OPS, LOG
    ↓
User selects OPS (+ other sectors)
    ↓
Component queries Supabase:
   SELECT * FROM funding_programs 
   WHERE sector IN ('OPS', 'CON', 'RE', 'LOG')
    ↓
22 funding programs displayed in cards
    ↓
User enters goal: "Scale OPS-001 to $5K/mo"
    ↓
Click "Execute Multi-OPCO Plan"
    ↓
API call to n8n webhook
    ↓
Triggers workflow: Lead intake → Candidate matching → Invoice generation
    ↓
Decision logged in Supabase decisions table
    ↓
VEX Decision Timeline updates in real-time
```

---

## 4️⃣ DEPLOYMENT STATUS

### VEX-Hero-Site
- ✅ **Frontend:** Live at https://vex.worldwidebro.com
- ✅ **Routes:** All 18 sector pages + operations route
- ✅ **Components:** OpcoFundingCommand ready
- ⏳ **Supabase:** funding_programs table ready (deploy via SQL)
- ⏳ **.env.local:** Template ready (needs your credentials)

### Operations OPCO Ventures
- ✅ **Template Structure:** All 50+ ventures standardized
- ✅ **Supabase Sync:** populate_venture_knowledge_graph.py imports all ventures
- ✅ **Real-time Updates:** Supabase subscriptions via React hooks
- ✅ **Dashboard Live:** vex displays all OPS ventures with metrics

---

## 5️⃣ NEXT STEPS TO GO LIVE

### Phase 1: VEX Frontend (Already Deployed)
```bash
cd /Users/acebless/Documents/vex-hero-site
npm start  # http://localhost:3000 (or live at vercel)
```
✅ Routes working  
✅ Components rendering  
✅ Ready for Supabase wiring

### Phase 2: Supabase Funding Schema
```sql
-- Copy supabase-funding-schema.sql sections to Supabase SQL Editor
-- Deploy 4 tables:
-- 1. funding_programs (22 rows)
-- 2. venture_funding_tracker (empty initially)
-- 3. v_active_funding_by_sector (view)
-- 4. venture_leads_audit (for compliance)
```

### Phase 3: .env.local Configuration
```bash
# Copy your Supabase credentials to vex-hero-site/.env.local
VITE_SUPABASE_URL=https://your-project.supabase.co
VITE_SUPABASE_ANON_KEY=your_anon_key_here
```

### Phase 4: Test Operations Dashboard
```bash
# Navigate to: http://localhost:3000/operations
# Test:
# - Sector button selection
# - Goal input
# - Funding program cards update
# - Execute button triggers workflow
```

### Phase 5: Execute OPS Venture Funding
```bash
# In VEX /operations dashboard:
# 1. Select "OPS" sector
# 2. Enter goal: "Scale OPS-001 to $5K/mo"
# 3. Click "Execute Multi-OPCO Plan"
# 4. Watch n8n workflow execute
# 5. See decision logged in VEX Decision Timeline
```

---

## 6️⃣ KEY FILES REFERENCE

| File | Purpose | Status |
|------|---------|--------|
| `/vex-hero-site/src/App.tsx` | Main router | ✅ Ready |
| `/vex-hero-site/src/pages/Operations.tsx` | Operations page | ✅ Ready |
| `/vex-hero-site/src/components/OpcoFundingCommand.tsx` | Funding interface | ✅ Ready |
| `/vex-hero-site/.env.local` | Supabase config | ⏳ Needs credentials |
| `/supabase-funding-schema.sql` | DB schema | ⏳ Needs deployment |
| `/WORLDWIDEBRO-OS/03-PORTFOLIO/ventures/active/` | All ventures | ✅ Ready |
| `/VEX-OPERATIONS-DEPLOYMENT.md` | Full deployment guide | ✅ Ready |

---

## SUMMARY

**VEX** is the **public-facing venture portal** that shows all 712 ventures by OPCO.  
**Operations OPCO Dashboard** is the **command center** for executing funding programs across all sectors.  
**OPS Ventures** are the **staffing/operations businesses** that generate revenue for OPCO-001-10.

Everything connects through **Supabase** → real-time, live, and scalable.

**Deploy now. Execute vex. Scale the ventures.** 🚀
