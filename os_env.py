"""
os_env.py — single source for service endpoints. Scripts import from here so the
whole pipeline runs against localhost (Air) OR the Mac Studio by env vars alone.

Defaults = localhost (Air). To route to Studio over Tailscale, export:
  OLLAMA_BASE_URL=http://100.87.214.70:11434
  QDRANT_URL=http://100.87.214.70:6333
  NEO4J_URI=bolt://100.87.214.70:7687   (+ NEO4J_USER / NEO4J_PASSWORD)
"""
import os


def _base(url):
    return url.rstrip("/")


OLLAMA_BASE = _base(os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434"))
OLLAMA_EMBED = OLLAMA_BASE + "/api/embeddings"
OLLAMA_CHAT = OLLAMA_BASE + "/v1/chat/completions"

QDRANT = _base(os.environ.get("QDRANT_URL", "http://localhost:6333"))

NEO4J_URI = os.environ.get("NEO4J_URI", "bolt://localhost:7687")
NEO4J_AUTH = (os.environ.get("NEO4J_USER", "neo4j"),
              os.environ.get("NEO4J_PASSWORD", "ventures2026"))

EMBED_MODEL = os.environ.get("EMBED_MODEL", "nomic-embed-text")
CHAT_MODEL = os.environ.get("OLLAMA_CHAT_MODEL", "qwen3:8b")
