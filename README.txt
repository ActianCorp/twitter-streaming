________         _______________            ____________                               
___  __/__      ____(_)_  /__  /______________  ___/_  /__________________ _______ ___ 
__  /  __ | /| / /_  /_  __/  __/  _ \_  ___/____ \_  __/_  ___/  _ \  __ `/_  __ `__ \
_  /   __ |/ |/ /_  / / /_ / /_ /  __/  /   ____/ // /_ _  /   /  __/ /_/ /_  / / / / /
/_/    ____/|__/ /_/  \__/ \__/ \___//_/    /____/ \__/ /_/    \___/\__,_/ /_/ /_/ /_/ 
                                                                                       

###########################################
### twitterStream Data Ingest version 1.0 
###########################################

To begin generating data:

1. First open twitterStream.py and add in the needed credentials for your twitter dev account.
	* http://dev.twitter.com
2. Then test by open terminal then cd into the directory with the python script and run:



### Replace the generic paths with the path in your configuration. 


>> python /path/to/twitterstreaming.py



3. to deliver the stream to kafka run:


>> python /path/to/twitterStream.py > pipe | path/to/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic twitterstream < pipe


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
