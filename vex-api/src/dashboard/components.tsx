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

// ============================================================================
// Types
// ============================================================================

interface LayerScore {
  layer: string;
  name: string;
  score: number; // 0-10
}

interface Assessment {
  date: string; // ISO 8601
  execution_rate: number; // 0-100
}

interface FounderHumanOS {
  founder_id: string;
  execution_success_rate: number; // 0-100
  learning_velocity: number; // hours
  governance_tier: string; // "90%+ AUTONOMOUS" | "70-79% MONITORED" | "<70% TRAINING"
  layer_scores: LayerScore[];
  last_assessment: string | null;
}

// ============================================================================
// Tier Badge Component
// ============================================================================

interface TierBadgeProps {
  tier: string; // "90%+ AUTONOMOUS" | "70-79% MONITORED" | "<70% TRAINING"
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
export const TierBadge: React.FC<TierBadgeProps> = ({ tier }) => {
  const getTierClass = (tierString: string): string => {
    if (tierString.includes('AUTONOMOUS')) return 'autonomous';
    if (tierString.includes('MONITORED')) return 'monitored';
    return 'training';
  };

  const getTierIcon = (tierString: string): string => {
    if (tierString.includes('AUTONOMOUS')) return '⚡';
    if (tierString.includes('MONITORED')) return '⚙️';
    return '⚠️';
  };

  const tierClass = getTierClass(tier);
  const icon = getTierIcon(tier);

  return (
    <div className={`tier-badge ${tierClass}`}>
      <div className="tier-badge-icon">{icon}</div>
      <div>{tier}</div>
    </div>
  );
};

// ============================================================================
// Layer Chart Component
// ============================================================================

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
export const LayerChart: React.FC<LayerChartProps> = ({ layers }) => {
  const getScoreClass = (score: number): string => {
    if (score >= 9) return 'excellent';
    if (score >= 5) return 'good';
    return 'atrisk';
  };

  const getScorePercentage = (score: number): number => {
    return (score / 10) * 100;
  };

  return (
    <section className="layers-section">
      <h2 className="section-title">Layer Progress (L1-L10)</h2>
      <div className="layers-grid">
        {layers.map((layer) => {
          const scoreClass = getScoreClass(layer.score);
          const percentage = getScorePercentage(layer.score);

          return (
            <article key={layer.layer} className="layer-card">
              <div className="layer-code">{layer.layer}</div>
              <div className="layer-name">{layer.name}</div>
              <div className="layer-bar">
                <div
                  className={`layer-bar-fill ${scoreClass}`}
                  style={{ width: `${percentage}%` }}
                  role="progressbar"
                  aria-valuenow={layer.score}
                  aria-valuemin={0}
                  aria-valuemax={10}
                  aria-label={`${layer.name}: ${layer.score} out of 10`}
                />
              </div>
              <div className="layer-score">{layer.score}/10</div>
            </article>
          );
        })}
      </div>
    </section>
  );
};

// ============================================================================
// Metrics Gauge Component
// ============================================================================

interface MetricsGaugeProps {
  executionRate: number; // 0-100
  learningVelocity: number; // hours (0-100+ but capped at 96 for display)
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
export const MetricsGauge: React.FC<MetricsGaugeProps> = ({
  executionRate,
  learningVelocity,
}) => {
  const getExecutionClass = (rate: number): string => {
    if (rate >= 90) return 'green';
    if (rate >= 70) return 'yellow';
    return 'red';
  };

  const getLearningClass = (velocity: number): string => {
    // Inverted: lower hours is better
    if (velocity <= 48) return 'green';
    if (velocity <= 72) return 'yellow';
    return 'red';
  };

  const getExecutionLabel = (rate: number): string => {
    if (rate >= 90) return 'Excellent';
    if (rate >= 70) return 'Good';
    return 'At Risk';
  };

  const getLearningLabel = (velocity: number): string => {
    if (velocity <= 48) return 'Fast';
    if (velocity <= 72) return 'Moderate';
    return 'Slow';
  };

  const executionClass = getExecutionClass(executionRate);
  const learningClass = getLearningClass(learningVelocity);
  const displayVelocity = Math.min(learningVelocity, 96);
  const velocityPercentage = (displayVelocity / 96) * 100;

  return (
    <section className="metrics-section">
      <div className="gauge">
        <div className="gauge-header">Execution Success Rate</div>
        <div className={`gauge-value ${executionClass}`}>{executionRate}%</div>
        <div className="gauge-bar">
          <div
            className={`gauge-bar-fill ${executionClass}`}
            style={{ width: `${executionRate}%` }}
            role="progressbar"
            aria-valuenow={executionRate}
            aria-valuemin={0}
            aria-valuemax={100}
            aria-label={`Execution success rate: ${executionRate} percent`}
          />
        </div>
        <div className="gauge-label">
          {getExecutionLabel(executionRate)} • Target: 90%+ for Autonomous tier
        </div>
      </div>

      <div className="gauge">
        <div className="gauge-header">Learning Velocity</div>
        <div className={`gauge-value ${learningClass}`}>
          {learningVelocity < 100 ? learningVelocity : '96'}h
        </div>
        <div className="gauge-bar">
          <div
            className={`gauge-bar-fill ${learningClass}`}
            style={{ width: `${velocityPercentage}%` }}
            role="progressbar"
            aria-valuenow={Math.min(learningVelocity, 96)}
            aria-valuemin={0}
            aria-valuemax={96}
            aria-label={`Learning velocity: ${learningVelocity} hours`}
          />
        </div>
        <div className="gauge-label">
          {getLearningLabel(learningVelocity)} • Target: ≤48h for Autonomous tier
        </div>
      </div>
    </section>
  );
};

// ============================================================================
// Trend Timeline Component
// ============================================================================

interface TrendTimelineProps {
  assessments: Assessment[]; // Last 4 assessments
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
export const TrendTimeline: React.FC<TrendTimelineProps> = ({ assessments }) => {
  const maxRate = Math.max(...assessments.map((a) => a.execution_rate), 100);
  const minRate = Math.min(...assessments.map((a) => a.execution_rate), 0);

  // Map execution rates to SVG y-coordinates (inverted: high rate = low y)
  const chartHeight = 150;
  const chartWidth = 400;
  const yPadding = 30;
  const pointSpacing = chartWidth / (assessments.length + 1);

  const points = assessments.map((assessment, index) => {
    const x = (index + 1) * pointSpacing;
    const normalizedRate = (assessment.execution_rate - minRate) / (maxRate - minRate);
    const y = yPadding + (1 - normalizedRate) * (chartHeight - yPadding * 2);
    return { x, y, rate: assessment.execution_rate };
  });

  const polylinePoints = points.map((p) => `${p.x},${p.y}`).join(' ');

  return (
    <section className="trend-section">
      <h2 className="section-title">Execution Trend (Last 4 Assessments)</h2>
      <div className="trend-chart">
        <svg
          className="sparkline"
          viewBox={`0 0 ${chartWidth} ${chartHeight}`}
          preserveAspectRatio="xMidYMid meet"
          role="img"
          aria-label="Execution rate trend chart"
        >
          {/* Grid lines */}
          <line
            x1="0"
            y1={yPadding}
            x2={chartWidth}
            y2={yPadding}
            stroke="#e9ecef"
            strokeWidth="1"
          />
          <line
            x1="0"
            y1={chartHeight / 2}
            x2={chartWidth}
            y2={chartHeight / 2}
            stroke="#e9ecef"
            strokeWidth="1"
          />
          <line
            x1="0"
            y1={chartHeight - yPadding}
            x2={chartWidth}
            y2={chartHeight - yPadding}
            stroke="#e9ecef"
            strokeWidth="1"
          />

          {/* Trend line */}
          <polyline
            points={polylinePoints}
            stroke="#ffc107"
            strokeWidth="3"
            fill="none"
            strokeLinecap="round"
            strokeLinejoin="round"
          />

          {/* Data points */}
          {points.map((point, index) => (
            <circle
              key={index}
              cx={point.x}
              cy={point.y}
              r="4"
              fill="#ffc107"
            />
          ))}
        </svg>
      </div>

      {/* Labels */}
      <div className="trend-labels">
        {assessments.map((assessment, index) => {
          const daysAgo = (assessments.length - index - 1) * 30; // Approximate
          const timeLabel = daysAgo === 0 ? 'Now' : `${daysAgo}d ago`;

          return (
            <div key={index} className="trend-point">
              <strong>{assessment.execution_rate}%</strong>
              <br />
              <small>{timeLabel}</small>
            </div>
          );
        })}
      </div>
    </section>
  );
};

// ============================================================================
// Full Dashboard Component
// ============================================================================

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
export const FounderDashboard: React.FC<FounderDashboardProps> = ({ data }) => {
  // Note: Phase 4 scaffold — no state, no hooks
  // Phase 5 will fetch this data via useFetchFounderHumanOS hook

  const historicalAssessments: Assessment[] = [
    // Phase 5: fetch via useHistoricalAssessments hook
    { date: '2026-04-29', execution_rate: 70 },
    { date: '2026-05-29', execution_rate: 75 },
    { date: '2026-06-29', execution_rate: 82 },
    { date: data.last_assessment || '2026-07-29', execution_rate: data.execution_success_rate },
  ];

  return (
    <div className="dashboard-container">
      {/* Header */}
      <header>
        <h1>Founder Dashboard</h1>
        <p>Human OS Governance Tier & Layer Progress</p>
        {data.last_assessment && (
          <p style={{ fontSize: '14px', color: '#999', marginTop: '8px' }}>
            Last assessment: {data.last_assessment}
          </p>
        )}
      </header>

      {/* Tier Badge */}
      <TierBadge tier={data.governance_tier} />

      {/* Metrics Gauges */}
      <MetricsGauge
        executionRate={data.execution_success_rate}
        learningVelocity={data.learning_velocity}
      />

      {/* Layer Progress */}
      <LayerChart layers={data.layer_scores} />

      {/* Trend Timeline */}
      <TrendTimeline assessments={historicalAssessments} />
    </div>
  );
};

// ============================================================================
// Export Types for Phase 5 Integration
// ============================================================================

export type {
  FounderHumanOS,
  LayerScore,
  Assessment,
  TierBadgeProps,
  LayerChartProps,
  MetricsGaugeProps,
  TrendTimelineProps,
  FounderDashboardProps,
};
