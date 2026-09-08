#!/bin/bash

# Phase 1 Deployment Script
# Deploys KG-017/028/048 (Graph API + MCP Tools) to Docker + OmniRoute
# Usage: bash deploy.sh [--build] [--test] [--clean]

set -e

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Paths
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../" && pwd)"
COMPOSE_FILE="$SCRIPT_DIR/docker-compose.yml"

# Options
BUILD_IMAGE=false
RUN_TESTS=false
CLEAN_CONTAINERS=false

# Parse arguments
while [[ $# -gt 0 ]]; do
  case $1 in
    --build) BUILD_IMAGE=true; shift ;;
    --test) RUN_TESTS=true; shift ;;
    --clean) CLEAN_CONTAINERS=true; shift ;;
    *) echo "Unknown option: $1"; exit 1 ;;
  esac
done

echo -e "${GREEN}=== Phase 1 Deployment ===${NC}"
echo "Project Root: $PROJECT_ROOT"
echo "Compose File: $COMPOSE_FILE"
echo ""

# Step 1: Clean (if requested)
if [ "$CLEAN_CONTAINERS" = true ]; then
  echo -e "${YELLOW}Step 1: Cleaning up old containers...${NC}"
  docker-compose -f "$COMPOSE_FILE" down --remove-orphans || true
  sleep 2
fi

# Step 2: Build image (if requested or if not exists)
if [ "$BUILD_IMAGE" = true ]; then
  echo -e "${YELLOW}Step 2: Building Docker image...${NC}"
  docker-compose -f "$COMPOSE_FILE" build --no-cache
else
  echo -e "${YELLOW}Step 2: Building/pulling images...${NC}"
  docker-compose -f "$COMPOSE_FILE" build
fi
echo ""

# Step 3: Start services
echo -e "${YELLOW}Step 3: Starting Graph API service...${NC}"
docker-compose -f "$COMPOSE_FILE" up -d
sleep 3
echo ""

# Step 4: Wait for health check
echo -e "${YELLOW}Step 4: Waiting for service to be healthy...${NC}"
max_retries=10
retry_count=0
while [ $retry_count -lt $max_retries ]; do
  if docker-compose -f "$COMPOSE_FILE" exec -T graph-api curl -s http://localhost:8000/health > /dev/null 2>&1; then
    echo -e "${GREEN}✅ Graph API is healthy${NC}"
    break
  fi
  echo "Waiting for service... ($((retry_count + 1))/$max_retries)"
  sleep 2
  retry_count=$((retry_count + 1))
done

if [ $retry_count -ge $max_retries ]; then
  echo -e "${RED}❌ Service failed to become healthy${NC}"
  docker-compose -f "$COMPOSE_FILE" logs graph-api
  exit 1
fi
echo ""

# Step 5: Verify connectivity
echo -e "${YELLOW}Step 5: Verifying database connectivity...${NC}"
docker-compose -f "$COMPOSE_FILE" exec -T graph-api python -c "
from graph_api import HybridSearchEngine
try:
    engine = HybridSearchEngine()
    engine.close()
    print('✅ Neo4j connected')
except Exception as e:
    print(f'❌ Neo4j connection failed: {e}')
    exit(1)
" || true
echo ""

# Step 6: Run tests (if requested)
if [ "$RUN_TESTS" = true ]; then
  echo -e "${YELLOW}Step 6: Running smoke tests...${NC}"

  # Test 1: Health check
  echo "Test 1: Health check..."
  if curl -s http://localhost:8000/health | grep -q '"status":"OK"'; then
    echo -e "${GREEN}✅ Health check passed${NC}"
  else
    echo -e "${RED}❌ Health check failed${NC}"
    exit 1
  fi

  # Test 2: Hybrid search (if Neo4j is accessible)
  echo "Test 2: Hybrid search endpoint..."
  response=$(curl -s -X POST http://localhost:8000/api/graph/query \
    -H "Authorization: Bearer changeme" \
    -H "Content-Type: application/json" \
    -d '{
      "query_text": "test",
      "search_type": "hybrid",
      "limit": 5
    }')

  if echo "$response" | grep -q '"results"'; then
    echo -e "${GREEN}✅ Hybrid search endpoint working${NC}"
  else
    echo -e "${YELLOW}⚠️ Hybrid search returned: $response${NC}"
  fi

  # Test 3: Context endpoint
  echo "Test 3: Context endpoint..."
  response=$(curl -s -X POST http://localhost:8000/api/graph/context \
    -H "Authorization: Bearer changeme" \
    -H "Content-Type: application/json" \
    -d '{
      "agent_id": "AGT-001",
      "focal_entity_id": "LT-005",
      "depth": 2
    }')

  if echo "$response" | grep -q '"agent_id"'; then
    echo -e "${GREEN}✅ Context endpoint working${NC}"
  else
    echo -e "${YELLOW}⚠️ Context returned: $response${NC}"
  fi

  echo ""
fi

# Step 7: Show service status
echo -e "${YELLOW}Step 7: Service Status${NC}"
docker-compose -f "$COMPOSE_FILE" ps
echo ""

# Step 8: Print next steps
echo -e "${GREEN}=== Deployment Complete ===${NC}"
echo ""
echo "Service is running at: http://localhost:8000"
echo ""
echo "Next steps:"
echo "1. Copy MCP tools to OmniRoute:"
echo "   cp _MCP/hybrid_query_tool.py /path/to/omniroute/tools/"
echo "   cp _MCP/context_assembly_tool.py /path/to/omniroute/tools/"
echo ""
echo "2. Restart OmniRoute to discover new tools"
echo ""
echo "3. Test via OmniRoute:"
echo "   curl http://localhost:20128/tools | grep hybrid_search"
echo "   curl http://localhost:20128/tools | grep agent_context"
echo ""
echo "4. View logs:"
echo "   docker-compose -f $COMPOSE_FILE logs -f graph-api"
echo ""
echo "5. Stop service:"
echo "   docker-compose -f $COMPOSE_FILE down"
echo ""
