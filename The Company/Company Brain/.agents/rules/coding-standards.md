# Coding Standards Rules — Company Brain

1. **No Fake Completion & No Placeholder Architecture**:
   - Never commit `// TODO: implement later`, fake mock APIs, dummy database handlers, or stubbed endpoints unless explicitly requested for a rapid prototype.
   - Code must execute and be verified before marking a task complete.

2. **Type Safety & Contracts**:
   - Python: Use Python 3.11+ type hints, Pydantic v2 models, and strict type checking where applicable.
   - TypeScript/JavaScript: Strict mode enabled, no implicit `any`, define explicit interfaces for API inputs and outputs.
   - Shell scripts: Use `set -euo pipefail` for bash scripts, validate exit codes, and avoid brittle hard-coded paths.

3. **Error Handling & Observability**:
   - Always catch specific exceptions; never use bare `except:` or empty `catch {}`.
   - Include structured contextual logging (service name, correlation ID, entity ID).
   - Route telemetry and traces toward Langfuse (`:3003`) and Grafana (`:3011`).

4. **Testing is Mandatory**:
   - Every new function or endpoint must include automated unit or integration tests.
   - Code without tests is considered incomplete and unverified.
