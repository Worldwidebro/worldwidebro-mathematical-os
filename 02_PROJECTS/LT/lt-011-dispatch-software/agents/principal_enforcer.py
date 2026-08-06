"""Principal enforcement: check goals, escalate if missed."""
import asyncio
import json
import sys
import logging
from pathlib import Path

class ColoredFormatter(logging.Formatter):
    COLORS = {
        'DEBUG': '\033[36m',
        'INFO': '\033[32m',
        'WARNING': '\033[33m',
        'ERROR': '\033[31m',
        'CRITICAL': '\033[35m'
    }
    RESET = '\033[0m'

    def format(self, record):
        color = self.COLORS.get(record.levelname, self.RESET)
        record.msg = f"{color}{record.msg}{self.RESET}"
        return super().format(record)

handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(ColoredFormatter('[%(asctime)s] %(name)s: %(message)s', datefmt='%H:%M:%S'))
logging.basicConfig(level=logging.INFO, handlers=[handler])
logger = logging.getLogger("PrincipalEnforcer")

class PrincipalEnforcer:
    def __init__(self, principal_yaml_path: str):
        """Load principal goals from JSON."""
        try:
            with open(principal_yaml_path) as f:
                data = json.load(f)
                self.goals = data.get("goals", [])
                self.name = data.get("name", "Principal")
        except FileNotFoundError:
            logger.warning(f"principal.json not found at {principal_yaml_path}")
            self.goals = []
            self.name = "Principal"

    async def check_goals(self):
        """Poll current metrics against goals; escalate if missed."""
        logger.info("="*60)
        logger.info(f"{self.name} GOAL CHECK")
        logger.info("="*60)

        if not self.goals:
            logger.info("No goals defined.")
            return

        escalations = []

        for goal in self.goals:
            metric = goal.get("metric", "unknown")
            target = goal.get("target", 0)
            current = goal.get("current", 0)
            tolerance = goal.get("tolerance", 0.05)
            action = goal.get("action_if_miss", "No action defined")

            lower_bound = target - (target * tolerance)
            is_met = current >= lower_bound

            status = "✓ PASS" if is_met else "✗ FAIL"
            logger.info(f"{status}: {metric} = {current:.2%} (target {target:.2%}, tolerance ±{tolerance:.2%})")

            if not is_met:
                escalations.append({
                    "metric": metric,
                    "current": current,
                    "target": target,
                    "action": action
                })

        if escalations:
            logger.info("-" * 60)
            logger.warning(f"ESCALATIONS ({len(escalations)})")
            logger.info("-" * 60)
            for esc in escalations:
                logger.warning(f"  • {esc['metric']}: {esc['action']}")
        else:
            logger.info("-" * 60)
            logger.info("✓ ALL GOALS MET")
            logger.info("-" * 60)

        return escalations

async def main():
    principal_path = Path(__file__).parent.parent / "principal.json"

    if not principal_path.exists():
        sample_principal = {
            "name": "LT-011 Dispatch Principal",
            "goals": [
                {"metric": "fill_rate", "target": 0.90, "current": 0.72, "tolerance": 0.05, "action_if_miss": "Run DISPATCH-PERF-OPTIMIZE workflow"},
                {"metric": "gross_margin_pct", "target": 0.32, "current": 0.28, "tolerance": 0.03, "action_if_miss": "Escalate low-margin loads to Decision Agent"},
                {"metric": "time_to_assignment_hours", "target": 2.0, "current": 1.8, "tolerance": 0.1, "action_if_miss": "Increase carrier matching pool"}
            ]
        }
        principal_path.write_text(json.dumps(sample_principal, indent=2))
        logger.info(f"Created sample principal at {principal_path}")

    enforcer = PrincipalEnforcer(str(principal_path))
    escalations = await enforcer.check_goals()

    logger.info("="*60)
    if escalations:
        logger.warning(f"FINAL: {len(escalations)} goals missed. Escalations queued.")
    else:
        logger.info("FINAL: All goals met. No escalations.")
    logger.info("="*60)

if __name__ == "__main__":
    asyncio.run(main())
