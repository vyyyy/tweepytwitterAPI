#! /usr/bin/env python3
#run script from bash commandline
#don't forget to setup file permission

#import modules
import time
import tweepy
import sys

#keys for authentication
consumer_key = X
consumer_secret = X
access_token_key = X
access_token_secret = X

#connect to Twitter API 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)

#create the Stream Listener class 
class Listener(tweepy.StreamListener):

    def on_status(self, status):
        print("New Tweet: ",status.author.screen_name,status.text)
        return True

    def on_error(self, status_code):
        if status_code == 420:
            #returning False disconnects the stream
            return False

#instantiate myStreamListener object
myStreamListener = Listener()

#stream will show incoming tweets
stream = tweepy.Stream(auth, myStreamListener)

#pass commandline argument as a string to filter and track tweets
stream.filter(track=[sys.argv[1]])
