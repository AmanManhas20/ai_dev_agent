import os
import time
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

class LLMClient:
    """
    Centralized LLM client for the AI Developer Agent system.
    Handles API communication, retries, and response formatting.
    """

    def __init__(self):

        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise EnvironmentError(
                "GROQ_API_KEY environment variable not set."
            )

        self.client = Groq(api_key=api_key)
        self.model = "llama-3.3-70b-versatile"
        self.max_retries = 3
        self.retry_delay = 2

    def generate(self, prompt: str) -> str:
        """
        Send prompt to the language model and return text response
        """

        if not prompt or len(prompt.strip()) == 0:
            raise ValueError("Prompt cannot be empty")

        for attempt in range(self.max_retries):

            try:

                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    temperature=0.3
                )

                content = response.choices[0].message.content

                if not content:
                    raise RuntimeError("Empty response from model")

                return content.strip()

            except Exception as e:

                if attempt == self.max_retries - 1:
                    raise RuntimeError(
                        f"LLM request failed after retries: {str(e)}"
                    )

                time.sleep(self.retry_delay)

    def health_check(self):
        """
        Verify connection to LLM API
        """

        try:
            response = self.generate("Reply with the word OK.")
            if "OK" in response.upper():
                return True
            return False
        except Exception:
            return False
