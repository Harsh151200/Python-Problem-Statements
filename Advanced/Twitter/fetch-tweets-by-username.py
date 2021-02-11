from credentials import *
import tweepy

print(tweepy.__version__)
userID = "realDonaldTrump"

consumer_key = 'your key'
consumer_secret = 'your secret key'

access_token = 'your token'
access_token_secret = 'your secret token'


# Authorize our Twitter credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweets = api.user_timeline(screen_name=userID, 
                           # 200 is the maximum allowed count
                           count=200,
                           include_rts = False,
                           # Necessary to keep full_text 
                           # otherwise only the first 140 words are extracted
                           tweet_mode = 'extended'
                           )

