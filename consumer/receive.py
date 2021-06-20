#!/usr/bin/env python
import pika, sys, os
import json
from mongo_interact import insert_into

HOST = 'mongodbhost'

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmqhost'))
    channel = connection.channel()

    channel.queue_declare(queue='products')

    def callback(ch, method, properties, body):
        product = json.loads(body)        
        print(" [x] Received %r" % product)
        insert_into(HOST, product)

    channel.basic_consume(queue='products', on_message_callback=callback, auto_ack=True)

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
            
