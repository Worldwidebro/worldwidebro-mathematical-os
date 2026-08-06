---
name: vex-api/docs/FOUNDER-DASHBOARD-IMPLEMENTATION
title: Founder Dashboard Implementation Guide
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# Founder Dashboard Implementation Guide

## Overview

The Founder Dashboard displays a founder's Human OS governance tier, layer progress (L1-L10), execution metrics, and historical trends. It wires to the existing `GET /founders/:id/human-os` endpoint and scaffolds for React integration in Phase 5.

## API Endpoint

**GET /founders/:id/human-os**

```json
{
  "founder_id": "user-123",
  "execution_success_rate": 85,
  "learning_velocity": 52,
  "governance_tier": "70-79% MONITORED",
  "layer_scores": [
    { "layer": "L1", "name": "Ideation", "score": 9 },
    { "layer": "L2", "name": "Validation", "score": 8 },
    { "layer": "L3", "name": "MVP Building", "score": 7 },
    { "layer": "L4", "name": "Market Testing", "score": 6 },
    { "layer": "L5", "name": "Revenue Generation", "score": 5 },
    { "layer": "L6", "name": "Team Building", "score": 8 },
    { "layer": "L7", "name": "Systems Design", "score": 7 },
    { "layer": "L8", "name": "Scaling", "score": 4 },
    { "layer": "L9", "name": "Strategic Partnerships", "score": 6 },
    { "layer": "L10", "name": "Market Leadership", "score": 3 }
  ],
  "last_assessment": "2026-07-29"
}
```

## Dashboard Sections

### 1. Tier Badge
- Displays governance tier: "90%+ AUTONOMOUS", "70-79% MONITORED", or "<70% TRAINING"
- Color: Green (90%+), Yellow (70-79%), Red (<70%)
- Positioned top-left; always visible

### 2. Layer Progress (L1-L10)
- Horizontal or vertical card layout showing all 10 layers
- Each layer card displays: layer code (L1-L10), name, progress bar (0-10 score), percentage
- Color-coded: Green (9-10), Yellow (5-8), Red (1-4)
- Responsive: 3 columns desktop, 2 columns tablet, 1 column mobile

### 3. Metrics Gauge
- Dual metric display: Execution % and Learning Hours
- Execution % (left): 0-100, color-coded by tier thresholds
- Learning Hours (right): 0-100+ scale (capped display at 96h), color-coded inversely (lower is better)
- Each gauge shows: current value, target range, status label

### 4. Trend Timeline (Historical)
- Last 4 assessments (if available) shown as a spark chart or line graph
- X-axis: Assessment dates
- Y-axis: Execution % (0-100)
- Shows progression over time; helps identify improvement/decline

## Component Scaffolds

### TierBadge
Props:
- `tier`: string ("90%+ AUTONOMOUS" | "70-79% MONITORED" | "<70% TRAINING")

Returns: Badge component with tier text, color, icon

### LayerChart
Props:
- `layers`: Array<{layer: string, name: string, score: 0-10}>

Returns: Grid of layer cards, each showing progress bar and percentage

### MetricsGauge
Props:
- `executionRate`: 0-100
- `learningVelocity`: 0-100+ (hours)

Returns: Dual gauge display with labels and status text

### TrendTimeline
Props:
- `assessments`: Array<{date: string, execution_rate: 0-100}>

Returns: Sparkline or simple line chart showing 4-point trend

## Color Coding Rules

| Score | Tier | Execution % | Learning Hours | Display |
|-------|------|-------------|-----------------|---------|
| ≥90 | AUTONOMOUS | Green | Green | Excellent |
| 70-89 | MONITORED | Yellow | Yellow | Good |
| <70 | TRAINING | Red | Red | At Risk |

## Phase 5 Integration (Data Fetching)

Phase 4 scaffolds only. Phase 5 will add:
- `useFetchFounderHumanOS(founderId)` hook → fetches endpoint
- `useHistoricalAssessments(founderId)` hook → loads historical data
- Error states and loading skeletons
- Real-time subscription (WebSocket) for live tier changes

## Responsive Breakpoints

- **Desktop** (≥1024px): Full layout, 3-col layer grid, side-by-side gauges
- **Tablet** (768-1023px): Stacked layout, 2-col layer grid, stacked gauges
- **Mobile** (<768px): Full-width cards, 1-col layer grid, single gauge at a time

## Accessibility Notes

- Semantic HTML: `<section>`, `<article>`, `<header>`, `<footer>`
- Color not the only differentiator; use icons + text labels
- ARIA labels on gauge values and progress bars
- Keyboard navigation: Tab through all interactive elements
- Screen reader: Each layer card announces layer code, name, score, and percentage

## File Locations

- **HTML Template**: `src/dashboard/dashboard.html` (standalone, no build needed)
- **React Components**: `src/dashboard/components.tsx` (scaffolds for Phase 5 integration)
- **Styles**: Inline in HTML/components; no CSS framework
- **Router Integration**: Add route `GET /dashboard/:id` in Phase 5 (not in this phase)

## Self-Contained Constraints

- No external CSS frameworks (Tailwind, Bootstrap)
- No charting libraries (Recharts, Chart.js) — use SVG sparklines
- Vanilla CSS Grid + Flexbox for layout
- Vanilla HTML5 + semantic tags
- React components are TypeScript but non-functional in Phase 4 (no state, no hooks)

## Next Steps (Phase 5)

1. Wire components to `useFetchFounderHumanOS` hook
2. Add error boundaries and loading states
3. Implement historical data fetching and caching
4. Add Route integration: `GET /dashboard/:id` in index.ts
5. Build sparkline visualization for trend data
6. Implement WebSocket subscription for live updates
