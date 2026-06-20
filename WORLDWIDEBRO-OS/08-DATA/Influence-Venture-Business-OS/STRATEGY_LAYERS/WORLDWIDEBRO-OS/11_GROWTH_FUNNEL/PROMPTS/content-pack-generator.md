# Content Pack Generator

One-shot prompt to produce a **full funnel content pack** for a venture.

## System

You are a growth operator. Given venture context, produce TOF, MOF, and BOF assets that feel like one brand.

## User message template

```
Venture: {{name}}
Sector: {{sector}}
One-liner: {{tagline}}
Primary ICP: {{icp}}
Main pain: {{pain}}
Desired outcome: {{outcome}}
Trigger moments: {{triggers}}
Tone: {{tone}}
Primary CTA: {{cta}}
Proof available: {{proof_or_none}}

Deliver:
1. audience.md (abbreviated if already filled)
2. 5 TOF hooks + 1 TOF 15s script
3. 1 MOF demo outline + 1 MOF 45s script
4. 1 BOF offer block + 1 BOF 30s script
5. landing_page.spec.md hero + 3 sections
6. channel_copy.json for YouTube Shorts, Instagram Reels, LinkedIn
```

## Output files

Write to venture funnel folder:
- `01_TOF/hooks.md`
- `01_TOF/scripts/tof-01.json`
- `02_MOF/demos.md`
- `02_MOF/scripts/mof-01.json`
- `03_BOF/offers.md`
- `03_BOF/scripts/bof-01.json`
- `publish/landing_page.spec.md`
- `publish/channel_copy.json`

## Integration

After generation, run:
```bash
python3 generate_funnel_content.py --venture-id ID --render tof
bash run_venture_video_pipeline.sh ID single
```
