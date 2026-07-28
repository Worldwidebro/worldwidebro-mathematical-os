#!/bin/bash
# Setup BrowserClaw MCP Server

set -e

echo "🔧 Setting up BrowserClaw MCP Server..."

# Create venv
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -q -r requirements.txt

# Setup env
if [ ! -f .env ]; then
  cp .env.example .env
  echo "✅ Created .env (update with your BrowserClaw API key)"
else
  echo "✅ .env already exists"
fi

# Verify
echo "🧪 Testing MCP server..."
python3 -c "from mcp.server import Server; print('✅ MCP SDK available')"

echo "✅ Setup complete!"
echo ""
echo "Next:"
echo "1. Edit .env with your BrowserClaw endpoint + API key"
echo "2. Add to ~/.claude/mcp-config.json (see README.md)"
echo "3. Restart Claude Code"
echo ""
echo "Or run standalone: python server.py"
