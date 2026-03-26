"""
A2A Coordinator

Discovers available A2A agents, then orchestrates the GitHub agent
pipeline by delegating tasks via HTTP:

  Reviewer  ->  Planner (with review context)  ->  Writer (with plan context)

Discovery:
  Each agent exposes GET /.well-known/agent.json  ->  Agent Card
  The coordinator fetches these to learn what agents are available.

Delegation:
  POST /tasks/send  with  {task_id, message, context}
  The agent returns      {task_id, status, output, agent}
"""
from __future__ import annotations

import uuid

import httpx
from rich.console import Console

from config import REVIEWER_PORT, PLANNER_PORT, WRITER_PORT

console = Console()

KNOWN_ENDPOINTS = [
    f"http://localhost:{REVIEWER_PORT}",
    f"http://localhost:{PLANNER_PORT}",
    f"http://localhost:{WRITER_PORT}",
]


class A2ACoordinator:
    def __init__(self) -> None:
        self.agents: list[dict] = []

    def discover(self) -> list[dict]:
        """Fetch Agent Cards from all known endpoints."""
        self.agents = []
        for endpoint in KNOWN_ENDPOINTS:
            try:
                resp = httpx.get(
                    f"{endpoint}/.well-known/agent.json", timeout=5
                )
                resp.raise_for_status()
                card = resp.json()
                card["endpoint"] = endpoint
                self.agents.append(card)
                console.print(
                    f"  [green]\u2713[/] [bold]{card['name']}[/]"
                    f"  skills={card['skills']}"
                    f"  \u2192 {endpoint}"
                )
            except Exception as exc:
                console.print(f"  [red]\u2717[/] {endpoint}: {exc}")
        return self.agents

    def send_task(
        self, endpoint: str, message: str, context: str = ""
    ) -> dict:
        """Send a task to an A2A agent and return the result dict."""
        payload = {
            "task_id": str(uuid.uuid4())[:8],
            "message": message,
            "context": context,
        }
        resp = httpx.post(
            f"{endpoint}/tasks/send", json=payload, timeout=120
        )
        resp.raise_for_status()
        return resp.json()

    def _find_agent(self, name: str) -> dict | None:
        return next((a for a in self.agents if a["name"] == name), None)

    def run_pipeline(self, repo_path: str, base: str = "main") -> dict[str, str]:
        """
        Sequential GitHub agent pipeline:
          1. Reviewer  — analyses the diff
          2. Planner   — decides action (receives review as context)
          3. Writer    — drafts issue/PR (receives review + plan as context)
        """
        results: dict[str, str] = {}

        reviewer = self._find_agent("Reviewer")
        planner = self._find_agent("Planner")
        writer = self._find_agent("Writer")

        if reviewer:
            console.print("\n[cyan]\u2192 Reviewer[/]  analysing diff ...")
            r = self.send_task(reviewer["endpoint"], message=repo_path, context=base)
            results["review"] = r["output"]
            console.print(f"[green]  \u2713 Review complete[/]  (status: {r['status']})")

        if planner:
            console.print("[cyan]\u2192 Planner[/]  deciding action ...")
            context = results.get("review", "")
            r = self.send_task(planner["endpoint"], message=repo_path, context=context)
            results["plan"] = r["output"]
            console.print(f"[green]  \u2713 Plan complete[/]  (status: {r['status']})")

        if writer:
            console.print("[cyan]\u2192 Writer[/]  drafting content ...")
            context = (
                f"=== REVIEW ===\n{results.get('review', '')}\n\n"
                f"=== PLAN ===\n{results.get('plan', '')}"
            )
            r = self.send_task(writer["endpoint"], message=repo_path, context=context)
            results["draft"] = r["output"]
            console.print(f"[green]  \u2713 Draft complete[/]  (status: {r['status']})")

        return results
