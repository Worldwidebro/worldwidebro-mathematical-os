[[STARTHERE]] | [[INDEX]] | [[AGENTS]]

---
title: WhatsApp Business Platform Setup Guide — Step-by-Step
authority: CP-027 (Infrastructure)
status: ACTIVE (Sep 19, 2026)
version: 1.0
created: 2026-09-19
---

# WhatsApp Business Platform Setup Guide — Step-by-Step

**Objective:** Get WhatsApp Business Platform configured and ready for Company Brain integration.

**Time required:** 45 minutes
**Prerequisites:** 
- Meta Business Account (create if needed)
- Admin access to Meta Business Account
- Phone number to register as WhatsApp Business number
- Webhook URL ready: `https://whatsapp-gateway.company-brain.ai/webhooks/whatsapp`

---

## Step 1: Access Meta Business Account

1. Go to **https://business.facebook.com**
2. Sign in with your Meta account (or create one)
3. You should see your Business Account dashboard

**If you don't have a Business Account:**
- Click "Create Account" in top left
- Enter business name: "Worldwidebro Holdings"
- Fill out business info
- Confirm email

**Credentials to save:**
- [ ] Business Account ID: ___________________

---

## Step 2: Create or Access WhatsApp App

### 2.1 Navigate to Apps

1. In Meta Business Suite, go to **All tools → Apps and websites**
2. Look for "WhatsApp" section
3. If you see "Set up WhatsApp", click it
4. If you see "Go to WhatsApp Manager", click it

### 2.2 Create WhatsApp Business App (if needed)

1. Click **"Create an app"** (if prompted)
2. Select app type: **Business**
3. App name: `Company Brain WhatsApp Gateway`
4. App purpose: Business messaging
5. Click **"Create App"**

**Credentials to save:**
- [ ] App ID: ___________________
- [ ] App Secret: ___________________

---

## Step 3: Get Your Business Account ID

1. In Meta Business Suite, go to **Settings (gear icon) → Account Settings**
2. Look for "Business information"
3. Copy **Business Account ID** (looks like `1234567890123456`)

**Credentials to save:**
- [ ] Business Account ID: ___________________

---

## Step 4: Register Your Phone Number

### 4.1 Navigate to Phone Numbers

1. Go to **Meta Business Suite → WhatsApp → Getting started**
2. Look for section: **"Add a phone number"** or **"Phone Numbers"**
3. Click **"Add phone number"**

### 4.2 Choose Phone Number Type

1. Select: **"Use your own phone number"** (NOT a virtual number)
2. Enter your phone number: **+1 (XXX) XXX-XXXX**
   - Must be in international format starting with `+1`
   - Example: `+1 704 555 0123`
3. Click **"Next"**

### 4.3 Verify Phone Number

1. Meta will send an SMS or call with a verification code
2. Enter the code
3. Click **"Verify"**

**Credentials to save:**
- [ ] Phone Number: ___________________
- [ ] Phone Number ID: ___________________

---

## Step 5: Generate Access Token

### 5.1 Navigate to Access Tokens

1. In Meta Business Suite, go to **Settings (gear icon) → Users**
2. Look for "System users"
3. Click **"Create system user"** (or use existing)
   - Name: `Company Brain Webhook`
   - Role: Admin
   - Click "Create"

### 5.2 Create App-Specific Token

1. Click on the system user you just created
2. Click **"Generate access token"**
3. Select app: **Company Brain WhatsApp Gateway**
4. Select token expiration: **Never expires** (or 60 days if required)
5. Select permissions:
   - ✅ `whatsapp_business_messaging`
   - ✅ `whatsapp_business_account_management`
6. Click **"Generate token"**

**IMPORTANT: Copy the token immediately.** You won't see it again.

**Credentials to save:**
- [ ] META_ACCESS_TOKEN: ___________________

---

## Step 6: Get Phone Number ID

### 6.1 Navigate to Phone Number Settings

1. Go to **WhatsApp → Phone numbers**
2. Click on the phone number you registered
3. Look for "Phone Number ID" in the details

**Credentials to save:**
- [ ] PHONE_NUMBER_ID: ___________________

---

## Step 7: Create Webhook Verification Token

### 7.1 Generate Random Token

Run this command in terminal:

```bash
openssl rand -hex 16
```

This generates a random 32-character hex string. Example output:
```
a1b2c3d4e5f6789012345678901234ab
```

**Credentials to save:**
- [ ] WEBHOOK_VERIFY_TOKEN: ___________________

---

## Step 8: Configure Webhook in Meta

### 8.1 Navigate to Webhook Settings

1. In Meta Business Suite, go to **WhatsApp → Configuration**
2. Look for section: **"Webhooks"** or **"Webhook URL"**
3. Click **"Edit"** or **"Add webhook"**

### 8.2 Enter Webhook Details

**Webhook URL:**
```
https://whatsapp-gateway.company-brain.ai/webhooks/whatsapp
```

**Verify Token:**
```
<paste your WEBHOOK_VERIFY_TOKEN from Step 7>
```

**Events to subscribe to:**
- ✅ `messages` (receive incoming messages)
- ✅ `message_status` (message delivery status)
- ✅ `message_template_status_update` (template changes)

3. Click **"Save"** or **"Confirm"**

### 8.3 Verify Webhook Connection (Important!)

Meta will send a verification request to your webhook URL:
```
GET /webhooks/whatsapp?hub.mode=subscribe&hub.challenge=XXXX&hub.verify_token=YYYY
```

Your FastAPI gateway must respond with the challenge token. Once configured, Meta will show:
- ✅ **Webhook verified**
- ✅ **Active**

---

## Step 9: Store Credentials in Bitwarden

1. Open **Bitwarden**
2. Create new item: **Type: Login**
3. Name: `WhatsApp Business Platform`
4. Add these custom fields:

| Field | Value |
|-------|-------|
| `META_ACCESS_TOKEN` | (from Step 5) |
| `BUSINESS_ACCOUNT_ID` | (from Step 3) |
| `PHONE_NUMBER_ID` | (from Step 6) |
| `WEBHOOK_VERIFY_TOKEN` | (from Step 7) |
| `PHONE_NUMBER` | (from Step 4) |
| `APP_ID` | (from Step 2) |

5. Save to Bitwarden

---

## Step 10: Add Credentials to Docker

### 10.1 Create `.env` file (local development)

Create file: `Company Brain/.env.whatsapp`

```bash
META_ACCESS_TOKEN=a1b2c3d4e5f6...
BUSINESS_ACCOUNT_ID=1234567890123456
PHONE_NUMBER_ID=9876543210987654
WEBHOOK_VERIFY_TOKEN=a1b2c3d4e5f6789012345678901234ab
PHONE_NUMBER=+1 704 555 0123
```

**DO NOT COMMIT TO GIT.** Add to `.gitignore`:

```bash
echo ".env.whatsapp" >> .gitignore
```

### 10.2 Update Docker Compose

Update `docker-compose.yml`:

```yaml
services:
  whatsapp_gateway:
    image: company-brain/whatsapp-gateway:1.0
    environment:
      - META_ACCESS_TOKEN=${META_ACCESS_TOKEN}
      - BUSINESS_ACCOUNT_ID=${BUSINESS_ACCOUNT_ID}
      - PHONE_NUMBER_ID=${PHONE_NUMBER_ID}
      - WEBHOOK_VERIFY_TOKEN=${WEBHOOK_VERIFY_TOKEN}
      - COMPANY_BRAIN_API=http://company-brain-api:8000
      - LOG_LEVEL=info
    ports:
      - "8001:8001"
    depends_on:
      - company-brain-api
    networks:
      - company-brain
```

Load credentials:

```bash
export $(cat .env.whatsapp | xargs)
docker-compose up whatsapp_gateway
```

---

## Step 11: Test Webhook Connection

### 11.1 Send Test Message

1. In Meta Business Suite, go to **WhatsApp → Testing**
2. Click **"Send test message"**
3. Enter a phone number to receive test message
4. Send message

### 11.2 Verify Receipt

1. Check your phone — you should receive the test message
2. Reply with something like: "Test"
3. Check FastAPI logs — you should see the incoming message:

```
INFO: Message received from +1704555XXXX: "Test"
INFO: Processing message...
INFO: Stored in Supabase
```

---

## Step 12: Verify Webhook is Validated

Go back to **WhatsApp → Configuration → Webhooks**

You should see:
- ✅ **Webhook URL:** `https://whatsapp-gateway.company-brain.ai/webhooks/whatsapp`
- ✅ **Status:** Active
- ✅ **Events subscribed:** messages, message_status, message_template_status_update

---

## Troubleshooting

### Webhook Not Connecting

**Problem:** Meta shows "Webhook could not be verified"

**Solutions:**
1. Check that webhook URL is publicly accessible (not localhost)
2. Check that FastAPI is running: `curl https://whatsapp-gateway.company-brain.ai/health`
3. Verify WEBHOOK_VERIFY_TOKEN matches in Meta and code
4. Check firewall — port 443 must be open to Meta IPs

### Not Receiving Messages

**Problem:** Send message but FastAPI doesn't log it

**Solutions:**
1. Verify webhook is marked "Active" in Meta
2. Check events are subscribed: `messages` must be checked
3. Verify phone number is correctly registered
4. Check Supabase — message might be stored but logs not visible

### Access Token Issues

**Problem:** "Invalid access token" error

**Solutions:**
1. Verify token hasn't expired
2. Verify token has `whatsapp_business_messaging` permission
3. Generate new token if needed — old one will be invalidated

---

## Credentials Checklist

Before you start deployment, verify you have:

- [ ] Meta Business Account ID
- [ ] WhatsApp App ID
- [ ] WhatsApp App Secret
- [ ] Phone Number (registered)
- [ ] Phone Number ID
- [ ] META_ACCESS_TOKEN (permanent)
- [ ] WEBHOOK_VERIFY_TOKEN (random 32-char)
- [ ] Webhook URL verified in Meta
- [ ] Credentials stored in Bitwarden
- [ ] `.env.whatsapp` created (NOT in Git)
- [ ] Docker compose updated
- [ ] Test message sent and received

---

## Next Steps

Once you've completed this setup:

1. **Deploy FastAPI gateway** (see `WHATSAPP-INTEGRATION-PLAN.md`)
2. **Wire orchestrator endpoints** (see Phase 3 in plan)
3. **Test intent classification** (send `/help` command)
4. **Enable natural language** (send "What's blocking LT-005?")

---

## Reference Links

- **Meta Business Suite:** https://business.facebook.com
- **WhatsApp API Docs:** https://faq.whatsapp.com/1050934623978152
- **Webhook Reference:** https://developers.facebook.com/docs/whatsapp/webhooks
- **API Reference:** https://developers.facebook.com/docs/whatsapp/cloud-api

---

**Owner:** CP-027 (Infrastructure)  
**Time to complete:** 45 minutes  
**Questions?** Check Troubleshooting section above or refer to official Meta docs

