import tweepy
from textblob import TextBlob

consumer_key = 'WL6PirdWmQ0d5N1TGoXZfqRRd'
consumer_secret = 'n467KKgZkheIyauSHJCu9nyLE7kCiTPdLeYxl95Wuo8fP6tND5'

access_token = '1445786018666323978-P7nvQOXIu3crXSBrHWn9MS7oMxnZEO'
access_token_secret = 'xJpIGr5QhSHXvgGmWYvQ02osDsu73NO0lmpvb9dWei7u9'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Updated method from api.search() to api.search_tweets()
public_tweets = api.search_tweets('trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
