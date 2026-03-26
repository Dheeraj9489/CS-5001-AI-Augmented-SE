"""
Tool handlers — pure Python functions, one per tool.

Function names must match the tool names in schemas.py exactly;
app.py dispatches by name using getattr(handlers, name).
"""
import subprocess
from pathlib import Path

MAX_FILE_CHARS = 8_000


def git_diff(repo_path: str, base: str = "main", head: str = "HEAD") -> str:
    try:
        result = subprocess.run(
            ["git", "diff", f"{base}...{head}"],
            capture_output=True, text=True, timeout=15,
            cwd=repo_path,
        )
        diff = result.stdout.strip()
        if not diff:
            result = subprocess.run(
                ["git", "diff", base, head],
                capture_output=True, text=True, timeout=15,
                cwd=repo_path,
            )
            diff = result.stdout.strip()
        return diff[:MAX_FILE_CHARS] if diff else "No diff found between the specified refs."
    except subprocess.CalledProcessError as exc:
        return f"Git diff error: {exc}"
    except FileNotFoundError:
        return f"Repository path not found: {repo_path}"


def get_recent_commits(repo_path: str, count: int = 5) -> str:
    try:
        result = subprocess.run(
            ["git", "log", f"-{count}", "--pretty=format:%h | %an | %ad | %s", "--date=short"],
            capture_output=True, text=True, timeout=15,
            cwd=repo_path,
        )
        return result.stdout.strip() or "No commits found."
    except subprocess.CalledProcessError as exc:
        return f"Git log error: {exc}"
    except FileNotFoundError:
        return f"Repository path not found: {repo_path}"


def read_file(path: str) -> str:
    return Path(path).read_text(errors="replace")[:MAX_FILE_CHARS]


def list_directory(path: str) -> str:
    entries = sorted(Path(path).iterdir(), key=lambda e: (e.is_file(), e.name))
    lines = [f"{'DIR ' if e.is_dir() else 'FILE'} {e.name}" for e in entries]
    return "\n".join(lines) or "(empty)"
