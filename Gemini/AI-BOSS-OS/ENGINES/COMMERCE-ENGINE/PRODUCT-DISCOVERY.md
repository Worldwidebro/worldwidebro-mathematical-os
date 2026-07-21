# Product Discovery: Market Scanning & Opportunity Identification

This document defines the protocols, scraping points, and analysis frameworks used by our automated agents to identify high-margin product opportunities.

---

## 1. Multi-Channel Scanning Matrix

The `Trend Hunter Agent` actively monitors 12 major commerce feeds daily. It filters items based on growth speed, customer complaints, and search volume:

```text
    TikTok Shop + Amazon Best Sellers + Google Trends + Reddit + Product Hunt
                                │
                                ▼
                       Opportunity Scanner
                                │
                                ▼
                     PRODUCT-OPPORTUNITIES.md
```

### Scraping Focus Areas
- **TikTok Shop**: Monitor trending items in categories like productivity tools, desk accessories, and tech organizers.
- **Amazon Best Sellers**: Track rapid risers in books, digital templates, and home office products.
- **Reddit Communities**: Analyze subreddits like `r/startup`, `r/nocode`, and `r/productivity` for user complaints ("I need a tool that does X").
- **Product Hunt**: Track successful software/template launches.
- **Meta Ads Library & Competitor Ads**: Identify which products are running high-spend ad campaigns.

---

## 2. Opportunity Scoring Formula

Every discovered product is scored on a scale of 0 to 100 based on the following weights:

```text
Product Score = 0.3 * Demand + 0.3 * Margin + 0.2 * Competition + 0.2 * ProductionComplexity
```

- **Demand (30%)**: Verified search velocity and viral video views.
- **Margin (30%)**: Target selling price minus sourcing/production cost (target margin > 70%).
- **Competition (20%)**: Number of active sellers or competitor ads running.
- **Production Complexity (20%)**: Digital templates and software get a 10/10. Custom-manufactured goods get lower scores (2/10 to 5/10) due to supply chain overhead.

---

## 3. Discovered Opportunity Output Format

Discovered opportunities are saved directly into `/Users/acebless/Documents/Gemini/AI-BOSS-OS/ENGINES/COMMERCE-ENGINE/PRODUCT-OPPORTUNITIES.md` in the following format:

```yaml
Opportunity: AI Productivity Planner
Demand: High (+45% MoM search)
Audience: Entrepreneurs & Developers
Pain: "I need to organize my multi-agent workflows and local models"
Competition: Medium
Target Margin: 82%
Recommendation: Create dynamic Notion template & Obsidian Vault.
```
