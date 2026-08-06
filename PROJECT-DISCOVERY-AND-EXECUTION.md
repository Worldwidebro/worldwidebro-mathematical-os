---
name: PROJECT-DISCOVERY-AND-EXECUTION
title: Project Discovery & Execution Framework
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# Project Discovery & Execution Framework
## Integrating Mac Studio, Claude, Composio & Paperclip

---

## Overview

This framework enables:
1. **Auto-discovery** of project files across Mac Studio and mounted drives
2. **Claude Code integration** for understanding and processing project context
3. **Composio integration** for executing business logic via connected tools
4. **Paperclip framework** for systematic deployment and automation
5. **Business logic execution** through agents and workflows

---

## Part 1: Mac Studio Project Discovery

### System Architecture

```
Mac Studio Resources
├── Local Filesystem (/Users/acebless/)
│   ├── Documents/
│   ├── Code/
│   ├── Projects/
│   └── Data/
├── Mounted Drives
│   ├── External SSD
│   ├── Network Shares
│   └── Cloud Mounts
└── Claude Code Context
    ├── Project Memory
    ├── CLAUDE.md Files
    └── Git Repositories
```

### Discovery Commands

```bash
# Find all project roots
find /Users/acebless -name "CLAUDE.md" -o -name "package.json" -o -name "pyproject.toml" | head -20

# List mounted drives
mount | grep "/Volumes"

# Find large project directories
du -sh /Users/acebless/* | sort -hr | head -10

# List git repositories
find /Users/acebless -maxdepth 3 -name ".git" -type d

# Search for specific project files
find /Users/acebless -name "*venture*" -o -name "*operating*" -o -name "*architecture*"
```

### Key Project Locations to Index

```
/Users/acebless/Documents/
├── ai-venture-studio-template/      # Venture templates
├── autonomous-venture-studio/        # Autonomous execution
├── iza-os-rag-system/              # Knowledge graph system
├── mission-control/                 # Central coordination
├── make-workflows/                  # Automation workflows
├── composio/                        # Composio SDK
└── .claude/                         # Claude Code config
    ├── CLAUDE.md                   # Global instructions
    ├── projects/                   # Per-project context
    └── memory/                     # Persistent memory
```

---

## Part 2: Claude Code Integration

### Loading Project Context

#### Step 1: Read CLAUDE.md Files
```bash
# Global instructions
cat /Users/acebless/.claude/CLAUDE.md

# Project-specific instructions
find /Users/acebless -name "CLAUDE.md" -exec head -30 {} \;
```

#### Step 2: Load Project Memory
```bash
# Access persistent memory
ls -la /Users/acebless/.claude/projects/*/memory/

# Read memory index
cat /Users/acebless/.claude/projects/-Users-acebless-Documents/memory/MEMORY.md
```

#### Step 3: Check Git Context
```bash
# Current branch and uncommitted changes
cd /Users/acebless/Documents && git status

# Recent commits for context
git log --oneline -10

# Project structure overview
find . -maxdepth 2 -type d | grep -v "\.git" | sort
```

### Using Claude Capabilities

```typescript
// In your code/Claude Code session:
// 1. Load project memory: /remember projects/-Users-acebless-Documents
// 2. Check current files: git status
// 3. Use tools (Read/Edit/Bash) to understand project
// 4. Claude maintains full context of your venture ecosystem
```

---

## Part 3: Composio Tool Execution

### Connect Business Logic to Tools

```bash
# 1. View connected tools
composio connected

# 2. Connect GitHub for venture repos
composio connect github

# 3. Connect Slack for notifications
composio connect slack

# 4. Connect Linear/Jira for task tracking
composio connect linear
composio connect jira

# 5. Connect Gmail for contact outreach
composio connect gmail
```

### Execute Business Logic with Composio

```python
from composio import Composio

composio = Composio(api_key="ak_nCUr47rLtuThE2_5XTqr")

# Example: Create GitHub repo for new venture
result = await composio.tools.execute('GITHUB_CREATE_REPO', {
    userId: 'venture-admin',
    arguments: {
        repo_name: 'venture-acme-studio',
        description: 'ACME Venture - AI-powered studio',
        private: False
    }
})

# Example: Send Slack notification
result = await composio.tools.execute('SLACK_SEND_MESSAGE', {
    userId: 'venture-admin',
    arguments: {
        channel: '#venture-updates',
        text: f'New venture created: {venture.name}'
    }
})
```

---

## Part 4: Paperclip Framework Integration

### Paperclip Deployment Structure

```
paperclip-deployment/
├── config/
│   ├── ventures.yaml          # Venture definitions
│   ├── workflows.yaml         # Execution workflows
│   └── integrations.yaml      # Tool integrations
├── templates/
│   ├── venture-bootstrap.yml  # New venture setup
│   ├── outreach-flow.yml      # Contact outreach
│   └── deal-pipeline.yml      # Deal tracking
└── execution/
    ├── deploy.py              # Deployment engine
    ├── monitor.py             # Execution monitor
    └── rollback.py            # Error handling
```

### Using Paperclip for Automation

```bash
# 1. Deploy venture infrastructure
python3 paperclip_deployment_plan.py --venture acme-construction

# 2. Initialize venture workspace
composio connect github
composio connect slack
composio connect linear

# 3. Execute venture setup workflow
python3 deploy.py --config ventures.yaml --venture acme-construction

# 4. Monitor execution
python3 monitor.py --venture acme-construction --watch
```

---

## Part 5: End-to-End Execution Flow

### Complete Workflow Example

```python
#!/usr/bin/env python3
"""
Integrated Project Discovery & Execution
Uses: Claude Code + Composio + Paperclip + Mac Studio Resources
"""

import os
import json
from pathlib import Path
from composio import Composio

class ProjectExecutionFramework:
    def __init__(self):
        self.composio = Composio(api_key=os.getenv('COMPOSIO_API_KEY'))
        self.workspace = '/Users/acebless/Documents'
        self.projects = self._discover_projects()
    
    def _discover_projects(self):
        """Discover all projects across Mac Studio"""
        projects = {}
        
        # Find CLAUDE.md files as project indicators
        for claude_file in Path(self.workspace).rglob('CLAUDE.md'):
            project_root = claude_file.parent
            project_name = project_root.name
            
            projects[project_name] = {
                'path': str(project_root),
                'claude_config': str(claude_file),
                'git': self._get_git_info(project_root),
                'files': self._scan_project_files(project_root)
            }
        
        return projects
    
    def _get_git_info(self, project_root):
        """Extract git information"""
        git_dir = project_root / '.git'
        if git_dir.exists():
            return {
                'exists': True,
                'branch': self._get_current_branch(project_root)
            }
        return {'exists': False}
    
    def _get_current_branch(self, project_root):
        """Get current git branch"""
        import subprocess
        try:
            result = subprocess.run(
                ['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
                cwd=project_root,
                capture_output=True,
                text=True
            )
            return result.stdout.strip()
        except:
            return 'unknown'
    
    def _scan_project_files(self, project_root):
        """Scan project structure"""
        files = {
            'src': [],
            'tests': [],
            'docs': [],
            'config': [],
            'other': []
        }
        
        for item in (project_root / 'src').glob('*') if (project_root / 'src').exists() else []:
            files['src'].append(item.name)
        
        return files
    
    def load_project_context(self, project_name):
        """Load full project context for Claude Code"""
        if project_name not in self.projects:
            raise ValueError(f"Project {project_name} not found")
        
        project = self.projects[project_name]
        context = {
            'project_name': project_name,
            'path': project['path'],
            'git_branch': project['git'].get('branch'),
            'files': project['files'],
            'memory': self._load_memory(project_name)
        }
        
        return context
    
    def _load_memory(self, project_name):
        """Load Claude Code memory for project"""
        memory_file = Path(self.workspace) / '.claude' / 'projects' / f'-{project_name}' / 'memory' / 'MEMORY.md'
        if memory_file.exists():
            return memory_file.read_text()
        return None
    
    async def execute_business_logic(self, venture_name, action):
        """Execute business logic via Composio"""
        
        if action == 'create_repo':
            result = await self.composio.tools.execute('GITHUB_CREATE_REPO', {
                'userId': 'venture-admin',
                'arguments': {
                    'repo_name': f'venture-{venture_name}',
                    'description': f'{venture_name} - AI-powered venture',
                    'private': False
                }
            })
            return result
        
        elif action == 'notify_team':
            result = await self.composio.tools.execute('SLACK_SEND_MESSAGE', {
                'userId': 'venture-admin',
                'arguments': {
                    'channel': '#venture-operations',
                    'text': f'🚀 New venture: {venture_name}'
                }
            })
            return result
        
        elif action == 'create_tracking':
            result = await self.composio.tools.execute('LINEAR_CREATE_ISSUE', {
                'userId': 'venture-admin',
                'arguments': {
                    'title': f'Setup: {venture_name}',
                    'description': f'Initialize {venture_name} venture operations',
                    'priority': 1
                }
            })
            return result
        
        return None
    
    def generate_report(self):
        """Generate discovery report"""
        return {
            'total_projects': len(self.projects),
            'projects': list(self.projects.keys()),
            'workspace': self.workspace,
            'mounted_drives': self._get_mounted_drives()
        }
    
    def _get_mounted_drives(self):
        """List mounted drives"""
        import subprocess
        result = subprocess.run(['mount'], capture_output=True, text=True)
        drives = [line for line in result.stdout.split('\n') if '/Volumes' in line]
        return drives

# Usage
if __name__ == '__main__':
    framework = ProjectExecutionFramework()
    
    # 1. Discover projects
    print("📍 Discovered Projects:")
    report = framework.generate_report()
    print(json.dumps(report, indent=2))
    
    # 2. Load specific project context
    if report['projects']:
        first_project = report['projects'][0]
        context = framework.load_project_context(first_project)
        print(f"\n📂 Project Context Loaded: {first_project}")
        print(json.dumps({
            'project': context['project_name'],
            'path': context['path'],
            'git_branch': context['git_branch']
        }, indent=2))
    
    # 3. Execute business logic (example)
    # result = await framework.execute_business_logic('acme-studio', 'create_repo')
```

---

## Part 6: Usage Instructions

### Quick Start

```bash
# 1. Load your project context in Claude Code
cd /Users/acebless/Documents
/remember projects/-Users-acebless-Documents

# 2. Check available tools
composio connected

# 3. Connect new tools if needed
composio connect github
composio connect slack

# 4. Run discovery script
python3 -c "
from PROJECT_DISCOVERY_AND_EXECUTION import ProjectExecutionFramework
fw = ProjectExecutionFramework()
print(fw.generate_report())
"

# 5. Execute business logic via agents
# Claude Code can now orchestrate across:
# - Local files and git repos
# - Connected Composio tools
# - Paperclip workflows
# - Mac Studio resources
```

### Integration Points

| Component | Purpose | Command |
|-----------|---------|---------|
| **Claude Code** | Project understanding & code generation | `/remember projects/-Users-acebless-Documents` |
| **Composio** | Tool execution (GitHub, Slack, etc.) | `composio connected` |
| **Paperclip** | Deployment & workflow automation | `python3 deploy.py` |
| **Mac Studio** | Resource access & file system | `find /Users/acebless -name "*.md"` |
| **Git** | Version control & context | `git status` |

---

## Workspace Configuration

Your workspace is ready with:
- ✅ Composio API Key: `ak_nCUr47rLtuThE2_5XTqr`
- ✅ Workspace: `winnerscirclewcllc_workspace`
- ✅ Project: `winnerscirclewcllc_workspace_first_project`
- ✅ Local CLI: `~/.composio/composio`
- ✅ Project Memory: `/Users/acebless/.claude/projects/*/memory/`

---

## Next Steps

1. **Load full project context** in Claude Code using memory system
2. **Connect required tools** via Composio CLI
3. **Define venture templates** in Paperclip
4. **Execute business logic** through integrated agents
5. **Track completion** via Composio dashboard

---

## Resources

- 📊 Composio Dashboard: https://dashboard.composio.dev/winnerscirclewcllc_workspace/
- 📚 Documentation: https://docs.composio.dev
- 🔧 Local CLI: `~/.composio/composio`
- 💾 Project Memory: `/Users/acebless/.claude/projects/*/memory/MEMORY.md`
