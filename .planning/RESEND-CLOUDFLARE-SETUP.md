# Resend + Cloudflare Setup for con-001-ace-construction

**Status:** Setup guide ready for execution  
**Venture:** con-001-ace-construction (Construction, North Carolina)  
**Supabase Project:** rhlkjelglvurowdalrgh.supabase.co  
**Timeline:** Complete these steps before Vercel deployment

---

## Overview

This guide sets up email (Resend) and DNS/SSL (Cloudflare) for lead capture and secure deployment. After completing these steps, con-001 can:
- Send transactional emails (lead confirmations, inquiry responses)
- Serve on a custom domain with SSL
- Route traffic through Cloudflare's CDN and security layer

---

## Step 1: Create Resend Account & Get API Key

### 1a. Sign up
1. Go to **https://resend.com**
2. Click **"Sign up"**
3. Use your email: `winnerscirclewcllc@gmail.com`
4. Verify email and set password

### 1b. Get API Key
1. After login, go to **Dashboard > API Keys**
2. Click **"Create API Key"**
3. Name it: `con-001-ace-construction`
4. Copy the key (format: `re_...`)
5. **SAVE THIS** — you'll need it in Step 6

---

## Step 2: Register Your Domain with Cloudflare

### 2a. Choose a domain for con-001
Options:
- `aceconstructionservices.com` (recommended, construction-specific)
- `aceconstructionpros.com`
- `ncacebuilders.com` (geo-specific to North Carolina)

Register via:
- Namecheap, GoDaddy, or your existing registrar
- Or register directly via Cloudflare (they'll handle everything)

**Cost:** ~$10-15/year

### 2b. Add domain to Cloudflare
1. Go to **https://dash.cloudflare.com**
2. Click **"Add a site"**
3. Enter your domain name
4. Click **"Add site"**
5. Select the **Free plan** (sufficient for lead capture)
6. Cloudflare will show you **two nameservers** to add

---

## Step 3: Update Domain Registrar Nameservers

This step connects your domain to Cloudflare.

### 3a. Copy Cloudflare nameservers
From Cloudflare dashboard, you'll see something like:
- `emma.ns.cloudflare.com`
- `neil.ns.cloudflare.com`

(The exact names vary per domain)

### 3b. Update your domain registrar
1. Log in to your domain registrar (Namecheap, GoDaddy, etc.)
2. Find **"Nameservers"** or **"DNS Settings"** for your domain
3. Replace existing nameservers with Cloudflare's two nameservers
4. **Save**
5. Wait 24-48 hours for propagation (often faster, 2-4 hours)

### Verify propagation
```bash
# In terminal, check when nameservers update
dig your-domain.com NS

# Should show Cloudflare nameservers after propagation
```

---

## Step 4: Add Resend DNS Records to Cloudflare

Once your domain is in Cloudflare, you need to add Resend's DNS records for email sending.

### 4a. Get Resend DNS records
1. In Resend dashboard: **Settings > Domains**
2. Click **"Add Domain"**
3. Enter your domain (e.g., `aceconstructionservices.com`)
4. Resend will show **3 DNS records** to add:
   - `CNAME` record for domain verification
   - `MX` record for mail receiving (if using Resend for incoming email)
   - `TXT` record for DKIM signing

Copy these records.

### 4b. Add records to Cloudflare
1. Go to Cloudflare: **Websites > Your Domain > DNS**
2. Click **"Add record"**
3. For each Resend record, fill:
   - **Type:** (CNAME, MX, or TXT)
   - **Name:** (from Resend, e.g., `default._domainkey`)
   - **Content:** (from Resend, e.g., `default.dkim.resend.com`)
   - **TTL:** 3600 (or default)
   - **Proxy status:** DNS only (gray cloud)
4. Click **"Save"** for each

### 4c. Verify in Resend
1. Back in Resend: **Settings > Domains**
2. Click **"Verify"** next to your domain
3. Resend will check DNS records
4. Status should show **"Verified"** after a few minutes

---

## Step 5: Test Resend Email via API

### 5a. Locally, test sending an email
Create a test script:

```bash
cat > /tmp/test-resend.sh << 'EOF'
#!/bin/bash
RESEND_API_KEY="re_YOUR_KEY_HERE"  # Replace with your key from Step 1b

curl -X POST https://api.resend.com/emails \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer $RESEND_API_KEY" \
  -d '{
    "from": "noreply@aceconstructionservices.com",
    "to": "your-email@gmail.com",
    "subject": "Test Email from ace-construction",
    "html": "<p>If you see this, Resend is working!</p>"
  }'
EOF

bash /tmp/test-resend.sh
```

**Expected response:**
```json
{
  "id": "abc123...",
  "from": "noreply@aceconstructionservices.com",
  "to": "your-email@gmail.com",
  "created_at": "2026-07-16T...",
  "status": "sent"
}
```

If successful, email arrives in your inbox within 30 seconds.

---

## Step 6: Configure con-001 Environment

### 6a. Fill in .env.local
Navigate to con-001:
```bash
cd /Users/acebless/Documents/con-001-ace-construction
```

Edit `.env.local` (already created):
```bash
nano .env.local
```

Replace placeholders:
```env
# From your actual Supabase project (already filled)
NEXT_PUBLIC_SUPABASE_URL=https://rhlkjelglvurowdalrgh.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=<get from Supabase dashboard > Settings > API Keys > anon key>

# From Resend Step 1b
RESEND_API_KEY=re_YOUR_KEY_FROM_STEP_1B

# Only if using Stripe for payments
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_test_...
STRIPE_SECRET_KEY=sk_test_...

# Update after Vercel deployment
NEXT_PUBLIC_APP_URL=http://localhost:3000  # Keep localhost for now
```

### 6b. Verify .env.local is in .gitignore
```bash
cat .gitignore | grep ".env.local"
# Should show: .env.local
```

If missing, add it:
```bash
echo ".env.local" >> .gitignore
```

### 6c. Test locally
```bash
npm install
npm run dev
```

Visit `http://localhost:3000` — should load without errors.

---

## Step 7: Deploy to Vercel with Env Vars

### 7a. Connect repo to Vercel (if not already done)
1. Go to **https://vercel.com**
2. Click **"Import Project"**
3. Select GitHub > `con-001-ace-construction` repo
4. Click **"Import"**

### 7b. Add environment variables in Vercel
1. In Vercel dashboard: **Project > Settings > Environment Variables**
2. Add each variable:
   - **Name:** `RESEND_API_KEY`
   - **Value:** `re_...` (from Step 1b)
   - **Select environments:** Production + Preview
   - Click **"Add"**

3. Repeat for:
   - `NEXT_PUBLIC_SUPABASE_URL`
   - `NEXT_PUBLIC_SUPABASE_ANON_KEY`
   - `NEXT_PUBLIC_APP_URL` (e.g., `https://aceconstructionservices.com`)

### 7c. Deploy
```bash
git add -A
git commit -m "chore: add Resend + Supabase configuration"
git push origin main
```

Vercel will auto-deploy. Watch the deployment in Vercel dashboard.

---

## Step 8: Point Custom Domain to Vercel

Once deployed, connect your custom domain to Vercel.

### 8a. In Vercel dashboard
1. Go to **Project > Settings > Domains**
2. Click **"Add Domain"**
3. Enter: `aceconstructionservices.com` (or your chosen domain)
4. Click **"Add"**
5. Vercel shows a **CNAME record** to add

### 8b. Add CNAME to Cloudflare
1. In Cloudflare: **DNS > Add record**
2. **Type:** CNAME
3. **Name:** `@` (or leave empty for root)
4. **Content:** (from Vercel, e.g., `cname.vercel-dns.com`)
5. **TTL:** 3600
6. **Proxy status:** DNS only (gray cloud)
7. Click **"Save"**

### 8c. Verify DNS
After 5-10 minutes:
```bash
dig aceconstructionservices.com

# Should show CNAME pointing to Vercel
```

Visit your domain in browser — should load con-001.

---

## Step 9: Test End-to-End Email + Lead Capture

### 9a. Fill out lead form on your site
1. Visit `https://aceconstructionservices.com`
2. Fill in a lead capture form (name, email, phone)
3. Submit

### 9b. Check Resend logs
1. In Resend dashboard: **Activity > Logs**
2. Should see an email sent to the lead with their inquiry details

### 9c. Verify in Supabase
1. Go to Supabase: **Project > Editor > venture_leads** table
2. Should see new row with the lead's info

**Expected flow:**
- User fills form → Supabase inserts row → Next.js API calls Resend → Lead gets email confirmation

---

## Step 10: SSL Certificate (Automatic)

Cloudflare automatically issues a free SSL certificate via Universal SSL.

### Verify SSL
```bash
curl -I https://aceconstructionservices.com

# Should show: HTTP/2 200 and certificate details
```

Your site is now served securely over HTTPS.

---

## Troubleshooting

### "Email not sent" (Resend API)
- Check API key is correct in `.env.local`
- Verify domain DNS records propagated (use `dig`)
- Check Resend activity logs for error message
- Try test script from Step 5a

### "DNS propagation stuck"
- Nameservers take 24-48 hours, sometimes longer
- Clear DNS cache: `sudo dscacheutil -flushcache` (macOS)
- Use online DNS checker: https://dnschecker.org

### "Domain not loading on Vercel"
- Ensure CNAME record added to Cloudflare
- Ensure CNAME target matches Vercel's cname.vercel-dns.com
- Wait 10 minutes for DNS propagation

### "Cloudflare blocking Resend API calls"
- In Cloudflare: **SSL/TLS > Overview** → ensure "Full" or "Full (strict)"
- Add Resend IP to Cloudflare whitelist if needed

---

## Checklist: Ready to Deploy

- [ ] Resend account created, API key saved
- [ ] Custom domain registered
- [ ] Domain added to Cloudflare
- [ ] Nameservers updated at registrar
- [ ] Resend DNS records added to Cloudflare
- [ ] Resend domain verified
- [ ] Test email sent successfully
- [ ] .env.local filled with Resend API key
- [ ] .env.local added to .gitignore
- [ ] Deployed to Vercel with environment variables
- [ ] Custom domain CNAME added to Cloudflare
- [ ] SSL certificate active (HTTPS working)
- [ ] Lead form tested end-to-end

---

## Next Steps (Post-Deployment)

1. **Monitor email delivery:** Resend dashboard > Activity
2. **Track leads:** Supabase > venture_leads table
3. **Set up lead notifications:** Configure Slack webhook or email alerts when new lead comes in
4. **Test from different regions:** Ensure Cloudflare CDN delivering fast
5. **Monitor uptime:** Uptime Robot or Cloudflare Analytics

---

**Support:**
- Resend docs: https://resend.com/docs
- Cloudflare docs: https://developers.cloudflare.com
- Vercel docs: https://vercel.com/docs
