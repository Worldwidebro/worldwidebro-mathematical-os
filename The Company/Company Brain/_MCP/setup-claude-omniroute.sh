#!/bin/bash
# Claude Code ↔ OmniRoute Gateway Setup Script
# Wires Claude Code to local OmniRoute (100.87.214.70:20128)

set -e

echo "🚀 Claude Code ↔ OmniRoute Integration Setup"
echo "=============================================="
echo ""

# Step 1: Verify OmniRoute running
echo "Step 1: Verifying OmniRoute running..."
if ! curl -s http://100.87.214.70:20128/api/health > /dev/null 2>&1; then
  echo "❌ OmniRoute not responding at http://100.87.214.70:20128"
  echo "   Start OmniRoute first: docker --context macstudio ps | grep omniroute"
  exit 1
fi
echo "✅ OmniRoute health check passed"
echo ""

# Step 2: Check API key
echo "Step 2: Checking OMNIROUTE_API_KEY..."
if [ -z "$OMNIROUTE_API_KEY" ]; then
  echo "⚠️  OMNIROUTE_API_KEY not set"
  echo "   Export it: export OMNIROUTE_API_KEY='oma_live_xxx...'"
  echo "   Or use: omniroute connect http://100.87.214.70:20128"
else
  echo "✅ OMNIROUTE_API_KEY is set (${OMNIROUTE_API_KEY:0:20}...)"
fi
echo ""

# Step 3: Generate profiles
echo "Step 3: Generating Claude Code profiles..."
if command -v omniroute &> /dev/null; then
  echo "   Running: omniroute setup-claude --remote http://100.87.214.70:20128"
  omniroute setup-claude --remote http://100.87.214.70:20128 --dry-run
  echo "   (dry-run) Run without --dry-run to write profiles"
  echo ""

  # Actual setup
  read -p "   Write profiles to ~/.claude/profiles/? (y/N) " -n 1 -r
  echo
  if [[ $REPLY =~ ^[Yy]$ ]]; then
    omniroute setup-claude --remote http://100.87.214.70:20128
    echo "✅ Profiles created at ~/.claude/profiles/"
  fi
else
  echo "❌ omniroute CLI not found"
  echo "   Install: npm install -g omniroute"
  exit 1
fi
echo ""

# Step 4: List available profiles
echo "Step 4: Available profiles:"
if [ -d ~/.claude/profiles ]; then
  ls -1 ~/.claude/profiles | sed 's/^/   ✓ /'
else
  echo "   (no profiles yet — run setup-claude above)"
fi
echo ""

# Step 5: Environment setup
echo "Step 5: Environment variables for ~/.zshrc:"
echo "   export ANTHROPIC_BASE_URL='http://100.87.214.70:20128'"
echo "   export CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY='1'"
echo "   export ANTHROPIC_AUTH_TOKEN='$OMNIROUTE_API_KEY'"
echo ""

# Step 6: Launch options
echo "Step 6: Launch Claude Code via OmniRoute:"
echo ""
echo "   Option A: Auto-detect (requires omniroute connect first)"
echo "   $ omniroute launch"
echo ""
echo "   Option B: Launch with specific model"
echo "   $ omniroute launch --profile glm52"
echo "   $ omniroute launch --profile kimi-k27"
echo ""
echo "   Option C: Manual environment setup"
echo "   $ export ANTHROPIC_BASE_URL='http://100.87.214.70:20128'"
echo "   $ export ANTHROPIC_AUTH_TOKEN='$OMNIROUTE_API_KEY'"
echo "   $ export CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY='1'"
echo "   $ claude"
echo ""

echo "=============================================="
echo "✅ Setup complete!"
echo ""
echo "Next: omniroute launch --profile <model>"
echo "      (or pick a model from ~/.claude/profiles/)"
