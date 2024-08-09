import tweepy
from textblob import TextBlob

consumer_key ='YOUR_CONSUMER'
consumer_secret ='YOUR_CON'

access_token='YOUR_ACCESS'
access_token='YOUR_ACCESS'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Updated method from api.search() to api.search_tweets()
public_tweets = api.search_tweets('trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
