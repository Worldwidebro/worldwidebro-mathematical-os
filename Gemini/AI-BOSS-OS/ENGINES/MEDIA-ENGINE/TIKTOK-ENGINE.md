# TikTok Engine: Media Acquisition Architecture

This document defines the technical architecture, agents, and feedback loops for the **TikTok Engine** (⭐). It is designed to act as an automated attention sensor feeding demand data and customer flows back to AI Boss Holdings.

---

## 1. Engine Architecture

The TikTok Engine operates as a closed-loop system:

```text
                MARKET INTELLIGENCE (Sensing)
                       |
                       ↓
              Trend Discovery Engine (Filtering)
                       |
                       ↓
              Content Strategy Engine (Mapping)
                       |
                       ↓
              Production Pipeline (Generating)
                       |
                       ↓
                 TikTok Publishing (Distributing)
                       |
                       ↓
               Analytics + Feedback (Measuring)
                       |
                       ↓
              Company Brain Learning (Adapting)
```

---

## 2. Phase-by-Phase Breakdown

### Phase 1: Market Intelligence & Trend Discovery
- **Inputs**: Google Trends, TikTok Trends, Reddit Communities, YouTube Comments, Competitor Ad Libraries, customer questions, and private database search indices.
- **Process**: The `Trend Hunter Agent` scans inputs to extract high-density themes, competitor topics, and audience pain points.
- **Output**: `CONTENT-IDEAS.md` (e.g. Trend: AI Agents ➔ Audience: Entrepreneurs ➔ Pain: Lack of OS/automation ➔ Concept: "Building a company with 1,000 AI employees").

### Phase 2: Content Strategy
- **Process**: Match trending concepts against the 9 Worldwidebro pillars (Entrepreneurship, AI, Wealth, Technology, etc.) to ensure brand alignment.
- **Rules**: Prevent style-drift. Reject content ideas that do not integrate with our product discovery matrix or affiliate databases.

### Phase 3: Idea Generation (Specialized AI Agents)
- **Agent Roles**: The `Script Agent` takes raw input concepts (e.g., "Business formation system") and outputs 50 Hooks, 10 Script variations, 5 video formats, 3 thumbnails/title templates, and multiple CTA options.

### Phase 4: Script Pipeline Structure
Every short-form video follows a strict time-block layout optimized for the TikTok algorithm:
1. **HOOK (0-3s)**: High-impact pattern interrupt (e.g., *"Most billion-dollar companies don't fail because of ideas."*)
2. **PROBLEM (3-10s)**: Establish the emotional pain or operational bottleneck (*"They fail because they lack operating systems."*)
3. **INSIGHT (10-40s)**: Deliver the resolution or high-value demonstration (*"Here is how AI Boss OS solves that."*)
4. **PROOF (40-50s)**: Show real screen recordings, terminal outputs, dashboard stats, or graph database nodes.
5. **CTA (50-60s)**: Direct action to profile link or lead capture (*"Follow the build."* / *"Grab the free setup."*)

### Phase 5: Production Pipeline
Scripts route to the automation pipeline:
- **Audio Generation**: Voice synthesis using ElevenLabs, OpenAI Voice, or Coqui TTS.
- **Visual Assets**: ComfyUI workflows, Stable Video Diffusion, Pika, or Runway for customized B-roll.
- **Editing & Captions**: Automated CapCut template integration or ffmpeg script processing to burn dynamic word-by-word styled captions.
- **Quality Check**: Lint script checks against advertising regulations (ad compliance audit).

### Phase 6: Daily Publishing Workflow
- **09:00**: Automated Trend Scan & Competitive Analysis.
- **10:00**: Agent Script Generation & Hook selection.
- **12:00**: Dynamic video rendering & asset packaging.
- **15:00**: Human-in-the-loop review via dashboard.
- **17:00**: Automate upload via TikTok API / Content Scheduler.
- **24 Hours Later**: Run retrieval of watch time, comments, and conversion data to feed back to the `Company Brain`.

### Phase 7: Analytics Brain
We measure:
- **Hook Rate (3s View Ratio)**: Measures stop-scroll power.
- **Retention Curve**: Indicates content quality and dropout spots.
- **Engagement Rate**: Comments, shares, saves, and likes.
- **Conversion Rate (Click-through to Signup/Sale)**: The North Star commercial metric.

### Phase 8: Feedback Loop & Company Brain Learning
Signals from high-performing videos trigger automatic product validation alerts. If a video on "AI Employees" achieves >2M views and high save rates:
1. The **Venture Factory** triggers a capability search in Neo4j.
2. A new Notion template or prompt pack is dynamically compiled.
3. The landing page updates to sell the new validated offer.

### Phase 9: Monetization Flow
Organic traffic is systematically funnelled:
```text
TikTok Organic ➔ Bio Link ➔ High-Value Free Gift ➔ Email Capture ➔ $29 OS Template ➔ $299 System OS ➔ Enterprise Setup
```
