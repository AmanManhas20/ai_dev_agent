import subprocess
import os


SOLUTION_PATH = os.path.join("generated_code", "solution.py")


def solution_exists():
    """
    Check if generated solution file exists
    """

    if not os.path.exists(SOLUTION_PATH):
        print("[Executor] No generated solution found.")
        return False

    return True


def execute_code():
    """
    Execute generated Python code and capture output
    """

    if not solution_exists():
        return "Execution aborted: solution.py not found."

    try:

        result = subprocess.run(
            ["python", SOLUTION_PATH],
            capture_output=True,
            text=True
        )

        stdout = result.stdout.strip()
        stderr = result.stderr.strip()

        if result.returncode != 0:
            return f"[Executor Error]\n{stderr}"

        return stdout if stdout else "[Executor] Program ran successfully (no output)."

    except Exception as e:
        return f"[Executor Failure] {str(e)}"