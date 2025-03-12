import openai
import tweepy
from .config import (
    OPENAI_API_KEY,
    TWITTER_API_KEY, TWITTER_API_SECRET,
    TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET
)


def summarize_caption(caption):

    prompt = f"Summarize this caption into a concise tweet under 280 characters:\n\n{caption}"
    
    try:
        openai.api_key = OPENAI_API_KEY
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=50
        )
        
        summary = response["choices"][0]["message"]["content"].strip()
        return summary if len(summary) <= 280 else summary[:277] + "..."

def post_tweet(tweet_text):
    try:
        auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
        auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
        api = tweepy.API(auth)

        tweet = api.update_status(tweet_text)
        return {"success": True, "tweet_id": tweet.id, "tweet_text": tweet_text}

    except Exception as e:
        return {"success": False, "error": str(e)}