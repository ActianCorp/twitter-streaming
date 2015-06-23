#!/usr/bin/env python
# ________         _______________            ____________                               
# ___  __/__      ____(_)_  /__  /______________  ___/_  /__________________ _______ ___ 
# __  /  __ | /| / /_  /_  __/  __/  _ \_  ___/____ \_  __/_  ___/  _ \  __ `/_  __ `__ \
# _  /   __ |/ |/ /_  / / /_ / /_ /  __/  /   ____/ // /_ _  /   /  __/ /_/ /_  / / / / /
# /_/    ____/|__/ /_/  \__/ \__/ \___//_/    /____/ \__/ /_/    \___/\__,_/ /_/ /_/ /_/ 
#                                                                                       

import tweepy
import threading, logging, time
from kafka.client import KafkaClient
from kafka.consumer import SimpleConsumer
from kafka.producer import SimpleProducer
import string

######################################################################
# Authentication details. To  obtain these visit dev.twitter.com
######################################################################

consumer_key = 'your-key-values'#eWkgf0izE2qtN8Ftk5yrVpaaI
consumer_secret = 'your-key-values'#BYYnkSEDx463mGzIxjSifxfXN6V1ggpfJaGBKlhRpUMuQ02lBX
access_token = 'your-key-values'#1355650081-Mq5jok7mbcrIbTpqZPcMHgWjcymqSrG1kVaut39
access_token_secret = 'your-key-values'#QovqxQnw0hSPrKwFIYLWct3Zv4MeGMash66IaOoFyXNWs

mytopic='topic'# ex. 'twitterstream', or 'test' ...

######################################################################
#Create a handler for the streaming data that stays open...
######################################################################

class StdOutListener(tweepy.StreamListener):

    #Handler
    ''' Handles data received from the stream. '''

    ######################################################################
    #For each status event
    ######################################################################

    def on_status(self, status):
        
        # Prints the text of the tweet
        #print '%d,%d,%d,%s,%s' % (status.user.followers_count, status.user.friends_count,status.user.statuses_count, status.user.id_str, status.user.screen_name)
        
        # Schema changed to add the tweet text
        print '%d,%d,%d,%s,%s' % (status.user.followers_count, status.user.friends_count,status.user.statuses_count, status.text, status.user.screen_name)
        message =  str(status.user.followers_count) + ',' + str(status.user.friends_count) + ',' + str(status.user.statuses_count) + ',' + status.text + ',' + status.user.screen_name
        msg = filter(lambda x: x in string.printable, message)
        try:
            #write out to kafka topic
            producer.send_messages(mytopic, str(msg))
        except Exception, e:
            return True
        
        return True
       
    ######################################################################
    #Supress Failure to keep demo running... In a production situation 
    #Handle with seperate handler
    ######################################################################
 
    def on_error(self, status_code):

        print('Got an error with status code: ' + str(status_code))
        return True # To continue listening
 
    def on_timeout(self):

        print('Timeout...')
        return True # To continue listening

######################################################################
#Main Loop Init
######################################################################


if __name__ == '__main__':
    
    listener = StdOutListener()

    #sign oath cert

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    auth.set_access_token(access_token, access_token_secret)

    #uncomment to use api in stream for data send/retrieve algorythms 
    #api = tweepy.API(auth)

    stream = tweepy.Stream(auth, listener)

    ######################################################################
    #Sample delivers a stream of 1% (random selection) of all tweets
    ######################################################################
    stream.sample()
    client = KafkaClient("localhost:9092")
    producer = SimpleProducer(client)

    ######################################################################
    #Custom Filter rules pull all traffic for those filters in real time.
    #Bellow are some examples add or remove as needed...
    ######################################################################
    #A Good demo stream of reasonable amount
    #stream.filter(track=['actian', 'BigData', 'Hadoop', 'Predictive', 'Quantum', 'bigdata', 'Analytics', 'IoT'])
    #Hadoop Summit following
    #stream.filter(track=['actian', 'hadoop', 'hadoopsummit'])

