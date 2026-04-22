#!/bin/bash
# ================================================================
# VENTURE REORGANIZATION SCRIPT
# From: Technical folder structure
# To: Legal/Corporate structure (Winners Circle WC Holdings)
# ================================================================

set -e  # Exit on error

echo "🚀 Starting Venture Reorganization..."
echo ""

# Define paths
DOCS_DIR="/Users/acebless/Documents"
HOLDINGS_DIR="$DOCS_DIR/Winners-Circle-WC-Holdings"

# ================================================================
# PHASE 1: Create New Structure
# ================================================================
echo "📁 PHASE 1: Creating new folder structure..."

mkdir -p "$HOLDINGS_DIR/00-Holdings-Board"
mkdir -p "$HOLDINGS_DIR/01-Divisions/Division-1-Beauty-Wellness"
mkdir -p "$HOLDINGS_DIR/01-Divisions/Division-2-Construction-Logistics"
mkdir -p "$HOLDINGS_DIR/01-Divisions/Division-3-Financial-Services"
mkdir -p "$HOLDINGS_DIR/01-Divisions/Division-4-Technology-AI"
mkdir -p "$HOLDINGS_DIR/01-Divisions/Division-5-E-Commerce-Retail"
mkdir -p "$HOLDINGS_DIR/02-Shared-Services"
mkdir -p "$HOLDINGS_DIR/03-Venture-Hub-Inc"
mkdir -p "$HOLDINGS_DIR/04-Capital-Management-LLC"
mkdir -p "$HOLDINGS_DIR/05-Legal-Entity-Docs"
mkdir -p "$HOLDINGS_DIR/06-Code-Repositories"

echo "✅ Holding company structure created"
echo ""

# ================================================================
# PHASE 2: Move Venture Folders
# ================================================================
echo "📦 PHASE 2: Moving venture folders..."

# Beauty & Wellness (BW-001)
if [ -d "$DOCS_DIR/bw-001-lash-extension-studio" ]; then
    mv "$DOCS_DIR/bw-001-lash-extension-studio" "$HOLDINGS_DIR/01-Divisions/Division-1-Beauty-Wellness/BW-001-Lash-Extension-Studio"
    echo "✅ Moved BW-001 (Lash Extension Studio)"
fi

# Construction (CON-001)
if [ -d "$DOCS_DIR/con-001-ace-construction" ]; then
    mv "$DOCS_DIR/con-001-ace-construction" "$HOLDINGS_DIR/01-Divisions/Division-2-Construction-Logistics/CON-001-Ace-Construction"
    echo "✅ Moved CON-001 (Ace Construction)"
fi

# Technology/AI ventures
if [ -d "$DOCS_DIR/autonomous-venture-studio" ]; then
    mv "$DOCS_DIR/autonomous-venture-studio" "$HOLDINGS_DIR/01-Divisions/Division-4-Technology-AI/Autonomous-Venture-Studio"
    echo "✅ Moved Autonomous Venture Studio"
fi

if [ -d "$DOCS_DIR/ai-venture-studio-template" ]; then
    mv "$DOCS_DIR/ai-venture-studio-template" "$HOLDINGS_DIR/01-Divisions/Division-4-Technology-AI/AI-Venture-Studio-Template"
    echo "✅ Moved AI Venture Studio Template"
fi

if [ -d "$DOCS_DIR/iza-os-rag-system" ]; then
    mv "$DOCS_DIR/iza-os-rag-system" "$HOLDINGS_DIR/01-Divisions/Division-4-Technology-AI/IZA-OS-RAG-System"
    echo "✅ Moved IZA OS RAG System"
fi

# E-Commerce
if [ -d "$DOCS_DIR/business-template-marketplace" ]; then
    mv "$DOCS_DIR/business-template-marketplace" "$HOLDINGS_DIR/01-Divisions/Division-5-E-Commerce-Retail/Business-Template-Marketplace"
    echo "✅ Moved Business Template Marketplace"
fi

# Operations (Shared Services)
if [ -d "$DOCS_DIR/venture-hub" ]; then
    mv "$DOCS_DIR/venture-hub" "$HOLDINGS_DIR/03-Venture-Hub-Inc"
    echo "✅ Moved Venture Hub"
fi

if [ -d "$DOCS_DIR/venture-factory-core" ]; then
    mv "$DOCS_DIR/venture-factory-core" "$HOLDINGS_DIR/02-Shared-Services/Venture-Factory-Core"
    echo "✅ Moved Venture Factory Core"
fi

if [ -d "$DOCS_DIR/pitch-kit" ]; then
    mv "$DOCS_DIR/pitch-kit" "$HOLDINGS_DIR/02-Shared-Services/Pitch-Kit"
    echo "✅ Moved Pitch Kit"
fi

if [ -d "$DOCS_DIR/The office" ]; then
    mv "$DOCS_DIR/The office" "$HOLDINGS_DIR/02-Shared-Services/The-Office"
    echo "✅ Moved The Office"
fi

if [ -d "$DOCS_DIR/mcp-dashboard" ]; then
    mv "$DOCS_DIR/mcp-dashboard" "$HOLDINGS_DIR/02-Shared-Services/MCP-Dashboard"
    echo "✅ Moved MCP Dashboard"
fi

if [ -d "$DOCS_DIR/civilization-os-local" ]; then
    mv "$DOCS_DIR/civilization-os-local" "$HOLDINGS_DIR/02-Shared-Services/Civilization-OS-Local"
    echo "✅ Moved Civilization OS Local"
fi

if [ -d "$DOCS_DIR/SecondBrain" ]; then
    mv "$DOCS_DIR/SecondBrain" "$HOLDINGS_DIR/02-Shared-Services/SecondBrain"
    echo "✅ Moved SecondBrain"
fi

if [ -d "$DOCS_DIR/data" ]; then
    mv "$DOCS_DIR/data" "$HOLDINGS_DIR/02-Shared-Services/Data"
    echo "✅ Moved Data"
fi

# Archive
if [ -d "$DOCS_DIR/archive" ]; then
    mv "$DOCS_DIR/archive" "$HOLDINGS_DIR/06-Code-Repositories/Archive"
    echo "✅ Moved Archive"
fi

# Delete (keep only .localized)
if [ -d "$DOCS_DIR/Claude" ]; then
    rm -rf "$DOCS_DIR/Claude"
    echo "✅ Deleted Claude folder (empty)"
fi

echo ""
echo "✅ PHASE 2 complete: All folders moved"
echo ""

# ================================================================
# PHASE 3: Create Legal Entity Subfolders
# ================================================================
echo "📂 PHASE 3: Creating Legal/Financials/Operations subfolders..."

# BW-001
mkdir -p "$HOLDINGS_DIR/01-Divisions/Division-1-Beauty-Wellness/BW-001-Lash-Extension-Studio/Legal"
mkdir -p "$HOLDINGS_DIR/01-Divisions/Division-1-Beauty-Wellness/BW-001-Lash-Extension-Studio/Financials"
mkdir -p "$HOLDINGS_DIR/01-Divisions/Division-1-Beauty-Wellness/BW-001-Lash-Extension-Studio/Operations"
mkdir -p "$HOLDINGS_DIR/01-Divisions/Division-1-Beauty-Wellness/BW-001-Lash-Extension-Studio/Code"

# CON-001
mkdir -p "$HOLDINGS_DIR/01-Divisions/Division-2-Construction-Logistics/CON-001-Ace-Construction/Legal"
mkdir -p "$HOLDINGS_DIR/01-Divisions/Division-2-Construction-Logistics/CON-001-Ace-Construction/Financials"
mkdir -p "$HOLDINGS_DIR/01-Divisions/Division-2-Construction-Logistics/CON-001-Ace-Construction/Operations"
mkdir -p "$HOLDINGS_DIR/01-Divisions/Division-2-Construction-Logistics/CON-001-Ace-Construction/Code"

echo "✅ PHASE 3 complete: Subfolders created"
echo ""

# ================================================================
# PHASE 4: Create Symlinks (Optional)
# ================================================================
echo "🔗 PHASE 4: Creating symlinks for easy access..."

cd "$HOLDINGS_DIR/06-Code-Repositories"

# Remove if exists, then create symlink
if [ -L "bw-001-lash-extension-studio" ]; then
    rm "bw-001-lash-extension-studio"
fi
ln -s "../01-Divisions/Division-1-Beauty-Wellness/BW-001-Lash-Extension-Studio" bw-001-lash-extension-studio
echo "✅ Created symlink for BW-001"

if [ -L "con-001-ace-construction" ]; then
    rm "con-001-ace-construction"
fi
ln -s "../01-Divisions/Division-2-Construction-Logistics/CON-001-Ace-Construction" con-001-ace-construction
echo "✅ Created symlink for CON-001"

echo ""
echo "✅ PHASE 4 complete: Symlinks created"
echo ""

# ================================================================
# COMPLETION
# ================================================================
echo "============================================================"
echo "🎉 REORGANIZATION COMPLETE!"
echo "============================================================"
echo ""
echo "New structure location: $HOLDINGS_DIR"
echo ""
echo "📁 Structure:"
echo "  00-Holdings-Board/          ← Board docs, cap tables"
echo "  01-Divisions/                ← 5 divisions (BW, CON, FIN, TECH, EC)"
echo "  02-Shared-Services/          ← HR, Accounting, Legal, Marketing, IT"
echo "  03-Venture-Hub-Inc/          ← Venture Hub dashboard"
echo "  04-Capital-Management-LLC/   ← FIN-036 function"
echo "  05-Legal-Entity-Docs/        ← All 687 LLC documents"
echo "  06-Code-Repositories/        ← Symlinks to venture code"
echo ""
echo "✅ NEXT STEPS:"
echo "  1. File 7 LLCs with NC Secretary of State"
echo "  2. Obtain 7 EINs from IRS"
echo "  3. Open 7 business bank accounts"
echo "  4. Purchase insurance"
echo "  5. Create operating agreements"
echo ""
echo "📖 Documentation: /Users/acebless/Documents/REORGANIZE-VENTURES.md"
echo ""
