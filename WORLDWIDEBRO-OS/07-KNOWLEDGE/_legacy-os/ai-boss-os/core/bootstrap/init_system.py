#!/usr/bin/env python3
"""Bootstrap AI Boss OS: entity registry, Postgres schema, Kafka topics."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = ROOT / "core" / "config" / "system_config.yaml"
SCHEMA_DIR = ROOT / "memory" / "postgres" / "schema"
LOADER = ROOT / "scripts" / "load_entity_registry.py"

EVENT_TYPES = [
    "orchestrator.started",
    "orchestrator.venture_agent.spawned",
    "orchestrator.all_agents.spawned",
    "orchestrator.shutdown_requested",
    "orchestrator.health_check.passed",
    "orchestrator.state_dump",
    "venture.initialized",
    "venture.decision.made",
    "venture.execution.started",
    "venture.execution.succeeded",
    "venture.execution.failed",
    "venture.repo_synced",
    "venture.contact_created",
    "venture.product_launched",
    "venture.milestone_reached",
    "venture.state_updated",
    "venture.risk_triggered",
    "venture.escalated_to_human",
    "risk.threshold_crossed",
    "risk.kill_decision",
    "risk.scale_decision",
    "risk.constraint_violated",
    "risk.capital_reallocated",
    "risk.warning_issued",
    "risk.all_constraints_ok",
]


def expand_env(value: str) -> str:
    pattern = re.compile(r"\$\{([^}:]+)(?::-([^}]*))?\}")

    def repl(match: re.Match[str]) -> str:
        key, default = match.group(1), match.group(2)
        return os.environ.get(key, default if default is not None else "")

    return pattern.sub(repl, value)


def load_yaml(path: Path) -> dict:
    try:
        import yaml  # type: ignore
    except ImportError:
        return _load_yaml_minimal(path)
    with path.open(encoding="utf-8") as f:
        raw = yaml.safe_load(f)
    return _expand_dict(raw)


def _load_yaml_minimal(path: Path) -> dict:
    """Parse flat key: value YAML without PyYAML."""
    result: dict = {}
    stack: list[tuple[int, dict]] = [(-1, result)]
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        indent = len(line) - len(line.lstrip())
        key, _, raw_val = line.strip().partition(":")
        while stack and indent <= stack[-1][0]:
            stack.pop()
        parent = stack[-1][1]
        if not raw_val.strip():
            parent[key] = {}
            stack.append((indent, parent[key]))
        else:
            parent[key] = expand_env(raw_val.strip())
    return result


def _expand_dict(node):
    if isinstance(node, dict):
        return {k: _expand_dict(v) for k, v in node.items()}
    if isinstance(node, list):
        return [_expand_dict(v) for v in node]
    if isinstance(node, str):
        return expand_env(node)
    return node


def kafka_topics(config: dict) -> list[str]:
    version = config.get("kafka", {}).get("topic_version", "v1")
    return [f"{event_type}.{version}" for event_type in EVENT_TYPES]


def run_loader(dry_run: bool) -> Path:
    entities_path = ROOT / "registries" / "entity_registry" / "entities.json"
    if dry_run and entities_path.exists():
        print(f"[dry-run] Entity registry exists: {entities_path}")
        return entities_path
    print("Loading entity registry from ventures-master.csv...")
    subprocess.run([sys.executable, str(LOADER)], check=True)
    return entities_path


def apply_postgres(config: dict, entities_path: Path, dry_run: bool) -> None:
    pg = config.get("postgres", {})
    host = pg.get("host", "localhost")
    port = pg.get("port", 5432)
    database = pg.get("database", "ai_boss_os")
    user = pg.get("user", "ai_boss")
    password = pg.get("password", "")

    sql_files = sorted(SCHEMA_DIR.glob("*.sql"))
    if dry_run:
        print(f"[dry-run] Would apply {len(sql_files)} SQL files to {database}@{host}:{port}")
        for sql_file in sql_files:
            print(f"  - {sql_file.name}")
        with entities_path.open(encoding="utf-8") as f:
            data = json.load(f)
        print(
            f"[dry-run] Would upsert {data['counts']['ventures']} ventures "
            f"and {data['counts']['sectors']} sectors"
        )
        return

    env = os.environ.copy()
    if password:
        env["PGPASSWORD"] = password

    for sql_file in sql_files:
        cmd = [
            "psql",
            "-h",
            str(host),
            "-p",
            str(port),
            "-U",
            str(user),
            "-d",
            str(database),
            "-f",
            str(sql_file),
        ]
        subprocess.run(cmd, check=True, env=env)

    with entities_path.open(encoding="utf-8") as f:
        data = json.load(f)

    sectors_sql = ROOT / "memory" / "postgres" / "schema" / "_seed_sectors.sql"
    ventures_sql = ROOT / "memory" / "postgres" / "schema" / "_seed_ventures.sql"
    _write_seed_sql(data, sectors_sql, ventures_sql)

    for seed in (sectors_sql, ventures_sql):
        subprocess.run(
            [
                "psql",
                "-h",
                str(host),
                "-p",
                str(port),
                "-U",
                str(user),
                "-d",
                str(database),
                "-f",
                str(seed),
            ],
            check=True,
            env=env,
        )
    print(f"Postgres seeded: {data['counts']['ventures']} ventures")


def _write_seed_sql(data: dict, sectors_path: Path, ventures_path: Path) -> None:
    sector_rows = []
    for s in data["sectors"]:
        sector_rows.append(
            "INSERT INTO sectors (sector_code, name, economic_layer, agent_id, dispatch_status) "
            f"VALUES ({_q(s['sector_code'])}, {_q(s['name'])}, {_q(s['economic_layer'])}, "
            f"{_q(s['agent_id'])}, {_q(s['dispatch_status'])}) "
            "ON CONFLICT (sector_code) DO UPDATE SET "
            "name = EXCLUDED.name, economic_layer = EXCLUDED.economic_layer, "
            "agent_id = EXCLUDED.agent_id, dispatch_status = EXCLUDED.dispatch_status;"
        )

    venture_rows = []
    for v in data["ventures"]:
        venture_rows.append(
            "INSERT INTO ventures (venture_id, name, sector_code, stage, status, repository_url, github_slug) "
            f"VALUES ({_q(v['venture_id'])}, {_q(v['name'])}, {_q(v['sector_code'])}, "
            f"{_q(v.get('stage'))}, {_q(v.get('status'))}, {_q(v.get('repository_url'))}, "
            f"{_q(v.get('github_slug'))}) "
            "ON CONFLICT (venture_id) DO UPDATE SET "
            "name = EXCLUDED.name, sector_code = EXCLUDED.sector_code, "
            "stage = EXCLUDED.stage, status = EXCLUDED.status, "
            "repository_url = EXCLUDED.repository_url, github_slug = EXCLUDED.github_slug, "
            "updated_at = NOW();"
        )

    sectors_path.write_text("\n".join(sector_rows) + "\n", encoding="utf-8")
    ventures_path.write_text("\n".join(venture_rows) + "\n", encoding="utf-8")


def _q(value) -> str:
    if value is None:
        return "NULL"
    return "'" + str(value).replace("'", "''") + "'"


def apply_kafka(config: dict, dry_run: bool) -> None:
    topics = kafka_topics(config)
    bootstrap = config.get("kafka", {}).get("bootstrap_servers", "localhost:9092")
    replication = config.get("kafka", {}).get("replication_factor", 1)
    retention = config.get("kafka", {}).get("retention_ms", 604800000)

    if dry_run:
        print(f"[dry-run] Would create {len(topics)} Kafka topics on {bootstrap}")
        for topic in topics[:5]:
            print(f"  - {topic}")
        if len(topics) > 5:
            print(f"  ... +{len(topics) - 5} more")
        return

    for topic in topics:
        cmd = [
            "kafka-topics",
            "--bootstrap-server",
            str(bootstrap),
            "--create",
            "--if-not-exists",
            "--topic",
            topic,
            "--partitions",
            "12",
            "--replication-factor",
            str(replication),
            "--config",
            f"retention.ms={retention}",
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0 and "already exists" not in (result.stderr or ""):
            raise RuntimeError(f"kafka-topics failed for {topic}: {result.stderr}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Bootstrap AI Boss OS")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        default=True,
        help="Print actions without applying (default)",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Apply Postgres schema and Kafka topics (requires running services)",
    )
    parser.add_argument("--skip-registry", action="store_true")
    parser.add_argument("--postgres-only", action="store_true")
    parser.add_argument("--kafka-only", action="store_true")
    args = parser.parse_args()

    dry_run = not args.apply
    if not CONFIG_PATH.exists():
        raise SystemExit(f"Missing config: {CONFIG_PATH}")

    config = load_yaml(CONFIG_PATH)
    print(f"AI Boss OS bootstrap — env={config.get('environment', 'unknown')} dry_run={dry_run}")

    entities_path = ROOT / "registries" / "entity_registry" / "entities.json"
    if not args.skip_registry:
        entities_path = run_loader(dry_run=False if args.apply else dry_run)

    if not args.kafka_only:
        apply_postgres(config, entities_path, dry_run=dry_run)

    if not args.postgres_only:
        apply_kafka(config, dry_run=dry_run)

    print("Bootstrap complete.")


if __name__ == "__main__":
    main()
