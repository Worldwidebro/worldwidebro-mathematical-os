# Shopping Intelligence: Commerce Signal Capture

This document outlines the technical mechanisms for parsing competitor advertising, e-commerce listings, and trends across multiple retail channels.

---

## 1. Commerce API & Scraping Mappings

The `Shopping Intelligence Agent` monitors external commerce APIs and listings sites to feed the `DEMAND-DATABASE`.

```text
Shopify Stores + Meta Ads Library + Pinterest Trends + Kickstarter
                        │
                        ▼
           Shopping Intelligence Parser
                        │
                        ▼
               Opportunity Scorecard
```

### A. Meta Ads Library
- **Goal**: Parse active ad spend. High ad run duration (e.g. ad running for >30 days) indicates a profitable product.
- **Process**: Search for keywords like "Obsidian template", "AI Planner", "Automation setup" and flag domains running multi-ad creatives.

### B. Pinterest Trends
- **Goal**: Capture visual, consumer-centric trends early.
- **Process**: Read monthly category reports in "home office", "productivity", and "design" to match color palettes and physical designs.

### C. Shopify Shop Crawling
- **Goal**: Track pricing changes and out-of-stock indicators.
- **Process**: Scan target shop `/collections/all` pages for inventory level drops and newly added SKU layouts.

---

## 2. Signal Integration Matrix

Discovered visual and pricing trends are output directly to `PRODUCT-OPPORTUNITIES.md` and loaded by the dashboard to simulate real-time market trends.
