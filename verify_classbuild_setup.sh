#!/bin/bash
# Verify ClassBuild is properly installed and configured

echo "🔍 ClassBuild Setup Verification"
echo "================================"

# 1. Check ClassBuild repo
echo ""
echo "1️⃣  ClassBuild Repository"
if [ -d "/tmp/classbuild" ]; then
    echo "   ✅ Found at /tmp/classbuild"
else
    echo "   ❌ Not found. Run:"
    echo "      cd /tmp && git clone https://github.com/jtangen/classbuild.git"
    exit 1
fi

# 2. Check npm installation
echo ""
echo "2️⃣  npm Installation"
if command -v npm &> /dev/null; then
    VERSION=$(npm --version)
    echo "   ✅ npm $VERSION"
else
    echo "   ❌ npm not found"
    exit 1
fi

# 3. Check node_modules
echo ""
echo "3️⃣  ClassBuild Dependencies"
if [ -d "/tmp/classbuild/node_modules" ]; then
    echo "   ✅ Dependencies installed"
else
    echo "   ⚠️  Installing dependencies..."
    cd /tmp/classbuild
    npm install > /dev/null 2>&1
    if [ $? -eq 0 ]; then
        echo "   ✅ Dependencies installed successfully"
    else
        echo "   ❌ npm install failed"
        exit 1
    fi
fi

# 4. Check API keys
echo ""
echo "4️⃣  API Keys"
if [ -n "$ANTHROPIC_API_KEY" ]; then
    KEY_PREVIEW="${ANTHROPIC_API_KEY:0:7}...${ANTHROPIC_API_KEY: -4}"
    echo "   ✅ ANTHROPIC_API_KEY set ($KEY_PREVIEW)"
else
    echo "   ❌ ANTHROPIC_API_KEY not set"
    echo "      Run: export ANTHROPIC_API_KEY=sk-..."
    exit 1
fi

if [ -n "$GEMINI_API_KEY" ]; then
    KEY_PREVIEW="${GEMINI_API_KEY:0:7}...${GEMINI_API_KEY: -4}"
    echo "   ✅ GEMINI_API_KEY set ($KEY_PREVIEW) [audio + infographics enabled]"
else
    echo "   ⚠️  GEMINI_API_KEY not set (audio + infographics disabled)"
    echo "      Optional: export GEMINI_API_KEY=..."
fi

# 5. Check configuration file
echo ""
echo "5️⃣  Configuration"
if [ -f "$HOME/Documents/classbuild_ventures.json" ]; then
    COUNT=$(jq 'length' "$HOME/Documents/classbuild_ventures.json")
    echo "   ✅ Found classbuild_ventures.json ($COUNT ventures)"
else
    echo "   ❌ classbuild_ventures.json not found"
    exit 1
fi

# 6. Check scripts
echo ""
echo "6️⃣  Generator Scripts"
for script in classbuild_venture_generator.sh classbuild_batch_generator.py; do
    if [ -f "$HOME/Documents/$script" ]; then
        echo "   ✅ $script"
    else
        echo "   ❌ $script not found"
    fi
done

# 7. Test run (optional)
echo ""
echo "7️⃣  Ready to Generate"
echo ""
echo "✅ All systems ready!"
echo ""
echo "To generate a course, run:"
echo "   ~/Documents/classbuild_venture_generator.sh EDU-023-Cybersecurity-Bootcamp 'Cybersecurity Bootcamp'"
echo ""
echo "To generate all 10 courses, run:"
echo "   python3 ~/Documents/classbuild_batch_generator.py"
