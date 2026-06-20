# Phase B: Complete Architecture

**Status:** Architecture design (before coding)
**Date:** 2026-06-10

---

## System Overview

```
VIDEO → INTAKE → RESEARCH → TRANSCRIPTION → DETECTION → PRODUCTION → DISTRIBUTION → ANALYTICS
  ↓        ↓        ↓           ↓             ↓            ↓              ↓           ↓
L1        L2       L3          L4           L5           L6            L7
```

---

## Layer 1: Content Intake
**Input:** YouTube/Drive link or local file
**Output:** MP4 file + metadata
**MCPs:** YouTube, Google Drive, Filesystem
**Depends on:** None

---

## Layer 2: Research
**Input:** Venture sector + name
**Output:** Trending topics + keywords (JSON)
**MCPs:** Tavily, Knowledge-Work-Plugins
**Depends on:** None (parallel to L1)

---

## Layer 3: Transcription
**Input:** MP4 file
**Output:** Transcript + timestamps (JSON)
**MCPs:** Whisper, WhisperX
**Depends on:** Layer 1

---

## Layer 4: Clip Detection ⭐ CORE
**Input:** Transcript + trends
**Output:** 12 best clips with scores (JSON)
**MCPs:** Custom Claude agent, Memory
**Depends on:** Layers 2, 3
**Logic:** Detect hooks, frameworks, quotes, contrarian takes

---

## Layer 5: Media Production
**Input:** Video + clip list
**Output:** Platform-specific videos (MP4 x6)
**MCPs:** Media, FFmpeg, Remotion
**Depends on:** Layers 1, 4
**Logic:** Extract segments, caption, format (TikTok 9:16, LinkedIn 16:9, etc)

---

## Layer 6: Distribution
**Input:** Formatted videos + venture strategy
**Output:** Scheduled posts (JSON)
**MCPs:** Postiz, YouTube
**Depends on:** Layer 5
**Logic:** Schedule by platform per venture

---

## Layer 7: Analytics
**Input:** Postiz metrics (daily)
**Output:** Dashboard + insights
**MCPs:** Postiz API, Custom KPI MCP
**Depends on:** Layer 6
**Logic:** Aggregate performance, store patterns

---

## Data Flow

```
L1 → L3 (video_path)
L2 → L4 (trends)
L3 → L4 (transcript)
L4 → L5 (clip_list)
L5 → L6 (videos)
L6 → L7 (scheduled_posts)
L7 → Memory (insights_feedback)
```

---

## File Structure

```
/clip-farming-system/
├── layers/
│   ├── 1-intake.js
│   ├── 2-research.js
│   ├── 3-transcription.js
│   ├── 4-detection.js
│   ├── 5-production.js
│   ├── 6-distribution.js
│   └── 7-analytics.js
├── orchestrator.js
├── config/
│   ├── venture-strategies.json
│   └── platform-formats.json
├── schemas/
│   ├── venture.json
│   ├── clip.json
│   └── metrics.json
└── tmp/
    ├── clips/
    └── output/
```

---

## Build Checklist

### Phase B-1: Architecture Complete ✅
- [x] Layer 1 spec
- [x] Layer 2 spec
- [x] Layer 3 spec
- [x] Layer 4 spec (core)
- [x] Layer 5 spec
- [x] Layer 6 spec
- [x] Layer 7 spec
- [x] Data flow mapped
- [x] Dependencies documented
- [x] File structure designed

### Phase B-2: Layer Implementation (NEXT)
- [ ] Layer 1: Content Intake (1.5h)
- [ ] Layer 3: Transcription (1.5h)
- [ ] Layer 4: Clip Detection (3h) ⭐
- [ ] Layer 5: Media Production (2h)
- [ ] Layer 6: Distribution (2h)
- [ ] Layer 7: Analytics (2h)
- [ ] Layer 2: Research (1h, parallel)

### Phase B-3: Integration
- [ ] Connect L1 → L3
- [ ] Connect L2 → L4
- [ ] Connect L3 → L4
- [ ] Connect L4 → L5
- [ ] Connect L5 → L6
- [ ] Connect L6 → L7
- [ ] Connect L7 → Memory

### Phase B-4: Testing
- [ ] Layer 1 unit test
- [ ] Layer 3 unit test
- [ ] Layer 4 unit test
- [ ] Layer 5 unit test
- [ ] Layer 6 unit test
- [ ] Layer 7 unit test
- [ ] End-to-end test (video → clips → distribution)

### Phase B-5: Deployment
- [ ] Package system
- [ ] Create startup script
- [ ] Document how to run
- [ ] Deploy to production

---

## Ready to Build All Layers?
