/**
 * Layer 1: Content Intake
 */

import fs from "fs";

export async function intakeContent(source, context) {
  const { venture_id = "unknown", venture_name = "Unknown" } = context;

  console.log(`\n📥 Layer 1: Intake`);

  const transcriptPath = source.replace(".mp4", "-transcript.txt");
  const hasTranscript = fs.existsSync(transcriptPath);

  if (!fs.existsSync(source) && !hasTranscript) {
    throw new Error(`Files not found`);
  }

  let fileSize = 0;
  if (fs.existsSync(source)) {
    fileSize = fs.statSync(source).size;
  } else if (hasTranscript) {
    fileSize = fs.statSync(transcriptPath).size;
  }

  return {
    venture_id,
    venture_name,
    video_path: source,
    transcript_available: hasTranscript,
    file_size_mb: (fileSize / 1024 / 1024).toFixed(2),
    status: "ready_for_transcription",
  };
}
