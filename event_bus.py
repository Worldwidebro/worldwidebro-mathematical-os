#!/usr/bin/env python3
"""
Connector 2: Redis Streams event bus for decoupled service communication.
Spec-compliant message envelope (Agent Communication Contract, section 1.1).

correlation_id: ties all messages in a business flow (for Langfuse tracing)
trace_id: OpenTelemetry span
causation_id: audit trail (links to message that caused this one)
"""

import asyncio
import json
import logging
import uuid
from datetime import datetime
from typing import Awaitable, Callable, Optional

import redis.asyncio as redis

logger = logging.getLogger(__name__)

EventHandler = Callable[[dict], Awaitable[None]]


def generate_id(prefix: str) -> str:
    """Generate ID: {prefix}_20260724_abc123."""
    ts = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    rand = uuid.uuid4().hex[:8]
    return f"{prefix}_{ts}_{rand}"


class EventBus:
    """Redis Streams-based pub/sub for async event handling."""

    def __init__(self, redis_url: str = "redis://localhost:6379"):
        self.redis_url = redis_url
        self.client = None
        self.handlers: dict[str, list[EventHandler]] = {}

    async def connect(self) -> None:
        """Connect to Redis."""
        self.client = await redis.from_url(self.redis_url, decode_responses=True)
        logger.info(f"✓ Connected to Redis at {self.redis_url}")

    async def close(self) -> None:
        """Close Redis connection."""
        if self.client:
            await self.client.close()

    async def publish(
        self,
        topic: str,
        payload: dict,
        agent_id: str = "system",
        correlation_id: Optional[str] = None,
        causation_id: Optional[str] = None,
    ) -> str:
        """Publish event wrapped in spec-compliant envelope."""
        if not self.client:
            raise RuntimeError("EventBus not connected")

        envelope_id = generate_id("env")
        envelope = {
            "envelope_id": envelope_id,
            "schema_version": "1.0",
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "correlation_id": correlation_id or generate_id("corr"),
            "causation_id": causation_id or envelope_id,
            "source": {"agent_id": agent_id, "topic": topic},
            "target": {"mode": "broadcast", "topic": topic},
            "intent": {"type": "event", "name": topic},
            "payload": payload,
            "context": {"trace_id": generate_id("trace"), "ttl_ms": 30000},
            "metadata": {"retry_count": 0},
        }

        msg_id = await self.client.xadd(topic, {"data": json.dumps(envelope)})
        logger.info(f"[{correlation_id}] Published {topic}: {msg_id}")
        return envelope_id

    def subscribe(self, topic: str, handler: EventHandler) -> None:
        """Register a handler for a topic."""
        if topic not in self.handlers:
            self.handlers[topic] = []
        self.handlers[topic].append(handler)
        logger.info(f"Subscribed to {topic}")

    async def listen(self, topic: str, last_id: str = "0") -> None:
        """Listen to a topic and dispatch to registered handlers (extracts payload from envelope)."""
        if not self.client or topic not in self.handlers:
            return

        while True:
            try:
                messages = await self.client.xread({topic: last_id}, block=0)
                if messages:
                    for stream, msg_list in messages:
                        for msg_id, data in msg_list:
                            envelope = json.loads(data["data"])
                            payload = envelope.get("payload", envelope)  # backward compat
                            corr_id = envelope.get("correlation_id", "?")
                            for handler in self.handlers[topic]:
                                await handler(payload)
                            logger.debug(f"[{corr_id}] Handled {topic}")
                            last_id = msg_id
            except Exception as e:
                logger.error(f"Error listening to {topic}: {e}")
                await asyncio.sleep(1)

    async def run_listeners(self, topics: list[str]) -> None:
        """Run all topic listeners concurrently."""
        await asyncio.gather(*[self.listen(topic) for topic in topics])


async def handle_payment(payload: dict) -> None:
    """Handler: Update Neo4j on payment."""
    logger.info(f"[payment] {payload}")


async def handle_vex_sync(payload: dict) -> None:
    """Handler: Regenerate vex portfolio.public.json."""
    logger.info(f"[vex-sync] {payload}")


async def handle_analytics(payload: dict) -> None:
    """Handler: Log to DuckDB."""
    logger.info(f"[analytics] {payload}")


if __name__ == "__main__":
    async def main():
        bus = EventBus()
        await bus.connect()
        bus.subscribe("payment.received", handle_payment)
        bus.subscribe("payment.received", handle_vex_sync)
        bus.subscribe("payment.received", handle_analytics)

        # Publish with spec-compliant envelope
        corr_id = generate_id("corr")
        await bus.publish(
            "payment.received",
            payload={"venture_id": "CON-001", "amount": 97.00},
            agent_id="hermes",
            correlation_id=corr_id,
        )
        print(f"Published with correlation_id: {corr_id}")

        try:
            await bus.run_listeners(["payment.received"])
        finally:
            await bus.close()

    asyncio.run(main())
