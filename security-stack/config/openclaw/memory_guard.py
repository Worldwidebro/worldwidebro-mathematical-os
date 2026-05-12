"""
T11 — Memory validation, user isolation, TTL (SQLite). Integrate into RAG ingest + retrieval.
"""

from __future__ import annotations

import hashlib
import json
import re
import sqlite3
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Set


class MemoryGuard:
    def __init__(self, db_path: str = "/app/data/memory_guard.db") -> None:
        self.db_path = db_path
        self.blocked_patterns: List[str] = [
            r"(?i)delete.*all.*memory",
            r"(?i)corrupt.*(knowledge|memory|vector)",
            r"(?i)previous.*context.*is.*wrong",
            r"(?i)ignore.*past.*(conversation|memory)",
            r"(?i)<!--.*-->.*<script",
            r"(\\x[0-9a-fA-F]{2}){40,}",
        ]
        self.blocked_hashes: Set[str] = {
            "8a1f5c9e3b7d2a4f6c8e0b1a3d5f7c9e2b4d6f8a0c2e4f6a8b0d2c4e6f8a0b2",
        }
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        self.init_database()

    def init_database(self) -> None:
        conn = sqlite3.connect(self.db_path)
        try:
            cur = conn.cursor()
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS memories (
                    id TEXT PRIMARY KEY,
                    content TEXT,
                    source TEXT,
                    user_id TEXT,
                    timestamp TEXT,
                    expires_at TEXT,
                    hash TEXT,
                    poison_score REAL,
                    is_poisoned INTEGER DEFAULT 0
                )
                """
            )
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS poisoning_attempts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    content TEXT,
                    source TEXT,
                    pattern_matched TEXT,
                    timestamp TEXT
                )
                """
            )
            self._migrate(conn)
            cur.execute(
                "CREATE INDEX IF NOT EXISTS idx_memories_user_ts ON memories(user_id, timestamp)"
            )
            cur.execute(
                "CREATE INDEX IF NOT EXISTS idx_memories_expires ON memories(expires_at)"
            )
            conn.commit()
        finally:
            conn.close()

    def _migrate(self, conn: sqlite3.Connection) -> None:
        cur = conn.execute("PRAGMA table_info(memories)")
        cols = {row[1] for row in cur.fetchall()}
        if not cols:
            return
        if "user_id" not in cols:
            conn.execute("ALTER TABLE memories ADD COLUMN user_id TEXT")
        if "expires_at" not in cols:
            conn.execute("ALTER TABLE memories ADD COLUMN expires_at TEXT")

    def is_trusted_source(self, source: str, trusted: Optional[Set[str]] = None) -> bool:
        trusted = trusted or {"system", "authenticated_user", "admin_api"}
        return source in trusted

    def log_attempt(self, content: str, source: str, reason: str) -> None:
        conn = sqlite3.connect(self.db_path)
        try:
            conn.execute(
                "INSERT INTO poisoning_attempts (content, source, pattern_matched, timestamp) VALUES (?,?,?,?)",
                (content[:2000], source, reason, datetime.now(timezone.utc).isoformat()),
            )
            conn.commit()
        finally:
            conn.close()

    def validate_before_write(
        self,
        content: str,
        source: str,
        metadata: Optional[Dict[str, Any]] = None,
        trusted_sources: Optional[Set[str]] = None,
        user_id: str = "default",
        ttl_hours: Optional[float] = None,
    ) -> bool:
        if not self.is_trusted_source(source, trusted_sources):
            self.log_attempt(content, source, "untrusted_source")
            return False

        if len(content) > 100_000:
            self.log_attempt(content, source, "excessive_length")
            return False

        poison_score = 0.0
        matched: List[str] = []
        for pattern in self.blocked_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                poison_score += 0.35
                matched.append(pattern)

        digest = hashlib.sha256(content.encode("utf-8")).hexdigest()
        if digest in self.blocked_hashes:
            self.log_attempt(content, source, "blocked_hash")
            return False

        if poison_score >= 0.5:
            self.log_attempt(content, source, f"patterns:{json.dumps(matched)}")
            return False

        expires_at: Optional[str] = None
        if ttl_hours is not None:
            expires_at = (datetime.now(timezone.utc) + timedelta(hours=ttl_hours)).isoformat()

        self._record_memory(
            content=content,
            source=source,
            user_id=user_id,
            digest=digest,
            poison_score=poison_score,
            is_poisoned=False,
            expires_at=expires_at,
        )
        return True

    def _record_memory(
        self,
        content: str,
        source: str,
        user_id: str,
        digest: str,
        poison_score: float,
        is_poisoned: bool,
        expires_at: Optional[str],
    ) -> None:
        row_id = hashlib.sha256(f"{user_id}:{digest}".encode("utf-8")).hexdigest()
        conn = sqlite3.connect(self.db_path)
        try:
            conn.execute(
                """
                INSERT OR REPLACE INTO memories
                (id, content, source, user_id, timestamp, expires_at, hash, poison_score, is_poisoned)
                VALUES (?,?,?,?,?,?,?,?,?)
                """,
                (
                    row_id,
                    content[:5000],
                    source,
                    user_id,
                    datetime.now(timezone.utc).isoformat(),
                    expires_at,
                    digest,
                    poison_score,
                    int(is_poisoned),
                ),
            )
            conn.commit()
        finally:
            conn.close()

    def get_memories(self, user_id: str, limit: int = 10) -> List[str]:
        now = datetime.now(timezone.utc).isoformat()
        self.cleanup_expired(now)
        conn = sqlite3.connect(self.db_path)
        try:
            cur = conn.execute(
                """
                SELECT content FROM memories
                WHERE user_id = ?
                  AND is_poisoned = 0
                  AND (expires_at IS NULL OR expires_at > ?)
                ORDER BY timestamp DESC
                LIMIT ?
                """,
                (user_id, now, limit),
            )
            return [row[0] for row in cur.fetchall()]
        finally:
            conn.close()

    def cleanup_expired(self, now_iso: Optional[str] = None) -> int:
        now_iso = now_iso or datetime.now(timezone.utc).isoformat()
        conn = sqlite3.connect(self.db_path)
        try:
            cur = conn.execute(
                "DELETE FROM memories WHERE expires_at IS NOT NULL AND expires_at <= ?",
                (now_iso,),
            )
            conn.commit()
            return cur.rowcount or 0
        finally:
            conn.close()
