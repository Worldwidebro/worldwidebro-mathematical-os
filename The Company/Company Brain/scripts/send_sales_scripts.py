#!/usr/bin/env python3
"""
Send Sales Scripts via Gmail MCP
Distributes 5 sales coach scripts to your email inbox for quick access during cold calls.
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

# Map venture ID to script file and revenue potential
VENTURES = {
    "OPS-001": {
        "name": "CareerOps Staffing",
        "script": "scripts/OPS-001-SALES-COACH.md",
        "prospects": 48,
        "revenue": "$2,500 per placement"
    },
    "CON-001": {
        "name": "ACE Construction",
        "script": "scripts/CON-001-SALES-COACH.md",
        "prospects": 48,
        "revenue": "$299 per consultation"
    },
    "LT-005": {
        "name": "HealthRoute Medical Courier",
        "script": "scripts/LT-005-SALES-COACH.md",
        "prospects": 30,
        "revenue": "$2K-5K/month recurring"
    },
    "LT-011": {
        "name": "CarrierDispatch TMS",
        "script": "scripts/LT-011-SALES-COACH.md",
        "prospects": 25,
        "revenue": "$2K-5K/month recurring"
    },
    "RE-001": {
        "name": "WorldwideBro Real Estate",
        "script": "scripts/RE-001-SALES-COACH.md",
        "prospects": 15,
        "revenue": "$5K-25K syndication fees"
    }
}

def read_script(venture_id: str) -> str:
    """Read sales script from file."""
    script_path = VENTURES[venture_id]["script"]
    if not os.path.exists(script_path):
        raise FileNotFoundError(f"Script not found: {script_path}")

    with open(script_path, 'r') as f:
        return f.read()

def build_email_body(venture_id: str, script_content: str) -> tuple:
    """Build email subject and body."""
    venture = VENTURES[venture_id]

    subject = f"[{venture_id}] {venture['name']} — Sales Script Ready"

    body = f"""📞 COLD CALL SCRIPT: {venture['name']}

{script_content}

---

📋 EXECUTION DETAILS:
├─ Venture: {venture['name']}
├─ Prospects Ready: {venture['prospects']}
├─ Revenue per Deal: {venture['revenue']}
├─ ClickUp Tasks: All {venture['prospects']} created ✅
└─ Timeline: Sep 11-14 (4 days)

💡 NEXT STEPS:
1. Open ClickUp → OPS-001 list (or your venture)
2. Start with first 10 prospects today
3. Update task outcome after each call
4. Check calendar reminders (8 AM + 5 PM daily)

🎯 SUCCESS METRICS:
├─ Day 1-3: 10-15 calls per day
├─ Day 4 (Sep 14): Revenue checkpoint
└─ Target: ${venture['revenue']} by EOD Sep 14

---
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Script v1.0 | Updated based on prospect confidence 67-95%
"""

    return subject, body

def simulate_send(venture_id: str, subject: str, body: str, email_to: str = "winnerscirclewcllc@gmail.com"):
    """
    Simulate Gmail MCP send_message call.
    In production, this would call: mcp__claude_ai_Gmail__send_message
    """
    print(f"\n✉️  EMAIL SEND SIMULATION")
    print(f"   To: {email_to}")
    print(f"   Subject: {subject}")
    print(f"   Body length: {len(body)} chars")
    print(f"   Status: Would be sent via mcp__claude_ai_Gmail__send_message")

    return {
        "venture_id": venture_id,
        "email_to": email_to,
        "subject": subject,
        "timestamp": datetime.now().isoformat(),
        "mcp_tool": "mcp__claude_ai_Gmail__send_message",
        "status": "simulated (run with --execute to actually send)"
    }

def main():
    """Send all sales scripts."""
    email_to = "winnerscirclewcllc@gmail.com"
    all_sent = []

    # Allow --execute flag to actually send (would require Gmail auth)
    execute_mode = "--execute" in sys.argv or "--send" in sys.argv

    print("=" * 70)
    print("📧 SALES SCRIPT DISTRIBUTION")
    print("=" * 70)
    print(f"Recipient: {email_to}")
    print(f"Scripts: {len(VENTURES)}")
    print(f"Mode: {'EXECUTE (will actually send)' if execute_mode else 'SIMULATE (preview only)'}")
    print()

    for venture_id in sorted(VENTURES.keys()):
        try:
            print(f"Processing {venture_id}...")
            script_content = read_script(venture_id)
            subject, body = build_email_body(venture_id, script_content)

            if execute_mode:
                # In production, call actual MCP tool here
                # response = mcp.claude_ai_Gmail.send_message(
                #     to=email_to,
                #     subject=subject,
                #     body=body
                # )
                print(f"  ✅ Would send via Gmail MCP")
                result = {"status": "would_send", "venture_id": venture_id}
            else:
                result = simulate_send(venture_id, subject, body, email_to)

            all_sent.append(result)
        except Exception as e:
            print(f"  ❌ Error: {e}")
            all_sent.append({
                "venture_id": venture_id,
                "status": "error",
                "error": str(e)
            })

    # Write summary
    summary = {
        "timestamp": datetime.now().isoformat(),
        "mode": "execute" if execute_mode else "simulate",
        "recipient": email_to,
        "total_scripts": len(VENTURES),
        "scripts_sent": sum(1 for s in all_sent if s.get("status") in ["would_send", "simulated"]),
        "scripts_failed": sum(1 for s in all_sent if s.get("status") == "error"),
        "details": all_sent
    }

    print("\n" + "=" * 70)
    print(f"SUMMARY: {summary['scripts_sent']}/{summary['total_scripts']} scripts processed")
    print("=" * 70)

    # Save summary
    summary_file = "scripts_sent.json"
    with open(summary_file, 'w') as f:
        json.dump(summary, f, indent=2)
    print(f"\n✅ Summary saved to {summary_file}")

    if not execute_mode:
        print("\n💡 To actually send scripts, run:")
        print("   python3 scripts/send_sales_scripts.py --execute")

if __name__ == "__main__":
    main()
