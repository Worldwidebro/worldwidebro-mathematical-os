# Layer 4: Clip Detection Engine ✅

**Status:** Complete and ready to test
**Date:** 2026-06-10

---

## Built: Clip Detection Engine

### Core Function
- **File:** `layers/4-detection.js`
- **Function:** `detectClips(transcript, context)`
- **Purpose:** Identify 12 most viral moments in founder interview

### How It Works

1. Takes transcript text + venture context
2. Uses Claude 3.5 Sonnet to analyze
3. Detects 5 clip types: emotional_hook, framework, quote, contrarian, actionable
4. Scores on: emotional_impact (1-10), relevance (1-10), shareability (1-10)
5. Calculates final_score = average of 3
6. Recommends best platforms per clip
7. Returns JSON sorted by score (highest first)

### Output Example

```json
{
  "venture_id": "hrms-001",
  "venture_name": "PayrollMaster",
  "clips_count": 12,
  "clips": [
    {
      "clip_id": 1,
      "timestamp": "00:12:34-00:12:45",
      "duration": 11,
      "type": "emotional_hook",
      "text": "That was the moment I realized payroll was broken",
      "emotional_impact": 9,
      "relevance": 8,
      "shareability": 9,
      "final_score": 8.7,
      "best_platforms": ["TikTok", "Instagram"],
      "suggested_hook": "The moment everything changed"
    }
  ]
}
```

---

## Scoring Rules

- **Emotional:** High emotion (8-10), medium relevance, high shareability
- **Framework:** Low emotion, high relevance, high shareability
- **Quote:** Medium emotion, high relevance, very high shareability
- **Contrarian:** Medium emotion, high relevance, very high shareability
- **Actionable:** Low emotion, high relevance, medium shareability

---

## Platform Recommendations

- TikTok: Emotional hooks, contrarian takes
- Instagram: Personal stories, frameworks
- LinkedIn: Frameworks, thought leadership
- Twitter: Quotes, contrarian takes
- YouTube: Detailed advice, stories
- Facebook: Personal stories, emotional

---

## Files Created

- `layers/4-detection.js` — Core detection engine
- `test-layer-4.js` — Test harness with example transcript
- `package.json` — Dependencies (Anthropic SDK)

---

## Test Command

```bash
npm install
npm run test:layer4
```

---

## Next Layer Sequence

1. ✅ Layer 4 (Clip Detection) — COMPLETE
2. ⏳ Layer 3 (Transcription) — Whisper MCP
3. ⏳ Layer 5 (Media Production) — Format videos
4. ⏳ Layer 6 (Distribution) — Schedule on Postiz
5. ⏳ Layer 7 (Analytics) — Track performance
6. ⏳ Orchestrator — Coordinate all layers

---

## Ready to Test or Build Next?
