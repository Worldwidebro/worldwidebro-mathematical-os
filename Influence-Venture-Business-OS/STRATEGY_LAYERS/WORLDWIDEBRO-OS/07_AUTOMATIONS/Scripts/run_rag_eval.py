#!/usr/bin/env python3
"""Run LightRAG eval questions and record pass rate for the Knowledge Ops scorecard."""

from __future__ import annotations

import argparse
import json
import re
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
EVAL_DOC = ROOT / "WORLDWIDEBRO-OS" / "08_RESEARCH" / "Knowledge-Ops" / "rag-eval-questions.md"
RAG_URL = "http://127.0.0.1:8000/query"


def parse_questions(md: str) -> list[tuple[int, str, str]]:
    rows: list[tuple[int, str, str]] = []
    for line in md.splitlines():
        if not line.startswith("|") or line.startswith("| #") or line.startswith("|---"):
            continue
        parts = [p.strip() for p in line.split("|") if p.strip()]
        if len(parts) < 3 or not parts[0].isdigit():
            continue
        num = int(parts[0])
        question = parts[1]
        expected = parts[2]
        rows.append((num, question, expected))
    return rows


def query_rag(question: str, mode: str = "hybrid") -> str:
    payload = json.dumps({"query": question, "mode": mode}).encode("utf-8")
    req = urllib.request.Request(
        RAG_URL,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        body = json.loads(resp.read().decode("utf-8"))
    return body.get("response") or body.get("answer") or json.dumps(body)


def score_answer(expected: str, answer: str) -> float:
    answer_l = answer.lower()
    tokens = re.findall(r"[a-z0-9][a-z0-9._/-]{2,}", expected.lower())
    if not tokens:
        return 0.0
    hits = sum(1 for t in tokens if t in answer_l)
    ratio = hits / len(tokens)
    if ratio >= 0.5:
        return 1.0
    if ratio >= 0.25:
        return 0.5
    return 0.0


def main() -> None:
    parser = argparse.ArgumentParser(description="LightRAG eval runner")
    parser.add_argument("--limit", type=int, default=0, help="Max questions (0 = all)")
    parser.add_argument("--dry-run", action="store_true", help="Parse only, no HTTP")
    parser.add_argument("--apply-scorecard", action="store_true", help="Update scorecard script hint")
    args = parser.parse_args()

    questions = parse_questions(EVAL_DOC.read_text(encoding="utf-8"))
    if args.limit:
        questions = questions[: args.limit]

    if args.dry_run:
        print(f"Parsed {len(questions)} questions from {EVAL_DOC}")
        return

    results = []
    for num, question, expected in questions:
        try:
            answer = query_rag(question)
            score = score_answer(expected, answer)
            results.append((num, score, question[:60]))
            print(f"Q{num:02d} score={score} — {question[:50]}...")
        except (urllib.error.URLError, TimeoutError) as e:
            print(f"Q{num:02d} skipped — RAG unavailable ({e})")
            break

    if not results:
        print("No results. Start LightRAG (port 8000) or use manual grading.")
        return

    pct = round((sum(s for _, s, _ in results) / len(questions)) * 100, 2)
    print(f"\nRAG eval: {pct}% ({len(results)}/{len(questions)} graded)")
    if args.apply_scorecard:
        import subprocess

        subprocess.run(
            [
                "python3",
                str(ROOT / "WORLDWIDEBRO-OS/07_AUTOMATIONS/Scripts/run_knowledge_ops_scorecard.py"),
                "--rag-eval",
                str(pct),
                "--notes",
                f"automated_rag_eval_{len(results)}_questions",
            ],
            check=False,
        )


if __name__ == "__main__":
    main()
