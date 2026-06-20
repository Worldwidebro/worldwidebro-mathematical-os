# Hook Agent

Generate **20 hooks**, rank by predicted viral fit, return **top 5–10** for TOF.

## Inputs
- `audience.md` pain + trigger moments
- `brand_identity.md` tone
- Optional: last week's winners from `gf_content_hooks` where status=winner

## Process
1. Generate 20 hooks (contrarian, pain, stat, POV, humor)
2. Score each 1–10 on: curiosity, specificity, shareability, brand fit
3. Output top N with scores

## Output format
```markdown
| Rank | Hook | Score | Format |
|------|------|-------|--------|
| 1 | ... | 9.2 | 15s reel |
```

## Rules
- No product dump in hook line
- First 8 words must stand alone
- Match tone from brand agent

## Schedule
- **Monday 9 AM** — primary batch
- **Sunday 6 PM** — next-week prefetch (20 hooks)
