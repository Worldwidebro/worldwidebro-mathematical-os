# Workflow: Implement (`/implement`)

**Objective:** Execute an approved technical plan with disciplined, atomic, test-driven changes.

## Steps

1. **Pre-Change Git Check**:
   ```bash
   git status && git branch && git diff
   ```
2. **Review Implementation Plan**:
   - Check `implementation_plan.md` for user approval and constraints.
3. **Reuse First**:
   - Verify if an existing internal library or component satisfies the need.
4. **Apply Changes**:
   - Implement minimal, modular code adhering to `.agents/rules/coding-standards.md`.
5. **Execute Automated Tests**:
   - Run relevant unit and integration test suites.
6. **Verify Working State**:
   - Confirm observable results before marking task complete.
