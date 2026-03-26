"""
MCP Server — tool registration and request handling.

Exposes git/GitHub tools (git_diff, get_recent_commits, read_file,
list_directory) so any MCP-compatible client can use them.
"""
from mcp.server import Server
from mcp.types import TextContent, Tool

from server import handlers
from server.schemas import TOOLS

app = Server("github-tools-server")


@app.list_tools()
async def list_tools() -> list[Tool]:
    return [Tool(**t) for t in TOOLS]


@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    try:
        fn = getattr(handlers, name)
        result = fn(**arguments)
        return [TextContent(type="text", text=result)]
    except AttributeError:
        return [TextContent(type="text", text=f"Unknown tool: {name}")]
    except Exception as exc:
        return [TextContent(type="text", text=f"ERROR: {exc}")]
