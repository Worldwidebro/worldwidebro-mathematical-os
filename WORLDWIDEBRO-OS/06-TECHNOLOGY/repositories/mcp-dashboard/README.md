# 🚀 MCP Dashboard — LOCAL TESTING (NO CONVEX, NO DEPLOYMENT)

A standalone React + Vite dashboard for testing MCP servers locally before production deployment.

## 📊 What This Does

Tests all 4 MCP components in sequence:

1. **Step 1:** Tool Router (localhost:9002) — routes tasks to Smithery MCPs
2. **Step 2:** Temporal Workflow (localhost:7233) — orchestrates 5-step venture launch
3. **Step 3:** Smithery MCPs (ports 9010-9013) — Stripe, GitHub, Postgres, Supabase
4. **Step 4:** Full Orchestration — end-to-end venture launch

## 🏃 Quick Start

### Prerequisites
- Node.js 18+
- Docker (for Temporal)
- Smithery CLI

### Install & Run

```bash
# 1. Install dependencies
npm install

# 2. Install Smithery MCPs locally
bash services/smithery-installer.sh

# 3. Start Temporal cluster
docker-compose up -d

# 4. Start Tool Router
node services/tool-router.js  # Runs on localhost:9002

# 5. Start Dashboard (new terminal)
npm run dev  # Runs on localhost:5174
```

### Test the 4 Steps

Open http://localhost:5174 and click buttons in order:

1. **Step 1: Test Tool Router** — Verifies localhost:9002 works
2. **Step 2: Test Temporal** — Verifies localhost:7233 works
3. **Step 3: Fetch Ventures** — Loads 669 ventures from Supabase
4. **Step 4: Launch Test Venture** — Full orchestration (5-step DAG)

## 🔌 Architecture

```
MCP Dashboard (React)
       ↓
Tool Router (localhost:9002)
       ↓
Smithery MCPs (localhost 9010-9013)
       ├─ Stripe (9010)
       ├─ GitHub (9011)
       ├─ Postgres (9012)
       └─ Supabase (9013)
       ↓
Temporal Workflow (localhost:7233)
       ↓
5-Step Venture Launch DAG
```

## 📋 Environment

Copy `.env.example` to `.env.local` and fill in:

```bash
cp .env.example .env.local
```

Then add your keys:
- `STRIPE_API_KEY` — test key from Stripe dashboard
- `GITHUB_TOKEN` — from GitHub settings
- `SUPABASE_URL` & `SUPABASE_API_KEY` — from Supabase dashboard

## 🎯 What Gets Tested

| Step | Tests | Tools | Cost |
|------|-------|-------|------|
| 1 | Tool routing | Tool Router → Smithery | $0 |
| 2 | Workflow orchestration | Temporal DAG | $0 |
| 3 | Data loading | Supabase queries | $0 |
| 4 | Full automation | Venture launch | $0 |

**Total cost: $0** (all local, no cloud deployment)

## 📊 Success Criteria

After running all 4 steps:

- ✅ Step 1 shows "Tool Router works"
- ✅ Step 2 shows "Temporal Workflow works"
- ✅ Step 3 loads 10 ventures from database
- ✅ Step 4 launches test venture with full DAG

## 🚀 Next Steps

After local testing passes:

1. Deploy Tool Router to production (Vercel/Railway)
2. Deploy Temporal cluster to production (Temporal Cloud)
3. Wire into The Office (Convex) — import tested MCPs
4. Scale to 250+ ventures/month

## 📞 Troubleshooting

### "Connection refused: localhost:9002"
→ Tool Router not running: `node services/tool-router.js`

### "Connection refused: localhost:7233"
→ Temporal not running: `docker-compose up -d`

### "Smithery not found"
→ Install CLI: `npm install -g @smithery/cli`

### "No .env.local"
→ Copy template: `cp .env.example .env.local`

---

**Cost to test before production: $0**
**Time to validate 4 steps: 5-10 minutes**
**Risk: Zero (local only)**
