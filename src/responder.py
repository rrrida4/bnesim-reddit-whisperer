import openai
from src.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_response(post):
    """
    Generates a helpful, authentic response to a Reddit post using OpenAI.
    The response should:
    - Address the user's concern
    - Mention BNESIM casually
    - Follow Reddit etiquette (non-spammy, friendly, helpful)
    """

    prompt = f"""
You are a friendly Reddit user who knows a lot about international travel and eSIMs.

Someone posted this in a subreddit:

Title: {post['title']}
Content: {post['content']}
Context type: {post['context']}

Write a helpful, natural-sounding comment that:
- Offers practical advice or insights
- Mentions BNESIM casually as a solution (not a sales pitch)
- Follows Reddit tone and etiquette
- Encourages genuine discussion if possible
"""
    