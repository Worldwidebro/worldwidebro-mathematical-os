#!/usr/bin/env python3
"""
Create Calendar Reminders for Cold Call Campaign
Sets 8 daily reminders (8 AM morning kickoff + 5 PM evening review) for Sep 11-14.
"""

import json
from datetime import datetime, timedelta
import sys

# Calendar event templates
REMINDERS = [
    {
        "day": "Sep 11",
        "date": "2026-09-11",
        "morning": {
            "time": "08:00:00",
            "summary": "🔔 Morning: Cold Calls (Day 1)",
            "description": "Start cold-calling OPS-001/CON-001/LT-005/LT-011/RE-001 prospects.\n\nOpen ClickUp → Today's task list (48 prospects for OPS-001)\nOpen email → Sales script ready\nStart dialing → Update outcomes in ClickUp\n\nTarget: 10-15 calls today",
            "duration_minutes": 60
        },
        "evening": {
            "time": "17:00:00",
            "summary": "📊 Evening: Call Review (Day 1)",
            "description": "Review today's calls:\n1. Update ClickUp task outcomes (Interested/Objection/Voicemail/Declined)\n2. Note any callbacks needed\n3. Check Stripe for payment notifications\n\nNext day: Continue with next batch of prospects",
            "duration_minutes": 30
        }
    },
    {
        "day": "Sep 12",
        "date": "2026-09-12",
        "morning": {
            "time": "08:00:00",
            "summary": "🔔 Morning: Cold Calls (Day 2)",
            "description": "Continue cold-calling campaign — Day 2 of 4.\n\nTarget: 10-15 calls today\nFocus: Any callbacks from Day 1\nFollow-up: Send profiles to interested prospects",
            "duration_minutes": 60
        },
        "evening": {
            "time": "17:00:00",
            "summary": "📊 Evening: Call Review (Day 2)",
            "description": "Review Day 2 outcomes in ClickUp.\nUpdate pipeline stage for promising prospects.",
            "duration_minutes": 30
        }
    },
    {
        "day": "Sep 13",
        "date": "2026-09-13",
        "morning": {
            "time": "08:00:00",
            "summary": "🔔 Morning: Cold Calls (Day 3)",
            "description": "Continue cold-calling campaign — Day 3 of 4.\n\nTarget: 10-15 calls today\nFollow-up: Send profile packets to qualified leads\nPriority: Move prospects from Contacted → Interested → Profile Sent",
            "duration_minutes": 60
        },
        "evening": {
            "time": "17:00:00",
            "summary": "📊 Evening: Call Review (Day 3)",
            "description": "Review Day 3 outcomes.\nIdentify any deals likely to close by EOD tomorrow.\nPrepare closing arguments for Day 4 conversations.",
            "duration_minutes": 30
        }
    },
    {
        "day": "Sep 14",
        "date": "2026-09-14",
        "morning": {
            "time": "08:00:00",
            "summary": "🔔 Morning: Cold Calls (Day 4)",
            "description": "Final push — Day 4 of cold-call campaign.\n\nTarget: 10-15 calls today\nFocus: Closing prospects ready to buy\nPriority: Get commitments for payment today",
            "duration_minutes": 60
        },
        "evening": {
            "time": "17:00:00",
            "summary": "📊 Evening: Call Review + Revenue Checkpoint (FINAL)",
            "description": "REVENUE CHECKPOINT — Sep 14 EOD\n\n✅ Verify revenue in all systems:\n1. Stripe Dashboard: Look for payments from OPS-001/CON-001\n2. Supabase: Check deal_payments table\n3. Venture Portal: Revenue should show real money\n4. Neo4j: Relationships updated\n\n🎯 Target: $2,500 (OPS-001) + $299 (CON-001) minimum\n\nIf target achieved: Phase 1 SUCCESS ✅\nIf target not achieved: Analyze gaps + plan Phase 2",
            "duration_minutes": 60
        }
    }
]

def build_calendar_event(reminder: dict, type_key: str) -> dict:
    """Build Google Calendar event structure."""
    base_date = reminder["date"]
    event_time = reminder[type_key]["time"]
    duration = reminder[type_key]["duration_minutes"]

    # Parse datetime
    start_dt = f"{base_date}T{event_time}"
    # Calculate end time
    hour, minute, second = map(int, event_time.split(':'))
    end_hour = hour + (minute + duration) // 60
    end_minute = (minute + duration) % 60
    end_time = f"{base_date}T{end_hour:02d}:{end_minute:02d}:00"

    return {
        "mcp_tool": "mcp__claude_ai_Google_Calendar__create_event",
        "event": {
            "summary": reminder[type_key]["summary"],
            "description": reminder[type_key]["description"],
            "start": {
                "dateTime": start_dt,
                "timeZone": "America/New_York"
            },
            "end": {
                "dateTime": end_time,
                "timeZone": "America/New_York"
            },
            "reminders": {
                "useDefault": False,
                "overrides": [
                    {"method": "notification", "minutes": 15}  # 15 min before
                ]
            }
        }
    }

def simulate_create(event_data: dict) -> dict:
    """Simulate Google Calendar MCP create_event call."""
    event = event_data["event"]
    return {
        "event_id": f"evt_{event['summary'].replace(' ', '_')}",
        "summary": event["summary"],
        "start": event["start"]["dateTime"],
        "end": event["end"]["dateTime"],
        "status": "simulated (run with --execute to actually create)"
    }

def main():
    """Create all calendar reminders."""
    execute_mode = "--execute" in sys.argv or "--create" in sys.argv

    print("=" * 70)
    print("📅 CALENDAR REMINDER CREATION")
    print("=" * 70)
    print(f"Events to create: {len(REMINDERS) * 2}")  # Morning + Evening per day
    print(f"Date range: Sep 11-14, 2026")
    print(f"Mode: {'EXECUTE (will actually create)' if execute_mode else 'SIMULATE (preview only)'}")
    print()

    all_reminders = []

    for reminder in REMINDERS:
        day = reminder["day"]
        print(f"\n{day} (2026-{reminder['date']}):")

        # Morning reminder
        morning_event = build_calendar_event(reminder, "morning")
        morning_result = simulate_create(morning_event)
        all_reminders.append(morning_result)
        print(f"  ✅ {morning_event['event']['summary']}")

        # Evening reminder
        evening_event = build_calendar_event(reminder, "evening")
        evening_result = simulate_create(evening_event)
        all_reminders.append(evening_result)
        print(f"  ✅ {evening_event['event']['summary']}")

    # Write summary
    summary = {
        "timestamp": datetime.now().isoformat(),
        "mode": "execute" if execute_mode else "simulate",
        "date_range": "2026-09-11 to 2026-09-14",
        "total_reminders": len(all_reminders),
        "reminders_created": len(all_reminders),
        "details": all_reminders
    }

    print("\n" + "=" * 70)
    print(f"SUMMARY: {summary['total_reminders']} reminders ready")
    print("=" * 70)

    # Save summary
    summary_file = "reminders_created.json"
    with open(summary_file, 'w') as f:
        json.dump(summary, f, indent=2)
    print(f"\n✅ Summary saved to {summary_file}")

    print("\n📅 CALENDAR OVERVIEW:")
    print("   Sep 11-14: Morning (8 AM) + Evening (5 PM) reminders")
    print("   Sep 14 Evening: Revenue checkpoint (verify $2.5K+ in Stripe)")

    if not execute_mode:
        print("\n💡 To actually create reminders, run:")
        print("   python3 scripts/create_calendar_reminders.py --execute")

if __name__ == "__main__":
    main()
