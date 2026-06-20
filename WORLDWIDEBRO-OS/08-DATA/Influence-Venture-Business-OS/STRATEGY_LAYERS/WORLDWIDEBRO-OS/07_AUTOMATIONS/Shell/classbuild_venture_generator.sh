#!/bin/bash
# ClassBuild per-venture course generator
# Usage: ./classbuild_venture_generator.sh EDU-023 "Cybersecurity Bootcamp"

set -e

VENTURE_FOLDER="$1"
VENTURE_NAME="$2"
VAULT="$HOME/Library/Mobile Documents/com~apple~CloudDocs/Documents/Obsidian Vault"
VENTURES_DIR="$VAULT/07-BUSINESS-STRATEGY/ventures/Education"
CONFIG_FILE="$HOME/Documents/classbuild_ventures.json"
CLASSBUILD_DIR="/tmp/classbuild"

if [ -z "$VENTURE_FOLDER" ] || [ -z "$VENTURE_NAME" ]; then
    echo "Usage: $0 VENTURE_FOLDER VENTURE_NAME"
    echo "Example: $0 EDU-023-Cybersecurity-Bootcamp 'Cybersecurity Bootcamp'"
    exit 1
fi

# Check environment
if [ ! -d "$CLASSBUILD_DIR" ]; then
    echo "❌ ClassBuild not found. Run:"
    echo "   cd /tmp && git clone https://github.com/jtangen/classbuild.git"
    exit 1
fi

if [ ! -d "$CLASSBUILD_DIR/node_modules" ]; then
    echo "📦 Installing ClassBuild dependencies..."
    cd "$CLASSBUILD_DIR"
    npm install > /dev/null 2>&1
fi

# Get config from JSON
CONFIG=$(jq ".\"$VENTURE_FOLDER\"" "$CONFIG_FILE")
TOPIC=$(echo "$CONFIG" | jq -r '.topic')
CHAPTERS=$(echo "$CONFIG" | jq -r '.chapters')
LEVEL=$(echo "$CONFIG" | jq -r '.level')
NOTES=$(echo "$CONFIG" | jq -r '.notes')

if [ "$TOPIC" == "null" ]; then
    echo "❌ Venture not found in config: $VENTURE_FOLDER"
    exit 1
fi

# Generate
VENTURE_PATH="$VENTURES_DIR/$VENTURE_FOLDER"
OUTPUT_DIR="$VENTURE_PATH/courses"
mkdir -p "$OUTPUT_DIR"

echo "🚀 Generating course for $VENTURE_NAME"
echo "   Topic: $TOPIC"
echo "   Chapters: $CHAPTERS | Level: $LEVEL"
echo ""

cd "$CLASSBUILD_DIR"
npx tsx scripts/generate-course.ts \
    --topic "$TOPIC" \
    --chapters "$CHAPTERS" \
    --level "$LEVEL" \
    --theme midnight \
    --length standard \
    --notes "$NOTES" \
    --output "$OUTPUT_DIR"

echo ""
echo "✅ Course generated at: $OUTPUT_DIR"
echo "   Files: $(ls -la "$OUTPUT_DIR" | wc -l) items"
