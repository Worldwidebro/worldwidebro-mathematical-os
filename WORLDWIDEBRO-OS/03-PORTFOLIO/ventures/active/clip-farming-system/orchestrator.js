/**
 * Orchestrator: Coordinate all 7 layers
 * Flow: L1 → L2 + L3 → L4 → L5 → L6 → L7
 */

import { intakeContent } from "./layers/1-intake.js";
import { researchTrends } from "./layers/2-research.js";
import { transcribeVideo } from "./layers/3-transcription.js";
import { detectClips } from "./layers/4-detection.js";
import { produceMedia } from "./layers/5-production.js";
import { distributeClips } from "./layers/6-distribution.js";
import { analyzePerformance } from "./layers/7-analytics.js";

export async function processVenture(venture, videoPath) {
  console.log("\n" + "=".repeat(60));
  console.log(`🚀 CLIP FARMING PIPELINE: ${venture.venture_name}`);
  console.log("=".repeat(60));

  try {
    // Layer 1: Content Intake
    const intake = await intakeContent(videoPath, venture);
    console.log(`   Size: ${intake.file_size_mb}MB`);

    // Layer 2 & 3: Parallel
    const [research, transcript] = await Promise.all([
      researchTrends(venture),
      transcribeVideo(videoPath, venture),
    ]);
    console.log(`   Words: ${transcript.word_count}`);

    // Layer 4: Clip Detection
    const detection = await detectClips(transcript.transcript, {
      ...venture,
      trending_topics: research.trending_topics,
    });
    console.log(`   Found: ${detection.clips_count} clips`);

    // Layer 5: Media Production
    const production = await produceMedia(
      videoPath,
      detection.clips,
      venture
    );
    console.log(`   Videos: ${production.total_videos}`);

    // Layer 6: Distribution
    const distribution = await distributeClips(production, venture);
    console.log(`   Scheduled: ${distribution.scheduled_count} posts`);

    // Layer 7: Analytics
    const analytics = await analyzePerformance(distribution, venture);
    console.log(`   Platforms: ${analytics.metrics.platforms.join(", ")}`);

    console.log("\n✅ COMPLETE");
    console.log("=".repeat(60));

    return {
      venture_id: venture.venture_id,
      venture_name: venture.venture_name,
      clips_detected: detection.clips_count,
      videos_produced: production.total_videos,
      posts_scheduled: distribution.scheduled_count,
      status: "complete",
    };
  } catch (error) {
    console.error(`\n❌ Error: ${error.message}`);
    throw error;
  }
}
