import os
from core.llm_client import LLMClient


class PlannerAgent:
    """
    Planner Agent
    Responsible for breaking a development task into smaller steps.
    """

    def __init__(self):
        self.llm = LLMClient()

    def build_prompt(self, task: str) -> str:
        """
        Create prompt for the LLM planner
        """

        prompt = f"""
You are a senior software engineer.

Break the following development task into clear implementation steps.

Rules:
- Provide numbered steps
- Be concise
- Focus only on coding tasks

TASK:
{task}

OUTPUT FORMAT:
1. Step one
2. Step two
3. Step three
"""

        return prompt.strip()

    def parse_steps(self, raw_output: str):
        """
        Convert LLM text response into a Python list
        """

        steps = []

        lines = raw_output.split("\n")

        for line in lines:

            line = line.strip()

            if not line:
                continue

            # remove numbering
            if line[0].isdigit():
                step = line.split(".", 1)[-1].strip()
                steps.append(step)
            else:
                steps.append(line)

        return steps

    def plan(self, task: str):
        """
        Main planning function
        """

        if not task or len(task.strip()) == 0:
            raise ValueError("Task cannot be empty")

        prompt = self.build_prompt(task)

        try:
            response = self.llm.generate(prompt)

            steps = self.parse_steps(response)

            print("\nGenerated Plan:\n")

            for i, step in enumerate(steps, start=1):
                print(f"{i}. {step}")

            return steps

        except Exception as e:
            print("PlannerAgent error:", str(e))
            return []