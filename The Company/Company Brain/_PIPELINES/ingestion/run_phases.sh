#!/bin/bash
# Phase 2.1-2.2 Orchestration Script
# Repository Intelligence: Ingestion & Normalization

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_DIR="$SCRIPT_DIR/logs"
RAW_DIR="$SCRIPT_DIR/raw"
NORMALIZED_DIR="$SCRIPT_DIR/normalized"

echo "========================================"
echo "PHASE 2: REPOSITORY INTELLIGENCE"
echo "Ingestion & Normalization"
echo "========================================"
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 not found"
    exit 1
fi

echo "[*] Python version:"
python3 --version
echo ""

# Check dependencies
echo "[*] Checking dependencies..."
if ! python3 -c "import requests" 2>/dev/null; then
    echo "ERROR: requests library not found"
    echo "Install with: pip install requests"
    exit 1
fi
echo "✓ requests library available"
echo ""

# Check GitHub token
if [ -z "$GITHUB_TOKEN" ]; then
    echo "WARNING: GITHUB_TOKEN not set"
    echo "Set it with: export GITHUB_TOKEN=<your_token>"
    echo ""
    echo "Get a token at: https://github.com/settings/tokens"
    echo "  Required scopes: public_repo, read:user"
    echo ""
fi

# Phase 2.1: Ingestion
echo "========================================"
echo "PHASE 2.1: GitHub Ingestion"
echo "========================================"
echo ""

if [ -f "$RAW_DIR/github-starred.json" ]; then
    echo "⚠ Raw data already exists: $RAW_DIR/github-starred.json"
    read -p "Overwrite? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Skipping ingestion"
    else
        python3 "$SCRIPT_DIR/github_ingest.py"
    fi
else
    echo "Starting GitHub ingestion..."
    if python3 "$SCRIPT_DIR/github_ingest.py"; then
        echo "✓ Phase 2.1 COMPLETE"
    else
        echo "✗ Phase 2.1 FAILED"
        exit 1
    fi
fi

echo ""
echo "========================================"
echo "PHASE 2.2: Normalization & Deduplication"
echo "========================================"
echo ""

if [ ! -f "$RAW_DIR/github-starred.json" ]; then
    echo "ERROR: Raw data not found. Run Phase 2.1 first."
    exit 1
fi

echo "Starting normalization..."
if python3 "$SCRIPT_DIR/normalize_repos.py"; then
    echo "✓ Phase 2.2 COMPLETE"
else
    echo "✗ Phase 2.2 FAILED"
    exit 1
fi

echo ""
echo "========================================"
echo "VERIFICATION & SUMMARY"
echo "========================================"
echo ""

# Verify output files
if [ -f "$RAW_DIR/github-starred.json" ]; then
    raw_size=$(du -sh "$RAW_DIR/github-starred.json" | cut -f1)
    raw_count=$(python3 -c "import json; data=json.load(open('$RAW_DIR/github-starred.json')); print(data['metadata']['total_repos'])" 2>/dev/null || echo "N/A")
    echo "✓ Raw data: $raw_size ($raw_count repos)"
else
    echo "✗ Raw data not found"
fi

if [ -f "$NORMALIZED_DIR/deduplicated.json" ]; then
    norm_size=$(du -sh "$NORMALIZED_DIR/deduplicated.json" | cut -f1)
    norm_count=$(python3 -c "import json; data=json.load(open('$NORMALIZED_DIR/deduplicated.json')); print(data['metadata']['total_repositories'])" 2>/dev/null || echo "N/A")
    echo "✓ Normalized data: $norm_size ($norm_count repos)"
else
    echo "✗ Normalized data not found"
fi

echo ""
echo "Logs:"
ls -1 "$LOG_DIR"/*.log 2>/dev/null | xargs -I {} bash -c 'echo "  - {}"; tail -3 {} | sed "s/^/    /"' || echo "  No logs found"

echo ""
echo "========================================"
echo "PHASE 2 COMPLETE"
echo "========================================"
echo ""
echo "Outputs:"
echo "  Raw:        $RAW_DIR/github-starred.json"
echo "  Normalized: $NORMALIZED_DIR/deduplicated.json"
echo "  Logs:       $LOG_DIR/"
echo ""
echo "Next steps:"
echo "  Phase 3: Classification (TODO)"
echo "  - Run: python3 classify_repos.py"
echo "  - Output: classified/repos-classified.json"
echo ""
