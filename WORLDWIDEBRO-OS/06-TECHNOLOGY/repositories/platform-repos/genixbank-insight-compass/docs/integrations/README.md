# GenixBank Insight Compass — Integration Contracts

This directory contains OpenAPI specifications for dashboard data sources.

## Required Integrations

1. **fin-023-metrics-api.yaml** — Portfolio performance metrics
2. **duckdb-analytics.yaml** — Analytical queries and aggregations

## Usage

- Dashboards poll these endpoints every 1-5 minutes
- Results cached in Redis for performance
- Implements circuit breaker for rate limiting
