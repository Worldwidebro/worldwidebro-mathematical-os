#!/usr/bin/env python3
"""Content brain storage: Supabase when configured, else local SQLite."""

from __future__ import annotations

import json
import os
import sqlite3
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path
from typing import Any

FUNNEL_ROOT = Path("/Users/acebless/Documents/WORLDWIDEBRO-OS/11_GROWTH_FUNNEL")
DATA_DIR = FUNNEL_ROOT / "DATA"
SQLITE_PATH = DATA_DIR / "content_brain.db"


def _supabase_configured() -> bool:
    return bool(os.environ.get("SUPABASE_URL") and os.environ.get("SUPABASE_SERVICE_ROLE_KEY"))


def _supabase_request(method: str, path: str, body: dict | list | None = None) -> Any:
    url = os.environ["SUPABASE_URL"].rstrip("/") + "/rest/v1/" + path.lstrip("/")
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers={
            "apikey": os.environ["SUPABASE_SERVICE_ROLE_KEY"],
            "Authorization": f"Bearer {os.environ['SUPABASE_SERVICE_ROLE_KEY']}",
            "Content-Type": "application/json",
            "Prefer": "return=representation",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            raw = resp.read().decode()
            return json.loads(raw) if raw else None
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode()
        raise RuntimeError(f"Supabase {method} {path} failed: {exc.code} {detail}") from exc


class ContentBrain:
    def __init__(self) -> None:
        self.use_supabase = _supabase_configured()
        if not self.use_supabase:
            DATA_DIR.mkdir(parents=True, exist_ok=True)
            self._init_sqlite()

    def _init_sqlite(self) -> None:
        conn = sqlite3.connect(SQLITE_PATH)
        conn.executescript(
            """
            create table if not exists ventures (
              venture_id text primary key,
              venture_code text,
              venture_name text,
              sector text,
              config text default '{}'
            );
            create table if not exists content_hooks (
              id integer primary key autoincrement,
              venture_id text not null,
              hook_text text not null,
              funnel_stage text default 'tof',
              source_day text,
              viral_score real default 0,
              status text default 'draft',
              metadata text default '{}',
              created_at text default (datetime('now'))
            );
            create table if not exists content_assets (
              id integer primary key autoincrement,
              venture_id text not null,
              funnel_stage text not null,
              format text default 'post',
              title text,
              hook text,
              body text,
              script_json text,
              platform text,
              day_of_week text,
              status text default 'draft',
              metadata text default '{}',
              created_at text default (datetime('now'))
            );
            create table if not exists publish_queue (
              id integer primary key autoincrement,
              venture_id text not null,
              funnel_stage text not null,
              platform text default 'youtube_shorts',
              payload text default '{}',
              status text default 'ready_for_review',
              created_at text default (datetime('now'))
            );
            create table if not exists weekly_reports (
              id integer primary key autoincrement,
              venture_id text not null,
              week_start text not null,
              report text not null,
              created_at text default (datetime('now')),
              unique(venture_id, week_start)
            );
            """
        )
        conn.commit()
        conn.close()

    def upsert_venture(self, venture_id: str, venture_code: str | None, venture_name: str, sector: str = "") -> None:
        row = {
            "venture_id": venture_id,
            "venture_code": venture_code,
            "venture_name": venture_name,
            "sector": sector,
        }
        if self.use_supabase:
            _supabase_request(
                "POST",
                "gf_ventures",
                {**row, "config": {}},
            )
            return
        conn = sqlite3.connect(SQLITE_PATH)
        conn.execute(
            """
            insert into ventures (venture_id, venture_code, venture_name, sector)
            values (?, ?, ?, ?)
            on conflict(venture_id) do update set
              venture_code=excluded.venture_code,
              venture_name=excluded.venture_name,
              sector=excluded.sector
            """,
            (venture_id, venture_code, venture_name, sector),
        )
        conn.commit()
        conn.close()

    def insert_hooks(self, venture_id: str, hooks: list[str], source_day: str, funnel_stage: str = "tof") -> int:
        count = 0
        if self.use_supabase:
            rows = [
                {
                    "venture_id": venture_id,
                    "hook_text": h,
                    "source_day": source_day,
                    "funnel_stage": funnel_stage,
                    "status": "draft",
                }
                for h in hooks
            ]
            _supabase_request("POST", "gf_content_hooks", rows)
            return len(rows)
        conn = sqlite3.connect(SQLITE_PATH)
        for h in hooks:
            conn.execute(
                "insert into content_hooks (venture_id, hook_text, source_day, funnel_stage) values (?,?,?,?)",
                (venture_id, h, source_day, funnel_stage),
            )
            count += 1
        conn.commit()
        conn.close()
        return count

    def insert_asset(
        self,
        venture_id: str,
        funnel_stage: str,
        fmt: str,
        hook: str | None,
        body: str | None,
        day_of_week: str,
        script_json: dict | None = None,
        platform: str | None = None,
        status: str = "queued",
    ) -> None:
        payload = {
            "venture_id": venture_id,
            "funnel_stage": funnel_stage,
            "format": fmt,
            "hook": hook,
            "body": body,
            "day_of_week": day_of_week,
            "status": status,
            "platform": platform,
            "script_json": script_json or {},
        }
        if self.use_supabase:
            _supabase_request("POST", "gf_content_assets", payload)
            return
        conn = sqlite3.connect(SQLITE_PATH)
        conn.execute(
            """
            insert into content_assets
            (venture_id, funnel_stage, format, hook, body, day_of_week, status, platform, script_json)
            values (?,?,?,?,?,?,?,?,?)
            """,
            (
                venture_id,
                funnel_stage,
                fmt,
                hook,
                body,
                day_of_week,
                status,
                platform,
                json.dumps(script_json or {}),
            ),
        )
        conn.commit()
        conn.close()

    def queue_publish(self, venture_id: str, funnel_stage: str, payload: dict, platform: str = "youtube_shorts") -> None:
        row = {
            "venture_id": venture_id,
            "funnel_stage": funnel_stage,
            "platform": platform,
            "payload": payload,
            "status": "ready_for_review",
        }
        if self.use_supabase:
            _supabase_request("POST", "gf_publish_queue", row)
            return
        conn = sqlite3.connect(SQLITE_PATH)
        conn.execute(
            "insert into publish_queue (venture_id, funnel_stage, platform, payload) values (?,?,?,?)",
            (venture_id, funnel_stage, platform, json.dumps(payload)),
        )
        conn.commit()
        conn.close()

    def save_weekly_report(self, venture_id: str, week_start: str, report: dict) -> None:
        if self.use_supabase:
            _supabase_request(
                "POST",
                "gf_weekly_reports",
                {"venture_id": venture_id, "week_start": week_start, "report": report},
            )
            return
        conn = sqlite3.connect(SQLITE_PATH)
        conn.execute(
            """
            insert into weekly_reports (venture_id, week_start, report)
            values (?,?,?)
            on conflict(venture_id, week_start) do update set report=excluded.report
            """,
            (venture_id, week_start, json.dumps(report)),
        )
        conn.commit()
        conn.close()

    def backend_label(self) -> str:
        return "supabase" if self.use_supabase else f"sqlite:{SQLITE_PATH}"
