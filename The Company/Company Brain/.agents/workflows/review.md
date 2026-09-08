# Workflow: Review (`/review`)

**Objective:** Conduct structured architectural, security, and quality code reviews before merging or deploying.

## Checklist

1. **Architecture Alignment**:
   - Does this respect layered boundaries?
   - Does it prevent duplicate infrastructure?
2. **Security & Secrets**:
   - Are any credentials, keys, or private endpoints exposed?
   - Are inputs properly validated at boundaries?
3. **No Fake Completion**:
   - Are there any TODOs, stubs, or placeholder mocks?
4. **Testing Evidence**:
   - Are test suites present and passing with recorded output?
