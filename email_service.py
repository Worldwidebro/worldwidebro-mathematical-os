#!/usr/bin/env python3
"""
Email service for transactional emails (Resend).
Triggered by: Zapier automation, event_bus (payment.received, subscription.started)

Sequences:
  - Day 0: Welcome email (first signup confirmation)
  - Day 2: Check-in email (onboarding)
  - Day 5: Follow-up email (upsell)
"""

import asyncio
import logging
import os
from dataclasses import dataclass
from enum import Enum
from typing import Optional

import httpx

logger = logging.getLogger(__name__)

RESEND_API_KEY = os.getenv("RESEND_API_KEY")
RESEND_API_URL = "https://api.resend.com"
FROM_EMAIL = os.getenv("FROM_EMAIL", "noreply@aceconstruction.com")


class EmailTemplate(str, Enum):
    WELCOME = "welcome"
    ONBOARDING_CHECKIN = "onboarding_checkin"
    UPSELL_FOLLOWUP = "upsell_followup"
    PAYMENT_RECEIPT = "payment_receipt"
    REFUND_NOTICE = "refund_notice"


@dataclass
class EmailPayload:
    to: str
    template: EmailTemplate
    subject: str
    html: str
    metadata: Optional[dict] = None


async def send_email(payload: EmailPayload) -> dict:
    """Send transactional email via Resend."""
    if not RESEND_API_KEY:
        logger.error("RESEND_API_KEY not configured")
        return {"error": "Email service not configured", "status": "error"}

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                f"{RESEND_API_URL}/emails",
                headers={"Authorization": f"Bearer {RESEND_API_KEY}"},
                json={
                    "from": FROM_EMAIL,
                    "to": payload.to,
                    "subject": payload.subject,
                    "html": payload.html,
                    "metadata": payload.metadata or {},
                },
            )

            result = response.json()
            logger.info(f"Email sent to {payload.to}: {result.get('id')}")
            return {"status": "success", "email_id": result.get("id")}

        except Exception as e:
            logger.error(f"Email send failed: {e}")
            return {"error": str(e), "status": "error"}


async def send_welcome_email(customer_email: str, venture_id: str) -> dict:
    """Send welcome email (Day 0)."""
    payload = EmailPayload(
        to=customer_email,
        template=EmailTemplate.WELCOME,
        subject="Welcome to Ace Construction — Your Account is Ready",
        html=f"""
        <h1>Welcome to Ace Construction!</h1>
        <p>Hi there,</p>
        <p>Your account for <strong>{venture_id}</strong> is now active and ready to use.</p>
        <p><strong>Quick start:</strong></p>
        <ul>
            <li>Log in to your dashboard</li>
            <li>Complete your profile</li>
            <li>Upload your first project</li>
        </ul>
        <p>Questions? Contact support@aceconstruction.com</p>
        """,
        metadata={"venture_id": venture_id, "sequence": "day_0"},
    )
    return await send_email(payload)


async def send_onboarding_checkin(customer_email: str, venture_id: str) -> dict:
    """Send onboarding check-in (Day 2)."""
    payload = EmailPayload(
        to=customer_email,
        template=EmailTemplate.ONBOARDING_CHECKIN,
        subject="How's your setup going? — Ace Construction",
        html=f"""
        <h1>Checking in on your setup</h1>
        <p>Hi there,</p>
        <p>We want to make sure your Ace Construction account is working smoothly for <strong>{venture_id}</strong>.</p>
        <p><strong>Have you:</strong></p>
        <ul>
            <li>✓ Logged in successfully?</li>
            <li>✓ Updated your profile?</li>
            <li>✓ Created your first project?</li>
        </ul>
        <p>If you're stuck, reply to this email or contact support.</p>
        """,
        metadata={"venture_id": venture_id, "sequence": "day_2"},
    )
    return await send_email(payload)


async def send_upsell_followup(customer_email: str, venture_id: str) -> dict:
    """Send upsell follow-up (Day 5)."""
    payload = EmailPayload(
        to=customer_email,
        template=EmailTemplate.UPSELL_FOLLOWUP,
        subject="Level up your Ace Construction workflow",
        html=f"""
        <h1>Ready to level up?</h1>
        <p>Hi there,</p>
        <p>Your <strong>{venture_id}</strong> account is looking great. Here's what you can do next:</p>
        <p><strong>Power features:</strong></p>
        <ul>
            <li>Team collaboration tools</li>
            <li>Advanced analytics and reporting</li>
            <li>Custom integrations</li>
        </ul>
        <p>Schedule a 15-minute walkthrough with our team.</p>
        """,
        metadata={"venture_id": venture_id, "sequence": "day_5"},
    )
    return await send_email(payload)


async def send_payment_receipt(customer_email: str, venture_id: str, amount_cents: int) -> dict:
    """Send payment receipt."""
    amount_usd = amount_cents / 100
    payload = EmailPayload(
        to=customer_email,
        template=EmailTemplate.PAYMENT_RECEIPT,
        subject=f"Payment Receipt — ${amount_usd:.2f}",
        html=f"""
        <h1>Payment Receipt</h1>
        <p>Hi there,</p>
        <p>Your payment has been received and confirmed.</p>
        <p><strong>Details:</strong></p>
        <ul>
            <li>Venture: {venture_id}</li>
            <li>Amount: ${amount_usd:.2f}</li>
            <li>Date: Today</li>
        </ul>
        <p>Thank you for your business!</p>
        """,
        metadata={"venture_id": venture_id, "type": "receipt"},
    )
    return await send_email(payload)


async def send_refund_notice(customer_email: str, venture_id: str, amount_cents: int) -> dict:
    """Send refund notice."""
    amount_usd = amount_cents / 100
    payload = EmailPayload(
        to=customer_email,
        template=EmailTemplate.REFUND_NOTICE,
        subject=f"Refund Confirmation — ${amount_usd:.2f}",
        html=f"""
        <h1>Refund Processed</h1>
        <p>Hi there,</p>
        <p>Your refund has been processed and will appear in your account within 3-5 business days.</p>
        <p><strong>Details:</strong></p>
        <ul>
            <li>Venture: {venture_id}</li>
            <li>Amount: ${amount_usd:.2f}</li>
            <li>Date: Today</li>
        </ul>
        <p>Questions? Contact support@aceconstruction.com</p>
        """,
        metadata={"venture_id": venture_id, "type": "refund"},
    )
    return await send_email(payload)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # Test: send welcome email
    result = asyncio.run(send_welcome_email("test@example.com", "CON-001"))
    print(f"Result: {result}")
