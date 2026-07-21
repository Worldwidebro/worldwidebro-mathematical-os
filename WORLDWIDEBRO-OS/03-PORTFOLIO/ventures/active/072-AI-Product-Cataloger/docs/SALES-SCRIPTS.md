---
execution_metadata:
  venture_id: "EC-072-AI-Product-Cataloger"
  agent_completed: "AG-CAO"
  department: "Sales & Billing"
  node: "HW-AIR-01"
  database_link: "DB-POSTGRES:PT-5433"
references:
  - [[EC-072-AI-Product-Cataloger-CAPABILITY-STATEMENT]]
  - [[EC-072-AI-Product-Cataloger-FORMATION-CREDENTIAL-TRACKER]]
  - [[EC-072-AI-Product-Cataloger-AGENT-COMMUNICATION]]
  - [[LOOP-FRAMEWORK]]
---

# ECO Sales Scripts — Brand & Retailer Outreach

**Use:** Acquiring e-commerce brands, local retailers, and product ventures for our digital storefront solutions.
**Pairs with:** `ECO-CAPABILITY-STATEMENT.md` · `ECO-FORMATION-CREDENTIAL-TRACKER.md`.

---

## 1) COLD CALL / INTRO SCRIPT (brand owner / e-com director)
> "Hi [Name], this is [Rep Name] with Ai Product Cataloger. I'm calling because I came across your storefront at [Store URL] and noticed a few optimization gaps in the mobile checkout flow that might be costing you sales. We build sub-second headless storefronts that lower cart abandonment and automate catalog syncs. I'm not looking to sell you a massive redesign today—I just want to send you a 2-page checkout speed audit we ran on your site. What's the best email to send that to?"

---

## 2) EMAIL SEQUENCE

### Touch 1 — Speed Audit & Cart Recovery (Day 0)
**Subject:** Speed audit for [Store Name] checkout flow

> Hi [Name],
>
> I noticed you are running [Platform, e.g., Shopify] for [Store Name]. We ran a quick LCP speed audit on your checkout path and noticed a few latency lags that usually cause a 15-20% drop-off on mobile devices.
>
> We specialize in high-performance storefront engines (Next.js/Medusa) that:
> • Load checkouts in under 300ms (sub-second)
> • Sync catalogs in real-time across Amazon, eBay, and your main site
> • Automate multi-channel cart recovery loops
>
> Speed audit report is attached. Would you be open to a 10-minute speed-check review next Tuesday at 2 PM?
>
> Best,
> [Rep Name] · Ai Product Cataloger

---

## 3) QUALIFYING QUESTIONS
1. What is your current cart abandonment rate?
2. How long does it take to update inventory across all your sales channels?
3. What is your average page-load speed on mobile?
