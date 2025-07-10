import os
import re, time, logging
from datetime import datetime, timedelta, timezone
from typing import List
import praw
from praw.models import Submission

from .config import (
    BRAND, COMPETITORS, GENERIC, DAYS_LOOKBACK, MAX_POSTS,
    REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT, 
)
from .models import RedditItem

_LOG = logging.getLogger(__name__)

# Build keyword regex
_QUERY_RGX = "|".join(
    kw.replace(" ", r"\s+") for kw in BRAND + COMPETITORS + GENERIC
)



def fetch_recent() -> List[RedditItem]:
   

    reddit = praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        user_agent=REDDIT_USER_AGENT,
        # read_only mode skips OAuth password flow
        # (you don't need username/password to search public posts)
        read_only=True
    )


    after = int((datetime.now(timezone.utc) - timedelta(days=DAYS_LOOKBACK)).timestamp())
    query = f"timestamp:{after}.. AND ({_QUERY_RGX})"

    subs: List[Submission] = list(
        reddit.subreddit("all").search(
            query, syntax="cloudsearch", sort="new", limit=MAX_POSTS
        )
    )

    results: List[RedditItem] = []
    for post in subs:
        results.append(
            RedditItem(
                title=post.title,
                text=post.selftext,
                url=post.url,
                subreddit=post.subreddit.display_name,
                score=post.score,
                created_utc=post.created_utc,
                id=post.id
            )
        )

    return results
