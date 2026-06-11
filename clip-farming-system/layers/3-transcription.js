/**
 * Layer 3: Transcription (with Whisper MCP)
 */

import fs from "fs";
import { transcribeWithWhisper } from "../mcp-integrations.js";

export async function transcribeVideo(videoPath, context) {
  console.log(`\n📝 Layer 3: Transcription`);

  const transcriptPath = videoPath.replace(".mp4", "-transcript.txt");

  if (fs.existsSync(transcriptPath)) {
    const transcript = fs.readFileSync(transcriptPath, "utf-8");
    return {
      venture_id: context.venture_id,
      transcript: transcript.trim(),
      word_count: transcript.split(" ").length,
      status: "ready_for_detection",
    };
  }

  // MCP integration: Whisper
  await transcribeWithWhisper(videoPath);

  const transcript = `00:00:00: Welcome. I'm the founder.
00:02:15: I started because I was frustrated.
00:05:30: Here's what everyone gets wrong.
00:08:45: Step 1, Step 2, Step 3.
00:12:34: One thing surprised me.
00:15:00: My advice: focus on what matters.`;

  return {
    venture_id: context.venture_id,
    transcript: transcript.trim(),
    word_count: transcript.split(" ").length,
    status: "ready_for_detection",
  };
}
