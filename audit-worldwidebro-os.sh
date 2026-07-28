#!/bin/bash

# ════════════════════════════════════════════════════════════════════════════
# WORLDWIDEBRO OS COMPLETE AUDIT
# Outputs: ONE report file with all findings
# Run: ./audit-worldwidebro-os.sh
# ════════════════════════════════════════════════════════════════════════════

set -e

REPORT_FILE="AUDIT-WORLDWIDEBRO-OS-$(date +%Y%m%d_%H%M%S).txt"

echo "════════════════════════════════════════════════════════════════════════════" | tee "$REPORT_FILE"
echo "WORLDWIDEBRO OS COMPLETE AUDIT" | tee -a "$REPORT_FILE"
echo "Generated: $(date)" | tee -a "$REPORT_FILE"
echo "════════════════════════════════════════════════════════════════════════════" | tee -a "$REPORT_FILE"

# ════════════════════════════════════════════════════════════════════════════
# 1. INFRASTRUCTURE STATUS
# ════════════════════════════════════════════════════════════════════════════

echo "" | tee -a "$REPORT_FILE"
echo "═══ 1. INFRASTRUCTURE STATUS ═══" | tee -a "$REPORT_FILE"
echo "Checking Docker services..." | tee -a "$REPORT_FILE"

if command -v docker &> /dev/null; then
  echo "" | tee -a "$REPORT_FILE"
  echo "Docker containers:" | tee -a "$REPORT_FILE"
  docker ps --format "{{.Names}}\t{{.Status}}" 2>/dev/null | tee -a "$REPORT_FILE" || echo "Docker not running" | tee -a "$REPORT_FILE"

  echo "" | tee -a "$REPORT_FILE"
  echo "Service health checks:" | tee -a "$REPORT_FILE"

  # Postgres
  echo -n "PostgreSQL: " | tee -a "$REPORT_FILE"
  psql -h localhost -U postgres -d ventures -c "SELECT 1;" &>/dev/null && echo "✅ ALIVE" | tee -a "$REPORT_FILE" || echo "❌ DOWN" | tee -a "$REPORT_FILE"

  # Neo4j
  echo -n "Neo4j: " | tee -a "$REPORT_FILE"
  curl -s http://localhost:7474 &>/dev/null && echo "✅ ALIVE" | tee -a "$REPORT_FILE" || echo "❌ DOWN" | tee -a "$REPORT_FILE"

  # Redis
  echo -n "Redis: " | tee -a "$REPORT_FILE"
  redis-cli ping &>/dev/null && echo "✅ ALIVE" | tee -a "$REPORT_FILE" || echo "❌ DOWN" | tee -a "$REPORT_FILE"

  # Qdrant
  echo -n "Qdrant: " | tee -a "$REPORT_FILE"
  curl -s http://localhost:6333/health &>/dev/null && echo "✅ ALIVE" | tee -a "$REPORT_FILE" || echo "❌ DOWN" | tee -a "$REPORT_FILE"

  # Langfuse
  echo -n "Langfuse: " | tee -a "$REPORT_FILE"
  curl -s http://localhost:3003 &>/dev/null && echo "✅ ALIVE" | tee -a "$REPORT_FILE" || echo "❌ DOWN" | tee -a "$REPORT_FILE"
else
  echo "Docker not installed" | tee -a "$REPORT_FILE"
fi

# ════════════════════════════════════════════════════════════════════════════
# 2. LIVE DATA: Ventures, Knowledge Graph, Skill Registry
# ════════════════════════════════════════════════════════════════════════════

echo "" | tee -a "$REPORT_FILE"
echo "═══ 2. LIVE DATA STATUS ═══" | tee -a "$REPORT_FILE"

# Ventures
echo "" | tee -a "$REPORT_FILE"
echo "Ventures in Supabase:" | tee -a "$REPORT_FILE"
psql -h localhost -U postgres -d ventures -c "SELECT COUNT(*) as total_ventures FROM ventures;" 2>/dev/null | tee -a "$REPORT_FILE" || echo "PostgreSQL not accessible" | tee -a "$REPORT_FILE"

echo "" | tee -a "$REPORT_FILE"
echo "Ventures by sector:" | tee -a "$REPORT_FILE"
psql -h localhost -U postgres -d ventures -c "SELECT sector, COUNT(*) as count FROM ventures GROUP BY sector ORDER BY count DESC;" 2>/dev/null | tee -a "$REPORT_FILE" || echo "Query failed" | tee -a "$REPORT_FILE"

echo "" | tee -a "$REPORT_FILE"
echo "Ventures by stage:" | tee -a "$REPORT_FILE"
psql -h localhost -U postgres -d ventures -c "SELECT stage, COUNT(*) as count FROM ventures GROUP BY stage ORDER BY count DESC;" 2>/dev/null | tee -a "$REPORT_FILE" || echo "Query failed" | tee -a "$REPORT_FILE"

# Neo4j
echo "" | tee -a "$REPORT_FILE"
echo "Knowledge Graph (Neo4j):" | tee -a "$REPORT_FILE"
curl -s -u neo4j:ventures2026 http://localhost:7474/db/data/cypher -X POST \
  -H "Content-Type: application/json" \
  -d '{"query":"MATCH (n) RETURN COUNT(n) as node_count LIMIT 1"}' 2>/dev/null | tee -a "$REPORT_FILE" || echo "Neo4j not accessible" | tee -a "$REPORT_FILE"

# Qdrant
echo "" | tee -a "$REPORT_FILE"
echo "Vector Database (Qdrant):" | tee -a "$REPORT_FILE"
curl -s http://localhost:6333/collections 2>/dev/null | tee -a "$REPORT_FILE" || echo "Qdrant not accessible" | tee -a "$REPORT_FILE"

# ════════════════════════════════════════════════════════════════════════════
# 3. CODE INVENTORY
# ════════════════════════════════════════════════════════════════════════════

echo "" | tee -a "$REPORT_FILE"
echo "═══ 3. CODE INVENTORY ═══" | tee -a "$REPORT_FILE"

echo "" | tee -a "$REPORT_FILE"
echo "Agent implementations:" | tee -a "$REPORT_FILE"
find . -type f -name "agent*.py" 2>/dev/null | wc -l | xargs echo "  Python:" | tee -a "$REPORT_FILE"
find . -type f -name "agent*.ts" -o -name "agent*.js" 2>/dev/null | wc -l | xargs echo "  TypeScript/JS:" | tee -a "$REPORT_FILE"

echo "" | tee -a "$REPORT_FILE"
echo "Skill implementations:" | tee -a "$REPORT_FILE"
find . -type f -name "*skill*.py" 2>/dev/null | wc -l | xargs echo "  Python:" | tee -a "$REPORT_FILE"
find . -type f -name "*skill*.ts" -o -name "*skill*.js" 2>/dev/null | wc -l | xargs echo "  TypeScript/JS:" | tee -a "$REPORT_FILE"

echo "" | tee -a "$REPORT_FILE"
echo "Command implementations:" | tee -a "$REPORT_FILE"
find . -type f -name "command*.py" 2>/dev/null | wc -l | xargs echo "  Python:" | tee -a "$REPORT_FILE"
find . -type f -name "command*.ts" -o -name "command*.js" 2>/dev/null | wc -l | xargs echo "  TypeScript/JS:" | tee -a "$REPORT_FILE"

echo "" | tee -a "$REPORT_FILE"
echo "Gemini code (business OS):" | tee -a "$REPORT_FILE"
find Gemini -type f \( -name "*.py" -o -name "*.ts" -o -name "*.js" \) 2>/dev/null | wc -l | xargs echo "  Files:" | tee -a "$REPORT_FILE"

echo "" | tee -a "$REPORT_FILE"
echo "Civilization code (infrastructure OS):" | tee -a "$REPORT_FILE"
find Civilization -type f \( -name "*.py" -o -name "*.ts" -o -name "*.js" \) 2>/dev/null | wc -l | xargs echo "  Files:" | tee -a "$REPORT_FILE"

echo "" | tee -a "$REPORT_FILE"
echo "Agent framework (.agents/skills):" | tee -a "$REPORT_FILE"
ls -d .agents/skills/*/ 2>/dev/null | wc -l | xargs echo "  Skill folders:" | tee -a "$REPORT_FILE"

# ════════════════════════════════════════════════════════════════════════════
# 4. CONFIGURATION & REGISTRY
# ════════════════════════════════════════════════════════════════════════════

echo "" | tee -a "$REPORT_FILE"
echo "═══ 4. CONFIGURATION & REGISTRY ═══" | tee -a "$REPORT_FILE"

echo "" | tee -a "$REPORT_FILE"
echo "Registered agents (Gemini/registry/agents.yaml):" | tee -a "$REPORT_FILE"
if [ -f "Gemini/registry/agents.yaml" ]; then
  grep -c "^  - " Gemini/registry/agents.yaml 2>/dev/null || echo "0" | tee -a "$REPORT_FILE"
else
  echo "File not found" | tee -a "$REPORT_FILE"
fi

echo "" | tee -a "$REPORT_FILE"
echo "Registered MCPs (MCP_REGISTRY.json):" | tee -a "$REPORT_FILE"
if [ -f "MCP_REGISTRY.json" ]; then
  jq '.mcps | length' MCP_REGISTRY.json 2>/dev/null || echo "Invalid JSON" | tee -a "$REPORT_FILE"
else
  echo "File not found" | tee -a "$REPORT_FILE"
fi

echo "" | tee -a "$REPORT_FILE"
echo "Tool capability map entries:" | tee -a "$REPORT_FILE"
if [ -f "TOOL_CAPABILITY_MAP.md" ]; then
  grep -c "^##" TOOL_CAPABILITY_MAP.md 2>/dev/null || echo "0" | tee -a "$REPORT_FILE"
else
  echo "File not found" | tee -a "$REPORT_FILE"
fi

echo "" | tee -a "$REPORT_FILE"
echo "Skill index entries:" | tee -a "$REPORT_FILE"
if [ -f "SKILL-INDEX.md" ]; then
  wc -l < SKILL-INDEX.md | tee -a "$REPORT_FILE"
else
  echo "File not found" | tee -a "$REPORT_FILE"
fi

# ════════════════════════════════════════════════════════════════════════════
# 5. STORAGE & DISK USAGE
# ════════════════════════════════════════════════════════════════════════════

echo "" | tee -a "$REPORT_FILE"
echo "═══ 5. STORAGE & DISK USAGE ═══" | tee -a "$REPORT_FILE"

echo "" | tee -a "$REPORT_FILE"
echo "Disk available:" | tee -a "$REPORT_FILE"
df -h /Users/acebless | tail -1 | tee -a "$REPORT_FILE"

echo "" | tee -a "$REPORT_FILE"
echo "Top folders by size:" | tee -a "$REPORT_FILE"
du -sh */ 2>/dev/null | sort -hr | head -20 | tee -a "$REPORT_FILE"

echo "" | tee -a "$REPORT_FILE"
echo "Large files (>100MB):" | tee -a "$REPORT_FILE"
find . -type f -size +100M 2>/dev/null | head -20 | tee -a "$REPORT_FILE"

echo "" | tee -a "$REPORT_FILE"
echo "node_modules size:" | tee -a "$REPORT_FILE"
du -sh node_modules 2>/dev/null | tee -a "$REPORT_FILE" || echo "Not found" | tee -a "$REPORT_FILE"

# ════════════════════════════════════════════════════════════════════════════
# 6. GIT STATUS
# ════════════════════════════════════════════════════════════════════════════

echo "" | tee -a "$REPORT_FILE"
echo "═══ 6. GIT STATUS ═══" | tee -a "$REPORT_FILE"

echo "" | tee -a "$REPORT_FILE"
echo "Current branch:" | tee -a "$REPORT_FILE"
git branch --show-current 2>/dev/null | tee -a "$REPORT_FILE"

echo "" | tee -a "$REPORT_FILE"
echo "Recent commits:" | tee -a "$REPORT_FILE"
git log --oneline -10 2>/dev/null | tee -a "$REPORT_FILE"

echo "" | tee -a "$REPORT_FILE"
echo "Uncommitted changes:" | tee -a "$REPORT_FILE"
git status --short 2>/dev/null | wc -l | xargs echo "  Modified files:" | tee -a "$REPORT_FILE"

echo "" | tee -a "$REPORT_FILE"
echo "All branches:" | tee -a "$REPORT_FILE"
git branch -a 2>/dev/null | tee -a "$REPORT_FILE"

echo "" | tee -a "$REPORT_FILE"
echo "Remotes:" | tee -a "$REPORT_FILE"
git remote -v 2>/dev/null | tee -a "$REPORT_FILE"

# ════════════════════════════════════════════════════════════════════════════
# 7. GITNEXUS INDEX STATUS
# ════════════════════════════════════════════════════════════════════════════

echo "" | tee -a "$REPORT_FILE"
echo "═══ 7. GITNEXUS INDEX STATUS ═══" | tee -a "$REPORT_FILE"

if command -v node &> /dev/null && [ -f ".gitnexus/run.cjs" ]; then
  echo "" | tee -a "$REPORT_FILE"
  node .gitnexus/run.cjs status 2>/dev/null | tee -a "$REPORT_FILE" || echo "GitNexus not ready" | tee -a "$REPORT_FILE"
else
  echo "GitNexus not installed" | tee -a "$REPORT_FILE"
fi

# ════════════════════════════════════════════════════════════════════════════
# 8. REPOSITORY CLONE STATUS
# ════════════════════════════════════════════════════════════════════════════

echo "" | tee -a "$REPORT_FILE"
echo "═══ 8. LOCALLY CLONED REPOS ═══" | tee -a "$REPORT_FILE"

echo "" | tee -a "$REPORT_FILE"
echo "Git repos in current directory:" | tee -a "$REPORT_FILE"
find . -maxdepth 2 -type d -name ".git" 2>/dev/null | cut -d/ -f2 | sort | uniq | tee -a "$REPORT_FILE"

# ════════════════════════════════════════════════════════════════════════════
# 9. SUMMARY
# ════════════════════════════════════════════════════════════════════════════

echo "" | tee -a "$REPORT_FILE"
echo "════════════════════════════════════════════════════════════════════════════" | tee -a "$REPORT_FILE"
echo "AUDIT COMPLETE" | tee -a "$REPORT_FILE"
echo "Report saved to: $REPORT_FILE" | tee -a "$REPORT_FILE"
echo "════════════════════════════════════════════════════════════════════════════" | tee -a "$REPORT_FILE"

# Print summary
echo ""
echo "✅ Audit complete!"
echo "📄 Report: $REPORT_FILE"
echo ""
echo "Next steps:"
echo "  1. cat $REPORT_FILE"
echo "  2. Copy & paste report content here"
echo "  3. We'll analyze what exists vs what needs building"
echo ""
