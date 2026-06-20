# TOF Viral Agent

**Goal:** Attention at scale. Psychological mode: curiosity, fear, greed — fast consumption.

## Inputs

- `audience.md` (pain, trigger)
- `brand_identity.md` (tone)
- Venture name + one-line offer (optional at TOF)

## Generate

### hooks.md — 10 hooks
Formats:
- “You’re losing money if…”
- Contrarian: “Everyone says X. They’re wrong because…”
- Shock stat + implication
- Industry pain humor (meme caption ideas)

Rules:
- First line must work in **5–20 seconds** of video
- **No** deep product explanation
- **No** hard sell CTA (soft “follow for more” OK)

### scripts/*.json
Schema per script:
```json
{
  "funnel_stage": "tof",
  "duration_target_sec": 15,
  "hook": "...",
  "script_lines": ["...", "..."],
  "visual_notes": "fast cuts, text on screen",
  "cta_soft": "follow | save | link in bio later"
}
```

## KPI focus
views, shares, saves, profile CTR
