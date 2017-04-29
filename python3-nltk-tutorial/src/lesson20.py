'''
Created on Apr 29, 2017

Twitter Sentiment Analysis with NLTK
https://www.youtube.com/watch?v=SB8ckgT8l9c&list=PLQVvvaa0QuDf2JswnfiGkliBInZnIC4HL&index=20

@author: ubuntu
'''
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s
import sys

#consumer key, consumer secret, access token, access secret.
#ckey="asdfsafsafsaf"
#csecret="asdfasdfsadfsa"
#atoken="asdfsadfsafsaf-asdfsaf"
#asecret="asdfsadfsadfsadfsadfsad"

# locally stored file with credentials
from twitter_api_keys import *

class listener(StreamListener):

    def on_data(self, data):
        try:
            all_data = json.loads(data)
    
            tweet = all_data["text"]
            sentiment_value, confidence = s.sentiment(tweet)
            print(tweet, sentiment_value, confidence)
    
            if confidence*100 >= 80:
                output = open("twitter-out.txt","a")
                output.write(sentiment_value)
                output.write('\n')
                output.close()
    
            return True
        except:
            print("Unexpected error:", sys.exc_info()[0])
            return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["happy"])