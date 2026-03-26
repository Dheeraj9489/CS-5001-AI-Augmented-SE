#!/usr/bin/env python3
"""
A2A GitHub Agent Pipeline — coordinator entry point.

Discovers the Reviewer, Planner, and Writer agents via their Agent Cards,
then runs the sequential pipeline:
  1. Reviewer  -> reads the diff, produces a structured code review
  2. Planner   -> receives the review, decides action (issue/PR/no_action)
  3. Writer    -> receives review + plan, drafts GitHub issue/PR content

All three agents must be running before calling this script:
    python agents/run_reviewer.py   # Terminal 1
    python agents/run_planner.py    # Terminal 2
    python agents/run_writer.py     # Terminal 3

Usage:
    python demo_pipeline.py /path/to/repo
    python demo_pipeline.py /path/to/repo --base main
"""
import argparse
import sys

from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

from coordinator import A2ACoordinator

console = Console()


def main(repo_path: str, base: str) -> None:
    console.print(
        Panel.fit(
            "[bold magenta]A2A GitHub Agent Pipeline[/]",
            subtitle="Agent-to-Agent protocol",
        )
    )

    coord = A2ACoordinator()

    console.print("\n[bold]Discovering agents ...[/]")
    agents = coord.discover()

    if not agents:
        console.print(
            "\n[red]No agents found.[/] Start them first:\n"
            "  [dim]python agents/run_reviewer.py[/]\n"
            "  [dim]python agents/run_planner.py[/]\n"
            "  [dim]python agents/run_writer.py[/]"
        )
        sys.exit(1)

    console.print(f"\n[bold]Running pipeline on[/] {repo_path} [bold]against[/] {base}\n")
    results = coord.run_pipeline(repo_path, base=base)

    if "review" in results:
        console.print(
            Panel(
                Markdown(results["review"]),
                title="[bold blue]Reviewer Agent[/]",
                border_style="blue",
            )
        )
    if "plan" in results:
        console.print(
            Panel(
                Markdown(results["plan"]),
                title="[bold yellow]Planner Agent[/]",
                border_style="yellow",
            )
        )
    if "draft" in results:
        console.print(
            Panel(
                Markdown(results["draft"]),
                title="[bold green]Writer Agent[/]",
                border_style="green",
            )
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run A2A GitHub agent pipeline on a repository"
    )
    parser.add_argument("repo_path", help="Path to the git repository")
    parser.add_argument("--base", default="main", help="Base branch/ref (default: main)")
    args = parser.parse_args()

    main(args.repo_path, args.base)
