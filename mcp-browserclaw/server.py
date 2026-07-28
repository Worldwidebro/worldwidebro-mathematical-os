#!/usr/bin/env python3
"""
BrowserClaw MCP Server
Exposes BrowserClaw browser control as MCP tools for Claude, Cursor, etc.
"""

import json
import os
import httpx
import asyncio
from typing import Any
from mcp.server import Server
from mcp.types import Tool, TextContent, ToolResult

# Initialize MCP server
server = Server("browserclaw")

# Configuration
BROWSERCLAW_ENDPOINT = os.getenv("BROWSERCLAW_ENDPOINT", "https://api.browseros.com/mcp")
BROWSERCLAW_API_KEY = os.getenv("BROWSERCLAW_API_KEY", "")

# HTTP client
client = httpx.AsyncClient(
    base_url=BROWSERCLAW_ENDPOINT,
    headers={"Authorization": f"Bearer {BROWSERCLAW_API_KEY}"},
    timeout=30.0
)


# ============================================================================
# Tool Definitions
# ============================================================================

TOOLS = [
    Tool(
        name="browserclaw_navigate",
        description="Navigate to a URL in BrowserClaw",
        inputSchema={
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "URL to navigate to"}
            },
            "required": ["url"]
        }
    ),
    Tool(
        name="browserclaw_click",
        description="Click an element on the page by reference or selector",
        inputSchema={
            "type": "object",
            "properties": {
                "ref": {"type": "string", "description": "Element reference (e.g., eN)"},
                "selector": {"type": "string", "description": "CSS selector (if ref not available)"}
            },
            "oneOf": [
                {"required": ["ref"]},
                {"required": ["selector"]}
            ]
        }
    ),
    Tool(
        name="browserclaw_fill",
        description="Fill form fields with values",
        inputSchema={
            "type": "object",
            "properties": {
                "fields": {
                    "type": "object",
                    "description": "Map of field selector/ref to value",
                    "additionalProperties": {"type": "string"}
                }
            },
            "required": ["fields"]
        }
    ),
    Tool(
        name="browserclaw_screenshot",
        description="Capture current page as PNG screenshot",
        inputSchema={
            "type": "object",
            "properties": {}
        }
    ),
    Tool(
        name="browserclaw_read",
        description="Extract current page as markdown + accessibility tree",
        inputSchema={
            "type": "object",
            "properties": {}
        }
    ),
    Tool(
        name="browserclaw_wait",
        description="Wait for element to appear or text to be visible",
        inputSchema={
            "type": "object",
            "properties": {
                "selector": {"type": "string", "description": "CSS selector to wait for"},
                "text": {"type": "string", "description": "Text content to wait for"},
                "timeout": {"type": "integer", "description": "Max wait time in seconds (default 30)"}
            },
            "oneOf": [
                {"required": ["selector"]},
                {"required": ["text"]}
            ]
        }
    ),
    Tool(
        name="browserclaw_evaluate",
        description="Execute JavaScript on the page and return result",
        inputSchema={
            "type": "object",
            "properties": {
                "js": {"type": "string", "description": "JavaScript code to execute"}
            },
            "required": ["js"]
        }
    ),
    Tool(
        name="browserclaw_type",
        description="Type text into focused element",
        inputSchema={
            "type": "object",
            "properties": {
                "text": {"type": "string", "description": "Text to type"}
            },
            "required": ["text"]
        }
    ),
    Tool(
        name="browserclaw_press",
        description="Press keyboard key",
        inputSchema={
            "type": "object",
            "properties": {
                "key": {"type": "string", "description": "Key name (Enter, Tab, Escape, etc.)"}
            },
            "required": ["key"]
        }
    ),
    Tool(
        name="browserclaw_scroll",
        description="Scroll page",
        inputSchema={
            "type": "object",
            "properties": {
                "x": {"type": "integer", "description": "Scroll X pixels"},
                "y": {"type": "integer", "description": "Scroll Y pixels"}
            }
        }
    ),
]


# ============================================================================
# Tool Implementations
# ============================================================================

async def call_browserclaw(action: str, **params) -> dict[str, Any]:
    """Call BrowserClaw API endpoint"""
    try:
        response = await client.post(
            "/action",
            json={"action": action, "params": params}
        )
        response.raise_for_status()
        return response.json()
    except httpx.HTTPError as e:
        return {"error": str(e), "status": "failed"}


@server.call_tool()
async def handle_tool_call(name: str, arguments: dict) -> ToolResult:
    """Handle tool calls from Claude/Cursor/etc"""

    try:
        if name == "browserclaw_navigate":
            result = await call_browserclaw("navigate", url=arguments["url"])

        elif name == "browserclaw_click":
            ref = arguments.get("ref")
            selector = arguments.get("selector")
            result = await call_browserclaw("click", ref=ref, selector=selector)

        elif name == "browserclaw_fill":
            result = await call_browserclaw("fill", fields=arguments["fields"])

        elif name == "browserclaw_screenshot":
            result = await call_browserclaw("screenshot")

        elif name == "browserclaw_read":
            result = await call_browserclaw("read")

        elif name == "browserclaw_wait":
            selector = arguments.get("selector")
            text = arguments.get("text")
            timeout = arguments.get("timeout", 30)
            result = await call_browserclaw("wait", selector=selector, text=text, timeout=timeout)

        elif name == "browserclaw_evaluate":
            result = await call_browserclaw("evaluate", js=arguments["js"])

        elif name == "browserclaw_type":
            result = await call_browserclaw("type", text=arguments["text"])

        elif name == "browserclaw_press":
            result = await call_browserclaw("press", key=arguments["key"])

        elif name == "browserclaw_scroll":
            x = arguments.get("x", 0)
            y = arguments.get("y", 0)
            result = await call_browserclaw("scroll", x=x, y=y)

        else:
            return ToolResult(content=[TextContent(type="text", text=f"Unknown tool: {name}")], is_error=True)

        # Format response
        if "error" in result:
            return ToolResult(
                content=[TextContent(type="text", text=json.dumps(result, indent=2))],
                is_error=True
            )

        return ToolResult(
            content=[TextContent(type="text", text=json.dumps(result, indent=2))],
            is_error=False
        )

    except Exception as e:
        return ToolResult(
            content=[TextContent(type="text", text=f"Error: {str(e)}")],
            is_error=True
        )


@server.list_tools()
async def list_tools() -> list[Tool]:
    """Return available tools"""
    return TOOLS


async def main():
    """Start MCP server"""
    async with server:
        print("🌐 BrowserClaw MCP Server running")
        print(f"📍 Endpoint: {BROWSERCLAW_ENDPOINT}")
        print(f"🔧 Tools: {len(TOOLS)}")
        await server.wait()


if __name__ == "__main__":
    asyncio.run(main())
