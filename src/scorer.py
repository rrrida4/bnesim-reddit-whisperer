from textblob import TextBlob
def analyze_sentiment(text):
    """
    Uses TextBlob to analyze the sentiment of the given text.
    Returns a sentiment polarity score between -1.0 (negative) and 1.0 (positive).
    """
    return TextBlob(text).sentiment.polarity


def score_opportunity(post):
    """
    Scores a Reddit post for marketing opportunity based on:
    - Sentiment (neutral/positive = better)
    - Engagement (upvotes + comments)
    - Intent (is it a question, complaint, or recommendation request)

    Returns a float score between 0 and 1.
    """
    sentiment_score = analyze_sentiment(post['content'])
    engagement_score = min((post['upvotes'] + post['num_comments']) / 50, 1)

    # Context boost
    context_type = post.get('context', '')
    if context_type == "question":
        intent_score = 1.0
    elif context_type == "recommendation":
        intent_score = 0.8
    elif context_type == "complaint":
        intent_score = 0.6
    else:
        intent_score = 0.3

    # Final weighted score
    final_score = (0.4 * sentiment_score) + (0.3 * engagement_score) + (0.3 * intent_score)
    return round(final_score, 3)
def score_response(post):
    return score_opportunity(post)
