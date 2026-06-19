#!/usr/bin/env python3
"""
Bridge Layer Orchestrator — Autonomous Loop
Chains all 7 pipeline steps into a single executable loop.

Usage:
  python3 bridge_layer_orchestrator.py --once      # Run once
  python3 bridge_layer_orchestrator.py --loop 24h  # Run daily
  python3 bridge_layer_orchestrator.py --loop 1h   # Run hourly

Execution sequence:
  1. Scan repos (GitHub → REPOSITORY-REGISTRY.json)
  2. Classify repos (semantic analysis)
  3. Load graph (Supabase entities + relationships)
  4. Create mappings (venture → repos)
  5. Export dashboard (Obsidian sync)
  6. Verify integrity (tests)
  7. Report results (to Slack, stdout, Supabase)
"""

import os
import sys
import json
import subprocess
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple
from dotenv import load_dotenv

# Load environment
load_dotenv()

class BridgeLayerOrchestrator:
    def __init__(self):
        self.base_dir = Path('/Users/acebless/Documents')
        self.start_time = None
        self.results = {}
        self.errors = []

    def run_step(self, name: str, script: str, args: List[str] = None) -> Tuple[bool, str]:
        """Execute a single pipeline step. Returns (success, output)"""
        print(f"\n{'='*100}")
        print(f"🔄 STEP: {name}")
        print(f"{'='*100}")

        cmd = [sys.executable, script]
        if args:
            cmd.extend(args)

        try:
            result = subprocess.run(
                cmd,
                cwd=str(self.base_dir),
                capture_output=True,
                text=True,
                timeout=600  # 10 minute timeout per step
            )

            # Print live output
            if result.stdout:
                print(result.stdout)

            if result.returncode == 0:
                print(f"✅ {name} completed successfully")
                self.results[name] = 'SUCCESS'
                return True, result.stdout
            else:
                error_msg = result.stderr or result.stdout or "Unknown error"
                print(f"❌ {name} failed: {error_msg}")
                self.results[name] = 'FAILED'
                self.errors.append((name, error_msg))
                return False, error_msg

        except subprocess.TimeoutExpired:
            print(f"⏱️  {name} timed out (>10 min)")
            self.results[name] = 'TIMEOUT'
            self.errors.append((name, "Timeout"))
            return False, "Timeout"
        except Exception as e:
            print(f"❌ {name} error: {e}")
            self.results[name] = 'ERROR'
            self.errors.append((name, str(e)))
            return False, str(e)

    def execute_pipeline(self) -> bool:
        """Execute the full bridge layer pipeline"""
        self.start_time = datetime.now()
        print("\n" + "="*100)
        print("🚀 BRIDGE LAYER ORCHESTRATOR — FULL PIPELINE EXECUTION")
        print(f"   Started: {self.start_time.isoformat()}")
        print("="*100)

        steps = [
            # Step 1: Scan repos
            {
                'name': '1️⃣ REPO DISCOVERY',
                'script': 'scan_repositories.py',
                'description': 'Fetch 1,669 repos from GitHub'
            },
            # Step 2: Classify phase 1
            {
                'name': '2️⃣ SEMANTIC CLASSIFICATION (Phase 1)',
                'script': 'repo_classification_phase1.py',
                'description': 'Categorize: Asset | Product | Service | Infrastructure'
            },
            # Step 3: Classify phase 2
            {
                'name': '3️⃣ ADVANCED ANALYSIS (Phase 2)',
                'script': 'repo_classification_phase2.py',
                'description': 'Score: reusability, revenue, strategic value (0-30)'
            },
            # Step 4: Load to graph
            {
                'name': '4️⃣ GRAPH INTEGRATION',
                'script': 'populate_venture_knowledge_graph.py',
                'description': 'Load to Supabase: entities + relationships'
            },
            # Step 5: Create mappings
            {
                'name': '5️⃣ VENTURE MAPPING',
                'script': 'repository_venture_mapping.py',
                'description': 'Generate: venture → [repos] lookup'
            },
            # Step 6: Export dashboard
            {
                'name': '6️⃣ OBSIDIAN SYNC',
                'script': 'obsidian_graph_sync.py',
                'description': 'Export graph to Obsidian dashboard'
            },
            # Step 7: Verify
            {
                'name': '7️⃣ VERIFICATION',
                'script': 'test_integration.py',
                'description': 'Run integration tests'
            },
        ]

        # Execute each step
        successful_steps = 0
        for step in steps:
            success, output = self.run_step(step['name'], step['script'])
            if success:
                successful_steps += 1
            else:
                # Continue on error, but track it
                print(f"⚠️  Continuing despite error in {step['name']}")

        return len(self.errors) == 0, successful_steps, len(steps)

    def report_results(self) -> Dict:
        """Generate execution report"""
        elapsed = (datetime.now() - self.start_time).total_seconds()

        report = {
            'timestamp': datetime.now().isoformat(),
            'duration_seconds': elapsed,
            'total_steps': len(self.results),
            'successful_steps': sum(1 for v in self.results.values() if v == 'SUCCESS'),
            'failed_steps': sum(1 for v in self.results.values() if v == 'FAILED'),
            'timeout_steps': sum(1 for v in self.results.values() if v == 'TIMEOUT'),
            'results': self.results,
            'errors': self.errors,
        }

        # Print report
        print("\n" + "="*100)
        print("📊 EXECUTION REPORT")
        print("="*100)
        print(f"\nDuration: {elapsed:.1f} seconds ({elapsed/60:.1f} minutes)")
        print(f"Steps completed: {report['successful_steps']}/{report['total_steps']}")
        print(f"Success rate: {100*report['successful_steps']/report['total_steps']:.0f}%")

        if self.errors:
            print(f"\n⚠️  {len(self.errors)} errors encountered:")
            for step_name, error in self.errors:
                print(f"   • {step_name}: {error[:100]}")

        # Save report to JSON
        report_path = self.base_dir / 'bridge_layer_execution_report.json'
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=2)

        print(f"\n📁 Report saved: bridge_layer_execution_report.json")

        return report

    def post_to_slack(self, report: Dict):
        """Send report to Slack (if configured)"""
        slack_webhook = os.getenv('SLACK_WEBHOOK_BRIDGE_LAYER')
        if not slack_webhook:
            return

        success = report['failed_steps'] == 0
        status = "✅ SUCCESS" if success else f"⚠️ {report['failed_steps']} failures"

        payload = {
            'text': f"Bridge Layer Pipeline Execution",
            'blocks': [
                {
                    'type': 'section',
                    'text': {
                        'type': 'mrkdwn',
                        'text': f"*Bridge Layer Pipeline Execution*\n{status}\n{report['successful_steps']}/{report['total_steps']} steps completed in {report['duration_seconds']/60:.1f}m"
                    }
                }
            ]
        }

        try:
            import urllib.request
            req = urllib.request.Request(
                slack_webhook,
                data=json.dumps(payload).encode(),
                headers={'Content-Type': 'application/json'},
                method='POST'
            )
            urllib.request.urlopen(req)
            print("✅ Report posted to Slack")
        except Exception as e:
            print(f"⚠️  Slack notification failed: {e}")

def main():
    import argparse

    parser = argparse.ArgumentParser(description='Bridge Layer Orchestrator')
    parser.add_argument('--once', action='store_true', help='Run once and exit')
    parser.add_argument('--loop', type=str, help='Run in loop (e.g., "1h", "24h", "daily")')
    parser.add_argument('--interval', type=int, help='Interval in seconds')
    args = parser.parse_args()

    # Determine execution mode
    loop_enabled = args.loop or args.interval

    if loop_enabled:
        # Parse interval
        interval = args.interval
        if args.loop:
            if args.loop == 'hourly' or args.loop == '1h':
                interval = 3600
            elif args.loop == 'daily' or args.loop == '24h':
                interval = 86400
            elif 'h' in args.loop:
                hours = int(args.loop.replace('h', ''))
                interval = hours * 3600
            elif 'm' in args.loop:
                minutes = int(args.loop.replace('m', ''))
                interval = minutes * 60
            else:
                interval = 3600  # Default 1h

        print(f"🔄 Running in LOOP mode (interval: {interval}s = {interval/3600:.1f}h)")
        print(f"Press Ctrl+C to stop\n")

        iteration = 0
        while True:
            iteration += 1
            print(f"\n{'#'*100}")
            print(f"# ITERATION {iteration} — {datetime.now().isoformat()}")
            print(f"{'#'*100}\n")

            orchestrator = BridgeLayerOrchestrator()
            success, successful, total = orchestrator.execute_pipeline()
            report = orchestrator.report_results()
            orchestrator.post_to_slack(report)

            print(f"\n⏳ Sleeping for {interval}s until next iteration...")
            time.sleep(interval)
    else:
        # One-time execution
        orchestrator = BridgeLayerOrchestrator()
        success, successful, total = orchestrator.execute_pipeline()
        report = orchestrator.report_results()
        orchestrator.post_to_slack(report)

        if not success:
            sys.exit(1)

if __name__ == '__main__':
    main()
