### Tutorial: Build Your Own Twitter Bot Using Python & Tweepy
### Hosted by Alaina Kafkes on behalf of Ladies Storm Hackathons

## Today, we'll build a communism + Pomeranian (Pommunism) bot!

import tweepy # Here's our lovely Twitter API wrapper!
import random # This will help us pick a random image later.
import os # This will help us get & save the image directory later.
import time # This will help us time our tweets later.

# Store Twitter consumer key & secret and API key & secret in a separate file
#   that you NEVER NEVER NEVER publish online. Seriously. If someone else gets
#   access to these, they could alter your code and your app!
# readlines() stores your four authorization components from secrets.txt in
#   an array called secrets
with open("secrets.txt") as f:
    secrets = f.readlines()
f.close()

# Set Twitter authorization information from secrets array, being sure to
#   remove the newline character aka '\n'
CONSUMER_KEY = secrets[0].rstrip('\n')
CONSUMER_SECRET = secrets[1].rstrip('\n')
ACCESS_TOKEN = secrets[2].rstrip('\n')
ACCESS_SECRET = secrets[3].rstrip('\n')

# Give your auth info to Tweepy so that you can access the Twitter API
# Otherwise, your Tweepy function calls will be rejected :/ v sad
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Build list of tweets!
# I came up with a preset list, but if you look at my Pommunism project on
#   GitHub you can see how I made my tweetlist larger and more complex
tweetlist = ["Woof! Long live the revolution.",
            "Bork bork you are doing me a capitalism. :/",
            "I bleed red. #PomsForComs",
            "Call me your comrade, I'm more like your POMrade lmao",
            "I want someone who loves the hammer & sickle like Drake loves Rihanna"]

# Set up a shortcut to your image directory so you have easy access to it later
imgdir = os.listdir("img/")

# Tweeting time! This is the Twitter API call at the heart of the code
# Tweepy has a function called api.update_with_media that lets you make
#   a new tweet with a photo and text!
# time.sleep(10) means that there will be a 10 second break between each tweet
for tweet in tweetlist:
	api.update_with_media("img/"+random.choice(imgdir), tweet)
    print("Good work, comrade!")
	time.sleep(10)
