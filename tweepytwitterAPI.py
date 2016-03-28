#! /usr/bin/env python3

import time
import tweepy
import os
import sys


consumer_key = X
consumer_secret = X
access_token_key = X
access_token_secret = X


class Listener(tweepy.StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

myStreamListener = Listener()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)
stream = tweepy.Stream(auth, myStreamListener)

stream.filter(track=[sys.argv[1]])
