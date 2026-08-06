"""Main entry point: load from Supabase, run workflow, log results."""
import asyncio
import sys
import logging
from datetime import datetime
from pathlib import Path

class ColoredFormatter(logging.Formatter):
    COLORS = {
        'DEBUG': '\033[36m',    # Cyan
        'INFO': '\033[32m',     # Green
        'WARNING': '\033[33m',  # Yellow
        'ERROR': '\033[31m',    # Red
        'CRITICAL': '\033[35m'  # Magenta
    }
    RESET = '\033[0m'

    def format(self, record):
        color = self.COLORS.get(record.levelname, self.RESET)
        record.msg = f"{color}{record.msg}{self.RESET}"
        return super().format(record)

handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(ColoredFormatter('[%(asctime)s] %(name)s: %(message)s', datefmt='%H:%M:%S'))
logging.basicConfig(level=logging.INFO, handlers=[handler])
logger = logging.getLogger("MainRunner")

try:
    from neo4j import AsyncGraphDatabase
    from graph_context import GraphContext
    NEO4J_AVAILABLE = True
except ImportError:
    logger.warning("Neo4j driver not installed; using mock mode")
    NEO4J_AVAILABLE = False

from dispatch_engine import WorkflowEngine, Load, Location

async def main():
    logger.info("="*60)
    logger.info("DISPATCH WORKFLOW ENGINE v1.0")
    logger.info("="*60)

    load = Load(
        id="load-20260805-001",
        shipper_id="shipper-123",
        origin=Location(address="Charlotte, NC", latitude=35.2271, longitude=-80.8431),
        destination=Location(address="Atlanta, GA", latitude=33.7490, longitude=-84.3880),
        equipment_type="53ft-dry-van",
        weight_lbs=45000,
        budget_usd=1250
    )

    logger.info(f"Load received: {load.id}")
    logger.info(f"  Route: {load.origin.address} → {load.destination.address}")
    logger.info(f"  Budget: ${load.budget_usd} | Weight: {load.weight_lbs} lbs")

    driver = None
    if NEO4J_AVAILABLE:
        try:
            logger.info("Connecting to Neo4j...")
            driver = AsyncGraphDatabase.driver("neo4j://localhost:7687", auth=("admin", "ventures2026"))
            await driver.verify_connectivity()
            logger.info("✓ Neo4j connected")
        except Exception as e:
            logger.warning(f"Neo4j unavailable ({e}); using mock graph")
            driver = None

    engine = WorkflowEngine()

    if driver:
        real_graph = GraphContext(driver)
        engine.agents["carrier_matching"].graph = real_graph
        engine.agents["rate_negotiation"].graph = real_graph

    logger.info("-" * 60)
    logger.info("STARTING WORKFLOW")
    logger.info("-" * 60)

    try:
        result = await engine.execute(load)

        logger.info("-" * 60)
        logger.info("WORKFLOW COMPLETE")
        logger.info("-" * 60)
        logger.info(f"Final Status: {result.load.status}")
        logger.info(f"Revenue: ${result.load.budget_usd}")
        logger.info(f"Cost: ${result.negotiated_rate}")
        logger.info(f"Margin: ${result.gross_margin_usd}")
        logger.info(f"Evaluation Score: {result.evaluation_score}")
        logger.info(f"Steps Executed: {len(result.history)}")
        logger.info("-" * 60)

        logger.info("EXECUTION TRACE:")
        for i, step in enumerate(result.history, 1):
            logger.info(f"  {i}. {step}")

        logger.info("="*60)
        logger.info("✓ SUCCESS")
        logger.info("="*60)

    except Exception as e:
        logger.error(f"Workflow failed: {e}")
        import traceback
        traceback.print_exc()
    finally:
        if driver:
            await driver.close()

if __name__ == "__main__":
    asyncio.run(main())
