# 🎬 Clip Farming System — Phase B Checklist

**Status:** Phase A (Tier 1 Business MCPs) — 95% Complete
**Date Started:** 2026-06-10
**Goal:** Build complete clip farming + distribution system for 712 ventures

---

## Phase A: Tier 1 Business MCPs ✅ (ALMOST DONE)

### Connected MCPs
- ✅ **ClickUp** — Connected (CRM, task management, pipeline)
- ✅ **HubSpot** — Connected (sales pipeline, contacts, deals)
- ✅ **Tavily** — Connected (research, web search)
- ✅ **Buffer** — Connected (social media scheduling)
- ✅ **Notion** — Connected (knowledge capture, playbooks)
- ✅ **GitHub** — Connected (repo management)
- ✅ **Supabase** — Connected (venture data)
- ✅ **Slack** — Connected (notifications, updates)

### Still Needed
- ⏳ **Beehiiv** API Key → https://www.beehiiv.com/settings/api
  - Purpose: Newsletter distribution
  - Once added: Complete Phase A ✅

---

## Phase B: Clip Farming Stack (NEXT)

### Layer 1: Content Intake ⏳
- [ ] YouTube MCP — pull founder videos, interviews
- [ ] Google Drive MCP — extract pitch decks, case studies
- [ ] Filesystem MCP — load existing content library
- [ ] Knowledge-Work-Plugins Document MCP — process transcripts

**Status:** Ready to install once Beehiiv key added

---

### Layer 2: Research ⏳
- [ ] Tavily MCP ✅ (already connected)
- [ ] Research MCP — deep topic analysis
- [ ] Knowledge-Work-Plugins Research plugin — AI-powered insights

**Status:** Tavily ready; others need setup

---

### Layer 3: Transcription ⏳
- [ ] Whisper MCP — convert video/audio to text
- [ ] WhisperX MCP — speaker diarization, timestamps

**Status:** Not yet installed

---

### Layer 4: Clip Detection ⭐ (CRITICAL)
- [ ] Custom Claude Agent — detects hooks, frameworks, quotes
  - Looks for: emotional moments, contrarian takes, step-by-step guides
  - Outputs: clip timestamp + viral score (1-10)
- [ ] Knowledge-Work-Plugins Memory plugin — stores what worked

**Status:** Need to build custom agent

---

### Layer 5: Media Production ⏳
- [ ] Media MCP — auto-captions, adds branding
- [ ] FFmpeg MCP — format for TikTok, Instagram, YouTube
- [ ] Remotion MCP — motion graphics generation

**Status:** Not yet installed

---

### Layer 6: Distribution ⭐ (POSTIZ INTEGRATION)
- [ ] Postiz API integration — multi-platform scheduling
  - Replaces Buffer for enterprise use
  - Platforms: Twitter, LinkedIn, TikTok, Instagram, Facebook, YouTube
- [ ] Per-venture distribution strategy
  - HRMS: LinkedIn, Twitter, YouTube
  - AI Agency: TikTok, Instagram, Twitter
  - SaaS: LinkedIn, Beehiiv, YouTube

**Status:** Need Postiz MCP wrapper

---

### Layer 7: Analytics ⏳
- [ ] Postiz analytics API — per-platform metrics
- [ ] Knowledge-Work-Plugins Analytics plugin — aggregated insights
- [ ] Custom KPI MCP — venture-level dashboard
  - Tracks: views, engagement, followers gained, leads from content

**Status:** Need to build custom KPI MCP

---

## Dependency Chain

```
Phase A ✅
  ↓
Get Beehiiv key (5 min)
  ↓
Phase B Layer 1 (Content Intake) — 2 hours
  ↓
Phase B Layer 2 (Research) — 1 hour
  ↓
Phase B Layer 3 (Transcription) — 1.5 hours
  ↓
Phase B Layer 4 (Clip Detection) ⭐ — 3 hours [CRITICAL]
  ↓
Phase B Layer 5 (Media Production) — 2 hours
  ↓
Phase B Layer 6 (Distribution via Postiz) ⭐ — 2 hours
  ↓
Phase B Layer 7 (Analytics) — 2 hours
  ↓
🚀 LIVE: Clip farming for 712 ventures
```

**Total Phase B Time:** ~14 hours (non-blocking)

---

## Expected Capabilities (When Complete)

### For Each Venture

**Input:**
```
Long-form founder interview (YouTube video, 30 minutes)
```

**Process:**
1. Transcribe video → get full text
2. Detect best clips → identify 12 high-value moments
3. Generate clip videos → auto-caption, format, brand
4. Distribute → schedule across 6 platforms
5. Track → measure performance per platform

**Output:**
```
12 formatted clips
↓
Twitter: 3 clips (Tuesday, Thursday, Friday)
LinkedIn: 3 clips (with founder quote)
TikTok: 2 clips (trending audio)
Instagram: 2 clips (Reels)
YouTube: 1 short (vertical)
Beehiiv: 1 clip (in weekly newsletter)

+ Analytics dashboard showing:
  - Views by platform
  - Engagement by clip
  - Followers gained
  - Leads generated
```

---

## Venture Studio ROI

**Without Clip Farming:**
- Each venture creates maybe 1-2 pieces of content per month
- Manual publishing to 1-2 platforms
- No learning (what works, what doesn't)

**With Clip Farming:**
- Each venture produces 12+ clips per month (from 1 interview)
- Automated distribution to 6+ platforms
- System learns: "Healthcare ventures respond to compliance hooks"
- Compounds over time: "This founder's clips get 3x engagement on LinkedIn"

**Expected Result:**
- 3-5x more content reach
- 2-3x more leads per venture
- Venture studio becomes content juggernaut

---

## Immediate Next Step

**Get Beehiiv API key:**
https://www.beehiiv.com/settings/api

Once you provide it, we:
1. Add to `.env`
2. Install Beehiiv MCP
3. Complete Phase A ✅
4. Start Phase B immediately 🚀
