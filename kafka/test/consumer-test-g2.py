#!/usr/bin/python3
from kafka import KafkaConsumer

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('test',group_id="test-gr2",
                         bootstrap_servers=['10.101.10.51:9092','10.101.10.52:9092','10.101.10.53:9092'],
                         auto_offset_reset='earliest')
                         #consumer_timeout_ms=1000)
for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))
