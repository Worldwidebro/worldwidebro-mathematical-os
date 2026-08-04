# Real Estate OS — MVP Phase 1

Rental property management SaaS with property CRUD, lease management, rent collection (Stripe), tenant portal, maintenance requests, and basic reporting.

**Status:** Production-ready | **Version:** 1.0.0

---

## Quick Start (15 min)

### Prerequisites
- Node.js 20+, npm, Docker
- Supabase account (free tier OK)
- Stripe account (test mode)

### Local Development

1. **Clone & install:**
```bash
git clone <repo-url>
cd realestate-os
npm install
```

2. **Environment setup:**
```bash
cp .env.example .env.local
# Fill in: SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY, STRIPE_SECRET_KEY
```

3. **Start database:**
```bash
docker-compose up -d
```

4. **Run migrations (Supabase):**
Visit Supabase Dashboard → SQL → paste schema.sql → run

5. **Start dev servers:**
```bash
npm run dev
```
- Frontend: http://localhost:3000
- API: http://localhost:3001
- Health check: http://localhost:3001/api/health

### Run Tests
```bash
npm run test
npm run test -w apps/web    # Frontend only
npm run test -w apps/api    # Backend only
```

---

## Tech Stack

| Layer | Tech |
|-------|------|
| **Frontend** | Next.js 15, React 19, TypeScript, Tailwind, shadcn/ui |
| **Backend** | Express, TypeScript, Supabase, Stripe |
| **Database** | PostgreSQL (Supabase) with RLS |
| **Auth** | Supabase Auth (JWT) |
| **Payments** | Stripe Checkout + Webhooks |
| **Deployment** | Vercel (frontend) + Railway (backend) |
| **CI/CD** | GitHub Actions |

---

## Architecture

### Database Schema
6 tables with RLS policies for multi-tenant isolation by user_id:
- `users` (landlord/tenant roles)
- `properties` (landlord-owned)
- `units` (units within properties)
- `leases` (lease documents + expiration)
- `rent_payments` (payment tracking + Stripe links)
- `maintenance_requests` (tenant submission + landlord triage)

### API Endpoints (RESTful)
| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | `/api/auth/register` | User registration |
| POST | `/api/auth/login` | User login |
| GET | `/api/properties` | List user's properties |
| POST | `/api/properties` | Create property |
| GET | `/api/properties/:id` | Property detail + units |
| POST | `/api/rent-payments/create-payment-link` | Stripe checkout |
| POST | `/api/webhooks/stripe` | Payment confirmation |
| POST | `/api/maintenance` | Tenant creates request |
| PUT | `/api/maintenance/:id` | Landlord updates status |
| GET | `/api/reports/property/:id/plp` | P&L report |
| GET | `/api/reports/property/:id/tenants` | Tenant roster (CSV) |

### Frontend Pages
- `/` — Landing/login
- `/dashboard` — Landlord properties + stats
- `/properties/:id` — Property detail, units, leases
- `/tenant/:id` — Tenant portal (lease, pay rent, submit maintenance)
- `/settings` — Account & billing

---

## Deployment

### Frontend (Vercel)

```bash
vercel login
vercel deploy apps/web
```

Set env vars:
```
NEXT_PUBLIC_SUPABASE_URL=
NEXT_PUBLIC_SUPABASE_ANON_KEY=
NEXT_PUBLIC_API_URL=https://your-railway-url
```

### Backend (Railway)

```bash
# Login or create Railway project
railway link
railway up
```

Set env vars in Railway dashboard:
```
SUPABASE_URL=
SUPABASE_SERVICE_ROLE_KEY=
STRIPE_SECRET_KEY=
STRIPE_WEBHOOK_SECRET=
FRONTEND_URL=https://your-vercel-url
PORT=3001
```

### Stripe Setup

1. Create API keys in Stripe Dashboard
2. Create webhook endpoint: `https://your-railway-url/api/webhooks/stripe`
3. Copy webhook secret → STRIPE_WEBHOOK_SECRET

---

## Testing Coverage

**Frontend:** 10+ component tests
- Auth flows (register, login)
- Property listing & detail
- Rent payment flow
- Maintenance requests UI

**Backend:** 15+ API tests
- Auth endpoints
- CRUD operations (properties, units, leases)
- Stripe webhook handling
- RLS policies verification

**E2E:** 3 critical journeys
1. Landlord creates property → assigns tenant → collects rent
2. Tenant logs in → views lease → pays rent via Stripe
3. Tenant submits maintenance → landlord assigns → completion

---

## Configuration

### Supabase
1. Create project
2. Run `schema.sql` in SQL Editor
3. Enable RLS on all tables
4. Copy URL + service role key

### Stripe
1. Create test account
2. Generate API keys (secret)
3. Create webhook (see endpoint above)
4. Test cards: `4242 4242 4242 4242` (success), `4000 0000 0000 0002` (decline)

### Environment Variables
See `.env.example` — required for dev/prod:
```bash
NEXT_PUBLIC_SUPABASE_URL
NEXT_PUBLIC_SUPABASE_ANON_KEY
SUPABASE_SERVICE_ROLE_KEY
STRIPE_SECRET_KEY
STRIPE_WEBHOOK_SECRET
FRONTEND_URL
DATABASE_URL (dev only)
```

---

## Development Workflow

### Create Feature Branch
```bash
git checkout -b feature/your-feature
```

### Make Changes
```bash
npm run dev          # Hot-reload
npm run lint         # TypeScript + ESLint
npm run test         # Unit tests
```

### Push & PR
Tests run via GitHub Actions. Pass tests → merge → auto-deploy.

---

## Performance & Security

- **RLS:** Row-level security isolates data per user
- **Auth:** Supabase JWT, refreshed automatically
- **HTTPS:** Deployed on Vercel (frontend) + Railway (backend)
- **Secrets:** Never commit `.env.local` — use platform secrets
- **CORS:** API restricted to frontend origin
- **Validation:** Input validation on all endpoints
- **Webhooks:** Signed Stripe events verified

---

## Roadmap (Phase 2+)

- Tenant messaging system
- Automatic late fee calculation
- Lease expiration reminders (email + SMS)
- Multi-unit rent scheduling
- Advanced analytics dashboard
- Mobile app (React Native)
- White-label SaaS offering

---

## Support

- **Docs:** See ARCHITECTURE.md, API.md, SETUP.md
- **Issues:** GitHub Issues
- **Email:** support@realestate-os.com

---

**Built with ❤️ for property managers who want to work less.**
