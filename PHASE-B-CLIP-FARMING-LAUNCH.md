# Phase B: Clip Farming System 🚀

**Start Date:** 2026-06-10
**Goal:** Automated clip production for 712 ventures
**Timeline:** 14+ hours (parallel-friendly)

---

## The 7-Layer Machine

```
VIDEO (30 min)
  ↓
Layer 1: Content Intake (YouTube, Drive)
  ↓
Layer 2: Research (Tavily - trending topics)
  ↓
Layer 3: Transcription (Whisper)
  ↓
Layer 4: Clip Detection ⭐ (Custom Claude agent)
  → Output: 12 best clips with scores
  ↓
Layer 5: Media Production (format, caption, brand)
  ↓
Layer 6: Distribution (Postiz - 6 platforms)
  ↓
Layer 7: Analytics (track performance)
  ↓
OUTPUT: 12 clips distributed + analytics
  ↓
FEEDBACK: "Healthcare performs 3x on LinkedIn"
```

---

## Layers at a Glance

| Layer | Purpose | MCPs | Status | Effort |
|-------|---------|------|--------|--------|
| 1 | Content Intake | YouTube, Drive | ⏳ | 1.5h |
| 2 | Research | Tavily, KWP | ✅ Ready | 1h |
| 3 | Transcription | Whisper | ⏳ | 1.5h |
| 4 | Clip Detection ⭐ | Custom Agent | ⏳ | 3h |
| 5 | Media Prod | Media, FFmpeg | ⏳ | 2h |
| 6 | Distribution | Postiz | ⏳ | 2h |
| 7 | Analytics | Postiz, KPI | ⏳ | 2h |

**Total:** 14 hours

---

## Layer 4: The Heart (Clip Detection)

This is the critical layer. It identifies:
- Emotional hooks ("moment I realized...")
- Contrarian takes ("everyone does X wrong")
- Frameworks ("step 1, 2, 3...")
- Quotes ("one sentence explains it all")

**Output:**
```json
{
  "timestamp": "00:12:34-00:12:45",
  "type": "emotional_hook",
  "text": "That was...",
  "viral_score": 9.2,
  "best_platform": "TikTok"
}
```

---

## Build Order

1. Layer 4 (Clip Detection) — 3h
2. Layer 3 (Transcription) — 1.5h
3. Layer 5 (Media) — 2h
4. Layer 6 (Distribution) — 2h
5. Layer 7 (Analytics) — 2h
6. Layers 1, 2 (parallel) — 2.5h

---

## Ready to Build?

**Starting:** Layer 4 (Clip Detection Agent)

This is where AI handles the hard part: finding viral moments in 30 minutes of footage.
