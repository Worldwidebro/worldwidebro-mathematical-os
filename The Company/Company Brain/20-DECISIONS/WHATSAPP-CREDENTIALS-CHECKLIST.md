---
title: WhatsApp Credentials Checklist — Print & Reference
status: ACTIVE
version: 1.0
---

# WhatsApp Business Platform — Credentials Checklist

**Print this page.** Use it while following `WHATSAPP-SETUP-GUIDE.md`.

**Date started:** _________________ | **Date completed:** _________________

---

## Phase 1: Meta Business Account

### Account Setup

- [ ] Meta Business Account created/accessed
  - URL: https://business.facebook.com
  - Account email: _________________________

- [ ] Business Account ID retrieved
  - Location: Settings → Account Settings → Business information
  - **Business Account ID:** `________________________________`

---

## Phase 2: WhatsApp App

### App Creation

- [ ] WhatsApp Business app created
  - App name: `Company Brain WhatsApp Gateway`
  - App type: Business

- [ ] App credentials saved
  - **App ID:** `________________________________`
  - **App Secret:** `________________________________`

---

## Phase 3: Phone Number Registration

### Phone Registration

- [ ] Phone number registered in Meta
  - Format: +1 (XXX) XXX-XXXX (international format)
  - **Phone Number:** `________________________________`

- [ ] Phone number verified via SMS/call
  - Verification code entered: ✅

- [ ] Phone Number ID retrieved
  - Location: WhatsApp → Phone numbers → Select number
  - **Phone Number ID:** `________________________________`

---

## Phase 4: Access Token

### System User Setup

- [ ] System user created
  - Name: `Company Brain Webhook`
  - Role: Admin
  - ✅ Confirmed

- [ ] Access token generated
  - App: `Company Brain WhatsApp Gateway`
  - Expiration: Never expires (or 60 days)
  - Permissions:
    - ✅ `whatsapp_business_messaging`
    - ✅ `whatsapp_business_account_management`

- [ ] Token saved immediately (only shown once!)
  - **META_ACCESS_TOKEN:** `________________________________`
  - ⚠️ Store in Bitwarden immediately

---

## Phase 5: Webhook Configuration

### Webhook Token

- [ ] Random verification token generated
  ```bash
  openssl rand -hex 16
  ```
  - **WEBHOOK_VERIFY_TOKEN:** `________________________________`

### Webhook Registration in Meta

- [ ] Webhook URL entered in Meta
  - **URL:** `https://whatsapp-gateway.company-brain.ai/webhooks/whatsapp`
  - ✅ Confirmed in Meta

- [ ] Webhook verification token entered
  - ✅ Token matches local copy

- [ ] Events subscribed in Meta
  - ✅ `messages`
  - ✅ `message_status`
  - ✅ `message_template_status_update`

- [ ] Webhook status in Meta
  - Status: ✅ **Active**
  - Verified: ✅ **Yes**

---

## Phase 6: Bitwarden Storage

### Secure Credential Storage

- [ ] Bitwarden item created
  - Name: `WhatsApp Business Platform`
  - Type: Login

- [ ] All 4 credentials stored
  - ✅ `META_ACCESS_TOKEN`
  - ✅ `BUSINESS_ACCOUNT_ID`
  - ✅ `PHONE_NUMBER_ID`
  - ✅ `WEBHOOK_VERIFY_TOKEN`

- [ ] Additional fields stored (reference)
  - ✅ `PHONE_NUMBER`
  - ✅ `APP_ID`

---

## Phase 7: Local Configuration

### .env File

- [ ] `.env.whatsapp` file created locally
  ```bash
  META_ACCESS_TOKEN=...
  BUSINESS_ACCOUNT_ID=...
  PHONE_NUMBER_ID=...
  WEBHOOK_VERIFY_TOKEN=...
  PHONE_NUMBER=...
  ```

- [ ] `.env.whatsapp` added to `.gitignore`
  ```bash
  echo ".env.whatsapp" >> .gitignore
  ```

- [ ] **DO NOT COMMIT TO GIT** ⚠️

### Docker Compose

- [ ] `docker-compose.yml` updated
  - ✅ `whatsapp_gateway` service added
  - ✅ Environment variables reference `.env.whatsapp`
  - ✅ Ports configured: `8001:8001`
  - ✅ Networks configured

---

## Phase 8: Testing

### Webhook Validation

- [ ] FastAPI gateway running
  ```bash
  docker-compose up whatsapp_gateway
  ```

- [ ] Health check passes
  ```bash
  curl https://whatsapp-gateway.company-brain.ai/health
  ```
  Response: `{"status": "ok"}`

- [ ] Test message sent from Meta
  - Location: WhatsApp → Testing → Send test message
  - Test message received on phone: ✅

- [ ] Reply sent from phone to test webhook
  - Message sent: `Test`
  - FastAPI logs show: `Message received from +1...`
  - ✅ Logged to Supabase

- [ ] Webhook marked Active in Meta
  - Status: ✅ **Active**
  - Last validated: ✅ **Today**

---

## Final Checklist

### All Credentials Gathered ✅

- [ ] Business Account ID: `_______________________`
- [ ] Phone Number ID: `_______________________`
- [ ] META_ACCESS_TOKEN: `_______________________`
- [ ] WEBHOOK_VERIFY_TOKEN: `_______________________`

### All Configured ✅

- [ ] Credentials stored in Bitwarden
- [ ] `.env.whatsapp` created locally
- [ ] `docker-compose.yml` updated
- [ ] Webhook registered in Meta
- [ ] Webhook verified and Active
- [ ] Test message sent & received
- [ ] FastAPI logs show incoming messages

### Ready for Phase 2 ✅

- [ ] All 8 phases complete
- [ ] Time elapsed: _________________ minutes
- [ ] No errors or blockers

---

## Troubleshooting Reference

If something fails, check:

### Webhook Not Connecting
- [ ] FastAPI is running on port 8001
- [ ] Webhook URL is publicly accessible (not localhost)
- [ ] WEBHOOK_VERIFY_TOKEN matches in Meta and code
- [ ] Firewall allows port 443 to Meta IPs

### Not Receiving Messages
- [ ] Webhook shows "Active" in Meta
- [ ] "messages" event is checked/subscribed
- [ ] Phone number is correctly registered
- [ ] Check Supabase — message may be logged even if logs don't show

### Access Token Issues
- [ ] Token hasn't expired
- [ ] Token has `whatsapp_business_messaging` permission
- [ ] Generate new token if needed

---

## Next Steps (After Setup)

Once all checkboxes are ✅:

1. **Deploy FastAPI gateway** (see `WHATSAPP-INTEGRATION-PLAN.md`)
2. **Wire orchestrator endpoints** (Phase 2 in integration plan)
3. **Test commands** (send `/help`)
4. **Enable natural language** (send "What's blocking LT-005?")

---

## Keep This Handy

- **Print this checklist**
- **Open `WHATSAPP-SETUP-GUIDE.md`** in browser
- **Have Bitwarden open**
- **Have Meta Business Account open**

---

**Owner:** CP-027 (Infrastructure)  
**Est. time:** 45 minutes  
**Difficulty:** Straightforward (follow steps exactly)

