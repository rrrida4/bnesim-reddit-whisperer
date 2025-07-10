from pathlib import Path
import os
from typing import List
from dotenv import load_dotenv
import os

load_dotenv()

REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")

# --- OpenAI ---
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# --- Business keywords ---
BRAND:    List[str] = ["bnesim"]
GENERIC:  List[str] = [
    "travel esim", "international roaming", "data roaming",
    "travel connectivity", "sim recommendation",
]
COMPETITORS: List[str] = [
    "airalo", "holafly", "gigsky", "nomad esim", "flexiroam"
]

DAYS_LOOKBACK = 7      # last N days
MAX_POSTS     = 200    # safety cap

# Weights for opportunity score
W_ENGAGE = 0.4
W_NEED   = 0.4
W_SENT   = 0.2
