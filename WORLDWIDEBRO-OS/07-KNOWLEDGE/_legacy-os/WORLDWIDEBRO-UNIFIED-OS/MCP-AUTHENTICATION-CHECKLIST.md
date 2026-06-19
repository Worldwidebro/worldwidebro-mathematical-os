# MCP Authentication Checklist — WORLDWIDEBRO Holdings

**Status:** Authentication in progress  
**Date:** 2026-06-09  
**Goal:** Authenticate all 30 MCPs before Task #26 execution

---

## **✅ ALREADY CONNECTED (14 MCPs)**

Stripe, Slack, Supabase, GitHub, Gmail, Google Calendar, Notion, ClickUp, Vercel, Make, Postman, Indeed, Hugging Face, Learning Commons

**Count: 14/30 ✅**

---

## **⏸ PENDING AUTHENTICATION (10 MCPs)**

### **Priority 1: Revenue + CRM (Day 1 execution)**

#### Buffer — Social Media Scheduling
- Get token from: https://buffer.com/settings/apps
- Env var: `BUFFER_ACCESS_TOKEN`

#### Beehiiv — Newsletter Platform
- Get key from: https://www.beehiiv.com/api
- Env var: `BEEHIIV_API_KEY`

#### Twitter — Post & Analytics
- Get keys from: https://developer.twitter.com/en/portal/dashboard
- Env vars: `TWITTER_API_KEY`, `TWITTER_API_SECRET`, `TWITTER_ACCESS_TOKEN`, `TWITTER_ACCESS_TOKEN_SECRET`

#### HubSpot — CRM & Sales
- Get key from: https://app.hubspot.com/l/app-marketplace/2916063
- Env var: `HUBSPOT_API_KEY`

---

### **Priority 2: Intelligence (Days 2-14)**

#### Tavily — Web Search
- Get key from: https://tavily.com
- Env var: `TAVILY_API_KEY`

#### Crunchbase — Company Research
- Get key from: https://data.crunchbase.com/api
- Env var: `CRUNCHBASE_API_KEY`

#### Qdrant — Vector Database
- Cloud: https://cloud.qdrant.io
- Env vars: `QDRANT_URL`, `QDRANT_API_KEY`

---

### **Priority 3: Content & Design (Week 2)**

#### Figma — Design System
- Get token from: https://www.figma.com/developers
- Env var: `FIGMA_API_TOKEN`

#### WordPress — Publishing
- Get app password from: WordPress admin → Users → Application Passwords
- Env vars: `WORDPRESS_URL`, `WORDPRESS_USERNAME`, `WORDPRESS_PASSWORD`

---

### **No Auth Required**

#### arXiv — Academic Research
- Public API — ready to use

---

## **🏗️ PROPRIETARY MCPs (Build after auth)**

Portfolio MCP, KPI MCP, Deal-Flow MCP, Media MCP, SOP MCP, Skills Registry MCP

---

## **AUTHENTICATION STATUS**

| Status | Count | MCPs |
|--------|-------|------|
| ✅ Connected | 14 | Stripe, Slack, Supabase, GitHub, Gmail, Google Calendar, Notion, ClickUp, Vercel, Make, Postman, Indeed, Hugging Face, Learning Commons |
| ⏸ Pending keys | 9 | Buffer, Beehiiv, Twitter, HubSpot, Tavily, Crunchbase, Qdrant, Figma, WordPress |
| ✅ No auth | 1 | arXiv |
| 🏗️ To build | 6 | Portfolio, KPI, Deal-Flow, Media, SOP, Skills Registry |
| **TOTAL** | **30** | **24/30 ready** |

---

## **NEXT STEP**

Provide API keys for the 9 pending MCPs, and I'll:
1. Set all environment variables
2. Test each MCP
3. Confirm all 30 are authenticated
4. Execute Task #26 Day 1

**Ready to gather keys?**
