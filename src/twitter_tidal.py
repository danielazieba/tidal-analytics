# scrapes twitter activity using tweepy api

import json
import tweepy
from tweepy import OAuthHandler

# remove these if uploading *

consumer_key = 'fAbbKl3kk8WStBiKPoVmxXQiU'
consumer_secret = 'J39i427SLo4MW2TJ5eS1vc05YSYUlv2CP5ESysxo5Wiy0iAiyX'
access_token = '1015005685761937408-KlMqmH6dhZS7nlkVJKnzvhC2Gvq5cY'
access_secret = '9qNv04hnF0b5zAlG5onxelCCZ5vQLzu4QRQGOlevhVt2r'

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
