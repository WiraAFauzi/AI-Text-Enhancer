import os
from openai import OpenAI
from dotenv import load_dotenv
from openai import RateLimitError

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
mock_mode = os.getenv("MOCK_MODE", "false").lower() == "true"

if not api_key and not mock_mode:
    raise ValueError("OPENAI_API_KEY is not set and MOCK_MODE is disabled")

client = OpenAI(api_key=api_key) if api_key else None


def mock_response(text: str, mode: str) -> str:
    if mode == "professional":
        return f"[MOCK PROFESSIONAL VERSION]: {text.capitalize()}."
    elif mode == "summarize":
        return f"[MOCK SUMMARY]: {text[:50]}..."
    elif mode == "improve":
        return f"[MOCK IMPROVED]: {text} (refined and clarified)"
    else:
        return f"[MOCK DEFAULT]: {text}"


def generate_text(text: str, mode: str) -> str:

    # If MOCK_MODE enabled, skip OpenAI entirely
    if mock_mode:
        return mock_response(text, mode)

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": f"Transform the text into {mode} style."},
                {"role": "user", "content": text}
            ],
        )

        return response.choices[0].message.content

    except RateLimitError:
        # Automatic fallback if quota exceeded
        return mock_response(text, mode)

    except Exception as e:
        print("Unexpected OpenAI Error:", e)
        raise
