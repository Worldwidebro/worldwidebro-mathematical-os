"""
Redact high-entropy secrets from log records before they hit handlers.
Wire: logging.getLogger().addFilter(RedactingFilter())
"""

from __future__ import annotations

import logging
import re
from typing import List, Pattern, Tuple

SECRET_PATTERNS: List[Tuple[Pattern[str], str]] = [
    (re.compile(r"\b[A-Za-z0-9_-]{32,}\b"), "[TOKEN_REDACTED]"),
    (re.compile(r"\bsk-[A-Za-z0-9]{20,}\b"), "[OPENAI_KEY_REDACTED]"),
    (re.compile(r"\bghp_[A-Za-z0-9]{20,}\b"), "[GITHUB_TOKEN_REDACTED]"),
    (re.compile(r"(?i)password\s*[:=]\s*\S+"), "password=[REDACTED]"),
    (re.compile(r"(?i)api[_-]?key\s*[:=]\s*\S+"), "api_key=[REDACTED]"),
]


class RedactingFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        try:
            msg = record.getMessage()
        except Exception:
            return True
        for pattern, replacement in SECRET_PATTERNS:
            msg = pattern.sub(replacement, msg)
        record.msg = msg
        record.args = ()
        return True
