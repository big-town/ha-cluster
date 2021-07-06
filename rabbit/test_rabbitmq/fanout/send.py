#!/usr/bin/env python3
import pika
import time

parameters = pika.URLParameters('amqp://test:123456@10.103.10.49:5672/')

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

for i in range(10):
    channel.basic_publish(exchange='test_ef', routing_key='ssdfsdfdf', body='Hello World! - fanout ' + str(i))
    print(" [x] Sent 'Hello World!'")
connection.close()
