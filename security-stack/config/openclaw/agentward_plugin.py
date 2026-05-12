"""
T10 — Example prompt / memory guard (AgentWard-style). Wire into your OpenClaw request path.
Dependencies: pyyaml
"""

from __future__ import annotations

import base64
import binascii
import hashlib
import json
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

import ipaddress
import yaml
from urllib.parse import urlparse


@dataclass
class GuardrailResult:
    allowed: bool
    risk_score: float
    flags: List[str] = field(default_factory=list)
    sanitized_prompt: str = ""


class SSRFProtection:
    """Block obvious metadata / loopback / internal-service fetches (markdown, webhooks, tool HTTP)."""

    BLOCKED_HOSTNAMES = frozenset(
        {
            "localhost",
            "metadata.google.internal",
            "metadata",
        }
    )
    BLOCKED_SERVICE_PORTS = frozenset({3000, 8200, 5432, 6379, 9096, 3100})

    def validate_url(self, url: str) -> bool:
        parsed = urlparse(url.strip())
        if parsed.scheme not in ("http", "https"):
            return False
        host = parsed.hostname
        if not host:
            return False
        if host.lower() in self.BLOCKED_HOSTNAMES:
            return False
        if host == "169.254.169.254" or host.startswith("169.254."):
            return False
        try:
            ip = ipaddress.ip_address(host)
            if ip.is_loopback or ip.is_link_local or ip.is_multicast or ip.is_reserved:
                return False
            if ip in ipaddress.ip_network("169.254.0.0/16"):
                return False
        except ValueError:
            if host.endswith(".localhost") or host.endswith(".internal"):
                return False

        scheme = (parsed.scheme or "http").lower()
        port = parsed.port
        if port is None:
            port = 443 if scheme == "https" else 80
        if port in self.BLOCKED_SERVICE_PORTS:
            return False
        return True


class AgentWardGuard:
    """Prompt injection and memory poisoning prevention (template implementation)."""

    def __init__(self, config_path: str | Path) -> None:
        self.config_path = Path(config_path)
        self.config: Dict[str, Any] = {}
        self.injection_patterns: List[str] = []
        self.override_phrases: List[str] = []
        self.blocked_encodings: List[str] = []
        self.poisoning_patterns: List[str] = []
        self.trusted_sources: List[str] = []
        self.blocked_hashes: set[str] = set()
        self.load_config()

    def load_config(self) -> None:
        with self.config_path.open("r", encoding="utf-8") as f:
            self.config = yaml.safe_load(f) or {}

        self.injection_patterns = list(self.config.get("injection_patterns") or [])
        self.override_phrases = list(self.config.get("override_phrases") or [])
        self.blocked_encodings = list(self.config.get("blocked_encodings") or [])
        self.poisoning_patterns = list(self.config.get("poisoning_patterns") or [])
        self.trusted_sources = list(self.config.get("trusted_sources") or [])
        self.blocked_hashes = set(self.config.get("blocked_hashes") or [])

    def check_prompt(self, prompt: str, context: Optional[Dict[str, Any]] = None) -> GuardrailResult:
        risk_score = 0.0
        flags: List[str] = []

        for pattern in self.injection_patterns:
            if re.search(pattern, prompt, re.IGNORECASE):
                risk_score += 0.3
                flags.append(f"injection_pattern:{pattern}")

        lower = prompt.lower()
        for phrase in self.override_phrases:
            if phrase.lower() in lower:
                risk_score += 0.5
                flags.append(f"override_attempt:{phrase}")

        for encoding in self.blocked_encodings:
            if self.detect_encoding(prompt, encoding):
                risk_score += 0.8
                flags.append(f"encoded_payload:{encoding}")

        if len(prompt) > 10_000:
            risk_score += 0.2
            flags.append("excessive_length")

        threshold = float(self.config.get("detection", {}).get("risk_threshold", 0.7))
        allowed = risk_score < threshold
        sanitized = self.sanitize(prompt) if not allowed else prompt

        return GuardrailResult(
            allowed=allowed,
            risk_score=risk_score,
            flags=flags,
            sanitized_prompt=sanitized,
        )

    def check_memory_write(self, content: str, source: str) -> bool:
        if source not in self.trusted_sources:
            return False

        for pattern in self.poisoning_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                self.log_poisoning_attempt(content, pattern)
                return False

        content_hash = hashlib.sha256(content.encode("utf-8")).hexdigest()
        if content_hash in self.blocked_hashes:
            return False

        return True

    def detect_encoding(self, text: str, encoding_type: str) -> bool:
        if encoding_type == "base64":
            b64_pattern = r"[A-Za-z0-9+/]{40,}={0,2}"
            for match in re.findall(b64_pattern, text):
                try:
                    decoded = base64.b64decode(match, validate=False).decode("utf-8", errors="ignore")
                    if any(x in decoded for x in ("curl", "wget", "exec", "eval")):
                        return True
                except (ValueError, binascii.Error, UnicodeDecodeError):
                    continue
        elif encoding_type == "hex":
            hex_pattern = r"[0-9a-fA-F]{100,}"
            for match in re.findall(hex_pattern, text):
                try:
                    decoded = bytes.fromhex(match).decode("utf-8", errors="ignore")
                    if any(x in decoded for x in ("curl", "wget", "exec")):
                        return True
                except ValueError:
                    continue
        return False

    def sanitize(self, prompt: str) -> str:
        prompt = re.sub(r"[A-Za-z0-9+/]{100,}={0,2}", "[BLOCKED_ENCODING]", prompt)
        dangerous_chars = ("$", "`", "$(", "${", "|", "&", ";", ">", "<")
        for char in dangerous_chars:
            prompt = prompt.replace(char, f"\\{char}")
        for phrase in self.override_phrases:
            prompt = re.sub(re.escape(phrase), "[REDACTED]", prompt, flags=re.IGNORECASE)
        return prompt

    def log_poisoning_attempt(self, content: str, pattern: str) -> None:
        log_path = Path("/var/log/openclaw/poisoning.log")
        log_path.parent.mkdir(parents=True, exist_ok=True)
        log_entry = {
            "event": "memory_poisoning_attempt",
            "pattern": pattern,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "content_preview": content[:200],
        }
        with log_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry) + "\n")
