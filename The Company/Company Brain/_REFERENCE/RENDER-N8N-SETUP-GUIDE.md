[[STARTHERE]] | [[_REFERENCE/README|Reference Index]] | [[REALITY]]

---
id: DOC-RENDER-N8N-001
title: Render + n8n Self-Hosted Setup Guide
description: Deploy n8n workflow automation on Render with Render CLI management
updated: 2026-09-10
status: ACTIVE
---

# Render + n8n Self-Hosted Setup Guide

Deploy n8n (workflow automation) on Render.com with CLI-based infrastructure management.

---

## Quick Start (5 min)

```bash
# 1. Install Render CLI
brew install render  # macOS
# or: curl -fsSL https://raw.githubusercontent.com/render-oss/cli/refs/heads/main/bin/install.sh | sh

# 2. Authenticate
render login
# (Browser opens for authorization)

# 3. List workspaces
render workspaces

# 4. Deploy n8n
cd _INFRASTRUCTURE
render deploy --name n8n-blueprint

# 5. View deployment
render services
# (Select n8n service to see live logs)
```

---

## What's Deployed

### **Services**

| Service | Type | Purpose |
|---------|------|---------|
| **n8n** | Web | Workflow automation engine |
| **n8n-db** | PostgreSQL | Workflow storage |

### **Architecture**

```
Render DNS (n8n-xxxx.onrender.com)
  ├── n8n Web Service (Docker)
  │   ├── Port: 5678 (HTTP → HTTPS)
  │   ├── Health check: /healthz every 30s
  │   ├── Scaling: 1–3 instances (auto)
  │   └── Env vars: Database connection, webhooks, timezone
  │
  └── PostgreSQL (n8n-db)
      ├── Database: n8n
      ├── User: n8n_user
      └── Auto-backup: Enabled
```

---

## Render CLI Commands (Most Common)

### **Deployment**

```bash
# Deploy from render.yaml
render deploy --name my-deployment

# List all services
render services

# Trigger a deploy
render deploys create <service-id> --wait

# View deploy history
render deploys list <service-id>
```

### **Logs & Debugging**

```bash
# Stream live logs
render services
# (Select service → View logs)

# Postgres access
render psql n8n-db -c "SELECT COUNT(*) FROM workflows;" -o text

# SSH into service (ephemeral shell)
render ssh n8n --ephemeral
```

### **Configuration**

```bash
# Set environment variables
render env set SERVICE_ID KEY=value

# List environment variables
render env list SERVICE_ID

# View service details
render services
```

---

## Environment Variables (Key Ones)

| Variable | Value | Purpose |
|----------|-------|---------|
| `N8N_HOST` | `${RENDER_EXTERNAL_URL}` | Public hostname |
| `N8N_PORT` | `5678` | Internal port |
| `N8N_PROTOCOL` | `https` | HTTPS enabled |
| `WEBHOOK_TUNNEL_URL` | `${RENDER_EXTERNAL_URL}/` | Webhook callbacks |
| `EXECUTION_MODE` | `queue` | Job queue (production) |
| `DB_TYPE` | `postgresdb` | Use PostgreSQL |

---

## First-Time Login

1. **Get the public URL:**
   ```bash
   render services
   # Look for n8n URL: https://n8n-xxxx.onrender.com
   ```

2. **Open in browser:**
   - `https://n8n-xxxx.onrender.com`

3. **Create admin user:**
   - Email: your@email.com
   - Password: (first user auto-becomes admin)

4. **Configure credentials:**
   - Settings → Credentials
   - Add API keys for integrations (Slack, GitHub, etc.)

---

## Using Render CLI in CI/CD

### **GitHub Actions Example**

```yaml
name: Deploy n8n to Render

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Install Render CLI
        run: |
          curl -fsSL https://github.com/render-oss/cli/releases/download/v1.1.0/cli_1.1.0_linux_amd64.zip -o render.zip
          unzip render.zip
          sudo mv cli_v1.1.0 /usr/local/bin/render
      
      - name: Deploy to Render
        env:
          RENDER_API_KEY: ${{ secrets.RENDER_API_KEY }}
        run: |
          render deploys create ${{ secrets.RENDER_SERVICE_ID }} --wait --confirm
```

**Setup secrets in GitHub:**
- `RENDER_API_KEY`: Generate at https://dashboard.render.com (Account → API Keys)
- `RENDER_SERVICE_ID`: Get from `render services` output

---

## Monitoring & Metrics

### **Render Dashboard**

1. Go to https://dashboard.render.com
2. Select your service
3. View:
   - **Logs** (live stream)
   - **Metrics** (CPU, memory, requests)
   - **Deploys** (history, rollbacks)

### **Health Checks**

```bash
# Manual health check
curl https://n8n-xxxx.onrender.com/healthz

# Expected response: 200 OK
```

### **Database Backups**

```bash
# List backups
render psql n8n-db --command "SELECT version();" -o text

# Render automatically backs up daily
# Restore: Contact Render support with backup ID
```

---

## Webhooks (Integration with Agent Layer)

n8n webhooks enable triggered workflows from external systems.

### **Create a Webhook in n8n**

1. **In n8n UI:**
   - Create new workflow
   - Add "Webhook" trigger node
   - Set method: POST
   - Copy webhook URL

2. **Use in agent layer:**
   ```python
   # In _AGENTS/agent_layer.py
   @register(344)
   class AgentEngineerAgent(BaseAgent):
       def execute(self, task: Task) -> dict:
           # Trigger n8n workflow
           webhook_url = "https://n8n-xxxx.onrender.com/webhook/my-workflow"
           requests.post(webhook_url, json={
               "agent_id": task.id,
               "role": self.role.id,
               "action": "execute",
           })
           return {"workflow_triggered": True}
   ```

3. **n8n executes the workflow:**
   - Send notifications (Slack, email)
   - Update databases
   - Trigger other services
   - Return results to agent

---

## Cost Estimate

| Service | Plan | Monthly Cost |
|---------|------|--------------|
| **n8n Web** | Standard | ~$7–$12 |
| **PostgreSQL** | Standard | ~$15 |
| **Total** | | ~$22–$27 |

(Prices as of Sep 2026; see Render pricing for current rates)

---

## Troubleshooting

### **Service won't start**

```bash
# View logs
render services  # Select n8n → View logs

# Check common issues:
# - Database not reachable: Check RENDER_EXTERNAL_URL
# - Port already in use: n8n is hardcoded to 5678
# - Health check failing: Increase initialDelaySeconds in render.yaml
```

### **Database connection error**

```bash
# Test database
render psql n8n-db -c "SELECT 1;" -o text

# If fails, check:
# - Database user credentials
# - IP allowlist (should be empty = allow all)
# - Database name = "n8n"
```

### **Webhooks not firing**

```bash
# Test webhook
curl -X POST https://n8n-xxxx.onrender.com/webhook/test-webhook \
  -H "Content-Type: application/json" \
  -d '{"test": true}'

# Check n8n logs for webhook execution
```

---

## Next: Wiring n8n into Agent Layer

Once n8n is running, integrate it with your agent system:

1. **Store n8n webhook URL in agents:**
   ```python
   N8N_WEBHOOK_BASE = "https://n8n-xxxx.onrender.com/webhook"
   ```

2. **Trigger workflows from agents:**
   - Agent executes task
   - Posts to n8n webhook
   - n8n workflow runs (notifications, integrations, etc.)
   - Workflow returns result

3. **Example: SDR Agent → Slack Notification**
   ```
   SDRAgent executes → Finds 5 prospects → Trigger n8n webhook
     ↓
   n8n workflow:
     1. Format prospect data
     2. Send Slack message to sales team
     3. Log to Google Sheets
     4. Return confirmation
   ```

---

## Files in This Deployment

```
_INFRASTRUCTURE/
├── render-n8n-blueprint.yaml     # Render deployment config
├── Dockerfile.n8n               # Docker image build
├── render-n8n-setup.sh          # Setup script
└── RENDER-N8N-SETUP-GUIDE.md    # This file
```

---

## Quick Reference: Render CLI Cheat Sheet

```bash
# Auth & workspaces
render login                          # Authenticate
render workspaces                     # List workspaces
render workspace set <name>           # Switch workspace

# Services & deployment
render services                       # List all services
render services create --repo <url>   # Create new service
render deploys create <service-id>    # Trigger deploy
render deploys list <service-id>      # View deploy history
render ssh <service-id>               # SSH into service

# Database
render psql <db-id> -c "SELECT ..." # Run SQL query

# Environment
render env list <service-id>          # List env vars
render env set <service-id> KEY=val   # Set env var

# Output formats
render services -o json               # JSON output
render services -o yaml               # YAML output
render services -o text               # Plain text
```

---

**Generated:** 2026-09-10  
**Authority:** [[_AGENTS/agent_layer.py|Agent Layer]]  
**Related:** [[_INFRASTRUCTURE/render-n8n-blueprint.yaml|Blueprint]], [[_INFRASTRUCTURE/render-n8n-setup.sh|Setup Script]]
