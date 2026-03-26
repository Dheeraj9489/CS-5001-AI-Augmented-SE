"""
Writer A2A Agent (port 8203)

Skills: content_drafting, github_formatting

Receives the Planner's decision and the Reviewer's analysis as context,
then drafts a GitHub issue or PR body — mirroring the Week 5 Writer agent
but using an LLM for natural language generation.
"""
from agents.base import BaseA2AAgent, Task
from config import WRITER_PORT


class WriterAgent(BaseA2AAgent):
    def __init__(self) -> None:
        super().__init__(
            name="Writer",
            description=(
                "Drafts GitHub issue or PR content with title, body, "
                "evidence, and test plan based on the review and plan."
            ),
            skills=["content_drafting", "github_formatting"],
            port=WRITER_PORT,
        )

    async def handle(self, task: Task) -> str:
        prior_context = (
            f"Prior analysis from Reviewer and Planner agents:\n{task.context}\n\n"
            if task.context else ""
        )

        prompt = (
            "You are a technical writer for GitHub. Based on the code review "
            "and planning decision below, draft a GitHub issue or pull request.\n\n"
            f"{prior_context}"
            f"Repository: {task.message}\n\n"
            "Write the draft in this format:\n\n"
            "## Title\n"
            "A concise, descriptive title with a category emoji "
            "(e.g. 🐛 for bugfix, ✨ for feature, ♻️ for refactor)\n\n"
            "## Body\n"
            "Include these sections:\n"
            "1. **Summary** — what changed and why\n"
            "2. **Classification** — category, risk level, action type in a table\n"
            "3. **Files Changed** — list of modified files\n"
            "4. **Issues Found** — any problems detected\n"
            "5. **Test Plan** — checkboxes for testing steps\n\n"
            "Make the draft professional and ready to post on GitHub."
        )
        return await self.llm_call(prompt)
