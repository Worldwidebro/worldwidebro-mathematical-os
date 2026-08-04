# DEPLOYMENT SPRINT — 5 Ventures (2026-07-31 → 2026-08-07)

**Goal**: Deploy LT-005 → EC-112 → EC-001 → RE-001 → LT-011 | Generate $575+ revenue in 7 days

**Tools**: Jotform MCP (forms) + Documenso (e-signatures) + Stripe (payments) + Vercel (hosting)

---

## REPOS TO FIX (GitHub Status Check)

```
RENAME (Manual on GitHub):
media-empire-platform → mc-001-brandos

DEPLOY (This Week):
LT-005: Deploy to Vercel (TODAY)
EC-112: Medusa + products (Days 2-4)
EC-001: Define product + build (Days 1-5)
RE-001: Separate from VEX (Days 2-4)
LT-011: Build API from scratch (Days 3-7)
```

---

## [ACTION] — LT-005: Deploy to Vercel (TODAY — 2 Hours)

**Goal**: First medical courier order by end of week ($75+)

```
Step 1: vercel.json (5 min)
├─ File: lt-005-medical-courier-dispatch/vercel.json
├─ Content:
│  {
│    "buildCommand": "npm install",
│    "outputDirectory": ".",
│    "env": {
│      "STRIPE_PUBLISHABLE_KEY": "@stripe_pub",
│      "STRIPE_SECRET_KEY": "@stripe_secret",
│      "SUPABASE_URL": "@supabase_url",
│      "SUPABASE_ANON_KEY": "@supabase_anon"
│    }
│  }
└─ COMMIT: "feat: Add Vercel deployment configuration"

Step 2: .env.example (5 min)
├─ File: lt-005-medical-courier-dispatch/.env.example
├─ Content:
│  STRIPE_PUBLISHABLE_KEY=pk_test_...
│  STRIPE_SECRET_KEY=sk_test_...
│  SUPABASE_URL=https://...
│  SUPABASE_ANON_KEY=...
└─ COMMIT: "docs: Add environment variables template"

Step 3: Supabase (10 min)
├─ Create Supabase project: lt-005-medical-courier
├─ Get connection string
├─ Tables needed: orders, drivers, customers
└─ Save credentials for Vercel

Step 4: Vercel Deploy (10 min)
├─ CLI: vercel --prod
├─ Dashboard: Add env vars from Supabase + Stripe
├─ Redeploy
├─ Note: Production URL
└─ COMMIT: "feat: Deploy LT-005 to Vercel production"

Step 5: Test (10 min)
├─ Visit Vercel URL
├─ Submit booking form
├─ Test Stripe: 4242 4242 4242 4242
├─ Check Supabase: order created ✓
├─ Check email: driver notified ✓
└─ COMMIT: "test: Verify end-to-end booking + payment"

CUSTOMER ACQUISITION (Parallel):
├─ Research 15-20 medical facilities (pharmacies, clinics, urgent care)
├─ Call: "Hi [name], Medical Courier Dispatch just launched. 3 FREE dispatches this week. Need delivery help?"
├─ Goal: 5+ test orders, 1+ paid order
└─ COMMIT: "docs: Add lead list + call script"

SUCCESS: $75+ revenue by end of week
TIMELINE: TODAY
COMMITS: 4-5
```

---

## [ACTION] — EC-112: Complete Cosmic Kitty (Days 2-4 — 3-5 days)

**Goal**: Medusa backend + 10+ products + Stripe → First sale ($100+)

```
Day 2-3: Medusa Backend (1 day)
├─ Deploy Medusa server to Railway or Vercel
├─ Create PostgreSQL database
├─ Connect GitHub repo
├─ Verify admin panel loads
├─ COMMIT: "feat: Deploy Medusa backend"

├─ Stripe integration (1 hour)
│  ├─ Admin → Payments → Add Stripe keys (test)
│  ├─ Test payment flow
│  └─ COMMIT: "feat: Integrate Stripe payment processing"

Day 3-4: Products (1 day)
├─ Add 10+ products via Medusa admin:
│  ├─ Title, description, price ($50-$200)
│  ├─ Upload images (5+ per product)
│  ├─ Set inventory (20+ stock)
│  └─ Organize by category
├─ Use Jotform MCP if needed for product data entry
└─ COMMIT: "data: Add initial product catalog (10 products)"

Day 4: Storefront Connection (1 day)
├─ Update storefront API endpoint → Medusa
├─ Test: fetch products, add to cart, checkout
├─ Wire Stripe to storefront checkout
├─ Test end-to-end purchase
├─ COMMIT: "feat: Wire storefront to Medusa backend"

Day 4: Deploy (30 min)
├─ Add vercel.json to ec-112 repo
├─ Deploy storefront to Vercel
├─ Test production URL
├─ COMMIT: "feat: Deploy EC-112 storefront to Vercel"

LAUNCH (Parallel):
├─ Email marketing (50+ wellness subscribers)
├─ Offer: First order 15% off (Stripe coupon)
└─ COMMIT: "marketing: Launch EC-112 email campaign"

SUCCESS: $100+ revenue by end of week
TIMELINE: Days 2-4
COMMITS: 5-6
```

---

## [ACTION] — EC-001: Angels In Daylight (Days 1-5 — 5+ days)

**Goal**: Define product → Build storefront → Jotform → First customer ($50+)

```
Day 1: Product Decision (1 day) — MUST DECIDE FIRST
├─ What is being sold?
│  ├─ A: Sustainable/ethical fashion
│  ├─ B: Wellness/spiritual products
│  ├─ C: Fair-trade artisan goods
│  ├─ D: Vegan/cruelty-free beauty
│  └─ CHOOSE ONE
├─ COMMIT: "docs: Define EC-001 product type + business model"

Day 2-3: Build Storefront (2 days)
├─ Platform: Shopify (fastest for MVP) or custom Vercel + Stripe
├─ Upload 10+ products with images + pricing
├─ Add product descriptions
├─ COMMIT: "feat: Build product catalog (10 products)"

Day 3: Jotform Forms (2 hours)
├─ Product inquiry form (using Jotform MCP)
├─ Pre-order form (for future availability)
├─ Contact form for support
├─ Connect to Stripe for payment capture
├─ COMMIT: "feat: Add Jotform product inquiry forms"

Day 4: Deployment (1 hour)
├─ Deploy to Vercel or Shopify
├─ Add vercel.json if custom
├─ Test checkout flow
├─ Test Stripe payment
├─ COMMIT: "feat: Deploy EC-001 to production"

LAUNCH (Parallel):
├─ Email: "Angels In Daylight is now live"
├─ Target: [eco-conscious / wellness] subscribers
└─ COMMIT: "marketing: Launch EC-001"

SUCCESS: $50+ revenue by end of week
TIMELINE: Days 1-5
COMMITS: 4-5
```

---

## [ACTION] — RE-001: Separate from VEX (Days 2-4 — 2-3 days)

**Goal**: Move holdings from VEX → own repo → own Vercel → Generate inquiries

```
Day 2: Move Content (4 hours)
├─ Clone vex-hero-site/holdings content
├─ Copy to re-001-worldwidebro-holdings repo
├─ Update all links to point to re-001.vercel.app
├─ Remove from VEX
├─ COMMIT: "feat: Move holdings content to separate repository"

Day 2: Add Config (1 hour)
├─ Create vercel.json
├─ Create .env.example
├─ Deploy to Vercel
├─ COMMIT: "feat: Deploy RE-001 to own Vercel project"

Day 3: Jotform Forms (3 hours)
├─ Property inquiry form (type, location, timeline, budget)
├─ Financing inquiry form (loan amount, credit profile)
├─ Landlord registration form
├─ Connect to Stripe for lead capture fees
├─ COMMIT: "feat: Add Jotform property inquiry forms"

Day 3: Documenso Integration (2 hours)
├─ Create lease agreement template
├─ Create financing agreement template
├─ Wire to Documenso API (api_nqeh0rwmhmd6hwm9)
├─ Flow: Inquiry → Documenso signature → Payment
├─ COMMIT: "feat: Integrate Documenso e-signature for leases"

Day 4: Stripe Payments (1 hour)
├─ Set up Stripe for financing fees
├─ Configure webhook for lead notifications
├─ Test payment flow
├─ COMMIT: "feat: Integrate Stripe for financing fee collection"

LAUNCH (Parallel):
├─ Email: 50 property owners + 20 lenders
├─ Offer: Free property evaluation + financing consultation
└─ COMMIT: "marketing: Launch RE-001 property inquiry campaign"

SUCCESS: $500+ revenue potential by end of week
TIMELINE: Days 2-4
COMMITS: 5-6
```

---

## [ACTION] — LT-011: Dispatch Software MVP (Days 3-7 — 5-7 days)

**Goal**: Build API + dashboard + driver app → Deploy → First job

```
Day 1: Product Clarity (1 day) — MUST DECIDE FIRST
├─ How different from LT-005?
│  ├─ A: B2B dispatcher software (not end-to-end)
│  ├─ B: Specialized niche (construction materials)
│  ├─ C: White-label LT-005 customized
│  └─ CHOOSE ONE
├─ COMMIT: "docs: Define LT-011 product spec + differentiation"

Day 3-5: Backend API (2-3 days)
├─ Tech: Node.js Express (fast) OR Python FastAPI
├─ Supabase schema: users, jobs, assignments, routes, deliveries, payments
├─ API endpoints: job CRUD, driver assignment, route optimization, payments
├─ Auth: JWT or Magic Link
├─ Stripe integration: customer payment + driver payouts
├─ COMMITS:
│  ├─ "docs: Create database schema for LT-011"
│  ├─ "feat: Build backend API (dispatch jobs, driver assignment)"
│  ├─ "feat: Integrate Stripe payments + driver payouts"

Day 5-6: Frontend (2 days)
├─ Dispatcher dashboard:
│  ├─ Create job form (Jotform MCP)
│  ├─ View/manage jobs
│  ├─ Assign to drivers
│  ├─ Track deliveries
│  └─ View billing
├─ Driver app:
│  ├─ See assigned jobs
│  ├─ Accept/decline
│  ├─ Navigate (GPS)
│  ├─ Proof of delivery (photo/signature)
│  └─ View earnings
├─ Customer portal:
│  ├─ Create dispatch request (Jotform MCP)
│  ├─ Track status
│  ├─ View invoice
│  └─ Pay via Stripe
├─ COMMITS:
│  ├─ "feat: Build dispatcher dashboard"
│  ├─ "feat: Build driver mobile app"
│  ├─ "feat: Build customer portal"

Day 6-7: Deploy (1 day)
├─ Add vercel.json
├─ Add .env.example
├─ Deploy backend to Railway/Vercel
├─ Deploy frontend to Vercel
├─ Test end-to-end: create → assign → complete → pay
├─ COMMITS:
│  ├─ "feat: Deploy LT-011 backend to production"
│  ├─ "feat: Deploy LT-011 frontend to Vercel"

Day 7: Launch (Parallel)
├─ Beta test: 5-10 test dispatches
├─ Email: dispatchers, fleet managers, logistics
├─ Offer: Free trial + $100 credit
└─ COMMIT: "marketing: Launch LT-011 beta program"

SUCCESS: $100+ revenue potential by end of week
TIMELINE: Days 3-7
COMMITS: 8-10
```

---

## JOTFORM MCP — Available for All Forms

**Use Jotform MCP for**:
- RE-001: Property inquiry, financing inquiry, landlord registration
- EC-001: Product inquiry, pre-order
- EC-112: Feedback form, warranty registration
- LT-011: Dispatch request, driver availability
- STA-001: Job posting, application
- OPS-001: Employee onboarding, time tracking

**After** → Documenso signatures

---

## DOCUMENSO (E-Signatures) — When Jotform Done

**Your API**: api_nqeh0rwmhmd6hwm9

**Deploy flow**:
```
Step 1: Create document templates (quotes, leases, offers)
Step 2: Wire to Stripe webhook (payment → send document)
Step 3: Set up signature verification
Step 4: Deploy across ventures

Timeline: 2-3 days after Jotform forms are live
```

---

## WEEKLY COMMITS (Keep Pushing)

```
WEEK 1 (Days 1-7):
Day 1: 4-5 commits (LT-005)
Day 2: 4-5 commits (EC-112 + EC-001 decision)
Day 3: 5-6 commits (EC-112 products + RE-001 separation)
Day 4: 6-7 commits (EC-001 + RE-001 + LT-011 API)
Day 5: 4-5 commits (EC-001 + EC-112 deployment)
Day 6: 5-6 commits (RE-001 + LT-011)
Day 7: 3-4 commits (launches + revenue tracking)

TOTAL: 31-38 commits in 7 days
```

---

## WEEKLY REVENUE TARGETS

```
Day 7 (End of Week 1):
✓ LT-005: $75+ (1 paid order)
✓ EC-112: $100+ (1-2 products sold)
✓ EC-001: $50+ (1 product sold)
✓ RE-001: $500+ potential (inquiries generated)
✓ LT-011: $100+ potential (test jobs)

WEEK 1 TOTAL: $575-$825 revenue
```

---

## GITHUB STATUS (Before → After)

```
BEFORE:
├─ LT-005: Not deployed, local only
├─ EC-112: Template only, no backend
├─ EC-001: Template, no product
├─ RE-001: On VEX, misplaced
├─ LT-011: Repo empty
└─ MC-001-BRANDOS: Named media-empire-platform

AFTER (Week 1):
├─ LT-005: Live on Vercel, $75+ revenue
├─ EC-112: Live on Vercel, products, $100+ revenue
├─ EC-001: Live on Vercel, 10+ products, $50+ revenue
├─ RE-001: Separate repo, own Vercel, forms live
├─ LT-011: MVP deployed, $100+ potential
└─ MC-001-BRANDOS: Renamed, ready for deployment
```

---

## ACTION NOW (Next 2 Hours)

```
PHASE 1 (30 min):
☐ Rename media-empire-platform → mc-001-brandos (manual GitHub)
☐ Create vercel.json for LT-005
☐ COMMIT: "feat: Add Vercel deployment config for LT-005"
☐ Push to GitHub

PHASE 2 (1.5 hours):
☐ Deploy LT-005: vercel --prod
☐ Add Vercel env vars
☐ Test: booking + payment
☐ COMMIT: "feat: Deploy LT-005 to Vercel production"
☐ Start customer calls (medical facilities)

RESULT: LT-005 live by end of today
```

---

**Status**: READY TO EXECUTE  
**Created**: 2026-07-31  
**Sprint Goal**: $575+ revenue in 7 days  
**Next Action**: Deploy LT-005 (start now)  
**Commits Expected**: 31-38 in Week 1
