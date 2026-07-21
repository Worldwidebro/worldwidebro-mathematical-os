# OPERATIONS-RUNBOOK.md — Daily Platform Operations

This is what you do every day. Not architecture. Operations.

---

## Morning (5 min)

```bash
platform doctor                              # Everything alive?
platform agent list --status failed          # Any failures overnight?
platform mcp list --status disconnected      # Any disconnected MCPs?
platform infra status                        # Infrastructure healthy?
platform agent retry <job-id>                # Fix failures
platform mcp connect <mcp>                   # Reconnect MCPs
```

---

## Throughout the Day

### Assign Work

```bash
platform agent run <name> --task "..."
platform skill invoke <name> --params '{...}'
platform workflow run <name>
```

### Monitor

```bash
platform agent logs <name> --follow
platform workflow logs <id> --follow
platform infra logs <service> --follow
```

### Respond to Issues

```bash
platform agent pause <name>                  # Agent stuck?
platform agent retry <job-id>                # Agent failed?
platform mcp health                          # MCP down?
platform infra restart <service>             # Service broken?
```

---

## End of Day (2 min)

```bash
platform agent list --status completed --since "today"  # What ran?
platform agent list --status failed --since "today"     # What failed?
platform skill costs --period today                      # Cost check
platform agent costs --period today
```

---

## Weekly (15 min)

```bash
platform doctor --full
platform mcp health --all
platform agent metrics --period 7d
platform knowledge index status
platform infra backup status
platform security scan --scope all
```

---

## Incident: Something Down

```bash
# 1. Diagnose
platform doctor
platform infra status
platform mcp health

# 2. Identify
platform agent list --status failed
platform infra logs <service> --last 100

# 3. Fix
platform infra restart <service>
platform mcp connect --all
platform agent retry --all-failed

# 4. Verify
platform doctor
```

---

## Incident: Agent Misbehaving

```bash
platform agent stop <name>
platform knowledge memory get <name>
platform knowledge memory clear <name>
platform agent run <name> --task "..." --verbose
```

---

## Incident: MCP Bad Data

```bash
platform mcp invoke <name> <tool> --params '{...}' --verbose
platform mcp disconnect <name>
platform mcp connect <name>
platform mcp health <name> --extended
```

---

## Common Recipes

### Process 500 Invoices

```bash
platform skill search "invoice"
platform skill invoke parse-invoice-pdf --params '{"file":"./invoices/batch/"}' --async
```

### Onboard Venture

```bash
platform venture create --template saas-standard --name "venture-new"
platform venture deploy venture-new --env staging
platform venture agents venture-new
```

### MRR Report

```bash
platform agent run finance-analyst --task "Generate MRR report for all active ventures, Q2 2026" --output ./reports/q2.pdf
```

### Email Campaign

```bash
platform skill chain segment-contacts generate-personalized-email send-email-batch track-opens \
  --input '{"segment":"enterprise","campaign":"q3"}'
```

### Deploy Venture

```bash
platform venture deploy venture-alpha --env production
platform venture status venture-alpha
```

### Triage Support

```bash
platform agent run support-triage --task "Triage last 50 tickets, categorize by urgency, assign to team"
```

---

## Daily Checklist

```
□ Morning: platform doctor
□ Morning: platform agent list --status failed
□ Assign: platform agent run ... / platform skill invoke ...
□ Monitor: platform agent logs ... --follow
□ EOD: platform agent list --status failed --since "today"
□ EOD: platform skill costs --period today
```

---

## The Golden Rule

**If you don't know the command, SEARCH.**

```bash
platform skill search "what you want"
platform agent list --capability "what you need"
platform mcp list --category "what system"
```

---

See COMMANDS.md for complete reference. See QUICK-START.md to begin.
