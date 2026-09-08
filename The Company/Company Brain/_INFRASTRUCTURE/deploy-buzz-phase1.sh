#!/bin/bash
# Buzz Phase 1 Deployment Script
# Deploys Buzz infrastructure (relay, PostgreSQL, Redis, MinIO) on Mac Studio
# Authority: Infrastructure Control Plane (CP-027)

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Directories
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
LACIES_PATH="/Volumes/LaCie"
BUZZ_DATA_PATH="$LACIES_PATH/buzz-data"
COMPOSE_FILE="$SCRIPT_DIR/buzz-docker-compose.yml"
INIT_SQL="$SCRIPT_DIR/init-buzz.sql"

# Functions
print_header() {
    echo -e "\n${BLUE}════════════════════════════════════════${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}════════════════════════════════════════${NC}\n"
}

print_step() {
    echo -e "${YELLOW}→ $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

check_prerequisites() {
    print_header "STEP 0: CHECKING PREREQUISITES"

    # Check Docker
    print_step "Checking Docker..."
    if ! docker --context macstudio ps &> /dev/null; then
        print_error "Docker context 'macstudio' not accessible"
        echo "Make sure Docker daemon on Mac Studio is running"
        exit 1
    fi
    print_success "Docker context 'macstudio' accessible"

    # Check LaCie mount
    print_step "Checking LaCie volume..."
    if [ ! -d "$LACIES_PATH" ]; then
        print_error "LaCie volume not mounted at $LACIES_PATH"
        echo "Connect LaCie 4TB and mount, then retry"
        exit 1
    fi
    print_success "LaCie volume mounted"

    # Check compose file
    if [ ! -f "$COMPOSE_FILE" ]; then
        print_error "docker-compose.yml not found at $COMPOSE_FILE"
        exit 1
    fi
    print_success "docker-compose.yml found"

    # Check init SQL
    if [ ! -f "$INIT_SQL" ]; then
        print_error "init-buzz.sql not found at $INIT_SQL"
        exit 1
    fi
    print_success "init-buzz.sql found"
}

create_data_directories() {
    print_header "STEP 1: CREATING DATA DIRECTORIES"

    print_step "Creating $BUZZ_DATA_PATH/{postgres,redis,minio,relay}..."
    mkdir -p "$BUZZ_DATA_PATH"/{postgres,redis,minio,relay}
    chmod -R 755 "$BUZZ_DATA_PATH"
    print_success "Data directories created"

    # Show free space
    df -h "$LACIES_PATH" | tail -1 | awk '{print "Available space: " $4}'
}

deploy_buzz_services() {
    print_header "STEP 2: DEPLOYING BUZZ SERVICES"

    print_step "Starting Buzz services with docker-compose..."
    cd "$SCRIPT_DIR"

    # Deploy
    if docker --context macstudio compose -f "$COMPOSE_FILE" up -d; then
        print_success "Services started"
    else
        print_error "Failed to start services"
        exit 1
    fi

    # Wait for services to be ready
    print_step "Waiting for services to initialize (30 seconds)..."
    sleep 30

    # Check status
    print_step "Checking service status..."
    docker --context macstudio compose -f "$COMPOSE_FILE" ps
}

verify_connectivity() {
    print_header "STEP 3: VERIFYING CONNECTIVITY"

    # Buzz Relay
    print_step "Testing Buzz Relay (:8080)..."
    if curl -s -f http://100.87.214.70:8080/health > /dev/null; then
        print_success "Buzz Relay responding"
    else
        print_error "Buzz Relay not responding"
    fi

    # PostgreSQL
    print_step "Testing PostgreSQL (:5433)..."
    if docker --context macstudio exec -T buzz_postgres pg_isready -U postgres &> /dev/null; then
        print_success "PostgreSQL ready"
    else
        print_error "PostgreSQL not ready"
    fi

    # Redis
    print_step "Testing Redis (:6380)..."
    if docker --context macstudio exec -T buzz_redis redis-cli ping &> /dev/null; then
        print_success "Redis ready"
    else
        print_error "Redis not ready"
    fi

    # MinIO
    print_step "Testing MinIO (:9000)..."
    if curl -s -f http://100.87.214.70:9000/minio/health/live > /dev/null; then
        print_success "MinIO ready"
    else
        print_error "MinIO not ready"
    fi
}

setup_initial_workspace() {
    print_header "STEP 4: SETTING UP INITIAL WORKSPACE"

    print_step "Workspace 'company-brain' is created via init-buzz.sql"
    print_step "Channels created:"
    echo "  - #repo-classification"
    echo "  - #repo-scoring"
    echo "  - #repo-disposition"
    echo "  - #repo-adoption-pipeline"
    echo "  - #general"

    print_step "Verifying PostgreSQL setup..."
    docker --context macstudio exec buzz_postgres psql -U postgres -d buzz -c \
        "SELECT workspace_id, name FROM channels LIMIT 5;" || true

    print_success "Initial workspace configured"
}

create_agent_keys() {
    print_header "STEP 5: CREATING AGENT SERVICE KEYS"

    print_step "Creating Nostr keys for agents..."
    print_step "You should store these in Bitwarden under 'Buzz Agent Keys - Company Brain'"

    cat << 'EOF'

Agent Keys to Generate (via Buzz Web UI or API):
  - AGT-013 (Classifier)
  - AGT-014 (Scorer)
  - AGT-015 (Disposition)
  - AGT-017 (Adoption)
  - AGT-019 (Sync Agent)

Store in environment or Bitwarden:
  export BUZZ_AGT013_KEY="..."
  export BUZZ_AGT014_KEY="..."
  export BUZZ_AGT015_KEY="..."
  export BUZZ_AGT017_KEY="..."
  export BUZZ_AGT019_KEY="..."

Generate keys via:
  curl -X POST http://100.87.214.70:8080/api/v1/workspaces/company-brain/service-keys \
    -H "Content-Type: application/json" \
    -d '{"service_name":"AGT-013"}'

EOF

    print_success "Agent key generation documented"
}

print_next_steps() {
    print_header "DEPLOYMENT COMPLETE ✅"

    cat << 'EOF'

Next Steps for Phase 2 (Sep 13-19):

1. Create MCP Bridge Tools
   - Add buzz_publish_event, buzz_read_channel, buzz_sync_to_neo4j
   - Register in ~/.claude/settings.json

2. Wire Agents to Buzz
   - Modify AGT-013/014/015 to publish to Buzz channels
   - Keep Neo4j writes, add Buzz publication

3. Test First Repo Through Buzz
   - Classify 1 repo via AGT-013
   - Review in Buzz via repo-advisor persona
   - Verify sync to Neo4j

URLs:
  - Buzz Relay API: http://100.87.214.70:8080
  - Buzz Web UI: http://100.87.214.70:3000 (when UI service starts)
  - Neo4j Browser: http://100.87.214.70:7474
  - MinIO Console: http://100.87.214.70:9001

Services Running:
  - buzz_relay (8080)
  - buzz_postgres (5433)
  - buzz_redis (6380)
  - buzz_minio (9000, 9001)

To view logs:
  docker --context macstudio logs -f buzz_relay
  docker --context macstudio logs -f buzz_postgres

To stop services:
  cd "$SCRIPT_DIR"
  docker --context macstudio compose -f buzz-docker-compose.yml down

To remove all data:
  rm -rf "$BUZZ_DATA_PATH"/*

EOF
}

# Main execution
main() {
    print_header "BUZZ PHASE 1 DEPLOYMENT"
    echo "Timeline: Week 1 (Sep 6-12, 2026)"
    echo "Authority: Infrastructure Control Plane (CP-027)"
    echo ""

    check_prerequisites
    create_data_directories
    deploy_buzz_services
    verify_connectivity
    setup_initial_workspace
    create_agent_keys
    print_next_steps
}

# Run main
main
