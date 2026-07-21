# MCP-OPERATIONS.md — Using MCPs

Every external system (database, API, cloud) is an MCP. Register once, use everywhere.

---

## Discovery

```bash
platform mcp list
platform mcp list --status connected
platform mcp list --category "database"
platform mcp list --category "api"
platform mcp search "stripe"
```

---

## Connection

```bash
platform mcp connect <name>
platform mcp disconnect <name>
platform mcp connect --all
platform mcp health
platform mcp health <name>
```

Health output:
```
  ✓ postgres-primary   connected   8ms
  ✓ stripe-api         connected   45ms
  ✗ legacy-crm         disconnected (3h ago)
```

---

## Usage

### See Tools

```bash
platform mcp tools postgres-primary
```

Output:
```
postgres-primary (v3.2.1) — 6 tools
  query     Execute SELECT
  execute   Execute INSERT/UPDATE/DELETE
  schema    Get table schema
  tables    List tables
  migrate   Run migration
  backup    Trigger backup
```

### Invoke Tool

```bash
# Query database
platform mcp invoke postgres-primary query --params '{"sql":"SELECT * FROM ventures WHERE status = '\''active'\''"}'

# Send Slack
platform mcp invoke slack-bot send_message --params '{"channel":"#alerts","text":"⚠️ Error rate high"}'

# Write file
platform mcp invoke filesystem-local write_file --params '{"path":"/data/report.md","content":"# Report"}'

# Create GitHub PR
platform mcp invoke github-api create_pr --params '{"repo":"venture-alpha","title":"feat: billing","branch":"feature/billing"}'

# Create Stripe charge
platform mcp invoke stripe-api create_charge --params '{"amount":9999,"currency":"usd","customer_id":"cus_abc"}'
```

---

## Register New MCP

```bash
platform mcp register --config ./mcp.yaml
platform mcp register --name "notion-api" --transport sse --url "https://mcp.internal/notion" --auth-header "Authorization: Bearer ${TOKEN}"
```

---

## Permissions

```bash
platform mcp grant stripe-api --agent finance-reconciler --tools "create_charge,refund"
platform mcp revoke stripe-api --agent marketing-writer
```

---

## Troubleshooting

```bash
platform mcp connect <name> --verbose
platform mcp health <name> --extended
platform doctor --mcp
```

---

See COMMANDS.md for complete reference.
