# MCP Quick Auth Guide — Get URLs & Keys

**Goal:** Authenticate 10 MCPs in 15 minutes, then execute Task #26 Day 1.

---

## **ALREADY AUTHENTICATED (13 MCPs) ✅**

No action needed. Use directly:
- Stripe, Slack, Supabase, Gmail, Calendar, ClickUp, Notion, Make, Vercel, Indeed, Hugging Face, Learning Commons, BrowserOS

---

## **NEED QUICK AUTH (10 MCPs)**

### **1. Buffer** — Social Media Scheduling
**URL:** https://buffer.com/settings/apps  
**Get:** Access Token  
**Set:** `export BUFFER_ACCESS_TOKEN="[token]"`  
**Time:** 2 min

---

### **2. Beehiiv** — Newsletter
**URL:** https://www.beehiiv.com/api  
**Get:** API Key  
**Set:** `export BEEHIIV_API_KEY="[key]"`  
**Time:** 2 min

---

### **3. Twitter** — Social Posting
**URL:** https://developer.twitter.com/en/portal/dashboard  
**Get:** 4 keys (API Key, Secret, Access Token, Token Secret)  
**Set:**
```bash
export TWITTER_API_KEY="[key]"
export TWITTER_API_SECRET="[secret]"
export TWITTER_ACCESS_TOKEN="[token]"
export TWITTER_ACCESS_TOKEN_SECRET="[secret]"
```
**Time:** 3 min

---

### **4. HubSpot** — CRM
**URL:** https://app.hubspot.com/l/app-marketplace/2916063  
**Get:** Private App Access Token  
**Set:** `export HUBSPOT_API_KEY="[key]"`  
**Time:** 2 min

---

### **5. Tavily** — Web Search
**URL:** https://tavily.com  
**Get:** API Key  
**Set:** `export TAVILY_API_KEY="[key]"`  
**Time:** 2 min

---

### **6. Crunchbase** — Company Research
**URL:** https://data.crunchbase.com/api  
**Get:** API Key  
**Set:** `export CRUNCHBASE_API_KEY="[key]"`  
**Time:** 2 min

---

### **7. Qdrant** — Vector Database
**URL:** https://cloud.qdrant.io  
**Get:** API Key + Cluster URL  
**Set:**
```bash
export QDRANT_URL="https://[cluster].qdrant.io"
export QDRANT_API_KEY="[key]"
```
**Time:** 3 min (or use localhost:6333 for local)

---

### **8. Figma** — Design System
**URL:** https://www.figma.com/developers  
**Get:** Personal Access Token  
**Set:** `export FIGMA_API_TOKEN="[token]"`  
**Time:** 2 min

---

### **9. WordPress** — Content Publishing
**URL:** Your WordPress admin → Users → Application Passwords  
**Get:** App Password  
**Set:**
```bash
export WORDPRESS_URL="https://yoursite.com"
export WORDPRESS_USERNAME="[username]"
export WORDPRESS_PASSWORD="[app_password]"
```
**Time:** 2 min

---

### **10. arXiv** — Academic Research
**Status:** ✅ Public API (no auth needed)

---

## **TOTAL AUTH TIME: ~22 minutes**

---

## **NEXT STEPS**

1. **Gather API keys** from the URLs above (15 min)
2. **Set environment variables** (5 min)
3. **Execute Task #26 Day 1** with authenticated MCPs (30 min)
4. **Checkpoint:** Lock in what works
5. **Continue:** Build proprietary MCPs or more auth

**Ready to start?**
