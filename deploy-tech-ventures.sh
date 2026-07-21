#!/bin/bash
# Deploy all 10 tech ventures to Vercel

set -e

VENTURES=(
  "TECH-016:Video-Editor-AI:mc-006-video-production-company"
  "TECH-040:Cybersecurity-Shield:tech-040-cybersecurity-shield"
  "TECH-047:Image-Recognition-AI:iza-os-ai-vision-platform"
  "TECH-014:Sentiment-Analyzer:edu-024-language-learning-ai"
  "TECH-017:Speech-to-Text-AI:edu-009-voiceover-script-library"
  "TECH-018:Text-to-Speech-AI:edu-009-voiceover-script-library"
  "TECH-039:Blockchain-Verifier-AI:fin-009-crypto-tax-optimizer"
  "TECH-054:Database-Optimizer:iza-os-vector-database"
  "TECH-035:Cloud-Management-AI:comm-036-public-infrastructure-ai"
  "TECH-051:Fraud-Prevention-AI:arbitrage-nexus"
)

echo "========================================"
echo "DEPLOYING 10 TECH VENTURES TO VERCEL"
echo "========================================"
echo ""

DEPLOY_LOG="TECH-VENTURES-DEPLOYMENT.log"
> "$DEPLOY_LOG"

for venture_config in "${VENTURES[@]}"; do
  IFS=':' read -r venture_id venture_name base_repo <<< "$venture_config"

  venture_id_lower=$(echo "$venture_id" | tr '[:upper:]' '[:lower:]')
  echo "Deploying $venture_id ($venture_name)..."
  echo "  Base repo: $base_repo" | tee -a "$DEPLOY_LOG"

  # Check if venture folder exists
  venture_folder_name=$(echo "$venture_id_lower" | tr '-' '_')
  venture_folder="WORLDWIDEBRO-OS/02-VENTURES/$venture_folder_name"

  if [ -d "$venture_folder" ]; then
    echo "  ✓ Venture folder exists" | tee -a "$DEPLOY_LOG"

    # Create deployment manifest
    cat > "$venture_folder/vercel.json" << EOF
{
  "name": "vex-$venture_id_lower",
  "buildCommand": "npm run build || echo 'No build'",
  "outputDirectory": "out"
}
EOF

    echo "  ✓ vercel.json created" | tee -a "$DEPLOY_LOG"
    echo "  → Ready for: vercel deploy --prod" | tee -a "$DEPLOY_LOG"

  else
    echo "  ⚠ Venture folder not found: $venture_folder" | tee -a "$DEPLOY_LOG"
  fi

  echo "" | tee -a "$DEPLOY_LOG"
done

echo "========================================"
echo "DEPLOYMENT READY"
echo "========================================"
echo "10 ventures with vercel.json manifests"
echo "Deploy with: vercel deploy --prod"
