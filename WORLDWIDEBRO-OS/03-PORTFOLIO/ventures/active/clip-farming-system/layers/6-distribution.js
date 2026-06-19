/**
 * Layer 6: Distribution (with Postiz MCP)
 */

import { scheduleWithPostiz } from "../mcp-integrations.js";

export async function distributeClips(videos, context) {
  console.log(`\n📤 Layer 6: Distribution`);
  console.log(`   Scheduling ${videos.total_videos} clips`);

  const strategy = context.platform_strategy || {
    linkedin: { posts_per_week: 3 },
    twitter: { posts_per_week: 2 },
    tiktok: { posts_per_week: 3 },
  };

  const scheduled = [];

  for (const video of videos.videos) {
    for (const [platform, config] of Object.entries(strategy)) {
      if (config.posts_per_week > 0) {
        scheduled.push({
          clip_id: video.clip_id,
          platform,
          video_path: video[platform],
        });
      }
    }
  }

  // MCP integration: Postiz
  await scheduleWithPostiz(scheduled, context.venture_id);

  console.log(`   ✅ ${scheduled.length} posts ready`);

  return {
    venture_id: context.venture_id,
    scheduled_count: scheduled.length,
    scheduled,
    status: "ready",
  };
}
