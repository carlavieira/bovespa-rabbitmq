#!/usr/bin/env python
#!/usr/bin/env python
import pika
import sys

def main():

    # Establishes connection with Rabbit MQ
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # Creates (if it doesn't already exist) a exchange named 'topic_assets' and with the type 'topic'
    channel.exchange_declare(exchange='topic_assets', exchange_type='topic')

    # Gets the routing key from args
    routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'

    # Gets the message from args
    message = ' '.join(sys.argv[2:]) or 'Hello World!'

    # Sends message with the routing key to the exchange named 'topic_assets'
    channel.basic_publish(
        exchange='topic_assets', routing_key=routing_key, body=message)
    print(" [x] Sent %r:%r" % (routing_key, message))

    # Terminate connection
    connection.close()

if __name__ == '__main__':
        main()