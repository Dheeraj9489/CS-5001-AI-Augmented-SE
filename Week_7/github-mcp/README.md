# GitHub MCP Agent — Code Review via Model Context Protocol

Re-implementation of the **Week 5 GitHub Agent** using **MCP (Model Context Protocol)** for tool access. Instead of calling git/file tools directly in Python, all tools are exposed through an MCP server. The LLM-driven client connects over HTTP/SSE and decides which tools to call at each step.

## Architecture

```
┌─────────────────────┐         HTTP/SSE          ┌─────────────────────┐
│  MCP Client         │ ◄──────────────────────►  │  MCP Server         │
│                     │   tools/list               │  (github-tools)     │
│  ┌───────────────┐  │   tools/call               │                     │
│  │ Ollama LLM    │  │                            │  ┌───────────────┐  │
│  │ (qwen3:0.6b)  │  │                            │  │ git_diff      │  │
│  └──────┬────────┘  │                            │  │ get_commits   │  │
│         │           │                            │  │ read_file     │  │
│  ┌──────▼────────┐  │                            │  │ list_dir      │  │
│  │ Agentic Loop  │  │                            │  └───────────────┘  │
│  └───────────────┘  │                            │                     │
└─────────────────────┘                            └─────────────────────┘
```

## Tools Exposed via MCP

| Tool | Description |
|------|-------------|
| `git_diff` | Get unified diff between two git refs |
| `get_recent_commits` | Fetch recent commit history (hash, author, date, message) |
| `read_file` | Read source file content (capped at 8000 chars) |
| `list_directory` | List files and subdirectories |

## Prerequisites

- **Python 3.10+**
- **Ollama** running locally with a tool-capable model (e.g. `qwen3:0.6b`)
- **git** on PATH

## Setup

```bash
cd Week_7/github-mcp
pip install -r requirements.txt
cp .env.example .env    # edit if needed
```

## Running

**Terminal 1** — Start the MCP server:
```bash
python server/http_app.py
```

**Terminal 2** — Run the review client:
```bash
python demo_review.py /path/to/your/repo
python demo_review.py /path/to/your/repo --base main --verbose
```

## How It Works

1. The **MCP server** registers git/file tools and listens on `http://localhost:8060/sse`
2. The **client** connects, retrieves tool schemas, and sends them to **Ollama** as available functions
3. The **agentic loop** runs: LLM calls `git_diff` → reads the diff → optionally calls `read_file` for deeper context → produces a structured code review
4. The review includes: summary, category, risk level, issues found, and a recommendation (create issue / create PR / no action)
