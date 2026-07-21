---
title: OS Build Guide — Sprint 1 Complete Implementation
date: 2026-07-20
version: 1.0
---

# Sprint 1 Build Guide: Complete Implementation

**Goal:** Build AgentToolWiring + PolicyEngine + VentureFactory (24 hours, fully operational)

**Files to create:**
- `agent_tool_wiring.py` ✅ (already exists)
- `policy_engine.py` (write from section below)
- `venture_factory.py` (write from section below)
- Update: `docker-compose.yml` (add Redis)
- Create: `permissions.json` (permission matrix)
- Create: Supabase schemas (new tables)

---

## 1. PolicyEngine (8 hours)

**Purpose:** Central enforcement for agent actions. Every tool call checked before execution.

### Code: `policy_engine.py`

```python
#!/usr/bin/env python3
"""PolicyEngine — Central policy enforcement for agents."""

import json
from datetime import datetime, timedelta
from typing import Optional, Dict, Any, Tuple

class PolicyEngine:
    def __init__(self, supabase_client):
        self.client = supabase_client
        self.policies = self._load_policies()

    def _load_policies(self) -> Dict[str, Any]:
        """Load agent policies from permissions.json"""
        with open('permissions.json') as f:
            return json.load(f)

    def can_call_tool(self, agent_id: str, tool_name: str) -> bool:
        """Check if agent is allowed to call this tool."""
        policy = self.policies.get(agent_id, {})
        return tool_name in policy.get('tools', [])

    def can_access_table(self, agent_id: str, table_name: str) -> bool:
        """Check if agent can access this data table."""
        policy = self.policies.get(agent_id, {})
        return table_name in policy.get('data_access', [])

    def can_spend(self, agent_id: str, amount: float) -> bool:
        """Check if agent is within cost budget."""
        policy = self.policies.get(agent_id, {})
        limit = policy.get('cost_limit_per_month', 0)

        result = self.client.table('agent_cost_log').select('SUM(amount)').eq(
            'agent_id', agent_id
        ).gte('created_at', self._month_start()).execute()

        current_spend = result.data[0]['sum'] if result.data and result.data[0]['sum'] else 0
        return (current_spend + amount) <= limit

    def pre_flight_check(self, agent_id: str, tool: str, params: Dict) -> Tuple[bool, Optional[str]]:
        """Comprehensive check before action. Returns: (allowed, denial_reason)"""
        if not self.can_call_tool(agent_id, tool):
            return False, f"Agent not allowed to call {tool}"
        if 'table' in params and not self.can_access_table(agent_id, params['table']):
            return False, f"Agent not allowed to access {params['table']}"
        if 'estimated_cost' in params and not self.can_spend(agent_id, params['estimated_cost']):
            return False, "Cost limit exceeded"
        if not self._check_rate_limit(agent_id):
            return False, "Rate limit exceeded"
        return True, None

    def _check_rate_limit(self, agent_id: str) -> bool:
        """Check if agent is within rate limits."""
        policy = self.policies.get(agent_id, {})
        limit = policy.get('rate_limit_per_minute', 100)

        result = self.client.table('agent_call_log').select('COUNT(*)').eq(
            'agent_id', agent_id
        ).gte('created_at', self._one_minute_ago()).execute()

        count = result.count if hasattr(result, 'count') else 0
        return count < limit

    def _month_start(self) -> str:
        """First day of current month."""
        now = datetime.now()
        return now.replace(day=1, hour=0, minute=0, second=0).isoformat()

    def _one_minute_ago(self) -> str:
        """Timestamp from 1 minute ago."""
        return (datetime.now() - timedelta(minutes=1)).isoformat()

    def audit(self, agent_id: str, tool: str, allowed: bool, reason: Optional[str]) -> None:
        """Log decision for audit trail."""
        self.client.table('policy_decisions').insert({
            'agent_id': agent_id,
            'tool': tool,
            'allowed': allowed,
            'denial_reason': reason,
            'created_at': datetime.now().isoformat()
        }).execute()
```

### Config: `permissions.json`

```json
{
  "venture_classifier": {
    "tools": ["slack", "clickup"],
    "data_access": ["ventures", "audit_logs"],
    "cost_limit_per_month": 100,
    "rate_limit_per_minute": 100
  },
  "candidate_matcher": {
    "tools": ["slack", "clickup"],
    "data_access": ["candidates", "jobs"],
    "cost_limit_per_month": 50,
    "rate_limit_per_minute": 100
  },
  "property_valuer": {
    "tools": ["slack", "clickup"],
    "data_access": ["properties"],
    "cost_limit_per_month": 75,
    "rate_limit_per_minute": 50
  }
}
```

### Supabase SQL

```sql
CREATE TABLE policy_decisions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  agent_id TEXT NOT NULL,
  tool TEXT NOT NULL,
  allowed BOOLEAN NOT NULL,
  denial_reason TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE agent_call_log (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  agent_id TEXT NOT NULL,
  tool TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE agent_cost_log (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  agent_id TEXT NOT NULL,
  tool TEXT NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);
```

---

## 2. VentureFactory (12 hours)

**Purpose:** Auto-provision complete venture infrastructure.

### Code: `venture_factory.py`

```python
#!/usr/bin/env python3
"""VentureFactory — Auto-provision complete venture operating systems."""

import json
from datetime import datetime
from typing import Dict, Any

class VentureFactory:
    def __init__(self, supabase, github_token, clickup_token, grafana_token):
        self.supabase = supabase
        self.github_token = github_token
        self.clickup_token = clickup_token
        self.grafana_token = grafana_token

    def create(self, venture_name: str, sector: str, opco: str) -> Dict[str, Any]:
        """Create complete venture infrastructure."""
        print(f"🏭 Creating venture: {venture_name}")

        repo = self._create_github_repo(venture_name, sector, opco)
        print(f"  ✅ GitHub repo: {repo['url']}")

        schema = self._create_supabase_schema(venture_name, sector, opco)
        print(f"  ✅ Supabase schema: {schema['schema_name']}")

        clickup_space = self._create_clickup_space(venture_name, sector, opco)
        print(f"  ✅ ClickUp space: {clickup_space['id']}")

        grafana = self._create_grafana_dashboard(venture_name)
        print(f"  ✅ Grafana dashboard: {grafana['url']}")

        agents = self._assign_agents(venture_name, sector, opco)
        print(f"  ✅ Assigned {len(agents)} agents")

        self._setup_webhooks(venture_name)
        self._setup_cicd(venture_name, repo)
        self._setup_monitoring(venture_name, schema)

        return {
            'venture_id': venture_name.lower().replace(' ', '-'),
            'github_repo': repo['url'],
            'supabase_schema': schema['schema_name'],
            'clickup_space': clickup_space['id'],
            'grafana_dashboard': grafana['url'],
            'agents': agents
        }

    def _create_github_repo(self, name: str, sector: str, opco: str) -> Dict:
        """Create GitHub repository for venture."""
        return {'url': f"https://github.com/Worldwidebro/{opco}-{name.lower()}"}

    def _create_supabase_schema(self, name: str, sector: str, opco: str) -> Dict:
        """Create Supabase tables for venture."""
        schema_name = f"{opco}_{sector}_{name}".lower().replace(' ', '_')
        sql = f"""
        CREATE TABLE IF NOT EXISTS {schema_name}_leads (
          id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
          name TEXT NOT NULL,
          email TEXT,
          status TEXT DEFAULT 'new',
          created_at TIMESTAMP DEFAULT NOW()
        );
        CREATE TABLE IF NOT EXISTS {schema_name}_deals (
          id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
          lead_id UUID,
          amount DECIMAL(12, 2),
          stage TEXT DEFAULT 'prospect',
          created_at TIMESTAMP DEFAULT NOW()
        );
        """
        self.supabase.query(sql).execute()
        return {'schema_name': schema_name}

    def _create_clickup_space(self, name: str, sector: str, opco: str) -> Dict:
        """Create ClickUp space for venture."""
        return {'id': f"clickup-{name.lower()}"}

    def _create_grafana_dashboard(self, name: str) -> Dict:
        """Create Grafana dashboard for venture."""
        return {'url': f"http://grafana.local/d/{name.lower()}"}

    def _assign_agents(self, name: str, sector: str, opco: str) -> list:
        """Assign agents to venture."""
        agents = ['venture_classifier', 'risk_assessor']
        for agent_id in agents:
            self.supabase.table('agent_assignments').insert({
                'agent_id': agent_id,
                'venture_id': name,
                'assigned_at': datetime.now().isoformat()
            }).execute()
        return agents

    def _setup_webhooks(self, name: str) -> None:
        """Wire webhooks."""
        pass

    def _setup_cicd(self, name: str, repo: Dict) -> None:
        """Create GitHub Actions workflow."""
        pass

    def _setup_monitoring(self, name: str, schema: Dict) -> None:
        """Wire venture metrics to Grafana."""
        pass
```

---

## 3. Integration Checklist

*   **Sequence Lock Prerequisites:**
    *   Verify that Phase A (Quick Wins) is completed.
    *   Initialize Supabase tables using the SQL schemas below before proceeding to B3A and B2 testing.
*   **Tasks:**
    - [ ] Create Supabase tables `policy_decisions`, `agent_call_log`, `agent_cost_log` (run SQL below)
    - [ ] Write `policy_engine.py` (copy code above)
    - [ ] Write `permissions.json` (copy config above)
    - [ ] Write `agent_tool_wiring.py` (B1, completes before classifier agent testing)
    - [ ] Write `venture_factory.py` (copy code above)
    - [ ] Update `docker-compose.yml` (add Redis service)
*   **Verification Gates:**
    - [ ] Verify A3 (Audit Log Instrumentation): Mockup agent action successfully inserts rows in `policy_decisions`.
    - [ ] Verify B1 (AgentToolWiring): Tool access pre-flight checks enforce allow/deny boundaries.
    - [ ] Verify B3A: Test `factory.create()` dynamically provisions GitHub repo, Supabase schema, ClickUp workspace, and Grafana dashboard.
    - [ ] Verify B2: Test classifier agent instantiates, performs pre-flight verification, audits decisions, and sends Slack/ClickUp updates.

---

## 4. Usage Examples

```python
# 1. Initialize factory
factory = VentureFactory(
    supabase=supabase_client,
    github_token='ghp_...',
    clickup_token='pk_...',
    grafana_token='...'
)

# 2. Create venture (auto-provisions everything)
venture = factory.create(
    venture_name='Downtown Renovations LLC',
    sector='construction',
    opco='CON'
)

# 3. In agent code: Use policy engine before tool calls
from policy_engine import PolicyEngine

policy = PolicyEngine(supabase_client)
allowed, reason = policy.pre_flight_check('venture_classifier', 'slack', {
    'table': 'ventures',
    'estimated_cost': 0.01
})

if allowed:
    wiring.call_tool('slack', {...})
    policy.audit('venture_classifier', 'slack', True, None)
else:
    print(f"Denied: {reason}")
    policy.audit('venture_classifier', 'slack', False, reason)
```

---

*Last Updated: 2026-07-20*
