# LT-005 Week 1 Agentic Execution Plan

**Scope:** Deploy HealthRoute Caller Portal by Sunday 10pm (Option B)  
**Timeline:** TODAY (Sep 14) 5pm → Sunday (Sep 15) 11pm  
**Total Capacity:** 9 hours focused work  
**Model Routing:** Haiku (boilerplate) → Sonnet (implementation)  

---

## PHASE 0: EVAL-FIRST BASELINE

### 6 Capability Evals

**E1: Supabase Schema Deployment**
- Success: 7 tables created, 10 script families seeded
- Regression: `SELECT COUNT(*) FROM scripts` → 10

**E2: Caller Dashboard**
- Success: `/caller/dashboard` → 200, KPI grid visible
- Regression: Lighthouse >85, <2s load time

**E3: Prospect Detail**
- Success: Click prospect → detail page loads with script
- Regression: No layout shift, buttons clickable

**E4: Call Logger Form**
- Success: Submit form → logs to DB → confirmation shows
- Regression: Required fields enforced, errors announced

**E5: Vercel Deploy**
- Success: `https://healthroute-courier.vercel.app` → 200
- Regression: Env vars loaded, no build errors

**E6: Authentication E2E**
- Success: Login → dashboard loads → RLS enforced
- Regression: Caller sees only own prospects, session persists on refresh

---

## EXECUTION PHASES (9 hours)

### PHASE 1: Supabase Schema (1h, TODAY 5-6pm)
**Agent:** Haiku | Deploy schema + seed script families | **Done:** E1 passes

### PHASE 2: Caller Dashboard (2h, TODAY 6-8pm)
**Agent:** Sonnet | Build dashboard with KPI grid + prospect list | **Done:** E2 passes

### PHASE 3: Prospect Detail (1h, TODAY 8-9pm)
**Agent:** Sonnet | Build detail page with script + call history | **Done:** E3 passes

### PHASE 4: Call Logger Form (1.5h, TODAY 9pm-10:30pm)
**Agent:** Sonnet | Build form with validation + API integration | **Done:** E4 partial

### PHASE 5: API Endpoints (1h, SUNDAY 10-11am)
**Agent:** Haiku | Create POST `/api/calls/log` endpoint | **Done:** E4 verified

### PHASE 6: Vercel Deploy (0.5h, SUNDAY 10:30-11pm)
**Agent:** Haiku | Deploy to Vercel + env vars | **Done:** E5 passes

### PHASE 7: E2E Auth Test (1h, SUNDAY 11pm-12am)
**Agent:** Sonnet | Test login → dashboard → logout | **Done:** E6 passes

---

## SUCCESS METRICS

✅ All 6 evals passing  
✅ Lighthouse >85 (Performance, Accessibility)  
✅ <2s load time on 3G  
✅ Keyboard navigation works  
✅ RLS enforced  

---

**Status:** READY TO EXECUTE  
**Decision:** Confirm start time (today 5pm or Sunday morning)

