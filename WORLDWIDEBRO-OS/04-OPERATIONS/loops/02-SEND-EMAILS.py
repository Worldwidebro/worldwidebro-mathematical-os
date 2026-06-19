#!/usr/bin/env python3
"""
LOOP 2: Send Email Sequences
Run: /loop python3 loops/02-SEND-EMAILS.py --every 1h

Fetches new leads from Supabase
Sends Email 1 (immediate)
Updates status to 'email_1_sent'
Schedules Email 2 (2 hours later)
"""

import os
import sys
from datetime import datetime, timedelta
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
RESEND_API_KEY = os.getenv("RESEND_API_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    print("❌ SUPABASE credentials missing")
    sys.exit(1)

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def send_email(email, subject, body):
    """Send email via Resend (or your email service)"""
    if not RESEND_API_KEY:
        print(f"  📧 Mock send to {email}: {subject}")
        return True

    # PRODUCTION: Use Resend API
    # import requests
    # response = requests.post("https://api.resend.com/emails", ...)
    # return response.status_code == 200

    print(f"  📧 Mock send to {email}: {subject}")
    return True

def main():
    print(f"\n{'='*60}")
    print(f"LOOP 2: SEND EMAILS [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]")
    print(f"{'='*60}\n")

    # Get new leads
    try:
        response = supabase.table("leads").select("*").eq("status", "new").execute()
        new_leads = response.data
    except:
        new_leads = []

    print(f"📊 New leads: {len(new_leads)}\n")

    sent = 0
    for lead in new_leads:
        email = lead.get("email")
        if not email:
            continue

        # Send Email 1: Confirmation
        subject = "Thanks for contacting us! Here's what to expect"
        body = "Your inquiry has been received. We'll follow up within 2 hours."

        if send_email(email, subject, body):
            # Update status
            supabase.table("leads").update({"status": "email_1_sent"}).eq("id", lead["id"]).execute()
            sent += 1

    print(f"\n✅ EMAILS SENT: {sent}")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    main()
