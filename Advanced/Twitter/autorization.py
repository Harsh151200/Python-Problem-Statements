import tweepy
import json

consumer_key = 'your key'
consumer_secret = 'your secret key'

access_token = 'your token'
access_token_secret = 'your secret token'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

try:
    redirect_url = auth.get_authorization_url()
    print(redirect_url)
except tweepy.TweepError:
    print('Error! Failed to get request token.')
    
# https://fairyonice.github.io/extract-someones-tweet-using-tweepy.html