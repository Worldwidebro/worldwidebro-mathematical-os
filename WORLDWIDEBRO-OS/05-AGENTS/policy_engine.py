#!/usr/bin/env python3
"""PolicyEngine — Central policy enforcement for agents."""

import os
import json
from datetime import datetime, timedelta
from typing import Optional, Dict, Any, Tuple

class PolicyEngine:
    def __init__(self, supabase_client):
        self.client = supabase_client
        self.policies = self._load_policies()

    def _load_policies(self) -> Dict[str, Any]:
        """Load agent policies from permissions.json"""
        dir_path = os.path.dirname(os.path.realpath(__file__))
        permissions_path = os.path.join(dir_path, 'permissions.json')
        try:
            with open(permissions_path) as f:
                return json.load(f)
        except Exception:
            return {}

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
        limit = policy.get('cost_limit_per_month', 0.0)

        try:
            result = self.client.table('agent_cost_log').select('amount').eq(
                'agent_id', agent_id
            ).gte('created_at', self._month_start()).execute()
            
            current_spend = sum(float(row.get('amount', 0.0)) for row in result.data) if result.data else 0.0
            return (current_spend + amount) <= limit
        except Exception as e:
            # Fallback to true if table not created yet to prevent blocking bootstrap
            print(f"PolicyEngine warning (can_spend): {e}")
            return True

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

        try:
            result = self.client.table('agent_call_log').select('id').eq(
                'agent_id', agent_id
            ).gte('created_at', self._one_minute_ago()).execute()
            
            count = len(result.data) if result.data else 0
            return count < limit
        except Exception as e:
            print(f"PolicyEngine warning (_check_rate_limit): {e}")
            return True

    def _month_start(self) -> str:
        """First day of current month."""
        now = datetime.now()
        return now.replace(day=1, hour=0, minute=0, second=0).isoformat()

    def _one_minute_ago(self) -> str:
        """Timestamp from 1 minute ago."""
        return (datetime.now() - timedelta(minutes=1)).isoformat()

    def audit(self, agent_id: str, tool: str, allowed: bool, reason: Optional[str]) -> None:
        """Log decision for audit trail."""
        try:
            self.client.table('policy_decisions').insert({
                'agent_id': agent_id,
                'tool': tool,
                'allowed': allowed,
                'denial_reason': reason
            }).execute()
        except Exception as e:
            print(f"PolicyEngine audit error: {e}")
