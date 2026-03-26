"""
Reviewer A2A Agent (port 8201)

Skills: diff_analysis, risk_assessment, issue_detection

Given a git repository path, this agent runs git diff, analyses the
changes, and produces a structured review with category, risk level,
and issues found — mirroring the Week 5 Reviewer agent but LLM-powered.
"""
import subprocess
from pathlib import Path

from agents.base import BaseA2AAgent, Task
from config import REVIEWER_PORT

MAX_DIFF_CHARS = 6_000


class ReviewerAgent(BaseA2AAgent):
    def __init__(self) -> None:
        super().__init__(
            name="Reviewer",
            description=(
                "Analyses git diffs: categorises changes, assesses risk, "
                "and detects code quality issues."
            ),
            skills=["diff_analysis", "risk_assessment", "issue_detection"],
            port=REVIEWER_PORT,
        )

    def _get_diff(self, repo_path: str, base: str = "main") -> str:
        try:
            result = subprocess.run(
                ["git", "diff", f"{base}...HEAD"],
                capture_output=True, text=True, timeout=15,
                cwd=repo_path,
            )
            diff = result.stdout.strip()
            if not diff:
                result = subprocess.run(
                    ["git", "diff", base, "HEAD"],
                    capture_output=True, text=True, timeout=15,
                    cwd=repo_path,
                )
                diff = result.stdout.strip()
            return diff[:MAX_DIFF_CHARS] if diff else ""
        except Exception as exc:
            return f"Error getting diff: {exc}"

    async def handle(self, task: Task) -> str:
        repo_path = task.message.strip()
        base = task.context if task.context else "main"

        p = Path(repo_path)
        if not p.is_dir():
            return f"Repository path not found: {repo_path}"

        diff = self._get_diff(repo_path, base)
        if not diff:
            return "No changes found in the diff. Nothing to review."

        prompt = (
            "You are a code reviewer. Analyse the following git diff and provide "
            "a structured review.\n\n"
            f"Git diff:\n```\n{diff}\n```\n\n"
            "Provide your review in this exact format:\n"
            "- **Category**: bugfix / feature / refactor / test / chore\n"
            "- **Risk Level**: low / medium / high — with a brief justification\n"
            "- **Files Changed**: list the files modified\n"
            "- **Summary**: 2-3 sentences on what changed\n"
            "- **Issues Found**: list any bugs, style problems, bare excepts, "
            "debug prints, TODOs, or security concerns. Say 'None' if clean.\n"
        )
        return await self.llm_call(prompt)
