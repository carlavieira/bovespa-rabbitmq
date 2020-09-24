#!/usr/bin/env python
import pika
import sys
import threading


class EmitStock(threading.Thread):

    def __init__(self, host, routing_key, message):
        threading.Thread.__init__(self)
        self.host = host
        self.routing_key = routing_key
        self.message = message

    def run(self):
        # Establishes connection with Rabbit MQ
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.host))
        channel = connection.channel()

        # Creates (if it doesn't already exist) a exchange named 'BOLSADEVALORES' and with the type 'topic'
        channel.exchange_declare(exchange='BOLSADEVALORES', exchange_type='topic')

        # Sends message with the routing key to the exchange named 'BOLSADEVALORES'
        channel.basic_publish(
            exchange='BOLSADEVALORES', routing_key=self.routing_key, body=self.message)
        #print(" [x] Sent %r:%r" % (self.routing_key, self.message))

        # Terminate connection
        connection.close()