To begin generating data open terminal then cd into the directory with the python script and run 


>> python twitterstreaming.py



to deliver the stream to kafka run:


>> python /path/to/twitterStream.py > pipe | path/to/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic twitterstream < pipe


that will begin to stream data events into a kafka producer.



