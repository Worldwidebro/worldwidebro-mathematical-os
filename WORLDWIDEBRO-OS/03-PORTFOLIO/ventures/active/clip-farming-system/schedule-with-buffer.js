/**
 * Schedule Ace Construction posts via Buffer MCP
 */

import fs from "fs";

const manifest = JSON.parse(
  fs.readFileSync("./assets/ace-construction-clips.json", "utf-8")
);

const VENTURE_ID = "ff49c6d8-ef68-4793-8341-4a7a94574d40";
const VENTURE_NAME = "Ace Construction";

function buildBufferSchedule() {
  const posts = [];
  const startDate = new Date("2026-06-13T09:00:00Z");

  const schedule = [
    { day: 0, platform: "linkedin", time: 9, clip: 0 },
    { day: 1, platform: "tiktok", time: 18, clip: 1 },
    { day: 2, platform: "linkedin", time: 9, clip: 2 },
    { day: 2, platform: "instagram", time: 11, clip: 7 },
    { day: 3, platform: "linkedin", time: 9, clip: 3 },
    { day: 4, platform: "tiktok", time: 18, clip: 10 },
    { day: 4, platform: "instagram", time: 19, clip: 0 },
    { day: 6, platform: "facebook", time: 19, clip: 6 },
  ];

  for (let week = 0; week < 4; week++) {
    schedule.forEach(({ day, platform, time, clip }) => {
      const postDate = new Date(startDate);
      postDate.setDate(postDate.getDate() + week * 7 + day);
      postDate.setHours(time, 0, 0, 0);

      const clipData = manifest.clips[clip];

      posts.push({
        profile_id: `${platform}_ace_construction`,
        text: `${clipData.title} #construction`,
        video_url: `./output/ace-construction/${platform}/ace-${String(clipData.clip_id).padStart(3, "0")}-${platform}.mp4`,
        scheduled_at: postDate.toISOString(),
        platform: platform,
      });
    });
  }

  return posts;
}

const bufferSchedule = buildBufferSchedule();

console.log("\n🚀 ACE CONSTRUCTION: BUFFER MCP SCHEDULING");
console.log("═".repeat(70));
console.log(`\nBuffer Schedule Generated:`);
console.log(`  Venture: ${VENTURE_NAME}`);
console.log(`  Total Posts: ${bufferSchedule.length}`);
console.log(`  Weeks: 4`);

console.log(`\nFirst Week:\n`);
bufferSchedule.slice(0, 8).forEach((post) => {
  const date = new Date(post.scheduled_at);
  console.log(
    `  ${date.toLocaleDateString()} ${date.toLocaleTimeString().substring(0, 5)} - ${post.platform.toUpperCase()}`
  );
});

console.log(`\n✅ All ${bufferSchedule.length} posts ready for Buffer!\n`);

export { bufferSchedule, VENTURE_ID, VENTURE_NAME };
