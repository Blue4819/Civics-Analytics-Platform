import praw
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import json

# Download VADER lexicon
nltk.download('vader_lexicon')

# Define user values in a dictionary
user_values = {
    "client_id": "J-hzwVyAncW42ZQJKdbqXQ",
    "client_secret": "lA3LgsFQPURJkXKuAjismV7ZJZJ6AQ",
    "user_agent": "CAP",
    "username": "LostAlfalfa7283",
    "password": "/MLxPig#YZ58a4j"
}

# Initialize the Reddit API client
reddit = praw.Reddit(
    client_id=user_values['client_id'],
    client_secret=user_values['client_secret'],
    user_agent=user_values['user_agent'],
    username=user_values['username'],
    password=user_values['password']
)

# Initialize VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Choose a subreddit and fetch posts
subreddit = reddit.subreddit("IndiaNews")  # Replace with the desired subreddit
hot_posts = subreddit.hot(limit=11)  # Fetch top 11 'hot' posts

# Perform sentiment analysis
post_sentiments = []

for post in hot_posts:
    title = post.title
    url = post.url

    # Perform sentiment analysis using VADER
    sentiment_scores = sia.polarity_scores(title)  # Returns a dictionary with sentiment metrics

    # Store results
    post_sentiments.append({
        "title": title,
        "url": url,
        "neg": sentiment_scores['neg'],  # Negative score
        "neu": sentiment_scores['neu'],  # Neutral score
        "pos": sentiment_scores['pos'],  # Positive score
        "compound": sentiment_scores['compound']  # Overall sentiment score
    })

# Display results
print("Sentiment Analysis of Reddit Posts:\n")
for post in post_sentiments:
    print(f"Title: {post['title']}")
    print(f"URL: {post['url']}")
    print(f"Negative: {post['neg']:.2f}, Neutral: {post['neu']:.2f}, Positive: {post['pos']:.2f}, Compound: {post['compound']:.2f}\n")


