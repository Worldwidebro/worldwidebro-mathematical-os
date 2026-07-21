#!/usr/bin/env python3
"""event_bus.py — Redis Event Bus Daemon for agent coordination."""

import os
import json
import redis
from typing import Callable, Dict, Any

class EventBus:
    def __init__(self, host: str = None, port: int = None, db: int = 0):
        if host is None:
            host = os.environ.get("REDIS_HOST", "100.87.214.70")
        if port is None:
            port = int(os.environ.get("REDIS_PORT", 6380))
        
        # Configure connection pool to prevent connection leaks
        self.pool = redis.ConnectionPool(host=host, port=port, db=db, decode_responses=True)
        self.redis_client = redis.Redis(connection_pool=self.pool)

    def publish(self, channel: str, message: Dict[str, Any]) -> int:
        """Publish a message JSON payload to a Redis channel."""
        payload = json.dumps(message)
        print(f"📡 [EventBus] Publishing to {channel}: {payload}")
        return self.redis_client.publish(channel, payload)

    def listen(self, handlers: Dict[str, Callable[[Dict[str, Any]], None]]):
        """Listen to channels and route incoming messages to handlers."""
        pubsub = self.redis_client.pubsub()
        pubsub.subscribe(*handlers.keys())
        
        print(f"🌀 [EventBus] Listening on channels: {list(handlers.keys())}...")
        for message in pubsub.listen():
            if message['type'] == 'message':
                channel = message['channel']
                data_str = message['data']
                try:
                    payload = json.loads(data_str)
                    print(f"📥 [EventBus] Received event on channel '{channel}'")
                    if channel in handlers:
                        handlers[channel](payload)
                except Exception as e:
                    print(f"❌ [EventBus] Error processing message on channel {channel}: {e}")

if __name__ == '__main__':
    # Dry run test mode
    import sys
    eb = EventBus()
    if '--test' in sys.argv:
        print("Running EventBus self-test...")
        eb.publish('lead_intake', {'test': 'data'})
        print("Self-test completed.")
