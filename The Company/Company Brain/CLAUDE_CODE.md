---
type: tool-specification
canonical: false
authority: intelligence-platform-layer
version: 1.0
updated_at: 2026-10-02T23:40:00Z
relates_to: CLAUDE_MASTER_ONTOLOGY
---

# CLAUDE_CODE — Code IDE Integration Layer

**Claude Code transforms Claude into a developer-grade IDE for local + remote codebases.**

**Last updated:** 2026-10-02  
**Status:** Production-ready  
**Gateway:** `claude --help`

---

## Core Layers

### [CLI]
**Command:** `claude [command] [options]`

```bash
# Start a session in current directory
claude

# Run a specific command
claude "implement feature X"

# Set working directory
claude --directory /path/to/project

# Use specific model (via OmniRoute)
claude --model claude-opus-5-5
```

**Available commands:** See `claude --help`

### [TERMINAL]
**Full terminal emulation**
- Real bash/zsh shell
- File system read/write
- Git operations
- Build system invocation
- Process execution

```bash
# Claude executes in current shell context
$ ls -la
$ git status
$ npm test
$ docker ps
```

### [CODEBASE]
**Repository intelligence**
- Automatic context loading
- Dependency tree mapping
- Symbol navigation
- Cross-file references
- Architecture analysis

```bash
# Claude automatically:
- Reads git remote + current branch
- Loads .claude/CLAUDE.md instructions
- Scans for package.json / requirements.txt
- Indexes code symbols via graft/sourcegraph
```

### [FILE_SYSTEM]
**Read/write operations**
- Read files (exact line ranges)
- Edit files (diffs, preserve indentation)
- Create new files
- Delete/move operations
- Watch for changes

**Files Claude CAN access:**
- Current working directory + subdirectories
- Files specified in `CLAUDE.md` allow-list
- Files matching `.claude/rules/*`

**Files Claude CANNOT access:**
- System files outside project
- Secret files (.env, credentials)
- Files in `.gitignore` (unless loaded explicitly)

### [GIT]
**Version control integration**
- Branch creation/switching
- Commit with message
- Pull requests (via GitHub integration)
- Diff visualization
- Merge conflict resolution
- Tag management

```bash
# Claude can:
$ git status
$ git diff
$ git commit -m "message"
$ git push
$ git checkout -b feature/x
```

**Governed by:**
- User's git user config
- Repo branch protection rules
- GitHub credentials via MCP auth
- `.claude/CLAUDE.md` git policies

### [BUILD_SYSTEM]
**Compile + test execution**
- Invoke build tools (npm, cargo, go, etc.)
- Run test suites
- Execute dev servers
- Parse build output
- Suggest fixes for build errors

```bash
# Claude can:
$ npm install && npm test
$ cargo build
$ python -m pytest
$ docker-compose up
```

### [DEBUG]
**Debugging workflows**
- Reproduce bugs
- Add logging
- Step-by-step execution
- Root cause analysis
- Test fixes

### [REFACTOR]
**Code transformation**
- Rename symbols (correctly across files)
- Extract functions
- Consolidate duplicates
- Modernize syntax
- Apply linting fixes

### [REPOSITORY_INTELLIGENCE]
**Deep codebase understanding**
- Symbol definitions + usage
- Call graphs
- Dependency analysis
- Dead code detection
- Import correctness

**Via graft MCP:** Fast symbol lookup (no re-parsing)

**Via sourcegraph MCP:** Deep code search + impact analysis

---

## Tool Ecosystem

### [MCP]
**Any MCP tool is available in Claude Code:**

```yaml
mcp:
  - npx: "@modelcontextprotocol/server-npm"
  - github: "@modelcontextprotocol/server-github"
  - postgres: "@modelcontextprotocol/server-postgres"
  - git: "@modelcontextprotocol/server-git"
```

**Usage:**
```bash
# Claude discovers + uses tools automatically
# Example: GitHub MCP
claude "create a PR with these changes"
# → Uses github MCP under the hood
```

### [SKILLS]
**Procedural automation**

```bash
# Use an installed skill
/skill-name "input"

# Example skills (Company Brain):
/code-review "current PR"
/test-driven-development "feature X"
/gsd-debug "error message"
```

### [PLUGINS]
**Extensible modules**
- Custom MCP servers
- Local automation scripts
- Shell hooks
- IDE integrations

### [SUBAGENTS]
**Delegate to specialists**

```bash
# Claude spawns subagents for:
- Code review (parallel eval agents)
- Build errors (language-specific resolvers)
- Security scanning
- Performance profiling
- Type checking
```

**Agent types:**
- `code-reviewer` — Code review specialist
- `everything-claude-code:build-error-resolver` — Build error fixer
- `everything-claude-code:security-reviewer` — Security auditor
- Plus 40+ more

### [HOOKS]
**Automation triggers**

**Supported events:**
- `pre_tool` — Before any tool executes
- `post_tool` — After tool completes
- `pre_command` — Before shell command
- `post_commit` — After git commit
- `on_error` — When error detected

**Example hook (in `settings.json`):**
```json
{
  "hooks": {
    "post_commit": "npm run lint && npm test"
  }
}
```

---

## Permissions & Governance

### [PERMISSIONS]
**Claude requests approval for:**
- File write/create/delete
- Shell command execution
- Network access
- MCP tool invocation
- Permission-sensitive operations

**Set via `settings.json`:**
```json
{
  "permissions": {
    "allow": ["npm", "git", "docker"],
    "ask": ["python", "bun"],
    "deny": ["rm -rf /"]
  }
}
```

### [CLAUDE_MD]
**Per-project instructions** (highest priority)

**File:** `.claude/CLAUDE.md` (in repo root)

**Contains:**
- Project context
- Coding standards
- Testing requirements
- Git workflow
- Architecture diagrams
- Permission overrides

**Example:**
```markdown
# PROJECT_NAME

## Context
[Project background]

## Standards
- Use TypeScript strict mode
- All functions must have tests
- Commit messages: conventional commits

## Permissions
- Allow: npm, git, docker, postgres
- Ask: external APIs
- Deny: rm -rf /

## Architecture
[System design]
```

### [SANDBOX]
**Isolation + safety**
- File system sandboxing
- Network isolation
- Resource limits
- Permission enforcement
- Rollback capability

---

## Session Management

### [SESSION]
**Conversation context**
- Preserves working directory
- Maintains git state
- Keeps file modifications
- Tracks tool results
- Survives interruptions

**State persisted:**
- Current branch + commits
- File edits (staged + unstaged)
- Tool invocation history
- Error logs

**State NOT persisted:**
- Running processes (stopped on exit)
- Memory/RAM allocations
- Temporary files

---

## Integration with Company Brain

```
[[COMPANY_BRAIN]]
        ↓
[[CLAUDE_CODE]]
        ↓
[[REPOSITORY]]
   (Git + Files)
        ↓
[Reads: .claude/CLAUDE.md]
[Reads: requirements.txt / package.json]
[Reads: .github/workflows/]
[Executes: build + test]
        ↓
[[OMNIROUTE]]
[Routes to appropriate model]
        ↓
[[MCP]]
[GitHub, graft, docker, postgres, etc.]
        ↓
[[EXECUTION]]
[Commit + push + deploy]
```

---

## Common Workflows

### Feature Development
```bash
$ claude "implement login form with validation"
→ Creates branch + files
→ Runs tests
→ Commits with conventional message
→ Suggests PR
```

### Bug Fixing
```bash
$ claude "fix crash when user clicks X"
→ Reproduces bug via test
→ Identifies root cause
→ Implements fix
→ Verifies with test
→ Commits
```

### Code Review
```bash
/code-review
→ Analyzes current PR
→ Comments on issues
→ Suggests improvements
→ Reports findings
```

### Testing
```bash
/tdd-workflow
→ Write test first
→ Run (fails)
→ Implement
→ Run (passes)
→ Refactor
```

---

## Limits & Constraints

| Constraint | Limit | Note |
|-----------|-------|------|
| **Max file size** | 16 MB | Per Edit/Read operation |
| **File operations per session** | Unlimited | Rate-limited by tool quota |
| **Build execution time** | 2 min | Timeout on hanging builds |
| **Process output** | 100K lines | Truncated after limit |
| **Git operations** | 100/session | Per session limit |

---

## Troubleshooting

**"Permission denied"**
- Check `.claude/CLAUDE.md` allow-list
- Run `claude --permissions` to see current policy

**"Build failed"**
- Use `/build-error-resolver` agent
- Check Bash output for root cause
- Verify dependencies installed

**"Git auth failed"**
- Verify GitHub credentials in Bitwarden
- Check token expiration
- Run `gh auth status`

**"Tool not found"**
- Load MCP servers: `claude --mcp list`
- Install missing tools via package manager

---

**Canonical source:** [[CLAUDE_MASTER_ONTOLOGY]]  
**Related:** [[CLAUDE_CODE]] [[MCP]] [[SKILLS]] [[SUBAGENTS]]

