# Worldwidebro Project Discovery & Integration System

## Overview
This system enables Claude on Mac Studio to discover, index, and operate on the Worldwidebro Holdings project across all mounted drives, leveraging Paperclip orchestration and Composio integrations.

## System Architecture

### Layer 1: Project Discovery
```bash
# Scan for project directories with known markers
find ~ -name "package.json" -o -name "vercel.json" -o -name "CLAUDE.md" | grep -E "(worldwidebro|ventures|paperclip|composio)"

# Index mounted drives
mount | grep -v "devfs" | awk '{print $3}' | while read drive; do
  find "$drive" -name ".claude" -o -name "venture-*" -o -name "ai-venture*" 2>/dev/null
done
```

### Layer 2: Context Loading
```typescript
// Load project context in order of precedence:
1. /Users/acebless/.claude/projects/-Users-acebless-Documents/memory/
   - System architecture
   - User context
   - Project state
   - Feedback patterns

2. /Users/acebless/Documents/venture-hub/
   - Business logic
   - Venture definitions
   - Sector frameworks

3. ~/.paperclip/instances/default/
   - Organizational structure
   - Agent configurations
   - Task definitions
   - Budget allocations

4. Composio Tool Integrations
   - OpenVolo (contact management)
   - Slack (communication)
   - GitHub (code repositories)
   - Linear (issue tracking)
```

### Layer 3: Business Logic Integration

#### Paperclip as Execution Engine
- **CEO Agent**: Strategic decisions on venture ROI, capital allocation
- **CTO (Operations Manager)**: Day-to-day execution, metric tracking
- **CFO (Financial Analyst)**: Unit economics, forecasting, burn rate
- **PM (Sector Leads)**: Venture-specific oversight and scaling

#### Composio as Action Layer
- **Tool Router**: Route tasks to appropriate integrations
- **Webhook Pipeline**: Receive updates from external systems
- **Command Executor**: Execute 91+ pre-defined business commands

#### Claude as Reasoning Layer
- Read project state across all systems
- Generate operational decisions with business logic
- Queue actions through Paperclip agents
- Execute via Composio tools

### Layer 4: File Organization & Mounted Drives

```
/Users/acebless/Documents/
├── venture-hub/                      # Primary project directory
│   ├── CLAUDE.md                    # Project-specific instructions
│   ├── ventures/                    # 687 ventures (indexed by sector)
│   ├── sectors/                     # 17 sector frameworks
│   └── products/                    # Product templates
├── paperclip-setup.ts              # Agent initialization
├── PROJECT-DISCOVERY-SYSTEM.md     # This file
├── /Volumes/*/                      # Mounted drives for:
│   ├── contact databases
│   ├── historical data
│   └── sector documentation
└── ~/.paperclip/instances/default/ # Paperclip state
    ├── companies/                  # Organization structure
    ├── agents/                     # Agent configurations
    └── db/                         # Embedded PostgreSQL
```

## Integration Flows

### Flow 1: Venture State -> Decision -> Action
```
1. Read venture metrics from database/Supabase
2. Financial Analyst (CFO) calculates CAC/LTV/churn
3. CEO agent evaluates ROI decision framework:
   - ROI < 0%: Kill venture (unless strategic)
   - ROI 0-50%: Hold, optimize
   - ROI 50-100%: Scale aggressively
   - ROI > 100%: Compounding machine
4. Paperclip queues decision as task
5. Composio routes execution:
   - Update venture status in Linear
   - Post decision in Slack #ventures channel
   - Update contacts in OpenVolo
6. Log activity to audit trail
```

### Flow 2: Sector-Level Optimization
```
1. Sector Lead (PM) gathers all ventures in sector
2. Identifies cross-venture collaboration opportunities
3. Calculates aggregate sector metrics
4. Escalates sector-wide risks to CEO
5. Recommends resource reallocation within sector
6. Facilitates knowledge sharing between ventures
```

### Flow 3: Portfolio Rebalancing (Monthly)
```
1. Financial Analyst generates monthly report:
   - Each venture's current ROI
   - Aggregate portfolio ROI
   - Capital efficiency by sector
2. CEO reviews and decides rebalancing:
   - Kill low-ROI ventures
   - Scale high-ROI ventures
   - Rebalance budget across sectors
3. Operations Manager executes:
   - Cancel projects for killed ventures
   - Allocate headcount/resources
   - Update sector budgets
4. Sector Leads implement changes
```

## Command Execution Through Composio

### Available Commands (91 total)
- **Venture Management**: create, scale, kill, pivot
- **Financial**: forecast, model, reallocate, audit
- **Team**: onboard, assign, escalate, review
- **Communication**: notify, brief, escalate, document
- **Integration**: sync contacts, update CRM, log activity

### Webhook Pipeline
```
External System (Linear, Slack, GitHub)
  → /api/webhooks/claude-command
  → Parse & validate command
  → Queue to appropriate agent
  → Paperclip execution
  → Composio action routing
  → Update state
  → Log audit trail
```

## Using This System

### From Claude on Mac Studio
```
1. Set environment: PAPERCLIP_API=http://localhost:3101/api
2. Load memory: read ~/.claude/projects/*/memory/MEMORY.md
3. Discover projects: find ~ -name "CLAUDE.md"
4. Connect to Paperclip: check agents at {PAPERCLIP_API}/companies
5. Queue operations through agent system
6. Execute via Composio tool router
```

### From Automation (cron/loop)
```
1. Start: /loop-start trigger
2. Load Worldwidebro CEO agent
3. Execute 24-hour business cycle:
   - Gather venture metrics
   - Calculate portfolio health
   - Make rebalancing decisions
   - Execute through Paperclip
   - Log results
4. Next cycle: 24 hours later
```

## Remaining Integration Gaps

1. **Venture Seeding**: Create initial 687 ventures in Paperclip/Supabase
2. **Metric Ingestion**: Connect venture databases to reporting layer
3. **Real-time Updates**: WebSocket for agent-to-dashboard updates
4. **Approval Workflows**: Board approval for ventures > $50K allocation
5. **Knowledge Graph**: Unified org structure across all systems

## Testing Checklist

- [ ] Discover project from clean Mac Studio startup
- [ ] Load all system context (memory + project files)
- [ ] Query Paperclip API for agents (CEO, CTO, CFO, Sector PMs)
- [ ] Queue test command through Composio
- [ ] Verify execution in agent logs
- [ ] Check Slack/Linear for notification
- [ ] Confirm audit trail in database
