# AGENT-OPERATIONS.md — Running Agents

---

## Morning Check

```bash
platform agent health
platform agent list --status failed --since "12h ago"
```

---

## Assign Work

```bash
# Simple
platform agent run code-reviewer-01 --task "Review all open PRs"

# With file input
platform agent run data-enrichment --task "Enrich leads" --input ./leads.csv --output ./results.json

# Async
platform agent run long-task --task "..." --async

# Scheduled (daily at 9am)
platform agent schedule code-reviewer --task "Review overnight PRs" --cron "0 9 * * *"
```

---

## Monitor

```bash
platform agent logs <name> --follow
platform agent logs <job-id> --follow
platform agent status <job-id>
```

---

## Intervene

```bash
platform agent pause <name>
platform agent resume <name>
platform agent stop <name> --force
platform agent retry <job-id>
```

---

## Agent Memory

```bash
platform knowledge memory get <agent>
platform knowledge memory clear <agent>
```

---

## Permissions

```bash
platform agent grant <agent> --mcp stripe-api --tools "create_charge,refund"
platform agent revoke <agent> --mcp stripe-api
```

---

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| Won't start | `platform agent health <name>` |
| Stuck | `platform agent logs <name> --last 50` |
| Failed | `platform agent retry <job-id>` |
| Slow | `platform agent metrics <name>` |
| Hallucinating | `platform knowledge memory clear <name>` |

---

See OPERATIONS-RUNBOOK.md for daily workflow.
