# Testing Patterns

**Analysis Date:** 2026-09-05

## Overview

Company Brain's test structure reflects its mixed nature:

1. **Main codebase (90%):** Obsidian markdown vault + infrastructure configs → no automated tests
2. **CLI (_CLI/bin/cb):** Bash scripts with manual test commands
3. **Python infrastructure (_MCP/, scripts/):** Subprocess calls verified via CLI tests
4. **Fractal subdirectory:** Comprehensive pytest suite (100+ tests) — separate from Company Brain proper; treated as reference only

This document covers testing *within* the Company Brain proper. The fractal folder (`fractal/tests/`) is an external dependency and has its own test conventions.

---

## Test Framework

### No Built-In Test Suite

The Company Brain core (markdown vault + infrastructure layer) **has no automated test runner**. Testing is manual and CLI-driven:

```bash
# CLI test commands available:
_CLI/bin/cb test e2e          # End-to-end infrastructure test
_CLI/bin/cb test models       # List available models
```

These commands verify infrastructure state against live services, not code correctness.

### Why No Automated Tests?

The codebase is primarily:
- **Markdown:** No executable code to test
- **YAML registries:** Validated by wikilink resolution and registry scans (external tools)
- **Bash/Python infrastructure:** Short lifecycle scripts that validate state against running services

Tests would be brittle (tightly coupled to infrastructure state) and low-value (one-shot deployment logic). Infrastructure validation is preferable to unit tests.

---

## CLI-Based Testing

### Test Commands

**Location:** `_CLI/bin/cb`

```bash
# Check all infrastructure components
cb test e2e

# List available models
cb test models
```

### End-to-End Test Pattern

```bash
case "$2" in
  e2e)
    echo "🧪 End-to-End Infrastructure Test"
    echo ""
    echo "Testing all components..."
    curl -s -m 2 http://100.87.214.70:20128/dashboard > /dev/null && \
        echo "  ✅ OmniRoute" || echo "  ❌ OmniRoute"
    curl -s -m 2 http://100.87.214.70:11434/api/tags > /dev/null && \
        echo "  ✅ Ollama" || echo "  ❌ Ollama"
    curl -s -m 2 http://100.87.214.70:7474 > /dev/null && \
        echo "  ✅ Neo4j" || echo "  ❌ Neo4j"
    curl -s -m 2 http://100.87.214.70:6333/health > /dev/null && \
        echo "  ✅ Qdrant" || echo "  ❌ Qdrant"
    echo ""
    echo "✅ E2E test complete"
    ;;
esac
```

**What it tests:**
- OmniRoute AI gateway reachability (port 20128)
- Ollama model runtime (port 11434)
- Neo4j graph database (port 7474)
- Qdrant vector store (port 6333)

**Test result:** List of ✅ / ❌ indicators per service.

### Health Check Pattern

All health checks use curl with timeout:

```bash
curl -s -f -m 2 http://100.87.214.70:PORT/endpoint > /dev/null 2>&1 && \
    echo "  ✅ Service: LIVE (PORT)" || \
    echo "  ❌ Service: DOWN"
```

- `-s` (silent, no progress bar)
- `-f` (fail on HTTP error)
- `-m 2` (2-second timeout, prevents hangs)
- `2>/dev/null` (suppress stderr)

---

## Python Testing Patterns

### MCP Server (`_MCP/fastmcp_server.py`)

The FastMCP server is **not unit-tested**; it's validated through CLI integration tests.

**Validation approach:**

1. **Service startup:** FastMCP server registers correctly with Claude Code
2. **Tool invocation:** `infrastructure_status()` executes and returns valid structure
3. **Subprocess calls:** Each tool shells out to `_CLI/bin/cb` subcommands
4. **Error handling:** Exceptions caught and returned as `{"status": "error", "error": "..."}`

**Manual test (via Claude Code MCP):**

```
User: "Use the infrastructure_status tool to check services"
→ MCP invokes infrastructure_status()
→ Calls subprocess: `_CLI/bin/cb infrastructure status`
→ Returns: {"status": "success", "output": "..."}
```

No pytest needed because:
- Tool merely wraps CLI commands
- CLI is tested by `cb test e2e`
- Integration is validated end-to-end

### Error Handling Test Cases

While not automated, these scenarios should be manually verified:

| Scenario | Expected Behavior | Evidence |
|----------|-------------------|----------|
| Service down | Return `{"status": "error", "error": "..."}` | CLI test shows ❌ |
| Subprocess timeout | Return `{"status": "error", "error": "..."}` | Timeout caught in try/except |
| Missing dependency | Print error + exit(1) | Script startup test |
| Invalid sector ID | Return `{"error": "Sector X not found"}` | MCP call returns error dict |

---

## Fractal Subdirectory Testing (Reference Only)

The `fractal/` folder contains an external project (`plasma-fractal`) with comprehensive tests. These tests do **not** validate Company Brain proper:

**Location:** `fractal/tests/`

**Framework:** pytest with `--doctest-modules`

**Coverage:** 100+ test files across:
- `test_core/` — lifecycle, workflow, state management
- `test_cli/` — CLI parsing, command dispatch
- `test_tui/` — Textual UI interactions
- `test_impl/` — provider implementations (Claude, Codex, Grok, etc.)
- `test_util/` — utility functions

**Usage:** Only referenced when modifying fractal dependencies. Company Brain dev does not run these tests.

**Run fractal tests (if needed):**

```bash
cd fractal
uv run pytest
```

---

## Manual Testing Checklist

Use this checklist when deploying infrastructure changes:

### Pre-Deployment

- [ ] Read the CLAUDE.md infrastructure notes (may flag known issues)
- [ ] Check git status: no uncommitted changes
- [ ] Review the deployment phase documentation

### Deployment

- [ ] Run: `cb infrastructure status` (verify current state)
- [ ] Run: `cb infrastructure deploy --phase 1` (or appropriate phase)
- [ ] Monitor docker logs: `docker --context macstudio logs -f neo4j`
- [ ] Wait for service startup (check logs for "started" messages)

### Post-Deployment

- [ ] Run: `cb test e2e` (verify all services responding)
- [ ] Run: `cb test models` (verify model availability)
- [ ] Verify Neo4j: `curl -s http://100.87.214.70:7474 | head -20`
- [ ] Verify Qdrant: `curl -s http://100.87.214.70:6333/health | jq .`
- [ ] Verify OmniRoute dashboard loads: open http://100.87.214.70:20128/dashboard
- [ ] Try a model inference via OmniRoute (chat tab)

### Rollback (if issues)

- [ ] Note the error (save logs)
- [ ] Run: `docker --context macstudio ps` (list running containers)
- [ ] Run: `docker --context macstudio logs SERVICE_NAME` (diagnose)
- [ ] Stop problematic service: `docker --context macstudio stop SERVICE_NAME`
- [ ] Fix configuration (if applicable)
- [ ] Restart: `docker --context macstudio up -d SERVICE_NAME`
- [ ] Re-run `cb test e2e`

---

## Test Coverage

**Status:** No coverage tracking for Company Brain proper.

Rationale:
- Markdown has no executable code (can't measure coverage)
- Infrastructure scripts are integration-only (full coverage requires live services)
- Single-use deployment logic; coverage would be misleading

Coverage is enforced within the fractal subdirectory (see `fractal/pyproject.toml`), but not at the Company Brain root.

---

## Fixture & Factory Patterns

No fixtures or factories in Company Brain proper. The fractal subdirectory uses pytest fixtures:

**Fractal reference pattern (FYI):**

```python
# fractal/tests/conftest.py
@pytest.fixture(scope='session', autouse=True)
def _isolate_loop_env() -> Iterator[None]:
    """Strip the running loop's exported env for the whole session."""
    # Fixture setup...
    yield
    # Fixture teardown...
```

Company Brain does not need this pattern because tests are CLI-driven, not pytest-driven.

---

## Mocking & Stubbing

**No mocking in Company Brain proper.** Infrastructure is tested against live services.

**Why:**
- E2E validation is more valuable than mocked unit tests
- Services are expected to be running (prerequisite for Company Brain operation)
- CLI tests already verify the happy path and error paths

**Fractal reference (if needed):**

Fractal uses `pytest.mock` and `monkeypatch` for subprocess mocking. Company Brain tests validate against actual infrastructure instead.

---

## Async Testing

**Not applicable.** No async code in Company Brain proper (bash/Python scripts are synchronous).

Fractal uses pytest-asyncio for async test cases (reference only).

---

## Logging & Debugging in Tests

### CLI Debug Output

Add verbose output to CLI tests by capturing stderr:

```bash
# With debug logging
cb infrastructure deploy --phase 1 2>&1 | tee deploy.log

# View full error
docker --context macstudio logs -f SERVICE_NAME
```

### Python Debug Output

In MCP server calls, check returned error dict:

```python
result = infrastructure_status()
if result["status"] == "error":
    print(f"Error: {result['error']}")
    print(f"Stderr: {result.get('stderr', 'N/A')}")
```

### Bash Debug Mode

Enable debugging in shell scripts (temporary):

```bash
set -x  # Print every command before executing
# ... commands to debug ...
set +x  # Turn off debugging
```

---

## Test Types

### Integration Tests (Primary)

Infrastructure deployment and service connectivity verified via:

```bash
cb test e2e      # Tests Neo4j, Qdrant, OmniRoute, Ollama
cb test models   # Tests model availability
```

**Scope:** Full stack end-to-end against live services.

### Manual Smoke Tests

Quick verification after changes:

```bash
# Verify Neo4j responding
cypher-shell -u neo4j -p changeme "RETURN 1;" 

# Verify Qdrant responding
curl -s http://100.87.214.70:6333/health | jq .

# Verify OmniRoute responding
curl -s http://100.87.214.70:20128/health
```

### Data Validation (YAML Registries)

Manually verify registries are valid YAML:

```bash
python3 -c "import yaml; yaml.safe_load(open('_REGISTRIES/ID_REGISTRY.yaml'))" && echo "✅ Valid"
```

No automated linting; manual verification on PR merge.

---

## When to Skip Tests

✅ **It's OK to skip automated tests when:**
- Change is markdown documentation only
- Change is YAML registry data (validate by hand)
- Change is infrastructure config (use `cb test e2e` instead)
- Change is one-shot deployment script (integration tests sufficient)

❌ **Do NOT skip tests when:**
- Changing Python code logic (manually test via MCP)
- Adding new CLI commands (manually test via `cb command`)
- Modifying subprocess calls (verify with `strace` or debug logging)

---

*Testing analysis: 2026-09-05*
