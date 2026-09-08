---
id: INFRA-OMNIROUTE-SETUP
title: "OmniRoute Installation & Setup Guide"
aliases: ["_INFRASTRUCTURE/omniroute/SETUP", "OmniRoute Setup"]
tags: [infrastructure, omniroute, setup, installation, docker, npm]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[_INFRASTRUCTURE/omniroute/README|OmniRoute Hub]] | [[17-MODELS/17-MODELS|17-MODELS]] | [[CLAUDE]]

# OmniRoute Setup for Worldwidebro

**Status:** Ready for installation  
**Date:** 2026-09-01  
**Integration:** GitHub + LiteLLM + Neo4j + Supabase

---

## Phase 1: Install OmniRoute

### Option A: Global NPM CLI (Recommended for Tailscale)

```bash
# Install globally
npm install -g omniroute

# Start OmniRoute
omniroute start

# This runs on port 3000 by default
# Access: http://localhost:3000 or https://omniroute-6da9315f.tailscale-magicnet.ts.net
```

### Option B: Docker (Recommended for production)

```bash
# Run via Docker
docker run -d \
  --name omniroute \
  -p 3000:3000 \
  -e GITHUB_TOKEN=$GITHUB_TOKEN \
  -e LITELLM_API_BASE=http://host.docker.internal:4001 \
  -e NEO4J_URI=neo4j://host.docker.internal:7687 \
  diegosouzapw/omniroute
```

### Option C: Source (For development)

```bash
git clone https://github.com/diegosouzapw/OmniRoute.git
cd OmniRoute
pnpm install
pnpm dev
```

---

## Phase 2: Configure OmniRoute for GitHub

### Step 1: GitHub Personal Access Token

You have: `gho_CfyCXg4GKNp...` (via GitHub CLI)

### Step 2: Create GitHub Webhook

1. Go to: `https://github.com/worldwidebro/Claude.Home/settings/hooks`
2. Click "Add webhook"
3. **Payload URL:** `https://omniroute-6da9315f.tailscale-magicnet.ts.net:3000/api/github/webhook`
4. **Content type:** `application/json`
5. **Events:** Pull requests, Issues, Push, Repository
6. Click "Add webhook"

### Step 3: Verify Webhook

```bash
# Dashboard shows webhook status
# Visit: http://localhost:3000/dashboard/webhooks
```

---

## Phase 3: Wire to LiteLLM → Ollama

### Configuration

```env
# GitHub Integration
GITHUB_TOKEN=gho_CfyCXg4GKNp...
GITHUB_WEBHOOKS_ENABLED=true

# LiteLLM Routing
LITELLM_API_BASE=http://localhost:4001
LITELLM_MODELS=local-coder,local-small,local-embed

# Neo4j Integration
NEO4J_URI=neo4j://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=ventures2026

# Supabase (Ventures Registry)
SUPABASE_URL=https://cyhzilqldouzgynacqpe.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

---

## Phase 4: Test the Stack

### Test 1: OmniRoute Health

```bash
curl http://localhost:3000/api/health
```

### Test 2: Route through LiteLLM

```bash
curl -X POST http://localhost:3000/api/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "local-coder",
    "messages": [{"role": "user", "content": "Hello"}]
  }'
```

### Test 3: Trigger GitHub Webhook

1. Create issue in `Claude.Home`
2. OmniRoute receives webhook
3. Routes to `local-small`
4. Result stored in Neo4j

---

## CLI Commands

```bash
omniroute start              # Start server
omniroute status             # Check status
omniroute-reset-password     # Reset admin
omniroute --help            # Help
```

---

## Live Dashboards

- **Main:** `http://localhost:3000`
- **Webhooks:** `http://localhost:3000/dashboard/webhooks`
- **Free Tiers:** `http://localhost:3000/dashboard/free-tiers`
- **Usage:** `http://localhost:3000/dashboard/usage`

---

## Connected Portals
- **OmniRoute Hub:** [[_INFRASTRUCTURE/omniroute/README|OmniRoute]]
- **Completion Report:** [[_INFRASTRUCTURE/omniroute/COMPLETION|Completion Report]]
- **Models Domain:** [[17-MODELS/17-MODELS|17-MODELS]]
- **Engineering Hub:** [[56-ENGINEERING/README|56-ENGINEERING]]
