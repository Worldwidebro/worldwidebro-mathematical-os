# Event Bus Architecture Design

Design specs for the asynchronous message broker serving IZA OS.

## 1. Topologies
*   **Redis Pub/Sub**: Light real-time message router.
*   **Redis Streams**: Persistent queues with retry logic.

## 2. Event Types
*   `VENTURE_CREATED`
*   `PERMISSIONS_MODIFIED`
*   `COST_LIMIT_EXCEEDED`
