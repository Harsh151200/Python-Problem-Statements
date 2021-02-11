import tweepy
import json

consumer_key = 'your key'
consumer_secret = 'your secret key'

access_token = 'your token'
access_token_secret = 'your secret token'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
    
user = api.get_user('patelharsh_1512')
print(user)

