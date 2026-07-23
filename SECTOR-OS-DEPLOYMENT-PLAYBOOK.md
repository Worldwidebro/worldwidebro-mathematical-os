---
title: Sector Operating Systems Deployment Playbook
version: 1.0
date: 2026-07-23
status: Active
---

# Sector OS Deployment Playbook

5 production-grade sector dashboards + Hermes meta-orchestration layer.

## Operating Systems (5)

| OS | OPCO | Repo | Agents | Status | Subdomain |
|----|------|------|--------|--------|-----------|
| NexusDispatch | Logistics (LOG) | `nexus-dispatch` | 8 | Built | `logistics-os.` |
| TerraOS | Real Estate (RE) | `terra-os` | 11 | Built | `realestate-os.` |
| BuildOS | Construction (CON) | `build-os` | 12 | Built | `construction-os.` |
| GrowthOS | Marketing | `growth-os` | 24 modules | Built | `growth-os.` |
| Hermes Command | Meta Layer | `hermes-command-center` | Orchestration | Built | `hermes.` (internal) |

## Missing (3 OPCOs)

- **Staffing OS** (STA-*) — Contractor graph, skills, payroll, crew scheduling
- **Education OS** (EDU-*) — Curriculum, students, content delivery
- **Finance OS** (FIN-*) — Ledger, risk models, treasury, compliance

## Architecture

```
vex-hero-site (landing)
  ├─ /sectors/logistics → nexus-dispatch.domain
  ├─ /sectors/realestate → terra-os.domain
  ├─ /sectors/construction → build-os.domain
  ├─ /sectors/marketing → growth-os.domain
  └─ /sectors/staffing → staffing-os.domain (TODO)

Each OS
  ├─ Next.js 15 frontend (dashboard)
  ├─ API routes (Supabase client + Neo4j queries)
  ├─ Auth middleware (check user OPCO role)
  └─ Deployed: Vercel (frontend) + Edge functions (API)

Hermes (admin/meta)
  ├─ Agent lifecycle management
  ├─ Cross-sector orchestration
  ├─ User/permission governance
  └─ Deployed internally (Tailscale accessible)
```

## Repo Structure (Per OS)

```
nexus-dispatch/
├─ app/
│  ├─ (auth)/
│  │  └─ login/page.tsx
│  ├─ dashboard/
│  │  ├─ page.tsx
│  │  ├─ agents/page.tsx
│  │  ├─ shipments/page.tsx
│  │  └─ finance/page.tsx
│  ├─ api/
│  │  ├─ auth/route.ts
│  │  ├─ shipments/route.ts
│  │  ├─ agents/[id]/route.ts
│  │  └─ webhook/stripe/route.ts
│  └─ layout.tsx
├─ lib/
│  ├─ supabase.ts (client + server)
│  ├─ neo4j.ts (graph queries)
│  ├─ auth.ts (session validation)
│  └─ constants.ts (agent rosters, integrations)
├─ components/
│  ├─ dashboard/
│  ├─ charts/
│  ├─ forms/
│  └─ shared/ (design system)
├─ public/
│  ├─ logo.svg
│  └─ icons/
├─ .env.example
├─ next.config.js
├─ tailwind.config.js
├─ package.json
└─ README.md
```

## Environment Variables (.env.local)

```bash
# Auth
NEXT_PUBLIC_SUPABASE_URL=https://xxx.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=xxx
SUPABASE_SERVICE_ROLE_KEY=xxx

# Neo4j (graph)
NEO4J_URI=bolt://neo4j.internal:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=ventures2026

# Qdrant (vectors)
QDRANT_URL=http://qdrant.internal:6333

# Stripe (payments)
STRIPE_SECRET_KEY=sk_live_xxx
STRIPE_WEBHOOK_SECRET=whsec_xxx
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_live_xxx

# Auth0 / Clerk (if using)
AUTH_SECRET=xxx
AUTH_PROVIDERS=...

# OS metadata
OPCO_NAME=Logistics
OPCO_SLUG=LOG
SECTOR_COLORS={"primary":"#10b981","accent":"#f59e0b"}
```

## Deployment Checklist

### Pre-Deploy
- [ ] Build passes: `npm run build`
- [ ] Tests pass: `npm test`
- [ ] Code review approved
- [ ] Environment variables set in Vercel dashboard
- [ ] Database migrations applied (Supabase)
- [ ] Neo4j indices created for performance

### Deploy
```bash
git push origin main  # triggers Vercel auto-deploy
# OR manual:
vercel deploy --prod
```

### Post-Deploy (Verify)
- [ ] Dashboard loads at subdomain
- [ ] Auth redirects work (redirect to /login if not authed)
- [ ] Supabase queries respond (check network tab)
- [ ] Chart.js renders (no 404 on CDN)
- [ ] Agents appear on dashboard (API call succeeded)
- [ ] Stripe webhooks fire (test with Stripe CLI)
- [ ] Error tracking live (Sentry / Vercel Logs)

### Rollback
```bash
vercel rollback  # reverts to previous deployment
# Or redeploy specific commit:
vercel deploy --prod --target=commit-sha
```

## Auth Flow

1. User visits `nexus-dispatch.domain`
2. Middleware checks for `auth_token` cookie
3. If missing → redirect to vex-hero-site login
4. Login validates `user.opco_role` against required OPCO
5. Token set, redirect to `/dashboard`
6. All API routes verify token before querying data

```typescript
// middleware.ts (runs on every request)
import { NextRequest, NextResponse } from 'next/server';

export function middleware(request: NextRequest) {
  const token = request.cookies.get('auth_token')?.value;
  
  if (!token && !request.nextUrl.pathname.startsWith('/login')) {
    return NextResponse.redirect(new URL('/login', request.url));
  }
  
  return NextResponse.next();
}

export const config = {
  matcher: ['/((?!_next/static|_next/image|favicon.ico).*)'],
};
```

## Data Integration

### Supabase Queries
```typescript
// lib/supabase.ts
import { createClient } from '@supabase/supabase-js';

export const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL,
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY
);

// Use in API routes:
const { data: shipments } = await supabase
  .from('shipments')
  .select('*')
  .eq('opco', 'LOG')
  .gte('created_at', sevenDaysAgo);
```

### Neo4j Queries
```typescript
// lib/neo4j.ts
import neo4j from 'neo4j-driver';

const driver = neo4j.driver(
  process.env.NEO4J_URI,
  neo4j.auth.basic(process.env.NEO4J_USER, process.env.NEO4J_PASSWORD)
);

export async function getAgentRoster(opco: string) {
  const session = driver.session();
  const result = await session.run(
    `MATCH (a:Agent)-[:ASSIGNED_TO]->(o:OPCO {name: $opco})
     RETURN a.name, a.status, count(a.tasks) as tasks`,
    { opco }
  );
  await session.close();
  return result.records.map(r => ({ ...r.toObject() }));
}
```

### Qdrant Vector Search
```typescript
// lib/vectors.ts
import { QdrantClient } from '@qdrant/js-client-rest';

const client = new QdrantClient({
  host: process.env.QDRANT_URL.split('://')[1],
  port: 6333,
});

export async function searchShipments(query: string, opco: string) {
  const results = await client.search('shipments', {
    vector: await embed(query),
    filter: { must: [{ key: 'opco', match: { value: opco } }] },
    limit: 10,
  });
  return results.map(r => r.payload);
}
```

## Monitoring & Observability

### Vercel Analytics
- Built-in Core Web Vitals
- Error tracking via Vercel Logs
- Deployment history & rollback one-click

### Sentry (optional)
```typescript
import * as Sentry from "@sentry/nextjs";

Sentry.init({
  dsn: process.env.NEXT_PUBLIC_SENTRY_DSN,
  tracesSampleRate: 1.0,
  environment: process.env.NODE_ENV,
});
```

### Database Monitoring
- Supabase dashboard: row counts, slow queries
- Neo4j: query performance via browser UI (localhost:7474)
- Qdrant: collection stats via API

### Health Checks
```bash
# Add to Hermes orchestration
curl https://nexus-dispatch.domain/api/health
# Returns: { status: 'ok', uptime: 123456, agents: 8, timestamp: '...' }
```

## Cross-OS Communication

Hermes knows all OS deployments:

```typescript
// In Hermes only
const SECTOR_OS = {
  LOG: 'https://nexus-dispatch.domain',
  RE: 'https://terra-os.domain',
  CON: 'https://build-os.domain',
  MKT: 'https://growth-os.domain',
  STA: 'https://staffing-os.domain', // TODO
  EDU: 'https://education-os.domain', // TODO
  FIN: 'https://finance-os.domain', // TODO
};

// Hermes can query any OS:
async function fetchAgentStatus(opco: string) {
  const url = `${SECTOR_OS[opco]}/api/agents/status`;
  return fetch(url, { headers: { Authorization: `Bearer ${HERMES_TOKEN}` } });
}
```

## Scaling Considerations

### Database Load
- Each OS queries its OPCO's data only (filter by opco_slug)
- Index on `(opco_slug, created_at)` for all tables
- Cache results in Redis for 5-min dashboards

### Agent Concurrency
- Each OS can run up to N agents (set in ENV)
- Hermes allocates compute budget across OPCOs
- If LOG needs 8 agents + CON needs 12, budget: 20 total

### Cost
- Vercel: $20/mo per OS (5 × $20 = $100 base)
- Supabase: ~$25–50/mo (shared)
- Neo4j/Qdrant: ~$50–100/mo (shared)
- **Total:** ~$200–250/mo for full suite

## Vex Integration (GitHub Awareness)

### Sector Pages Route to OS Cores

Each `vex-hero-site/sectors/{slug}` page links to corresponding `iza-os-{sector}-core` deployed on Vercel:

```
User visits vex-hero-site
  ↓
Clicks sector (construction, staffing, etc.)
  ↓
Page shows "Core" nav link or hero CTA
  ↓
Routes to: https://{sector}-os.{domain}
  ↓
Vercel redirects to deployed iza-os-{sector}-core
  ↓
Auth middleware checks user.opco_role
  ↓
Dashboard filters ventures by OPCO (CON-*, STA-*, etc.)
```

### Core-Venture Map

**File:** `IZA-OS-CORE-VENTURE-MAP.json`

Maps each GitHub core repo to:
- Venture ID (CON-001, STA-001, etc.)
- vex sector page URL
- Deployed OS subdomain
- Ventures powered (all CON-*, all STA-*, etc.)

**Example:** User clicks "Construction" sector on vex → routed to `construction-os.domain` → loads ConstructionOS dashboard → sees all CON ventures (jobs, crews, compliance).

### Naming Convention

```
GitHub repo:      iza-os-{sector}-core
Vercel subdomain: {sector}-os
vex sector page:  /sectors/{slug}

Examples:
- iza-os-construction-core → construction-os → /sectors/construction
- iza-os-staffing-core → staffing-os → /sectors/staffing
- iza-os-logistics-core → logistics-os → /sectors/transportation
- iza-os-marketing-core → growth-os → /sectors/marketplace
```

---

## Next Steps

1. **Rename con-os-build** → iza-os-construction-core (via `gh repo rename`)
2. **Create missing core repos** (staffing, education, finance)
3. **Wire vex-hero-site routing** (sectors.ts → each core's subdomain)
4. **Deploy cores to Vercel** with auth + data integration
5. **Test end-to-end** (vex sector click → OS loads → ventures display)
6. **Add Hermes orchestration** for cross-core communication

---

## Reference Files

- **Mapping:** `IZA-OS-CORE-VENTURE-MAP.json` (core repos, venture counts, vex routes)
- **Sectors config:** `vex-hero-site/src/data/sectors.ts` (16 sectors, 7 with cores)
- **Deployment:** Each `iza-os-{sector}-core/README.md` includes sector link

## Reference Commits

- Init + Next.js setup: `git log --oneline | head -1`
- Supabase integration: search for `supabase`
- Auth middleware: search for `middleware.ts`
- Deployment: `vercel logs`
