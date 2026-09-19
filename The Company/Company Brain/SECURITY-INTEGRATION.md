# SECURITY-INTEGRATION.md — Zero-Trust Security & Permission Governance

**Authority:** Security & Compliance Control Plane (CP-028)  
**Standard:** Zero-Trust Architecture (NIST SP 800-207)  
**Status:** `AUDITED_SECURE`  

---

## 1. Zero-Trust Security Architecture

```text
       ┌────────────────────────────────────────────────────────┐
       │                   AUTHENTICATED MESH                   │
       │     WireGuard-Encrypted Tailscale Network Mesh         │
       │    Mac Studio (100.87.214.70) ↔ MacBook Air (100.121)   │
       └───────────────────────────┬────────────────────────────┘
                                   │
               ┌───────────────────┴───────────────────┐
               │                                       │
               ▼                                       ▼
  Strict Localhost / Mesh Only                Zero Public Port Exposure
  - Neo4j Bolt (:7687)                        - All Docker containers bind
  - Qdrant REST (:6333)                         to Tailscale IP or 127.0.0.1
  - OmniRoute Router (:20128)                 - No public WAN port forwarding
  - Ollama Inference (:11434)                 - 100% encrypted in transit
```

---

## 2. Secrets & Credential Hygiene

1. **Rule of Clean Repositories:**
   - No raw API keys, bearer tokens, or database passwords may ever be committed to git repositories.
   - All credentials reside in `.env` or local system configurations (`~/.gemini/config/mcp_config.json`, `~/.omniroute/`).
2. **Key Masking & Redaction:**
   - OmniRoute and FastMCP automatically mask tokens in request/response headers (`Bearer sk-30c3...`).
   - Logging modules redact `authorization`, `x-api-key`, and `cookie` headers in diagnostic logs.

---

## 3. MCP & Tool Sandboxing

1. **Read-Only by Default:**
   - All database inspection and knowledge retrieval tools default to read-only queries.
2. **Gated Mutating Operations:**
   - Operations that write or alter filesystem state (`write_to_file`, `replace_file_content`, `run_command` with modifying shell scripts) require explicit confirmation when operating outside verified developer workflows.
3. **Execution Isolation:**
   - Antigravity sandbox isolates unprivileged commands from the root filesystem and blocks unauthorized outbound network traffic unless explicitly elevated (`BypassSandbox: true`).
