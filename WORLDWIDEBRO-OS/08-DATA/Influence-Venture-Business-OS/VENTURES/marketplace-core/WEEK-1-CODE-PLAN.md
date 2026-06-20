# Week 1 Code Plan: Marketplace Core Platform
**Repo:** `Worldwidebro/marketplace-core`  
**May 12-16, 2026 | Target: Staging Deployment Friday EOD**

---

## OVERVIEW

**Build ONE shared marketplace platform** (customer app, contractor app, admin dashboard) that both roofing (CON-009) and plumbing (CON-010) customize.

**Success Criteria:**
- ✅ Staging deployment Friday EOD
- ✅ All core features working (jobs, contractors, quotes, payments, chat, GPS, SMS)
- ✅ Customizations ready (roofing inspections + quotes, plumbing emergency dispatch)
- ✅ Zero blockers for Week 2 marketing launch

---

## MONDAY, MAY 12 — ARCHITECTURE & FOUNDATION

### Morning (9am-12:30pm)

**9:00am - 9:15am: Team Standup**
- [ ] Goals: Core marketplace done by EOW
- [ ] Blockers: None yet
- [ ] Dependencies: All dev machines ready, Supabase access confirmed

**9:15am - 10:15am: Database Schema (1 hour)**
- [ ] PostgreSQL schema finalization
- [ ] Tables: jobs, contractors, customers, quotes, payments, photos, chat, ratings
- [ ] Foreign keys + indexes
- [ ] Deploy to Supabase staging

**10:15am - 11:15am: Repo Setup (1 hour)**
- [ ] Create 3 repos locally (if not exist)
- [ ] Stack: Node.js + Express, React Native (Expo), PostgreSQL
- [ ] .env.example, .gitignore, README.md
- [ ] GitHub Actions CI/CD workflow

**11:15am - 1:15pm: Backend API Skeleton (2 hours)**
- [ ] Express server setup (port 3001)
- [ ] Routes: /api/jobs, /api/contractors, /api/quotes, /api/auth, /api/payments, /api/chat
- [ ] Database connection pool
- [ ] Error handling + logging middleware

### Afternoon (1:15pm-5:30pm)

**1:15pm - 2:15pm: Lunch**

**2:15pm - 4:15pm: Customer + Contractor Apps (2 hours)**
- [ ] React Native screens for customer app (LoginScreen, CreateJobScreen, ContractorListScreen, ChatScreen, RatingScreen)
- [ ] React Native screens for contractor app (JobAlertScreen, JobDetailScreen, EarningsScreen)
- [ ] Navigation setup (React Navigation)
- [ ] Basic styling

**4:15pm - 5:15pm: Admin Dashboard (1 hour)**
- [ ] React setup
- [ ] Dashboard overview, real-time map, job list
- [ ] Navigation structure

**5:15pm - 5:30pm: EOD Standup**
```
What's done:
✅ Database schema
✅ Repos setup
✅ Backend API skeleton
✅ Customer + contractor app skeletons
✅ Admin dashboard start

What's next:
→ GPS + SMS integration
→ Payment integration
→ Matching algorithm

Blockers:
None yet
```

---

## TUESDAY, MAY 13 — INTEGRATIONS

### Morning (9am-1:15pm)

**9:00am - 9:15am: Standup**

**9:15am - 11:15am: GPS + Google Maps (2 hours)**
- [ ] Google Maps API setup
- [ ] Background location tracking (iOS + Android)
- [ ] Permission handling
- [ ] Update contractor location every 10 sec
- [ ] Display on customer map (real-time)

**11:15am - 1:15pm: SMS + Twilio (2 hours)**
- [ ] Twilio account + phone number
- [ ] Send SMS on events (job assigned, accepted, ETA, completed)
- [ ] Webhook for SMS replies
- [ ] Test flow end-to-end

### Afternoon (1:15pm-5:30pm)

**1:15pm - 2:15pm: Lunch**

**2:15pm - 3:45pm: Photo Upload (1.5 hours)**
- [ ] AWS S3 or Cloudinary setup
- [ ] Photo upload endpoint + compression
- [ ] Display in app

**3:45pm - 4:45pm: Authentication (1 hour)**
- [ ] Clerk or Firebase phone OTP
- [ ] JWT token generation + storage
- [ ] Protected API routes

**4:45pm - 5:15pm: Admin Dashboard Continued (30 min)**
- [ ] Real-time map
- [ ] Job overview
- [ ] Revenue dashboard

**5:15pm - 5:30pm: EOD Standup**
```
What's done:
✅ GPS integration
✅ SMS integration (Twilio)
✅ Photo upload + compression
✅ Auth flow (phone OTP)
✅ Admin dashboard skeleton

What's next:
→ Payment integration (Stripe)
→ Matching algorithm
→ Chat system

Blockers:
None yet
```

---

## WEDNESDAY, MAY 14 — CORE SYSTEMS

### Morning (9am-1:15pm)

**9:00am - 9:15am: Standup**

**9:15am - 12:15pm: Stripe Payment Integration (3 hours)**
- [ ] Stripe account setup
- [ ] Payment Intent flow
- [ ] Save payment method
- [ ] Webhook: payment_intent.succeeded
- [ ] Contractor payout setup (Stripe Connect)
- [ ] Test with Stripe test cards

**12:15pm - 2:15pm: Admin Dashboard Core (2 hours)**
- [ ] Jobs overview (pending, in-progress, completed)
- [ ] Real-time map (all jobs, all contractors, live locations)
- [ ] Revenue dashboard (daily, weekly, by contractor)

### Afternoon (1:15pm-5:30pm)

**1:15pm - 2:15pm: Lunch**

**2:15pm - 3:45pm: Matching Algorithm (1.5 hours)**
- [ ] Find contractors within 5-mile radius
- [ ] Filter by trade (roofing vs plumbing)
- [ ] Sort by ratings
- [ ] Send to top 3, first accept wins

**3:45pm - 4:45pm: Payment Method Storage (1 hour)**
- [ ] Save card (PCI-compliant)
- [ ] Choose payment method for future jobs
- [ ] Delete payment method

**4:45pm - 5:15pm: Chat Prep (30 min)**
- [ ] Firebase Realtime DB setup
- [ ] Schema: messages(job_id, sender_id, message, timestamp)

**5:15pm - 5:30pm: EOD Standup**
```
What's done:
✅ Stripe integration
✅ Admin dashboard (jobs, revenue, contractors)
✅ Matching algorithm
✅ Payment method storage
✅ Chat prep

What's next:
→ Push notifications
→ Chat real-time
→ Trade customizations

Blockers:
None yet
```

---

## THURSDAY, MAY 15 — NOTIFICATIONS & CUSTOMIZATIONS START

### Morning (9am-1:15pm)

**9:00am - 9:15am: Standup**

**9:15am - 11:15am: Push Notifications (2 hours)**
- [ ] Firebase Cloud Messaging
- [ ] iOS + Android certificates
- [ ] Job alert notifications
- [ ] Test on real devices

**11:15am - 12:45pm: Chat System (1.5 hours)**
- [ ] Real-time messaging (Firebase)
- [ ] Customer ask questions before accepting
- [ ] Contractor clarify details
- [ ] Unread count

### Afternoon (1:15pm-5:30pm)

**1:15pm - 2:15pm: Lunch**

**2:15pm - 4:15pm: ROOFING CUSTOMIZATIONS (Parallel)**
- [ ] Inspection photos (before/after)
- [ ] Materials library (shingles, flashing, gutters)
- [ ] Quote creation flow
- [ ] Quote comparison view
- [ ] Weather integration
- [ ] Scheduling calendar

**2:15pm - 4:15pm: PLUMBING CUSTOMIZATIONS (Parallel)**
- [ ] Emergency intake (phone + SMS)
- [ ] Auto-dispatch (nearest plumber)
- [ ] ETA calculation
- [ ] Upfront pricing
- [ ] Real-time tracking
- [ ] License verification

**4:15pm - 5:15pm: Integration Testing (1 hour)**
- [ ] SMS → job assignment end-to-end
- [ ] GPS tracking
- [ ] Payments (test cards)
- [ ] Photos
- [ ] Chat real-time

**5:15pm - 5:30pm: EOD Standup**
```
What's done:
✅ Push notifications
✅ Chat real-time
✅ Roofing customizations started
✅ Plumbing customizations started
✅ Integration testing started

What's next:
→ Finish customizations
→ Complete testing
→ Deploy to staging

Blockers:
None yet
```

---

## FRIDAY, MAY 16 — FINISH & DEPLOY

### Morning (9am-1:15pm)

**9:00am - 9:15am: Standup**

**9:15am - 11:15am: Finish Roofing Customizations (2 hours)**
- [ ] Scheduling calendar (date/time picker)
- [ ] Warranty tracking
- [ ] Material inventory
- [ ] Invoice generation

**11:15am - 1:15pm: Finish Plumbing Customizations (2 hours)**
- [ ] License verification
- [ ] Shift management
- [ ] After-hours support
- [ ] Callback system

### Afternoon (1:15pm-5:30pm)

**1:15pm - 2:15pm: Lunch**

**2:15pm - 3:15pm: Integration Testing (1 hour)**
- [ ] SMS → job assignment end-to-end
- [ ] GPS + payments + photos + chat
- [ ] Push notifications
- [ ] All trade-specific features

**3:15pm - 4:15pm: Bug Fixes (1 hour)**
- [ ] Fix issues from testing
- [ ] Performance optimization
- [ ] Error handling

**4:15pm - 4:45pm: Staging Deployment (30 min)**
- [ ] Deploy backend to AWS staging
- [ ] Deploy web to Vercel staging
- [ ] Deploy apps to TestFlight + Firebase App Distribution
- [ ] Verify all systems working

**4:45pm - 5:15pm: Final Testing (30 min)**
- [ ] Test critical flows
- [ ] Document login credentials
- [ ] Create deployment docs

**5:15pm - 5:30pm: EOD Standup**
```
What's done:
✅ MARKETPLACE CORE COMPLETE
✅ All customizations done
✅ Testing complete
✅ STAGING DEPLOYED ✅

What's next:
→ Beta testing Mon-Tue (real contractors)
→ Bug fixes from beta
→ Week 2 marketing launch

Blockers:
NONE - READY FOR WEEK 2
```

---

## DAILY PROGRESS TRACKING

Create `marketplace-core/PROGRESS-TRACKING.md` and update daily:

```markdown
# Daily Progress: Week 1 Code Sprint

## Monday
- Code: 25% → API skeleton, app skeletons
- Blockers: None
- Next: GPS, SMS

## Tuesday
- Code: 50% → Integrations complete
- Blockers: None
- Next: Payments, matching, chat

## Wednesday
- Code: 75% → Core systems complete
- Blockers: None
- Next: Customizations, testing

## Thursday
- Code: 85% → Customizations 80%, testing 60%
- Blockers: None
- Next: Finish customizations, final testing, deploy

## Friday
- Code: 100% → STAGING DEPLOYED ✅
- Blockers: NONE
- Status: READY FOR WEEK 2 LAUNCH
```

---

## SUCCESS DEFINITION

✅ **By 5:30pm Friday, May 16:**
- Backend complete + deployed to staging
- All 3 apps (customer, contractor, admin) deployed to staging
- GPS, SMS, Photos, Payments, Chat all working
- Roofing + Plumbing customizations complete
- Integration testing passed
- **ZERO blockers for Week 2 marketing launch**

**If any blocker appears:** Escalate immediately → don't let it carry to Friday. Fix it same day.

