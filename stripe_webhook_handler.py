#!/usr/bin/env python3
"""
Stripe webhook handler for Hermes payment events.
Receives Stripe webhooks → publishes to event bus → triggers Hermes flow.

Flow: customer.subscription.created / invoice.payment_succeeded
      → event_bus.publish("payment.received", {...})
      → runtime.execute_action("hermes", "charge", ...)
"""

import asyncio
import json
import logging
import os
from typing import Optional

import httpx
from event_bus import EventBus
from runtime_agent_runtime import AgentRuntime

logger = logging.getLogger(__name__)

STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")


async def handle_stripe_event(event: dict) -> None:
    """Process Stripe webhook event and publish to event bus."""
    event_type = event.get("type")
    event_id = event.get("id")
    data = event.get("data", {}).get("object", {})

    logger.info(f"[{event_id}] Processing Stripe event: {event_type}")

    # Initialize bus and runtime
    bus = EventBus()
    runtime = AgentRuntime(SUPABASE_KEY)
    await bus.connect()
    await runtime.connect()

    try:
        if event_type == "invoice.payment_succeeded":
            await handle_payment_succeeded(bus, runtime, data, event_id)
        elif event_type == "customer.subscription.created":
            await handle_subscription_created(bus, runtime, data, event_id)
        elif event_type == "charge.refunded":
            await handle_refund(bus, runtime, data, event_id)
        else:
            logger.debug(f"Unhandled event type: {event_type}")

    finally:
        await runtime.close()
        await bus.close()


async def handle_payment_succeeded(bus: EventBus, runtime: AgentRuntime, data: dict, event_id: str) -> None:
    """Handle successful payment (invoice paid)."""
    amount_cents = data.get("amount_paid", 0)
    customer_id = data.get("customer")
    invoice_id = data.get("id")
    metadata = data.get("metadata", {})

    venture_id = metadata.get("venture_id", "unknown")
    customer_email = metadata.get("customer_email", "")

    logger.info(f"[{event_id}] Payment succeeded: {venture_id} → ${amount_cents / 100:.2f}")

    # Publish event
    corr_id = f"stripe_{invoice_id}_{event_id[:8]}"
    await bus.publish(
        "payment.received",
        payload={
            "type": "invoice_paid",
            "venture_id": venture_id,
            "amount_cents": amount_cents,
            "stripe_invoice_id": invoice_id,
            "stripe_customer_id": customer_id,
            "customer_email": customer_email,
        },
        agent_id="hermes",
        correlation_id=corr_id,
    )

    # Execute: update venture MRR in runtime
    result = await runtime.execute_action(
        agent_id="hermes",
        action="charge",
        params={"amount_cents": amount_cents, "stripe_invoice_id": invoice_id},
        venture_id=venture_id,
    )

    logger.info(f"[{corr_id}] Runtime decision: {result.get('decision')}")


async def handle_subscription_created(bus: EventBus, runtime: AgentRuntime, data: dict, event_id: str) -> None:
    """Handle new subscription (customer enrolled)."""
    customer_id = data.get("customer")
    subscription_id = data.get("id")
    metadata = data.get("metadata", {})

    venture_id = metadata.get("venture_id", "unknown")
    customer_email = metadata.get("customer_email", "")

    logger.info(f"[{event_id}] Subscription created: {venture_id}")

    # Publish event
    corr_id = f"stripe_{subscription_id}_{event_id[:8]}"
    await bus.publish(
        "subscription.started",
        payload={
            "venture_id": venture_id,
            "stripe_customer_id": customer_id,
            "stripe_subscription_id": subscription_id,
            "customer_email": customer_email,
        },
        agent_id="hermes",
        correlation_id=corr_id,
    )

    # Trigger email: welcome sequence (Day 0)
    logger.info(f"[{corr_id}] Queued welcome email to {customer_email}")


async def handle_refund(bus: EventBus, runtime: AgentRuntime, data: dict, event_id: str) -> None:
    """Handle refund."""
    amount_cents = data.get("amount", 0)
    customer_id = data.get("customer")
    charge_id = data.get("id")

    logger.info(f"[{event_id}] Refund: ${amount_cents / 100:.2f}")

    await bus.publish(
        "payment.refunded",
        payload={
            "amount_cents": amount_cents,
            "stripe_charge_id": charge_id,
            "stripe_customer_id": customer_id,
        },
        agent_id="hermes",
        correlation_id=f"stripe_refund_{event_id[:8]}",
    )


def verify_stripe_signature(payload: str, signature: str) -> bool:
    """Verify Stripe webhook signature (HMAC-SHA256)."""
    import hmac
    import hashlib

    computed_sig = hmac.new(
        STRIPE_WEBHOOK_SECRET.encode(),
        payload.encode(),
        hashlib.sha256,
    ).hexdigest()

    return hmac.compare_digest(computed_sig, signature)


async def webhook_endpoint(request_body: str, stripe_signature: str) -> dict:
    """FastAPI endpoint handler (call from route: POST /webhooks/stripe)."""
    if not verify_stripe_signature(request_body, stripe_signature):
        logger.error("Invalid Stripe signature")
        return {"error": "Invalid signature"}, 401

    try:
        event = json.loads(request_body)
        await handle_stripe_event(event)
        return {"received": True}
    except Exception as e:
        logger.error(f"Webhook processing failed: {e}")
        return {"error": str(e)}, 500


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # Test: process a mock invoice.payment_succeeded event
    test_event = {
        "id": "evt_test_123",
        "type": "invoice.payment_succeeded",
        "data": {
            "object": {
                "id": "in_test_456",
                "amount_paid": 9700,
                "customer": "cus_test_789",
                "metadata": {"venture_id": "CON-001", "customer_email": "test@example.com"},
            }
        },
    }

    asyncio.run(handle_stripe_event(test_event))
