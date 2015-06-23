________         _______________            ____________                               
___  __/__      ____(_)_  /__  /______________  ___/_  /__________________ _______ ___ 
__  /  __ | /| / /_  /_  __/  __/  _ \_  ___/____ \_  __/_  ___/  _ \  __ `/_  __ `__ \
_  /   __ |/ |/ /_  / / /_ / /_ /  __/  /   ____/ // /_ _  /   /  __/ /_/ /_  / / / / /
/_/    ____/|__/ /_/  \__/ \__/ \___//_/    /____/ \__/ /_/    \___/\__,_/ /_/ /_/ /_/ 
                                                                                       

###########################################
### twitterStream Data Ingest version 1.0 
###########################################

To begin generating data:

1. First open twitter_kafka_direct and add in the needed credentials for your twitter dev account.
	* http://dev.twitter.com
2. Ensure you have all requirements installed and that python can access the modules (see requirements.txt) . 
	- if you need for example tweepy and have pip :
		>> pip install tweepy
	- if you don't have pip download get_pip.py (latest from the google webs :) and run:
		>> python get_pip.py 
		>> pip install tweepy
	- if you like you can also track tweepy down and install it manually but I don't see why when pip is so awesome. 


3. Then test by opening a terminal window then cd into the directory with the python script and run:

### Replace the generic paths with the path in your configuration. 
		>> python /path/to/twitter_kafka_direct.py

4. to deliver the stream to csv:
	- replace stubs with values for your tokens in twitterStream.py 

		>> python /path/to/twitterStream.py > twitterData.csv

5. to write data to kafka:
	- Use twitter_kafka_direct.py. Replace token stubs with your values and state your topic mytopic
	  default is 'topic'

	 	>> python /path/to/twitter_kafka_direct.py


that will begin to stream data events into a kafka producer.

###########################################
*** Note ***

this procedure assumes a topic named twitterstream exists in kafka to produce the data to.
if you need to create a topic use the following code :

>> bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic twitterstream

check what topics you have with:
>> bin/kafka-topics.sh --list --zookeeper localhost:2181

to check if data is in fact landing in kafka:
>> bin/kafka-console-consumer.sh --zookeeper localhost:2181 --topic twitterstream --from-beginning 

###########################################
