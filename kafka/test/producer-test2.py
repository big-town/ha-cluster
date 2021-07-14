#!/usr/bin/python3

import sys
import random
import logging

r = random.randint(0, 1000)
from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(acks='all', bootstrap_servers=['10.101.10.51:9092','10.101.10.52:9092','10.101.10.53:9092'])
#producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'])
# Asynchronous by default
#future = producer.send('events', b'raw_bytes'+str.encode(sys.argv[1]))
#producer.send('events', b'--------------------')
for x in range(r,r+10):
    #future = producer.send('events', bytes([131, 100, 0, 3, 110, 105, 108]))
    future = producer.send('test2', key=b'foo'+str.encode(str(x)), value=b'bar'+str.encode(str(x)))
    print(x)

# Block for 'synchronous' sends
try:
    record_metadata = future.get(timeout=10)
except KafkaError:
    # Decide what to do if produce request failed...
    print("huiny kakaeto")
    pass

# Successful result returns assigned partition and offset
print (record_metadata.topic)
print (record_metadata.partition)
print (record_metadata.offset)
