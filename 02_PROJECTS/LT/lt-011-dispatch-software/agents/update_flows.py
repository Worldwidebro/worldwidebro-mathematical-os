"""Update flows: what happens when workflow state changes."""
import logging
from datetime import datetime
from typing import Dict, Any

logger = logging.getLogger("UpdateFlows")

class UpdateFlows:
    async def on_load_completed(self, load_id: str, result: Dict[str, Any]):
        """Workflow COMPLETED → update Supabase, Neo4j, emit events."""
        logger.info(f"Load completed: {load_id}")

        try:
            from supabase import AsyncClient
            supabase = AsyncClient("https://rhlkjelglvurowdalrgh.supabase.co", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJobGtqZWxnbHZvdW9yb3dkYWxyZ2giLCJyb2xlIjoiYW5vbiIsImlhdCI6MTY4ODc2NzkyOCwiZXhwIjoyMDE0MzQzOTI4fQ.vROFfx3LRGqlJGLG-nUi3lJMcPwQDr6WdQGHa84C_a8")
            await supabase.table("loads").update({
                "status": "COMPLETED",
                "completed_at": datetime.now().isoformat(),
                "margin_captured": result.get("gross_margin_usd", 0)
            }).eq("id", load_id).execute()
            logger.info(f"✓ Supabase updated")
        except Exception as e:
            logger.error(f"Supabase update failed: {e}")

        try:
            from neo4j import AsyncGraphDatabase
            driver = AsyncGraphDatabase.driver("neo4j://localhost:7687", auth=("admin", "ventures2026"))
            async with driver.session() as session:
                await session.run("""
                    MATCH (l:Load {id: $id})
                    SET l.status = 'COMPLETED', l.margin = $margin, l.completed_at = datetime()
                """, {"id": load_id, "margin": result.get("gross_margin_usd", 0)})
            await driver.close()
            logger.info(f"✓ Neo4j updated")
        except Exception as e:
            logger.error(f"Neo4j update failed: {e}")

        try:
            from langfuse import Langfuse
            langfuse = Langfuse()
            langfuse.event(name="load_completed", input={"load_id": load_id, "margin": result.get("gross_margin_usd", 0)})
            logger.info(f"✓ Langfuse logged")
        except:
            pass

    async def on_escalation_received(self, escalation: Dict[str, str]):
        """Principal flagged goal miss → create task, alert ops."""
        logger.info(f"Escalation: {escalation['metric']}")

        try:
            import httpx
            async with httpx.AsyncClient() as client:
                # Post to call center queue
                await client.post("http://localhost:8000/api/dispatch/escalate",
                    json=escalation, timeout=2.0)
            logger.info(f"✓ Call center queued")
        except:
            pass

    async def on_carrier_assigned(self, load_id: str, carrier_name: str, rate: float):
        """Rate negotiation selected carrier → notify carrier."""
        logger.info(f"Carrier: {carrier_name} @ ${rate}/mi")

        try:
            from supabase import AsyncClient
            supabase = AsyncClient("https://rhlkjelglvurowdalrgh.supabase.co", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJobGtqZWxnbHZvdW9yb3dkYWxyZ2giLCJyb2xlIjoiYW5vbiIsImlhdCI6MTY4ODc2NzkyOCwiZXhwIjoyMDE0MzQzOTI4fQ.vROFfx3LRGqlJGLG-nUi3lJMcPwQDr6WdQGHa84C_a8")
            await supabase.table("loads").update({
                "carrier_name": carrier_name,
                "negotiated_rate": rate,
                "status": "ASSIGNED"
            }).eq("id", load_id).execute()
            logger.info(f"✓ Load marked ASSIGNED")
        except Exception as e:
            logger.error(f"Supabase error: {e}")

update_flows = UpdateFlows()
