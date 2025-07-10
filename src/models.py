from dataclasses import dataclass
from datetime import datetime

@dataclass(slots=True)
class RedditItem:
    id: str
    url: str
    title: str
    body: str
    subreddit: str
    created_at: datetime
    upvotes: int
    comments: int
    context: str | None = None      # question / complaint / recommend / fyi
    sentiment: str | None = None    # positive / neutral / negative
    score: float | None = None
    reply: str | None = None
