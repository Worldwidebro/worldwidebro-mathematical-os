#!/bin/bash
# Generate videos using FFmpeg + ImageMagick (no Python dependencies)

OUTPUT_DIR="/Users/acebless/Documents/moneyprinter-output"

echo "🎬 FFmpeg Video Generator"
echo "=========================="
echo ""

# Check for ffmpeg
if ! command -v ffmpeg &> /dev/null; then
  echo "❌ ffmpeg not found. Install: brew install ffmpeg"
  exit 1
fi

count=0
for venture_dir in "$OUTPUT_DIR"/*; do
  if [ ! -f "$venture_dir/metadata.json" ]; then
    continue
  fi

  venture_id=$(basename "$venture_dir")
  output_file="$venture_dir/output.mp4"

  # Extract metadata
  title=$(jq -r '.title' "$venture_dir/metadata.json")
  script=$(jq -r '.script' "$venture_dir/metadata.json")

  echo "[$(( count + 1 ))] $title"

  # Create frame with text using ffmpeg drawtext filter
  # Duration: 30 seconds, size: 1080x1920 (vertical)

  # Use ffmpeg's built-in drawtext filter
  ffmpeg -f lavfi -i color=c='#1a1a2e':s=1080x1920:d=30 \
    -vf "drawtext=text='$title':fontsize=60:fontcolor=white:x=50:y=100, \
         drawtext=text='$script':fontsize=36:fontcolor='#00ff00':x=50:y=300:line_spacing=20" \
    -c:v libx264 -pix_fmt yuv420p \
    -y "$output_file" 2>&1 | grep -E "frame=|error" || true

  if [ -f "$output_file" ] && [ -s "$output_file" ]; then
    size=$(du -h "$output_file" | cut -f1)
    echo "   ✅ Video created: $size"
    count=$(( count + 1 ))
  else
    echo "   ❌ FFmpeg generation failed"
  fi

done

echo ""
echo "=========================================="
echo "✅ Generated $count videos"
echo "📂 Location: $OUTPUT_DIR"
echo "=========================================="
