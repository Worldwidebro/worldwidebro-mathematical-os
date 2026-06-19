# Venture Handle Management System

**Purpose:** Know which venture you're in, which GitHub handle to use, when to switch contexts.

---

## Quick Start

### 1. Add to Shell Profile

Add this line to **~/.zshrc** or **~/.bash_profile**:

```bash
source /Users/acebless/Documents/.venture-shell-config
```

Then reload:
```bash
source ~/.zshrc
```

### 2. Switch Ventures

```bash
# List all ventures
vl

# Switch to a venture
venture EDU-006

# See current context
vc
```

---

## How It Works

### The Flow

```
You type: venture EDU-006
          ↓
Looks up in VENTURE-HANDLE-MAP.json
          ↓
Finds: handle=@Worldwidebro, email=winnerscirclewcllc@gmail.com
          ↓
Updates git config (if in a repo)
          ↓
Updates .venture-context file
          ↓
Your commits now use correct identity
```

### What Gets Updated

When you run `venture EDU-006`:

**Git Config** (in current repo):
```bash
user.name = @Worldwidebro
user.email = winnerscirclewcllc@gmail.com
```

**.venture-context** (global tracking):
```
CURRENT_VENTURE=EDU-006
HANDLE=@Worldwidebro
EMAIL=winnerscirclewcllc@gmail.com
```

---

## Workflow Example

### Scenario 1: Working on EDU-006

```bash
cd /Users/acebless/Documents/edu-006-repo

venture EDU-006
# ✅ EDU-006: Homeschooling Content AI
# Git config updated

git commit -m "Add first script"
# Commits as @Worldwidebro
```

### Scenario 2: Switching to EDU-001

```bash
cd ~/documents/edu-001-repo

venture EDU-001
# ✅ EDU-001: Youth Entrepreneurship
# Git config updated

git commit -m "Update curriculum"
# Commits as @Worldwidebro (same for all)
```

### Scenario 3: Check Current Context

```bash
vc
# CURRENT_VENTURE=EDU-001
# HANDLE=@Worldwidebro
# EMAIL=winnerscirclewcllc@gmail.com
```

---

## Files in the System

| File | Purpose |
|------|---------|
| **VENTURE-HANDLE-MAP.json** | Source of truth: all venture → handle mappings |
| **.venture-shell-config** | Shell functions and aliases |
| **.venture-context** | Current active venture (key-value file) |
| **VENTURE-HANDLE-GUIDE.md** | This guide |

---

## Adding New Ventures

When you create a new venture, add it to **VENTURE-HANDLE-MAP.json**:

```json
{
  "id": "EDU-041",
  "name": "New Venture Name",
  "sector": "education",
  "repo": "https://github.com/Worldwidebro/edu-041-new-venture",
  "handle": "@Worldwidebro",
  "email": "winnerscirclewcllc@gmail.com",
  "status": "planned"
}
```

Then it's immediately available:
```bash
vl              # Shows new venture
venture EDU-041 # Switches to it
```

---

## Commands Reference

```bash
# Switch to venture
venture EDU-006

# List all ventures
vl

# Show current context
vc

# View venture details
jq '.ventures[] | select(.id == "EDU-006")' VENTURE-HANDLE-MAP.json
```

---

## For Teams/Multiple Handles

If you have multiple GitHub handles:

1. Add them to VENTURE-HANDLE-MAP.json:
```json
{
  "id": "EDU-001",
  "handle": "@Agent-EON",
  "email": "agent-eon@worldwidebro.ai"
}
```

2. Run: `venture EDU-001` (automatically switches to correct handle)

---

## Troubleshooting

**Command not found: `venture`**
- Reload shell: `source ~/.zshrc`
- Check path: `echo $VENTURE_MAP`

**Git config not updating**
- Make sure you're in a git repo: `git status`
- Check if .git folder exists

**Venture not found**
- List available: `vl`
- Check spelling: `venture EDU-006` (not `eduction-006`)

**Want to reset to default**
```bash
git config --global user.name "Worldwidebro"
git config --global user.email "winnerscirclewcllc@gmail.com"
```

