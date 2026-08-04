# INCOME ACTION PLAN — CON-001 + LT-005

**Objective**: First paying customer for each venture within 7 days  
**Priority**: P0 (revenue-critical)  
**Timeline**: Today → Day 7  
**Target Revenue**: $575+ combined (proof of concept)

---

## [PARALLEL] — Deployment + Customer Acquisition

```
Ventures:
- CON-001 (Ace Construction)
- LT-005 (Medical Courier Dispatch)

Tracks:
- Deployment (24 hours)
- Customer acquisition (Days 1-5)
- Payment processing (Days 6-7)
- Revenue verification (Day 7)

Critical Path:
1. Deploy CON-001 (30 min) + LT-005 (1 hour)
2. Customer research (3 hours)
3. Lead outreach (5-10 calls)
4. Qualification + proposal (4-5 hours)
5. First payment received (proof)
```

---

## [ACTION] CON-001 — Deploy + Acquire First Customer

### Phase 1: Deploy (TODAY — 24 hours)

**Task**: Push Vercel env vars + test

```
1. Get keys:
   └─ Supabase: con-001-ace-construction project
      └─ SUPABASE_URL
      └─ SUPABASE_ANON_KEY
      └─ SUPABASE_SERVICE_ROLE_KEY
   └─ Stripe: dashboard
      └─ STRIPE_PUBLISHABLE_KEY
      └─ STRIPE_SECRET_KEY

2. Deploy:
   └─ Vercel dashboard → Settings → Environment Variables
   └─ Paste all 5 keys
   └─ Redeploy (automatic or manual: vercel --prod)

3. Verify:
   └─ Visit production URL
   └─ Submit test form
   └─ Check Supabase: row created in leads table ✓
   └─ Check email: notification received ✓

Timeline: 30 min total
Owner: User (key gathering) + Vercel (deployment)
Success: Production URL live, form → Supabase working
```

### Phase 2: Customer Acquisition (Days 1-3)

**Task**: 5-10 local construction businesses

```
Research:
├─ Google: "[city] construction services"
├─ Yelp: construction company reviews → phone numbers
├─ Facebook: "[city] construction" groups
├─ LinkedIn: construction company owners
└─ Target: Mix of contractors + homeowner-facing services

Outreach (5-10 calls):
├─ Call script: "Hi [name], Ace Construction just started serving [city]. 
│  Free consultation + estimate this week. Do you have 2 min?"
├─ If yes: "Perfect—I'll send you our form: [url]/contact"
├─ If no: "No problem, I'll email it anyway"
└─ Log: Contact name, company, phone, response

Timeline: 3-5 hours (research + calling)
Owner: User
Success: 5+ leads captured via form
```

### Phase 3: Conversion (Days 4-7)

**Task**: Convert leads to first customer

```
1. Qualification call (2-3 calls):
   ├─ Project type + scope
   ├─ Timeline (urgent = higher priority)
   ├─ Budget ($500-$5000 range)
   └─ Schedule estimate/consultation

2. Proposal (same day):
   ├─ Email project scope + pricing
   ├─ Send Stripe payment link for deposit
   ├─ Schedule consultation call

3. Close (Days 6-7):
   ├─ First customer pays deposit/full amount
   ├─ Record payment in Supabase
   └─ Revenue logged ✓

Timeline: 5-10 hours (qualification + proposal + follow-up)
Owner: User
Success: 1+ customer pays $500+
```

### Success Criteria — CON-001

```
✓ Production URL live
✓ Form submits → Supabase
✓ Email notifications working
✓ 5+ leads captured
✓ 1+ consultation scheduled
✓ 1+ invoice sent
✓ 1+ payment received ($500+)
```

**Revenue Target (Month 1)**: 3 customers × $500-$2000 = $1,500-$6,000

---

## [ACTION] LT-005 — Deploy + Process First Order

### Phase 1: Deploy (Days 1-2)

**Task**: Railway/Vercel + Stripe integration

```
1. Railway setup (15 min):
   └─ railway.app → New Project
   └─ Connect GitHub: worldwidebro/lt-005-medical-courier-dispatch
   └─ Confirm deployment

2. Environment variables (15 min):
   └─ Railway dashboard → Variables
   └─ Add:
      ├─ STRIPE_PUBLISHABLE_KEY
      ├─ STRIPE_SECRET_KEY
      ├─ SUPABASE_URL
      ├─ SUPABASE_ANON_KEY
      └─ SUPABASE_SERVICE_ROLE_KEY

3. Supabase project (15 min):
   └─ Create new Supabase project for LT-005
   └─ Copy connection string
   └─ Paste into Railway variables

4. Test (30 min):
   ├─ Visit production URL
   ├─ Submit booking form
   ├─ Check Supabase: order created ✓
   ├─ Test Stripe payment (use test card: 4242 4242 4242 4242)
   ├─ Verify payment → order marked paid ✓
   └─ Email driver notification received ✓

Timeline: 1 hour total
Owner: User (setup) + Railway (deployment)
Success: Production URL live, booking + payment flow working
```

### Phase 2: Customer Acquisition (Days 2-4)

**Task**: 10-15 medical facilities

```
Research:
├─ Google: "[city] pharmacy" + "clinic" + "urgent care"
├─ Yelp: pharmacy + clinic listings → phone numbers
├─ Industry directory: NCPA.co (pharmacy association)
├─ LinkedIn: medical facility operations managers
└─ Target: pharmacies, clinics, urgent care centers, medical offices

Outreach (10-15 calls):
├─ Call script: "Hi [name], Medical Courier Dispatch just launched 
│  in [city]. FREE dispatch for 3 orders this week. Do you need 
│  help with prescription/lab delivery?"
├─ If yes: "Perfect—booking link: [url]"
├─ If no: "I'll email it anyway—check it out"
└─ Log: Contact name, facility, phone, response

Timeline: 4-6 hours (research + calling)
Owner: User
Success: 5+ test orders completed (free trial)
```

### Phase 3: First Paid Order (Days 5-7)

**Task**: Process 1+ paid dispatch

```
1. Test orders (3 free):
   ├─ Facility places order via form
   ├─ Driver accepts in portal
   ├─ Order marked complete
   ├─ Feedback collected

2. Paid order (1+):
   ├─ Follow-up call: "How was the service? Ready to start paying?"
   ├─ Offer first paid order at 50% discount
   ├─ Send Stripe payment link
   ├─ First customer pays ✓

3. Verify:
   ├─ Payment received in Stripe
   ├─ Order marked paid in Supabase
   ├─ Driver notification sent ✓
   └─ Revenue logged ✓

Timeline: 5-8 hours (test orders + follow-up + payment)
Owner: User
Success: 1+ order paid ($75-$150)
```

### Success Criteria — LT-005

```
✓ Production URL live
✓ Booking form submits → Supabase
✓ Stripe payment flow working
✓ Email notifications to driver
✓ 5+ test orders completed
✓ 1+ paid order processed
✓ Payment received ($75+)
```

**Revenue Target (Month 1)**: 8-12 orders × $75-$150 = $600-$1,800

---

## DEPLOYMENT CHECKLIST (TODAY)

### CON-001

- [ ] Get Supabase keys (con-001 project)
- [ ] Get Stripe keys (Stripe dashboard)
- [ ] Vercel dashboard → Environment Variables
- [ ] Paste 5 keys
- [ ] Redeploy
- [ ] Visit production URL
- [ ] Submit test form
- [ ] Verify Supabase row created
- [ ] Check email received

**Time**: 30 min  
**Owner**: User  
**Blocking**: Everything else until done

### LT-005

- [ ] Create Railway project
- [ ] Connect GitHub repo
- [ ] Confirm deployment
- [ ] Get Supabase keys (create new project)
- [ ] Get Stripe keys
- [ ] Railway Variables → paste keys
- [ ] Supabase connection string → Railway
- [ ] Visit production URL
- [ ] Test booking form
- [ ] Test Stripe payment (card: 4242 4242 4242 4242)
- [ ] Verify Supabase order created
- [ ] Check email sent

**Time**: 1 hour  
**Owner**: User  
**Blocking**: Customer acquisition until done

---

## CUSTOMER ACQUISITION SCRIPTS

### CON-001 (Construction)

**Cold Call (30 sec)**:
```
"Hi [name], this is [you] from Ace Construction. 
We just started offering [service: roofing/electrical/plumbing] 
in [city] and we're booking free consultations this week. 
Is this a good time for a quick chat?"

If yes:
"Great! What type of project are you thinking about?"
[Listen 30 sec]
"Perfect—I'll send you our form to get the details: [url]/contact"

If no:
"No problem—I'll email the link. Have a great day!"
```

**Email Follow-up**:
```
Subject: Free consultation + estimate

Hi [Name],

Thanks for chatting with me! Here's the form to get started:
→ [con-001-url]/contact

We'll follow up within 24 hours with your free estimate.

[Your name]
Ace Construction
```

### LT-005 (Medical Courier)

**Cold Call (30 sec)**:
```
"Hi [name], this is [you] from Medical Courier Dispatch. 
We just launched in [city] and offering 3 FREE dispatches 
this week for medical facilities. Do you need help with 
delivery logistics?"

If yes:
"Excellent! Here's our booking form: [url]"

If no:
"No problem—I'll send the link anyway. You can try it out anytime."
```

**Email Follow-up**:
```
Subject: FREE dispatch trial (3 free orders)

Hi [Name],

Medical Courier Dispatch is now serving [city]!

GET 3 FREE ORDERS:
→ [lt-005-url]

Perfect for: prescription delivery, lab pickup, medical supplies

No credit card needed.

[Your name]
Medical Courier Dispatch
```

---

## 7-DAY CHECKPOINT

**Day 1-2 Metrics**:
```
CON-001:
├─ URL live? [✓/✗]
├─ Form → Supabase? [✓/✗]
├─ Email working? [✓/✗]
├─ Leads captured (target: 0-5)
└─ Status: ON TRACK / BLOCKED

LT-005:
├─ URL live? [✓/✗]
├─ Booking form → Supabase? [✓/✗]
├─ Stripe payment working? [✓/✗]
├─ Test orders (target: 0-3)
└─ Status: ON TRACK / BLOCKED
```

**Day 7 Success Metrics**:
```
CON-001:
├─ Leads captured (target: 5+)
├─ Consultations scheduled (target: 1+)
├─ Invoices sent (target: 1+)
├─ Payments received (target: $500+) [✓]
└─ Status: SUCCESS / PARTIAL / FAILED

LT-005:
├─ Test orders (target: 3+)
├─ Paid orders (target: 1+)
├─ Payment received (target: $75+) [✓]
└─ Status: SUCCESS / PARTIAL / FAILED

Combined Revenue:
├─ CON-001: $[amount]
├─ LT-005: $[amount]
└─ Total: $[amount] (target: $575+)
```

---

## WEEK 2 SCALE PLAN (If Day 7 Success)

**If both ventures generated revenue:**
- Apply playbook to OPS-STAFF-001, EC-112, FIN-006
- Increase CON-001 lead gen (paid ads $200/week)
- Increase LT-005 outreach (20-30 facilities)
- Target: $2,000+ combined revenue/week

---

**Status**: READY TO EXECUTE  
**Blocking Issue**: None (code is ready, just needs deployment + sales)  
**Confidence**: HIGH (deployment is 1-2 hours, customer acquisition is proven model)  
**Owner**: User (all tasks)  
**Next Step**: Deploy CON-001 (30 min, right now)

**Created**: 2026-07-30  
**Review**: 2026-07-31 (24 hours)
