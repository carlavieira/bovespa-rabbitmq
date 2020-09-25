from datetime import datetime
from stock.emit_stock import EmitStock

class Transaction():
    """
    classe responsável gerar a mensagem de transação pela EmmitStock e por armazenar as transações realizadas
    """
    transactions = []

    @staticmethod
    def store_transaction(host, asset, amount, value, broker_sale, broker_purchase):
        """
        método responsável armazenar uma nova transação realizada e instanciar a mensagem de transação pela EmmitStock
        """    
        now = datetime.now()

        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        transaction = {
            "datetime": dt_string,
            "asset": asset,
            "amount": amount,
            "value": value,
            "broker_sale": broker_sale,
            "broker_purchase": broker_purchase
        }

        Transaction.transactions.append(transaction)

        transaction_routing_key = "transacao." + transaction["asset"].lower()
        transaction_message = transaction["datetime"] + "; " + transaction["broker_sale"] + "; " + transaction["broker_purchase"] + "; " + transaction["amount"] + "; " + transaction["value"]

        emit_stock =  EmitStock(host=host, routing_key=transaction_routing_key, message=transaction_message)
        emit_stock.start()