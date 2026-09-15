from ai_client import AIClient


client = AIClient()

response = client.chat("Reply with exactly one sentence saying Hello from the Employee AI Platform.")

print(response)