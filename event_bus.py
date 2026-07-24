#!/usr/bin/env python3
"""
Connector 2: Redis Streams event bus for decoupled service communication.
Pattern: Stripe payment → event → subscribers (Neo4j, vex, analytics).
"""

import asyncio
import json
import logging
from typing import Awaitable, Callable

import redis.asyncio as redis

logger = logging.getLogger(__name__)

EventHandler = Callable[[dict], Awaitable[None]]


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

    async def publish(self, topic: str, payload: dict) -> None:
        """Publish event to a topic."""
        if not self.client:
            raise RuntimeError("EventBus not connected")
        msg_id = await self.client.xadd(topic, {"data": json.dumps(payload)})
        logger.info(f"Published {topic}: {msg_id}")

    def subscribe(self, topic: str, handler: EventHandler) -> None:
        """Register a handler for a topic."""
        if topic not in self.handlers:
            self.handlers[topic] = []
        self.handlers[topic].append(handler)
        logger.info(f"Subscribed to {topic}")

    async def listen(self, topic: str, last_id: str = "0") -> None:
        """Listen to a topic and dispatch to registered handlers."""
        if not self.client or topic not in self.handlers:
            return

        while True:
            try:
                messages = await self.client.xread({topic: last_id}, block=0)
                if messages:
                    for stream, msg_list in messages:
                        for msg_id, data in msg_list:
                            payload = json.loads(data["data"])
                            for handler in self.handlers[topic]:
                                await handler(payload)
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
        try:
            await bus.run_listeners(["payment.received"])
        finally:
            await bus.close()

    asyncio.run(main())
