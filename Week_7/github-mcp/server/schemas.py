"""
Tool schemas — git and GitHub tools for the MCP server.

Each tool mirrors a capability from the Week 5 GitHub Agent (git_diff,
read_file, list_directory) plus get_recent_commits for richer context.
"""

TOOLS = [
    {
        "name": "git_diff",
        "description": (
            "Get the git diff between two refs in a repository. "
            "Returns the unified diff text showing all changes."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "repo_path": {
                    "type": "string",
                    "description": "Absolute path to the git repository",
                },
                "base": {
                    "type": "string",
                    "description": "Base ref (branch, tag, or commit). Default: 'main'",
                },
                "head": {
                    "type": "string",
                    "description": "Head ref. Default: 'HEAD'",
                },
            },
            "required": ["repo_path"],
        },
    },
    {
        "name": "get_recent_commits",
        "description": (
            "Get the most recent git commits from a repository. "
            "Returns commit hash, author, date, and message for each."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "repo_path": {
                    "type": "string",
                    "description": "Absolute path to the git repository",
                },
                "count": {
                    "type": "integer",
                    "description": "Number of recent commits to return. Default: 5",
                },
            },
            "required": ["repo_path"],
        },
    },
    {
        "name": "read_file",
        "description": "Read the content of a source file (capped at 8000 chars).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "Absolute or relative file path",
                },
            },
            "required": ["path"],
        },
    },
    {
        "name": "list_directory",
        "description": "List files and subdirectories inside a directory.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "Directory path",
                },
            },
            "required": ["path"],
        },
    },
]
