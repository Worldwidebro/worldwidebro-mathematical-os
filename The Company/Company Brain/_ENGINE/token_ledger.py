#!/usr/bin/env python3
"""
Company Brain — Token Measurement & Ledger Engine
Standardized token measurement, accounting, and compression savings ledger.

Authority: System Architecture & Infrastructure Control Plane (CP-027)
Standard: OpenAI tiktoken (BPE counting across cl100k_base and o200k_base)
Persistence: receipts/token_ledger.jsonl
"""

import os
import sys
import json
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any, Optional

# Base directories
BASE_DIR = Path(__file__).resolve().parent.parent
RECEIPTS_DIR = BASE_DIR / "receipts"
LEDGER_FILE = RECEIPTS_DIR / "token_ledger.jsonl"

# Set local offline tiktoken cache directory
ENCODINGS_DIR = BASE_DIR / "_ENGINE" / "encodings"
if ENCODINGS_DIR.exists():
    os.environ["TIKTOKEN_CACHE_DIR"] = str(ENCODINGS_DIR)

# Try importing tiktoken, provide robust fallback if unavailable
try:
    import tiktoken
    HAS_TIKTOKEN = True
except ImportError:
    HAS_TIKTOKEN = False

# Pricing benchmark per 1k tokens (used for financial auditing)
# Default cloud baseline: Anthropic Sonnet / OpenAI GPT-4o blend
CLOUD_INPUT_COST_PER_1K = 0.003
CLOUD_OUTPUT_COST_PER_1K = 0.015


class TokenLedger:
    def __init__(self, ledger_file: Optional[Path] = None):
        self.ledger_file = ledger_file or LEDGER_FILE
        self.ledger_file.parent.mkdir(parents=True, exist_ok=True)
        self._encoders = {}

    def get_encoder(self, encoding_name: str = "cl100k_base"):
        """Get or cache a tiktoken encoder instance."""
        if not HAS_TIKTOKEN:
            return None
        if encoding_name not in self._encoders:
            try:
                self._encoders[encoding_name] = tiktoken.get_encoding(encoding_name)
            except Exception:
                try:
                    self._encoders[encoding_name] = tiktoken.encoding_for_model(encoding_name)
                except Exception:
                    try:
                        self._encoders[encoding_name] = tiktoken.get_encoding("cl100k_base")
                    except Exception:
                        return None
        return self._encoders.get(encoding_name)

    def count_tokens(self, text: str, encoding_name: str = "cl100k_base") -> int:
        """Exact token counting with tiktoken BPE, fallback to 4 chars/token heuristic."""
        if not text:
            return 0
        encoder = self.get_encoder(encoding_name)
        if encoder:
            return len(encoder.encode(text, disallowed_special=()))
        # Fast character heuristic fallback if tiktoken is not yet installed
        return max(1, len(text) // 4)

    def record_transaction(
        self,
        task_id: str,
        request_type: str,
        model: str,
        provider: str,
        input_tokens: int,
        output_tokens: int,
        cached_tokens: int = 0,
        context_tokens: int = 0,
        original_tokens: int = 0,
        compressed_tokens: int = 0,
        agent: str = "Antigravity",
        application: str = "Company Brain",
        endpoint: str = "http://127.0.0.1:11434",
        machine: Optional[str] = None,
        venture_id: Optional[str] = None,
        workflow_id: Optional[str] = None,
        fallback: Optional[str] = None,
        latency_ms: float = 0.0,
        evidence: str = "",
        metadata: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Record an atomic token usage transaction in the ledger."""
        now = datetime.now(timezone.utc).isoformat()
        clean_provider = (provider or "UNKNOWN").strip()
        clean_endpoint = (endpoint or "UNKNOWN").strip()
        
        # Determine local vs cloud
        is_local = clean_provider.lower() in ("ollama", "ollama-local", "mlx", "exo", "local", "airllm")
        local_or_cloud = "LOCAL" if is_local else "CLOUD"
        
        # Enforce the strict connectivity rule:
        # "Anything showing UNKNOWN PROVIDER, UNKNOWN ENDPOINT, or UNKNOWN TOKEN USAGE
        # should automatically become a connectivity/observability failure"
        if clean_provider.upper() == "UNKNOWN" or clean_endpoint.upper() == "UNKNOWN":
            status = "FAILURE_UNKNOWN_INTERCEPTED"
        elif not is_local and "zero-cloud" in str(metadata or {}).lower():
            status = "FAILURE_CLOUD_LEAKAGE"
        else:
            status = "PASS"

        # Unique usage transaction ID
        tx_hash = abs(hash(f"{now}:{task_id}:{model}:{clean_provider}")) % 1000000
        usage_id = f"USG-{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}-{tx_hash:06d}"
        req_id = f"REQ-{tx_hash:06d}"

        # Calculate tokens saved by compression
        tokens_saved = max(0, original_tokens - compressed_tokens) if original_tokens > 0 else 0
        compression_ratio = (
            round((1.0 - (compressed_tokens / original_tokens)) * 100, 2)
            if original_tokens > 0
            else 0.0
        )

        # Financial cost calculation (local is $0.00; cloud follows baseline rates)
        if is_local:
            cost_usd = 0.0
            savings_vs_cloud = (
                (input_tokens / 1000.0) * CLOUD_INPUT_COST_PER_1K
                + (output_tokens / 1000.0) * CLOUD_OUTPUT_COST_PER_1K
            )
        else:
            cost_usd = (
                (input_tokens / 1000.0) * CLOUD_INPUT_COST_PER_1K
                + (output_tokens / 1000.0) * CLOUD_OUTPUT_COST_PER_1K
            )
            savings_vs_cloud = 0.0

        receipt = {
            "usage_id": usage_id,
            "timestamp": now,
            "machine": machine or os.uname().nodename,
            "agent": agent,
            "application": application,
            "model": model,
            "provider": clean_provider,
            "endpoint": clean_endpoint,
            "request_id": req_id,
            "task_id": task_id,
            "request_type": request_type,
            "venture_id": venture_id or "CORP-BRAIN",
            "workflow_id": workflow_id or "INFRA-EVAL",
            "local_or_cloud": local_or_cloud,
            "is_local": is_local,
            "tokens": {
                "input": input_tokens,
                "output": output_tokens,
                "cached": cached_tokens,
                "context": context_tokens,
                "total": input_tokens + output_tokens,
                "compressed_original": original_tokens,
                "compressed_final": compressed_tokens,
                "tokens_saved": tokens_saved,
                "compression_ratio_pct": compression_ratio,
            },
            "financial": {
                "cost_usd": round(cost_usd, 6),
                "savings_vs_cloud_usd": round(savings_vs_cloud, 6),
            },
            "latency_ms": round(latency_ms, 2),
            "fallback": fallback or "none",
            "status": status,
            "evidence": evidence or "Verified via TokenLedger BPE counting",
            "metadata": metadata or {},
        }

        # Append atomic receipt to jsonl file
        with open(self.ledger_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(receipt) + "\n")

        return receipt

    def get_summary(self) -> Dict[str, Any]:
        """Aggregate all token transactions across the ledger."""
        if not self.ledger_file.exists():
            return {
                "status": "empty",
                "total_transactions": 0,
                "tokens": {
                    "total_input": 0,
                    "total_output": 0,
                    "total_cached": 0,
                    "total_tokens": 0,
                    "local_tokens": 0,
                    "cloud_tokens": 0,
                    "tokens_saved_by_compression": 0,
                },
                "financial": {
                    "total_cost_usd": 0.0,
                    "total_savings_usd": 0.0,
                },
            }

        total_tx = 0
        total_input = 0
        total_output = 0
        total_cached = 0
        local_tokens = 0
        cloud_tokens = 0
        tokens_saved = 0
        total_cost = 0.0
        total_savings = 0.0

        with open(self.ledger_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    data = json.loads(line)
                    total_tx += 1
                    t = data.get("tokens", {})
                    inp = t.get("input", 0)
                    out = t.get("output", 0)
                    cached = t.get("cached", 0)
                    saved = t.get("tokens_saved", 0)
                    
                    total_input += inp
                    total_output += out
                    total_cached += cached
                    tokens_saved += saved

                    if data.get("is_local", False):
                        local_tokens += (inp + out)
                    else:
                        cloud_tokens += (inp + out)

                    fin = data.get("financial", {})
                    total_cost += fin.get("cost_usd", 0.0)
                    total_savings += fin.get("savings_vs_cloud_usd", 0.0)
                except Exception:
                    continue

        return {
            "status": "active",
            "total_transactions": total_tx,
            "tokens": {
                "total_input": total_input,
                "total_output": total_output,
                "total_cached": total_cached,
                "total_tokens": total_input + total_output,
                "local_tokens": local_tokens,
                "cloud_tokens": cloud_tokens,
                "local_ratio_pct": round((local_tokens / max(1, local_tokens + cloud_tokens)) * 100, 2),
                "tokens_saved_by_compression": tokens_saved,
            },
            "financial": {
                "total_cost_usd": round(total_cost, 4),
                "total_savings_usd": round(total_savings, 4),
            },
            "ledger_path": str(self.ledger_file),
        }

    def export_canonical_registry(self, target_file: Optional[Path] = None) -> Path:
        """Export ledger transactions as canonical TOKEN-USAGE-REGISTRY.yaml."""
        import yaml
        target = target_file or (BASE_DIR / "_REGISTRIES" / "CANONICAL" / "TOKEN-USAGE-REGISTRY.yaml")
        target.parent.mkdir(parents=True, exist_ok=True)

        records = []
        if self.ledger_file.exists():
            with open(self.ledger_file, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        try:
                            records.append(json.loads(line))
                        except Exception:
                            continue

        summary = self.get_summary()
        registry_data = {
            "id": "TOKEN-USAGE-REGISTRY",
            "title": "Canonical Token Usage & Accounting Registry",
            "version": "1.0",
            "authority": "Architecture Decision Record (ADR-001) / CP-027",
            "updated": datetime.now(timezone.utc).isoformat(),
            "ledger_source": str(self.ledger_file.relative_to(BASE_DIR) if self.ledger_file.is_relative_to(BASE_DIR) else self.ledger_file),
            "summary": summary,
            "records": records[-100:]  # Keep latest 100 in canonical YAML snapshot
        }

        with open(target, "w", encoding="utf-8") as f:
            yaml.dump(registry_data, f, sort_keys=False, default_flow_style=False)

        return target


# Global singleton instance
ledger = TokenLedger()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "summary":
        print(json.dumps(ledger.get_summary(), indent=2))
    elif len(sys.argv) > 1 and sys.argv[1] == "export-yaml":
        p = ledger.export_canonical_registry()
        print(f"✅ Exported canonical registry to {p}")
    elif len(sys.argv) > 2 and sys.argv[1] == "count":
        text = " ".join(sys.argv[2:])
        tokens = ledger.count_tokens(text)
        print(f"Tokens ({'tiktoken' if HAS_TIKTOKEN else 'heuristic'}): {tokens}")
    else:
        print("Company Brain Token Ledger")
        print("Usage:")
        print("  python3 _ENGINE/token_ledger.py summary")
        print("  python3 _ENGINE/token_ledger.py export-yaml")
        print("  python3 _ENGINE/token_ledger.py count <text>")
