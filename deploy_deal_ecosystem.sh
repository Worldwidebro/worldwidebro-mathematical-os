#!/bin/bash
set -e

echo "=========================================="
echo "DEAL ECOSYSTEM — DOCKER DEPLOYMENT"
echo "=========================================="
echo ""

GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

DOCS_DIR="/Users/acebless/Documents"
COMPOSE_FILE="$DOCS_DIR/docker-compose-deal-ecosystem.yml"

echo -e "${BLUE}[1/5] Checking Docker...${NC}"
if ! command -v docker &> /dev/null; then
    echo "❌ Docker not found"
    exit 1
fi
docker ps > /dev/null 2>&1 || {
    echo "❌ Docker daemon not running"
    exit 1
}
echo -e "${GREEN}✅ Docker: $(docker --version)${NC}"
echo ""

echo -e "${BLUE}[2/5] Loading environment...${NC}"
if [ -f "$DOCS_DIR/.env" ]; then
    export $(cat $DOCS_DIR/.env | grep -v '#' | xargs)
    echo -e "${GREEN}✅ Environment loaded${NC}"
fi
echo ""

echo -e "${BLUE}[3/5] Pulling images...${NC}"
docker pull python:3.12-slim
docker pull n8nio/n8n:latest
docker pull postgres:15-alpine
docker pull grafana/grafana:latest
echo -e "${GREEN}✅ Images ready${NC}"
echo ""

echo -e "${BLUE}[4/5] Creating volumes...${NC}"
docker volume create deal-data 2>/dev/null || true
docker volume create grafana-data 2>/dev/null || true
echo -e "${GREEN}✅ Volumes ready${NC}"
echo ""

echo -e "${BLUE}[5/5] Deploying stack...${NC}"
docker-compose -f "$COMPOSE_FILE" down 2>/dev/null || true
docker-compose -f "$COMPOSE_FILE" up -d
echo -e "${GREEN}✅ Deployment complete${NC}"
echo ""

sleep 2
docker-compose -f "$COMPOSE_FILE" ps

echo ""
echo "=========================================="
echo "ENDPOINTS"
echo "=========================================="
echo "  Deal Ecosystem:  http://localhost:8080"
echo "  N8n:             http://localhost:5678"
echo "  Grafana:         http://localhost:3000 (admin/admin)"
echo "  PostgreSQL:      localhost:5432"
echo ""
