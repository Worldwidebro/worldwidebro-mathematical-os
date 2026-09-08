#!/bin/bash

# DealFlowOS Neo4j API Server Startup Script

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR/.."

echo "Starting DealFlowOS Neo4j API Server..."
echo ""

# Check if server is already running
if lsof -i :8081 > /dev/null 2>&1; then
    echo "⚠️  Port 8081 is already in use. Killing existing process..."
    lsof -i :8081 | grep python3 | awk '{print $2}' | xargs kill -9 2>/dev/null || true
    sleep 1
fi

# Set environment variables
export NEO4J_URI="bolt://100.87.214.70:7687"
export NEO4J_USER="neo4j"
export NEO4J_PASSWORD="ventures2026"

# Start the API server
python3 "_MCP/dealflow_neo4j_api.py"
