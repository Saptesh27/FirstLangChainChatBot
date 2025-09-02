import os
from dotenv import load_dotenv

load_dotenv()  # safe: reads .env if present but uses env var if set

_GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
_GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not _GOOGLE_API_KEY:
    raise RuntimeError("Missing GOOGLE_API_KEY environment variable")
if not _GROQ_API_KEY:
    raise RuntimeError("Missing GROQ_API_KEY environment variable")
