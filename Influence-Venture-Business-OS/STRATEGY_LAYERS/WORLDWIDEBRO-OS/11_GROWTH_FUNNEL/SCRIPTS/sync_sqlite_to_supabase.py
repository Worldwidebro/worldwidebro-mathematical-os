#!/usr/bin/env python3
"""Push local SQLite content brain rows to Supabase (after migration applied)."""

from __future__ import annotations

import json
import os
import sqlite3
import sys
from pathlib import Path

FUNNEL_ROOT = Path("/Users/acebless/Documents/WORLDWIDEBRO-OS/11_GROWTH_FUNNEL")
sys.path.insert(0, str(FUNNEL_ROOT / "SCRIPTS"))

from content_brain import ContentBrain, _supabase_configured, _supabase_request  # noqa: E402

SQLITE_PATH = FUNNEL_ROOT / "DATA/content_brain.db"


def main() -> None:
    if not _supabase_configured():
        print("❌ Set SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY")
        raise SystemExit(1)
    if not SQLITE_PATH.exists():
        print(f"❌ No local DB at {SQLITE_PATH}")
        raise SystemExit(1)

    conn = sqlite3.connect(SQLITE_PATH)
    conn.row_factory = sqlite3.Row

    ventures = conn.execute("select * from ventures").fetchall()
    for row in ventures:
        _supabase_request(
            "POST",
            "gf_ventures",
            {
                "venture_id": row["venture_id"],
                "venture_code": row["venture_code"],
                "venture_name": row["venture_name"],
                "sector": row["sector"],
                "config": json.loads(row["config"] or "{}"),
            },
        )
    print(f"✅ Synced {len(ventures)} ventures")

    hooks = conn.execute("select * from content_hooks").fetchall()
    if hooks:
        batch = [
            {
                "venture_id": h["venture_id"],
                "hook_text": h["hook_text"],
                "funnel_stage": h["funnel_stage"],
                "source_day": h["source_day"],
                "viral_score": h["viral_score"],
                "status": h["status"],
            }
            for h in hooks
        ]
        _supabase_request("POST", "gf_content_hooks", batch)
        print(f"✅ Synced {len(hooks)} hooks")

    assets = conn.execute("select * from content_assets").fetchall()
    if assets:
        batch = [
            {
                "venture_id": a["venture_id"],
                "funnel_stage": a["funnel_stage"],
                "format": a["format"],
                "hook": a["hook"],
                "body": a["body"],
                "day_of_week": a["day_of_week"],
                "status": a["status"],
                "platform": a["platform"],
                "script_json": json.loads(a["script_json"] or "{}"),
            }
            for a in assets
        ]
        _supabase_request("POST", "gf_content_assets", batch)
        print(f"✅ Synced {len(assets)} assets")

    queue = conn.execute("select * from publish_queue").fetchall()
    if queue:
        batch = [
            {
                "venture_id": q["venture_id"],
                "funnel_stage": q["funnel_stage"],
                "platform": q["platform"],
                "payload": json.loads(q["payload"] or "{}"),
                "status": q["status"],
            }
            for q in queue
        ]
        _supabase_request("POST", "gf_publish_queue", batch)
        print(f"✅ Synced {len(queue)} publish queue rows")

    conn.close()
    print("Done. Verify in Supabase Table Editor.")


if __name__ == "__main__":
    main()
