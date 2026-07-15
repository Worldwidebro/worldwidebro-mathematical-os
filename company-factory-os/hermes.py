#!/usr/bin/env python3
"""
Hermes — local-first orchestration agent for the Company Factory OS.

Runs ENTIRELY on a local model via Ollama (default qwen3:8b). No cloud / no API key.
Replaces the cloud `anthropic.Anthropic` client in the old spec
(WORLDWIDEBRO-OS/07-KNOWLEDGE/research/ODYSSEUS-HERMES-ORCHESTRATION-WEEK-1.md).

What it does:
  1. Loads the entity graph (entity-graph.json) — the function-based corporate OS.
  2. classify(): given any new business/deal description, decides its ROLE
     (CONTROL/OPERATIONS/EXPERIMENTATION/CAPITAL/PROTECTION), the right legal
     structure, where it attaches in the graph, and its cash-flow + risk profile.
  3. red_team(): enforces the structural rules (dead layers, IP exposure, SPV reuse).
  4. score_capital(): ranks an OPERATIONS entity for capital allocation by layer margin.

Usage:
  python3 hermes.py validate
  python3 hermes.py classify "an invoice-factoring arm to fund our staffing contracts"
  python3 hermes.py classify "a single roofing job for a $400k commercial client"
  HERMES_MODEL=qwen2.5:3b python3 hermes.py classify "..."   # faster, smaller
"""
import json
import os
import re
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
GRAPH_PATH = os.path.join(HERE, "entity-graph.json")

OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434/v1/chat/completions")
MODEL = os.environ.get("HERMES_MODEL", "qwen3:8b")

ROLES = ["CONTROL", "OPERATIONS", "EXPERIMENTATION", "CAPITAL", "PROTECTION"]


def load_graph():
    with open(GRAPH_PATH) as f:
        return json.load(f)


def _llm(system, user, temperature=0.1):
    """Single chat call to the LOCAL model via Ollama's OpenAI-compatible API."""
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "temperature": temperature,
        "stream": False,
        "response_format": {"type": "json_object"},
    }
    headers = {"Content-Type": "application/json"}
    key = os.environ.get("OLLAMA_API_KEY")
    if key:
        headers["Authorization"] = f"Bearer {key}"
    req = urllib.request.Request(
        OLLAMA_URL,
        data=json.dumps(payload).encode(),
        headers=headers,
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.loads(resp.read())
    return data["choices"][0]["message"]["content"]


def _extract_json(text):
    """qwen3 may wrap output in <think> blocks or prose; pull the JSON object out."""
    # strip <think>...</think> blocks qwen3 emits
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1:
        raise ValueError(f"No JSON found in model output:\n{text}")
    blob = text[start : end + 1]
    try:
        return json.loads(blob)
    except json.JSONDecodeError:
        blob = re.sub(r",(\s*[}\]])", r"\1", blob)  # drop trailing commas
        return json.loads(blob)


def classify(description, graph):
    roles_desc = "\n".join(f"- {k}: {v}" for k, v in graph["roles"].items())
    system = (
        "You are Hermes, the entity-classifier for a holding-company OS. "
        "Every new business idea is a FUNCTION in a system, never just a 'type'. "
        "Assign exactly one role from this set:\n" + roles_desc + "\n"
        "Return ONLY a JSON object, no prose, with keys: "
        "role (one of " + "/".join(ROLES) + "), structure (LLC|C-Corp|LP|Trust|Project LLC), "
        "function (one sentence), cash_flow_in (array), cash_flow_out (array), "
        "risk_level (isolated|exposed), attach_to (an existing entity id from the graph), "
        "reasoning (one sentence)."
    )
    entity_ids = ", ".join(e["id"] for e in graph["entities"])
    user = f"Existing entity ids to attach under: {entity_ids}\n\nNew idea: {description}"
    raw = _llm(system, user)
    result = _extract_json(raw)
    result["_warnings"] = red_team(result)
    return result


def red_team(entity):
    """Enforce the structural rules from the graph. Returns list of violations."""
    w = []
    if not entity.get("function"):
        w.append("DEAD STRUCTURE: no function defined.")
    if not entity.get("cash_flow_in") or not entity.get("cash_flow_out"):
        w.append("DEAD STRUCTURE: missing cash_flow_in/out — a layer with no money flow is dead.")
    if entity.get("role") in ("PROTECTION", "CAPITAL") and entity.get("risk_level") == "exposed":
        w.append("FIREWALL BREACH: IP/cash-role entity is 'exposed' — must be isolated.")
    if entity.get("role") == "EXPERIMENTATION" and entity.get("risk_level") == "exposed":
        w.append("BLAST RADIUS: an SPV/deal entity must be isolated, not exposed.")
    return w


def score_capital(layer, graph):
    """Return the capital-allocation priority for a given layer (1-4)."""
    cl = graph["capital_layers"].get(str(layer))
    if not cl:
        return None
    # Higher margin -> higher allocation priority. Layer 2 (60-80%) ranks top.
    rank = {"2": 1, "3": 2, "1": 3, "4": 4}
    return {"layer": layer, "name": cl["name"], "margin": cl["margin"],
            "allocation_priority": rank.get(str(layer), 99), "lives_in": cl["lives_in"]}


def validate(graph):
    """Run red_team over every existing entity in the graph."""
    print(f"Validating {len(graph['entities'])} entities against red-team rules...\n")
    clean = True
    for e in graph["entities"]:
        warnings = red_team(e)
        status = "OK" if not warnings else "FAIL"
        if warnings:
            clean = False
        print(f"[{status}] {e['id']:<14} {e['role']:<16} {e['name']}")
        for x in warnings:
            print(f"        ! {x}")
    print("\nGraph is structurally sound." if clean else "\nGraph has violations above.")
    return clean


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    graph = load_graph()
    cmd = sys.argv[1]
    if cmd == "validate":
        validate(graph)
    elif cmd == "classify":
        if len(sys.argv) < 3:
            print("usage: hermes.py classify \"<description>\"")
            return
        desc = " ".join(sys.argv[2:])
        print(f"[local model: {MODEL} via {OLLAMA_URL}]\n")
        result = classify(desc, graph)
        print(json.dumps(result, indent=2))
    elif cmd == "score":
        layer = sys.argv[2] if len(sys.argv) > 2 else "2"
        print(json.dumps(score_capital(layer, graph), indent=2))
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
