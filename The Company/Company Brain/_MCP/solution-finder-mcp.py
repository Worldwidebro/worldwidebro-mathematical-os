#!/usr/bin/env python3
"""
SOLUTION FINDER MCP SERVER
Exposes solution discovery to Claude Code and agents
2026-09-19
"""

import asyncio
import subprocess
import json
import os
import sys
from mcp.server import Server
from mcp.types import Tool, TextContent, ToolResult

# Initialize MCP server
server = Server("solution-finder")

# Import the JS solution finder (via Node.js subprocess)
async def call_solution_finder(query: str) -> dict:
    """Call the JS SolutionFinder via Node subprocess"""
    try:
        # Create a simple Node script to import and run finder
        script = f"""
const {{ default: SolutionFinder }} = await import('./solution-finder-core.js');
const finder = new SolutionFinder({{ threshold: 0.75 }});
const result = await finder.findSolution('{query.replace("'", "\\'")}');
console.log(JSON.stringify(result));
await finder.close();
"""

        # Write script to temp file
        script_path = '/tmp/sf-query.mjs'
        with open(script_path, 'w') as f:
            f.write(script)

        # Execute via Node
        result = subprocess.run(
            ['node', script_path],
            cwd='/Users/acebless/Documents/The Company/Company Brain/_MCP',
            capture_output=True,
            text=True,
            timeout=5
        )

        if result.returncode != 0:
            return {
                'found': False,
                'error': result.stderr,
                'query': query
            }

        # Parse result
        output_lines = result.stdout.strip().split('\n')
        json_line = [line for line in output_lines if line.startswith('{')]
        if json_line:
            return json.loads(json_line[0])

        return {'found': False, 'query': query}

    except Exception as e:
        return {
            'found': False,
            'error': str(e),
            'query': query
        }

# Define MCP tools

@server.tool()
async def find_solution(query: str) -> ToolResult:
    """
    Find an existing solution in the codebase.

    Searches:
    1. Neo4j knowledge graph (by problem name)
    2. Qdrant vectors (semantic similarity)
    3. graft (code patterns)

    Returns existing solution if found (score > 0.75), otherwise 'not found'.
    """
    result = await call_solution_finder(query)

    if result.get('found'):
        solution = result.get('solution', {})
        return ToolResult(
            content=[TextContent(
                text=f"""✅ Solution Found: {solution.get('name')}

Repository: {solution.get('repo')}
Code Path: {solution.get('codePath')}
Language: {solution.get('language')}
Confidence: {solution.get('confidence', 0):.2%}
Source: {solution.get('source')}

Status: REUSE THIS SOLUTION - Do not re-implement."""
            )],
            is_error=False
        )
    else:
        return ToolResult(
            content=[TextContent(
                text=f"""❌ No Solution Found: "{query}"

Searched in:
- Neo4j knowledge graph
- Qdrant vector database
- graft code patterns

Status: NEW PROBLEM - Execute new solution and register it."""
            )],
            is_error=False
        )

@server.tool()
async def list_solutions() -> ToolResult:
    """List all registered solutions in the knowledge graph."""

    script = """
import neo4j

driver = neo4j.GraphDatabase.driver('bolt://100.87.214.70:7687', auth=('neo4j', 'changeme'))
session = driver.session()

result = session.run('''
  MATCH (s:Solution)-[r:SOLVES]->(p:Problem)
  RETURN s.id, s.name, p.name as problem, s.repo, r.confidence, s.usageCount
  ORDER BY s.usageCount DESC
''')

solutions = []
for record in result:
    solutions.append({
        'id': record['s.id'],
        'name': record['s.name'],
        'problem': record['problem'],
        'repo': record['s.repo'],
        'confidence': record['r.confidence'],
        'usageCount': record['s.usageCount']
    })

print(json.dumps(solutions, indent=2))
session.close()
driver.close()
"""

    try:
        result = subprocess.run(
            ['python3', '-c', script],
            capture_output=True,
            text=True,
            timeout=5
        )

        if result.returncode == 0:
            solutions = json.loads(result.stdout)
            return ToolResult(
                content=[TextContent(text=json.dumps(solutions, indent=2))],
                is_error=False
            )
        else:
            return ToolResult(
                content=[TextContent(text=f"Error: {result.stderr}")],
                is_error=True
            )
    except Exception as e:
        return ToolResult(
            content=[TextContent(text=f"Error: {str(e)}")],
            is_error=True
        )

@server.tool()
async def register_solution(
    solution_id: str,
    name: str,
    description: str,
    code_path: str,
    repo: str,
    language: str,
    solves_problem: str,
    domain: str
) -> ToolResult:
    """Register a new solution after implementing it."""

    script = f"""
import neo4j
from datetime import datetime

driver = neo4j.GraphDatabase.driver('bolt://100.87.214.70:7687', auth=('neo4j', 'changeme'))
session = driver.session()

session.run('''
  MERGE (s:Solution {{id: $id}})
  SET s.name = $name,
      s.description = $description,
      s.codePath = $codePath,
      s.repo = $repo,
      s.language = $language,
      s.created = datetime(),
      s.confidence = 0.90,
      s.usageCount = 0

  MERGE (p:Problem {{name: $problem}})
  SET p.domain = $domain

  MERGE (s)-[r:SOLVES]-(p)
  SET r.confidence = 0.90
''', {{
    'id': '{solution_id}',
    'name': '{name}',
    'description': '{description}',
    'codePath': '{code_path}',
    'repo': '{repo}',
    'language': '{language}',
    'problem': '{solves_problem}',
    'domain': '{domain}'
}})

session.close()
driver.close()
print("Registered: " + '{name}')
"""

    try:
        result = subprocess.run(
            ['python3', '-c', script],
            capture_output=True,
            text=True,
            timeout=5
        )

        if result.returncode == 0:
            return ToolResult(
                content=[TextContent(text=f"✅ Registered: {name}\nID: {solution_id}")],
                is_error=False
            )
        else:
            return ToolResult(
                content=[TextContent(text=f"Error: {result.stderr}")],
                is_error=True
            )
    except Exception as e:
        return ToolResult(
            content=[TextContent(text=f"Error: {str(e)}")],
            is_error=True
        )

if __name__ == "__main__":
    # Run MCP server
    import mcp.server.stdio
    mcp.server.stdio.stdio_server(server).run()
