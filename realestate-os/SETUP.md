---
name: realestate-os/SETUP
title: Setup Guide
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# Setup Guide

## Prerequisites
- Node.js 20+
- npm or yarn
- Docker & Docker Compose
- Git
- Supabase account (free)
- Stripe account (test mode)

## Step 1: Clone & Install

```bash
git clone https://github.com/worldwidebro/realestate-os.git
cd realestate-os
npm install
```

## Step 2: Supabase Setup

1. Create a new Supabase project at https://app.supabase.com
2. Note your project URL and API keys
3. In Supabase SQL Editor, paste `schema.sql` and run
4. Enable RLS: Auth → Policies tab on each table (should auto-enable)

## Step 3: Stripe Setup

1. Create Stripe account at https://stripe.com
2. Go to Developers → API Keys
3. Copy Secret Key (starts with `sk_test_`)
4. Go to Webhooks → Add Endpoint
5. Endpoint: `http://localhost:3001/api/webhooks/stripe` (dev) or production URL
6. Events: `checkout.session.completed`
7. Copy Signing Secret (`whsec_...`)

## Step 4: Environment Variables

```bash
cp .env.example .env.local
```

Edit `.env.local`:
```
# From Supabase
NEXT_PUBLIC_SUPABASE_URL=https://xxxxx.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJxxx...
SUPABASE_SERVICE_ROLE_KEY=eyJxxx...

# From Stripe
STRIPE_SECRET_KEY=sk_test_xxx
STRIPE_WEBHOOK_SECRET=whsec_xxx

# Local
FRONTEND_URL=http://localhost:3000
NEXT_PUBLIC_API_URL=http://localhost:3001
PORT=3001
```

## Step 5: Start Local Database

```bash
docker-compose up -d
```

Verify:
```bash
docker ps
# Should show postgres and redis running
```

## Step 6: Run Development Servers

Terminal 1 (Frontend):
```bash
npm run dev -w apps/web
```

Terminal 2 (Backend):
```bash
npm run dev -w apps/api
```

Terminal 3 (Optional - watch tests):
```bash
npm run test:watch -w apps/api
```

## Step 7: Test Locally

**Login (Supabase Auth):**
1. Open http://localhost:3000
2. Register: any email + password
3. Check /dashboard
4. Should see empty properties list

**Create Property:**
```bash
curl -X POST http://localhost:3001/api/properties \
  -H "Content-Type: application/json" \
  -H "X-User-ID: your-user-id" \
  -d '{"address":"123 Main St","city":"Austin","state":"TX","zipCode":"78701","unitsCount":2}'
```

**Test Stripe Webhook (locally):**
```bash
stripe listen --forward-to localhost:3001/api/webhooks/stripe
# Copy signing secret → .env.local STRIPE_WEBHOOK_SECRET

# In another terminal:
stripe trigger payment_intent.succeeded
```

## Step 8: Run Tests

```bash
# All tests
npm run test

# Frontend only
npm run test -w apps/web

# Backend only
npm run test -w apps/api

# Watch mode
npm run test:watch -w apps/web
```

## Troubleshooting

**"Cannot find module" errors:**
```bash
npm install
npm run build
```

**Database connection fails:**
```bash
# Check PostgreSQL is running
docker ps

# Restart if needed
docker-compose restart postgres
```

**Stripe webhooks not firing:**
- Verify `STRIPE_WEBHOOK_SECRET` is correct (from `stripe listen` command)
- Use Stripe CLI to test: `stripe trigger checkout.session.completed`

**Port already in use:**
```bash
# Change in .env.local
PORT=3002
# or kill existing process
lsof -i :3001 | awk 'NR!=1 {print $2}' | xargs kill -9
```

## Next Steps

1. **Create your first property:** Use dashboard UI
2. **Invite a tenant:** Assign to a unit (requires tenant registration first)
3. **Test rent payment:** Create payment link → complete Stripe checkout
4. **Check reports:** View P&L and tenant roster

---

For deployment, see README.md **Deployment** section.
