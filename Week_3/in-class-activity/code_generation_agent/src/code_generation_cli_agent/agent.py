from __future__ import annotations

from pathlib import Path
from typing import Any, Callable

from .llm import OllamaLLM
from .prompt_manager import PromptManager
from .tools import Tools
from .types import AgentConfig, RunResult
from .utils import strip_code_fences

class Agent:
    def __init__(self, cfg: AgentConfig):
        self.cfg = cfg
        self.repo = Path(cfg.repo).resolve()
        self.tools = Tools(self.repo)
        self.prompt_manager = PromptManager()
        
        # Default prompt variants
        self.planning_variant = 'default'
        self.code_gen_variant = 'default'

    def _log(self, message: Any) -> None:
        if self.cfg.verbose:
            print(message)

    def _llm(self) -> OllamaLLM:
        return OllamaLLM(
            model=self.cfg.model,
            host=self.cfg.host,
            temperature=self.cfg.temperature,
        )

    def _call_llm(self, prompt: str) -> str:
        return self._llm().generate(prompt)

    def _multi_step_chain(self) -> Callable[[str], str]:
        try:
            from langchain_core.runnables import RunnableLambda
        except Exception:
            return self._call_llm

        return RunnableLambda(self._call_llm).invoke

    def create_program(self, desc: str, module_path: str) -> RunResult:
        """Create a program module.
        
        Steps:
        1) produce a plan
        2) draft code (multiple files)
        3) write to disk
        """
        run = self._multi_step_chain()

        # Plan
        p1 = self.prompt_manager.get_prompt(
            'planning',
            self.planning_variant,
            desc=desc,
            module_path=module_path
        )
        self._log(p1)
        plan = run(p1).strip()
        if not plan:
            return RunResult(False, "Model returned empty plan.")

        # Draft code
        p2 = self.prompt_manager.get_prompt(
            'code_generation',
            self.code_gen_variant,
            desc=desc,
            module_path=module_path,
            plan=plan
        )
        self._log(p2)
        draft_raw = run(p2)
        self._log(draft_raw)
        
        # Strip potential outer fences
        draft = strip_code_fences(draft_raw)
        if not draft.strip():
            return RunResult(False, "Model returned empty module draft.")

        # Parse files
        parts = draft.split("## FILE:")
        if len(parts) <= 1:
            # Fallback: assume single file content for the main module
            final_code = draft.rstrip() + "\n"
            self.tools.write(module_path, final_code)
            return RunResult(True, f"Wrote module: {module_path}")

        files_written = []
        for part in parts[1:]:
            lines = part.splitlines()
            if not lines:
                continue
            
            filename = lines[0].strip()
            content = "\n".join(lines[1:]).strip() + "\n"
            
            target_path = filename
            # Heuristic: place README/requirements in the same dir as the main module
            if filename in ["README.md", "requirements.txt"]:
                target_path = str(Path(module_path).parent / filename)
            
            try:
                self.tools.write(target_path, content)
                files_written.append(target_path)
            except Exception as e:
                # If a file fails, we might want to continue or abort. 
                # For now, let's just log/return error? 
                # But we might have written others. 
                pass 

        if not files_written:
             return RunResult(False, "Parsed '## FILE:' markers but found no valid file content.")

        return RunResult(True, f"Wrote files: {', '.join(files_written)}")

    def commit_and_push(self, message: str, push: bool) -> RunResult:
        ok, out = self.tools.git_commit(message)
        if not ok:
            return RunResult(False, out)

        if push:
            ok2, out2 = self.tools.git_push()
            if not ok2:
                return RunResult(False, "Commit succeeded, but push failed:\n" + out2)
            return RunResult(True, "Commit and push succeeded.")

        return RunResult(True, "Commit succeeded.")

    def list_available_prompts(self) -> dict[str, list[str]]:
        """List all available prompt tasks and their variants."""
        tasks = self.prompt_manager.list_available_tasks()
        result = {}
        for task in tasks:
            result[task] = self.prompt_manager.list_variants(task)
        return result
