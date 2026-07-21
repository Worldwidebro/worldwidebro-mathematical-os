/**
 * Venture Readiness and Codebase Evaluation Rubrics
 */

export interface VentureMetrics {
  codeCompleteness: number;  // 0 to 100
  apiReadiness: number;      // 0 to 100
  documentationScore: number;// 0 to 100
  testCoverage: number;      // 0 to 100
}

export class ScoringEngine {
  /**
   * Calculates overall venture readiness based on four core criteria
   */
  calculateReadiness(metrics: VentureMetrics): {
    score: number;
    tier: 'TRAINING' | 'MONITORED' | 'SUPERVISED' | 'AUTONOMOUS';
  } {
    const rawScore = (
      metrics.codeCompleteness * 0.4 +
      metrics.apiReadiness * 0.3 +
      metrics.documentationScore * 0.2 +
      metrics.testCoverage * 0.1
    );

    const score = Math.round(rawScore);
    
    // Auto-approve authority limits mapped from AGENTS.md rules
    let tier: 'TRAINING' | 'MONITORED' | 'SUPERVISED' | 'AUTONOMOUS';
    if (score >= 90) {
      tier = 'AUTONOMOUS';
    } else if (score >= 80) {
      tier = 'SUPERVISED';
    } else if (score >= 70) {
      tier = 'MONITORED';
    } else {
      tier = 'TRAINING';
    }

    return { score, tier };
  }

  /**
   * Generates a feedback report with improvement guidelines
   */
  generateReport(metrics: VentureMetrics): string {
    const { score, tier } = this.calculateReadiness(metrics);
    
    const lines = [
      `📊 Venture Readiness Audit: ${score}% (${tier})`,
      `==========================================`,
      `- Code Completeness: ${metrics.codeCompleteness}%`,
      `- API Gateway Wiring: ${metrics.apiReadiness}%`,
      `- Documentation Depth: ${metrics.documentationScore}%`,
      `- Test Suite Coverage: ${metrics.testCoverage}%`,
      ``,
    ];

    if (tier === 'AUTONOMOUS') {
      lines.push('✅ System is 100% autonomous. Ready for direct deployment without supervision.');
    } else if (tier === 'SUPERVISED') {
      lines.push('⚠️ Requires team lead approval ($1K+) or manual oversight for transactions.');
    } else if (tier === 'MONITORED') {
      lines.push('⚠️ Requires manager/director approval on all executions.');
    } else {
      lines.push('❌ Undergoing training. Pull from production until score reaches 70%.');
    }

    return lines.join('\n');
  }
}
