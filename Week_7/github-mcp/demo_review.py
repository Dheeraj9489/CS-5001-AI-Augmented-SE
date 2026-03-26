#!/usr/bin/env python3
"""
GitHub MCP Agent — LLM-driven code review via MCP tools.

The agent connects to the MCP server, uses git tools (git_diff,
get_recent_commits, read_file, list_directory) through the MCP protocol,
and the LLM decides which tools to call to produce a code review.

Usage:
    python demo_review.py /path/to/repo
    python demo_review.py /path/to/repo --base main --verbose
"""
import argparse
import asyncio

from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

from agent import GitHubMCPAgent
from client.session import DEFAULT_URL

console = Console()


async def main(repo_path: str, base: str, verbose: bool, server_url: str) -> None:
    console.print(
        Panel.fit(
            "[bold cyan]GitHub MCP Agent — Code Review[/]",
            subtitle=server_url,
        )
    )

    async with GitHubMCPAgent(server_url) as agent:
        if verbose:
            tools = await agent.list_tools()
            console.print(f"[dim]Tools: {[t['name'] for t in tools]}[/]")

        console.print(f"\n[cyan]Reviewing changes in[/] {repo_path} [cyan]against[/] {base} ...\n")
        report = await agent.review_changes(repo_path, base=base, verbose=verbose)

    console.print(
        Panel(Markdown(report), title="[bold green]Review Report[/]", border_style="green")
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Review git changes via MCP tools (LLM-driven)"
    )
    parser.add_argument("repo_path", help="Path to the git repository to review")
    parser.add_argument("--base", default="main", help="Base branch/ref (default: main)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Print MCP tool calls")
    parser.add_argument(
        "--server-url", default=DEFAULT_URL, metavar="URL",
        help=f"MCP server SSE URL (default: {DEFAULT_URL})",
    )
    args = parser.parse_args()

    asyncio.run(main(args.repo_path, args.base, args.verbose, args.server_url))
