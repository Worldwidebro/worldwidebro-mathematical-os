"""Complete stack: Supabase → dispatch_engine → principal_enforcer → API → portals."""
import asyncio
import sys
import logging
from pathlib import Path

class ColoredFormatter(logging.Formatter):
    COLORS = {'DEBUG': '\033[36m', 'INFO': '\033[32m', 'WARNING': '\033[33m', 'ERROR': '\033[31m', 'CRITICAL': '\033[35m'}
    RESET = '\033[0m'
    def format(self, record):
        color = self.COLORS.get(record.levelname, self.RESET)
        record.msg = f"{color}{record.msg}{self.RESET}"
        return super().format(record)

handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(ColoredFormatter('[%(asctime)s] %(name)s: %(message)s', datefmt='%H:%M:%S'))
logging.basicConfig(level=logging.INFO, handlers=[handler])
logger = logging.getLogger("Stack")

try:
    from neo4j import AsyncGraphDatabase
    from graph_context import GraphContext
    NEO4J_AVAILABLE = True
except ImportError:
    NEO4J_AVAILABLE = False

from dispatch_engine import WorkflowEngine, Load, Location
from supabase_loader import SupabaseLoader
from principal_enforcer import PrincipalEnforcer
import os
import httpx

async def main():
    logger.info("="*70)
    logger.info("COMPLETE DISPATCH STACK")
    logger.info("="*70)

    # 1. Load from Supabase
    logger.info("\n[1] SUPABASE")
    load_rows = [
        {"id": "load-001", "shipper_id": "shipper-001", "origin_address": "Charlotte, NC", "origin_lat": 35.2271, "origin_lng": -80.8431, "destination_address": "Atlanta, GA", "destination_lat": 33.7490, "destination_lng": -84.3880, "equipment_type": "53ft-dry-van", "weight_lbs": 45000, "budget_usd": 1250},
        {"id": "load-002", "shipper_id": "shipper-002", "origin_address": "Greensboro, NC", "origin_lat": 36.0726, "origin_lng": -79.7920, "destination_address": "Miami, FL", "destination_lat": 25.7617, "destination_lng": -80.1918, "equipment_type": "53ft-reefer", "weight_lbs": 38000, "budget_usd": 1800}
    ]
    logger.info(f"✓ {len(load_rows)} demo loads loaded")

    # 2. Run dispatch engine
    logger.info("\n[2] DISPATCH ENGINE")
    driver = None
    if NEO4J_AVAILABLE:
        try:
            driver = AsyncGraphDatabase.driver("neo4j://localhost:7687", auth=("admin", "ventures2026"))
            await driver.verify_connectivity()
            logger.info("✓ Neo4j connected")
        except:
            logger.warning("✗ Neo4j offline (using mock graph)")

    engine = WorkflowEngine()
    if driver:
        engine.agents["carrier_matching"].graph = GraphContext(driver)
        engine.agents["rate_negotiation"].graph = GraphContext(driver)

    results = []
    for row in load_rows:
        loader = SupabaseLoader("", "")
        load = loader.supabase_to_load(row)
        logger.info(f"  Processing: {load.id}")
        result = await engine.execute(load)
        results.append(result)
        logger.info(f"    → Margin: ${result.gross_margin_usd}")

    # 3. Check principal
    logger.info("\n[3] PRINCIPAL GOALS")
    enforcer = PrincipalEnforcer("/Users/acebless/Documents/02_PROJECTS/LT/lt-011-dispatch-software/principal.json")
    escalations = await enforcer.check_goals()

    # 4. Post to API
    logger.info("\n[4] API ESCALATIONS")
    if escalations:
        try:
            async with httpx.AsyncClient() as client:
                for esc in escalations:
                    await client.post("http://localhost:8000/api/dispatch/escalate", json={"metric": esc["metric"], "action": esc["action"]}, timeout=1.0)
            logger.info(f"✓ {len(escalations)} escalations posted")
        except:
            logger.warning("✗ API offline")
    else:
        logger.info("✓ All goals met")

    # Summary
    logger.info("\n" + "="*70)
    logger.info("READY FOR PORTALS")
    logger.info("="*70)
    logger.info(f"Processed: {len(results)} loads | Total margin: ${sum(r.gross_margin_usd for r in results)}")
    logger.info("\nStartup commands:")
    logger.info("  # API server (new terminal)")
    logger.info("  cd agents && python api_routes.py")
    logger.info("\n  # VEX frontend (new terminal)")
    logger.info("  cd vex-hero-site && npm run dev")
    logger.info("\n  # Access:")
    logger.info("  Call Center: http://localhost:3000/dispatch/call-center")
    logger.info("  API Health: http://localhost:8000/api/dispatch/health")
    logger.info("="*70)

    if driver:
        await driver.close()

if __name__ == "__main__":
    asyncio.run(main())
