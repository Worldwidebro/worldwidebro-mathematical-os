# OPENCLAW PHASE 1: SaaS Setup (10 minutes)

**Status:** Execute immediately  
**Timeline:** 10 minutes to get API credentials  
**Cost:** Free tier available  

---

## STEP 1: Sign Up for OpenClaw SaaS

1. **Go to:** https://openclaw.com (or https://app.openclaw.io)

2. **Click "Sign Up"**
   - Email: winnerscirclewcllc@gmail.com
   - Password: [create strong password]
   - Organization: Worldwidebro Holdings

3. **Verify Email** (check inbox)

4. **Complete Setup:**
   - Organization name: Worldwidebro Holdings
   - Your name: [Your name]
   - Use case: Contract management for ventures

**Time: 3 minutes**

---

## STEP 2: Generate API Credentials

Once logged in, go to **Settings → API**

### Get Your API Key
1. Click "Create API Key"
2. Name: `worldwidebro-ventures`
3. Permissions: Read + Write
4. **COPY** the key that appears
   - Format: `sk_live_xxxxxxxxxxxxxxxx`
   - **SAVE THIS** → You'll need it for .env.openclaw

### Get OAuth Credentials
1. Go to **Settings → OAuth Apps**
2. Click "Create OAuth App"
3. Name: `worldwidebro-ventures-portal`
4. Redirect URI: `https://your-domain.com/api/auth/callback`
5. **COPY** the Client ID and Secret
   - Client ID format: `oc_client_xxxxxxx`
   - Client Secret format: `oc_secret_xxxxxxx`

### Get Webhook Secret
1. Go to **Settings → Webhooks**
2. Click "Create Webhook Endpoint"
3. URL: `https://your-domain.com/api/webhooks/openclaw-contract-signed`
4. Events: Select `contract.signed`, `contract.signed_by_all`
5. **COPY** the Webhook Secret
   - Format: `whsec_xxxxxxx`

**Time: 5 minutes**

**You now have:**
```
OPENCLAW_API_KEY = sk_live_XXXXXXXXXX
OPENCLAW_CLIENT_ID = oc_client_XXXXXXX
OPENCLAW_CLIENT_SECRET = oc_secret_XXXXXXX
OPENCLAW_WEBHOOK_SECRET = whsec_XXXXXXX
```

---

## STEP 3: Create Contract Templates

In OpenClaw admin dashboard:

1. **Go to:** Templates → Create Template

2. **Create Template #1: Letter of Intent (LOI)**
   - Name: `LOI_GENERIC`
   - Type: Contract
   - Add fields:
     - `venture_name` (text)
     - `customer_name` (text)
     - `customer_email` (email)
     - `terms` (textarea)
     - `amount` (number)
   - Save
   - **COPY template ID** (shown after save)

3. **Create Template #2: Customer Agreement**
   - Name: `CUSTOMER_AGREEMENT`
   - Similar structure
   - **COPY template ID**

4. **Create Template #3: NDA**
   - Name: `NDA_TEMPLATE`
   - **COPY template ID**

**Note:** You can use simple templates for now. Update later.

**Time: 2 minutes**

---

## STEP 4: Fill in .env.openclaw

Now edit your `.env.openclaw` file and fill in:

```bash
# Replace these XXXXXXXXXXX with your actual values:

Line 14:  OPENCLAW_API_KEY="sk_live_YOUR_KEY_HERE"
Line 15:  OPENCLAW_CLIENT_ID="oc_client_YOUR_ID_HERE"
Line 16:  OPENCLAW_CLIENT_SECRET="oc_secret_YOUR_SECRET_HERE"
Line 17:  OPENCLAW_WEBHOOK_SECRET="whsec_YOUR_SECRET_HERE"

# Also fill in:
Line 23:  NEO4J_PASSWORD="your_neo4j_password"
Line 26:  DATABASE_URL="postgresql://user:pass@localhost:5432/company_brain"
```

Save the file (it's in .gitignore, stays local).

**Time: 2 minutes**

---

## ✅ PHASE 1 COMPLETE

You now have:
✅ OpenClaw SaaS account created
✅ API credentials generated
✅ OAuth app set up
✅ Webhook endpoint configured
✅ Contract templates created
✅ .env.openclaw filled in

**Total time: ~10 minutes**

---

## NEXT: Phase 2 (Week 2)

When you're ready for production (Week 2):
- Deploy OpenClaw Docker container
- Migrate from SaaS to self-hosted
- Keep same API keys
- Scale to unlimited contracts

For now: **SaaS is fast and works perfectly for the 5-venture pilot.**

---

## QUICK REFERENCE

**OpenClaw SaaS URLs:**
- Dashboard: https://app.openclaw.io
- API Docs: https://docs.openclaw.io
- Settings: https://app.openclaw.io/settings

**Support:**
- Docs: https://docs.openclaw.io
- Email: support@openclaw.io

