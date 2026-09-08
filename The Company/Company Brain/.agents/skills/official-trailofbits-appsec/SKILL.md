---
name: official-trailofbits-appsec
description: Official Trail of Bits Application Security (AppSec) skill covering static analysis (Semgrep, CodeQL), cryptographic primitive auditing, memory safety, dependency supply chain security, and threat modeling.
source: VoltAgent/awesome-agent-skills
origin: Trail of Bits Engineering Standards
---

[[15-SKILLS/README|15-SKILLS]] | [[16-AGENTS/README|16-AGENTS]] | [[STARTHERE]]

# 🛡️ Official Trail of Bits AppSec Skill

> Authoritative application security standards based on Trail of Bits engineering guidelines, continuous SAST scanning, and zero-trust verification.

## 🧠 Core Principles

1. **Defense-in-Depth**: Never rely on a single layer of validation or security controls. Validate at API gateways, application controllers, and database boundaries.
2. **Deterministic SAST**: Integrate automated static analysis (Semgrep, Slither, CodeQL) into every PR gate before merging.
3. **Cryptographic Primitives**: Never invent custom cryptographic routines. Use audited, standard libraries (libsodium, subtle crypto, Web Crypto API).
4. **Supply Chain Defense**: Pin dependencies with exact lockfiles, verify package hashes, and audit for transitive dependency vulnerabilities.

---

## 🛠️ Implementation Patterns

### 1. Automated Semgrep Security Configuration

```yaml
# .github/workflows/security.yml
name: Security Audit Gate
on: [push, pull_request]

jobs:
  semgrep:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run Semgrep SAST
        uses: returntocorp/semgrep-action@v1
        with:
          config: >-
            p/security-audit
            p/secrets
            p/owasp-top-ten
          generateSarif: "1"

      - name: Upload SARIF to GitHub Security Tab
        uses: github/codeql-action/upload-sarif@v3
        if: always()
        with:
          sarif_file: semgrep.sarif
```

---

## 🔒 AppSec Audit Gate Checklist

- [ ] All user-supplied inputs pass through strict runtime schema validation (e.g. Zod, Pydantic).
- [ ] Authentication headers, cookies, and tokens are inspected for strict expiration and Secure/HttpOnly flags.
- [ ] No hardcoded secrets, private keys, or internal bearer tokens exist in source files or commit histories.
