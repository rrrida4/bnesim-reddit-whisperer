import re, logging
from typing import List
from transformers import pipeline

from .models import RedditItem

_LOG = logging.getLogger(__name__)

# Load sentiment model (from HuggingFace)
_SENTIMENT = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest",
    batch_size=8,
    truncation=True,
)

# Regex rules to identify post type
_Q = re.compile(r"\?")
_COMPLAINT = re.compile(r"(ripoff|overcharg|problem|issue|terrible|awful)", re.I)
_RECOMMEND = re.compile(r"(recommend|suggest|best esim|which esim)", re.I)

def _classify(text: str) -> str:
    t = text.lower()
    if _Q.search(text) and _RECOMMEND.search(text):
        return "recommend"
    if _COMPLAINT.search(t):
        return "complaint"
    if _Q.search(text):
        return "question"
    return "fyi"

def enrich(items: List[RedditItem]) -> None:
    texts = [f"{it.title}. {it.body}" for it in items]
    senti = _SENTIMENT(texts)
    for it, s in zip(items, senti):
        it.context   = _classify(f"{it.title} {it.body}")
        it.sentiment = s["label"].lower()  # positive / neutral / negative
