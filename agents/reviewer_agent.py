from core.llm_client import LLMClient


class ReviewerAgent:
    """
    Code review agent.
    Uses LLM to analyze generated code and provide feedback.
    """

    def __init__(self):
        self.llm = LLMClient()

    def build_prompt(self, code: str) -> str:
        """
        Build prompt for code review
        """

        prompt = f"""
You are a senior Python code reviewer.

Review the following Python code carefully.

Focus on:
1. Bugs or logical errors
2. Code readability
3. Performance issues
4. Edge cases
5. Suggestions for improvement

Provide concise feedback.

CODE:
{code}

OUTPUT FORMAT:

Bugs:
- ...

Improvements:
- ...

Optimization suggestions:
- ...
"""

        return prompt.strip()

    def review(self, code: str):
        """
        Run code review using LLM
        """

        if not code or len(code.strip()) == 0:
            raise ValueError("No code provided for review")

        prompt = self.build_prompt(code)

        try:
            response = self.llm.generate(prompt)

            print("\n[ReviewerAgent] Code Review Feedback:\n")
            print(response)

            return response

        except Exception as e:
            print("[ReviewerAgent] Error:", str(e))
            return None