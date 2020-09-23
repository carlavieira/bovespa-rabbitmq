from datetime import datetime

class Transaction():

    transactions = []

    @staticmethod
    def store_transaction(host=host, asset=asset, amount=amount, value=value, broker_sale=broker_sale, broker_purchase=broker_purchase):
        
        now = datetime.now()

        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        transaction = {
            "datetime"; dt_string,
            "asset": asset,
            "amount": amount,
            "value": value,
            "broker_sale": broker_sale,
            "broker_purchase": broker_purchase
        }

        Transaction.transactions.append(transaction)

        transaction_routing_key = "transacao." + transaction["asset"].lower()
        transaction_message = transaction["datetime"] + "; " + transaction["broker_sale"] + "; " + transaction["broker_purchase"] + "; " transaction["amount"] + "; " + transaction["value"]

        emit_stock =  EmitStock(host=host, routing_key=transaction_routing_key, message=transaction_message)
        emit_stock.start()