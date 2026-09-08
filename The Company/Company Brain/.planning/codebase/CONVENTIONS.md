# Coding Conventions

**Analysis Date:** 2026-09-05

## Overview

Company Brain mixes three distinct codebase layers: Obsidian markdown vault (90% of code), Python scripts (MCP servers, utilities), and bash CLI. Each layer has distinct conventions documented here. The overarching principle is **clarity through consistency** — all code should read as if one person wrote it within its own layer.

---

## Markdown & Wikilink Conventions (Obsidian Vault)

### Frontmatter Format

All markdown files use YAML frontmatter with these standard fields:

```yaml
---
id: "TYPE-000001"              # Machine ID (required for registries)
title: "Human Readable Title"  # Required
aliases: ['slug', 'Alternative Name']  # Alternative reference names (optional)
tags: [category, taxonomy, cross-cutting-concern]  # Categorical tags
status: "ACTIVE|PLANNING|RETIRED"  # Explicit lifecycle state
last_verified: "YYYY-MM-DD"    # Last audit date
---
```

**Domain Examples:**
- `SECTORS/SEC-001-beauty-wellness.md`: Uses `sector_id`, `opco`, `status` frontmatter
- `CLAUDE.md` (infrastructure): Uses `Updated: YYYY-MM-DD` + `Authority: CP-027` pattern in title
- README files: Minimal frontmatter, focus on content

**Rule:** If a file contains structured data (sectors, ventures, capabilities), include frontmatter ID. If it's ephemeral (meeting notes, session summaries), frontmatter is optional.

### Wikilink Usage

Internal cross-references use double-bracket wiki syntax: `[[target]]` or `[[target|display text]]`

**Patterns:**

- **Domain links:** `[[00-CONSTITUTION]]` (folder), `[[16-AGENTS]]` (domain)
- **Control plane links:** `[[Infrastructure Control Plane]]`, `[[Agent Control Plane]]`
- **Registry links:** `[[_REGISTRIES/ventures-by-sector.yaml]]`, `[[[_REGISTRIES/control-points]]]`
- **File references:** `[[CLAUDE.md]]` or `[[CLAUDEMD.md|Infrastructure Config]]`
- **Aliased links:** `[[00-CONSTITUTION/SECTOR-TAXONOMY-MASTER|SECTOR-TAXONOMY-MASTER.md]]`

**Navigation breadcrumb pattern (top of files):**
```markdown
[[STARTHERE]] | [[REALITY]] | [[00-CONSTITUTION]] | [[INDEX-DOMAINS-COMPLETE]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]
```

This creates a horizontal menu in Obsidian graph view for rapid navigation across the system.

### Section Structure

Every domain README follows this template:

```markdown
# Domain Name

**Scope:** One-line purpose  
**Authority:** Control plane responsible  
**Status:** 🟢/🟡/❌

## Overview
What this domain owns and why it exists.

## Contents
- Subdomain 1: Purpose
- Subdomain 2: Purpose

## Key Files
- `_REGISTRIES/file.yaml`: Description
- `path/to/README.md`: Description

## Connected Domains
- [[upstream-domain]] → downstream (relationship direction)
- [[downstream-domain]] ← upstream

## Control Points
See [[_REGISTRIES/control-points]] for X operations in this domain.

## Status
🟡 In progress
---
Last updated: YYYY-MM-DD
```

### Comment & Annotation Patterns

**Status markers:**
- 🟢 Active / Grounded in Code Reality
- 🟡 In progress / Partial
- ❌ Blocked / Not started
- ✅ Complete (use sparingly, reserved for truly final state)

**Emphasis:**
- **Bold:** Important terms, file paths, config values
- `Code backticks`: File paths, IDs, command examples, API names
- _Italic_: Rarely used; prefer bold

**Tables for structured data:**

```markdown
| Column | Purpose | Notes |
|--------|---------|-------|
| Data | Summary | Details |
```

Use tables for registries, status matrices, decision tables. Avoid excessive nesting; if a table grows beyond 5 columns, consider splitting into multiple tables or a YAML registry.

---

## ID Naming Conventions

**Format:** `TYPE-000001` (human-readable) + ULID (machine ID, internal)

All system entities use a unified ID taxonomy from `_REGISTRIES/ID_REGISTRY.yaml`. When creating new entities, always assign a human-readable ID:

### Standard Prefixes

| Prefix | Scope | Range | Example |
|--------|-------|-------|---------|
| **ORG** | Organization/Holding | ORG-000001 to ORG-000999 | ORG-000001 (Worldwidebro Holdings) |
| **VEN** | Venture | VEN-000001 to VEN-999999 | VEN-000047 (specific venture) |
| **REP** | Repository | REP-000001 to REP-999999 | REP-000142 (GitHub repo) |
| **CAP** | Capability | CAP-000001 to CAP-999999 | CAP-001 (API Design) |
| **SKL** | Skill | SKL-000001 to SKL-999999 | SKL-042 (Claude Code skill) |
| **AGT** | Agent | AGT-000001 to AGT-999999 | AGT-006 (Routing agent) |
| **MOD** | Model | MOD-000001 to MOD-999999 | MOD-001 (qwen2.5-coder:14b) |
| **MCP** | MCP Server | MCP-000001 to MCP-999999 | MCP-OMNIROUTE (OmniRoute gateway) |
| **CBP** | Company Brain Point (control) | CBP-000001 to CBP-000500 | CBP-027 (Infrastructure CP) |

**Rule:** Use the prefix systematically. A venture should be `VEN-*`, never an arbitrary short name. A registry entry should cite the full ID in headers and frontmatter.

### Sector Codes

Sectors use short prefixes: `SEC-001` through `SEC-035`. Ventures within a sector use sector prefix + number:
- `CON-001` to `CON-999` (Construction)
- `LT-001` to `LT-999` (Logistics)
- `FIN-001` to `FIN-999` (Finance)
- `RE-001` to `RE-999` (Real Estate)

**Where IDs appear:**
- YAML frontmatter: `id: "CAP-001"`
- File paths (when appropriate): `14-CAPABILITIES/CAP-001-api-design.md`
- Code comments and docstrings: Reference as `CAP-001` or full `CAP-001 (API Design)`
- Python objects: Store as `cap_id: "CAP-001"` (string, not enum)

---

## Python Code Conventions

### File Structure & Shebang

Every executable Python file starts with:

```python
#!/usr/bin/env python3
"""
Module docstring - one line summary.

Authority: CP-027 (if infrastructure-related)
Framework: FastMCP, Typer, etc. (if applicable)
"""

import subprocess
import json
import os
import sys
from pathlib import Path
from typing import Optional, Dict, List

# Imports grouped: stdlib → third-party → local
```

### Docstrings & Comments

**Module docstring:** Always present, one-line summary at top.

```python
"""Company Brain FastMCP Server - exposes infrastructure as MCP tools."""
```

**Function docstring:** Present for all public functions, present for complex private functions.

```python
def infrastructure_status() -> dict:
    """Check Company Brain infrastructure health (OmniRoute, Neo4j, Qdrant, Ollama)"""
    # Implementation
```

**Inline comments:** Use `#` for non-obvious logic. Comment **why**, not what:

```python
# Try importing fastmcp, provide installation instructions if missing
try:
    from fastmcp import FastMCP
except ImportError:
    print("❌ FastMCP not installed")
    sys.exit(1)
```

Good: Explains the rationale (conditional import with user-facing error).  
Bad: `from fastmcp import FastMCP  # Import FastMCP` (obvious from code).

### Type Hints

Always use type hints for function parameters and return types:

```python
def get_sector_info(sector_id: str) -> dict:
    """Get information about a specific sector"""
    pass

def infrastructure_deploy(phase: str = "all") -> dict:
    """Deploy phases - defaults to 'all'"""
    pass
```

Use `Optional[T]` for nullable returns:

```python
def find_venture(venture_id: str) -> Optional[Dict]:
    """Returns venture data or None if not found"""
    pass
```

### Error Handling

**Pattern:** Catch exceptions at boundaries (external calls, file I/O); return structured responses.

```python
try:
    result = subprocess.run(
        cmd,
        cwd=COMPANY_BRAIN_DIR,
        capture_output=True,
        text=True,
        timeout=10
    )
    return {
        "status": "success" if result.returncode == 0 else "error",
        "output": result.stdout,
        "error": result.stderr if result.returncode != 0 else None
    }
except Exception as e:
    return {"status": "error", "error": str(e)}
```

**Rule:** Never let exceptions bubble up silently. Return a structured error dict with `status: "error"` and an error message. Subprocess calls always include `timeout` to prevent hangs.

### Path Handling

Use `pathlib.Path` for all file operations:

```python
from pathlib import Path

COMPANY_BRAIN_DIR = Path(__file__).parent.parent
config_file = COMPANY_BRAIN_DIR / "_CLI" / "schema.yaml"

if not config_file.exists():
    return {"error": f"Config file not found: {config_file}"}
```

Never use string concatenation for paths.

### Subprocess Calls

Always use these patterns:

```python
result = subprocess.run(
    ["command", "arg1", "arg2"],      # List, not string
    cwd=COMPANY_BRAIN_DIR,            # Explicit working directory
    capture_output=True,              # Always capture for inspection
    text=True,                        # String output, not bytes
    timeout=10                        # Always set timeout
)

# Check return code, never assume success
if result.returncode == 0:
    return {"status": "success", "output": result.stdout}
else:
    return {"status": "error", "error": result.stderr}
```

---

## Bash CLI Conventions

### Script Structure (`_CLI/bin/cb`)

```bash
#!/bin/bash
# Company Brain CLI - short description
# Authority: CP-027

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
SCHEMA="$PROJECT_ROOT/_CLI/schema.yaml"

case "$1" in
  infrastructure)
    case "$2" in
      status)
        echo "🔍 Infrastructure Status Report"
        # Implementation
        ;;
      deploy)
        PHASE="${4:-all}"
        ENV="${6:-production}"
        # Implementation
        ;;
    esac
    ;;
  *)
    echo "Usage: cb [command] [subcommand] [options]"
    exit 1
    ;;
esac
```

**Patterns:**
- `set -euo pipefail` (not used here but recommended for safety scripts)
- Case statement for command dispatch (not getopts)
- Uppercase `$VARIABLE_NAMES` for script-level state
- Numbered args: `$1`, `$2`, etc. with defaults: `"${4:-all}"`
- Comments before logical blocks

### Error Handling & Output

**Exit codes:** 0 for success, non-zero for failure.

```bash
# Check command availability
if command -v cypher-shell &> /dev/null; then
    cypher-shell -u neo4j -p changeme "MATCH (n) RETURN count(n);"
else
    echo "  ⚠️  cypher-shell not found - install: brew install neo4j-client"
    exit 1
fi
```

**Output formatting:**
- Emoji status indicators: 🔍 (action), ✅ (success), ❌ (error), ⚠️ (warning), 🧪 (test)
- Echo sections with blank lines for readability
- Structured output for piping (JSON when appropriate)

```bash
echo ""
echo "Phase 1️⃣: Database Deployment"
echo "  • Neo4j Graph Database (7687/7474)"
echo "  • Qdrant Vector Store (6333)"
```

### Health Checks

Use `curl` with timeout and silent flags:

```bash
curl -s -f -m 2 http://100.87.214.70:20128/dashboard > /dev/null 2>&1 && \
    echo "  ✅ OmniRoute: LIVE (20128)" || \
    echo "  ❌ OmniRoute: DOWN / AUTH REQUIRED"
```

Pattern: `-s` (silent), `-f` (fail on HTTP error), `-m 2` (2-second timeout).

---

## YAML Registry Conventions

All registries in `_REGISTRIES/` follow this structure:

```yaml
# Company Brain [Entity] Registry

# Global standards
# Format: TYPE-000001 (human-readable) + ULID (machine)

prefixes:
  TYPE:
    description: "What this type represents"
    range: "TYPE-000001 to TYPE-999999"
    example: "TYPE-000042"

entities:
  TYPE-000001:
    name: "Entity Name"
    description: "What it does"
    status: "active|planning|retired"
    properties:
      key: value
```

**Rules:**
- Comments at top explain the format
- YAML structure mirrors the ID taxonomy
- Keys are lowercase_with_underscores
- Dates in `YYYY-MM-DD` format
- Status is one of: `active`, `planning`, `retired`, `archived`

---

## Data Type Conventions

### Status Values

System-wide status vocabulary (do not invent new ones):
- 🟢 `ACTIVE` — operational, grounded in code
- 🟡 `IN_PROGRESS` — partial, work ongoing
- ❌ `BLOCKED` — cannot proceed (why in adjacent note)
- `RETIRED` — no longer used but history preserved

### Timestamp Format

All dates in ISO 8601: `YYYY-MM-DD` or `YYYY-MM-DDTHH:MM:SSZ` for datetime.

Use `last_verified: "2026-09-05"` for manual audits.

---

## Naming Patterns Summary

| What | Pattern | Example |
|------|---------|---------|
| **Variables (Python)** | snake_case | `company_brain_dir`, `ventures_file` |
| **Constants (Python)** | UPPER_SNAKE_CASE | `MAX_COST`, `DEFAULT_PHASE` |
| **Functions (Python/Bash)** | snake_case or kebab-case | `infrastructure_status()`, `wire-ontology` |
| **Files (Code)** | snake_case.py / kebab-case.sh | `fastmcp_server.py`, `create-domain-readmes.sh` |
| **Files (Documentation)** | UPPER_CASE.md or Title-Case.md | `CONVENTIONS.md`, `README.md` |
| **Folders** | kebab-case or domain numbers | `_MCP`, `14-CAPABILITIES`, `_REGISTRIES` |
| **IDs (System)** | TYPE-000001 | `VEN-000047`, `CAP-001` |
| **URLs/Endpoints** | kebab-case | `/api/models/test`, `/health` |

---

## Cross-Cutting Patterns

### Logging & Debugging

No built-in logger; use print (Python) or echo (Bash) with emoji status:

```python
# Python
print("❌ FastMCP not installed")
print("✅ Infrastructure deployed")
return {"status": "success", "output": result.stdout}

# Bash
echo "🔍 Infrastructure Status Report"
echo "  ✅ OmniRoute: LIVE (20128)"
echo "  ❌ Neo4j: DOWN"
```

### Authority & Attribution

Every infrastructure file includes authority attribution:

```markdown
**Authority:** Infrastructure Control Plane (CP-027)
```

In code:

```python
"""
Company Brain FastMCP Server
Authority: Infrastructure Control Plane (CP-027)
"""
```

This signals responsibility and makes it clear who to contact for changes.

---

*Convention analysis: 2026-09-05*
