# Creator Workflow: Production Pipeline & Quality Gates

This document defines the standard operating procedures (SOPs) for the creation, editing, voice synthesis, and quality checks of Worldwidebro media assets.

---

## 1. Production Pipeline Flow

```text
SCRIPT ➔ AI Voice Synthesis ➔ Visual Asset Assembly ➔ Burned Captions ➔ Quality Check ➔ Publish
```

### Step 1: Voice Generation
- **Provider**: ElevenLabs or OpenAI TTS.
- **Voice Profile**: "Marcus" (Deep, authoritative, slightly gravelly) or "Sarah" (Clear, professional, rapid pace).
- **Settings**: Stability = 75%, Clarity/Artifacts = 85%, Style Exaggeration = 10%.
- **Output**: 24kHz Mono WAV file.

### Step 2: B-Roll & Visual Asset Gathering
- **Screen Captures**: Record terminal commands (`git log`, database queries, Cypher scripts) and dashboard metrics.
- **AI Art / Motion Graphic Elements**: ComfyUI rendering pipelines (GPT Image 2 + Stable Video Diffusion) or Runway Gen-2.
- **Asset Specs**: 1080x1920 (9:16 vertical), 30fps or 60fps, MP4/MOV format.

### Step 3: Editing & Assembly
- **Software**: Automated script renders (DaVinci Resolve Python scripting API) or lightweight mobile templates (CapCut).
- **Audio Levels**: Voice track peak at -3dB, background music loop (low-bass synth, ambient techno) set to -22dB.
- **Captions**: Positioned in the middle of the vertical frame (safe zone: Y=40% to 60%). Single-word or short-phrase layout.

---

## 2. Quality Assurance Gates

Before any video is marked "Approved" for posting, the publishing agent verifies:

1. **Title & Tags Check**: Focus keyword in first 3 words. 3-5 hyper-targeted hashtags (e.g. `#aiagents #saas #solopreneur`).
2. **Readability Check**: Do captions clash with TikTok's interface buttons (right-side icons and bottom text overlay)?
3. **Sound Sync**: Is the synthetic voice aligned with visual edits? No dead space longer than 0.3 seconds.
4. **Link Routing Validation**: Does the bio link match the specific CTA mentioned in the script?
5. **Regulatory Compliance (Audit)**: Verify script does not make unverified financial claims or medical advice (strictly "For Educational Purposes").
