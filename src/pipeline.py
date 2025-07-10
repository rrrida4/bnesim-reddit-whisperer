from src.reddit_clients import fetch_recent
from src.responder import generate_response
from src.scorer import score_response
if __name__ == "__main__":
    posts = fetch_recent()


    for post in posts:
        print("\n📨 New Reddit Post:")
        print(f"Title: {post['title']}")
        print(f"Content: {post['content']}")
        print(f"Context: {post['context']}")

        response = generate_response(post)
        score = score_response(response)

        print("\n🤖 AI Response:")
        print(response)
        print(f"\n📊 Response Score: {score}/10")
