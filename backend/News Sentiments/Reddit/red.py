import praw
import json

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

def create_reddit_object(json_file="C:\\Users\\Purva\\Desktop\\WORK\\Sem-7\\Capstone\\Civics-Analytics-Platform\\News Sentiments\\Reddit\\reddit_config.json", json_key="reddit"):
    # Load configuration from the JSON file
    with open(json_file, "r") as file:
        config = json.load(file)
    
    # Get the relevant key for Reddit configuration
    reddit_config = config[json_key]
    
    # Initialize and return the Reddit object
    reddit = praw.Reddit(
        client_id=reddit_config['client_id'],
        client_secret=reddit_config['client_secret'],
        user_agent=reddit_config['user_agent'],
        username=reddit_config['username'],
        password=reddit_config['password']
    )
    
    return reddit




subred = reddit.subreddit("India's News")
hot = subred.hot(limit = 11)
new = subred.new(limit = 10)
controv = subred.controversial(limit=10)
top = subred.top(limit = 10)
gilded = subred.gilded(limit=10)

type(hot)
x= next(hot)
dir(x)

for i in hot:
    print(i.title, i.url)

