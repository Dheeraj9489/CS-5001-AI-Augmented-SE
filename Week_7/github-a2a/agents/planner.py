"""
Planner A2A Agent (port 8202)

Skills: action_planning, decision_making

Receives the Reviewer's analysis as context and decides the next action:
create_issue, create_pr, or no_action — mirroring the Week 5 Planner but
using an LLM to reason about the evidence.
"""
from agents.base import BaseA2AAgent, Task
from config import PLANNER_PORT


class PlannerAgent(BaseA2AAgent):
    def __init__(self) -> None:
        super().__init__(
            name="Planner",
            description=(
                "Decides the appropriate GitHub action (create issue, "
                "create PR, or no action) based on the code review."
            ),
            skills=["action_planning", "decision_making"],
            port=PLANNER_PORT,
        )

    async def handle(self, task: Task) -> str:
        review_context = (
            f"Code review from the Reviewer agent:\n{task.context}\n\n"
            if task.context else ""
        )

        prompt = (
            "You are a planning agent for a GitHub workflow. Based on the "
            "code review below, decide the best action.\n\n"
            f"{review_context}"
            f"Repository: {task.message}\n\n"
            "Choose exactly ONE action and justify it:\n"
            "- **create_issue** — if the changes need tracking, have quality "
            "issues, or are high-risk and need discussion\n"
            "- **create_pr** — if the changes are a complete feature or bugfix "
            "ready for peer review\n"
            "- **no_action** — if the diff is empty or trivial\n\n"
            "Respond in this format:\n"
            "- **Action**: create_issue / create_pr / no_action\n"
            "- **Justification**: 2-3 sentences explaining why\n"
            "- **Priority**: low / medium / high\n"
            "- **Suggested Labels**: comma-separated GitHub labels\n"
        )
        return await self.llm_call(prompt)
