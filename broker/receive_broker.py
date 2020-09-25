
#!/usr/bin/env python
import pika
import sys
import os
import threading


class ReceiveBroker(threading.Thread):

    def __init__(self, host, binding_keys=["#"]):
        threading.Thread.__init__(self)
        self.host = host
        self.binding_keys = binding_keys

    def run(self):

        try:
            # Establishes connection with Rabbit MQ
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=self.host))
            channel = connection.channel()

            # Creates (if it doesn't already exist) a exchange named 'BOLSADEVALORES' and with the type 'topic'
            channel.exchange_declare(
                exchange='BOLSADEVALORES', exchange_type='topic')

            # Creates a new queue with a randon name which will be deleted at the end of the connection
            result = channel.queue_declare(queue='', exclusive=True)

            # Gets the queue name
            queue_name = result.method.queue

            # For each binding key given, a bind is created between the exchange 'BOLSADEVALORES' and the new queue created with the binding key definitions given
            for binding_key in self.binding_keys:
                channel.queue_bind(
                    exchange='BOLSADEVALORES', queue=queue_name, routing_key=binding_key)

            #print(' [*] Waiting for logs. To exit press CTRL+C')

            # Defines the callback message that will be invoked inside basic_consumer to print the message when a new message is received
            def callback(ch, method, properties, body):
                topics = method.routing_key.split(".")
                data_menssage = body.decode().split("; ")
                if topics[0] == "transacao":
                    messageFormat = "Transação - Ativo: "+ topics[1].upper() + " Data-hora: " + data_menssage[0] + " Corretora-Compra: " + data_menssage[1] + " Corretora-Venda: " + data_menssage[2] + " Quantidade: " + data_menssage[3] + " Valor: " + data_menssage[4] + '\n'
                if topics[0] == "compra" or topics[0] == "venda":
                    messageFormat = topics[0].capitalize() +" - Ativo: "+ topics[1].upper() + " Quantidade: " + data_menssage[0] + " Valor: " + data_menssage[1] + " Corretora: " + data_menssage[2] + '\n'
                print(messageFormat)

            # Creates a new consumer to receive messages from the queue previously created
            channel.basic_consume(
                queue=queue_name, on_message_callback=callback, auto_ack=True)

            # Waits to receive messages until there is an interruption
            channel.start_consuming()

        except KeyboardInterrupt:
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)
