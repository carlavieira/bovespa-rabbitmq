from stock.emit_stock import EmitStock
from stock.receive_stock import ReceiveStock

def main():
   emit_stock =  EmitStock(host='localhost', routing_key="compra.petr2", message="100; 26,46; BKR1")
   emit_stock.run()

   emit_stock =  EmitStock(host='localhost', routing_key="transacao.petr2", message="25/08/2020; BKR1; BKR1; 100; 26,46")
   emit_stock.run()

if __name__ == "__main__":
    main()