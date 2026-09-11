#!/bin/bash
# Render + n8n Self-Hosted Setup Script
# Sets up Render CLI and deploys n8n instance to Render

set -e

echo "=== Render + n8n Self-Hosted Setup ==="
echo ""

# 1. Install Render CLI
echo "1. Installing Render CLI..."
if ! command -v render &> /dev/null; then
    if [[ "$OSTYPE" == "darwin"* ]]; then
        brew install render
    else
        curl -fsSL https://raw.githubusercontent.com/render-oss/cli/refs/heads/main/bin/install.sh | sh
    fi
    echo "✓ Render CLI installed"
else
    echo "✓ Render CLI already installed: $(render --version)"
fi

echo ""
echo "2. Authenticating with Render..."
echo "   Run: render login"
echo "   (This will open your browser for authorization)"
echo ""
read -p "   Have you run 'render login'? (y/n) " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "✓ Render CLI authenticated"
else
    echo "Please run 'render login' first, then re-run this script"
    exit 1
fi

echo ""
echo "3. Checking Render workspace..."
render workspaces --output text

echo ""
echo "4. To deploy n8n:"
echo "   - A render.yaml blueprint is available at: _INFRASTRUCTURE/render-n8n-blueprint.yaml"
echo "   - Or deploy manually:"
echo "     render services create --from-repo https://github.com/n8n-io/n8n --name n8n-self-hosted"
echo ""
echo "5. To view logs:"
echo "   render services"
echo "   (Select the n8n service to see live logs)"
echo ""
echo "=== Setup Complete ==="
