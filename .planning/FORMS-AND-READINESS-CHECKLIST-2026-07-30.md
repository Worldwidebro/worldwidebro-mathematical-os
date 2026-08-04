# FORMS + DEPLOYMENT CHECKLIST — 8 Ventures

**Question**: Don't we need forms for customer acquisition?  
**Answer**: YES. Forms = lead capture → payment → revenue. Critical blocker for all ventures.

---

## MASTER READINESS CHECKLIST (What's Needed to Run NOW)

| Venture | Code | Forms | DB | Payment | Blocker | Days to Live | Priority |
|---------|------|-------|----|---------|---------|----|----------|
| **CON-001** | ✓ | ✓ | ✓ | ⚠️ | Vercel env vars | 1-2 | P0 |
| **LT-005** | ✓ | ⚠️ | ⚠️ | ⚠️ | Railway setup | 5-7 | P0 |
| **STA-001** | ✗ | ✗ | ✗ | ✗ | No backend API | 14 | P1 |
| **OPS-001** | ✗ | ✗ | ✗ | ✗ | No backend API | 14 | P1 |
| **EC-001** | ✗ | ✗ | ✗ | ✗ | No product spec | 30+ | P3 |
| **EC-112** | ⚠️ | ✗ | ✗ | ✗ | No Medusa backend | 21 | P2 |
| **RE-001** | ✗ | ✗ | ✗ | ✗ | Unclear scope | 45+ | P3 |
| **LT-011** | ✗ | ✗ | ✗ | ✗ | No repo | 30+ | P3 |

---

## [AUDIT] — Forms by Venture

### CON-001 (Ace Construction)

**Forms Inventory**:
- ✓ Contact/Inquiry Form
- ✓ Project Scope Form
- ✓ Estimate Request Form
- ? Quote Template (verify exists)
- ? Invoice/Payment Form (Stripe link)

**For Customer Acquisition Flow**:
```
Customer finds CON-001 → Fills contact form
      ↓
Email notification sent to you
      ↓
You call customer (30 sec pitch)
      ↓
Customer fills project scope form
      ↓
You send estimate/quote (PDF + Stripe payment link)
      ↓
Customer pays via Stripe
      ↓
Revenue ✓
```

**Blocker**: Stripe payment link not automated (manual step OK for MVP)  
**To Deploy**: Push Vercel env vars → test form → go live

---

### LT-005 (Medical Courier Dispatch)

**Forms Inventory**:
- ✓ Booking Form (customer + driver)
- ✓ Dispatch Request Form
- ? Payment Form (Stripe integration incomplete)
- ? Proof of Delivery Form (signature/photo)
- ? Receipt/Invoice Form (email)

**For Customer Acquisition Flow**:
```
Facility finds LT-005 → Clicks "Book Dispatch"
      ↓
Customer fills dispatch request (pickup, delivery, timeline)
      ↓
Stripe payment form appears
      ↓
Customer enters card (test: 4242 4242 4242 4242)
      ↓
Payment processed → Driver notified
      ↓
Driver accepts order → Proof of delivery captured
      ↓
Receipt emailed to customer
      ↓
Revenue ✓
```

**Blocker**: Stripe integration not complete  
**To Deploy**: Wire Stripe to booking form → test payment → go live

---

### STA-001 (Staffing)

**Forms Inventory**:
- ✗ Job Posting Form (missing)
- ✗ Job Application Form (missing)
- ✗ Profile/Resume Upload (missing)
- ✗ Interview Scheduling (missing)
- ✗ Offer Letter (missing)
- ✗ Payment/Invoice (missing)

**For Customer Acquisition Flow**:
```
Employer finds STA-001 → Wants to post job
      ↓
Clicks "Post Job" → Form appears
      ↓
Employer fills: title, description, salary, location
      ↓
Job posted live
      ↓
Candidates search jobs → Find STA-001 posting
      ↓
Candidate clicks "Apply" → Application form appears
      ↓
Candidate fills: resume, experience, availability
      ↓
You review → Schedule interview
      ↓
Interview completed → Send offer
      ↓
Candidate accepts → Employer pays placement fee
      ↓
Revenue ✓
```

**Blocker**: No backend API to store jobs/applications  
**To Deploy**: Build API + create forms → test end-to-end → go live

---

### OPS-001 (HR/Operations)

**Forms Inventory**:
- ✗ Employee Onboarding Form (missing)
- ✗ Time Tracking Form (missing)
- ✗ Payroll Setup Form (missing)
- ✗ Time-Off Request Form (missing)
- ✗ Payslip/Statement (missing)
- ✗ Payment Processing (missing)

**For Customer Acquisition Flow**:
```
Company needs HR system → Finds OPS-001
      ↓
Signs up → Fills company profile
      ↓
Adds first employee → Employee onboarding form sent
      ↓
Employee fills: personal info, tax info, direct deposit
      ↓
Employee starts work → Time tracking begins
      ↓
Week 1 complete → Time entry submitted
      ↓
You process payroll → Calculate hours, taxes, deductions
      ↓
Payslip generated → Sent to employee
      ↓
Payment processed via Stripe
      ↓
Revenue ✓ (subscription or per-employee-per-month)
```

**Blocker**: No backend API for employee management  
**To Deploy**: Build API + create forms → test payroll flow → go live

---

### EC-001 (Angels In Daylight)

**Forms Inventory**:
- ? Product Catalog (what is this selling?)
- ✗ Shopping Cart Form (missing)
- ✗ Checkout Form (missing)
- ✗ Customer Account Form (missing)
- ✗ Order Tracking (missing)

**For Customer Acquisition Flow**:
```
Customer finds EC-001 → Browsing products
      ↓
Customer adds item to cart
      ↓
Clicks checkout → Payment form appears
      ↓
Customer enters card details
      ↓
Payment processed
      ↓
Order confirmation emailed
      ↓
Customer tracks shipment
      ↓
Receives package
      ↓
Revenue ✓
```

**Blocker**: Unclear what product is being sold  
**Required First**: Define EC-001 business model before building forms

---

### EC-112 (Cosmic Kitty)

**Forms Inventory**:
- ✓ Storefront (HTML preview only)
- ✗ Product Catalog (Medusa backend missing)
- ✗ Shopping Cart Form (not connected)
- ✗ Checkout Form (not connected)
- ✗ Customer Account (missing)

**For Customer Acquisition Flow**:
```
Customer finds EC-112 → Browses products
      ↓
Adds item to cart (needs Medusa backend)
      ↓
Proceeds to checkout → Stripe payment form
      ↓
Enters card details
      ↓
Payment processed
      ↓
Order confirmation emailed
      ↓
Fulfillment begins
      ↓
Revenue ✓
```

**Blocker**: Medusa backend not deployed (no product database)  
**To Deploy**: Deploy Medusa + create product catalog → wire Stripe → go live

---

### RE-001 (Worldwidebro Holdings)

**Forms Inventory**:
- ✗ Property Search/Listing (missing)
- ✗ Property Inquiry Form (missing)
- ✗ Financing Request Form (missing)
- ✗ Agent Contact Form (missing)
- ✗ Lease/Offer Form (missing)

**For Customer Acquisition Flow**:
```
Real estate customer finds RE-001 → Searches properties
      ↓
Customer filters by location, price, type
      ↓
Views property details → Clicks "Inquire"
      ↓
Property inquiry form appears
      ↓
Customer enters contact info + questions
      ↓
Email sent to agent
      ↓
Agent calls customer
      ↓
Agent schedules showing
      ↓
Customer makes offer OR applies for financing
      ↓
Transaction completed
      ↓
Revenue ✓ (commission or financing fee)
```

**Blocker**: Unclear if this is:
- Customer-facing marketplace (Zillow competitor)?
- Internal holdings platform?
- Financing platform?

**Required First**: Clarify RE-001 product scope before building forms

---

### LT-011 (Dispatch Software)

**Forms Inventory**:
- ✗ Dispatch Job Form (missing)
- ✗ Driver Assignment Form (missing)
- ✗ Route Optimization Form (missing)
- ✗ Proof of Delivery Form (missing)
- ✗ Driver Availability Form (missing)

**For Customer Acquisition Flow**:
```
Dispatcher finds LT-011 → Wants to manage fleet
      ↓
Signs up → Creates account
      ↓
Adds jobs to dispatch
      ↓
System assigns drivers based on location
      ↓
Driver accepts job on mobile app
      ↓
Driver navigates to delivery
      ↓
Customer receives package
      ↓
Driver submits proof (photo + signature)
      ↓
Job marked complete
      ↓
Revenue ✓ (subscription or per-job fee)
```

**Blocker**: Repository doesn't exist yet  
**Required First**: Create repo + clarify if this is separate from LT-005

---

## DEPLOYMENT CHECKLIST

### CON-001 (Ready Today)

```
TODAY (30 min):
☐ Get Supabase keys → con-001-ace-construction project
   └─ SUPABASE_URL
   └─ SUPABASE_ANON_KEY
   └─ SUPABASE_SERVICE_ROLE_KEY

☐ Get Stripe keys → Stripe dashboard
   └─ STRIPE_PUBLISHABLE_KEY
   └─ STRIPE_SECRET_KEY

☐ Vercel Dashboard → Settings → Environment Variables
   └─ Paste all 5 keys
   └─ Redeploy

☐ Testing (15 min)
   └─ Visit production URL
   └─ Submit test form
   └─ Check Supabase: leads table has new row ✓
   └─ Check email: notification received ✓

LIVE STATUS: ✓ Ready for customer acquisition
Timeline: 1-2 days to first customer
```

### LT-005 (Ready Tomorrow)

```
TODAY (1 hour):
☐ Railway.app setup
   └─ Create account (if needed)
   └─ New Project → Connect GitHub
   └─ Select: worldwidebro/lt-005-medical-courier-dispatch
   └─ Confirm deployment

☐ Create Supabase project for LT-005
   └─ Copy connection string

☐ Get Stripe keys (test mode)
   └─ STRIPE_PUBLISHABLE_KEY
   └─ STRIPE_SECRET_KEY

☐ Railway Variables → Settings → Environment Variables
   └─ Paste:
      ├─ SUPABASE_URL
      ├─ SUPABASE_ANON_KEY
      ├─ STRIPE_PUBLISHABLE_KEY
      └─ STRIPE_SECRET_KEY

☐ Testing (30 min)
   └─ Visit production URL (from Railway)
   └─ Submit booking form
   └─ Test payment (card: 4242 4242 4242 4242)
   └─ Check Supabase: orders table has new row ✓
   └─ Check email: driver notification sent ✓

LIVE STATUS: ✓ Ready for customer acquisition
Timeline: 5-7 days to first paid order
```

### STA-001 (Next Week)

```
Decision needed first:
☐ Tech stack: Node.js + Express? OR Python + FastAPI?

Backend build (5-7 days):
☐ Authentication system (Magic Link or JWT)
☐ Job posting API endpoints
☐ Application management endpoints
☐ Database schema (jobs, applications, users)

Forms creation (2-3 days):
☐ Job posting form
☐ Application form
☐ Profile upload form
☐ Interview scheduling form
☐ Offer letter form

Testing + go live (2-3 days):
☐ End-to-end: post job → apply → schedule → offer
☐ Payment flow: collect placement fee
☐ Deploy to Vercel/Railway

Timeline: 14 days total
```

### OPS-001 (Next Week)

```
Same as STA-001 (parallel work):
☐ Backend API (authentication, employee management)
☐ Forms (onboarding, time tracking, payroll)
☐ Testing + deployment

Timeline: 14 days total
```

### EC-112 (2-3 Weeks)

```
☐ Deploy Medusa backend (2-3 days)
☐ Create product catalog (10+ products) (2-3 days)
☐ Wire Stripe integration (1 day)
☐ Test checkout flow (1 day)
☐ Deploy storefront to Vercel (1 day)

Timeline: 14-21 days total
```

### EC-001, RE-001, LT-011 (Defer)

```
Blocker: Product spec unclear
Action: Define business model FIRST, then create forms

Timeline: 30-45+ days
```

---

## FORMS ARCHITECTURE (Shared Library)

**Build ONE library serving all ventures**:

```
/forms
├── core/
│   ├── contact-inquiry.jsx
│   ├── booking.jsx
│   ├── payment-checkout.jsx
│   ├── profile-registration.jsx
│   ├── document-upload.jsx
│   └── email-notifications.jsx
│
├── industry/
│   ├── construction/
│   │   ├── project-scope.jsx
│   │   ├── estimate-request.jsx
│   │   └── invoice-template.jsx
│   ├── logistics/
│   │   ├── dispatch-request.jsx
│   │   ├── proof-of-delivery.jsx
│   │   └── tracking-link.jsx
│   ├── staffing/
│   │   ├── job-posting.jsx
│   │   ├── application.jsx
│   │   ├── interview-schedule.jsx
│   │   └── offer-letter.jsx
│   ├── operations/
│   │   ├── employee-onboarding.jsx
│   │   ├── time-tracking.jsx
│   │   ├── payroll-setup.jsx
│   │   └── payslip-generator.jsx
│   ├── ecommerce/
│   │   ├── product-catalog.jsx
│   │   ├── shopping-cart.jsx
│   │   └── checkout.jsx
│   └── realestate/
│       ├── property-listing.jsx
│       ├── financing-inquiry.jsx
│       └── lease-application.jsx
│
└── templates/
    ├── email/
    │   ├── lead-capture.html
    │   ├── order-confirmation.html
    │   ├── payment-receipt.html
    │   └── notification.html
    ├── pdf/
    │   ├── invoice.html
    │   ├── quote.html
    │   ├── offer-letter.html
    │   └── payslip.html
    └── success/
        ├── thank-you.jsx
        ├── order-tracking.jsx
        └── dashboard.jsx
```

**Benefits**:
- CON-001 reuses: `core/contact-inquiry` + `core/payment-checkout` + `industry/construction/estimate`
- LT-005 reuses: `core/booking` + `core/payment-checkout` + `industry/logistics/proof-of-delivery`
- STA-001 reuses: `core/profile-registration` + `industry/staffing/job-posting` + `industry/staffing/application`
- All ventures share payment flow (single source of truth)

---

## CUSTOMER ACQUISITION READY (This Week)

### CON-001 + LT-005 (P0 — Deploy Today)
- Forms: ✓ Ready
- Database: ✓ Ready
- Payment: ⚠️ Need Stripe keys
- Action: Deploy → Get forms live → Start calling customers

### STA-001 + OPS-001 (P1 — Ready Next Week)
- Forms: Need to build
- Database: Need to create
- Payment: Stripe ready
- Action: Build backend → Create forms → Start enrolling customers

### EC-112 (P2 — Ready in 3 Weeks)
- Forms: Need to wire to Medusa
- Database: Medusa provides
- Payment: Stripe ready
- Action: Deploy Medusa → Wire forms → Create product catalog → Go live

### EC-001, RE-001, LT-011 (P3 — Defer)
- Forms: Blocked on product spec
- Action: Clarify business model → Then build

---

## SUMMARY: What You Need for Each Venture to Be Running NOW

**CON-001**: Vercel env vars (30 min) + customer calls = INCOME  
**LT-005**: Railway setup (1 hour) + Stripe wiring (30 min) + customer calls = INCOME  
**STA-001**: Backend API (7 days) + forms (3 days) + recruitment = INCOME  
**OPS-001**: Backend API (7 days) + forms (3 days) + employee signups = INCOME  
**EC-112**: Medusa deploy (3 days) + product catalog (3 days) + product photos = INCOME  
**EC-001**: Product spec (1 day) + platform build (21 days) = INCOME  
**RE-001**: Scope decision (1 day) + platform build (30 days) = INCOME  
**LT-011**: Repo creation (1 day) + product spec (3 days) + build (30 days) = INCOME  

---

**Priority**: P0 = CON-001 + LT-005 (TODAY)  
**Next**: P1 = STA-001 + OPS-001 (next week, parallel)  
**Then**: P2 = EC-112 (when P1 starts moving)  
**Defer**: P3 = EC-001, RE-001, LT-011 (clarify scope first)

**Created**: 2026-07-30
