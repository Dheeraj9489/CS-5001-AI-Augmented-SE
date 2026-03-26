"""
GitHubMCPAgent — orchestrator

Composes MCPSession, AgenticLoop, and OllamaClient.
Connects to the running MCP server via HTTP/SSE and uses
the LLM-driven agentic loop to review git changes.

Usage:
    async with GitHubMCPAgent() as agent:
        report = await agent.review_changes("/path/to/repo")
"""
from __future__ import annotations

from client.loop import AgenticLoop
from client.session import MCPSession, DEFAULT_URL
from llm import OllamaClient


class GitHubMCPAgent:
    def __init__(self, url: str = DEFAULT_URL) -> None:
        self._session = MCPSession(url)
        self._loop: AgenticLoop | None = None

    async def review_changes(
        self, repo_path: str, base: str = "main", verbose: bool = False
    ) -> str:
        task = (
            f"You are a GitHub code-review agent. Analyse the git changes in "
            f"the repository at: {repo_path}\n\n"
            f"Use the available tools to:\n"
            f"1. Run git_diff with repo_path='{repo_path}' and base='{base}' to get the diff\n"
            f"2. Run get_recent_commits with repo_path='{repo_path}' for context\n"
            f"3. Optionally read specific changed files for deeper understanding\n\n"
            f"Then provide a structured review:\n"
            f"- **Summary**: What changed and why (2-3 sentences)\n"
            f"- **Category**: bugfix / feature / refactor / test / chore\n"
            f"- **Risk Level**: low / medium / high with justification\n"
            f"- **Issues Found**: Any bugs, style problems, or concerns\n"
            f"- **Recommendation**: create_issue / create_pr / no_action with reason"
        )
        return await self._loop.run(task, verbose=verbose)

    async def list_tools(self) -> list[dict]:
        return await self._session.list_tools()

    async def __aenter__(self) -> "GitHubMCPAgent":
        await self._session.__aenter__()
        self._loop = AgenticLoop(self._session, OllamaClient())
        return self

    async def __aexit__(self, *args) -> None:
        await self._session.__aexit__(*args)
