import tweepy

######################################################################
# Authentication details. To  obtain these visit dev.twitter.com
######################################################################
consumer_key = ''#example : eWkgf0izE2qtN8Ftk5yrVpaaI
consumer_secret = ''#example : BYYnkSEDx463mGzIxjSifxfXN6V1ggpfJaGBKlhRpUMuQ02lBX
access_token = ''#example : 1355650081-Mq5jok7mbcrIbTpqZPcMHgWjcymqSrG1kVaut39
access_token_secret = ''#example : QovqxQnw0hSPrKwFIYLWct3Zv4MeGMash66IaOoFyXNWs

######################################################################
#Creat a handler for the streaming data that stays open...
######################################################################

class StdOutListener(tweepy.StreamListener):

    #Handler
    ''' Handles data received from the stream. '''

    ######################################################################
    #For each status event
    ######################################################################

    def on_status(self, status):

        # Prints the text of the tweet
        print '%d,%d,%d,%s,%s' % (status.user.followers_count, status.user.friends_count,status.user.statuses_count, status.user.id_str, status.user.screen_name)

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

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    stream = tweepy.Stream(auth, listener)

    ######################################################################
    #Sample dilivers a stream of 1% (random selection) of all tweets
    ######################################################################

    stream.sample()

    ######################################################################
    #Custom Filter rules pull all traffic for those filters in real time.
    #Bellow are some examples add or remove as needed...
    ######################################################################
    #A Good demo stream of reasonable amount
    #stream.filter(track=['actian', 'BigData', 'Hadoop', 'Predictive', 'Quantum', 'bigdata', 'Analytics', 'IoT'])
    #Hadoop Summit following
    #stream.filter(track=['actian', 'hadoop', 'hadoopsummit'])

