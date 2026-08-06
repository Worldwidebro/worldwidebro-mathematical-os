#!/usr/bin/env python3
import os
import sys
import json
import urllib.request

def send_email():
    api_key = os.getenv("RESEND_API_KEY")
    if not api_key:
        print("Error: RESEND_API_KEY environment variable is not set.")
        sys.exit(1)
        
    html_path = "/Users/acebless/Documents/WORLDWIDEBRO-OS/03-PORTFOLIO/ventures/active/CON-001/docs/email_lead_gen.html"
    if not os.path.exists(html_path):
        print(f"Error: HTML template not found at {html_path}")
        sys.exit(1)
        
    with open(html_path, "r") as f:
        html_content = f.read()
        
    # We use onboarding@resend.dev as the sender to guarantee delivery to the owner's address (winnerscirclewcllc@gmail.com)
    # without needing a verified custom domain.
    payload = {
        "from": "Ace Construction <onboarding@resend.dev>",
        "to": "winnerscirclewcllc@gmail.com",
        "subject": "🏗️ Your Custom Blueprint Assessment - Ace Construction",
        "html": html_content
    }
    
    url = "https://api.resend.com/emails"
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        },
        method="POST"
    )
    
    try:
        with urllib.request.urlopen(req) as res:
            response_data = json.loads(res.read().decode("utf-8"))
            print("🚀 Email sent successfully via Resend API!")
            print(json.dumps(response_data, indent=2))
    except urllib.error.HTTPError as e:
        error_msg = e.read().decode("utf-8")
        print(f"❌ Failed to send email. HTTP Error {e.code}: {e.reason}")
        print(error_msg)
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    send_email()
