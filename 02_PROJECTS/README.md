# 02_PROJECTS — Active Work & Execution

**Purpose:** All active ventures, sector builds, and in-flight projects. Live execution tracked in real time.

**Canonical Structure:**

## Sector Folders
```
02_PROJECTS/
├── CON/ (Construction)
├── FIN/ (Finance)
├── LT/ (Logistics)
├── RE/ (Real Estate)
├── TECH/ (Technology)
└── COMM/ (Communications)
```

Each sector folder contains:
- `sector-os.md` — Operating system for that sector (build targets, automation loops, revenue model)
- `ventures/` — All ventures in that sector (one folder per `{SECTOR}-{NUM}`)
- `status.csv` — Real-time venture status tracker (updated weekly)
- `roadmap-{QUARTER}.md` — Quarterly sequencing plan

## Venture Folder (e.g., `CON-001/`)
```
CON-001/
├── README.md — Venture one-pager
├── STATUS.md — Current readiness % + blockers
├── ROADMAP.md — 12-week execution plan
├── codebase/ — App code (Next.js, FastAPI, etc.)
├── data/ — Venture-specific data (CSV, JSON)
├── docs/ — Technical docs, API specs, deployment guides
├── scripts/ — Automation (Python, Node, Bash)
└── supabase/ — Database migrations & schemas
```

## Cross-Project Folders
```
02_PROJECTS/
├── _shared/ — Shared components (design tokens, API clients, utilities)
├── _templates/ — Venture bootstrap templates
└── _deployments/ — Deployment configs (Vercel, Railway, Supabase)
```

---

**Key Metadata Files:**

### `venture.json` (per venture)
```json
{
  "id": "CON-001",
  "name": "Ace Construction",
  "sector": "CON",
  "stage": "MVP",
  "revenue_annual": 12000,
  "team_size": 1,
  "urls": {
    "live": "https://example.vercel.app",
    "repo": "https://github.com/Worldwidebro/con-ventures",
    "supabase": "https://example.supabase.co"
  },
  "readiness": 0.35,
  "blockers": ["Payment processing", "Tax compliance"],
  "last_updated": "2026-07-27"
}
```

### `status.csv` (per sector)
```
venture_id,stage,readiness,income_annual,blockers_count,last_update
CON-001,MVP,35%,12000,2,2026-07-27
CON-002,Planned,0%,0,5,2026-07-15
```

---

**Access Rules:**
- ✅ **All ventures are live** — code changes deploy immediately (GitHub → Vercel/Railway)
- 📊 **Status is source of truth** — VENTURE-READINESS-SCORECARD.csv supersedes local status.md
- 🔄 **Supabase is canonical DB** — local SQL files are mirrors; never edit raw data
- 🚀 **Deploy = 1 command** — `npm run deploy` or equivalent in each venture
- 📋 **Roadmaps are negotiable** — user + Claude agree before committing to dates

**How to Navigate:**
1. **Want to work on a venture?** → `cd 02_PROJECTS/{SECTOR}/{venture-id}` → read STATUS.md for context
2. **Need venture context?** → Read `venture.json` + `STATUS.md` (sync to Supabase if needed)
3. **Deploying?** → Verify `supabase/migrations` are applied, then `npm run deploy`
4. **Adding a new venture?** → Copy from `_templates/{sector-template}/`, fill in `venture.json`, update `status.csv`

---

**Sync Rules:**
- Every venture has `venture.json` as its identity
- `status.csv` pulls data from Supabase nightly (automatic via GitHub Actions)
- Repo links must be `worldwidebro/{sector}-ventures`
- Live URLs must be publicly accessible (demo credentials in venture.json under `demo_login`)

---

**Last Updated:** 2026-07-27
