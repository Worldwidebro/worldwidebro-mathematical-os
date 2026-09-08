#!/usr/bin/env python3
"""
Company Brain — Context & Prompt Compression Engine
Deterministic token reduction via RTK (tool outputs) and Caveman (prompts).

Authority: System Architecture & Infrastructure Control Plane (CP-027)
Latency Target: < 2.0 ms execution time
Zero Neural Overhead: Pure deterministic text, regex, and AST compaction
"""

import re
import json
import time
from typing import Tuple, Dict, Any, Optional
from pathlib import Path

# Import token ledger for exact token measurement
try:
    from .token_ledger import ledger
except ImportError:
    try:
        from token_ledger import ledger
    except ImportError:
        ledger = None


class RTKCompactor:
    """
    Real-Time Token (RTK) Compactor.
    Specialized in tool execution outputs, bash returns, file listings, and JSON trees.
    Target reduction: 60% - 90% of raw output tokens.
    """

    # ANSI color and escape code pattern
    ANSI_ESCAPE = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")

    # Git diff header lines that waste tokens without aiding LLM code reasoning
    GIT_DIFF_JUNK = re.compile(r"^\s*index [0-9a-f]{7,40}\.\.[0-9a-f]{7,40}(?: \d+)?\s*$", re.MULTILINE)
    GIT_FILE_MODE = re.compile(r"^\s*(?:new file mode|old mode|deleted file mode) \d+\s*$", re.MULTILINE)
    GIT_EXTENDED_HEADER = re.compile(r"^\s*(?:similarity index|rename from|rename to) .+$", re.MULTILINE)

    @classmethod
    def strip_ansi(cls, text: str) -> str:
        """Remove all terminal escape sequences and colors."""
        return cls.ANSI_ESCAPE.sub("", text)

    @classmethod
    def compact_whitespace(cls, text: str) -> str:
        """Collapse redundant blank lines and trailing whitespace."""
        # Replace 3 or more newlines with 2 newlines
        text = re.sub(r"\n{3,}", "\n\n", text)
        # Strip trailing whitespace on each line
        lines = [line.rstrip() for line in text.splitlines()]
        return "\n".join(lines).strip()

    @classmethod
    def compact_json(cls, text: str) -> str:
        """Compact JSON text, removing nulls, empty collections, and unnecessary indenting."""
        try:
            data = json.loads(text)
            def _clean(obj):
                if isinstance(obj, dict):
                    return {k: _clean(v) for k, v in obj.items() if v is not None and v != "" and v != [] and v != {}}
                elif isinstance(obj, list):
                    return [_clean(item) for item in obj if item is not None and item != "" and item != [] and item != {}]
                return obj
            cleaned = _clean(data)
            return json.dumps(cleaned, separators=(",", ":"))
        except Exception:
            return text

    @classmethod
    def compact_git_diff(cls, text: str) -> str:
        """Remove low-information git metadata from diff outputs."""
        text = cls.GIT_DIFF_JUNK.sub("", text)
        text = cls.GIT_FILE_MODE.sub("", text)
        text = cls.GIT_EXTENDED_HEADER.sub("", text)
        # Shorten @@ hunk headers from "@@ -12,8 +12,9 @@ def foo():" to "@@ def foo():"
        text = re.sub(r"^\s*@@ -\d+(?:,\d+)? \+\d+(?:,\d+)? @@", "@@", text, flags=re.MULTILINE)
        return text

    @classmethod
    def deduplicate_repeated_lines(cls, text: str, min_consecutive: int = 3) -> str:
        """Collapse repeated log lines into [repeated N times]."""
        lines = text.splitlines()
        if len(lines) < min_consecutive:
            return text

        result = []
        i = 0
        while i < len(lines):
            line = lines[i]
            count = 1
            while i + count < len(lines) and lines[i + count] == line:
                count += 1
            if count >= min_consecutive:
                result.append(f"{line} [repeated {count} times]")
                i += count
            else:
                result.append(line)
                i += 1
        return "\n".join(result)

    @classmethod
    def compact(cls, text: str) -> str:
        """Run full RTK compression pipeline on tool or CLI output."""
        if not text:
            return ""
        # 1. Strip ANSI escapes
        text = cls.strip_ansi(text)
        # 2. Compact git diffs if diff syntax is detected
        if "diff --git" in text or "@@" in text:
            text = cls.compact_git_diff(text)
        # 3. Compact JSON if payload is valid JSON
        stripped = text.strip()
        if (stripped.startswith("{") and stripped.endswith("}")) or (stripped.startswith("[") and stripped.endswith("]")):
            text = cls.compact_json(text)
        # 4. Deduplicate repeated progress logs
        text = cls.deduplicate_repeated_lines(text)
        # 5. Collapse excessive whitespace
        text = cls.compact_whitespace(text)
        return text


class CavemanCompactor:
    """
    Caveman Prompt & Conversational Compactor.
    Specialized in system prompts, conversational history, and user requests.
    Target reduction: 20% - 45% of prompt tokens without semantic degradation.
    """

    # Conversational filler and politeness patterns to prune
    FILLER_PATTERNS = [
        r"\b(?:please|kindly|could you|would you|can you|if you don't mind)\b",
        r"\b(?:hello|hi there|hey|greetings|hope you are doing well)\b",
        r"\b(?:thank you|thanks in advance|i would really appreciate it)\b",
        r"\b(?:as you may know|as you know|needless to say|it goes without saying)\b",
        r"\b(?:in order to|with the intention of|for the purpose of)\b",
        r"\b(?:make sure that you|be sure to|ensure that you|it is important that you)\b",
        r"\b(?:feel free to|at your earliest convenience)\b",
        r"\b(?:i want you to|i would like you to|your task is to)\b",
    ]

    # Pre-compiled regex patterns
    COMPILED_FILLERS = [re.compile(p, re.IGNORECASE) for p in FILLER_PATTERNS]

    @classmethod
    def compact(cls, text: str) -> str:
        """Compact conversational text while rigorously protecting code and Markdown blocks."""
        if not text:
            return ""

        # Protect code blocks (```code```) from any regex manipulation
        code_blocks = []
        def _save_code(match):
            code_blocks.append(match.group(0))
            return f"__CODE_BLOCK_{len(code_blocks) - 1}__"

        protected_text = re.sub(r"```[\s\S]*?```", _save_code, text)

        # Protect inline code (`code`)
        inline_blocks = []
        def _save_inline(match):
            inline_blocks.append(match.group(0))
            return f"__INLINE_BLOCK_{len(inline_blocks) - 1}__"

        protected_text = re.sub(r"`[^`\n]+`", _save_inline, protected_text)

        # Prune filler phrases from prose
        for pattern in cls.COMPILED_FILLERS:
            protected_text = pattern.sub("", protected_text)

        # Collapse whitespace resulting from stripped words
        protected_text = re.sub(r"[ \t]+", " ", protected_text)
        protected_text = re.sub(r"\n\s*\n+", "\n\n", protected_text)

        # Restore inline code
        for idx, block in enumerate(inline_blocks):
            protected_text = protected_text.replace(f"__INLINE_BLOCK_{idx}__", block)

        # Restore code blocks
        for idx, block in enumerate(code_blocks):
            protected_text = protected_text.replace(f"__CODE_BLOCK_{idx}__", block)

        return protected_text.strip()


class UnifiedCompressor:
    """Unified Context Compression Manager for Company Brain."""

    @staticmethod
    def compress(text: str, mode: str = "auto") -> Tuple[str, Dict[str, Any]]:
        """
        Compress text and measure exact token reduction and execution latency.
        Modes:
          - 'auto': Automatically detects tool output vs. conversational prompt
          - 'rtk': Enforces RTK output compression
          - 'caveman': Enforces Caveman prompt compaction
          - 'both': Runs RTK followed by Caveman
        """
        start_time = time.perf_counter()

        # Token count before
        orig_tokens = ledger.count_tokens(text) if ledger else max(1, len(text) // 4)
        orig_chars = len(text)

        if mode == "auto":
            # Heuristic: tool outputs typically have git diffs, JSON braces, or lots of punctuation
            is_tool_output = (
                text.startswith("{") or text.startswith("[") or
                "diff --git" in text or "total " in text or "\x1b" in text or
                text.count("\n") > 15
            )
            mode = "rtk" if is_tool_output else "caveman"

        if mode == "rtk":
            compressed = RTKCompactor.compact(text)
        elif mode == "caveman":
            compressed = CavemanCompactor.compact(text)
        elif mode == "both":
            compressed = CavemanCompactor.compact(RTKCompactor.compact(text))
        else:
            compressed = text

        latency_ms = round((time.perf_counter() - start_time) * 1000, 3)

        # Token count after
        comp_tokens = ledger.count_tokens(compressed) if ledger else max(1, len(compressed) // 4)
        comp_chars = len(compressed)

        savings_tokens = max(0, orig_tokens - comp_tokens)
        savings_pct = round((savings_tokens / max(1, orig_tokens)) * 100, 2)
        char_savings_pct = round(((orig_chars - comp_chars) / max(1, orig_chars)) * 100, 2)

        stats = {
            "mode": mode,
            "original_tokens": orig_tokens,
            "compressed_tokens": comp_tokens,
            "tokens_saved": savings_tokens,
            "savings_pct": savings_pct,
            "original_chars": orig_chars,
            "compressed_chars": comp_chars,
            "char_savings_pct": char_savings_pct,
            "latency_ms": latency_ms,
        }

        return compressed, stats


# Global helper functions
def compress_tool_output(text: str) -> str:
    compressed, _ = UnifiedCompressor.compress(text, mode="rtk")
    return compressed


def compress_prompt(text: str) -> str:
    compressed, _ = UnifiedCompressor.compress(text, mode="caveman")
    return compressed


if __name__ == "__main__":
    import sys
    sample_text = """
    Please ensure that you make sure to check the following git diff output kindly:
    diff --git a/app.py b/app.py
    index 83a1b2c..94d3e4f 100644
    --- a/app.py
    +++ b/app.py
    @@ -10,4 +10,4 @@ def run():
     -    print("Old debugging log")
     +    print("Optimized production log")
    """
    comp, metrics = UnifiedCompressor.compress(sample_text, mode="both")
    print("--- Original ---")
    print(sample_text.strip())
    print("\n--- Compressed ---")
    print(comp)
    print("\n--- Metrics ---")
    print(json.dumps(metrics, indent=2))
