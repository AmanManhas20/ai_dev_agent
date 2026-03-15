import sys
import os
import traceback
from dotenv import load_dotenv
from pathlib import Path

# Force load from the correct location
dotenv_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=dotenv_path)

print("KEY FOUND:", bool(os.getenv("GEMINI_API_KEY")))
print("Looking in:", dotenv_path)
print("File exists:", dotenv_path.exists())
import traceback

from agents.planner_agent import PlannerAgent
from agents.coder_agent import CoderAgent
from agents.reviewer_agent import ReviewerAgent
from agents.tester_agent import TesterAgent
from core.executor import execute_code


class AIDevAgent:

    def __init__(self):
        """Initialize all agents"""
        self.planner = PlannerAgent()
        self.coder = CoderAgent()
        self.reviewer = ReviewerAgent()
        self.tester = TesterAgent()

    def run(self, task: str):
        """
        Main pipeline for executing the AI developer workflow
        """

        try:
            print("\n--- AI Developer Agent Started ---\n")

            # Step 1: Plan task
            print("[1] Planning development steps...\n")
            steps = self.planner.plan(task)

            if not steps:
                raise ValueError("Planner failed to generate steps")

            # Step 2: Generate code
            print("\n[2] Generating code...\n")
            generated_code = self.coder.generate_code(steps)

            if not generated_code:
                raise ValueError("Code generation failed")

            # Step 3: Execute generated code
            print("\n[3] Executing generated code...\n")
            execution_output = execute_code()

            print("Execution Output:")
            print(execution_output)

            # Step 4: Run tests
            print("\n[4] Running automated tests...\n")
            test_results = self.tester.run_tests()

            print("Test Results:")
            print(test_results)

            # Step 5: Review code
            print("\n[5] Reviewing code quality...\n")
            review_feedback = self.reviewer.review(generated_code)

            print("Review Feedback:")
            print(review_feedback)

            print("\n--- Pipeline Completed Successfully ---\n")

        except Exception as e:
            print("\n[ERROR] Pipeline failed")
            print(str(e))
            traceback.print_exc()


def get_user_task():
    """
    Safely read user task input
    """

    print("\nEnter development task:")
    task = input("> ").strip()

    if not task:
        print("Task cannot be empty")
        sys.exit(1)

    return task


def main():
    """
    Application entry point
    """

    task = get_user_task()

    agent = AIDevAgent()
    agent.run(task)


if __name__ == "__main__":
    main()