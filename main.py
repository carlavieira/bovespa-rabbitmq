from broker.emit_broker import EmitBroker
from broker.receive_broker import ReceiveBroker

def main():
   emit_broker =  EmitBroker(host='localhost', routing_key="compra.petr2", message="<100; 26,46; BKR1>")
   emit_broker.publish()

   receive_brocker = ReceiveBroker(host='localhost', binding_keys="*.petr2")
   receive_brocker.consume()

if __name__ == "__main__":
    main()