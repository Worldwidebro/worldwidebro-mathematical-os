---
date: 2026-07-29
status: Ready to configure
---

# Jotform Webhook Setup (Replaces Zapier)

## What This Does

Jotform form submissions → POST to Vercel → Serverless function:
1. Saves to Supabase assessments table
2. Records email in venture_leads table  
3. Sends personalized email via Resend
4. Sends admin notification

**Advantage:** No Zapier dependency, runs on Vercel, full control.

---

## Monday 8:00 AM Setup (3 min)

### Step 1: Deploy webhook code (1 min)

Webhook code is already committed. Just push and Vercel auto-deploys.

```bash
cd /Users/acebless/Documents/con-001-ace-construction
git push origin main
# Watch deployment: https://vercel.com → con-001-ace-construction
```

**Expected:** Green checkmark on Vercel

---

### Step 2: Configure Jotform webhook (2 min)

**In Jotform dashboard:**

1. Go to https://form.jotform.com/262034682245051
2. Click **Form Settings** (left menu)
3. Scroll to **Webhooks**
4. Click **Add Webhook**
5. **URL:** `https://con-001-ace-construction.vercel.app/api/webhooks/jotform`
6. **Trigger:** Form Submission
7. **Method:** POST
8. Click **Save**

**Expected:** Webhook shows "Active"

---

## Form Field Mapping

Webhook expects these Jotform fields:

| Jotform Field | Field Key | Example |
|---------------|-----------|---------|
| Full Name | q3_fullName | "John Smith" |
| Email | q4_email | "john@example.com" |
| Industry | q5_industry | "Construction" |
| Hours on Decisions | q6_hoursOnDecisions | "20" |

**If field keys differ:** Update `/api/webhooks/jotform/route.ts` lines 11-14.

---

## Test (2 min)

**Submit test form:**
```
1. https://form.jotform.com/262034682245051
2. Fill: Name=Test, Email=test@example.com, Industry=Construction, Hours=20
3. Submit
⏱ Wait 5 sec
✓ Email arrives with "Test, here's your readiness score: 50%"
✓ Row in Supabase assessments table
```

**Verify Supabase:**
```sql
SELECT * FROM assessments ORDER BY created_at DESC LIMIT 1;
SELECT * FROM venture_leads WHERE venture_id = 'CON-001' LIMIT 1;
```

---

## Fallback

| Issue | Fix |
|-------|-----|
| No email | Check RESEND_API_KEY in Vercel env |
| Webhook 500 error | Check Vercel build logs |
| Form not recorded | Check Supabase network tab in browser |

---

**Result: Form→Email automated. No Zapier needed.**
