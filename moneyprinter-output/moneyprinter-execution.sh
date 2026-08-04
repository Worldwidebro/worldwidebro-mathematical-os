#!/bin/bash
# Auto-generated MoneyPrinterTurbo Construction Ventures Batch
# Generated: 2026-06-05T11:55:26.957235

set -e

MONEYPRINTER_PATH="/path/to/MoneyPrinterTurbo"
CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/configs"
LOG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/logs"

# Create log directory
mkdir -p "$LOG_DIR"

echo "🎬 MoneyPrinterTurbo Construction Ventures - Batch Start"
echo "Generated at: $(date)"
echo "Config directory: $CONFIG_DIR"
echo ""

echo "[1/8] Processing: 5 Home Renovation Mistakes to Avoid (Venture: N/A)"

cd "$MONEYPRINTER_PATH"
python src/main.py --config "$CONFIG_DIR/CON-008_5_Home_Renovation_Mistakes_to_Avoid_20260605_115526.json" 2>&1 | tee "$LOG_DIR/CON-008_5_Home_Renovation_Mistakes_to_Avoid_20260605_115526.log"

echo "[2/8] Processing: Budget Kitchen Renovation Under $5000 (Venture: N/A)"

cd "$MONEYPRINTER_PATH"
python src/main.py --config "$CONFIG_DIR/CON-008_Budget_Kitchen_Renovation_Under_$5000_20260605_115526.json" 2>&1 | tee "$LOG_DIR/CON-008_Budget_Kitchen_Renovation_Under_$5000_20260605_115526.log"

echo "[3/8] Processing: Bathroom Renovation Ideas 2024 (Venture: N/A)"

cd "$MONEYPRINTER_PATH"
python src/main.py --config "$CONFIG_DIR/CON-008_Bathroom_Renovation_Ideas_2024_20260605_115526.json" 2>&1 | tee "$LOG_DIR/CON-008_Bathroom_Renovation_Ideas_2024_20260605_115526.log"

echo "[4/8] Processing: Signs Your Roof Needs Replacement (Venture: N/A)"

cd "$MONEYPRINTER_PATH"
python src/main.py --config "$CONFIG_DIR/CON-009_Signs_Your_Roof_Needs_Replacement_20260605_115526.json" 2>&1 | tee "$LOG_DIR/CON-009_Signs_Your_Roof_Needs_Replacement_20260605_115526.log"

echo "[5/8] Processing: Metal vs Asphalt Shingles: Which is Better? (Venture: N/A)"

cd "$MONEYPRINTER_PATH"
python src/main.py --config "$CONFIG_DIR/CON-009_Metal_vs_Asphalt_Shingles:_Which_is_Better?_20260605_115526.json" 2>&1 | tee "$LOG_DIR/CON-009_Metal_vs_Asphalt_Shingles:_Which_is_Better?_20260605_115526.log"

echo "[6/8] Processing: DIY Plumbing Fixes You Can Do Yourself (Venture: N/A)"

cd "$MONEYPRINTER_PATH"
python src/main.py --config "$CONFIG_DIR/CON-010_DIY_Plumbing_Fixes_You_Can_Do_Yourself_20260605_115526.json" 2>&1 | tee "$LOG_DIR/CON-010_DIY_Plumbing_Fixes_You_Can_Do_Yourself_20260605_115526.log"

echo "[7/8] Processing: Home Electrical Safety Checklist (Venture: N/A)"

cd "$MONEYPRINTER_PATH"
python src/main.py --config "$CONFIG_DIR/CON-011_Home_Electrical_Safety_Checklist_20260605_115526.json" 2>&1 | tee "$LOG_DIR/CON-011_Home_Electrical_Safety_Checklist_20260605_115526.log"

echo "[8/8] Processing: How Often Should You Service Your HVAC? (Venture: N/A)"

cd "$MONEYPRINTER_PATH"
python src/main.py --config "$CONFIG_DIR/CON-012_How_Often_Should_You_Service_Your_HVAC?_20260605_115526.json" 2>&1 | tee "$LOG_DIR/CON-012_How_Often_Should_You_Service_Your_HVAC?_20260605_115526.log"

echo ""
echo "✅ All videos generated successfully!"
echo "Output directory: ./videos"
echo "Logs: $LOG_DIR"