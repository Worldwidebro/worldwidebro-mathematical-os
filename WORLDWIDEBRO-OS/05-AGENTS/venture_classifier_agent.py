#!/usr/bin/env python3
"""venture_classifier_agent.py — AI agent for classifying and routing ventures/leads."""

import os
import sys
import json
import psycopg2
from datetime import datetime
from typing import Any, Dict

# Resolve package directory to find policy_engine and event_bus
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from policy_engine import PolicyEngine
from event_bus import EventBus

# Defaults
POSTGRES_URL = os.environ.get("PG_URL", "postgresql://divinejohns@100.87.214.70:5432/iza_os_ventures")

class PGClientWrapper:
    """Wrapper that translates Supabase JS-like calls into SQL queries."""
    def __init__(self, conn):
        self.conn = conn

    def table(self, table_name: str):
        return PGTableWrapper(self.conn, table_name)

class PGTableWrapper:
    def __init__(self, conn, table_name: str):
        self.conn = conn
        self.table_name = table_name
        self.filters = {}
        self.gte_filters = {}

    def select(self, columns: str):
        return self

    def eq(self, field: str, value: Any):
        self.filters[field] = value
        return self

    def gte(self, field: str, value: Any):
        self.gte_filters[field] = value
        return self

    def insert(self, data: Dict):
        if not self.conn:
            return self
        try:
            cursor = self.conn.cursor()
            # Ensure table exists
            if self.table_name == 'policy_decisions':
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS policy_decisions (
                  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                  agent_id TEXT NOT NULL,
                  tool TEXT NOT NULL,
                  allowed BOOLEAN NOT NULL,
                  denial_reason TEXT,
                  created_at TIMESTAMP DEFAULT NOW()
                );
                """)
            
            fields = list(data.keys())
            values = list(data.values())
            placeholders = ", ".join(["%s"] * len(fields))
            sql = f"INSERT INTO {self.table_name} ({', '.join(fields)}) VALUES ({placeholders})"
            cursor.execute(sql, tuple(values))
            self.conn.commit()
            cursor.close()
        except Exception as e:
            print(f"PGTableWrapper insert error for {self.table_name}: {e}")
        return self

    def execute(self):
        class Result:
            def __init__(self, data):
                self.data = data
        
        if not self.conn:
            return Result([])

        try:
            cursor = self.conn.cursor()
            # Ensure tables exist
            if self.table_name == 'agent_cost_log':
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS agent_cost_log (
                  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                  agent_id TEXT NOT NULL,
                  tool TEXT NOT NULL,
                  amount DECIMAL(10, 2) NOT NULL,
                  created_at TIMESTAMP DEFAULT NOW()
                );
                """)
            elif self.table_name == 'agent_call_log':
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS agent_call_log (
                  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                  agent_id TEXT NOT NULL,
                  tool TEXT NOT NULL,
                  created_at TIMESTAMP DEFAULT NOW()
                );
                """)

            sql = f"SELECT * FROM {self.table_name}"
            where_clauses = []
            params = []
            
            for k, v in self.filters.items():
                where_clauses.append(f"{k} = %s")
                params.append(v)
            for k, v in self.gte_filters.items():
                where_clauses.append(f"{k} >= %s")
                params.append(v)
                
            if where_clauses:
                sql += " WHERE " + " AND ".join(where_clauses)
                
            cursor.execute(sql, tuple(params))
            colnames = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            cursor.close()
            
            data = [dict(zip(colnames, row)) for row in rows]
            return Result(data)
        except Exception as e:
            print(f"PGTableWrapper execute error for {self.table_name}: {e}")
            return Result([])

class VentureClassifierAgent:
    def __init__(self):
        self.agent_id = "venture_classifier"
        try:
            self.db_conn = psycopg2.connect(POSTGRES_URL)
            self.client = PGClientWrapper(self.db_conn)
        except Exception as e:
            print(f"Agent warning (DB connection failed): {e}")
            self.client = PGClientWrapper(None)
            
        self.policy_engine = PolicyEngine(self.client)
        self.event_bus = EventBus()

    def run_preflight(self, tool_name: str, params: dict) -> bool:
        """Enforce PolicyEngine pre-flight checks."""
        allowed, reason = self.policy_engine.pre_flight_check(self.agent_id, tool_name, params)
        self.policy_engine.audit(self.agent_id, tool_name, allowed, reason)
        if not allowed:
            print(f"🚫 [VentureClassifier] Denied {tool_name}: {reason}")
            return False
        return True

    def classify(self, name: str, description: str, sector: str) -> dict:
        """Classify a venture/lead and log results."""
        print(f"🤖 [VentureClassifier] Classifying lead: {name} ({sector})")
        
        # Enforce database check before accessing tables
        if not self.run_preflight("postgres", {"table": "ventures"}):
            return {"error": "Policy rejection"}

        text = f"{name} {description} {sector}".lower()
        
        # Archetype classification
        archetype = "general"
        confidence = 0.5
        
        if any(w in text for w in ["marketplace", "gig", "contractor", "matching"]):
            archetype = "marketplace"
            confidence = 0.95
        elif any(w in text for w in ["saas", "productivity", "management", "collaboration"]):
            archetype = "saas_tool"
            confidence = 0.90
        elif any(w in text for w in ["fintech", "payment", "banking", "money"]):
            archetype = "fintech_wealth"
            confidence = 0.92
        elif any(w in text for w in ["health", "fitness", "wellness"]):
            archetype = "health_wellness"
            confidence = 0.88

        result = {
            "name": name,
            "sector": sector,
            "archetype": archetype,
            "confidence": confidence,
            "classified_at": datetime.now().isoformat()
        }

        # Log classification to PG database
        try:
            if self.db_conn:
                cursor = self.db_conn.cursor()
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS venture_classifications (
                  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                  name TEXT NOT NULL,
                  sector TEXT NOT NULL,
                  archetype TEXT NOT NULL,
                  confidence DECIMAL(4,3),
                  created_at TIMESTAMP DEFAULT NOW()
                );
                """)
                cursor.execute(
                    "INSERT INTO venture_classifications (name, sector, archetype, confidence) VALUES (%s, %s, %s, %s)",
                    (name, sector, archetype, confidence)
                )
                self.db_conn.commit()
                cursor.close()
                print("  ✅ Classification logged to Database")
        except Exception as e:
            print(f"  ⚠️ DB insert failed: {e}")

        # Send Slack update mock
        if self.run_preflight("slack", {"estimated_cost": 0.01}):
            print(f"  💬 [Slack] Routed lead '{name}' to #{sector}-venture channel")

        return result

    def start_listener(self):
        """Subscribe to lead_intake event channel."""
        def handle_lead(payload):
            name = payload.get("name", "Unknown Lead")
            desc = payload.get("description", "")
            sector = payload.get("sector", "general")
            self.classify(name, desc, sector)

        self.event_bus.listen({"lead_intake": handle_lead})

if __name__ == "__main__":
    # Test script execution
    agent = VentureClassifierAgent()
    if "--test" in sys.argv:
        print("🧪 Running VentureClassifierAgent local test...")
        test_lead = {
            "name": "Ace Staffing Agency LLC",
            "description": "A 2-sided marketplace matching contractors to local businesses",
            "sector": "staffing"
        }
        res = agent.classify(test_lead["name"], test_lead["description"], test_lead["sector"])
        print("Test Classification Result:")
        print(json.dumps(res, indent=2))
        print("🧪 Test completed successfully!")
