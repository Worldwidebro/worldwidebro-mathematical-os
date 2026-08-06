---
name: AOC-SWARM-RUNNER
title: 'AOC SWARM RUNNER: Execution Layer Architecture'
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# AOC SWARM RUNNER: Execution Layer Architecture

**Status:** Ready to build  
**Purpose:** Read aoc_ready_tasks → route to agent → execute → write results back  
**Scope:** Turn 4,977 pending tasks into real work across 708 ventures

---

## The Problem

You have:
- ✅ 708 ventures defined
- ✅ 554 agents defined (100 genius + 454 sub)
- ✅ 4,977 tasks queued in `aoc_ready_tasks` table
- ✅ Full infrastructure (Supabase, GitHub, n8n, MCP tools)
- ❌ **NO execution loop** — tasks sit in database, nothing picks them up

The swarm runner is the execution loop. It's the "nervous system" that makes the agents do work.

---

## Architecture: The 3-Tier Execution Model

```
TIER 1: MASTER ORCHESTRATOR (Claude Code / Mac Studio)
├─ Reads aoc_ready_tasks table
├─ Claims task (status = 'running', claimed_by = agent_id)
├─ Routes to appropriate agent type
└─ Writes results back to Supabase + GitHub + Notion

TIER 2: SECTOR AGENT SWARM (Parallel Claude instances)
├─ E-Commerce Agent (110 ventures)
├─ Finance Agent (50+ ventures)
├─ Beauty Agent (40+ ventures)
├─ Food Agent (35+ ventures)
├─ Construction Agent (20 ventures)
├─ Technology Agent (60 ventures)
└─ [13 more sector agents]

TIER 3: TOOL INTEGRATION LAYER (MCP servers)
├─ GitHub API (create repos, commits, PRs)
├─ Supabase SQL (update venture status, task completion)
├─ Notion (status updates, dashboards)
├─ Slack (notifications, escalations)
├─ Make.com (trigger next-phase tasks)
└─ n8n (workflow automation)
```

---

## Data Flow: Single Task Execution

```
1. CLAIM PHASE
   Master reads: SELECT * FROM aoc_ready_tasks 
                WHERE status = 'pending' 
                LIMIT 100
   
   For each task:
   - Record claimed_by = agent_id
   - Set status = 'running'
   - Set claimed_at = now()
   - Lock task (prevent double-execution)

2. ROUTE PHASE
   Master determines: Which agent should execute this?
   
   Routing logic:
   - task.sector_id → sector_agent[sector]
   - task.type → agent_capability[type]
   - Example: (sector='ecommerce', type='mvp_build') 
             → e_commerce_agent.execute_mvp_build()

3. EXECUTE PHASE
   Agent executes task:
   - Read task definition + venture data
   - Execute work (create repo, write code, build product)
   - Generate outputs (repo URL, files, status)
   - Handle errors (retry 3x, then escalate)

4. RESULT PHASE
   Agent writes results:
   - Update Supabase: venture.progress_pct += increment
   - Commit to GitHub: [task complete] message
   - Update task: status = 'complete', result = { ... }
   - Trigger next task via Make.com
   - Notify in Slack

5. TRACKING PHASE
   Dashboard updates:
   - Per-venture progress bar
   - Task completion timeline
   - Agent performance metrics
   - Dependency graph for next phases
```

---

## Task Execution Queue: By Type

### Type 1: ENTITY FORMATION (687 tasks)
```
Task: Create LLC + get EIN + register business
Agent capability: Finance Agent or Formation Agent
Expected output:
  - Formation documents (PDF in repo)
  - EIN assignment (stored in Supabase)
  - Business registration number
  - Timeline: 3-5 days (some require manual step)
Status tracking: formation_complete (boolean)
Next trigger: tax_setup task
```

### Type 2: TAX SETUP (687 tasks)
```
Task: Quarterly filing schedule + tax ID + accounting setup
Agent capability: Finance Agent
Expected output:
  - Tax filing calendar (in repo/Notion)
  - Accounting ledger template
  - Quarterly reminder schedule
  - Tax rate by venture type
Status tracking: tax_setup_complete (boolean)
Next trigger: vendor_onboarding task
Dependencies: entity_formation must be complete
```

### Type 3: GRANT APPLICATIONS (857 tasks)
```
Task: Research applicable grants + prepare applications
Agent capability: Finance Agent + Research Agent
Expected output:
  - List of eligible grants (spreadsheet)
  - Application templates (partially filled)
  - Deadlines + funding amounts
  - Status: draft | submitted | approved | denied
Status tracking: grant_applications_submitted (count)
Next trigger: funding_received task (when approved)
```

### Type 4: MVP BUILD (594 tasks)
```
Task: Create minimal viable product (landing page, demo, or prototype)
Agent capability: Tech Agent + Sector Agent (specialized MVP type)
Expected output:
  - GitHub repo with code/landing page
  - Deployed demo URL
  - Feature list
  - Screenshots/video walkthrough
Status tracking: mvp_complete (boolean), mvp_url (text)
Next trigger: go_to_market task
```

### Type 5: CONTENT GENERATION (89 tasks)
```
Task: Blog posts, case studies, testimonials, SOPs
Agent capability: Content Agent or Sector Agent
Expected output:
  - 5-10 blog posts (markdown in repo)
  - Social media templates
  - Email sequences
  - Video script outlines
Status tracking: content_pieces_generated (count)
Next trigger: social_media_launch or marketing_setup
```

### Type 6: MONETIZATION (685 tasks)
```
Task: Set up Stripe products + pricing + payment flow
Agent capability: Finance Agent + Tech Agent
Expected output:
  - Stripe product IDs (stored in Supabase)
  - Pricing tiers (exported to ventures table)
  - Payment page/checkout link
  - Invoice templates
Status tracking: stripe_products_created (boolean), payment_url (text)
Next trigger: sales_launch task
```

### Type 7: OPS SETUP (596 tasks)
```
Task: SOPs, team structure, vendor integrations, automation workflows
Agent capability: Operations Agent or Sector Agent
Expected output:
  - SOP documentation (in repo)
  - Team roles defined (in Notion/Supabase)
  - Vendor list + integration plan
  - n8n workflow templates
Status tracking: ops_ready (boolean), integrations_count (number)
Next trigger: launch task
```

### Type 8: GO-TO-MARKET / SALES (685 tasks)
```
Task: Launch strategy + lead generation + sales collateral
Agent capability: Sales Agent or Sector Agent
Expected output:
  - GTM plan (doc in repo)
  - Sales deck (PDF)
  - Email templates for outreach
  - Lead list (CSV)
  - ICP definition
Status tracking: gtm_plan_complete (boolean), leads_generated (count)
Next trigger: launch task
```

### Type 9: LAUNCH (48 tasks)
```
Task: Go live + announce + monitor first 48 hours
Agent capability: Launch Agent (specialized)
Expected output:
  - Live status (live | soft_launch | beta)
  - Press release/announcement
  - Social media announcements scheduled
  - First day metrics collected
Status tracking: launch_status (enum), announcement_live (boolean)
Next trigger: growth / revenue tasks
```

---

## Master Orchestrator Loop (Pseudocode)

```python
# Main execution loop runs in Claude Code session
def swarm_runner_main():
    while True:
        # 1. CLAIM PHASE
        pending_tasks = supabase.query("""
            SELECT id, venture_id, task_type, sector_id, task_order
            FROM aoc_ready_tasks
            WHERE status = 'pending'
            ORDER BY task_order, created_at
            LIMIT 50  # Batch size per loop
        """)
        
        if not pending_tasks:
            logger.info("No pending tasks. Waiting 5 minutes...")
            time.sleep(300)
            continue
        
        # 2. CLAIM LOCK
        for task in pending_tasks:
            supabase.update('aoc_ready_tasks', 
                task_id=task['id'],
                status='running',
                claimed_by=determine_agent(task),
                claimed_at=now()
            )
        
        # 3. ROUTE & EXECUTE (parallel)
        results = []
        for task in pending_tasks:
            agent = get_agent_for_task(task)
            try:
                result = agent.execute(task)
                results.append({
                    'task_id': task['id'],
                    'status': 'complete',
                    'output': result
                })
            except Exception as e:
                results.append({
                    'task_id': task['id'],
                    'status': 'error',
                    'error': str(e)
                })
        
        # 4. WRITE RESULTS BACK
        for result in results:
            if result['status'] == 'complete':
                # Update Supabase
                supabase.update('aoc_ready_tasks',
                    task_id=result['task_id'],
                    status='complete',
                    result=result['output'],
                    completed_at=now()
                )
                
                # Update venture progress
                update_venture_progress(result)
                
                # Trigger next task
                trigger_next_task(result)
                
                # Notify
                notify_slack(f"✅ Task {result['task_id']} complete")
            
            elif result['status'] == 'error':
                # Retry logic or escalation
                handle_error(result)
        
        # 5. WAIT FOR NEXT CYCLE
        time.sleep(60)  # Check for new tasks every 60 seconds


def determine_agent(task):
    """Route task to correct agent type"""
    routing = {
        'entity_formation': 'finance_agent',
        'tax_setup': 'finance_agent',
        'grant_applications': 'finance_agent',
        'mvp_build': f"{task['sector_id']}_agent",
        'content_generation': 'content_agent',
        'monetization': 'finance_agent',
        'ops_setup': f"{task['sector_id']}_agent",
        'go_to_market': 'sales_agent',
        'launch': 'launch_agent',
    }
    return routing.get(task['task_type'], 'general_agent')


def update_venture_progress(result):
    """Update venture.progress_pct based on task completion"""
    venture = supabase.get('business_ventures', result['venture_id'])
    tasks_done = supabase.query(f"""
        SELECT COUNT(*) as count
        FROM aoc_ready_tasks
        WHERE venture_id = '{result['venture_id']}'
        AND status = 'complete'
    """)[0]['count']
    
    total_tasks = supabase.get('business_ventures', 
                               result['venture_id'])['total_tasks']
    
    progress_pct = (tasks_done / total_tasks) * 100
    
    supabase.update('business_ventures',
        id=result['venture_id'],
        progress_pct=progress_pct,
        last_task_completed_at=now()
    )


def trigger_next_task(completed_task):
    """When a task completes, create its dependent task"""
    task_dependencies = {
        'entity_formation': 'tax_setup',
        'tax_setup': 'vendor_onboarding',
        'grant_applications': 'funding_received',
        'mvp_build': 'go_to_market',
        'content_generation': 'social_media_launch',
        'monetization': 'sales_launch',
        'ops_setup': 'launch',
        'go_to_market': 'launch',
        'launch': 'growth_tracking',
    }
    
    next_task_type = task_dependencies.get(completed_task['task_type'])
    if next_task_type:
        supabase.create('aoc_ready_tasks', {
            'venture_id': completed_task['venture_id'],
            'task_type': next_task_type,
            'sector_id': completed_task['sector_id'],
            'status': 'pending',
            'task_order': completed_task['task_order'] + 1,
        })
```

---

## Dashboard: Real-Time Progress View

### Per-Venture View
```
BW-001 | Lash Studio
├─ Progress: ████░░░░░░ 40% (4/10 tasks complete)
├─ Assigned Agent: Beauty Agent
├─ Current Task: MVP Build (in progress, 60% done)
├─ Latest Updates:
│  ✅ Entity Formation (complete, 2026-05-05)
│  ✅ Tax Setup (complete, 2026-05-06)
│  ✅ Monetization (complete, 2026-05-07)
│  ✅ Ops Setup (complete, 2026-05-08)
│  ⏳ MVP Build (started 2026-05-09)
│  ⏳ Go-to-Market (pending)
│  ⏳ Launch (pending)
└─ Next Action: Agent will deploy landing page by 2026-05-11
```

### Sector Aggregate View
```
Beauty & Wellness (41 ventures)
├─ Overall Progress: 32% (52/160 tasks complete)
├─ Agent: Beauty Agent (qwen-beauty-wellness)
├─ Task Distribution:
│  ✅ Entity Formation: 41/41 (100%)
│  ✅ Tax Setup: 41/41 (100%)
│  ✅ Monetization: 39/41 (95%)
│  ⏳ MVP Build: 8/41 (20%)
│  ⏳ Go-to-Market: 0/41 (0%)
└─ ETA for Sector Launch: 2026-05-20
```

### Global Queue View
```
All Tasks: 4,977 total
├─ ✅ Complete: 278 (5.6%)
├─ ⏳ Running: 47 (0.9%)
├─ ⏳ Pending: 4,652 (93.5%)
├─ ❌ Failed: 0 (0%)
└─ ETA to 50% Complete: 2026-05-16
```

---

## Integration Points (What Agents Can Do)

### GitHub Integration
- Create repos for each venture
- Commit code + SOPs + documentation
- Create PRs for review
- Update README with venture info

### Supabase Integration
- Read venture definitions + product data
- Update progress_pct, status, assigned_agent
- Write task results + completion timestamps
- Read historical task results for context

### Notion Integration
- Create venture dashboards
- Update status pages
- Post completion notifications
- Track blockers + escalations

### Slack Integration
- Daily summary: "X tasks complete, Y tasks started, Z tasks blocked"
- Task completion notifications: "BW-001 MVP build complete!"
- Error alerts: "Task failed, needs human review"
- Escalation notifications: "Finance approval needed for $50K+"

### Make.com Integration
- Trigger next-phase task when current task completes
- Create webhooks for external systems
- Route information to other tools
- Conditional workflows (e.g., "if funding approved, trigger growth phase")

---

## Error Handling & Escalation

### 3-Strike Retry Protocol
```
Attempt 1: Agent tries task
  → If fails: Log error, retry in 1 hour
  
Attempt 2: Agent retries with modified approach
  → If fails: Log error, notify human
  
Attempt 3: Human reviews + provides guidance
  → If still fails: Task marked "needs_review"
  → Escalate to Finance/Legal/CEO based on task type
```

### Escalation Rules
```
Task type: entity_formation
  Blocks: All subsequent tasks (critical)
  Escalate to: Finance Manager
  
Task type: grant_applications
  Blocks: Funding tasks only
  Escalate to: CFO
  
Task type: mvp_build (tech_sector)
  Blocks: Go-to-market tasks
  Escalate to: Tech Manager + CTO (if needed)
  
Task type: go_to_market
  Blocks: Launch
  Escalate to: Sales Head / Head of Growth
```

---

## Next Steps to Execute

### Step 1: Build Master Orchestrator (Claude Code)
- Initialize Supabase client
- Implement claim/route/execute/result loop
- Set up error handling
- Deploy on Mac Studio

### Step 2: Build Dashboard (Supabase + Notion)
- Add progress_pct to ventures table
- Create Notion dashboard with venture progress cards
- Add sector aggregate views
- Real-time metrics

### Step 3: Wire Agents (By Sector)
- Finance Agent: entity_formation, tax_setup, grants, monetization
- Beauty Agent: beauty-specific MVP + content + GTM
- [etc for each sector]

### Step 4: Integration Testing
- Test single task end-to-end (claim → execute → result)
- Test parallel execution (50 tasks at once)
- Test error handling + retry logic
- Monitor performance

### Step 5: Full Deployment
- Enable swarm runner on all 4,977 tasks
- Monitor dashboard for real-time progress
- Handle escalations as they emerge
- Adjust parallelization based on system load

---

## Success Metrics

| Metric | Target | Trigger |
|--------|--------|---------|
| Tasks complete (daily) | 100-200 | Swarm running smoothly |
| Tasks complete (weekly) | 500-1000 | Scale to full capacity |
| Venture progress (avg) | 50% by 2026-05-20 | Halfway through pipeline |
| First revenue-generating ventures | 10+ | Launch complete |
| Fully automated ventures | 100+ | All 10 phases complete |

---

**Status:** Ready to build

The infrastructure exists. The agents are defined. The tasks are queued.

Next: Build the execution loop.
