#!/usr/bin/env python3
import os
import sys
import json
from datetime import datetime
from typing import Dict, Any, List

class GovernanceEngine:
    def __init__(self):
        self.audit_log_path = "/Users/acebless/Documents/Gemini/reports/governance_audit.jsonl"
        os.makedirs(os.path.dirname(self.audit_log_path), exist_ok=True)

    def check_policy(self, user_role: str, action: str, resource_sector: str, details: Dict[str, Any] = None) -> Dict[str, Any]:
        """Simple compliance evaluation rules for GDPR and RBAC mapping."""
        if details is None:
            details = {}

        # Rule 1: Admins can do anything
        if user_role == "admin":
            return {"allowed": True, "reason": "Admin role bypass restrictions"}

        # Rule 2: Agents can only read/write from their matching sector
        if user_role == "agent":
            agent_sector = details.get("agent_sector", "")
            if agent_sector == resource_sector:
                return {"allowed": True, "reason": "Agent sector aligns with resource sector"}
            else:
                return {
                    "allowed": False, 
                    "reason": f"Access Denied: Agent sector '{agent_sector}' does not match resource sector '{resource_sector}'"
                }

        # Rule 3: GDPR data retention rules
        if action == "store_pii":
            retention_days = details.get("retention_days", 0)
            if retention_days > 365:
                return {
                    "allowed": False,
                    "reason": f"GDPR Violation: Personal Identifiable Information (PII) retention ({retention_days} days) exceeds limit of 365 days"
                }

        return {"allowed": False, "reason": "No policy matched allow rules"}

    def log_decision(self, user: str, action: str, resource: str, status: str, details: str):
        log_entry = {
            "timestamp": str(datetime.now()),
            "user": user,
            "action": action,
            "resource": resource,
            "status": status,
            "details": details
        }
        try:
            with open(self.audit_log_path, 'a', encoding='utf-8') as f:
                f.write(json.dumps(log_entry) + '\n')
        except Exception as e:
            print(f"Failed to write audit log: {e}")

    def get_audit_trail(self, limit=100) -> List[Dict[str, Any]]:
        if not os.path.exists(self.audit_log_path):
            return []
        
        logs = []
        try:
            with open(self.audit_log_path, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip():
                        logs.append(json.loads(line))
            return logs[-limit:]
        except Exception as e:
            print(f"Error reading audit log: {e}")
            return []

if __name__ == '__main__':
    gov = GovernanceEngine()
    chk = gov.check_policy("agent", "read", "beauty", {"agent_sector": "beauty"})
    print("Allowed? ", chk["allowed"], " - Reason: ", chk["reason"])
