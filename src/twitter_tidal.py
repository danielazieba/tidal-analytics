# scrapes twitter activity using tweepy api

import json
import tweepy
from tweepy import OAuthHandler


consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

def process_or_store(tweet):
    print(json.dumps(tweet))

def print_texts(tweets):
	for i in tweets:
		print(i.text)

#tweets = api.user_timeline(screen_name='kanyewest',count=200)

def get_tweets(user, num):
    tweets = api.user_timeline(screen_name=user,count=num)
    return tweets
