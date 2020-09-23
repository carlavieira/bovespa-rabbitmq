from stock.emit_stock import EmitStock
from stock.receive_stock import ReceiveStock

def main():
   receive_stock = ReceiveStock(host='localhost')
   receive_stock.start()

if __name__ == "__main__":
    main()