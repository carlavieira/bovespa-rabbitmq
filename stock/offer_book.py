from stock.transaction import Transaction

class OfferBook():
    """
    classe responsável armazenar as ofertas de compra e venda realizadas e efetuar a lógica de negócio para conferir correspondências entre ofertas de compra e venda para realizar uma transação.
    """
    purchases_offers = []
    sales_offers = []

    @staticmethod
    def store_offer(host, routing_key, menssage):
        """
        método responsável por armazenar as ofertas de compra e venda realizadas.
        """
        topics = routing_key.split(".")
        data_menssage = menssage.split("; ")

        offer = {}
        offer["asset"] = topics[1]
        offer["amount"] = data_menssage[0]
        offer["value"] = data_menssage[1]
        offer["broker"] = data_menssage[2]
        
        if topics[0] == "venda":
            offer["id"] = len(OfferBook.sales_offers)
            OfferBook.sales_offers.append(offer)
        if topics[0] == "compra":
            offer["id"] = len(OfferBook.purchases_offers)
            OfferBook.purchases_offers.append(offer)

        OfferBook.check_offers(host=host, topics=topics, offer=offer)
    
    @staticmethod
    def check_offers(host, topics, offer):
        """
        método responsável por efetuar a lógica de negócio para conferir correspondências entre ofertas de compra e venda para realizar uma transação.
        """
        if topics[0] == "compra":

            purchase_value = float(offer["value"])

            for sale_offer in OfferBook.sales_offers:

                if sale_offer["asset"] == offer["asset"]:

                    sale_value = float(sale_offer["value"])

                    if purchase_value >= sale_value:

                        purchase_amount = int(offer["amount"])
                        sale_amount = int(sale_offer["amount"])

                        if sale_amount > purchase_amount:

                            Transaction.store_transaction(host=host, asset=offer["asset"], amount=offer["amount"], value=offer["value"], broker_purchase=offer["broker"], broker_sale=sale_offer["broker"])

                            sale_offer["amount"] = str(sale_amount - purchase_amount)
                            OfferBook.purchases_offers.remove(offer)
                            OfferBook.print_book()
                            return
                        
                        if sale_amount < purchase_amount:

                            Transaction.store_transaction(host=host, asset=offer["asset"], amount=sale_offer["amount"], value=offer["value"], broker_purchase=offer["broker"], broker_sale=sale_offer["broker"])

                            index_offer = OfferBook.purchases_offers.index(offer)
                            offer["amount"] = str(purchase_amount - sale_amount)
                            OfferBook.sales_offers.remove(sale_offer)
                            OfferBook.purchases_offers[index_offer] = offer
                            OfferBook.print_book()

                        if sale_amount == purchase_amount:

                            Transaction.store_transaction(host=host, asset=offer["asset"], amount=offer["amount"], value=offer["value"], broker_purchase=offer["broker"], broker_sale=sale_offer["broker"])

                            OfferBook.purchases_offers.remove(offer)
                            OfferBook.sales_offers.remove(sale_offer)
                            return

        if topics[0] == "venda":

            sale_value = float(offer["value"])

            for purchase_offer in OfferBook.purchases_offers:

                if purchase_offer["asset"] == offer["asset"]:

                    purchase_value = float(purchase_offer["value"])

                    if sale_value >= purchase_value:

                        sale_amount = int(offer["amount"])
                        purchase_amount = int(purchase_offer["amount"])

                        if purchase_amount > sale_amount:

                            Transaction.store_transaction(host=host, asset=offer["asset"], amount=offer["amount"], value=purchase_offer["value"], broker_purchase=purchase_offer["broker"], broker_sale=offer["broker"])

                            purchase_offer["amount"] = str(purchase_amount - sale_amount)
                            OfferBook.sales_offers.remove(offer)
                            OfferBook.print_book()
                            return
                        
                        if purchase_amount < sale_amount:

                            Transaction.store_transaction(host=host, asset=offer["asset"], amount=purchase_offer["amount"], value=purchase_offer["value"], broker_purchase=purchase_offer["broker"], broker_sale=offer["broker"])

                            index_offer = OfferBook.sales_offers.index(offer)
                            offer["amount"] = str(sale_amount - purchase_amount)
                            OfferBook.purchases_offers.remove(purchase_offer)
                            OfferBook.sales_offers[index_offer] = offer
                            OfferBook.print_book()

                        if purchase_amount == sale_amount:

                            Transaction.store_transaction(host=host, asset=offer["asset"], amount=offer["amount"], value=purchase_offer["value"], broker_purchase=purchase_offer["broker"], broker_sale=offer["broker"])

                            OfferBook.sales_offers.remove(offer)
                            OfferBook.purchases_offers.remove(purchase_offer)
                            return

    @staticmethod
    def print_book():
        print("purchases_offers: ")
        for offer in OfferBook.purchases_offers:
            print("ID: "+str(offer["id"]) + " Amount: "+offer["amount"]+" Value: "+ offer["value"]+" Broaker: "+offer["broker"])
        print("sales_offers: ")
        for offer in OfferBook.sales_offers:
            print("ID: "+str(offer["id"]) + " Amount: "+offer["amount"]+" Value: "+ offer["value"]+" Broaker: "+offer["broker"])
