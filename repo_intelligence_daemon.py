#!/usr/bin/env python3
"""
Continuous Repository Intelligence Updater
Keeps system knowledge of all repos + completion % + capabilities current
Runs every 6 hours: builds capability catalog, embeddings, graph
Cost: 0 LLM tokens (all local Ollama + Qdrant + Neo4j)
"""

import subprocess
import schedule
import time
import logging
from datetime import datetime
import os

# Setup logging
os.makedirs("/Users/acebless/Documents/.logs", exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("/Users/acebless/Documents/.logs/repo_intelligence.log"),
        logging.StreamHandler()
    ]
)

SCRIPTS = [
    "build_capability_catalog.py",
    "build_repo_summaries.py",
    "build_repo_rag.py --build",
    "build_readme_corpus.py",
    "build_capability_backfill.py",
    "build_venture_capabilities.py",
    "build_repo_graph.py",
]

def run_pipeline():
    """Run full repo intelligence update pipeline"""
    logging.info("=" * 80)
    logging.info("Starting Repository Intelligence Update Pipeline")
    logging.info("=" * 80)

    start_time = time.time()

    try:
        for i, script in enumerate(SCRIPTS, 1):
            logging.info(f"[{i}/{len(SCRIPTS)}] Running: {script}")

            result = subprocess.run(
                f"cd /Users/acebless/Documents && python3 {script}",
                shell=True,
                capture_output=True,
                text=True,
                timeout=600  # 10 min per script
            )

            if result.returncode != 0:
                logging.error(f"ERROR in {script}")
                logging.error(f"STDOUT: {result.stdout}")
                logging.error(f"STDERR: {result.stderr}")
                return False
            else:
                logging.info(f"  ✓ {script} completed successfully")

        elapsed = time.time() - start_time
        logging.info("=" * 80)
        logging.info(f"Repository Intelligence Updated Successfully (took {elapsed:.1f}s)")
        logging.info("System now knows:")
        logging.info("  ✓ All 1,597 repos + their state")
        logging.info("  ✓ Capabilities in each repo")
        logging.info("  ✓ Completion % for each")
        logging.info("  ✓ Dependencies between repos")
        logging.info("=" * 80)
        return True

    except subprocess.TimeoutExpired:
        logging.error("Pipeline timeout (>10min per script)")
        return False
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return False


def scheduled_job():
    """Wrapper for scheduler"""
    success = run_pipeline()
    if not success:
        logging.warning("Pipeline failed - will retry in 6 hours")


if __name__ == "__main__":
    logging.info("Repository Intelligence Daemon Starting")
    logging.info("Update frequency: Every 6 hours")
    logging.info("Cost: 0 LLM tokens (local Ollama + Qdrant + Neo4j)")

    # Run immediately on startup
    logging.info("Running initial pipeline...")
    run_pipeline()

    # Schedule subsequent runs
    schedule.every(6).hours.do(scheduled_job)

    logging.info("Daemon ready. Waiting for scheduled updates...")

    try:
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
    except KeyboardInterrupt:
        logging.info("Daemon stopped by user")
