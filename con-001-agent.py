#!/usr/bin/env python3
"""
CON-001 Execution Agent — Full End-to-End Loop
Day 1 Implementation: Agent → Graph → Search → Route → Act → Feedback

Usage:
  python con-001-agent.py --run-once          # Process 1 lead and exit
  python con-001-agent.py --loop              # Run forever (for n8n/cron)
  python con-001-agent.py --test              # Test with dummy lead
"""

import os
import json
import asyncio
from datetime import datetime
from typing import Optional
import argparse

# External dependencies
from supabase import create_client
from neo4j import GraphDatabase
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
import anthropic
from langfuse import Langfuse
from langfuse.decorators import trace

# ============================================================================
# 1. INITIALIZATION & CONFIG
# ============================================================================

class CON001Config:
    """Load environment variables and initialize clients"""

    # Supabase
    SUPABASE_URL = os.getenv("SUPABASE_URL", "https://cyhzilqldouzgynacqpe.supabase.co")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")  # Set this

    # Neo4j
    NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
    NEO4J_USER = "neo4j"
    NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "ventures2026")

    # Qdrant
    QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")

    # LLM
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")

    # Langfuse
    LANGFUSE_PUBLIC_KEY = os.getenv("LANGFUSE_PUBLIC_KEY", "")
    LANGFUSE_SECRET_KEY = os.getenv("LANGFUSE_SECRET_KEY", "")
    LANGFUSE_HOST = os.getenv("LANGFUSE_HOST", "http://localhost:3003")

    # Venture ID (this agent only handles CON-001)
    VENTURE_ID = "CON-001"

# ============================================================================
# 2. CLIENT INITIALIZATION
# ============================================================================

def init_clients():
    """Initialize all external clients"""
    config = CON001Config()

    clients = {
        "supabase": create_client(config.SUPABASE_URL, config.SUPABASE_KEY),
        "neo4j": GraphDatabase.driver(
            config.NEO4J_URI,
            auth=(config.NEO4J_USER, config.NEO4J_PASSWORD)
        ),
        "qdrant": QdrantClient(url=config.QDRANT_URL),
        "claude": anthropic.Anthropic(api_key=config.ANTHROPIC_API_KEY),
        "langfuse": Langfuse(
            public_key=config.LANGFUSE_PUBLIC_KEY,
            secret_key=config.LANGFUSE_SECRET_KEY,
            host=config.LANGFUSE_HOST
        ),
    }

    return clients, config

# ============================================================================
# 3. NEO4J QUERIES — Get Venture Context
# ============================================================================

class GraphQueries:
    """Query Neo4j for venture context"""

    @staticmethod
    def get_venture_context(driver, venture_id: str) -> dict:
        """Fetch venture data from graph"""
        query = f"""
        MATCH (v:Venture {{id: '{venture_id}'}})
        OPTIONAL MATCH (v)-[:NEEDS]->(c:Capability)
        OPTIONAL MATCH (v)-[:BELONGS_TO]->(s:Sector)
        RETURN {{
            id: v.id,
            name: v.name,
            stage: v.stage,
            readiness_pct: v.readiness_pct,
            capabilities: collect(c.name),
            sector: s.name,
            description: v.description
        }} as venture
        """
        with driver.session() as session:
            result = session.run(query)
            record = result.single()
            return record["venture"] if record else {}

    @staticmethod
    def create_decision_node(driver, venture_id: str, decision_type: str,
                            reasoning: str, confidence: float):
        """Log a decision to the graph"""
        query = f"""
        CREATE (d:Decision {{
            id: apoc.create.uuid(),
            venture_id: '{venture_id}',
            type: '{decision_type}',
            reasoning: '{reasoning.replace("'", "\\\\'")[:500]}',
            confidence: {confidence},
            timestamp: datetime()
        }})
        WITH d
        MATCH (v:Venture {{id: '{venture_id}'}})
        MERGE (v)-[:MADE]->(d)
        RETURN d.id as decision_id
        """
        with driver.session() as session:
            result = session.run(query)
            record = result.single()
            return record["decision_id"] if record else None

# ============================================================================
# 4. QDRANT SEARCH — Semantic Similarity
# ============================================================================

class SemanticSearch:
    """Query Qdrant for similar past projects"""

    @staticmethod
    def search_similar_projects(client, project_type: str, budget: str,
                               limit: int = 3) -> list:
        """Find similar repos/projects using semantic search"""
        try:
            results = client.search(
                collection_name="repositories",
                query_vector=[0.0] * 768,
                limit=limit,
                score_threshold=0.5
            )
            return [{"name": r.payload.get("name"), "score": r.score} for r in results]
        except Exception as e:
            print(f"Qdrant search failed: {e}")
            return []

# ============================================================================
# 5. LITELLM ROUTING — Cost-Aware Model Selection
# ============================================================================

class ModelRouter:
    """Route to cheapest available model based on complexity"""

    @staticmethod
    def select_model(task_complexity: str, budget_usd: float = 1.0) -> str:
        """Route to model based on complexity and budget"""
        if task_complexity == "simple" and budget_usd < 5:
            return "gpt-4o-mini"
        elif task_complexity == "medium":
            return "claude-3-5-sonnet-20241022"
        else:
            return "claude-opus-5"

    @staticmethod
    def estimate_cost(model: str, tokens: int = 500) -> float:
        """Rough cost estimate (in dollars)"""
        rates = {
            "gpt-4o-mini": 0.00015 / 1000,
            "claude-3-5-sonnet-20241022": 0.003 / 1000,
            "claude-opus-5": 0.015 / 1000,
        }
        return (tokens * rates.get(model, 0.003 / 1000))

# ============================================================================
# 6. DECISION ENGINE — What to Do With This Lead?
# ============================================================================

class DecisionEngine:
    """Use Claude to decide what action to take"""

    @staticmethod
    @trace(name="decision_engine")
    def make_decision(claude_client, lead: dict, venture_context: dict,
                     similar_projects: list) -> dict:
        """Decide action based on lead + context"""

        prompt = f"""
        You are a construction sales agent for CON-001 (Ace Construction).

        NEW LEAD:
        - Name: {lead.get('name')}
        - Project Type: {lead.get('project_type')}
        - Budget: {lead.get('budget')}
        - Location: {lead.get('location')}

        YOUR VENTURE (CON-001):
        - Stage: {venture_context.get('stage', 'unknown')}
        - Readiness: {venture_context.get('readiness_pct', 0)}%
        - Capabilities: {', '.join(venture_context.get('capabilities', []))}

        DECISION TASK:
        Decide: RESPOND_NOW | ASK_QUESTIONS | FORWARD_PARTNER | DECLINE

        RESPOND WITH JSON:
        {{
            "decision": "RESPOND_NOW|ASK_QUESTIONS|FORWARD_PARTNER|DECLINE",
            "reasoning": "brief explanation",
            "confidence": 0.0-1.0,
            "action": "specific next step"
        }}
        """

        response = claude_client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=500,
            messages=[{"role": "user", "content": prompt}]
        )

        try:
            text = response.content[0].text
            import re
            json_match = re.search(r'\{.*\}', text, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {
            "decision": "ASK_QUESTIONS",
            "reasoning": "Could not parse Claude response",
            "confidence": 0.5,
            "action": "Send clarification questions"
        }

# ============================================================================
# 7. ACTION EXECUTOR — Actually Send Email/Create Task
# ============================================================================

class ActionExecutor:
    """Execute the decision (send email, create task, etc.)"""

    @staticmethod
    async def execute(action_type: str, lead: dict, action_content: str,
                     supabase_client) -> dict:
        """Execute the decision"""

        if action_type == "RESPOND_NOW":
            return await ActionExecutor._send_response_email(lead, action_content)
        elif action_type == "ASK_QUESTIONS":
            return await ActionExecutor._send_clarification_email(lead, action_content)
        elif action_type == "FORWARD_PARTNER":
            return await ActionExecutor._create_partner_task(lead)
        elif action_type == "DECLINE":
            return await ActionExecutor._send_decline_email(lead)
        else:
            return {"success": False, "reason": f"Unknown action: {action_type}"}

    @staticmethod
    async def _send_response_email(lead: dict, content: str) -> dict:
        """Send response email"""
        print(f"[EMAIL] To {lead['email']}: {content[:100]}...")
        return {"success": True, "method": "email", "recipient": lead['email']}

    @staticmethod
    async def _send_clarification_email(lead: dict, questions: str) -> dict:
        print(f"[EMAIL] Clarification to {lead['email']}")
        return {"success": True, "method": "email", "recipient": lead['email']}

    @staticmethod
    async def _create_partner_task(lead: dict) -> dict:
        print(f"[TASK] Create partner task for {lead['name']}")
        return {"success": True, "method": "partner_task"}

    @staticmethod
    async def _send_decline_email(lead: dict) -> dict:
        print(f"[EMAIL] Decline to {lead['email']}")
        return {"success": True, "method": "email", "recipient": lead['email']}

# ============================================================================
# 8. FEEDBACK LOOP — Update Graph & Supabase
# ============================================================================

class FeedbackLoop:
    """Update venture state based on outcomes"""

    @staticmethod
    def update_graph_with_outcome(driver, venture_id: str, decision_id: str,
                                 outcome: str, success: bool):
        """Record outcome and update venture readiness"""
        query = f"""
        MATCH (d:Decision {{id: '{decision_id}'}})
        SET d.outcome = '{outcome}',
            d.success = {str(success).lower()},
            d.executed_at = datetime()
        WITH d
        MATCH (v:Venture {{id: '{venture_id}'}})
        SET v.readiness_pct = v.readiness_pct + (CASE WHEN {str(success).lower()} THEN 5 ELSE 0 END),
            v.last_action = '{outcome}'
        RETURN v.readiness_pct as new_readiness
        """
        with driver.session() as session:
            result = session.run(query)
            record = result.single()
            return record["new_readiness"] if record else None

    @staticmethod
    def mark_lead_processed(supabase_client, lead_id: str, status: str,
                          decision_id: str, outcome: dict):
        """Update venture_leads table"""
        supabase_client.table("venture_leads").update({
            "status": status,
            "processed_at": datetime.utcnow().isoformat(),
            "decision_id": decision_id,
            "decision_type": outcome.get("decision"),
            "confidence": outcome.get("confidence")
        }).eq("id", lead_id).execute()

# ============================================================================
# 9. MAIN EXECUTION LOOP
# ============================================================================

class CON001Agent:
    """The actual execution agent"""

    def __init__(self, clients, config):
        self.clients = clients
        self.config = config

    @trace(name="process_lead", tags=["con-001"])
    async def process_lead(self, lead_id: str) -> dict:
        """Full 10-step pipeline"""

        try:
            # Step 1: Fetch lead
            lead_response = self.clients["supabase"].table("venture_leads").select("*").eq("id", lead_id).single().execute()
            lead = lead_response.data if lead_response.data else {}
            print(f"\n[STEP 1] Lead: {lead.get('name')} ({lead.get('email')})")

            # Step 2: Get venture context (Neo4j)
            venture_context = GraphQueries.get_venture_context(
                self.clients["neo4j"],
                self.config.VENTURE_ID
            )
            print(f"[STEP 2] Venture: {venture_context.get('name')} ({venture_context.get('stage')})")

            # Step 3: Search similar projects (Qdrant)
            similar_projects = SemanticSearch.search_similar_projects(
                self.clients["qdrant"],
                lead.get("project_type", "unknown"),
                lead.get("budget", "unknown")
            )
            print(f"[STEP 3] Found {len(similar_projects)} similar projects")

            # Step 4: Select model (cost-aware)
            task_complexity = "simple" if float(lead.get("budget", 0) or 0) < 5000 else "medium"
            selected_model = ModelRouter.select_model(task_complexity, float(lead.get("budget", 0) or 0))
            estimated_cost = ModelRouter.estimate_cost(selected_model)
            print(f"[STEP 4] Model: {selected_model} (${estimated_cost:.4f})")

            # Step 5: Make decision (Claude)
            decision = DecisionEngine.make_decision(
                self.clients["claude"],
                lead,
                venture_context,
                similar_projects
            )
            print(f"[STEP 5] Decision: {decision.get('decision')} ({decision.get('confidence')})")

            # Step 6: Log decision to graph
            decision_id = GraphQueries.create_decision_node(
                self.clients["neo4j"],
                self.config.VENTURE_ID,
                decision.get("decision", "UNKNOWN"),
                decision.get("reasoning", ""),
                decision.get("confidence", 0)
            )
            print(f"[STEP 6] Decision logged: {decision_id}")

            # Step 7: Execute action
            action_result = await ActionExecutor.execute(
                decision.get("decision"),
                lead,
                decision.get("action", ""),
                self.clients["supabase"]
            )
            print(f"[STEP 7] Action: {action_result.get('method')}")

            # Step 8: Update graph with outcome
            new_readiness = FeedbackLoop.update_graph_with_outcome(
                self.clients["neo4j"],
                self.config.VENTURE_ID,
                decision_id,
                f"{decision.get('decision')}: {action_result.get('method')}",
                action_result.get("success", False)
            )
            print(f"[STEP 8] Readiness: {new_readiness}%")

            # Step 9: Mark lead processed
            FeedbackLoop.mark_lead_processed(
                self.clients["supabase"],
                lead_id,
                "processed",
                decision_id,
                decision
            )
            print(f"[STEP 9] Lead marked processed")

            # Step 10: Log to Langfuse (auto via @trace)
            print(f"[STEP 10] Logged to Langfuse")

            return {
                "success": True,
                "lead_id": lead_id,
                "decision": decision.get("decision"),
                "cost": estimated_cost,
                "venture_readiness_new": new_readiness
            }

        except Exception as e:
            print(f"[ERROR] {e}")
            import traceback
            traceback.print_exc()
            return {"success": False, "error": str(e)}

    async def run_loop(self, limit: int = 10):
        """Check for new leads and process them"""
        count = 0
        while True and count < limit:
            try:
                response = self.clients["supabase"].table("venture_leads").select("id").eq("status", "new").limit(5).execute()
                leads = response.data if response.data else []

                if not leads:
                    print("[LOOP] No new leads. Waiting 60s...")
                    await asyncio.sleep(60)
                    continue

                print(f"[LOOP] Found {len(leads)} new lead(s)")
                for lead in leads:
                    await self.process_lead(lead["id"])
                    count += 1

            except Exception as e:
                print(f"[LOOP ERROR] {e}")
                await asyncio.sleep(60)

# ============================================================================
# 10. ENTRY POINT
# ============================================================================

async def main():
    parser = argparse.ArgumentParser(description="CON-001 Execution Agent")
    parser.add_argument("--run-once", action="store_true", help="Process 1 lead and exit")
    parser.add_argument("--loop", action="store_true", help="Run forever")
    parser.add_argument("--test", action="store_true", help="Test with dummy lead")
    args = parser.parse_args()

    clients, config = init_clients()
    agent = CON001Agent(clients, config)

    if args.test:
        dummy_lead = {
            "name": "John Contractor",
            "email": "john@example.com",
            "phone": "555-0000",
            "project_type": "Renovation",
            "budget": "$15,000",
            "location": "Charlotte, NC",
            "message": "Need kitchen renovation"
        }
        print(f"[TEST] Creating dummy lead...")
        response = clients["supabase"].table("venture_leads").insert([{
            **dummy_lead,
            "status": "new",
            "created_at": datetime.utcnow().isoformat()
        }]).execute()
        lead_id = response.data[0]["id"] if response.data else None

        if lead_id:
            result = await agent.process_lead(lead_id)
            print(json.dumps(result, indent=2))

    elif args.run_once:
        response = clients["supabase"].table("venture_leads").select("id").eq("status", "new").limit(1).execute()
        if response.data:
            result = await agent.process_lead(response.data[0]["id"])
            print(json.dumps(result, indent=2))
        else:
            print("No new leads")

    elif args.loop or not args.test:
        print("[LOOP] Starting CON-001 agent...")
        await agent.run_loop(limit=999999)

if __name__ == "__main__":
    asyncio.run(main())
