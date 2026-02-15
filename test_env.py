import os
from dotenv import load_dotenv

load_dotenv()

print("KEY:", os.getenv("OPENAI_API_KEY"))
