# OpenClaw SaaS Signup - Visual Step-by-Step Guide

**Timeline:** 10 minutes  
**Cost:** Free tier  
**Status:** Ready to execute  

---

## STEP 1: Go to OpenClaw Signup (1 min)

```
1. Open your browser
2. Go to: https://app.openclaw.io
3. You'll see the OpenClaw login page
4. Click "Sign Up" button (usually top right or center)
```

**What you'll see:**
- OpenClaw logo (top left)
- "Sign In" and "Sign Up" buttons
- A description: "The open-source legal document management platform"

---

## STEP 2: Create Account (2 min)

**Form fields to fill:**

```
Email:        winnerscirclewcllc@gmail.com
Password:     [Create a strong password, 12+ chars, mix upper/lower/numbers]
Organization: Worldwidebro Holdings
Full Name:    [Your name]
```

**After filling:**
- Click "Sign Up" button
- Check your email for verification link
- Click the verification link in your email
- Return to OpenClaw - you'll be logged in

---

## STEP 3: Go to Settings → API (2 min)

**Once logged in:**

```
1. Look for "Settings" in the top right menu (usually your avatar/gear icon)
2. Click "Settings"
3. In the left sidebar, click "API"
4. Click "Create API Key"
```

**Fill the form:**
- **Name:** `worldwidebro-ventures`
- **Permissions:** Select "Read + Write"
- Click "Create"

**IMPORTANT:** After clicking Create, you'll see the API key displayed ONCE
```
⚠️  COPY THIS IMMEDIATELY - you won't see it again:
   sk_live_xxxxxxxxxxxxxxxx

💾 Save it to a text file or clipboard
```

**You now have:**
```
OPENCLAW_API_KEY = sk_live_xxxxxxxxxxxxxxxx
```

---

## STEP 4: Create OAuth App (2 min)

**Still in Settings:**

```
1. In the left sidebar, look for "OAuth Apps" or "Applications"
2. Click "Create OAuth App"
```

**Fill the form:**
```
Name:           worldwidebro-ventures-portal
Redirect URI:   https://your-domain.com/api/auth/callback
               (This is your Vercel domain - adjust if different)
```

**After creation, you'll see:**
```
Client ID:     oc_client_xxxxxxx
Client Secret: oc_secret_xxxxxxx

⚠️  COPY BOTH IMMEDIATELY - you won't see the secret again
```

**You now have:**
```
OPENCLAW_CLIENT_ID = oc_client_xxxxxxx
OPENCLAW_CLIENT_SECRET = oc_secret_xxxxxxx
```

---

## STEP 5: Create Webhook Endpoint (2 min)

**Still in Settings:**

```
1. In the left sidebar, click "Webhooks"
2. Click "Create Webhook Endpoint"
```

**Fill the form:**
```
Name:   worldwidebro-contracts
URL:    https://your-domain.com/api/webhooks/openclaw-contract-signed
Events: Select these checkboxes:
        ☑ contract.signed
        ☑ contract.signed_by_all
```

**After creation, you'll see:**
```
Webhook Secret: whsec_xxxxxxx

⚠️  COPY THIS IMMEDIATELY - you won't see it again
```

**You now have:**
```
OPENCLAW_WEBHOOK_SECRET = whsec_xxxxxxx
```

---

## STEP 6: Create Contract Templates (1 min)

**Still in OpenClaw:**

```
1. Look for "Templates" in the left sidebar or top menu
2. Click "Create Template"
3. Name: LOI_GENERIC
4. Type: Contract
5. Add these fields:
   - venture_name (text)
   - customer_name (text)
   - customer_email (email)
   - terms (textarea)
   - amount (number)
6. Click "Create"
7. After creation, note the template ID shown
```

**Repeat for:**
- CUSTOMER_AGREEMENT (same fields)
- NDA_TEMPLATE (same fields)

---

## STEP 7: You Now Have All Credentials

**Your credentials (from Steps 3-5):**

```
OPENCLAW_API_KEY = sk_live_xxxxxxxxxxxxxxxx
OPENCLAW_CLIENT_ID = oc_client_xxxxxxx
OPENCLAW_CLIENT_SECRET = oc_secret_xxxxxxx
OPENCLAW_WEBHOOK_SECRET = whsec_xxxxxxx
```

---

## NEXT: Auto-Fill .env.openclaw

Once you have the 4 credentials above, run this command:

```bash
bash _IMPLEMENTATION/OPENCLAW-CREDENTIALS-FILL-SCRIPT.sh
```

The script will:
1. Ask you to paste each credential
2. Automatically fill .env.openclaw
3. Show you what was filled (without exposing secrets)

---

## TROUBLESHOOTING

**"I can't find the Settings menu"**
- Look for your avatar or profile icon in the top right corner
- Click it, then look for "Settings" or "Account Settings"

**"I can't find API section"**
- Go to Settings → scroll down → look for "API Keys" or "Developer"

**"I lost the API key/secret"**
- Go back to Settings → API Keys → Delete old one and create new one

**"Webhook endpoint not showing"**
- Make sure you're in Settings → Webhooks → not Settings → API

---

## TIMELINE

- Step 1 (Go to OpenClaw): 1 min
- Step 2 (Create account): 2 min
- Step 3 (Get API key): 2 min
- Step 4 (Create OAuth): 2 min
- Step 5 (Create webhook): 2 min
- Step 6 (Create templates): 1 min
- **TOTAL: 10 minutes**

---

## WHAT TO DO AFTER

Once you have all 4 credentials (API key, Client ID, Client Secret, Webhook Secret):

1. Run the auto-fill script:
   ```bash
   bash _IMPLEMENTATION/OPENCLAW-CREDENTIALS-FILL-SCRIPT.sh
   ```

2. Come back and tell me: **"✅ OpenClaw credentials filled"**

3. I'll guide you through Phase 2 (GitHub Secrets)

---

## START NOW

Go to: **https://app.openclaw.io**

Click "Sign Up"

⏱️ You'll be done in 10 minutes

