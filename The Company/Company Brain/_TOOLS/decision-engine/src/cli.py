"""CLI entrypoint for Company Brain Decision Engine."""

import argparse
import json
import sys
from .engine import DecisionEngine


def main():
    parser = argparse.ArgumentParser(
        prog="decide",
        description="Company Brain Decision Engine — High-speed reflex routing & ambient signal capture.",
    )
    subparsers = parser.add_subparsers(dest="command", help="Subcommand to execute")

    # Route subcommand
    route_parser = subparsers.add_parser("route", help="Resolve text to a GBrain skill")
    route_parser.add_argument("query", type=str, help="The user prompt or instruction")
    route_parser.add_argument("--top-k", type=int, default=5, help="Number of shortlisted candidates")
    route_parser.add_argument("--json", action="store_true", help="Output raw JSON")

    # Signal subcommand
    signal_parser = subparsers.add_parser("signal", help="Detect ambient original thinking & entities")
    signal_parser.add_argument("text", type=str, help="Text to analyze")
    signal_parser.add_argument("--json", action="store_true", help="Output raw JSON")

    # Turn subcommand
    turn_parser = subparsers.add_parser("turn", help="Evaluate full reflex arc for a turn")
    turn_parser.add_argument("text", type=str, help="Full conversation turn text")
    turn_parser.add_argument("--json", action="store_true", help="Output raw JSON")

    # Eval subcommand
    eval_parser = subparsers.add_parser("eval", help="Benchmark resolver against all routing fixtures")
    eval_parser.add_argument("--json", action="store_true", help="Output raw JSON")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    engine = DecisionEngine()

    if args.command == "route":
        res = engine.resolve_skill(args.query, top_k=args.top_k)
        if args.json:
            print(json.dumps(res.model_dump(), indent=2))
        else:
            print(f"🎯 Target Skill:   {res.selected}")
            print(f"🔒 Confidence:     {res.confidence * 100:.1f}%")
            print(f"⚡ Latency:        {res.latency_ms:.2f} ms")
            print(f"📊 Delta Margin:   {res.margin:.3f}")
            print("📋 Shortlist:")
            for cand in res.shortlist:
                print(f"   • {cand.option:<24} (score: {cand.score:.3f})")

    elif args.command == "signal":
        res = engine.detect_signal(args.text)
        if args.json:
            print(json.dumps(res.model_dump(), indent=2))
        else:
            thought_str = f"YES ({res.thought_category})" if res.is_original_thought else "NO"
            print(f"💡 Original Thought: {thought_str}")
            print(f"📡 Signal Strength:  {res.signal_strength}/5")
            print(f"🏢 Entities:         {', '.join(res.entities) if res.entities else 'None'}")
            print(f"⚡ Latency:          {res.latency_ms:.2f} ms")
            print(f"🚀 Action:           {res.recommended_action}")
            print(f"📝 Rationale:        {res.rationale}")

    elif args.command == "turn":
        res = engine.evaluate_turn(args.text)
        print(json.dumps(res, indent=2))

    elif args.command == "eval":
        metrics = engine.benchmark_resolver()
        if args.json:
            print(json.dumps(metrics, indent=2))
        else:
            print("\nGBrain Skill Resolver Benchmark")
            print("===============================")
            print(f"Total Fixtures Evaluated: {metrics['total_fixtures']}")
            print(f"Top-1 Accuracy:           {metrics['top1_accuracy'] * 100:.2f}%")
            print(f"Top-3 Accuracy:           {metrics['top3_accuracy'] * 100:.2f}%")
            print(f"Mean Inference Latency:   {metrics['mean_latency_ms']:.2f} ms")
            print(f"P95 Inference Latency:    {metrics['p95_latency_ms']:.2f} ms")


if __name__ == "__main__":
    main()
