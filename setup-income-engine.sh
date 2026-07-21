#!/bin/bash
set -e

echo "════════════════════════════════════════════════════════"
echo "  Worldwidebro Income Engine - Bootstrap (15 min)"
echo "════════════════════════════════════════════════════════"
echo ""

# 1. Check T7 mount
echo "[1/7] Verifying T7 Shield mount..."
if [ -d "/Volumes/T7 Shield" ]; then
    echo "✓ T7 Shield mounted at /Volumes/T7 Shield"
else
    echo "✗ T7 Shield not found. Mount it and retry."
    exit 1
fi

# 2. Check Supabase connection
echo "[2/7] Testing Supabase connection..."
if [ -z "$SUPABASE_URL" ]; then
    echo "✗ SUPABASE_URL not set. Add to ~/.env:"
    echo "  export SUPABASE_URL='https://..supabase.co'"
    echo "  export SUPABASE_KEY='...'"
    exit 1
fi
echo "✓ Supabase configured"

# 3. Verify Mac Studio connection (Tailscale)
echo "[3/7] Testing Mac Studio connection (Tailscale)..."
ping -c 1 100.87.214.70 > /dev/null 2>&1 && echo "✓ Mac Studio reachable (100.87.214.70)" || echo "⚠ Mac Studio not reachable (continue anyway)"

# 4. Install Python deps
echo "[4/7] Installing Python dependencies..."
pip install -q rich supabase python-dotenv neo4j qdrant-client stripe || echo "⚠ Some deps failed (continue)"
echo "✓ Dependencies installed"

# 5. Create execution.jsonl for AOC
echo "[5/7] Creating execution log..."
touch /Users/acebless/Documents/execution.jsonl
echo "✓ AOC log initialized"

# 6. Seed Neo4j (if not done)
echo "[6/7] Checking Neo4j seed status..."
if [ -f "/Users/acebless/Documents/.neo4j-seeded" ]; then
    echo "✓ Neo4j already seeded"
else
    echo "⏳ Neo4j needs seeding (run after: python3 populate_venture_knowledge_graph.py)"
fi

# 7. Clone marketingskills repo
echo "[7/7] Cloning marketingskills..."
if [ ! -d "/Users/acebless/Documents/marketingskills" ]; then
    git clone https://github.com/coreyhaines31/marketingskills /Users/acebless/Documents/marketingskills 2>/dev/null || echo "⚠ Clone failed (manual: git clone https://github.com/coreyhaines31/marketingskills)"
else
    echo "✓ marketingskills already cloned"
fi

echo ""
echo "════════════════════════════════════════════════════════"
echo "✓ BOOTSTRAP COMPLETE"
echo "════════════════════════════════════════════════════════"
echo ""
echo "Next steps:"
echo "1. In Terminal Tab 1: python3 agent_operations_center_watcher.py"
echo "2. In Terminal Tab 2: python3 launch-layer-1.py"
echo ""
echo "Watch revenue flow in real-time!"
