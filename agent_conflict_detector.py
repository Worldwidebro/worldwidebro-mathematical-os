#!/usr/bin/env python3
"""
Agent Conflict Detector
Analyzes Paperclip agents for overlapping decision logic and responsibility duplication.
Identifies conflicts that could cause coordination failures or duplicate work.
"""

import os
import json
import requests
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime

# Config
PAPERCLIP_API = os.getenv("PAPERCLIP_API", "http://localhost:3101/api")
COMPANY_ID = os.getenv("PAPERCLIP_COMPANY_ID", "1450a240-2be1-4dc6-b74c-ada307ca6ddb")
SUPABASE_URL = os.getenv("SUPABASE_URL", "https://iefnvvfxbnpxfcggzljq.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")

# Responsibility keywords to extract from prompts
RESPONSIBILITY_KEYWORDS = {
    "decision_making": ["decision", "decide", "approve", "authorize", "escalate"],
    "metrics": ["track", "monitor", "calculate", "measure", "metric", "kpi", "health"],
    "capital": ["capital", "budget", "allocate", "spending", "resource"],
    "venture_ops": ["venture", "escalate", "execute", "route", "coordinate"],
    "financial": ["roi", "margin", "cac", "ltv", "burn", "revenue", "cost"],
    "strategic": ["strategic", "plan", "vision", "roadmap", "portfolio"],
    "risk": ["risk", "flag", "alert", "intervention", "underperform"],
}

@dataclass
class AgentProfile:
    """Agent's responsibilities and decision logic"""
    agent_id: str
    name: str
    role: str
    system_prompt: str
    responsibilities: Dict[str, List[str]]
    budget: float

@dataclass
class ConflictReport:
    """Detected conflict between two agents"""
    agent_a: str
    agent_b: str
    conflict_type: str  # "responsibility_overlap" | "circular_escalation" | "decision_duplication"
    severity: str  # "high" | "medium" | "low"
    description: str
    impact: str
    recommendation: str


class AgentConflictDetector:
    """Main conflict detection system"""

    def __init__(self):
        self.session = requests.Session()
        self.agents: List[AgentProfile] = []
        self.conflicts: List[ConflictReport] = []

    def fetch_agents(self) -> List[Dict]:
        """Fetch all agents from Paperclip"""
        try:
            response = self.session.get(
                f"{PAPERCLIP_API}/companies/{COMPANY_ID}/agents",
                timeout=10
            )
            if response.status_code == 200:
                return response.json()
            else:
                print(f"❌ Failed to fetch agents: {response.status_code}")
                return []
        except Exception as e:
            print(f"❌ Error fetching agents: {e}")
            return []

    def get_role_responsibilities(self, role: str) -> Dict[str, List[str]]:
        """Get standard responsibilities for agent role"""

        role_map = {
            "ceo": {
                "decision_making": ["Strategic capital allocation", "Portfolio optimization", "ROI-based venture decisions"],
                "capital": ["Budget approval", "Resource allocation"],
                "strategic": ["Long-term vision", "Portfolio strategy"],
            },
            "cto": {
                "venture_ops": ["Day-to-day coordination", "Process automation", "Task routing"],
                "metrics": ["Operational KPI tracking", "Venture health monitoring"],
            },
            "cfo": {
                "financial": ["CAC/LTV calculation", "Margin analysis", "Revenue forecasting"],
                "metrics": ["Financial metric tracking", "Performance analysis"],
                "risk": ["Burn rate monitoring", "Financial risk flagging"],
            },
            "pm": {
                "venture_ops": ["Sector-specific operations", "Venture health monitoring"],
                "strategic": ["Market analysis", "Growth strategy"],
                "risk": ["Risk escalation to CEO"],
            }
        }

        return role_map.get(role, {})

    def extract_responsibilities(self, text: str) -> Dict[str, List[str]]:
        """Extract responsibility categories from agent prompt (fallback)"""
        responsibilities = {}

        if not text:
            return responsibilities

        text_lower = text.lower()

        for category, keywords in RESPONSIBILITY_KEYWORDS.items():
            found = []
            for keyword in keywords:
                if keyword in text_lower:
                    # Extract sentence containing keyword
                    for sentence in text.split('.'):
                        if keyword in sentence.lower():
                            cleaned = sentence.strip()
                            if cleaned and cleaned not in found:
                                found.append(cleaned)
                                break

            if found:
                responsibilities[category] = found

        return responsibilities

    def analyze_agents(self):
        """Analyze all agents for conflicts"""
        agent_data = self.fetch_agents()

        if not agent_data:
            print("❌ No agents found. Is Paperclip running?")
            return

        print(f"\n📊 Analyzing {len(agent_data)} agents...\n")

        # Profile each agent
        role_counts = {}
        for agent in agent_data:
            role = agent.get("role", "unknown")
            role_counts[role] = role_counts.get(role, 0) + 1

            profile = AgentProfile(
                agent_id=agent.get("id", "unknown"),
                name=agent.get("name", "Unknown"),
                role=role,
                system_prompt=agent.get("system_prompt", ""),
                responsibilities=self.get_role_responsibilities(role),
                budget=agent.get("budgetMonthlyCents", 0) / 100
            )
            self.agents.append(profile)
            print(f"✓ Profiled: {profile.name} ({profile.role})")

        # Check for duplicate roles
        print()
        for role, count in role_counts.items():
            if count > 1:
                print(f"⚠️  WARNING: {count} agents with role '{role}' - should have exactly 1")

        print(f"\n🔍 Detecting conflicts...\n")

        # Check for conflicts
        for i, agent_a in enumerate(self.agents):
            for agent_b in self.agents[i+1:]:
                self.detect_conflicts_between(agent_a, agent_b)

    def detect_conflicts_between(self, agent_a: AgentProfile, agent_b: AgentProfile):
        """Check for conflicts between two agents"""

        # Find overlapping responsibility categories
        overlap = set(agent_a.responsibilities.keys()) & set(agent_b.responsibilities.keys())

        if not overlap:
            return

        for category in overlap:
            conflict = self.build_conflict_report(agent_a, agent_b, category)
            if conflict:
                self.conflicts.append(conflict)

    def build_conflict_report(self, agent_a: AgentProfile, agent_b: AgentProfile, category: str) -> Optional[ConflictReport]:
        """Build conflict report for overlapping category"""

        # Determine conflict type and severity based on category
        conflict_type = "responsibility_overlap"
        severity = "medium"

        if category == "decision_making":
            severity = "high"
            conflict_type = "decision_duplication"
        elif category == "financial" and category in ["metrics", "capital"]:
            severity = "high"
            conflict_type = "circular_escalation"
        elif category in ["risk", "metrics"]:
            severity = "medium"
        else:
            severity = "low"

        # Special handling for specific agent pairs
        if agent_a.role == "ceo" and agent_b.role in ["cto", "cfo"]:
            # CEO shouldn't be duplicating subordinate work
            severity = "high"

        if agent_a.role == agent_b.role and agent_a.role == "pm":
            # Different sector PMs managing ventures in same category
            severity = "low"

        description = f"Both {agent_a.name} and {agent_b.name} claim responsibility for {category}"

        impact = self._assess_impact(agent_a, agent_b, category)
        recommendation = self._recommend_resolution(agent_a, agent_b, category)

        return ConflictReport(
            agent_a=agent_a.name,
            agent_b=agent_b.name,
            conflict_type=conflict_type,
            severity=severity,
            description=description,
            impact=impact,
            recommendation=recommendation
        )

    def _assess_impact(self, agent_a: AgentProfile, agent_b: AgentProfile, category: str) -> str:
        """Assess impact of conflict"""

        if category == "decision_making":
            return "May cause conflicting decisions or approval delays"
        elif category == "metrics":
            return "May cause metric inconsistencies across reports"
        elif category == "capital":
            return "May result in budget conflicts or double-allocation"
        elif category == "financial":
            return "May cause inconsistent financial forecasting"
        elif category == "risk":
            return "May cause critical risks to be missed or over-escalated"
        else:
            return f"Unclear responsibility boundary for {category}"

    def _recommend_resolution(self, agent_a: AgentProfile, agent_b: AgentProfile, category: str) -> str:
        """Recommend resolution"""

        # Rule-based recommendations
        if agent_a.role == "ceo" and agent_b.role in ["cfo", "cto"]:
            return f"CEO should delegate {category} decisions to {agent_b.name}. Update CEO prompt to remove this category."

        if agent_b.role == "ceo" and agent_a.role in ["cfo", "cto"]:
            return f"CEO should delegate {category} decisions to {agent_a.name}. Update CEO prompt to remove this category."

        if agent_a.role == "cfo" and agent_b.role == "cto":
            return f"CFO owns {category} for all ventures. CTO should escalate to CFO instead of acting independently."

        if agent_a.role == "pm" and agent_b.role == "pm":
            return f"Sector PMs should coordinate on cross-sector {category} via Operations Manager."

        if "analyst" in agent_a.name.lower() or "analyst" in agent_b.name.lower():
            return f"Analyst should own {category} calculations. Others should request via API/workflow."

        return f"Clarify decision boundary: who owns {category}? Document in decision framework."

    def print_report(self):
        """Print conflict summary"""

        print(f"\n{'='*80}")
        print(f"AGENT CONFLICT DETECTION REPORT")
        print(f"{'='*80}\n")

        if not self.conflicts:
            print("✅ No conflicts detected.\n")
            return

        print(f"Found {len(self.conflicts)} conflicts:\n")

        # Group by severity
        by_severity = {"high": [], "medium": [], "low": []}
        for conflict in self.conflicts:
            by_severity[conflict.severity].append(conflict)

        for severity in ["high", "medium", "low"]:
            if by_severity[severity]:
                emoji = {"high": "🔴", "medium": "🟡", "low": "🟢"}[severity]
                print(f"{emoji} {severity.upper()} SEVERITY ({len(by_severity[severity])} issues)\n")

                for conflict in by_severity[severity]:
                    print(f"  {conflict.agent_a} ↔ {conflict.agent_b}")
                    print(f"  Conflict: {conflict.conflict_type}")
                    print(f"  Issue: {conflict.description}")
                    print(f"  Impact: {conflict.impact}")
                    print(f"  → {conflict.recommendation}\n")

        print(f"{'='*80}\n")

    def store_conflicts_in_supabase(self) -> bool:
        """Store conflicts in Supabase for audit trail"""

        if not SUPABASE_KEY:
            print("⚠️  SUPABASE_KEY not set, skipping audit storage")
            return False

        try:
            headers = {
                "Authorization": f"Bearer {SUPABASE_KEY}",
                "Content-Type": "application/json"
            }

            for conflict in self.conflicts:
                record = {
                    "task_type": "agent_conflict_detected",
                    "severity": conflict.severity,
                    "agent_a": conflict.agent_a,
                    "agent_b": conflict.agent_b,
                    "conflict_type": conflict.conflict_type,
                    "description": conflict.description,
                    "impact": conflict.impact,
                    "recommendation": conflict.recommendation,
                    "detected_at": datetime.utcnow().isoformat()
                }

                response = requests.post(
                    f"{SUPABASE_URL}/rest/v1/aoc_tasks",
                    headers=headers,
                    json=record
                )

                if response.status_code not in [200, 201]:
                    print(f"⚠️  Failed to store conflict: {response.status_code}")
                    return False

            print(f"✅ Stored {len(self.conflicts)} conflicts in Supabase")
            return True

        except Exception as e:
            print(f"❌ Error storing conflicts: {e}")
            return False


def main():
    """Run conflict detection"""
    detector = AgentConflictDetector()
    detector.analyze_agents()
    detector.print_report()
    detector.store_conflicts_in_supabase()


if __name__ == "__main__":
    main()
