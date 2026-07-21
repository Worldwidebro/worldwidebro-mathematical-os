#!/bin/bash

# AI Boss OS Tool & Service Health Check
# Purpose: Verify all tools, MCPs, services are installed, running, healthy
# Usage: ./check-tools.sh [--verbose] [--fix] [--category <category>]

VERBOSE=false
FIX=false
CATEGORY=""
TIMESTAMP=$(date +%Y-%m-%d\ %H:%M:%S)

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

HEALTHY=0
UNHEALTHY=0
WARNING=0

while [[ $# -gt 0 ]]; do
  case $1 in
    --verbose) VERBOSE=true; shift ;;
    --fix) FIX=true; shift ;;
    --category) CATEGORY="$2"; shift 2 ;;
    *) shift ;;
  esac
done

echo -e "${BLUE}╔════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║         AI BOSS OS - TOOL & SERVICE HEALTH CHECK           ║${NC}"
echo -e "${BLUE}║                  ${TIMESTAMP}                  ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════╝${NC}"
echo ""

# REPOSITORY INTELLIGENCE
if [ -z "$CATEGORY" ] || [ "$CATEGORY" = "repository_intelligence" ]; then
  echo -e "${BLUE}📚 REPOSITORY INTELLIGENCE LAYER${NC}"
  command -v repomix &>/dev/null && echo -e "  ${GREEN}✓${NC} Repomix" && ((HEALTHY++)) || echo -e "  ${RED}✗${NC} Repomix" && ((UNHEALTHY++))
  command -v serena &>/dev/null && echo -e "  ${GREEN}✓${NC} Serena" && ((HEALTHY++)) || echo -e "  ${RED}✗${NC} Serena" && ((UNHEALTHY++))
  command -v gitnexus &>/dev/null && echo -e "  ${GREEN}✓${NC} GitNexus" && ((HEALTHY++)) || echo -e "  ${RED}✗${NC} GitNexus" && ((UNHEALTHY++))
  echo ""
fi

# AI MODELS
if [ -z "$CATEGORY" ] || [ "$CATEGORY" = "models" ]; then
  echo -e "${BLUE}🧠 AI MODEL LAYER${NC}"
  curl -s http://localhost:4000/health &>/dev/null && echo -e "  ${GREEN}✓${NC} LiteLLM" && ((HEALTHY++)) || echo -e "  ${YELLOW}⚠${NC} LiteLLM" && ((WARNING++))
  command -v ollama &>/dev/null && echo -e "  ${GREEN}✓${NC} Ollama" && ((HEALTHY++)) || echo -e "  ${RED}✗${NC} Ollama" && ((UNHEALTHY++))
  echo ""
fi

# AGENTS
if [ -z "$CATEGORY" ] || [ "$CATEGORY" = "agents" ]; then
  echo -e "${BLUE}🤖 AGENT LAYER${NC}"
  [ -f /Users/acebless/Documents/WORLDWIDEBRO-OS/05-AGENTS/agent_factory.py ] && echo -e "  ${GREEN}✓${NC} Agent Factory" && ((HEALTHY++)) || echo -e "  ${YELLOW}⚠${NC} Agent Factory" && ((WARNING++))
  command -v crewai &>/dev/null && echo -e "  ${GREEN}✓${NC} CrewAI" && ((HEALTHY++)) || echo -e "  ${RED}✗${NC} CrewAI" && ((UNHEALTHY++))
  echo ""
fi

# OBSERVABILITY
if [ -z "$CATEGORY" ] || [ "$CATEGORY" = "observability" ]; then
  echo -e "${BLUE}📊 OBSERVABILITY LAYER${NC}"
  curl -s http://localhost:3003 &>/dev/null && echo -e "  ${GREEN}✓${NC} Langfuse" && ((HEALTHY++)) || echo -e "  ${YELLOW}⚠${NC} Langfuse" && ((WARNING++))
  curl -s http://localhost:9090 &>/dev/null && echo -e "  ${GREEN}✓${NC} Prometheus" && ((HEALTHY++)) || echo -e "  ${YELLOW}⚠${NC} Prometheus" && ((WARNING++))
  curl -s http://localhost:3001 &>/dev/null && echo -e "  ${GREEN}✓${NC} Grafana" && ((HEALTHY++)) || echo -e "  ${YELLOW}⚠${NC} Grafana" && ((WARNING++))
  echo ""
fi

# MEMORY
if [ -z "$CATEGORY" ] || [ "$CATEGORY" = "memory" ]; then
  echo -e "${BLUE}🧠 MEMORY LAYER${NC}"
  curl -s http://localhost:6333/health &>/dev/null && echo -e "  ${GREEN}✓${NC} Qdrant" && ((HEALTHY++)) || echo -e "  ${YELLOW}⚠${NC} Qdrant" && ((WARNING++))
  docker ps 2>/dev/null | grep -q neo4j && echo -e "  ${GREEN}✓${NC} Neo4j" && ((HEALTHY++)) || echo -e "  ${YELLOW}⚠${NC} Neo4j" && ((WARNING++))
  redis-cli ping &>/dev/null && echo -e "  ${GREEN}✓${NC} Redis" && ((HEALTHY++)) || echo -e "  ${YELLOW}⚠${NC} Redis" && ((WARNING++))
  echo ""
fi

# DATA
if [ -z "$CATEGORY" ] || [ "$CATEGORY" = "data" ]; then
  echo -e "${BLUE}💾 DATA LAYER${NC}"
  [ -f /Users/acebless/Documents/worldwidebro_os.duckdb ] && echo -e "  ${GREEN}✓${NC} DuckDB" && ((HEALTHY++)) || echo -e "  ${RED}✗${NC} DuckDB" && ((UNHEALTHY++))
  command -v supabase &>/dev/null && echo -e "  ${GREEN}✓${NC} Supabase CLI" && ((HEALTHY++)) || echo -e "  ${YELLOW}⚠${NC} Supabase CLI" && ((WARNING++))
  echo ""
fi

# AUTOMATION
if [ -z "$CATEGORY" ] || [ "$CATEGORY" = "automation" ]; then
  echo -e "${BLUE}⚙️  AUTOMATION LAYER${NC}"
  curl -s http://localhost:5678 &>/dev/null && echo -e "  ${GREEN}✓${NC} n8n" && ((HEALTHY++)) || echo -e "  ${YELLOW}⚠${NC} n8n" && ((WARNING++))
  echo ""
fi

# SUMMARY
TOTAL=$((HEALTHY + UNHEALTHY + WARNING))
echo -e "${BLUE}╔════════════════════════════════════════════════════════════╗${NC}"
echo -e "║ ${GREEN}✓ Healthy:${NC}    $HEALTHY  ${YELLOW}⚠ Warning:${NC}    $WARNING  ${RED}✗ Unhealthy:${NC}  $UNHEALTHY"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════╝${NC}"

if [ $UNHEALTHY -gt 0 ]; then
  exit 2
elif [ $WARNING -gt 0 ]; then
  exit 1
else
  exit 0
fi
