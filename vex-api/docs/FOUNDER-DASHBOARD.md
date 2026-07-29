# Founder Profile Dashboard

## Overview

Real-time founder development tracking dashboard showing Human OS layers, governance tier, and learning velocity.

**Data Source:** GET `/founders/:id/human-os` (vex-api)

---

## Dashboard Layout

### Tier Badge
```
Tier: [90%+ AUTONOMOUS | 70-79% MONITORED | <70% TRAINING]
Assessment: [YYYY-MM-DD]
```

### Key Metrics
```
Execution Success Rate: [94%] ████░
Learning Velocity: [36h] ████░
Average Layer Score: [8.5] ████░
```

### Layer Progression (L1-L10)

```
Layer      Score  
───────────────────
L1 Identity      [9/10] ████████░
L2 Emotion       [9/10] ████████░
L3 Cognition     [9/10] ████████░
L4 Intuition     [8/10] ███████░░
L5 Energy        [9/10] ████████░
L6 Frequency     [10/10] █████████
L7 Network       [9/10] ████████░
L8 Creativity    [9/10] ████████░
L9 Character     [9/10] ████████░
L10 Legacy       [8/10] ███████░░
───────────────────
Average: [8.9/10]
```

### Tier Logic

```
Execution ≥ 90% AND Learning ≤ 48h → 90%+ AUTONOMOUS
Execution 70-79% OR Learning 48-72h → 70-79% MONITORED
Execution < 70% OR Learning > 72h → <70% TRAINING
```

### Historical Trend

```
Q3 2026: 90%+ AUTONOMOUS ↗
Q2 2026: 70-79% MONITORED ↗
Q1 2026: 70-79% MONITORED ↗
Q4 2025: <70% TRAINING (baseline)
```

---

## API Integration

**Endpoint:** `GET /founders/{founder_id}/human-os`

**Response:**
```json
{
  "founder_id": "founder-001",
  "execution_success_rate": 94,
  "learning_velocity": 36,
  "governance_tier": "90%+ AUTONOMOUS",
  "layer_scores": [
    {"layer": "L1", "score": 10},
    {"layer": "L2", "score": 9}
  ],
  "last_assessment": "2026-07-28T19:22:24.873Z"
}
```

---

## Frontend Components

- **TierBadge:** Display current tier with color (green/yellow/red)
- **LayerChart:** Progress bars for L1-L10
- **MetricsGauge:** Execution % and Learning hours
- **TrendTimeline:** Quarter-over-quarter tier changes
- **ActionItems:** Contextual suggestions per tier

---

## Quarterly Review Workflow

1. Recalibration job runs
2. Dashboard auto-updates from Neo4j
3. Manager reviews tier + recommendations
4. Tier improved → Next growth focus
5. Tier declined → Schedule coaching

---

## OPCO-Specific Customizations

- **CON-OS:** Focus on L9 (character under pressure)
- **STA-OS:** Focus on L7 (employer/candidate network)
- **FIN-OS:** Focus on L9 (ethics), L6 (client responsiveness)
- **RE-OS:** Focus on L9 (disclosure), L8 (service innovation)
- **EDU-OS:** Focus on L8 (curriculum), L7 (alumni)
- **LOG-OS:** Focus on L9 (safety), L6 (reliability)

---

**Status:** Dashboard specification complete. Ready for frontend implementation.
