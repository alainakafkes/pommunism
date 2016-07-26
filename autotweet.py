# pommunism auto-tweeter

import tweepy, time
import brainscrape
import random
import os

with open("secrets/twittersecrets.txt") as f:
    secrets = f.readlines()

# get twitter auth secrets, being sure to remove the newline character
CONSUMER_KEY = secrets[0].rstrip('\n')
CONSUMER_SECRET = secrets[1].rstrip('\n')
ACCESS_TOKEN = secrets[2].rstrip('\n')
ACCESS_SECRET = secrets[3].rstrip('\n')

# auth is love, auth is life
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# obtain quotes using brainscrape.py, parse so that only <160 character tweets are made
tweetbase, size = brainscrape.getQuotes()
tweetlist = []
for i in range(0,size):
    if len(str(tweetbase[i][0])) <= 140: # then cite by author
        tweetlist.append(str(tweetbase[i][0]) + " - " + str(tweetbase[i][1]))
    elif len(str(tweetbase[i][0])) <= 160: # not enough space for author
        tweetlist.append(str(tweetbase[i][0]))

# randomize images and status to create random tweets
imgdir = os.listdir("img/")
randomtweet = random.choice(tweetlist)
api.update_with_media("img/"+random.choice(imgdir),randomtweet)

return "Good work, comrade!"
