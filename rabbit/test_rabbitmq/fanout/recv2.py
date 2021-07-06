#!/usr/bin/env python3
import pika, sys, os

def main():
    parameters = pika.URLParameters('amqp://test:123456@10.103.10.49:5672/')
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    #channel.queue_declare(queue='hello')

    def on_message(ch, method, properties, body):
        print(" [x] Received %r" % body.decode())

#    channel.basic_consume(queue='xt_in', callback, auto_ack=True)
    channel.basic_consume(on_message, 'test_qf2', True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)