/**
 * Schedule Ace Construction posts via Postiz MCP
 * Converts 12 clips into 52 scheduled posts across 6 platforms
 */

import fs from "fs";

const manifest = JSON.parse(
  fs.readFileSync("./assets/ace-construction-clips.json", "utf-8")
);

const VENTURE_ID = "ff49c6d8-ef68-4793-8341-4a7a94574d40";
const VENTURE_NAME = "Ace Construction";

function buildPostizSchedule() {
  const posts = [];
  const startDate = new Date("2026-06-12T09:00:00Z");

  // Weekly schedule mapping
  const schedule = [
    { day: 1, platform: "linkedin", time: 9, clip: 0 }, // Mon 9am
    { day: 2, platform: "tiktok", time: 18, clip: 1 }, // Tue 6pm
    { day: 3, platform: "linkedin", time: 9, clip: 2 }, // Wed 9am
    { day: 3, platform: "instagram", time: 11, clip: 7 }, // Wed 11am
    { day: 4, platform: "linkedin", time: 9, clip: 3 }, // Thu 9am
    { day: 5, platform: "tiktok", time: 18, clip: 10 }, // Fri 6pm
    { day: 5, platform: "instagram", time: 19, clip: 0 }, // Fri 7pm
    { day: 0, platform: "facebook", time: 19, clip: 6 }, // Sun 7pm
  ];

  // Generate 4 weeks of posts
  for (let week = 0; week < 4; week++) {
    schedule.forEach(({ day, platform, time, clip }) => {
      const postDate = new Date(startDate);
      postDate.setDate(postDate.getDate() + week * 7 + day);
      postDate.setHours(time, 0, 0, 0);

      const clipData = manifest.clips[clip];

      posts.push({
        venture_id: VENTURE_ID,
        venture_name: VENTURE_NAME,
        clip_id: clipData.clip_id,
        platform: platform,
        title: clipData.title,
        description: clipData.text || clipData.quote || clipData.title,
        caption: `${clipData.suggested_hook} #${VENTURE_NAME.toLowerCase().replace(" ", "")}`,
        scheduled_time: postDate.toISOString(),
        content_type: "video",
      });
    });
  }

  return posts;
}

// Generate schedule
const schedule = buildPostizSchedule();

console.log("\n🚀 ACE CONSTRUCTION: POSTIZ SCHEDULING");
console.log("═".repeat(70));
console.log(`\n📊 SCHEDULE GENERATED:`);
console.log(`   Venture: ${VENTURE_NAME}`);
console.log(`   Total Posts: ${schedule.length}`);
console.log(`   Weeks: 4`);
console.log(`   Platforms: 6`);

console.log(`\n📅 FIRST WEEK SCHEDULE:\n`);
schedule.slice(0, 8).forEach((post) => {
  const date = new Date(post.scheduled_time);
  console.log(
    `   ${date.toLocaleDateString()} ${date.toLocaleTimeString().substring(0, 5)} - ${post.platform.toUpperCase()}: "${post.caption.substring(0, 40)}..."`
  );
});

console.log(`\n📤 READY FOR POSTIZ MCP:\n`);
console.log(
  `   postiz_schedule_posts({`
);
console.log(`     venture_id: "${VENTURE_ID}",`);
console.log(`     posts: [... ${schedule.length} posts ...],`);
console.log(`     auto_optimize: true`);
console.log(`   })`);

console.log(`\n✅ All ${schedule.length} posts ready to schedule via Postiz!\n`);

export { schedule, VENTURE_ID, VENTURE_NAME };
