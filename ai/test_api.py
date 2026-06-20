from ai.gemini_client import get_gemini_response

response = get_gemini_response(
    "Say hello in one sentence."
)

print(response)