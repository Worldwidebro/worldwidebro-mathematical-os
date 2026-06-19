# GenixBank Financial System — Integration Contracts

This directory contains OpenAPI specifications for all downstream API calls.

## Required Integrations

1. **fin-023-api.yaml** — Portfolio engine (positions, performance, rebalancing)
2. **fin-004-api.yaml** — Treasury system (balances, allocations, forecasts)
3. **fin-026-api.yaml** — Compliance scanner (audit status, violations)

Each spec follows OpenAPI 3.0.0 standard.

## Usage

- Frontend calls these endpoints via environment variables (PORTFOLIO_API_URL, etc.)
- All endpoints require Bearer token authentication
- All responses include standard error envelope: { error, message, timestamp }
