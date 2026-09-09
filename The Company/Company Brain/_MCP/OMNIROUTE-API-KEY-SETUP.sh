#!/bin/bash
# OmniRoute API Key Configuration (DO NOT COMMIT)
# Save this in ~/.zshrc or ~/.bashrc for persistent access

# Set OmniRoute API Key
export OMNIROUTE_API_KEY="sk-89df9958a35a1f3e-a5b3fe-a1b77b99"

# Gateway URL
export OMNIROUTE_BASE_URL="http://100.87.214.70:20128"

# Claude Code Gateway Settings (optional)
export ANTHROPIC_BASE_URL="http://100.87.214.70:20128"
export ANTHROPIC_AUTH_TOKEN="$OMNIROUTE_API_KEY"
export CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY="1"

# Quick Commands
alias omniroute-health="curl -s $OMNIROUTE_BASE_URL/api/health | jq ."
alias omniroute-models="curl -s -H \"Authorization: Bearer $OMNIROUTE_API_KEY\" $OMNIROUTE_BASE_URL/v1/models | jq '.data[] | {id, owned_by}'"
alias omniroute-setup-profiles="omniroute setup-claude --remote $OMNIROUTE_BASE_URL --api-key $OMNIROUTE_API_KEY"
alias omniroute-launch-default="omniroute launch --remote $OMNIROUTE_BASE_URL --api-key $OMNIROUTE_API_KEY"
alias omniroute-launch-glm="omniroute launch --profile glm52 --remote $OMNIROUTE_BASE_URL --api-key $OMNIROUTE_API_KEY"
alias omniroute-launch-kimi="omniroute launch --profile kimi-k27 --remote $OMNIROUTE_BASE_URL --api-key $OMNIROUTE_API_KEY"

echo "✅ OmniRoute configured:"
echo "   API Key: ${OMNIROUTE_API_KEY:0:20}..."
echo "   Base URL: $OMNIROUTE_BASE_URL"
echo ""
echo "Available commands:"
echo "   omniroute-health         # Check gateway health"
echo "   omniroute-models         # List available models"
echo "   omniroute-setup-profiles # Generate Claude Code profiles"
echo "   omniroute-launch-default # Launch Claude Code (auto-detect)"
echo "   omniroute-launch-glm     # Launch with GLM 5.2"
echo "   omniroute-launch-kimi    # Launch with Kimi K2.7"
