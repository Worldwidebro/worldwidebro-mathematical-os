#!/bin/bash
# Test Fractal launch script

set -e

echo "🚀 Testing Fractal Agent Spawn..."
echo

# Activate venv
source .fractal-venv/bin/activate

# Test 1: List available nodes
echo "📋 Checking registered Fractal nodes..."
cd /Users/acebless/.fractal/ventures
fractal ls 2>&1 || echo "(No nodes yet)"
echo

# Test 2: View node config
echo "⚙️  Ventures Node Config:"
if [ -f config.json ]; then
  cat config.json | head -20
else
  echo "Config will be generated on first launch"
fi
echo

# Test 3: Show workspace structure
echo "📁 Ventures Workspace Structure:"
ls -la /Users/acebless/.fractal/ventures/ | grep -v ".git"
echo

# Test 4: Display root.md task
echo "📋 Venture Audit Task (root.md):"
head -30 /Users/acebless/.fractal/ventures/root.md
echo

# Test 5: Verify venv
echo "✅ Fractal Version:"
fractal --version
echo

echo "🎯 Ready to launch with: fractal node start"
echo "   (Requires Claude API key in environment)"
