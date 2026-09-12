[[STARTHERE]] | [[AGENTS.md]] | [[ANTIGRAVITY.md]]

# Workflow: Test (`/test`)

**Objective:** Run comprehensive testing across static analysis, unit, integration, and E2E suites.

## Steps

1. **Static Analysis**:
   - Run type checker and linter on modified files.
2. **Unit Tests**:
   - Run local unit tests for the affected component.
3. **Integration & E2E**:
   - Run integration tests or execute `_CLI/bin/cb test e2e`.
4. **Capture Test Results**:
   - Document commands, exit codes, and output in `TEST_REPORT.md`.
