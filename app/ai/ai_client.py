from openai import OpenAI
from app.config.settings import settings

class AIClient:
    def __init__(self):
        self.client = OpenAI(api_key=settings.openai_api_key)

    def generate_response(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content.strip()

    def chat(self, prompt: str) -> str:
        return self.generate_response(prompt)

    def generate_structured_response(self, prompt: str, response_model):
        response = self.client.beta.chat.completions.parse(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}],
            response_format=response_model
        )
        return response.choices[0].message.parsed
    