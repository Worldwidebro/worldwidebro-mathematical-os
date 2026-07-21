# Content Distribution Calendar

## Architecture: Writing Engine → Publishing → Metrics

```
Content Created (Writing Engine)
    ↓
Supabase: content_releases table
    ↓
n8n Automation (when scheduled_date reached)
    ├─ Email (Resend API)
    ├─ Social (TikTok, Instagram, Twitter)
    ├─ Blog (GitHub → Vercel)
    ├─ Communities (Discord, Circle)
    └─ YouTube (Studio API)
    ↓
Analytics (impressions, clicks, conversions)
```

---

## Weekly Release Schedule (Example: CON-001 + @worldwidebroconstruction)

### MONDAY
| Time | Platform | Content | Venture | Status |
|------|----------|---------|---------|--------|
| 6 AM | Email | Weekly newsletter | CON-001 | scheduled |
| 8 AM | TikTok | Contractor tip | CON-001 | scheduled |
| 10 AM | Blog | Case study | CON-001 | scheduled |
| 12 PM | LinkedIn | Industry insights | @worldwidebroconstruction | draft |

### TUESDAY  
| Time | Platform | Content | Venture | Status |
|------|----------|---------|---------|--------|
| 6 AM | Instagram | Carousel (5 slides) | CON-001 | scheduled |
| 8 AM | TikTok | Behind-the-scenes | CON-001 | scheduled |
| 3 PM | Discord | Community post | @worldwidebroconstruction | live |

### WEDNESDAY
| Time | Platform | Content | Venture | Status |
|------|----------|---------|---------|--------|
| 6 AM | Email | Feature deep-dive | CON-001 | scheduled |
| 8 AM | Twitter | Thread (5 tweets) | @worldwidebroconstruction | scheduled |
| 3 PM | Discord | Live AMA | @worldwidebroconstruction | scheduled |

### THURSDAY
| Time | Platform | Content | Venture | Status |
|------|----------|---------|---------|--------|
| 6 AM | Instagram | Reel (30s) | CON-001 | scheduled |
| 8 AM | TikTok | Educational | @worldwidebroconstruction | scheduled |
| 10 AM | Blog | How-to guide | CON-001 | scheduled |

### FRIDAY
| Time | Platform | Content | Venture | Status |
|------|----------|---------|---------|--------|
| 6 AM | Email | Wins showcase | @worldwidebroconstruction | scheduled |
| 8 AM | Instagram | Testimonial | CON-001 | scheduled |
| 3 PM | YouTube | Upload 1 video | CON-sector | scheduled |

---

## Platforms & Posting Frequency

| Platform | Posts/Week | Best For | Target CTR |
|----------|-----------|----------|-----------|
| Email | 2-4 | Nurture, conversions | 3-5% |
| TikTok | 3-5 | Viral, trending | 2-5% |
| Instagram | 2-4 | Lifestyle, proof | 1-3% |
| Twitter | 2-3 | News, engagement | 0.5-1.5% |
| Blog | 2 | SEO, authority | 5-10% |
| YouTube | 1-2 | Deep content | 1-3% |
| Discord | Daily | Community | 5-10% |
| Circle | Daily | Nurture | 10-15% |

---

## Supabase Table: content_releases

```sql
venture_id | platform | title | scheduled_date | status | published_url | impressions | clicks | conversions
CON-001 | email | "5 contractor tips" | 2026-08-04T06:00 | published | sendout-123 | 450 | 18 | 3
CON-001 | tiktok | "Electrical code 101" | 2026-08-04T08:00 | published | tiktok.com/... | 2300 | 45 | 2
CON-001 | blog | "Ace saves $18K" | 2026-08-04T10:00 | published | blog.con.com/... | 125 | 8 | 1
```

---

## n8n Workflow: Auto-Publish

```
Trigger: Every 30 minutes, check:
  IF content_release.status = 'published' 
  AND NOW() >= content_release.scheduled_date
  THEN:

  FOR EACH row:
    IF platform = 'email':
      → Resend API (send_bulk_email)
    IF platform = 'tiktok':
      → TikTok API (schedule_video)
    IF platform = 'instagram':
      → Instagram API (schedule_post)
    IF platform = 'blog':
      → GitHub commit (auto-deploy)
    IF platform = 'discord':
      → Discord webhook (post_message)
    
    → Update status = 'live'
    → Start analytics tracking
```

---

## Daily Metrics (Automated Report)

```
Date: 2026-08-04

Performance:
- Total impressions: 15,430
- Total clicks: 287
- Total conversions: 23
- Revenue: $2,231 (23 × $97)

Top content (24h):
1. TikTok: "5 contractor mistakes" — 2,300 imp, 45 clicks, 2 conv
2. Email: "Weekly newsletter" — 450 opens, 18 clicks, 3 conv
3. Blog: "Hiring guide" — 125 views, 8 clicks, 1 conv

Lowest:
1. Twitter thread — 12 impressions, 0 clicks
2. LinkedIn post — 8 impressions, 0 clicks

Recommendation: Increase TikTok to 5x/week
```
