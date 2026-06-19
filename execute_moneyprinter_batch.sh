#!/bin/bash
# Execute MoneyPrinter V2 video generation for prepared ventures

OUTPUT_DIR="/Users/acebless/Documents/moneyprinter-output"
MONEYPRINTER_DIR="/Users/acebless/MoneyPrinterV2"

echo "🎬 Starting MoneyPrinter V2 batch video generation..."
echo ""

# Count preparation files
VENTURE_COUNT=$(find "$OUTPUT_DIR" -name "metadata.json" | wc -l)
echo "📹 Found $VENTURE_COUNT ventures ready for video generation"
echo ""

# Run MoneyPrinter V2 main.py with batch mode
cd "$MONEYPRINTER_DIR"

# Create batch config file
cat > /tmp/mp_batch_config.json <<'EOF'
{
  "batch_mode": true,
  "input_dir": "$OUTPUT_DIR",
  "output_format": "mp4",
  "quality": "1080p",
  "target_platform": "youtube_shorts",
  "parallel_jobs": 2
}
EOF

# Execute MoneyPrinter V2 (requires Python 3.10+)
python3.12 src/main.py --config /tmp/mp_batch_config.json

echo ""
echo "✅ Video generation complete!"
echo "📂 Check output: $OUTPUT_DIR"
