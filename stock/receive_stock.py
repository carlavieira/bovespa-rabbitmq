
#!/usr/bin/env python
import pika, sys, os

class ReceiveStock():

    def __init__(self, host, binding_keys):
        self.host = host
        self.binding_keys = binding_keys

    def consume(self):

        try:
            # Establishes connection with Rabbit MQ
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=self.host))
            channel = connection.channel()

            # Creates (if it doesn't already exist) a exchange named 'BROKER' and with the type 'topic'
            channel.exchange_declare(
                exchange='BROKER', exchange_type='topic')

            # Creates a new queue with a randon name which will be deleted at the end of the connection
            result = channel.queue_declare(queue='', exclusive=True)

            # Gets the queue name
            queue_name = result.method.queue

            # For each binding key given, a bind is created between the exchange 'BROKER' and the new queue created with the binding key definitions given
            for binding_key in self.binding_keys:
                channel.queue_bind(
                    exchange='BROKER', queue=queue_name, routing_key=binding_key)

            print(' [*] Waiting for logs. To exit press CTRL+C')

            # Defines the callback message that will be invoked inside basic_consumer to print the message when a new message is received
            def callback(ch, method, properties, body):
                print(" [x] %r:%r" % (method.routing_key, body.decode()))

            # Creates a new consumer to receive messages from the queue previously created
            channel.basic_consume(
                queue=queue_name, on_message_callback=callback, auto_ack=True)

            # Waits to receive messages until there is an interruption
            channel.start_consuming()

        except KeyboardInterrupt:
            print('Interrupted')
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)
