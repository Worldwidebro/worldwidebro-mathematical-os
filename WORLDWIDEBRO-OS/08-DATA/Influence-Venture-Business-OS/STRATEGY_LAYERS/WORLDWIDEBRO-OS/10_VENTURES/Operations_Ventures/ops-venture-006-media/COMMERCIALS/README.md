# Media Operations Hub

Central system for generating, testing, distributing, and measuring marketing assets across all 712 ventures.

## Quick Start

```bash
# Generate commercial for any venture
./generate.sh --venture angels-in-daylight --url https://angels-in-daylight.com --duration 30

# Sync to target repo
./push_to_venture.sh --repo ec-001-angels-in-daylight --venture angels-in-daylight
```

## Structure

- **00_STRATEGY** — Brand positioning, messaging, avatars, unique value propositions
- **01_AVATARS** — Customer profiles (primary, secondary, enterprise variants)
- **02_HOOKS** — Opening angles (pain, curiosity, authority, emotional, urgency)
- **03_SCRIPTS** — Video scripts organized by duration (15s, 30s, 60s, long-form)
- **04_STORYBOARDS** — Visual planning and shot lists
- **05_ASSETS** — Brand kit, logos, music, voiceovers, graphics, b-roll
- **06_PRODUCTION** — Filming plans, equipment, locations, talent, schedules
- **07_EDITING** — Project files, exports, thumbnails, captions
- **08_DISTRIBUTION** — Channel-specific exports (YouTube, TikTok, Instagram, etc.)
- **09_ANALYTICS** — Performance reports, A/B tests, conversion metrics, ROI tracking
- **10_WINNERS** — Top-performing ads, proven scripts, successful campaign templates

## Integration

- **Higgsfield**: Marketing Studio AI for video/image generation
- **GitHub**: Auto-syncs to venture repos via `push_to_venture.sh`
- **Supabase**: Logs campaign performance and venture metadata

## Ventures Using This System

- angels-in-daylight (clothing)
- [more to be added]
