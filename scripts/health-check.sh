#!/usr/bin/env bash
set -euo pipefail

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

PASSED=0
FAILED=0

check() {
    local name=$1
    local port=$2
    local path=${3:-/}

    if curl -sf "http://localhost:$port$path" >/dev/null 2>&1; then
        echo -e "${GREEN}[✓]${NC} $name (localhost:$port)"
        ((PASSED++))
    else
        echo -e "${RED}[✗]${NC} $name (localhost:$port)"
        ((FAILED++))
    fi
}

echo ""
echo -e "${BLUE}AI BOSS OS - Health Check${NC}"
echo ""

check "Neo4j Browser" "7474"
check "Qdrant HTTP" "6333"
check "Grafana UI" "3001" "/api/health"
check "LiteLLM" "4000" "/health/liveliness"
check "Langfuse" "3003" "/api/public/health"
check "Prometheus" "9090" "/-/healthy"
check "n8n" "5678" "/healthz"

echo ""
TOTAL=$((PASSED + FAILED))
if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}✅ ALL CHECKS PASSED ($PASSED/$TOTAL)${NC}"
    exit 0
else
    echo -e "${YELLOW}⚠️  $FAILED CHECKS FAILED ($PASSED/$TOTAL)${NC}"
    exit 1
fi
