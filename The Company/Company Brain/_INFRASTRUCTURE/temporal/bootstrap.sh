#!/bin/bash

# Temporal Bootstrap Script for LT-005
# Starts Temporal stack, creates namespace, and initializes workflow environment

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
NAMESPACE="lt-005-audit"
TASK_QUEUE="HIPAA_AUDIT_TASK_QUEUE"

echo ""
echo "═══════════════════════════════════════════════════════════"
echo "  Temporal Bootstrap for LT-005"
echo "═══════════════════════════════════════════════════════════"
echo ""

# Step 1: Check Docker
echo "📦 Checking Docker installation..."
if ! command -v docker &> /dev/null; then
    echo "❌ Docker not found. Please install Docker first."
    exit 1
fi
echo "✅ Docker found: $(docker --version)"

# Step 2: Start Docker services
echo ""
echo "🚀 Starting Temporal stack..."
cd "$PROJECT_ROOT"

if docker-compose -f temporal-docker-compose.yml ps | grep -q "Up"; then
    echo "ℹ️  Services already running"
else
    docker-compose -f temporal-docker-compose.yml up -d
    echo "✅ Services started"
fi

# Step 3: Wait for services to be healthy
echo ""
echo "⏳ Waiting for services to be healthy..."
max_attempts=30
attempt=0

while [ $attempt -lt $max_attempts ]; do
    if docker-compose -f temporal-docker-compose.yml ps | grep "Up" > /dev/null; then
        # Check Temporal server health
        if curl -s http://localhost:6939/health > /dev/null 2>&1; then
            echo "✅ Temporal server is healthy"
            break
        fi
    fi
    
    echo "   (attempt $(($attempt + 1))/$max_attempts)"
    sleep 1
    attempt=$((attempt + 1))
done

if [ $attempt -eq $max_attempts ]; then
    echo "❌ Services did not become healthy. Check logs:"
    echo "   docker-compose -f temporal-docker-compose.yml logs"
    exit 1
fi

# Step 4: Create namespace
echo ""
echo "🔧 Setting up namespace..."

if command -v temporal &> /dev/null; then
    # Check if namespace exists
    if temporal namespace describe --namespace "$NAMESPACE" &> /dev/null; then
        echo "ℹ️  Namespace '$NAMESPACE' already exists"
    else
        temporal namespace create --name "$NAMESPACE" --description "LT-005 HealthRoute Audit Workflows"
        echo "✅ Namespace created: $NAMESPACE"
    fi
else
    echo "⚠️  Temporal CLI not found. Namespace creation skipped."
    echo "   Create manually at: http://localhost:8080"
fi

# Step 5: Install SDK dependencies
echo ""
echo "📚 Installing workflow dependencies..."
cd "$SCRIPT_DIR/workflows"

if [ -d "node_modules" ]; then
    echo "ℹ️  Dependencies already installed"
else
    if command -v npm &> /dev/null; then
        npm install
        echo "✅ Dependencies installed"
    else
        echo "❌ npm not found. Please install Node.js"
        exit 1
    fi
fi

# Step 6: Display summary
echo ""
echo "═══════════════════════════════════════════════════════════"
echo "✅ Temporal Bootstrap Complete!"
echo "═══════════════════════════════════════════════════════════"
echo ""
echo "🌐 Web UI:        http://localhost:8080"
echo "📡 API Endpoint:  localhost:7233"
echo "🗄️  Database:     localhost:5433 (temporal/temporal_changeme)"
echo ""
echo "📋 Next Steps:"
echo ""
echo "   1. Start the worker (polling for tasks):"
echo "      cd $SCRIPT_DIR/workflows"
echo "      npm run worker"
echo ""
echo "   2. In another terminal, start a test delivery:"
echo "      cd $SCRIPT_DIR/workflows"
echo "      npm run client -- start DELIV-TEST-001"
echo ""
echo "   3. Send signals and check status:"
echo "      npm run client -- pickup DELIV-TEST-001"
echo "      npm run client -- deliver DELIV-TEST-001 success"
echo "      npm run client -- audit DELIV-TEST-001"
echo ""
echo "   4. Monitor in Web UI:"
echo "      http://localhost:8080"
echo "      Namespace: $NAMESPACE"
echo ""

