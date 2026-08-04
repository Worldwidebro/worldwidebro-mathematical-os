import React from 'react';
/**
 * Founder Dashboard Components
 *
 * Phase 4 scaffolds: Non-functional component structure for Phase 5 integration.
 * - No state management (useState, useEffect) — added in Phase 5
 * - No data fetching (useFetchFounderHumanOS) — added in Phase 5
 * - Props-only presentation layer
 *
 * Phase 5 will wrap these with:
 * - useFounderHumanOS(founderId) hook
 * - useHistoricalAssessments(founderId) hook
 * - Error boundaries and loading skeletons
 * - WebSocket subscription for live updates
 */
interface LayerScore {
    layer: string;
    name: string;
    score: number;
}
interface Assessment {
    date: string;
    execution_rate: number;
}
interface FounderHumanOS {
    founder_id: string;
    execution_success_rate: number;
    learning_velocity: number;
    governance_tier: string;
    layer_scores: LayerScore[];
    last_assessment: string | null;
}
interface TierBadgeProps {
    tier: string;
}
/**
 * TierBadge — Displays governance tier with color coding
 *
 * Props:
 *   tier: governance tier string from API
 *
 * Example:
 *   <TierBadge tier="70-79% MONITORED" />
 *
 * Color coding:
 *   "90%+ AUTONOMOUS" → green (#28a745)
 *   "70-79% MONITORED" → yellow (#ffc107)
 *   "<70% TRAINING" → red (#dc3545)
 *
 * Phase 5: Add icon animation, tooltip on hover
 */
export declare const TierBadge: React.FC<TierBadgeProps>;
interface LayerChartProps {
    layers: LayerScore[];
}
/**
 * LayerChart — Grid display of L1-L10 layer progress
 *
 * Props:
 *   layers: Array of {layer: "L1", name: "Ideation", score: 9}
 *
 * Features:
 *   - 10 layer cards in responsive grid (3 cols → 2 cols → 1 col)
 *   - Progress bar (0-10 scale, displayed as 0-100% width)
 *   - Color coding: Green (9-10), Yellow (5-8), Red (1-4)
 *   - Hover effect: translateY(-2px), enhanced shadow
 *
 * Phase 5:
 *   - Add click handler → route to layer detail page
 *   - Add tooltip on hover → show layer description
 *   - Add animation on score change (score-delta arrow)
 *   - Add sparkline for layer history (last 4 assessments)
 */
export declare const LayerChart: React.FC<LayerChartProps>;
interface MetricsGaugeProps {
    executionRate: number;
    learningVelocity: number;
}
/**
 * MetricsGauge — Dual metric display: Execution % and Learning Hours
 *
 * Props:
 *   executionRate: 0-100 (success rate percentage)
 *   learningVelocity: 0-100+ (hours to integrate feedback, capped at 96 for display)
 *
 * Features:
 *   - Two side-by-side gauges (responsive to single column on mobile)
 *   - Execution %: Green (≥90), Yellow (70-89), Red (<70)
 *   - Learning Hours: Red (>72), Yellow (48-72), Green (≤48) — inverted because lower is better
 *   - Progress bar visualization
 *   - Target range display
 *
 * Phase 5:
 *   - Add historical comparison (last assessment delta)
 *   - Add animation on value change (pulse effect)
 *   - Add tooltip explaining metric definitions
 *   - Add tier threshold line on gauge
 */
export declare const MetricsGauge: React.FC<MetricsGaugeProps>;
interface TrendTimelineProps {
    assessments: Assessment[];
}
/**
 * TrendTimeline — Sparkline visualization of execution rate over time
 *
 * Props:
 *   assessments: Array of {date: "2026-07-29", execution_rate: 85}
 *                Expected: 4 assessments (3 months, 2 months, 1 month, now)
 *
 * Features:
 *   - SVG sparkline (polyline + circle markers)
 *   - Yellow line (#ffc107) for trend
 *   - Labels below with dates and execution %
 *   - Responsive: maintains aspect ratio
 *
 * Phase 5:
 *   - Add animated transitions on new data
 *   - Add hover tooltip with exact values
 *   - Add comparison indicators (↑ ↓ →) for delta
 *   - Add ability to load more history (pagination)
 *   - Add tier threshold line overlay
 */
export declare const TrendTimeline: React.FC<TrendTimelineProps>;
interface FounderDashboardProps {
    data: FounderHumanOS;
}
/**
 * FounderDashboard — Main dashboard layout container
 *
 * Props:
 *   data: Complete FounderHumanOS response from GET /founders/:id/human-os
 *
 * Combines all sub-components:
 *   1. TierBadge
 *   2. MetricsGauge (Execution + Learning)
 *   3. LayerChart (L1-L10)
 *   4. TrendTimeline (Historical)
 *
 * Phase 5:
 *   - Wrap with useFetchFounderHumanOS(founderId) hook
 *   - Add loading skeleton while fetching
 *   - Add error boundary
 *   - Add refresh button (refetch)
 *   - Add assessment date display (last_assessment)
 *   - Add comparison vs previous quarter
 */
export declare const FounderDashboard: React.FC<FounderDashboardProps>;
export type { FounderHumanOS, LayerScore, Assessment, TierBadgeProps, LayerChartProps, MetricsGaugeProps, TrendTimelineProps, FounderDashboardProps, };
//# sourceMappingURL=components.d.ts.map