import praw
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import pandas as pd

# Download VADER lexicon if not already downloaded
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
subreddit = reddit.subreddit("IndiaNews")  # Replace with your desired subreddit
hot_posts = subreddit.hot(limit=60)  # Fetch top 500 'hot' posts

# Perform sentiment analysis and store results
post_sentiments = []

for post in hot_posts:
    title = post.title
    url = post.url

    # Perform sentiment analysis using VADER
    sentiment_scores = sia.polarity_scores(title)  # Returns a dictionary with sentiment metrics

    # Determine sentiment category based on compound score
    if sentiment_scores['compound'] >= 0.05:
        sentiment_category = 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        sentiment_category = 'Negative'
    else:
        sentiment_category = 'Neutral'

    # Append results to the list
    post_sentiments.append({
        "Title": title,
        "URL": url,
        "Negative": sentiment_scores['neg'],  # Negative score
        "Neutral": sentiment_scores['neu'],  # Neutral score
        "Positive": sentiment_scores['pos'],  # Positive score
        "Compound": sentiment_scores['compound'],  # Overall sentiment score
        "Sentiment Category": sentiment_category  # Add sentiment category
    })

# Convert the list of dictionaries to a Pandas DataFrame
df = pd.DataFrame(post_sentiments)

# Check if DataFrame is empty
if df.empty:
    print("No data collected. DataFrame is empty.")
else:
    # Save the DataFrame to a CSV file
    csv_file_path = r"C:\Users\Purva\Desktop\WORK\Sem-7\Civics-Analytics-Platform\backend\News Sentiments\Reddit\reddit_sentiment_analysis.csv"

    try:
        df.to_csv(csv_file_path, index=False)
        print(f"Sentiment analysis completed and results saved to {csv_file_path}")
    except Exception as e:
        print(f"Error saving CSV file: {e}")