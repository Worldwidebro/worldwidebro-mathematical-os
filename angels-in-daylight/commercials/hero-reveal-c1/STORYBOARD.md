---
references:
  - [[VENTURE-MASTER]]
  - [[LOOP-FRAMEWORK]]
  - [[ORB-MASTER-CONNECTOR-2026-06-11]]
---

# Angels in Daylight — Hero Reveal (Concept c1)

**Status: NOT READY TO PUBLISH.** One scene is a visible placeholder. See "Before you publish" below.

- Concept: "The label doesn't say sustainable. It says exactly what's in it."
- Platform: TikTok (1080x1920, 9:16)
- Duration: 13.0s
- Pipeline: OpenMontage `cinematic` (render_runtime: hyperframes, composition_mode: templated)
- Rendered: 2026-07-04
- Final file: `final.mp4`

## Why this concept

Real research (4 web searches, cited in `artifacts/research_brief.json`) found that ~60% of fashion sustainability claims are unsubstantiated, and 73% of Gen Z buyers have abandoned a purchase after spotting a poor environmental record. The brand kit's original generic copy ("Beautiful clothing that doesn't cost the earth") risked reading as greenwashing to its own target audience. This concept counters that directly: it promises specificity instead of a vague sustainability claim.

## Storyboard

| Scene | Time | Frame | Description |
|---|---|---|---|
| s0 | 0.0–1.3s | `frames/scene-1.png` | Brand ID card, pre-animation frame (tween starts at 0.1s) |
| s1 | 1.3–4.3s | `frames/scene-2.png` | Hero product reveal — real photo, red zip hoodie, full wings/wordmark logo |
| s2 | 4.3–5.5s | `frames/scene-3.png` | "The label doesn't say sustainable." |
| s3 | 5.5–6.8s | `frames/scene-4.png` | "It says exactly what's in it." |
| s4 | 6.8–9.3s | `frames/scene-5.png` | Second real product photo — vintage wordmark tee |
| s5 | 9.3–11.0s | `frames/scene-6.png` | **PLACEHOLDER — see below** |
| s6 | 11.0–13.0s | `frames/scene-7.png` | CTA — "Shop the collection — link in bio" |

## Before you publish

Scene s5 currently reads: *"[CONFIRM BEFORE PUBLISHING: one verified, specific material or production fact]"*

This is intentional, not a bug — I don't have verified data on Angels in Daylight's actual material composition, sourcing, or production practice, and inventing one would recreate the exact greenwashing risk this concept exists to counter. Replace this line with a real, verifiable fact (fabric %, certification, factory practice, etc.), then re-run the OpenMontage `cinematic` pipeline compose stage to re-render — same pipeline, one text change, few minutes.

## Also not done yet

- No background music (no `music_library/` track configured, deferred for v1)
- No automated posting set up (see venture-level notes on Mixpost/Zapier/postiz-app)

## Full audit trail

All source artifacts (research brief, proposal with 3 concept options, script, scene plan, asset manifest, edit decisions, render report, final review) are in `artifacts/`. Original OpenMontage project workspace (regenerable, gitignored there): `OpenMontage/projects/angels-in-daylight-hero-reveal/`.
