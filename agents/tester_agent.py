import subprocess
import os


class TesterAgent:
    """
    Tester Agent
    Responsible for executing test cases and reporting results.
    """

    def __init__(self):
        self.test_directory = "tests"

    def tests_exist(self):
        """
        Check if tests directory exists
        """

        if not os.path.exists(self.test_directory):
            print("[TesterAgent] No tests directory found.")
            return False

        return True

    def run_tests(self):
        """
        Run test suite using pytest
        """

        if not self.tests_exist():
            return "No tests available."

        try:

            result = subprocess.run(
                ["pytest", self.test_directory],
                capture_output=True,
                text=True
            )

            output = result.stdout + "\n" + result.stderr

            if result.returncode == 0:
                status = "ALL TESTS PASSED"
            else:
                status = "TEST FAILURES DETECTED"

            print(f"\n[TesterAgent] {status}\n")

            return output

        except FileNotFoundError:
            return "pytest is not installed. Run: pip install pytest"

        except Exception as e:
            return f"[TesterAgent] Error running tests: {str(e)}"