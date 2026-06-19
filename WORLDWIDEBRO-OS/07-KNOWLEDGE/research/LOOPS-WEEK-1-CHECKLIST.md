# WEEK 1 EXECUTION CHECKLIST (Loop-based)

## TODAY - Monday, June 16 (3 hours)

### Morning: Setup (1 hour)
- [ ] Create Supabase `leads` table (run SQL from loops/README.md)
- [ ] Verify table created: `psql` or Supabase UI
- [ ] Add SUPABASE_URL + SUPABASE_KEY to .env

### Afternoon: Test Loops (2 hours)
- [ ] Run Loop 1: `python3 loops/01-FETCH-LEADS.py`
  - Expected output: ✅ TOTAL ADDED: 5 (mock data)
- [ ] Run Loop 2: `python3 loops/02-SEND-EMAILS.py`
  - Expected output: ✅ EMAILS SENT: 5
- [ ] Run Loop 3: `python3 loops/03-SCORE-LEADS.py`
  - Expected output: Cost/lead by source + recommendation

**EOD:** All 3 loops working ✓ | Table populated with test data ✓

---

## Tuesday, June 17 (2 hours)

### Morning: Schedule Loops (1 hour)
- [ ] Start Loop 1 (every 4h): `/loop python3 loops/01-FETCH-LEADS.py --every 4h`
- [ ] Start Loop 2 (every 1h): `/loop python3 loops/02-SEND-EMAILS.py --every 1h`
- [ ] Start Loop 3 (every 24h): `/loop python3 loops/03-SCORE-LEADS.py --every 24h`
- [ ] Verify running: `/loop status`

### Afternoon: Contracts B,C,D (1 hour)
- [ ] Option B: Auto-templates (30 min)
- [ ] Option C: Contract-OS mapping (30 min)
- [ ] Option D: Parallel approval (done, skipping)

**EOD:** All loops scheduled ✓ | Automated lead pipeline live ✓ | Contracts B,C,D done ✓

---

## Wednesday-Friday (Video + Repo Work)

**While loops run automatically in background:**

**Wed:** Video production
- [ ] Record Video 1: "Why electrical code matters"
- [ ] Record Video 2: "Signs your home needs electrical work"
- [ ] Upload both to YouTube

**Thu:** Video + trading system
- [ ] Record Video 3: "How much does rewiring cost"
- [ ] Start Trading System Phase 2 setup

**Fri:** Measurement + repo
- [ ] Query Supabase: Leads by source (should have 50-100)
- [ ] Calculate: Cost per lead
- [ ] Expand repo ranking to 100 repos
- [ ] Commit all work

---

## WEEK 1 RESULT

✅ 50-100 leads in Supabase (automated)
✅ 50-100 emails sent (automated)
✅ Cost per lead calculated (automated)
✅ Contracts complete (legal foundation)
✅ 3 videos published (content marketing)
✅ Repo intelligence expanded (strategic clarity)
✅ All loops running 24/7 (zero manual work)

**Cost:** $0 (loops) + $5 video test budget
**Revenue:** $0 (setup week)
**Next:** CON-011 launch Wed-Thu with paid ads

---

## LIVE MONITORING

**During Week 1, check daily:**
```bash
/loop logs loops/01-FETCH-LEADS.py      # Leads added today
/loop logs loops/02-SEND-EMAILS.py      # Emails sent today
/loop logs loops/03-SCORE-LEADS.py      # ROI analysis
```

**Expected patterns:**
- Loop 1: 5-10 new leads per 4-hour run
- Loop 2: Send 1-2 emails per hour
- Loop 3: Daily recommendation (day 3+)

---

**Status:** Ready to execute today

