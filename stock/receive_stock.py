
#!/usr/bin/env python
import pika, sys, os, threading

from stock.emit_stock import EmitStock
from stock.offer_book import OfferBook

class ReceiveStock(threading.Thread):

    def __init__(self, host):
        threading.Thread.__init__(self)
        self.host = host

    def run(self):

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

            # A bind is created between the exchange 'BROKER' and the new queue created for all topics
            channel.queue_bind(exchange='BROKER', queue=queue_name, routing_key="#")

            # [OTAVIO] Colocar aqui código de mandar a menssagem "Negociações iniciadas" na interface StockGUI
            print(' [*] Waiting for logs. To exit press CTRL+C')

            # Defines the callback message that will be invoked inside basic_consumer to print the message when a new message is received
            def callback(ch, method, properties, body):
                topics = method.routing_key.split(".")
                data_menssage = body.decode().split("; ")

                if topics[0] == "transacao":
                    messageFormat = "Transação - Ativo: "+ topics[1].upper() + " Data-hora: " + data_menssage[0] + " Corretora-Compra: " + data_menssage[1] + " Corretora-Venda: " + data_menssage[2] + " Quantidade: " + data_menssage[3] + " Valor: " + data_menssage[4]
                if topics[0] == "compra" or topics[0] == "venda":
                    messageFormat = topics[0].capitalize() +" - Ativo: "+ topics[1].upper() + " Quantidade: " + data_menssage[0] + " Valor: " + data_menssage[1] + " Corretora: " + data_menssage[2]
                
                # [OTAVIO] Colocar aqui código para passar o messageFormat para a interface StockGUI
                print(messageFormat)

                emit_stock =  EmitStock(host=self.host, routing_key=method.routing_key, message=body.decode())
                emit_stock.start()

                OfferBook.store_offer(self.host, method.routing_key, body.decode());

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
