from broker.emit_broker import EmitBroker
from broker.receive_broker import ReceiveBroker

def main():

   receive_brocker = ReceiveBroker(host='localhost', binding_keys="#")
   receive_brocker.consume()

if __name__ == "__main__":
    main()