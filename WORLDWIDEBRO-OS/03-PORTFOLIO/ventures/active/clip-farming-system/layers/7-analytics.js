/**
 * Layer 7: Analytics
 * Input: Scheduled posts → Output: Performance metrics
 */

export async function analyzePerformance(scheduled, context) {
  console.log(`\n📊 Layer 7: Analytics`);
  console.log(`   Analyzing ${scheduled.scheduled_count} posts`);

  const metrics = {
    total_posts: scheduled.scheduled_count,
    platforms: [...new Set(scheduled.scheduled.map((s) => s.platform))],
    clips_count: [...new Set(scheduled.scheduled.map((s) => s.clip_id))].length,
  };

  console.log(`   ✅ ${metrics.platforms.length} platforms`);

  return {
    venture_id: context.venture_id,
    metrics,
    status: "complete",
  };
}
