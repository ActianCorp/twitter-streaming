To begin generating data:
1. First open twitterStream.py and add in the needed credentials for your twitter dev account.
2. Then test by open terminal then cd into the directory with the python script and run:


### Replace the generic paths with the path in your configuration. 


>> python twitterstreaming.py



3. to deliver the stream to kafka run:


>> python /path/to/twitterStream.py > pipe | path/to/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic twitterstream < pipe


that will begin to stream data events into a kafka producer.



