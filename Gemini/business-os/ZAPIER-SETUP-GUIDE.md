# Zapier Automation Setup Guide

Three Zapier zaps for Ace Construction customer lifecycle automation. Each zap is UI-only — no code required.

## Prerequisites

- Zapier account (free tier sufficient)
- Jotform account (form responses trigger zaps)
- Resend API key (for email delivery)
- Supabase connection string

---

## Zap 1: Jotform → Supabase (Customer Signup)

**Trigger:** New Jotform submission  
**Action:** Insert row into Supabase `deal_payments` table

### Setup Steps

1. **Create new Zap** → Zapier dashboard → "Create"
2. **Set trigger:**
   - App: Jotform
   - Trigger: New submission
   - Select form: "Ace Construction Contact Form"
3. **Set action:**
   - App: Zapier Tables (or Supabase connector if available)
   - Action: Create Record
   - Connect Supabase project
   - Table: `deal_payments`
   - Map fields:
     - `venture_id` ← Form field "Service Type"
     - `customer_email` ← Form field "Email"
     - `customer_name` ← Form field "Name"
     - `status` ← "pending"
     - `created_at` ← Current timestamp

4. **Test & publish**

---

## Zap 2: Day 0 Welcome Email (Immediate)

**Trigger:** New Supabase row in `deal_payments`  
**Action:** Send email via Resend

### Setup Steps

1. **Create new Zap** → "Create"
2. **Set trigger:**
   - App: Supabase
   - Trigger: New row in table
   - Table: `deal_payments`
   - Filter: `status` = "pending"
3. **Set action:**
   - App: Webhooks by Zapier
   - Action: POST
   - URL: `https://api.resend.com/emails`
   - Method: POST
   - Headers:
     ```
     Authorization: Bearer YOUR_RESEND_API_KEY
     Content-Type: application/json
     ```
   - Body (JSON):
     ```json
     {
       "from": "noreply@aceconstruction.com",
       "to": "{{customer_email}}",
       "subject": "Welcome to Ace Construction — Your Account is Ready",
       "html": "<h1>Welcome to Ace Construction!</h1><p>Hi {{customer_name}},</p><p>Your account for <strong>{{venture_id}}</strong> is now active and ready to use.</p>"
     }
     ```
4. **Test & publish**

---

## Zap 3: Day 2 & Day 5 Follow-ups (Delayed)

**Trigger:** Scheduled (every 2 days)  
**Conditions:** Unpaid customers from 2+ days ago  
**Action:** Send email via Resend

### Setup Steps

1. **Create new Zap** → "Create"
2. **Set trigger:**
   - App: Schedule by Zapier
   - Trigger: Every 2 days at 9 AM
3. **Set condition:**
   - App: Supabase
   - Lookup rows where:
     - `status` = "pending"
     - `created_at` < 2 days ago
4. **Set action (for each row):**
   - App: Webhooks by Zapier
   - POST to Resend (same as Zap 2, but vary subject)
   - Day 2 subject: `"How's your setup going? — Ace Construction"`
   - Day 5 subject: `"Level up your Ace Construction workflow"`
5. **Test & publish**

---

## Quick Checklist

- [ ] Jotform form created and connected
- [ ] Zapier account connected to Supabase
- [ ] Resend API key saved in Zapier
- [ ] Zap 1: Customer signup → Supabase (tested)
- [ ] Zap 2: Day 0 welcome email (tested)
- [ ] Zap 3: Day 2/5 follow-ups (tested)
- [ ] All three zaps published (toggled ON)

---

## Testing

**For each zap:**
1. Submit test form via Jotform
2. Verify row in Supabase
3. Verify email delivery in Resend logs
4. Check recipient inbox

**Expected flow:**
```
Jotform form → Zap 1 (Supabase) → Zap 2 (Day 0 email)
                                ↓
                          Zap 3 (Day 2 email)
                                ↓
                          Zap 3 (Day 5 email)
```

---

## Monitoring

Monitor zap execution in Zapier dashboard:
- Task history tab (shows all runs)
- Success/failure counts per zap
- Error logs for debugging

If a zap fails:
1. Check Jotform form still submitting
2. Verify Supabase credentials (not expired)
3. Check Resend API key valid
4. Review Zapier logs for error message
