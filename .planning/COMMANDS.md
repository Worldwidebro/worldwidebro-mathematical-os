# COMMANDS.md — Master Command Reference

**Rule:** If it's not here, it doesn't exist to an operator.

All commands follow: `platform <domain> <verb> <target> [flags]`

---

## AGENT COMMANDS

```bash
platform agent list
platform agent list --status running
platform agent get <name>
platform agent run <name> --task "..."
platform agent run <name> --task "..." --async
platform agent run <name> --task "..." --output ./results.json
platform agent logs <name> --follow
platform agent pause <name>
platform agent resume <name>
platform agent stop <name>
platform agent retry <job-id>
platform agent health
```

---

## SKILL COMMANDS

```bash
platform skill search "email"
platform skill list --category "communication"
platform skill list --mcp "stripe-api"
platform skill get <name>
platform skill invoke <name> --params '{...}'
platform skill invoke <name> --params '{...}' --dry-run
platform skill invoke <name> --params '{...}' --async
platform skill chain skill1 skill2 skill3 --input ./data.json
platform skill costs --period today
```

---

## MCP COMMANDS

```bash
platform mcp list
platform mcp list --status connected
platform mcp get <name>
platform mcp tools <name>
platform mcp invoke <name> <tool> --params '{...}'
platform mcp connect <name>
platform mcp disconnect <name>
platform mcp health
```

---

## VENTURE COMMANDS

```bash
platform venture list
platform venture get <name>
platform venture create --template saas-standard --name "new-venture"
platform venture deploy <name> --env production
platform venture status <name>
platform venture agents <name>
```

---

## INFRASTRUCTURE COMMANDS

```bash
platform infra status
platform infra health
platform infra logs <service> --follow
platform infra restart <service>
platform infra backup run --target all
```

---

## KNOWLEDGE COMMANDS

```bash
platform knowledge search "how does billing work"
platform knowledge index status
platform knowledge memory get <agent>
platform knowledge memory clear <agent>
```

---

## WORKFLOW COMMANDS

```bash
platform workflow list
platform workflow run <name>
platform workflow status <id>
platform workflow logs <id> --follow
```

---

## REGISTRY COMMANDS

```bash
platform registry agents
platform registry skills
platform registry mcps
platform registry prompts
platform registry models
```

---

## GLOBAL FLAGS

| Flag | Effect |
|------|--------|
| `--json` | JSON output |
| `--verbose` | Debug info |
| `--dry-run` | Simulate only |
| `--async` | Background execution |
| `--follow` | Stream output |
| `--timeout <dur>` | Max execution time |
| `--help` | Show help |

---

## QUICK REFERENCE

```
FIND      platform skill search "what"
          platform agent list --capability "what"
          platform mcp list --category "what"

USE       platform skill invoke <name> --params '{...}'
          platform agent run <name> --task "..."
          platform mcp invoke <name> <tool> --params '{...}'

MONITOR   platform agent logs <name> --follow
          platform workflow logs <id> --follow

CHECK     platform doctor
          platform agent health
          platform mcp health

GET HELP  platform <anything> --help
```

See QUICK-START.md to get started in 5 minutes.
