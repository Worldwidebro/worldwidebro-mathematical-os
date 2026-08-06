# Email Revenue Loop Integration Guide

**Status:** Branded email template created, ready for Resend + Hermes integration  
**Venture:** CON-001 (Ace Construction)  
**Updated:** 2026-08-05

---

## Quick Start (5 min)

### 1. Store Resend API Key

```bash
# Create config directory
mkdir -p ~/.config/resend

# Save your Resend API key
echo "re_your_actual_key_here" > ~/.config/resend/key
chmod 600 ~/.config/resend/key

# Or set environment variable
export RESEND_API_KEY="re_your_key_here"
```

### 2. Load Email Template into Supabase

Seed the `email_sequences` table with CON-001's welcome email:

```sql
INSERT INTO email_sequences (venture_id, stage, template_name, subject, body_html, cta_text, cta_url, delay_hours, enabled)
VALUES 
  ('CON-001', 'welcome', 'con-001-welcome', 
   '🏗️ Your free construction assessment is ready',
   '{{LOAD HTML FROM: WORLDWIDEBRO-OS/05-COMMUNICATIONS/EMAIL-TEMPLATES/con-001-welcome.html}}',
   'Book Your Consultation',
   '/con-001/book-consultation?utm_source=email&utm_campaign=welcome',
   0,
   true
  );
```

### 3. Test Email Send

Expected response from Resend API:
```json
{
  "id": "66ec61cd16e43ce11234567",
  "from": "Ace Construction <noreply@aceconstructionco.com>",
  "to": "winnerscirclewcllc@gmail.com",
  "created_at": "2026-08-05T12:34:56Z"
}
```

---

## Email Template Details

| File | Purpose | Delay |
|------|---------|-------|
| `con-001-welcome.html` | Welcome email ✅ Created | 0h |
| `con-001-value.html` | Day-1 value email | 24h |
| `con-001-quote.html` | Day-3 quote email | 72h |
| `con-001-close.html` | Day-7 close email | 168h |

---

## Brand System

**Header:** Dark green gradient (#1a472a → #2d6a3d)  
**Logo:** 🏗️ Ace Construction  
**Tagline:** Build Better. Build Faster. Build Smart.  
**CTA Button:** Forest green (#2d6a3d), rounded, hover state darkens  
**Benefits:** Green checkmarks, light green highlight box  
**Footer:** Gray background, brand copyright  

---

## Cost

- **Resend:** $0.20/email
- **50 leads/week × 4-email sequence = 200/week ≈ $40/week**
- **Monthly:** ~$160 per venture

---

## Next Steps

1. Configure Resend API key
2. Insert email_sequences rows into Supabase (4 emails)
3. Wire trigger.dev workflow → Hermes → Resend
4. Test full end-to-end: form → Hermes → email send
5. Monitor deal_interactions table for tracking

---

**Template Ready:** ✅ Yes  
**Ready to Deploy:** ⏳ Awaiting Resend API key configuration
