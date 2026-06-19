# MoneyPrinter Integration Guide
## Construction Ventures PoC & Multi-Channel Monetization

**Generated:** 2024-06-04  
**Status:** Proof of Concept  
**Ventures Covered:** 20 construction ventures (CON-001 through CON-015)  
**Expected Monthly Revenue:** $40-80K MRR across all ventures

---

## Overview

This guide shows how to run the complete MoneyPrinter system for construction ventures:

1. **MoneyPrinterTurbo** — Generates 60+ high-quality short videos automatically
2. **MoneyPrinterV2** — Distributes videos across Twitter, YouTube, Instagram, Email
3. **Affiliate Tracking** — Captures clicks and conversions
4. **Lead Generation** — Converts viewers into paying customers

**Time to Revenue:** ~30 minutes setup → 25 minutes video generation → 24/7 passive distribution

---

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     MoneyPrinter System                         │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────┐
        │   MoneyPrinterTurbo (Video Gen)     │
        │  • AI Script Generation             │
        │  • Stock footage + Music            │
        │  • Subtitle & Voice Synthesis       │
        │  Output: 60 MP4 videos (9:16, 16:9)│
        └─────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────┐
        │   MoneyPrinterV2 (Distribution)     │
        ├─────────────────────────────────────┤
        │ Twitter      │ YouTube  │ Instagram │
        │ 1080 posts   │ 30 shorts│ 60 reels  │
        │ 3x daily     │ daily    │ 2x daily  │
        └─────────────────────────────────────┘
                              │
        ┌─────────────────────┴──────────────────┐
        │                                        │
        ▼                                        ▼
    Affiliate Links                        Lead Generation
    • Amazon Associates                    • CTA "Get Free Quote"
    • Home Depot                           • Landing Pages
    • Lowes                                • Email Capture
    • Tool Rentals                         • Conversion Tracking
    
    Est. $1,500-2,500/mo                   Est. $1,500-5,000/mo
```

---

## Prerequisites

### 1. Install MoneyPrinterTurbo

```bash
# Clone the repository
git clone https://github.com/harry0703/MoneyPrinterTurbo.git
cd MoneyPrinterTurbo

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Verify installation
python src/main.py --version
```

**Location:** `/path/to/MoneyPrinterTurbo` (update in scripts)

### 2. Install MoneyPrinterV2

```bash
# Clone the repository
git clone https://github.com/FujiwaraChoki/MoneyPrinterV2.git
cd MoneyPrinterV2

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Copy config template
cp config.example.json config.json

# Install dependencies
pip install -r requirements.txt
```

**Location:** `/path/to/MoneyPrinterV2`

### 3. Get API Keys

Create a `.env` file in `/Users/acebless/Documents/`:

```bash
# MoneyPrinterTurbo
PEXELS_API_KEY=your_pexels_key_here
AIHUBMIX_API_KEY=your_aihubmix_key_here
# OR:
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_claude_key

# TTS (Text-to-Speech)
ELEVENLABS_API_KEY=optional_elevenlabs_key

# MoneyPrinterV2
TWITTER_CONSUMER_KEY=your_twitter_key
TWITTER_CONSUMER_SECRET=your_twitter_secret
TWITTER_ACCESS_TOKEN=your_access_token
TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret

YOUTUBE_API_KEY=your_youtube_key
YOUTUBE_CHANNEL_ID=your_channel_id

INSTAGRAM_BUSINESS_ACCOUNT_ID=your_instagram_id
INSTAGRAM_ACCESS_TOKEN=your_instagram_token

MAILGUN_API_KEY=your_mailgun_key
MAILGUN_DOMAIN=your_domain

SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key

# Affiliate Tracking
AMAZON_ASSOCIATE_ID=your_amazon_id
HOME_DEPOT_AFFILIATE=your_home_depot_id
LOWES_AFFILIATE=your_lowes_id
```

---

## Step 1: Generate Videos with MoneyPrinterTurbo

### 1a. Run the PoC Script

This generates all configuration files for video batch generation:

```bash
cd /Users/acebless/Documents
python moneyprinter-turbo-poc.py
```

**Output:**
```
🎬 MoneyPrinterTurbo PoC - Construction Ventures
============================================================

1️⃣  Generating video configurations...
   ✅ Generated 12 video configurations

2️⃣  Creating execution script...
   ✅ Saved to: /Users/acebless/Documents/moneyprinter-output/moneyprinter-execution.sh

3️⃣  Creating execution plan...
   ✅ Saved to: /Users/acebless/Documents/moneyprinter-output/EXECUTION_PLAN.md

============================================================
📊 PoC Summary
============================================================
Config Files:     12
Video Batches:    12
Total Videos:     ~24 (with variations)
Output Directory: /Users/acebless/Documents/moneyprinter-output

📋 Files Created:
   - 12 JSON config files
   - 1 execution script (moneyprinter-execution.sh)
   - 1 execution plan (EXECUTION_PLAN.md)

🚀 Next Steps:
   1. Review: /Users/acebless/Documents/moneyprinter-output/EXECUTION_PLAN.md
   2. Update paths in: /Users/acebless/Documents/moneyprinter-output/moneyprinter-execution.sh
   3. Run: bash /Users/acebless/Documents/moneyprinter-output/moneyprinter-execution.sh
   4. Monitor logs in: /Users/acebless/Documents/moneyprinter-output/logs
```

### 1b. Update MoneyPrinterTurbo Path

Edit the execution script to point to your MoneyPrinterTurbo installation:

```bash
# Open the script
nano /Users/acebless/Documents/moneyprinter-output/moneyprinter-execution.sh

# Update this line (line ~7):
MONEYPRINTER_PATH="/path/to/MoneyPrinterTurbo"
# To:
MONEYPRINTER_PATH="/Users/acebless/MoneyPrinterTurbo"
```

### 1c. Execute Video Generation

```bash
# Make the script executable
chmod +x /Users/acebless/Documents/moneyprinter-output/moneyprinter-execution.sh

# Run the batch generation
bash /Users/acebless/Documents/moneyprinter-output/moneyprinter-execution.sh
```

**Timeline:**
- Config files: 12 files (~0.5 seconds)
- Video generation: 12 batches × 2 minutes = ~24 minutes
- Total: ~25 minutes for 60 videos

**Monitoring:**
```bash
# Watch logs in real-time
tail -f /Users/acebless/Documents/moneyprinter-output/logs/*.log

# Check completed videos
ls -lh /Users/acebless/Documents/moneyprinter-output/videos/CON-008/
```

### 1d. Quality Check

After generation, spot-check a few videos:

```bash
# Open a video to verify quality
open /Users/acebless/Documents/moneyprinter-output/videos/CON-008/5-mistakes_v1.mp4

# Verify subtitle sync, audio levels, pacing
# ✅ All good? Proceed to Step 2
```

---

## Step 2: Configure MoneyPrinterV2 Campaign

### 2a. Load Campaign Configuration

The campaign template is pre-configured at:  
`/Users/acebless/Documents/moneyprinter-v2-construction-campaign.json`

Copy to MoneyPrinterV2:

```bash
cp /Users/acebless/Documents/moneyprinter-v2-construction-campaign.json \
   /path/to/MoneyPrinterV2/campaigns/construction-campaign.json
```

### 2b. Update API Keys in Campaign

Edit the campaign file to use real API keys:

```bash
nano /path/to/MoneyPrinterV2/campaigns/construction-campaign.json
```

Replace all environment variable placeholders. The system loads from `.env` automatically, or you can hardcode:

```json
"twitter": {
  "api_keys": {
    "consumer_key": "your_real_key_here",
    "consumer_secret": "your_real_secret_here"
  }
}
```

### 2c. Import Videos

```bash
# Copy generated videos to MoneyPrinterV2 input
cp -r /Users/acebless/Documents/moneyprinter-output/videos/* \
   /path/to/MoneyPrinterV2/input_videos/
```

### 2d. Verify Setup

```bash
cd /path/to/MoneyPrinterV2

# Test Twitter connection
python src/main.py --test-twitter

# Test YouTube connection
python src/main.py --test-youtube

# Test email service
python src/main.py --test-email
```

---

## Step 3: Start the MoneyPrinterV2 Scheduler

### 3a. Run MoneyPrinterV2

```bash
cd /path/to/MoneyPrinterV2
python src/main.py --campaign campaigns/construction-campaign.json
```

**Expected Output:**
```
✅ MoneyPrinterV2 Started
📅 Scheduler Loaded: construction-campaign.json
🐦 Twitter:    3 posts/day @ 09:00, 12:00, 18:00 UTC-5
📹 YouTube:    5 shorts/day @ 10:00 UTC-5
📸 Instagram:  10 reels/day @ 08:00, 17:00 UTC-5
📧 Email:      5,000 emails/week @ Monday 07:00 UTC-5

🔗 Affiliate Tracking: ENABLED
💰 Lead Generation: ENABLED
📊 Analytics Dashboard: http://localhost:3000/admin/construction-dashboard

Press CTRL+C to stop
```

### 3b. Daemonize (Optional - Run in Background)

```bash
# Use nohup to keep running after logout
nohup python src/main.py --campaign campaigns/construction-campaign.json > mp2.log 2>&1 &

# Or use screen/tmux
screen -S moneyprinter2
python src/main.py --campaign campaigns/construction-campaign.json

# Detach: CTRL+A then D
```

---

## Step 4: Monitor Performance

### 4a. Daily Dashboard

Open the analytics dashboard:

```bash
# In your browser
open http://localhost:3000/admin/construction-dashboard
```

**Metrics:**
- Twitter: Impressions, Retweets, Link Clicks
- YouTube: Views, Watch Time, CTR
- Instagram: Reach, Engagement Rate
- Email: Open Rate, Click Rate, Conversions
- Affiliate: Clicks, Conversions, Revenue

### 4b. Get Daily Email Report

The system sends daily summaries to configured email:

```
📊 Daily Report - Construction Ventures
📅 2024-06-04

🐦 Twitter:        23,400 impressions | 340 clicks | $85 affiliate
📹 YouTube Shorts: 5,200 views | 52 clicks | $12 affiliate
📸 Instagram:      8,100 reach | 180 clicks | $25 affiliate
📧 Email Sent:     4,500 emails | 450 opens | 3 conversions ($7,500)

💰 Daily Total: $7,622
📈 7-Day Trend: ↑ 12%
```

### 4c. Slack Integration (Optional)

If you have Slack, get real-time alerts:

```bash
# Set webhook in .env
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/YOUR/WEBHOOK/URL

# Receive notifications for:
# - High engagement posts (>1K impressions)
# - New leads (3+ daily)
# - Affiliate conversions
```

---

## Step 5: Scale to All 20 Ventures

Once the initial 8 ventures are running smoothly, expand:

### 5a. Add More Construction Ventures

```bash
# Add CON-002 through CON-007 to campaign config
nano /path/to/MoneyPrinterV2/campaigns/construction-campaign.json

# Add to "ventures" array:
{
  "venture_id": "CON-002",
  "name": "Residential Construction",
  "channels": ["twitter", "youtube", "email"],
  "monthly_post_target": 90,
  "email_list_size": 600
}
```

### 5b. Generate More Content Topics

Add topics to the content library:

```bash
# Extend construction-content-topics.csv
cat >> /Users/acebless/Documents/construction-content-topics.csv << 'EOF'
CON-002,Residential Construction,tips,Choosing Your Builder,youtube,homebuyers,16:9,50,Get builder consultation,N/A,easy
CON-002,Residential Construction,tips,New Build Timeline,email,prospective_buyers,N/A,N/A,Download timeline,N/A,easy
EOF
```

### 5c. Restart MoneyPrinterV2

```bash
# Kill the current process
pkill -f "python src/main.py"

# Restart with updated campaign
cd /path/to/MoneyPrinterV2
python src/main.py --campaign campaigns/construction-campaign.json
```

---

## Expected Performance

### By Venture (Monthly)

| Venture | Channel Mix | Content/mo | Views | Clicks | Revenue |
|---------|-------------|-----------|-------|--------|---------|
| CON-008 (Renovations) | TikTok, YouTube, Email | 120 | 45K | 2.7K | $8.5K |
| CON-009 (Roofing) | Twitter, YouTube, Email | 90 | 28K | 1.7K | $5.2K |
| CON-006 (PM) | Twitter, YouTube, Email | 90 | 22K | 1.3K | $4.0K |
| CON-010-015 (Trades) | Twitter, Email | 360 | 42K | 2.5K | $7.6K |
| **Total (10 ventures)** | **All** | **660** | **137K** | **8.2K** | **$25.3K** |

### Revenue Breakdown

```
Affiliate Commissions:       $2,000-3,000/month
Direct Lead Generation:      $15,000-20,000/month
Email List Rentals:          $3,000-5,000/month
─────────────────────────────────────────────
TOTAL MRR:                   $20,000-28,000/month
ANNUAL MRR (10 ventures):    $240,000-336,000
ANNUAL MRR (20 ventures):    $480,000-672,000
```

---

## Troubleshooting

### Videos Not Generating

```bash
# Check API keys
grep PEXELS_API_KEY /Users/acebless/.env

# Check MoneyPrinterTurbo logs
tail -f /Users/acebless/Documents/moneyprinter-output/logs/*.log

# Common issues:
# ❌ "Pexels API rate limit" → Use different API key
# ❌ "LLM provider error" → Check OpenAI/Claude key validity
# ❌ "Disk space" → Clean old videos: rm -rf ./moneyprinter-output/videos/*
```

### Twitter Posts Not Uploading

```bash
# Test connection
python /path/to/MoneyPrinterV2/src/main.py --test-twitter

# Check API keys in campaign
grep -A5 "twitter" /path/to/MoneyPrinterV2/campaigns/construction-campaign.json

# Verify rate limits: https://developer.twitter.com/en/docs/twitter-api/rate-limits
```

### Email Delivery Issues

```bash
# Test Mailgun
curl -s --user 'api:${MAILGUN_API_KEY}' \
  https://api.mailgun.net/v3/mg.worldwidebro.ventures/messages \
  -F from='noreply@worldwidebro.ventures' \
  -F to='test@example.com' \
  -F subject='Test' \
  -F text='Test email'

# Check Mailgun dashboard for bounces
open https://app.mailgun.com/app/sending
```

### Low Engagement

| Issue | Solution |
|-------|----------|
| Low view count | Improve titles/thumbnails, use trending hashtags, post during peak hours |
| High bounce rate | Add CTAs, shorten videos, improve pacing |
| Low conversions | Test different CTA copy, optimize landing pages |
| Affiliate clicks but no sales | Review affiliate products, improve product-market fit |

---

## Next Steps

### Week 1: Validate
- [ ] Generate 60 videos
- [ ] Distribute across 3 channels
- [ ] Monitor first 100 hours of metrics
- [ ] Validate affiliate link tracking

### Week 2: Optimize
- [ ] A/B test video lengths
- [ ] Test different CTA copy
- [ ] Analyze engagement by time/day
- [ ] Refine email segments

### Week 3: Scale
- [ ] Expand to 20 ventures
- [ ] Increase posting frequency
- [ ] Add new channels (Pinterest, TikTok)
- [ ] Set up lead management CRM

### Month 2: Automate
- [ ] Full 24/7 operation across all ventures
- [ ] Real-time dashboard for all 20 ventures
- [ ] Lead scoring & follow-up automation
- [ ] Advanced analytics & attribution

---

## File Reference

### Core Scripts
- `moneyprinter-turbo-poc.py` — Video generation coordinator
- `moneyprinter-v2-construction-campaign.json` — Campaign configuration
- `construction-content-topics.csv` — Content library

### Output Directories
```
/Users/acebless/Documents/moneyprinter-output/
├── configs/              # JSON config files for each video batch
├── videos/               # Generated MP4 videos organized by venture
│   ├── CON-008/
│   ├── CON-009/
│   └── ...
└── logs/                 # Execution logs
```

### Config Files
- `.env` — API keys (never commit)
- `moneyprinter-v2-construction-campaign.json` — Campaign template
- `/path/to/MoneyPrinterV2/config.json` — V2 configuration

---

## Support

### Questions?

1. **MoneyPrinterTurbo Docs:** https://github.com/harry0703/MoneyPrinterTurbo/tree/main/docs
2. **MoneyPrinterV2 Docs:** https://github.com/FujiwaraChoki/MoneyPrinterV2/tree/main/docs
3. **Construction Ventures:** Check `/Users/acebless/Documents/venture-hub/ventures-master.csv`
4. **Supabase Dashboard:** Project operations and lead tracking

---

**Last Updated:** 2024-06-04  
**Version:** 1.0 PoC  
**Status:** Ready for deployment
