# Hermes Command Center

AI Organization Operations Dashboard powered by real agent, task, and decision data from Supabase.

## Features

- **Live Agent Metrics** — Real-time status from `aoc_agents`, `agent_assignments`, `venture_agent_assignments`
- **Task Tracking** — Running tasks from `agent_tasks`
- **Decision Timeline** — Pending decisions from `agent_decisions`
- **Skill Execution** — Performance metrics from `skill_executions`
- **ISR (Incremental Static Regeneration)** — Dashboard updates every 60 seconds

## Queries

- `aoc_agents` → Active agents + status
- `agent_tasks` → Running tasks by status
- `agent_decisions` → Pending decisions
- `skill_executions` → Skill metrics
- `agent_assignments` → Team/OPCO assignments

## Deployment

### Local Development

```bash
cd /Users/acebless/Documents/hermes-command-center
npm install
cp .env.example .env.local
# Edit .env.local with your Supabase ANON_KEY
npm run dev
```

Open [http://localhost:3000](http://localhost:3000)

### Deploy to Vercel

1. Push to GitHub:
```bash
cd /Users/acebless/Documents/hermes-command-center
git init
git add .
git commit -m "Initial Hermes dashboard"
git branch -M main
git remote add origin https://github.com/yourusername/hermes-command-center.git
git push -u origin main
```

2. Deploy via Vercel:
- Go to [vercel.com](https://vercel.com)
- Click "Add New..." → "Project"
- Import the GitHub repo
- Add environment variable: `NEXT_PUBLIC_SUPABASE_ANON_KEY=<your-key>`
- Click "Deploy"

3. Your dashboard will be live at: `https://hermes-command-center-yourusername.vercel.app`

## Environment Variables

Required in Vercel Settings:

```
NEXT_PUBLIC_SUPABASE_URL=https://cyhzilqldouzgynacqpe.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_anon_key_here
```

Get your anon key from Supabase Settings → API Keys

## Data Refresh

- Dashboard refreshes every 60 seconds via ISR
- Manual refresh in browser (Cmd/Ctrl + R)
- All queries are read-only (safe)

## Architecture

```
page.tsx (Server Component)
├── getAgents() → aoc_agents
├── getAgentTasks() → agent_tasks
├── getAgentDecisions() → agent_decisions
└── getSkillExecutions() → skill_executions
```

Each query has error handling — missing tables return empty arrays.
