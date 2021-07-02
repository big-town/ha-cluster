#!/usr/bin/python3

import random

r = random.randint(0, 1000)
from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(bootstrap_servers=['10.101.10.51:9092','10.101.10.52:9092','10.101.10.53:9092'])
for x in range(r,r+10):
    future = producer.send('events', key=b'key_message', value=b'value message')
    print(x)

try:
    record_metadata = future.get(timeout=10)
except KafkaError:
    print("Error send!")

print (record_metadata.topic)
print (record_metadata.partition)
print (record_metadata.offset)
