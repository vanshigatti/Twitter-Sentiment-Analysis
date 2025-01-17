# Import necessary libraries
import tweepy
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns

# Twitter API credentials (Replace these with your own API keys)
consumer_key = 'dN9V8lYj6CdSMGMJJe5bDTf9a'
consumer_secret = 'mHgGMZAcwjF4sv8wsNXAGP3JwXR9xGdlXJGksWHo2qUN6IjBNO'
access_token = '1880081705161097216-7WCrCfkpMCox7W270l6dIWFbGp57Py'
access_token_secret = 'V6x4sgGui0W00NTgqwY4auFswn7QybU1FBcp5h77WvM04'

# Set up Tweepy authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Function to fetch tweets
def fetch_tweets(query, count=100):
    # Fetch tweets based on a search query (updated method for Tweepy v4.x+)
    tweets = tweepy.Cursor(api.search_tweets, q=query, lang='en').items(count)
    
    # Create a DataFrame to store tweet text and sentiment analysis
    tweet_data = []
    for tweet in tweets:
        tweet_data.append({'tweet': tweet.text, 'date': tweet.created_at})
    
    return pd.DataFrame(tweet_data)

# Function to perform sentiment analysis
def analyze_sentiment(text):
    # Use TextBlob to calculate sentiment polarity (-1 to 1)
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

# Fetch tweets for a specific query
tweets_df = fetch_tweets('Python programming', 200)

# Analyze sentiment for each tweet and add a new column for sentiment score
tweets_df['sentiment'] = tweets_df['tweet'].apply(analyze_sentiment)

# Visualize sentiment distribution
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.histplot(tweets_df['sentiment'], bins=30, kde=True, color='blue')
plt.title('Sentiment Distribution of Tweets')
plt.xlabel('Sentiment Score')
plt.ylabel('Frequency')
plt.show()

# Display the first few rows of the DataFrame
print(tweets_df.head())
