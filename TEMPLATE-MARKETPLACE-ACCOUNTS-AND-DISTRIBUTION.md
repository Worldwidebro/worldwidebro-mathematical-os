# Template Marketplace: Accounts, Emails & Distribution Sites

**Date:** 2026-08-05  
**Status:** Setup checklist for Week 1  
**Owner:** Worldwidebro Holdings (winnerscirclewcllc@gmail.com)

---

## PRIMARY EMAIL ASSIGNMENTS

| Platform/Service | Email | Status | Purpose |
|---|---|---|---|
| **GitHub (worldwidebro org)** | winnerscirclewcllc@gmail.com | ✅ | Code repos, marketplace-core, integrations |
| **Gumroad** | winnerscirclewcllc@gmail.com | ⏳ | Template sales (10% fee) |
| **Lemon Squeezy** | winnerscirclewcllc@gmail.com | ⏳ | Template sales (5-8% fee, better margins) |
| **Notion Marketplace** | winnerscirclewcllc@gmail.com | ⏳ | Notion template listing (0% fee, approval) |
| **Supabase** | winnerscirclewcllc@gmail.com | ✅ | ventures project (local + cloud) |
| **Stripe** | winnerscirclewcllc@gmail.com | ✅ | Payments (3% fee for direct sales) |
| **Vercel** | winnerscirclewcllc@gmail.com | ✅ | Deployments (template landing pages) |
| **SendGrid / Resend** | winnerscirclewcllc@gmail.com | ⏳ | Email marketing (launch sequences) |
| **Twitter/X** | @worldwidebro (handle) | ⏳ | Social launch (templates + SaaS) |
| **Product Hunt** | winnerscirclewcllc@gmail.com | ⏳ | Launch platform (high ROI, optional) |
| **Notion (workspace)** | winnerscirclewcllc@gmail.com | ✅ | Template creation + docs |

---

## ACCOUNT CREATION CHECKLIST (WEEK 1)

### Priority 1: Revenue (Do This First)

- [ ] **Gumroad**
  - URL: https://gumroad.com/signup
  - Email: winnerscirclewcllc@gmail.com
  - Purpose: Sell individual + bundle templates
  - Revenue share: 90% (you keep, 10% fee)
  - Setup time: 15 min
  - First product live: 30 min
  - Webhook: Save for marketplace-core integration

- [ ] **Lemon Squeezy**
  - URL: https://www.lemonsqueezy.com
  - Email: winnerscirclewcllc@gmail.com
  - Purpose: Mirror Gumroad (better margins)
  - Revenue share: 92-95% (you keep, 5-8% fee)
  - Setup time: 20 min
  - First product live: 30 min
  - Webhook: Save for marketplace-core integration

- [ ] **Stripe (if not already connected)**
  - URL: https://dashboard.stripe.com
  - Email: winnerscirclewcllc@gmail.com
  - Purpose: Direct sales + subscriptions (template + SaaS bundle)
  - Revenue share: 97% (you keep, 3% fee)
  - Setup time: 10 min
  - API keys: Save to encrypted credentials store

### Priority 2: Marketing (Email + Social)

- [ ] **Resend**
  - URL: https://resend.com
  - Email: winnerscirclewcllc@gmail.com
  - Purpose: Launch email sequence (7 emails over 10 days)
  - Setup time: 20 min
  - Email templates: 5 templates pre-built
  - API key: Save to encrypted credentials store

- [ ] **Twitter/X Account Verification**
  - URL: https://twitter.com/worldwidebro (if exists)
  - Email: winnerscirclewcllc@gmail.com
  - Purpose: Launch thread + ongoing promotion
  - Setup time: 5 min (verify + connect)
  - First tweet: Day 1 of Week 3 launch

- [ ] **LinkedIn (Personal Branding)**
  - Email: winnerscirclewcllc@gmail.com
  - Purpose: Professional launch announcement
  - Setup time: 10 min (update profile, add links)
  - First post: Day 1 of Week 3 launch

### Priority 3: Marketplace Listing (Approval Required)

- [ ] **Notion Marketplace**
  - URL: https://www.notion.so/marketplace/partners
  - Email: winnerscirclewcllc@gmail.com
  - Purpose: List templates (0% fee, high discovery)
  - Approval time: 2-5 business days
  - Revenue share: 100% (you keep, 0% fee)
  - Apply by: End of Week 2

- [ ] **Product Hunt** (Optional)
  - URL: https://www.producthunt.com
  - Email: winnerscirclewcllc@gmail.com
  - Purpose: Launch day visibility (500-1000 sales typical)
  - Setup time: 30 min
  - Launch day: First Wednesday of Week 3

### Priority 4: Analytics

- [ ] **Google Analytics 4**
  - URL: https://analytics.google.com
  - Email: winnerscirclewcllc@gmail.com
  - Purpose: Track landing page + template page traffic
  - Setup time: 10 min

---

## API KEYS & CREDENTIALS (Encrypted Storage)

**Location:** `~/.config/worldwidebro/credentials.enc` (encrypted, NOT committed)  
**Tool:** Use `pass` or age encryption

### Keys to Store (Week 1)

| Service | Key Type | Status | Notes |
|---|---|---|---|
| Gumroad | API Token | ⏳ Create | Account → Settings → API |
| Lemon Squeezy | API Key | ⏳ Create | Account → Settings → API Tokens |
| Stripe | Publishable + Secret | ✅ Store existing | Dashboard → API Keys |
| Resend | API Key | ⏳ Create | Account → API Keys |
| GitHub | PAT | ✅ Store existing | Settings → Developer settings |
| Supabase | Service Role Key | ✅ Store existing | Project → Settings → API |

---

## DISTRIBUTION CHANNELS (Week 2-3)

### Primary Sales Channels

| Channel | Fee | Best For | Launch | Expected Monthly |
|---|---|---|---|---|
| **Gumroad** | 10% | Direct sales + recurring | Week 2 | $500-1000 |
| **Lemon Squeezy** | 5-8% | Global audience | Week 2 | $500-1500 |
| **Your Site** | 3% (Stripe) | Brand building | Week 3 | $1000-3000 |
| **Notion Marketplace** | 0% | Discovery + trust | Week 3 | $200-500 |
| **Product Hunt** | N/A | Launch day | Week 3 Day 1 | $2000-5000 (spike) |

### Secondary Discovery

| Channel | Cost | Best For | Launch |
|---|---|---|---|
| **Google Ads** | PPC | Keyword targeting | Week 4 |
| **Twitter Ads** | PPC | Audience targeting | Week 4 |
| **Reddit** | Organic | Community posts | Week 2 |
| **Discord** | Organic | B2B/dev communities | Week 2 |

---

## MARKETPLACE-CORE INTEGRATION

**Account mapping in `marketplace-core/config/creators.yaml`:**

```yaml
creators:
  - id: "bw-001"
    name: "Worldwidebro / BW-001 Beauty"
    email: "winnerscirclewcllc@gmail.com"
    distribution:
      gumroad:
        api_key: "{{ GUMROAD_API_KEY }}"  # encrypted reference
        products: 5
      lemon_squeezy:
        api_key: "{{ LEMON_SQUEEZY_API_KEY }}"  # encrypted reference
        products: 5
      notion_marketplace:
        approved: false
        templates: 3
      direct_sales:
        stripe_account: "{{ STRIPE_CONNECT_ID }}"  # encrypted reference
        landing_page: "https://templates.worldwidebro.com/bw-001"
```

---

## EMAIL LAUNCH SEQUENCE

### Pre-Launch (Week 1-2)

**Day 1-3: Lead Magnet Capture**
- Landing page: "Get the Free Beauty Salon Template"
- CTA: Email capture + template link
- Target: 100-200 Day 1, 200-400 total

**Day 4-7: Email Sequence**
```
Day 4: Welcome + Free Template Access (subject: "Your Free Template Inside")
Day 5: "3 Ways Salon Owners Manage Clients" (content/value email)
Day 6: "Pro Templates Launch Tomorrow" (teaser)
Day 7: "Early Bird 24-Hour Pricing" (launch day)
Day 10: "Last Chance" (pricing expires)
```

### Launch Week (Week 3)

**Day 1 (Tuesday): Launch Day**
- 6am: Email blast to 500+ subscribers
- 10am: Twitter thread (5 tweets)
- 12pm: LinkedIn post + Product Hunt launch
- 2pm: Reddit posts (3 communities)

---

## PAYMENT FLOW (Customer Journey)

```
Customer
   ↓
Gumroad/Lemon Squeezy → Stripe → Bank Account
   ↓
Notion Template (duplicate link)
   ↓
Email nurture sequence
   ↓
SaaS trial
   ↓
SaaS subscription ($29-99/month)
```

**Revenue mix (Month 1-4 per venture):**
- Template sales: 60% of revenue ($1-3K)
- SaaS subscriptions: 40% of revenue ($600-2K)
- **Total:** $1.6-5K/month

---

## WEEK 1 EXECUTION CHECKLIST

- [ ] Gumroad account created + 5 products listed
- [ ] Lemon Squeezy account created + mirror products
- [ ] Resend email account + sequences templated
- [ ] Landing page created (Vercel/Webflow)
- [ ] Email lead magnet live
- [ ] GitHub marketplace-core cloned
- [ ] API keys stored encrypted
- [ ] Gumroad + Lemon Squeezy + Stripe webhooks connected
- [ ] Twitter profile verified + bio updated
- [ ] Google Analytics 4 tracking added
- [ ] Notion template finalized + tested

---

## FAQ: Why One Email for All Accounts?

**All accounts use:** `winnerscirclewcllc@gmail.com`

**Why?**
- Unified creator identity across all platforms
- Easier credential management
- One billing + payout routing
- Aliases can forward to other emails if needed

**Can you add team members later?**
- Gumroad: Yes (Team feature, Pro plan)
- Lemon Squeezy: Yes (Team Members)
- Stripe: Yes (Account Roles)
- Supabase: Yes (Project Members)

---

## STATUS TRACKER

| Task | Status | Deadline |
|---|---|---|
| Gumroad setup | ⏳ | Aug 6 |
| Lemon Squeezy setup | ⏳ | Aug 6 |
| Resend email setup | ⏳ | Aug 7 |
| Landing page live | ⏳ | Aug 7 |
| marketplace-core audit | ⏳ | Aug 8 |
| Lead magnet launch | ⏳ | Aug 9 |
| Twitter verification | ⏳ | Aug 10 |
| Notion Marketplace apply | ⏳ | Aug 12 |
| Launch day (Week 3) | ⏳ | Aug 19 |

---

**Next:** Week 1 execution. Start with Gumroad (15 min) + landing page (1 hour).

**Related files:**
- TEMPLATE-MARKETPLACE-EXECUTION-PLAN.md (Week 1-4 timeline)
- MASTER-INDEX.md (links all setup docs)
