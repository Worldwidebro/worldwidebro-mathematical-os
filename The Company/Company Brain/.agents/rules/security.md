# Security & Zero-Trust Rules — Company Brain

1. **Zero Exposure of Secrets**:
   - Never write API keys, database passwords, private keys, or tokens into code, markdown, comments, git commits, logs, or test fixtures.
   - Always reference environment variables (e.g. `${GITHUB_TOKEN}`, `${NEO4J_PASSWORD}`) or approved secret management systems.

2. **Input Validation**:
   - Treat all external input (HTTP parameters, webhook payloads, file uploads, LLM outputs) as untrusted.
   - Validate and sanitize all schemas strictly at system boundaries using Pydantic, Zod, or type-safe schemas.

3. **High-Risk Operations & Human Approval**:
   - Any destructive action (deleting production data, dropping database tables, changing security rules, destructive git pushes, financial/revenue mutations) requires explicit human review: `PLAN → PREVIEW → APPROVAL → EXECUTION`.

4. **External Code Auditing**:
   - Never import external/starred repositories without verifying licenses (MIT, Apache 2.0, BSD vs GPL/AGPL restrictions) and reviewing dependency supply chains for known vulnerabilities.
