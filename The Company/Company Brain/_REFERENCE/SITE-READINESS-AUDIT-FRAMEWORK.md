# Site Readiness Audit Framework

**Comprehensive audit for all 6 Tier-0 ventures (Week 1 revenue validation)**

---

## Overview

Before executing Week 1 revenue, we need to verify:
1. **Deployed sites work** (load without errors)
2. **Critical paths function** (signup → checkout → confirmation)
3. **Data flows correctly** (form submissions → database)
4. **Payment processing works** (Stripe integration)
5. **Mobile is responsive** (users might apply on phone)

---

## Tier-0 Ventures Under Audit

| Venture | URL | Owner | Revenue Model |
|---------|-----|-------|----------------|
| **OPS-001** | https://ops-staff-001-staffing.vercel.app/ | Staffing | $2.5K/placement |
| **LT-005** | https://healthroute-courier.vercel.app/ | Medical courier | $85-150/delivery |
| **CALLCENTER** | https://callcenter-eosin.vercel.app/ | Call center | $50-200/call |
| **CON-001** | https://con-001-ace-construction.vercel.app/ | Construction | $5K-50K/project |
| **RE-001** | https://re-001-worldwidebro-holdings.vercel.app/ | Real estate | $50K-500K/deal |
| **LT-011** | https://lt-011-dispatch-software.vercel.app/ | Dispatch software | $1K-5K/month |

---

## Audit Categories

### **Category 1: Page Load & Performance**

**What to check:**
- [ ] Site loads without 5xx errors
- [ ] Page load time < 3 seconds
- [ ] No broken images/CSS
- [ ] Console has no critical errors
- [ ] Mobile viewport renders correctly

**Tools:**
- Automated: Python requests + Selenium
- Manual: Browser DevTools (Network tab, Console)

### **Category 2: Core User Journey**

**What to check:**
- [ ] Homepage CTA visible + clickable
- [ ] Signup/trial form accessible
- [ ] Form fields populate correctly
- [ ] Form validation works (empty field tests)
- [ ] Form submission succeeds
- [ ] Confirmation email received
- [ ] Data in database (Supabase check)

**Tools:**
- Automated: Playwright (full journey simulation)
- Manual: Checklist + email verification

### **Category 3: Payment Integration**

**What to check:**
- [ ] Stripe checkout loads
- [ ] Test card accepted (Stripe test mode)
- [ ] Payment succeeds
- [ ] Receipt email sent
- [ ] Order recorded in DB
- [ ] No double-charges

**Tools:**
- Automated: Stripe test mode + API validation
- Manual: Stripe dashboard verification

### **Category 4: Mobile Responsiveness**

**What to check:**
- [ ] Responsive design active (< 768px)
- [ ] Touch targets >= 44px
- [ ] Forms fillable on mobile
- [ ] CTA buttons accessible
- [ ] No horizontal scroll

**Tools:**
- Automated: Playwright mobile emulation
- Manual: iPhone/Android physical testing

### **Category 5: Database Integrity**

**What to check:**
- [ ] Form submissions appear in Supabase
- [ ] Email field validated (not NULL)
- [ ] Company field validated
- [ ] Timestamps correct
- [ ] No duplicate entries
- [ ] RLS policies working (privacy)

**Tools:**
- Automated: Supabase API queries
- Manual: Supabase dashboard browse

### **Category 6: Email Integration**

**What to check:**
- [ ] Confirmation email sent within 30 seconds
- [ ] Email contains correct data (name, company)
- [ ] Email has clear CTA
- [ ] Reply-to address correct
- [ ] No typos/formatting issues

**Tools:**
- Automated: Email webhook monitoring
- Manual: Check inbox + spam folder

---

## Automated Audit Script (Python)

**File:** `_REFERENCE/site_audit.py`

**Checks:**
1. HTTP status codes (200 for success pages)
2. Page load time
3. HTML validity
4. Broken links
5. Form field presence
6. Database connectivity
7. Email delivery

**Usage:**
```bash
python3 site_audit.py --venture LT-005 --full
```

---

## Browser Automation Audit (Playwright)

**File:** `_REFERENCE/site_audit_playwright.py`

**Simulates:**
1. User visits homepage
2. Clicks CTA button
3. Fills out form (name, email, company)
4. Submits form
5. Verifies confirmation page
6. Checks Supabase for data
7. Verifies email received
8. Mobile viewport test

**Usage:**
```bash
python3 site_audit_playwright.py --venture LT-005 --headless
```

---

## Manual Checklist

**File:** `_REFERENCE/SITE-AUDIT-CHECKLIST.md`

**Quick reference:**
- [ ] Open site in Chrome
- [ ] Check homepage loads (no errors)
- [ ] Check CTA visible
- [ ] Fill form with test data
- [ ] Submit form
- [ ] Verify confirmation page
- [ ] Check email inbox
- [ ] Verify data in Supabase
- [ ] Try mobile view
- [ ] Check payment (if applicable)

---

## Success Criteria

| Venture | Must-Have | Nice-to-Have | Status |
|---------|-----------|--------------|--------|
| **OPS-001** | Homepage + Form | Payment | 🔴 TBD |
| **LT-005** | Homepage + Form + Email | Payment | 🔴 TBD |
| **CALLCENTER** | Homepage + Form | Twilio integration | 🔴 TBD |
| **CON-001** | Homepage + Form | Quote generator | 🔴 TBD |
| **RE-001** | Homepage + Form | Deal engine | 🔴 TBD |
| **LT-011** | Homepage + Form | API docs | 🔴 TBD |

---

## Timeline

**Sep 10 (Today):**
- [ ] Run automated audits (all 6 ventures)
- [ ] Run Playwright tests
- [ ] Create audit report

**Sep 11 (Tomorrow):**
- [ ] Fix any blockers found
- [ ] Re-run tests
- [ ] Manual spot-checks

**Sep 12-15 (Week 1):**
- [ ] Monitor during revenue execution
- [ ] Track form submissions + conversions
- [ ] Alert on any failures

---

## Risk Mitigation

**If site fails:**
1. Fallback to manual forms (Google Forms → Supabase)
2. Manual payment collection (Venmo, ACH)
3. Email-based onboarding (no automated flow)
4. Still achievable: $1K-$3K revenue via phone + email

**If payment fails:**
1. Use Stripe test mode for verification
2. Switch to manual invoicing
3. Collect payment later (focus on trial first)

**If email fails:**
1. Send confirmation via SMS
2. Manual email from founder
3. Verify in Supabase instead of email

---

## Audit Results Template

```
VENTURE: LT-005
DATE: Sep 10, 2026
AUDITOR: [name]

PAGE LOAD
  Status: ✅ PASS (loaded in 1.2s)
  Errors: None

FORM SUBMISSION
  Status: ✅ PASS (submitted successfully)
  Data in DB: ✅ Yes
  
EMAIL DELIVERY
  Status: ✅ PASS (received in 15 seconds)

PAYMENT
  Status: 🟡 NOT TESTED (test mode)

MOBILE
  Status: ✅ PASS (responsive)

OVERALL: 🟢 READY FOR WEEK 1
```

---

## Next Steps

1. Create `site_audit.py` (automated)
2. Create `site_audit_playwright.py` (browser automation)
3. Create `SITE-AUDIT-CHECKLIST.md` (manual)
4. Run all audits against 6 ventures
5. Fix any blockers
6. Sign off: Ready for revenue execution

