# Analytics Agent

**Goal:** Pull platform data, rank content, feed the content brain.

## Inputs
- `gf_content_assets` where status=published
- Platform APIs: YouTube, Instagram, TikTok, X (via n8n or manual CSV)
- Thresholds from `REGISTRY/weekly-triggers.json`

## Outputs
- `gf_analytics_snapshots` rows (24h cadence)
- Updated `viral_score` / `conversion_score` on hooks and assets
- Saturday `gf_weekly_reports` JSON

## Scoring (simple v1)
```
viral_score = log10(views+1)*2 + shares*3 + saves*2 + ctr*100
conversion_score = site_visits*0.5 + email_signups*5
```

## Promotion rules
| Condition | Action |
|-----------|--------|
| views ≥ 5000 | Tag asset winner → trigger MOF expansion |
| top 20% Monday | Tuesday repost queue |
| MOF warm threshold | Queue BOF sequence |

## Saturday report sections
1. Top 5 hooks by viral_score
2. Top 3 assets by conversion_score
3. Losers to archive
4. Funnel stage balance (TOF/MOF/BOF publish ratio)
5. Recommendations for next week

## Cron
Saturday 12 PM — `weekly_funnel_runner.py --day saturday`
