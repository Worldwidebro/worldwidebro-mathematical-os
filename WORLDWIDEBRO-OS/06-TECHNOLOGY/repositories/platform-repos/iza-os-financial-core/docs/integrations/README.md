# IZA OS Financial Core — Integration Contracts

This directory contains OpenAPI specifications for shared services.

## Provided Integrations

1. **advisory-api.yaml** — Forecasting, compliance rules, risk assessment
2. **registry-api.yaml** — Venture reference data (read-only)

These services are called by all FIN ventures.

## Usage

- All endpoints require Bearer token (API key from venture-hub)
- Returns standardized JSON response structure
- Implements exponential backoff for rate limiting
