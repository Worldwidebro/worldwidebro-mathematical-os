#!/bin/bash
# Test Instagram Intelligence System — Full Option 1 Pipeline

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$SCRIPT_DIR/../../../"
INTAKE_DIR="$PROJECT_DIR/00_INTAKE_LAYER"
TEMP_DIR="/tmp/instagram_pipeline_test"

echo "═══════════════════════════════════════════════════════════════"
echo "INSTAGRAM INTELLIGENCE PIPELINE — TEST RUN"
echo "═══════════════════════════════════════════════════════════════"
echo ""

mkdir -p "$TEMP_DIR"
echo "✓ Test directory: $TEMP_DIR"
echo ""

# Check for sample images
echo "STEP 1: Checking for sample images"
echo "─────────────────────────────────────────────────────────────────"
SAMPLE_COUNT=$(find "$INTAKE_DIR/Instagram_Screenshots/" -type f \( -iname "*.png" -o -iname "*.jpg" -o -iname "*.jpeg" \) 2>/dev/null | wc -l)

if [ "$SAMPLE_COUNT" -eq 0 ]; then
    echo "⚠️  No sample images found in $INTAKE_DIR/Instagram_Screenshots/"
    echo ""
    echo "To test, add 1-5 Instagram screenshot images to:"
    echo "  $INTAKE_DIR/Instagram_Screenshots/"
    echo ""
    echo "Then run this script again."
    exit 0
fi

echo "✓ Found $SAMPLE_COUNT sample image(s)"
echo ""

# Step 1: OCR Vision Processor
echo "STEP 2: OCR Vision Processor (Claude Vision API)"
echo "─────────────────────────────────────────────────────────────────"
python3 "$SCRIPT_DIR/ocr_vision_processor.py" \
    --batch-dir "$INTAKE_DIR/Instagram_Screenshots/" \
    --output "$TEMP_DIR/01_extracted.json"

echo "✓ Extraction complete: $TEMP_DIR/01_extracted.json"
echo ""

# Step 2: Extraction Agent
echo "STEP 3: Extraction Agent (Venture Routing)"
echo "─────────────────────────────────────────────────────────────────"
python3 "$SCRIPT_DIR/extraction_agent.py" \
    --input "$TEMP_DIR/01_extracted.json" \
    --output "$TEMP_DIR/02_classified.json"

echo "✓ Classification complete"
echo ""

# Step 3: Dedup
echo "STEP 4: Deduplication (LightRAG Semantic Search)"
echo "─────────────────────────────────────────────────────────────────"
python3 "$SCRIPT_DIR/dedup_against_lightrag.py" \
    --input "$TEMP_DIR/02_classified.json" \
    --output "$TEMP_DIR/03_deduped.json"

echo "✓ Deduplication complete"
echo ""

# Step 4: Push to Obsidian
echo "STEP 5: Push to Obsidian Vault (CloudDocs)"
echo "─────────────────────────────────────────────────────────────────"
python3 "$SCRIPT_DIR/push_to_obsidian.py" \
    --input "$TEMP_DIR/03_deduped.json" \
    --supabase-output "$TEMP_DIR/04_supabase_batch.json"

echo "✓ Push to Obsidian complete"
echo ""

# Results
echo "STEP 6: Results Summary"
echo "─────────────────────────────────────────────────────────────────"
echo ""
echo "📂 Temp Files Created:"
echo "  1. Extracted:  $TEMP_DIR/01_extracted.json"
echo "  2. Classified: $TEMP_DIR/02_classified.json"
echo "  3. Deduped:    $TEMP_DIR/03_deduped.json"
echo "  4. Supabase:   $TEMP_DIR/04_supabase_batch.json"
echo ""

VAULT_PATH="$HOME/Library/Mobile Documents/com~apple~CloudDocs/Documents/Obsidian Vault"
echo "📝 Obsidian Notes Created:"
echo "  Location: $VAULT_PATH/Instagram_Ideas/"
echo ""

# Preview
echo "Preview — First classified idea:"
echo "─────────────────────────────────────────────────────────────────"
python3 -c "
import json
try:
    with open('$TEMP_DIR/02_classified.json') as f:
        ideas = json.load(f)
        if ideas:
            idea = ideas[0]
            print(f\"Idea: {idea.get('idea_text', '')[:80]}...\")
            print(f\"Category: {idea.get('category', 'Unknown')}\")
            print(f\"Venture Type: {idea.get('venture_type_primary', 'Unknown')}\")
            print(f\"Confidence: {idea.get('confidence', 0):.1%}\")
except Exception as e:
    print(f'Preview error: {e}')
"
echo ""

# Next steps
echo "STEP 7: Next Steps"
echo "─────────────────────────────────────────────────────────────────"
echo ""
echo "✅ Option 1 Pipeline Complete!"
echo ""
echo "Next actions:"
echo "  1. Check Obsidian for new notes:"
echo "     $VAULT_PATH/Instagram_Ideas/"
echo ""
echo "  2. (Optional) Re-ingest into LightRAG:"
echo "     cd /Users/acebless/Documents/iza-os-rag-system && python3 -m src.ingest --source=vault"
echo ""
echo "  3. Review Supabase batch:"
echo "     cat $TEMP_DIR/04_supabase_batch.json"
echo ""
echo "═══════════════════════════════════════════════════════════════"
