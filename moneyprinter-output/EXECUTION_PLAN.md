---
name: moneyprinter-output/EXECUTION_PLAN
title: MoneyPrinterTurbo - Construction Ventures PoC
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# MoneyPrinterTurbo - Construction Ventures PoC
## Execution Plan

Generated: 2026-06-05T11:55:26.957370

### Overview
Generate 60+ high-quality short videos across 8 construction ventures using MoneyPrinterTurbo.

### Ventures Targeted
1. **CON-008**: Home Renovation Services (4 batches, 7 videos total)
2. **CON-009**: Roofing Company (2 batches, 5 videos total)
3. **CON-010**: Plumbing Services (1 batch, 2 videos total)
4. **CON-011**: Electrical Services (1 batch, 2 videos total)
5. **CON-012**: HVAC Services (1 batch, 2 videos total)
Plus 3-5 more trades as demand dictates

### Output Metrics
- **Total Videos**: 60 variations
- **Formats**: Mix of 9:16 (vertical TikTok/Instagram) and 16:9 (YouTube Shorts)
- **Duration**: 45-60 seconds each
- **Languages**: English (expandable to Chinese, Spanish, etc.)
- **Total Video Content**: ~50 minutes of polished footage

### Video Topics by Venture

**CON-008: Home Renovation Services**
- 5 Common Renovation Mistakes
- Budget Kitchen Under $5000
- Modern Bathroom Ideas
- Living Room Transformation
- Bedroom Renovation Trends

**CON-009: Roofing Company**
- Signs Your Roof Needs Replacement
- Metal vs Asphalt Shingles
- Roof Maintenance 101
- Energy-Efficient Roofing
- Storm Damage Prevention

**CON-010: Plumbing Services**
- DIY Plumbing Fixes
- When to Call a Plumber
- Common Plumbing Myths
- Water Conservation Tips

**CON-011: Electrical Services**
- Home Electrical Safety
- Outlet and Switch Upgrades
- Circuit Breaker Guide
- Smart Home Electrical

**CON-012: HVAC Services**
- HVAC Maintenance Schedule
- Energy Efficient Cooling
- Winter Furnace Prep
- Smart Thermostat Benefits

### Technical Setup

1. **Prerequisites**:
   - MoneyPrinterTurbo installed at `/path/to/MoneyPrinterTurbo`
   - Python 3.10+
   - API keys configured:
     - Pexels API (free stock video)
     - LLM provider (OpenAI/Claude/AIHubMix)
     - TTS service (Google/Azure/ElevenLabs)

2. **Configuration Files**:
   - Located in: `./moneyprinter-output/configs/`
   - 15 JSON config files (one per batch)
   - Each specifies: script prompt, video format, voice, music, subtitles

3. **Execution**:
   \`\`\`bash
   # Execute all batches
   bash moneyprinter-execution.sh

   # Or run individual video
   cd /path/to/MoneyPrinterTurbo
   python src/main.py --config configs/CON-008_5-mistakes.json
   \`\`\`

### Expected Timeline

**Assumptions**:
- 3 concurrent videos (batch_size=3)
- 2 minutes per video (includes LLM + TTS + video assembly)
- API rate limits respected

| Phase | Duration | Output |
|-------|----------|--------|
| Config Generation | <1 min | 15 JSON files |
| Video Batch 1-5 | 10 min | 15 videos (renovation + roofing) |
| Video Batch 6-10 | 10 min | 15 videos (trades) |
| Review & QA | 5 min | Manual spot check |
| **Total** | **~25 minutes** | **60 videos ready** |

### Integration with MoneyPrinterV2

After videos are generated:
1. Videos automatically copied to MoneyPrinterV2 input directory
2. V2 distributes across YouTube Shorts, TikTok, Instagram
3. Affiliate links embedded in video descriptions
4. Tracking enabled for conversions and revenue

### Output Structure

\`\`\`
moneyprinter-output/
├── configs/
│   ├── CON-008_5-mistakes_20240604_120000.json
│   ├── CON-008_kitchen-budget_20240604_120000.json
│   ├── CON-009_roof-signs_20240604_120000.json
│   └── ... (15 total)
├── videos/
│   ├── CON-008/
│   │   ├── 5-mistakes_v1.mp4
│   │   ├── 5-mistakes_v2.mp4
│   │   ├── 5-mistakes_v3.mp4
│   │   └── ...
│   ├── CON-009/
│   ├── CON-010/
│   └── ... (organized by venture)
└── logs/
    ├── CON-008_5-mistakes_20240604_120000.log
    └── ... (execution logs)
\`\`\`

### Quality Gates

Before publishing to MoneyPrinterV2:
- [ ] All videos render without errors
- [ ] Subtitles sync with voiceover
- [ ] Background music levels acceptable
- [ ] Video bitrate suitable for platforms (TikTok, YouTube, Instagram)
- [ ] Venture branding/CTAs clear

### Revenue Model

Each 60-video batch creates multiple revenue streams:

1. **YouTube Shorts**: 60 shorts × 500 views avg = 30K views → AdSense
2. **TikTok/Instagram**: 60 shorts × 1K views avg = 60K views → Creator Fund + Affiliate
3. **Direct Leads**: CTA "Get free estimate" → 5% conversion = 3 leads × $2,500 = $7,500
4. **Affiliate Revenue**: Product recommendations in videos → $2-5 per viewer click

**Conservative Monthly**: $3-5K from this venture alone

### Next Steps

1. Verify MoneyPrinterTurbo path and API keys
2. Run: `python moneyprinter-turbo-poc.py`
3. Execute generated shell script
4. Wait for videos to complete
5. Review output quality
6. Proceed to MoneyPrinterV2 distribution
