---
name: testing
description: Governs test execution, validation frameworks, and quality verification across the ecosystem. Use when running unit tests, integration tests, E2E browser tests, or validating code quality before marking tasks complete.
---


[[15-SKILLS/README|15-SKILLS]] | [[16-AGENTS/README|16-AGENTS]] | [[STARTHERE]]

# Testing Skill

This skill enforces the testing mandate defined in Rule 14 of `ANTIGRAVITY.md`.

## Testing Ladder

Execute testing at the highest feasible tier:
1. **Linter / Static Analysis**: `ruff check`, `eslint`, `mypy`, `tsc --noEmit`
2. **Unit Tests**: `pytest`, `npm test`, `cargo test`, `go test`
3. **Integration Tests**: Test API routes and database interactions against mock or isolated containers
4. **End-to-End Tests**: Verify full request/response cycle, browser rendering, or CLI execution (`_CLI/bin/cb test e2e`)
5. **Production Smoke Tests**: Query health checks and verify observability telemetry in Grafana/Langfuse

## Evidence Required

Never state "tests pass" without providing:
- The exact command executed
- Exit code
- Number of passed/failed tests
- Relevant log output snippet
