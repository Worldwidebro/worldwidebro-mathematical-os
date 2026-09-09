#!/usr/bin/env python3
"""
Form Submission → ClickUp Task Automation

Triggers when a venture form is submitted:
1. Extracts lead data from form
2. Queries Neo4j for relationship context (warm intros)
3. Queries gbrain for venture context
4. Creates ClickUp task with full intelligence
5. Updates Supabase lead record
6. Notifies Growth OS

Author: Company Brain Automation
"""

import os
import json
import re
import asyncio
from typing import Optional, Dict, Any
from datetime import datetime
from urllib.parse import urljoin

import httpx
from neo4j import GraphDatabase
from dotenv import load_dotenv

load_dotenv()

# Configuration
NEO4J_URI = os.getenv("NEO4J_URI", "bolt://100.87.214.70:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "changeme")

CLICKUP_API_KEY = os.getenv("CLICKUP_API_KEY")
CLICKUP_WORKSPACE_ID = os.getenv("CLICKUP_WORKSPACE_ID")
CLICKUP_TEAM_ID = os.getenv("CLICKUP_TEAM_ID")

GBRAIN_API = os.getenv("GBRAIN_API", "http://localhost:8000")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
GROWTH_OS_WEBHOOK = os.getenv("GROWTH_OS_WEBHOOK")

VENTURE_MAPPING = {
    "ops-001": {"name": "CareerOps Staffing", "sector": "SEC-014", "list_id": ""},
    "con-001": {"name": "ACE Construction", "sector": "SEC-002", "list_id": ""},
    "lt-005": {"name": "HealthRoute Courier", "sector": "SEC-017", "list_id": ""},
    "lt-011": {"name": "CarrierDispatch TMS", "sector": "SEC-017", "list_id": ""},
    "re-001": {"name": "WorldwideBro RE", "sector": "SEC-020", "list_id": ""},
}


class FormWebhookHandler:
    """Handles form submissions and creates ClickUp tasks with intelligence"""

    def __init__(self):
        self.neo4j_driver = GraphDatabase.driver(
            NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD)
        )
        self.http_client = httpx.AsyncClient(timeout=30.0)

    async def close(self):
        """Clean up resources"""
        self.neo4j_driver.close()
        await self.http_client.aclose()

    async def handle_form_submission(
        self, venture_id: str, form_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Main entry point: Process form submission and create ClickUp task

        Args:
            venture_id: e.g., "ops-001"
            form_data: {
                "name": "John Doe",
                "email": "john@example.com",
                "phone": "+1-555-0123",
                "message": "I need staffing for warehouse",
                "company": "Acme Corp",
                ...
            }

        Returns:
            {
                "success": bool,
                "clickup_task_id": str,
                "context": {...},
                "warm_intros": [...]
            }
        """

        venture_info = VENTURE_MAPPING.get(venture_id.lower())
        if not venture_info:
            return {"success": False, "error": f"Unknown venture: {venture_id}"}

        try:
            # Step 1: Extract and validate lead data
            lead_data = self._extract_lead_data(form_data, venture_id)

            # Step 2: Query Neo4j for warm introduction paths
            warm_intros = await self._find_warm_intros(
                lead_data, venture_info["sector"]
            )

            # Step 3: Query gbrain for venture context
            venture_context = await self._get_venture_context(venture_id, lead_data)

            # Step 4: Create ClickUp task
            clickup_task = await self._create_clickup_task(
                venture_id, venture_info, lead_data, warm_intros, venture_context
            )

            # Step 5: Update Supabase lead record
            await self._update_supabase_lead(venture_id, lead_data, clickup_task)

            # Step 6: Notify Growth OS
            await self._notify_growth_os(venture_id, lead_data, clickup_task)

            return {
                "success": True,
                "clickup_task_id": clickup_task.get("id"),
                "context": venture_context,
                "warm_intros": warm_intros,
                "timestamp": datetime.utcnow().isoformat(),
            }

        except Exception as e:
            print(f"Error handling form submission: {e}")
            return {"success": False, "error": str(e)}

    def _extract_lead_data(self, form_data: Dict, venture_id: str) -> Dict:
        """Extract and normalize lead data from form"""
        return {
            "venture_id": venture_id,
            "name": form_data.get("name", "").strip(),
            "email": form_data.get("email", "").strip(),
            "phone": self._normalize_phone(form_data.get("phone", "")),
            "company": form_data.get("company", "").strip(),
            "message": form_data.get("message", "").strip(),
            "captured_at": datetime.utcnow().isoformat(),
        }

    def _normalize_phone(self, phone: str) -> str:
        """Normalize phone number to E.164 format"""
        if not phone:
            return ""
        # Remove non-digits
        digits = re.sub(r"\D", "", phone)
        # Add +1 if US number
        if len(digits) == 10:
            digits = "1" + digits
        return "+" + digits if digits else ""

    async def _find_warm_intros(self, lead_data: Dict, sector: str) -> list:
        """
        Query Neo4j for warm introduction paths

        Looks for:
        - Existing relationships between lead's company and our advisors
        - Similar leads who converted (same industry/company size)
        - Sector-specific patterns
        """
        query = """
        MATCH (lead_company:ORGANIZATION {name: $company_name})
        OPTIONAL MATCH (lead_company)-[rel:CONNECTED_TO|WORKS_WITH|INVESTED_IN]-
                       (advisor:PERSON {role: 'ADVISOR'})
        OPTIONAL MATCH (advisor)-[:ADVISES]-(venture:VENTURE {sector: $sector})
        RETURN advisor, venture, rel
        LIMIT 5
        """

        async def run_query():
            with self.neo4j_driver.session() as session:
                result = session.run(
                    query,
                    company_name=lead_data.get("company"),
                    sector=sector,
                )
                return [record.data() for record in result]

        try:
            results = await asyncio.to_thread(run_query)
            return [
                {
                    "advisor": r.get("advisor", {}).get("name"),
                    "venture": r.get("venture", {}).get("name"),
                    "relationship_type": r.get("rel", {}).get("type"),
                }
                for r in results
                if r.get("advisor")
            ]
        except Exception as e:
            print(f"Neo4j query error: {e}")
            return []

    async def _get_venture_context(
        self, venture_id: str, lead_data: Dict
    ) -> Dict:
        """
        Query gbrain for venture context

        Returns relevant info like:
        - Industry trends from venture docs
        - Historical customer profiles
        - Relevant processes/scripts
        """
        prompt = f"""
        Context for {venture_id} lead:
        Company: {lead_data.get("company")}
        Industry signals: {lead_data.get("message")}

        Find:
        1. Similar customer profiles in our database
        2. Relevant processes for this type of lead
        3. Key talking points from our docs
        """

        try:
            response = await self.http_client.post(
                f"{GBRAIN_API}/search",
                json={
                    "query": prompt,
                    "venture": venture_id,
                    "limit": 3,
                },
            )
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            print(f"gbrain query error: {e}")

        return {"similar_customers": [], "processes": [], "talking_points": []}

    async def _create_clickup_task(
        self,
        venture_id: str,
        venture_info: Dict,
        lead_data: Dict,
        warm_intros: list,
        venture_context: Dict,
    ) -> Dict:
        """
        Create ClickUp task with full context

        Task structure:
        - Title: Lead name + company
        - Description: Full context + warm intro paths
        - Custom fields: Venture, revenue potential, priority
        - Assigned to: Script-determined agent
        - Due date: 24 hours
        """

        task_title = f"[{venture_id.upper()}] {lead_data['name']} - {lead_data['company']}"

        # Build context markdown
        context_md = f"""
# Lead Context

**Name:** {lead_data['name']}
**Email:** {lead_data['email']}
**Phone:** {lead_data['phone']}
**Company:** {lead_data['company']}

## Message
{lead_data['message']}

## Warm Introductions
"""
        for intro in warm_intros:
            if intro.get("advisor"):
                context_md += (
                    f"\n- **{intro['advisor']}** ({intro.get('venture', 'N/A')}) "
                    f"via {intro.get('relationship_type', 'connection')}"
                )

        if not warm_intros:
            context_md += "\nNo warm paths found. Cold outreach required."

        # Add venture context
        if venture_context.get("similar_customers"):
            context_md += "\n\n## Similar Customers\n"
            for customer in venture_context["similar_customers"][:3]:
                context_md += f"- {customer}\n"

        # Determine revenue potential
        revenue_potential = self._estimate_revenue_potential(venture_id, lead_data)

        task_body = {
            "name": task_title,
            "description": context_md,
            "priority": 2 if revenue_potential > 1000 else 3,  # 1=urgent, 4=low
            "due_date": int(
                (datetime.utcnow().timestamp() + 86400) * 1000
            ),  # 24 hours
            "custom_fields": [
                {
                    "id": "venture",
                    "value": venture_id,
                },
                {
                    "id": "revenue_potential",
                    "value": revenue_potential,
                },
                {
                    "id": "warm_intros",
                    "value": len(warm_intros),
                },
            ],
        }

        try:
            response = await self.http_client.post(
                f"https://api.clickup.com/api/v2/team/{CLICKUP_TEAM_ID}/task",
                headers={"Authorization": CLICKUP_API_KEY},
                json=task_body,
            )

            if response.status_code == 200:
                return response.json()
            else:
                print(f"ClickUp error: {response.status_code} {response.text}")
                return {}

        except Exception as e:
            print(f"ClickUp creation error: {e}")
            return {}

    def _estimate_revenue_potential(self, venture_id: str, lead_data: Dict) -> int:
        """Estimate revenue potential from lead signals"""
        potential = 0

        # Venture-specific base
        venture_base = {
            "ops-001": 2500,  # Staffing placement
            "con-001": 299,  # Consultation
            "lt-005": 1500,  # Courier contract
            "lt-011": 5000,  # TMS contract
            "re-001": 50000,  # RE syndication
        }
        potential += venture_base.get(venture_id.lower(), 1000)

        # Boost for signals
        message_lower = lead_data.get("message", "").lower()
        if any(word in message_lower for word in ["urgent", "asap", "immediate"]):
            potential *= 1.5

        if any(word in message_lower for word in ["contract", "agreement", "deal"]):
            potential *= 1.3

        return int(potential)

    async def _update_supabase_lead(
        self, venture_id: str, lead_data: Dict, clickup_task: Dict
    ):
        """Update Supabase with lead record and ClickUp link"""
        try:
            lead_record = {
                "venture_id": venture_id,
                "name": lead_data["name"],
                "email": lead_data["email"],
                "phone": lead_data["phone"],
                "company": lead_data["company"],
                "message": lead_data["message"],
                "clickup_task_id": clickup_task.get("id"),
                "status": "contacted",
                "captured_at": lead_data["captured_at"],
            }

            response = await self.http_client.post(
                f"{SUPABASE_URL}/rest/v1/venture_leads",
                headers={
                    "Authorization": f"Bearer {SUPABASE_KEY}",
                    "Content-Type": "application/json",
                },
                json=lead_record,
            )

            if response.status_code not in [200, 201]:
                print(f"Supabase error: {response.status_code} {response.text}")

        except Exception as e:
            print(f"Supabase update error: {e}")

    async def _notify_growth_os(
        self, venture_id: str, lead_data: Dict, clickup_task: Dict
    ):
        """Notify Growth OS dashboard of new lead"""
        if not GROWTH_OS_WEBHOOK:
            return

        try:
            payload = {
                "event": "lead_captured",
                "venture_id": venture_id,
                "lead_name": lead_data["name"],
                "lead_email": lead_data["email"],
                "clickup_task_id": clickup_task.get("id"),
                "timestamp": datetime.utcnow().isoformat(),
            }

            await self.http_client.post(GROWTH_OS_WEBHOOK, json=payload)

        except Exception as e:
            print(f"Growth OS notification error: {e}")


async def main():
    """Example usage"""
    handler = FormWebhookHandler()

    try:
        # Example form submission
        result = await handler.handle_form_submission(
            "ops-001",
            {
                "name": "John Smith",
                "email": "john@acmecorp.com",
                "phone": "(555) 123-4567",
                "company": "Acme Manufacturing",
                "message": "We need to hire 5 warehouse workers immediately for Q4 surge",
            },
        )

        print(json.dumps(result, indent=2))

    finally:
        await handler.close()


if __name__ == "__main__":
    asyncio.run(main())
