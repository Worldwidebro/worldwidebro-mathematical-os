# Docker Compose Updates Guide

Details docker-compose changes needed to support Redis pubsub and monitoring.

## 1. Service Additions
Add Redis to your `docker-compose.yml`:

```yaml
services:
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    restart: always
```

## 2. Verification
Ensure port `6379` is open by running `redis-cli ping` on your host.
