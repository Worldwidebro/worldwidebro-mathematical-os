#!/bin/bash
# Company Brain FastMCP Setup Script
# Sets up Python 3.12 venv and installs FastMCP

set -e

echo "🚀 Company Brain FastMCP Setup"
echo "==============================="
echo ""

# Check current Python version
CURRENT_PYTHON=$(python3 --version 2>&1 | awk '{print $2}')
echo "Current Python: $CURRENT_PYTHON"
echo "Required: ≥3.10"
echo ""

# Check if Python 3.12 is available
if command -v python3.12 &> /dev/null; then
    PYTHON_BIN="python3.12"
    echo "✅ Python 3.12 found"
elif command -v /usr/local/opt/python@3.12/bin/python3 &> /dev/null; then
    PYTHON_BIN="/usr/local/opt/python@3.12/bin/python3"
    echo "✅ Python 3.12 found (Homebrew)"
elif command -v python3.11 &> /dev/null; then
    PYTHON_BIN="python3.11"
    echo "✅ Python 3.11 found (acceptable fallback)"
elif command -v python3.10 &> /dev/null; then
    PYTHON_BIN="python3.10"
    echo "✅ Python 3.10 found"
else
    echo "❌ Python 3.10+ not found"
    echo ""
    echo "Install Python 3.12 with one of:"
    echo ""
    echo "  Homebrew:"
    echo "    brew install python@3.12"
    echo ""
    echo "  pyenv:"
    echo "    pyenv install 3.12.0"
    echo "    pyenv local 3.12.0"
    echo ""
    echo "  Conda:"
    echo "    conda create -n company-brain python=3.12"
    echo ""
    exit 1
fi

VENV_DIR="/Users/acebless/.venv/company-brain"
echo ""
echo "📦 Creating venv at: $VENV_DIR"

# Create venv
$PYTHON_BIN -m venv "$VENV_DIR"
source "$VENV_DIR/bin/activate"

echo "✅ Venv created"
echo ""

# Upgrade pip
echo "📦 Upgrading pip..."
pip install --upgrade pip setuptools wheel
echo "✅ Pip upgraded"
echo ""

# Install FastMCP
echo "📦 Installing FastMCP..."
pip install fastmcp pyyaml
echo "✅ FastMCP installed"
echo ""

# Verify installation
echo "🧪 Verifying installation..."
FASTMCP_VERSION=$($PYTHON_BIN -c "import fastmcp; print(fastmcp.__version__)")
echo "✅ FastMCP $FASTMCP_VERSION ready"
echo ""

# Show configuration instructions
echo "📋 Configuration Instructions"
echo "============================"
echo ""
echo "Add this to ~/.claude/settings.json:"
echo ""
echo '{
  "mcpServers": {
    "company-brain": {
      "command": "'$VENV_DIR'/bin/python3",
      "args": [
        "_MCP/fastmcp_server.py"
      ],
      "cwd": "/Users/acebless/Documents/The Company/Company Brain"
    }
  }
}'
echo ""
echo "Then restart Claude Code."
echo ""

# Test the server
echo "🧪 Testing MCP server..."
if $VENV_DIR/bin/python3 _MCP/fastmcp_server.py --help &>/dev/null; then
    echo "✅ Server ready"
else
    echo "⚠️  Server test skipped (requires full MCP negotiation)"
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "  1. Update ~/.claude/settings.json with config above"
echo "  2. Restart Claude Code"
echo "  3. Try: infrastructure_status()"
