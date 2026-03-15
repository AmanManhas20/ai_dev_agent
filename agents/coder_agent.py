from core.llm_client import LLMClient
from core.file_manager import save_code


class CoderAgent:
    """
    Code generation agent
    Responsible for generating Python code from planning steps
    """

    def __init__(self):
        self.llm = LLMClient()

    def build_prompt(self, steps):
        """
        Build LLM prompt from planning steps
        """

        formatted_steps = "\n".join(
            [f"{i+1}. {step}" for i, step in enumerate(steps)]
        )

        prompt = f"""
You are an experienced Python software engineer.

Write clean, production-quality Python code implementing the following steps.

STEPS:
{formatted_steps}

Rules:
- Return only Python code
- No explanations
- Include necessary functions
- Include a small example execution in __main__

OUTPUT: Python code only
"""

        return prompt.strip()

    def generate_code(self, steps):
        """
        Generate Python code from plan
        """

        if not steps:
            raise ValueError("No steps provided to coder agent")

        prompt = self.build_prompt(steps)

        try:
            response = self.llm.generate(prompt)

            # remove markdown if model returns ```python blocks
            code = response.replace("```python", "").replace("```", "")

            save_code(code)

            print("\nGenerated code saved to generated_code/solution.py\n")

            return code

        except Exception as e:
            print("CoderAgent error:", str(e))
            return None