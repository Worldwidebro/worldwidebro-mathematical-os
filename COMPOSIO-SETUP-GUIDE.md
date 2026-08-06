---
name: COMPOSIO-SETUP-GUIDE
title: Composio Setup Guide for WinnersCircle
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# Composio Setup Guide for WinnersCircle

## Overview

Your workspace: `winnerscirclewcllc_workspace`
Project: `winnerscirclewcllc_workspace_first_project`
Dashboard: https://dashboard.composio.dev/winnerscirclewcllc_workspace/winnerscirclewcllc_workspace_first_project

## What is Composio?

Composio is an AI tool orchestration platform that lets you:
1. **Connect integrations** (GitHub, Slack, Gmail, 100+ tools)
2. **Create agents** that use these tools
3. **Track execution** of agent work in your dashboard
4. **Manage credentials** securely

## Local CLI Setup

### Step 1: Authentication

To connect your local CLI to your Composio account:

```bash
composio login
```

This will:
- Open your browser to authenticate
- Store your API key locally
- Connect you to your workspace

**Your credentials are stored at:** `~/.composio/config.json`

### Step 2: Check Your Authentication

```bash
composio whoami
```

Should show your email/account information.

### Step 3: List Available Tools

```bash
# List all available tools/integrations
composio tools list

# Search for specific tools
composio tools search github
composio tools search slack
```

### Step 4: Connect Tools to Your Account

```bash
# Connect GitHub to your account
composio connect github

# Connect Slack
composio connect slack

# Connect Gmail
composio connect gmail

# View all connected tools
composio connected
```

## Understanding Your Dashboard

Your dashboard at `https://dashboard.composio.dev/winnerscirclewcllc_workspace/winnerscirclewcllc_workspace_first_project/` shows:

1. **Getting Started** - Initial setup guide
2. **Connected Accounts** - Tools you've authenticated
3. **Tools** - Available integrations
4. **Executions** - History of completed work
5. **Agents** - AI agents you've created
6. **API Keys** - For programmatic access

## Local CLI Commands

### Tool Management
```bash
composio connect <tool>          # Connect a new tool
composio connected               # List connected tools
composio disconnect <tool>       # Disconnect a tool
composio tools list              # List available tools
composio tools search <query>    # Search tools
```

### Work/Execution Tracking
```bash
composio executions list         # List recent executions
composio executions status       # Check execution status
composio logs                    # View recent logs
```

### Agent Management
```bash
composio agent create            # Create new agent
composio agent list              # List your agents
composio agent run <agent>       # Run an agent
```

### Configuration
```bash
composio config set              # Set configuration
composio config get              # Get configuration
composio version                 # Check version
composio upgrade                 # Upgrade CLI
```

## API Integration (Local Development)

If you want to use Composio in your local code:

### Python SDK

```python
from composio import Composio

# Initialize with your API key (stored in ~/.composio/config.json)
composio = Composio()

# List available tools
tools = composio.tools.get_all()

# Execute a tool
result = await composio.tools.execute(
    'GITHUB_CREATE_REPO',
    userId='your-user-id',
    arguments={
        'repo_name': 'my-repo',
        'description': 'My new repository'
    }
)
```

### TypeScript/JavaScript SDK

```typescript
import { Composio } from '@composio/core';

const composio = new Composio({
  // API key can be set via environment variable: COMPOSIO_API_KEY
});

const tools = await composio.tools.get('user-id', {
  toolkits: ['GITHUB']
});

const result = await composio.tools.execute('GITHUB_CREATE_REPO', {
  userId: 'user-id',
  arguments: {
    repo_name: 'my-repo'
  }
});
```

## Next Steps

1. **Authenticate locally:**
   ```bash
   composio login
   ```

2. **Connect your first tool:**
   ```bash
   composio connect github
   ```

3. **View connected tools:**
   ```bash
   composio connected
   ```

4. **Check your dashboard:**
   Visit: https://dashboard.composio.dev/winnerscirclewcllc_workspace/winnerscirclewcllc_workspace_first_project/

5. **Create your first agent or integration in code**

## Troubleshooting

### Authentication Issues
```bash
# Check if authenticated
composio whoami

# Re-authenticate
rm ~/.composio/config.json
composio login
```

### Path Issues
If `composio` command not found:
```bash
# Add to your shell profile
export PATH="$HOME/.composio:$PATH"

# Reload shell
exec $SHELL
```

### View Logs
```bash
# Check CLI logs
composio logs

# Enable debug mode
COMPOSIO_LOG_LEVEL=debug composio <command>
```

## Workspace Structure

```
WinnersCircle Workspace
├── winnerscirclewcllc_workspace_first_project
│   ├── Connected Accounts (GitHub, Slack, etc.)
│   ├── Custom Tools
│   ├── Agents
│   └── Execution History
```

## Resources

- **Dashboard:** https://dashboard.composio.dev
- **Documentation:** https://docs.composio.dev
- **Discord:** https://discord.gg/composio
- **GitHub:** https://github.com/ComposioHQ/composio

## Your API Key

To get your API key for programmatic access:
1. Go to: https://dashboard.composio.dev/settings
2. Navigate to API Keys section
3. Create or copy your API key
4. Set environment variable: `export COMPOSIO_API_KEY="your-key"`

---

**Next:** Run `composio login` to authenticate your local CLI with your workspace.
