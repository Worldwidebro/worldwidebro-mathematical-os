# AUTONOMOUS LOOPS (Instead of n8n)

**3 production-ready loops for lead automation. Run immediately.**

---

## THE 3 LOOPS

### Loop 1: Fetch Leads (Every 4 hours)
```bash
/loop python3 loops/01-FETCH-LEADS.py --every 4h
```
- Fetches from HomeAdvisor, Angi, SAM.gov APIs
- Deduplicates by email
- Stores in Supabase `leads` table
- Reports: Leads added per source

---

### Loop 2: Send Emails (Every 1 hour)
```bash
/loop python3 loops/02-SEND-EMAILS.py --every 1h
```
- Queries leads where `status='new'`
- Sends Email 1: Confirmation
- Updates status to `email_1_sent`
- Reports: Emails sent

---

### Loop 3: Score Leads (Every 24 hours)
```bash
/loop python3 loops/03-SCORE-LEADS.py --every 24h
```
- Analyzes leads by source
- Calculates cost per lead
- Identifies cheapest source
- Recommends budget allocation

---

### Loop 4: USASpending Contracts (Every 24 hours) — LIVE
```bash
/loop python3 loops/04-USASPENDING-CONTRACTS.py --every 24h
```
- Pulls awarded NC federal construction contracts (USASpending API, **no key needed**)
- Filters construction NAICS (238160/238210/238220/236220/236118/238290), NC, last 90d
- Stores in Supabase `gov_awards`, deduped by award_id
- These primes = subcontracting targets → see `../GOV-CONTRACT-REVENUE-ACTION-SHEET.md`

---

### Loop 5: SAM.gov Opportunities (Every 24 hours) — needs API key
```bash
/loop python3 loops/05-SAM-OPPORTUNITIES.py --every 24h
```
- Pulls OPEN federal RFPs you can bid on (SAM.gov Opportunities API)
- **Requires** `SAM_GOV_API_KEY` in `.env` (free: sam.gov → Account Details → API Key)
- Stores in Supabase `gov_opportunities`, deduped by notice_id

---

## QUICK START (TODAY)

### Step 1: Supabase Table (5 min)
```sql
CREATE TABLE leads (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  source TEXT,
  email TEXT NOT NULL,
  phone TEXT,
  zip TEXT,
  status TEXT DEFAULT 'new',
  created_at TIMESTAMP DEFAULT NOW(),
  UNIQUE(email)
);

CREATE INDEX idx_source ON leads(source);
CREATE INDEX idx_status ON leads(status);
```

### Step 2: .env Setup (2 min)
```bash
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-anon-key
RESEND_API_KEY=re_xxx (optional)
```

### Step 3: Run Loops (5 min)
```bash
# Test once
python3 loops/01-FETCH-LEADS.py
python3 loops/02-SEND-EMAILS.py
python3 loops/03-SCORE-LEADS.py

# Schedule (production)
/loop python3 loops/01-FETCH-LEADS.py --every 4h
/loop python3 loops/02-SEND-EMAILS.py --every 1h
/loop python3 loops/03-SCORE-LEADS.py --every 24h
```

---

## PRODUCTION: Replace Mock APIs

### Loop 1 Line ~50 (fetch_leads_from_sources)
- Replace mock data with real API calls
- HomeAdvisor, Angi, SAM.gov each need API key

### Loop 2 Line ~35 (send_email)
- Replace mock print with Resend/SendGrid/AWS SES
- Add `RESEND_API_KEY=re_xxx` to .env

### Loop 3
- No changes needed (reads from Supabase)

---

## MONITORING

```bash
/loop status              # See all running loops
/loop logs [script.py]    # View output
python3 loops/01-*.py    # Manual test run
```

---

## WEEK 1 TIMELINE

**Mon:** Create table + run loops manually (1 hr)
**Tue:** Schedule all 3 loops (1 hr)
**Wed-Fri:** Leads flowing automatically + videos + repo work

**Result:** 50-100 leads by Friday, fully automated

---

## COMPARISON

**Loops:** 15 min setup, $0/mo, full control, easy to scale
**n8n:** 1 hr setup, $50+/mo, UI black box, harder to debug

**Choose:** Loops for solo bootstrap

---

**Ready to execute. Start now.**

