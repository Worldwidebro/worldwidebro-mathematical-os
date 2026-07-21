# SKILL-OPERATIONS.md — Using 2,000 Skills

**Three-step pattern:** Search → Inspect → Invoke.

---

## Discovery

```bash
# Semantic search
platform skill search "convert PDF"
platform skill search "send SMS"
platform skill search "forecast revenue"

# By category
platform skill list --category "data-processing"
platform skill list --category "communication"
platform skill list --category "finance"

# By MCP
platform skill list --mcp "stripe-api"
platform skill list --mcp "slack-bot"
```

---

## Inspect

```bash
platform skill get <name>
```

Returns: description, input params, output format, dependencies, cost, examples.

---

## Invoke

```bash
# Simple
platform skill invoke generate-uuid

# With params
platform skill invoke resize-image --params '{"input":"./photo.png","width":800,"format":"webp"}'

# With file
platform skill invoke parse-invoice-pdf --params '{"file":"./invoices/batch.pdf"}'

# Piped
cat data.csv | platform skill invoke enrich-lead-data --stdin

# Dry run
platform skill invoke expensive --params '{...}' --dry-run

# Async
platform skill invoke long-task --params '{...}' --async

# Output routing
platform skill invoke generate-report --params '{...}' --output ./report.pdf
```

---

## Chaining (Pipelines)

```bash
# Linear
platform skill chain scrape-website extract-data summarize-document send-email-smtp \
  --input '{"url":"https://..."}' \
  --params-final '{"to":"team@company.com"}'

# Parallel
platform skill parallel generate-copy generate-deck generate-pricing \
  --input '{"product":"CloudSync"}' \
  --output-dir ./launch/
```

---

## Cost Tracking

```bash
platform skill costs --period today
platform skill costs --period this-month --breakdown
platform skill invoke expensive --params '{...}' --estimate-cost
```

---

See COMMANDS.md for complete reference.
