#!/bin/bash
# Phase 2: Consolidate Ventures & Repos Registry
# Moves scattered ventures into standardized folder structure

set -e

DOCS_DIR="/Users/acebless/Documents"
OS_DIR="$DOCS_DIR/WORLDWIDEBRO-OS"
VENTURES_DIR="$OS_DIR/10_VENTURES"

echo "=== Phase 2: Ventures & Repos Consolidation ==="
echo ""

# Create target directories
echo "📁 Creating target directories..."
mkdir -p "$VENTURES_DIR/Operations_Ventures"
mkdir -p "$VENTURES_DIR/SaaS_Ventures"
mkdir -p "$OS_DIR/00_CLIENT_WORK"

# Move con-001 (construction/operations)
if [ -d "$DOCS_DIR/con-001-ace-construction" ]; then
    echo "📦 Moving con-001-ace-construction → Operations_Ventures..."
    mv "$DOCS_DIR/con-001-ace-construction" "$VENTURES_DIR/Operations_Ventures/con-001-ace-construction"
    echo "   ✅ Moved"
else
    echo "   ⚠️  con-001-ace-construction not found (may already be moved)"
fi

# Move bw-001 (SaaS)
if [ -d "$DOCS_DIR/bw-001-lash-extension-studio" ]; then
    echo "📦 Moving bw-001-lash-extension-studio → SaaS_Ventures..."
    mv "$DOCS_DIR/bw-001-lash-extension-studio" "$VENTURES_DIR/SaaS_Ventures/bw-001-lash-extension-studio"
    echo "   ✅ Moved"
else
    echo "   ⚠️  bw-001-lash-extension-studio not found (may already be moved)"
fi

# Move venture-factory-core (determine category later)
if [ -d "$DOCS_DIR/venture-factory-core" ]; then
    echo "📦 Moving venture-factory-core → SaaS_Ventures (tentative)..."
    mv "$DOCS_DIR/venture-factory-core" "$VENTURES_DIR/SaaS_Ventures/venture-factory-core"
    echo "   ✅ Moved (verify category and reorganize if needed)"
else
    echo "   ⚠️  venture-factory-core not found"
fi

# Move YES-LLC client work
if [ -d "$DOCS_DIR/YES-LLC-CONTRACTOR-DELIVERY" ]; then
    echo "📦 Moving YES-LLC-CONTRACTOR-DELIVERY → 00_CLIENT_WORK..."
    mv "$DOCS_DIR/YES-LLC-CONTRACTOR-DELIVERY" "$OS_DIR/00_CLIENT_WORK/YES-LLC-Wave-Rideshare"
    echo "   ✅ Moved"
else
    echo "   ⚠️  YES-LLC-CONTRACTOR-DELIVERY not found"
fi

echo ""
echo "=== Loading Venture-Repo Linkage ==="
echo ""

# Use the existing venture-repo alignment CSV
LINKAGE_FILE="$OS_DIR/08_RESEARCH/Ventures-Data/WORLDWIDEBRO-VENTURES-REPOS-ALIGNMENT.csv"

if [ -f "$LINKAGE_FILE" ]; then
    echo "✅ Found linkage: $LINKAGE_FILE"
    echo ""
    echo "Sample (first 5 ventures):"
    head -6 "$LINKAGE_FILE" | cut -d',' -f1-6
    echo ""
    echo "📊 Total ventures in linkage: $(wc -l < "$LINKAGE_FILE")"
else
    echo "❌ Linkage file not found: $LINKAGE_FILE"
    exit 1
fi

echo ""
echo "=== Phase 2 Complete ==="
echo ""
echo "Folder structure updated:"
find "$VENTURES_DIR" -maxdepth 2 -type d | sort

echo ""
echo "Next steps:"
echo "  1. Run: python3 verify_venture_linkage.py"
echo "  2. Run: python3 moneyprinter_v2_batch_generator.py"
echo "  3. Run: python3 instagram_scraper.py"
