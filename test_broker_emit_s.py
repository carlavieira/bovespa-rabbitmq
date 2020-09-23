from broker.emit_broker import EmitBroker
from broker.receive_broker import ReceiveBroker

def main():
   emit_broker =  EmitBroker(host='localhost', routing_key="venda.petr2", message="150; 26.46; BKR1")
   emit_broker.start()

   # emit_broker =  EmitBroker(host='localhost', routing_key="compra.petr2", message="150; 26.46; BKR1")
   # emit_broker.start()

if __name__ == "__main__":
    main()