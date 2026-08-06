"""Scheduler: cron jobs for enforcement, metrics, health."""
import asyncio
import logging
from datetime import datetime, timedelta
from typing import Callable, Dict

logger = logging.getLogger("Scheduler")

class DispatchScheduler:
    def __init__(self):
        self.jobs = []
        self.running = False

    def add_job(self, func: Callable, interval_seconds: int, name: str):
        self.jobs.append({
            "func": func, "interval": interval_seconds, "name": name,
            "last_run": None, "next_run": datetime.now()
        })
        logger.info(f"✓ {name} (every {interval_seconds}s)")

    async def run(self):
        self.running = True
        logger.info("Scheduler started")
        while self.running:
            now = datetime.now()
            for job in self.jobs:
                if now >= job["next_run"]:
                    try:
                        logger.info(f"→ {job['name']}")
                        await job["func"]()
                        job["last_run"] = now
                        job["next_run"] = now + timedelta(seconds=job["interval"])
                        logger.info(f"✓ {job['name']}")
                    except Exception as e:
                        logger.error(f"✗ {job['name']}: {e}")
            await asyncio.sleep(5)

    def stop(self):
        self.running = False

async def check_principal():
    from principal_enforcer import PrincipalEnforcer
    import httpx
    enforcer = PrincipalEnforcer("/Users/acebless/Documents/02_PROJECTS/LT/lt-011-dispatch-software/principal.json")
    escalations = await enforcer.check_goals()
    if escalations:
        try:
            async with httpx.AsyncClient() as client:
                for esc in escalations:
                    await client.post("http://localhost:8000/api/dispatch/escalate",
                        json={"metric": esc["metric"], "action": esc["action"]}, timeout=2.0)
        except:
            pass

async def collect_metrics():
    try:
        from langfuse import Langfuse
        langfuse = Langfuse()
        langfuse.event(name="dispatch_metrics", input={"timestamp": datetime.now().isoformat()})
    except:
        pass

async def health_check():
    checks = {}
    try:
        from neo4j import AsyncGraphDatabase
        driver = AsyncGraphDatabase.driver("neo4j://localhost:7687", auth=("admin", "ventures2026"))
        await driver.verify_connectivity()
        checks["neo4j"] = "✓"
        await driver.close()
    except:
        checks["neo4j"] = "✗"
    try:
        import httpx
        async with httpx.AsyncClient() as client:
            resp = await client.get("http://localhost:8000/api/dispatch/health", timeout=1.0)
            checks["api"] = "✓" if resp.status_code == 200 else "✗"
    except:
        checks["api"] = "✗"
    status = "FAILED" if any(v == "✗" for v in checks.values()) else "OK"
    logger.info(f"Health: {status} {checks}")

scheduler = DispatchScheduler()
scheduler.add_job(check_principal, 300, "Principal Goals")
scheduler.add_job(collect_metrics, 600, "Metrics")
scheduler.add_job(health_check, 60, "Health Check")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(name)s: %(message)s', datefmt='%H:%M:%S')
    asyncio.run(scheduler.run())
