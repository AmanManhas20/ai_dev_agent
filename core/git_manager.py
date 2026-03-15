import subprocess
from pathlib import Path


class GitManager:
    """
    Utility class for basic Git operations used by the AI agent:
    - pull latest changes
    - stage files
    - commit generated code
    """

    def __init__(self, repo_path: str = "."):
        self.repo_path = Path(repo_path)

    def _run(self, args):
        """
        Run a git command safely and return stdout/stderr.
        """
        result = subprocess.run(
            ["git"] + args,
            cwd=self.repo_path,
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            raise RuntimeError(result.stderr.strip())

        return result.stdout.strip()

    def pull(self):
        """
        Pull latest changes from remote repository.
        """
        print("[GitManager] Pulling latest changes...")
        return self._run(["pull"])

    def add_all(self):
        """
        Stage all changes.
        """
        print("[GitManager] Staging changes...")
        return self._run(["add", "."])

    def commit(self, message: str):
        """
        Commit staged changes.
        """
        if not message:
            raise ValueError("Commit message cannot be empty")

        print("[GitManager] Creating commit...")
        return self._run(["commit", "-m", message])

    def push(self):
        """
        Push commits to remote repository.
        """
        print("[GitManager] Pushing to remote...")
        return self._run(["push"])