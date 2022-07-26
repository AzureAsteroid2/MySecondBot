"""Steals a twitter post from a specific moon account
Returns the result to main"""
import tweepy
import os
auth = tweepy.OAuthHandler(os.environ['twitter1'], os.environ['twitter2'])
auth.set_access_token(os.environ['twitter3'], os.environ['twitter4'])
api = tweepy.API(auth)
#t = Twitter(auth=OAuth(os.environ['twitter1'], os.environ['twitter2'], os.environ['twitter3'], os.environ['twitter4']))
class Twealer:
  def __init__(self):
    pass
  def steal(self, name = "mymoonphaseapp"):
    tweet = api.user_timeline(screen_name = name, count=1)[0]
    result = f'https://twitter.com/{name}/status/{tweet.id}'
    return result