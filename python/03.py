import tweepy
from textblob import TextBlob

# Twitter API credentials
consumer_key = 'YOUR_CON'
consumer_secret= 'YOUR_CON_SEC'

access_token= 'YOUR_ACC_TOK'
access_token_secret= 'YOUR_ACC_TOK_SEC'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Updated method from api.search() to api.search_tweets()
public_tweets = api.search_tweets('trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
