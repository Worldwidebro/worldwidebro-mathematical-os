#!/usr/bin/env python3
"""
Manifest-driven RAG ingestion.

Reads RAG-INGESTION-MANIFEST.csv and sends each registered source through the
existing preprocessing and LightRAG/Supabase sync pipeline.
"""

import argparse
import csv
import json
import os
from pathlib import Path
from typing import Dict, List


DEFAULT_MANIFEST = "RAG-INGESTION-MANIFEST.csv"
STATUS_FILE = "RAG-INGESTION-STATUS.json"


def load_env_file(env_path: Path) -> None:
    if not env_path.exists():
        return

    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def load_manifest(manifest_path: Path) -> List[Dict[str, str]]:
    with manifest_path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def ingest_manifest(manifest_path: Path, dry_run: bool = False, sync: bool = False) -> Dict:
    root = manifest_path.parent
    load_env_file(root / ".env")

    from lightrag_complete_pipeline import RAGPipeline

    rows = load_manifest(manifest_path)
    pipeline = RAGPipeline()
    results = []

    for row in rows:
        source_path = root / row["file_path"]
        record = {
            "source_id": row["source_id"],
            "file_path": row["file_path"],
            "domain": row["domain"],
            "rag_priority": row["rag_priority"],
            "status": "pending",
        }

        if not source_path.exists():
            record["status"] = "missing"
            record["error"] = f"File not found: {source_path}"
            results.append(record)
            continue

        if dry_run:
            record["status"] = "ready"
            record["bytes"] = source_path.stat().st_size
            results.append(record)
            continue

        result = pipeline.process_document(str(source_path), venture_id=row.get("domain"))
        if "error" in result:
            record["status"] = "failed"
            record["error"] = result["error"]
        else:
            record["status"] = "ingested"
            record["entities_extracted"] = result.get("entities_extracted", 0)
            record["relationships_extracted"] = result.get("relationships_extracted", 0)

        results.append(record)

    sync_result = None
    if sync and not dry_run:
        sync_result = pipeline.sync_to_supabase()

    status = {
        "manifest": str(manifest_path),
        "dry_run": dry_run,
        "sync_to_supabase": sync,
        "sources_total": len(rows),
        "sources_ready": sum(1 for r in results if r["status"] == "ready"),
        "sources_ingested": sum(1 for r in results if r["status"] == "ingested"),
        "sources_missing": sum(1 for r in results if r["status"] == "missing"),
        "sources_failed": sum(1 for r in results if r["status"] == "failed"),
        "results": results,
        "sync_result": sync_result,
    }

    status_path = root / STATUS_FILE
    status_path.write_text(json.dumps(status, indent=2), encoding="utf-8")
    return status


def main() -> int:
    parser = argparse.ArgumentParser(description="Ingest files listed in RAG-INGESTION-MANIFEST.csv")
    parser.add_argument("--manifest", default=DEFAULT_MANIFEST, help="Path to ingestion manifest CSV")
    parser.add_argument("--dry-run", action="store_true", help="Validate manifest file paths without ingesting")
    parser.add_argument("--sync", action="store_true", help="Sync extracted graph data to Supabase after ingestion")
    args = parser.parse_args()

    status = ingest_manifest(Path(args.manifest).resolve(), dry_run=args.dry_run, sync=args.sync)
    print(json.dumps({
        "sources_total": status["sources_total"],
        "sources_ready": status["sources_ready"],
        "sources_ingested": status["sources_ingested"],
        "sources_missing": status["sources_missing"],
        "sources_failed": status["sources_failed"],
        "status_file": STATUS_FILE,
    }, indent=2))
    return 1 if status["sources_missing"] or status["sources_failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
